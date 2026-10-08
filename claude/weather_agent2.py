import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "name": "get_weather",
        "description": "Get today's current weather for a city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "The city to check"}
            },
            "required": ["city"],
        },
    },
    {
        "name": "get_forecast",
        "description": "Get the weather forecast for the next few days for a city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "The city to check"}
            },
            "required": ["city"],
        },
    },
]

#fake data, in a real app these would call a weather API
def get_weather(city):
    return f"Weather in {city}: 95F, sunny"

def get_forecast(city):
    return f"Forecast for {city}: 97F sunny tomorrow, 88F with storms the day after"

def run_tool(name, tool_input):
    if name == "get_weather":
        return get_weather(tool_input["city"])
    if name == "get_forecast":
        return get_forecast(tool_input["city"])
    raise ValueError(f"Unknown tool: {name}")

messages = [
    {"role": "user",
     "content": "What should I wear in Austin today, and should I plan anything outdoors this week?"}
]

while True:
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        messages=messages,
        tools=tools,
    )

    if response.stop_reason != "tool_use":
        # Claude is done — this is the final answer
        break

    messages.append({"role": "assistant", "content": response.content})

    tool_results = [
        {
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": run_tool(block.name, block.input),
        }
        for block in response.content
        if block.type == "tool_use"
    ]

    messages.append({"role": "user", "content": tool_results})

for block in response.content:
    if block.type == "text":
        print(block.text)
