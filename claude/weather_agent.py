import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city to get weather for",
                }
            },
            "required": ["city"],
        },
    }
]

#this would pull from a database or API etc in a real app
def run_tool(name, tool_input):
    if name == "get_weather":
        return f"Weather in {tool_input['city']}: 95F, sunny"
    raise ValueError(f"Unknown tool: {name}")

#in a real app you would recieve a message que from some front end?
messages = [
    {"role": "user",
     "content": "What should I wear in Austin today?"}
]

#AGENT LOOP
#send/recieve a message from claude
#if the message is "end turn" it's done and post result
#otheriwse use the tool, get a new response resend that to claude
#loop that unitl done

while True:
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

    if response.stop_reason == "end_turn":
        for block in response.content:
            if block.type == "text":
                print(block.text)
        break

    #if claude wants to use a tool, run the tool
    #then get a new response from claude with the tool return
    elif response.stop_reason == "tool_use":
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = run_tool(block.name, block.input)
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    }
                )

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})

    #any other stop reason (e.g. max_tokens) would loop forever, so stop here
    else:
        print(f"Stopped unexpectedly: {response.stop_reason}")
        break
                         