# import server
# from server import get_exchange_rate

# print(server.get_exchange_rate("USD", "EUR"))
# print("Hey, welcome to our agent program...")


# fp = open("dependency.txt", "r+")
# fp.read()
# fp.write("Hello")
# fp.close()


# with open("dependency.txt", "r+") as fp:
#     fp.read()
#     fp.write("Hi")

# print("End of code")

def test_func(num1, num2):
    sum = num1 + num2
    diff = num1 - num2
    return sum, diff


# answer = test_func(10, 8)
# a = answer[0]
# b = answer[1]
# print(answer)
a, b = test_func(10, 8)
print(a)
print(b)

with test_func(10, 8) as (a, b):
    print(a)
    print(b)