import sys
from mcp.server.fastmcp import FastMCP

# Initializing the MCP Server
mcp = FastMCP("Currency-Converter-Service")

@mcp.tool()
def get_exchange_rate(base_currency: str, target_currency: str) -> str:
    """
    Fetches the currency exchange rates between two currencies.
    Use this tool whenever the user asks about currency values or conversion.
    """
    # For learning purpose, we will hardcode the currency exchange rates
    rates = {
        ("USD", "EUR") : 0.92,
        ("EUR", "USD") : 1.09,
        ("USD", "INR") : 90.5,
        ("INR", "USD") : 0.011
    }
    pair = (base_currency.upper(), target_currency.upper())
    rate = rates.get(pair, 1.0)
    return f"The exchange rate for {pair[0]} to {pair[1]} is: {rate}"

@mcp.tool()
def time_zone_converter(source: str, destination: str) -> str:
    """
    Takes time zone names of two locations (eg - IST and GMT) and returns string with needed adjustment
    """
    time_adj = {
        ("IST", "GMT") : -5.5,
        ("GMT", "IST") : 5.5,
        ("IST", "EST") : -8.5
    }
    pair = (source.upper(), destination.upper())
    adjustment = time_adj[pair]
    return f"To convert {source.upper()} to {destination.upper()} add {adjustment} to {source.upper()}"

if __name__ == "__main__":
    print("The MCP Server is running now...")
    # MCP servers use standard input/output (stdio) to communicate with clients locally
    mcp.run(transport= "stdio")