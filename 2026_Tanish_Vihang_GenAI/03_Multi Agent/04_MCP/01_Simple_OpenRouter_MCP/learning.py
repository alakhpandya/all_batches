"""
f = open("requirements.txt", "r")

text = f.read()

f.close()

updated_text = text.upper()
print(updated_text)
"""

# Using "with" block:
with open("requirements.txt", "r") as f:        # same as writing: f = open("requirements.txt", "r")
    text = f.read()

updated_text = text.upper()
print(updated_text)


# "this" = "that"   ->      with "that" as "this":