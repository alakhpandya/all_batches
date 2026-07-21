from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("File System Server")

WORKSPACE = Path("workspace").resolve()

# print("Actual path:", WORKSPACE)

# ------------------ "Safe" Path Function ------------------
def get_safe_path(filename: str) -> Path:

    file_path = (WORKSPACE / filename).resolve()
    # print("File path =", file_path)
    
    if WORKSPACE not in file_path.parents and file_path.parents != WORKSPACE:
        # print("Access Denied.")
        raise ValueError("Access Denied: Unauthorized Access.")

    return file_path

# file_path = get_safe_path("C:\\Users\\alakh\\Desktop\\all_batches\\24_DS_Gen_Ahm_1\\12_GenAI\\04 MCP Architecture\\03_File_System_MCP_Server\\workspace\\ai_notes.txt")

# file_path = get_safe_path("C:\\Users\\alakh\\Desktop\\all_batches\\24_DS_Gen_Ahm_1\\11_MLOps\\gen24_flask_demo_app_key.pem")

# print(file_path)
# This is called Path Traversal Protection

# ------------------ Tool-1: List all the files ------------------

@mcp.tool()
def list_files() -> list[str]:
    """
    List all the files available in the workspace.
    """
    files = []
    
    # print("RGlob:", WORKSPACE.rglob("*"))
    # for i in WORKSPACE.rglob("*"):
    #     print(i)
    for path in WORKSPACE.rglob("*"):
        # print(path)
        if path.is_file():
            relative_path = path.relative_to(WORKSPACE)
            # print("Relative Path =", relative_path)
            
            files.append(str(relative_path))

    return files


# print("All files =", list_files())


# ------------------ Tool-2: Read a specific file ------------------
@mcp.tool()
def read_file(filename: str) -> str:
    """
    Reads the complete content of the file from the workspace.
    """

    file_path = get_safe_path(filename)

    if not file_path.exists():
        return "File not found."
    
    if not file_path.is_file():
        return "The path is not a file."
    
    return file_path.read_text(
        encoding= "utf-8"
    )

# ------------------ Tool-3: Search Tool ------------------
@mcp.tool()
def search_files(query: str) -> list[dict]:
    """
    Search for the "query" across all the .txt files in the workspace.
    """

    result = []
    
    for path in WORKSPACE.rglob("*"):

        if path.is_file():

            content = path.read_text(
                encoding= "utf-8"
            )

            if query.lower() in content.lower():
                result.append(
                    {
                        "file" : str(path.relative_to(WORKSPACE)),
                        "matched" : True
                    }
                )

    return result

# ------------------ Tool-4: Get File Info ------------------
@mcp.tool()
def get_file_info(filename: str) -> dict:
    """
    Gets information about a file in the workspace.
    """
    file_path = get_safe_path(filename)

    if not file_path.exists():
        return {
            "error" : "File not found"
        }
    
    if not file_path.is_file():
        return {
            "error" : "The path is not a file"
        }
    
    return {
        "name" : file_path.name,

        "size_bytes" : file_path.stat().st_size,

        "extension" : file_path.suffix,

        "relative_path" : str(file_path.relative_to(WORKSPACE))
    }

# ------------------ Resources ------------------

@mcp.resource(
        "workspace://files/{filename}"
)
def get_file_resource(filename: str) -> str:
    """
    Reads the file from the workspace as an MCP Resource
    """
    file_path = get_safe_path(filename)

    if not file_path.exists():
        return "File not found."
    
    if not file_path.is_file():
        return "The path is not a file."
    
    return file_path.read_text(
        encoding= "utf-8"
    )


# ------------------ Running the server ------------------
if __name__ == "__main__":
    mcp.run()