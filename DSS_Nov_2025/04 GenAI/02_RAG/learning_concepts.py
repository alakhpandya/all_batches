"""
st = "Developed an AI-powered Helmet Detection System using YOLOv8 and OpenCV to identify helmet compliance among two-wheeler riders. Applied Python, NumPy, Pandas, PyTorch, and OpenCV applied for data preprocessing, model training, and real-time detection. "

print(len(st))
# print(st[24])
# print(st[0 : 20])
# print(st[20 : 40])
# print(st[40 : 60])

chunk_size = 20

print("Start\tStop")
for i in range(0, len(st), chunk_size):     # i = 0, 20, 40, 60, ... 240
    # print(i)
    print(i, "\t", chunk_size + i)
    
"""

# enumerate:
"""
my_list = ["Apple", "Banana", "Mango"]

# print(list(enumerate(my_list)))       # -> [(0, "Apple"), (1, "Banana"), (2, "Mango")]

for index, fruit in enumerate(my_list):
    print(index, "\t", fruit)
"""

# join

result = ['a Science, Machine \nLearning. \nEXPERIENCE \nInfoLabz Ahmedabad, Flutter Intern June 2026 – July 2026 ', 'earning, data \nstructures, and algorithms. Adept at problem-solving and enthusiastic about developin', 'Harsh Vadhvana \nAhmedabad, Gujarat, India , harsh.vadhvana7@gmail.com , +91-9228229572 , LinkedIn , ', 'ring and Technology | Ahmedabad                   \n• Coursework: Data Structures & Algorithms, Objec', 'penCV, TensorFlow, PyTorch  \nConcepts: Machine Learning, Data Structures, Data Science and RESTAPI  ']

# result.join("|")            # error

# context = "|".join(result)
context = "\n\n".join(result)
print(context)