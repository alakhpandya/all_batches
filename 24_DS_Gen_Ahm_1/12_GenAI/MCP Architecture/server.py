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


if __name__ == "__main__":
    print("The MCP Server is running now...")
    # MCP servers use standard input/output (stdio) to communicate with clients locally
    mcp.run(transport= "stdio")