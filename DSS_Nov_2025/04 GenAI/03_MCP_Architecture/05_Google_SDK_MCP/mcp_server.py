from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP Server")

@mcp.tool()
def get_exchange_rate(base_currency: str, target_currency: str) -> str:
    """
    Fetches the currency exchange rate between two currencies.
    """

    rates = {
        ("USD", "INR") : 90,
        ("INR", "USD") : 0.011,
        ("USD", "EUR") : 0.92,
        ("EUR", "USD") : 1.09
    }

    pair = (base_currency.upper(), target_currency.upper())
    rate = rates[pair]

    return f"The exchange rate for {base_currency.upper()} to {target_currency.upper()} conversion is: {rate}"

@mcp.tool()
def time_zone_converter(source: str, destination:str) -> str:
    """
    Takes time zone names of two locations (eg IST, GMT) and returns a string including the needed adjustment.
    """

    time_adj = {
        ("IST", "GMT") : -5.5,
        ("GMT", "IST") : +5.5,
        ("IST", "EST") : -8.5
    }

    pair = (source.upper(), destination.upper())
    adjustment = time_adj[pair]

    return f"To convert {source.upper()} time into {destination.upper()} time, add {adjustment} hours into {source.upper()} time"


if __name__ == "__main__":
    mcp.run()
    # mcp.run(transport= "stdio")