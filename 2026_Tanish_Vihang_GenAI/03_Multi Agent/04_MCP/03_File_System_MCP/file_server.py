from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("File System Server")

WORKSPACE = Path("workspace").resolve()

# print("Actual Path:", WORKSPACE)

# ----------------------------- Guard rails to getting "safe" path -----------------------------

def get_safe_path(file_name: str) -> Path:

    file_path = (WORKSPACE / file_name).resolve()

    # print("file_path:", file_path)

    # print("file_path.parent:", file_path.parent)
    
    # print("file_path.parents:", file_path.parents)
    # for i in file_path.parents:
    #     print(i)

    if file_path.parent != WORKSPACE and WORKSPACE not in file_path.parents:
        # print("Access Denied")
        # return False
        raise ValueError("Access Denied: Unauthorized Access")

    return file_path


# file_path = get_safe_path("ai_notes.txt")
# file_path = get_safe_path("legal/privacy_policy.txt")

# file_path = get_safe_path("C:\\Users\\alakh\\Desktop\\all_batches\\2026_Tanish_Vihang_GenAI\\03_Multi Agent\\03_RAG\\gk-book.pdf")

# file_path = get_safe_path("C:\\Users\\alakh\\Desktop\\all_batches\\2026_Tanish_Vihang_GenAI\\03_Multi Agent\\04_MCP\\03_File_System_MCP\\no_access.txt")

# file_path = get_safe_path("C:\\Users\\alakh\\Desktop\\all_batches\\2026_Tanish_Vihang_GenAI\\03_Multi Agent\\04_MCP\\03_File_System_MCP\\workspace\\ai_notes.txt")

# print(file_path)

# This is known as Path Traversal Protection

# ----------------------------- Tool-1: Listing all files in the WORKSPACE -----------------------------

@mcp.tool()
def list_files() -> list[str]:
    """Lists all the files availble in the workspace"""

    files = []

    # print("Rglob object:", WORKSPACE.rglob("*"))

    # print("Rglob:")
    for path in WORKSPACE.rglob("*"):
        # print(path)
        if path.is_file():
            relative_path = path.relative_to(WORKSPACE)
            # print(relative_path)
            files.append(relative_path)

    return files


# print(list_files())

# ----------------------- Tool-2: Reading a specific file from the WORKSPACE -----------------------

@mcp.tool()
def read_file(file_name: str) -> str:
    """Reads the complete content of the file from the WORKSPACE"""

    file_path = get_safe_path(file_name)
    # print("file_path:", file_path)
    # print("file_path Type:", type(file_path))

    if not file_path.exists():
        # print("File not found")
        return "File not found"

    if not file_path.is_file():
        # print("The path is not a file")    
        return "The path is not a file"

    return file_path.read_text(encoding= "utf-8")

# read_file("ai_notes.txt")
# read_file("advanced_ai_notes.txt")
# read_file("legal")

# print(read_file("ai_notes.txt"))

# ----------------------- Tool-3: Search Tool -----------------------

@mcp.tool()
def search_files(query: str) -> list[dict]:
    """Searches for the "query" across all the .txt files present in the workspace"""

    result = []

    for path in WORKSPACE.rglob("*"):
        # print(path)
        if path.is_file():

            content = path.read_text()

            if query.lower() in content.lower():

                result.append(
                    {
                        "file" : str(path.relative_to(WORKSPACE)),
                        "matched" : True
                    }
                )

    return result

# print(search_files("Language"))

# ----------------------- Tool-4: Get file info -----------------------
@mcp.tool()
def get_file_info(filename: str) -> dict:
    """Get information of a particular file in the workspace"""

    file_path = get_safe_path(filename)

    if not file_path.exists():
        return {
            "error": "File not found"
        }

    if not file_path.is_file():
        return {
            "error": "The path is not a file"
        }

    return {
        "name" : file_path.name,

        "size_bytes" : file_path.stat().st_size,

        "extension" : file_path.suffix,

        "relative_path" : str(file_path.relative_to(WORKSPACE))
    }


# print(get_file_info("legal/privacy_policy.txt"))

# ----------------------- Resource-1: Read from a file -----------------------

@mcp.resource(
        "workspace://files/{file_name}"
)
def get_file_resource(file_name: str) -> str:
    """Reads a file from the WORKSPACE as an MCP resource"""

    file_path = get_safe_path(file_name)

    if not file_path.exists():
        return "File not found"

    if not file_path.is_file():
        return "The path is not a file"

    return file_path.read_text(encoding= "utf-8")

if __name__ == "__main__":
    mcp.run()