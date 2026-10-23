# memoization
# from functools import lru_cache

# @lru_cache()
# def fibonnaci(num):
#   if(num==1 or num==0):
#     return num
#   return fibonnaci(num-1)+fibonnaci(num-2)

terms = {}
def fibonnaci(num):
  global terms
  if num in terms:
    return terms[num]
  
  if(num==1 or num==0):
    terms[num] = num
    return num

  term = fibonnaci(num-1)+fibonnaci(num-2)
  terms[num] = term
  return term

n=int(input("Please enter a number: "))
print("Sr No.\t Term")
for i in range(n):
  print(i,"\t",fibonnaci(i))

"""
Sr.No   Term
0       1
1       1
2       2
3       3
4       5
"""