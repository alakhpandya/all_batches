from openai import OpenAI
from dotenv import load_dotenv
import json
import os
from pprint import pprint

# ---------------- LLM Client ---------------- 

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

messages = [
    {
        "role": "system",
        "content": """
        You are a student relationship expert and professional copywriter for an educational institute.

        Generate a warm, personalized, and motivational welcome message for a newly enrolled student of Royal Technosoft.

        ### Student Details
        - Student Name: "Harsh Vaghasiya"
        - Gender: "Male"
        - Course Enrolled: "Generative AI"

        ### Instructions

        Write a message that:

        1. Begins with a warm greeting using the student's name.
        2. Congratulates the student on joining Royal Technosoft.
        3. Appreciates their decision to invest in learning the enrolled course.
        4. Motivates the student by explaining that consistent learning and regular attendance are the keys to success.
        5. Encourages the student to attend every session on time, actively participate, ask questions without hesitation, complete assignments, and practice regularly.
        6. Makes the student feel that Royal Technosoft is not just an institute but a supportive learning family where trainers and staff are always ready to help.
        7. Encourages the student to communicate openly whenever they face any difficulty, whether academic or technical.
        8. Ends with an inspiring note wishing them success in their learning journey and future career.
        9. Maintain a friendly, encouraging, and professional tone.
        10. Keep the message between 180 and 250 words.
        11. Do not use overly formal or robotic language.
        12. Use gender-appropriate pronouns based on the provided gender.
        13. Include 2-3 relevant emojis naturally (such as 🎓, 🚀, 💻, 🌟) without overusing them.
        14. Mention the enrolled course naturally within the message.
        15. Do not use quotation marks around the message.

        The message should sound as if it is personally written by the Royal Technosoft team.
        """
    }
]

response = client.chat.completions.create(

    model="deepseek/deepseek-chat",

    messages=messages
)


final_response = response.choices[0].message.content
print("[Agent] :\n", final_response)
