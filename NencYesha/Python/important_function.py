def avg(n):
    return sum(n)/len(n)

def factorial(a):
    f = 1
    for i in range(1, a+1):
        f =f*i
    return f

def palindrom(s):
    s2 = s[ : : -1]
    if s == s2 :
         return True
    else :
         return False
    
def sum_of_squares(a,b):
    sum=(a ** 2) + (b ** 2)
    return sum

def evenCapitalize(word):
    length = len(word)
    new_word = ""
    for i in range(length):
        if i % 2 == 0:
            new_word = new_word+ word[i].upper()
        else :
            new_word = new_word+ word[i].lower()
    return new_word