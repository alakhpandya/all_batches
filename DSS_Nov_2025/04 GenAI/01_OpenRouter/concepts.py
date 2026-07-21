st = "hey, good morning to all of you! I am so much excited to learn Generative AI this weekend!!! I hope you are also equally excited..."
# print(st.split("!"))
word_list = st.split()
print(word_list)
print(len(word_list))
# print(word_list[0 : 10])
# print(word_list[ : 10])
# print(word_list[5 : ])
# word_list[50]                 # Error

summary_list = word_list[ :20]
# print(summary_list)

# summary_list.join("-")            # Error
# summary =  "-".join(summary_list)
summary =  " ".join(summary_list)
print(summary)