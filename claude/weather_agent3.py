import anthropic
from anthropic import beta_tool

client = anthropic.Anthropic()

#fake data, in a real app these would call a weather API
def fetch_weather(city):
    return f"Weather in {city}: 72F, partly cloudy"

def fetch_forecast(city):
    return f"Forecast for {city}: 65F with afternoon showers tomorrow, 45F and snow flurries the day after"

# Wrap the same two lookups we ran by hand. @beta_tool builds each tool's
# schema from the function signature and its descriptions from the docstring
@beta_tool
def get_weather(city: str) -> str:
    """Get today's current weather for a city.

    Args:
        city: The city to check
    """
    return fetch_weather(city)

@beta_tool
def get_forecast(city: str) -> str:
    """Get the weather forecast for the next few days for a city.

    Args:
        city: The city to check
    """
    return fetch_forecast(city)

runner = client.beta.messages.tool_runner(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "I'm packing for a three-day trip to Denver. What's the weather today and over the next few days?",
        }
    ],
    tools=[get_weather, get_forecast],
)

# Run the loop to get the final message after all the tool ping-pong has settled
final_message = runner.until_done()

for block in final_message.content:
    if block.type == "text":
        print(block.text)
