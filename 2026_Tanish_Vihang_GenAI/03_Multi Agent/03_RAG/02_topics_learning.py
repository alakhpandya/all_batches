# ------------------ pypdf ------------------
# from pypdf import PdfReader

# pdf_path = "harsh.pdf"
# # pdf_path = "mohit.pdf"

# reader = PdfReader(pdf_path)

# # print(reader.pages)
# for page in reader.pages:
#     print(page.extract_text())
#     break


# ------------------ range & slicing with step ------------------
# for i in range(10, 31, 2):
# for i in range(10, 31, 3):
#     print(i)

st = "Tanish stays in New York city in the United States"
# print(st[10])
# print(st[2 : 18])
# print(st[2 : 18 : 2])

# print(len(st))

# ------------------ Enumerate ------------------
sentences = ["This is an example sentence", "Here is the second one to learn enumerate", "Did you understand what enumerate does now?"]

# for i in enumerate(sentences):
#     print(i)

for i, j in enumerate(sentences):
    # print(i)
    # print(j)
    print(i, j)