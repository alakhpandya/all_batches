from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP(name="File system server")

WORKSPACE = Path("workspace").resolve()

# print("Actual path:", WORKSPACE)


# ----------------------- Guard rail to getting "safe" path -----------------------

def get_safe_path(filename: str) -> Path:

    file_path = (WORKSPACE / filename).resolve()

    # print("\nfile_path =", file_path)

    # print("\nfile_path.parent =", file_path.parent)

    # print("\nfile_path.parents =", file_path.parents)
    
    # print("\nfile_path.parents:")
    # for item in file_path.parents:
    #     print(item)

    if WORKSPACE not in file_path.parents and file_path.parents != WORKSPACE:
        # print("Access Denied.")
        raise ValueError("Access Denied: Unauthorized Access")

    return file_path

# get_safe_path("python_syllabus.pdf")

# file_path = get_safe_path("C:\\Users\\alakh\\Desktop\\all_batches\\DSS_Nov_2025\\04 GenAI\\03_MCP_Architecture\\03_File_System_MCP\\workspace\\ai_notes.txt")

# file_path = get_safe_path("C:\\Users\\alakh\\Desktop\\all_batches\\DSS_Nov_2025\\04 GenAI\\02_RAG\\gk-book.pdf")

# file_path = get_safe_path("workspace\\ai_notes.txt")
# file_path = get_safe_path("workspace\\legal\\privacy_policy.txt")

# print(file_path)
# This is called Path Traversal Protection


# ----------------------- Tool - 1: Listing all the files -----------------------

@mcp.tool()
def list_files() -> list[str]:

    """Lists all the files present in the workspace"""

    files = []

    # print("RGlob:", WORKSPACE.rglob("*"))
    # print("RGlob:")
    # for i in WORKSPACE.rglob("*"):
    #     print(i)

    # print("Available Files:")
    for path in WORKSPACE.rglob("*"):

        if path.is_file():
            relative_path = path.relative_to(WORKSPACE)
            # print(relative_path)
            # print(type(relative_path))
            files.append(str(relative_path))

    return files

# print(list_files())

# ----------------------- Tool - 2: Read a specific file -----------------------

@mcp.tool()
def read_file(filename: str) -> str:
    """Reads the complete content of a file from the workspace"""

    file_path = get_safe_path(filename)
    # print("file_path =", file_path)
    # print("type =", type(file_path))

    if not file_path.exists():
        return "File not found."

    if not file_path.is_file():
        return "Path is not a file."

    return file_path.read_text(encoding= "utf-8")

# print(read_file("attendance_register.txt"))
# print(read_file("ai_notes.txt"))
# print(read_file("legal"))

# ----------------------- Tool - 3: Search Tool -----------------------

# @mcp.tool()
def search_files(query: str) -> list[dict]:
    """Serches for the "query" across all the .txt files present in the workspace"""

    result = []
    for path in WORKSPACE.rglob("*"):

        if path.is_file():

            content = path.read_text(encoding= "utf-8")

            if query.lower() in content.lower():

                result.append(
                    {
                        "file" : str(path.relative_to(WORKSPACE)),
                        "matched" : True
                    }
                )

    return result


print(search_files("Language"))

# ------------------ Tool-4: Get File Info ------------------
