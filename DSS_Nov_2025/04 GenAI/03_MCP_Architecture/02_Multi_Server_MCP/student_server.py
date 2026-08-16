from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Student Server")

students = {
    101 : "Nikita",
    102 : "Kushal",
    103 : "Mohit",
    104 : "Jay",
    105 : "Yash"
}

@mcp.tool()
def get_student_name(student_id: int) -> str:
    """Gets the name of the student from their id"""

    # return students[student_id]
    return students.get(student_id, "Student not found")


# print(get_student_name(107))

@mcp.tool()
def total_students() -> int:
    """Returns total number of students"""

    return len(students)


if __name__ == "__main__":
    mcp.run()


# This server knows nothing about the calculations!