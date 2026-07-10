from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Student Server")

students = {
    101: "Shrey",
    102: "Param",
    103: "Marmik"
}


@mcp.tool()
def get_student(student_id: int):
    """Get student name by ID"""
    return students.get(student_id, "Student not found")


@mcp.tool()
def total_students():
    """Return total number of students"""
    return len(students)

# @mcp.tool()
# def add(stu1: str, stu2: str) -> str:
#     """Concatenate names of students"""
#     return stu1 + stu2

if __name__ == "__main__":
    mcp.run()


# This server knows nothing about mathematics!!