# Decision Making (if-else)

"""
int a = -10, c = 5;

if (a > 0){
    printf("You are positive!");
  c--;
 printf("New value of c = %d", c);
}
printf("Thanks for using our program!");

blocks
"""
a = float(input("a: "))
c = 5
if a > 0:
    print("You are positive!")
    c -= 1
    print("New value of c =", c)
print("Thanks for using our program!")
