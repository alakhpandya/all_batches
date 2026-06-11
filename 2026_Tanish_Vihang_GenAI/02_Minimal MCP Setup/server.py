# server.py
import sys
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("Currency-Converter-Service")

@mcp.tool()
def get_exchange_rate(base_currency: str, target_currency: str) -> str:
    """
    Fetches the current exchange rate between two currencies.
    Use this tool whenever the user asks about currency values or conversions.
    """
    # Hardcoded simulation for training purposes
    rates = {
        ("USD", "EUR"): 0.92,
        ("EUR", "USD"): 1.09,
        ("USD", "GBP"): 0.78
    }
    
    pair = (base_currency.upper(), target_currency.upper())
    rate = rates.get(pair, 1.0)
    return f"The current exchange rate for {pair[0]} to {pair[1]} is {rate}."


@mcp.tool()
def time_zone_converter(source: str, destination: str) -> str:
    """
    Takes two locations and return the time to be added to the time at source to get time of destination location.
    """
    time_adj = {
        ("IST", "EST"): -8.5,
        ("GMT", "IST"): 5.5
    }
    pair = (source.upper(), destination.upper())
    adjustment = time_adj[pair]
    return f"The current exchange rate for {pair[0]} to {pair[1]} is {adjustment}."

if __name__ == "__main__":
    # MCP servers use standard input/output (stdio) to communicate with clients locally
    mcp.run(transport="stdio")