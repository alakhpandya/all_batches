from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name = "Student Server")

students = {
    101 : {
        "name" : "Tanish",
        "age" : 23,
        "gender" : "Male",
        "course" : "GenAI",
        "total fees" : 100000,
        "fees paid" : 40000,
        "batch type" : "one to one",
        "batch name" : "2026_Tanish_Vihang_GenAI"
    },
    102 : {
            "name" : "Vihang",
            "age" : 44,
            "gender" : "Male",
            "course" : "GenAI",
            "total fees" : 100000,
            "fees paid" : 55000,
            "batch type" : "one to one",
            "batch name" : "2026_Tanish_Vihang_GenAI"
    },
    103 : {
            "name" : "Alakh",
            "age" : 45,
            "gender" : "Male",
            "course" : "Data Science",
            "total fees" : 200000,
            "fees paid" : 140000,
            "batch type" : "Gen200",
            "batch name" : "2026_DSAIML_Gen_002"
    }
}


@mcp.tool()
def get_student_info(student_id: int) -> dict:
    """Gets the details like name, age, gender, course, fees paid, total fees, batch type & batch name from their student id"""

    # student_data = students[student_id]
    student_data = students.get(student_id, {"status" : "Student with this student_id does not exist"})
    # print(student_data)
    return student_data

# print(type(get_student_info(201)))

@mcp.tool()
def total_students() -> int:
    """Returns total number of students present in the data"""

    return len(students)

# print(total_students())

if __name__ == "__main__":
    mcp.run()

# Note that this server knows nothing about calculations.