// Operators in C
/*
3. Logical Operators
    And Operator : &&
        1. To complete the homework, you need to do ex1 and ex2.
        2. Your password must be atleast 8 characters long and must contain a special character
                    Ex1     Ex2     Done?
        Alakh       F       F       F
        Nency       F       T       F
        Yesha       T       F       F
        Krishna     T       T       T

    Or Operator : ||
        1. To pass the test attempt either Q1 or Q2 correctly.
        2. To signup, please enter your email address or phone number.
                    Q1     Q2     Done?
        Alakh       F       F       F       
        Nency       F       T       T      
        Yesha       T       F       T      
        Krishna     T       T       T       

    Not Operator : !
        1. Do not write your name on answer sheet.
        2. Special characters are NOT accepted in the phone number feild.
                Wrote Name      OK?
        Alakh       T           F
        Nency       F           T

4. Assignment Operators
    =   : Equals to
        a = 5       5 + 3 = z       z = 5 + 3
         <--             <--         <--
                      WRONG           RIGHT
        
        a = 10
    +=  :   a += b  :   a = a + b
    -=  :   a -= b  :   a = a - b
    *=  :   a *= b  :   a = a * b
    /=  :   a /= b  :   a = a / b
    %=  :   a %= b  :   a = a % b

5.  Increment/Decrement Operators
    a = 10
    a = a + 1 or a += 1
    Post increment Post Decrement
        a++
        a--

    Pre increment Pre Decrement
        ++a
        --a

// Next Lecture:
6. Bitwise Operators
*/
#include<stdio.h>
int main()
{
    /*
    int a, b;
    a = 3 > 5;
    b = 10 < 100;
    printf("a : %d\n",a);
    printf("b : %d\n",b);
    printf("a and b: %d\n", a && b);
    printf("a or b: %d\n", a || b);
    printf("Not a : %d\n", !a);
    printf("Not b : %d\n", !b);
    return 0;
    */
   int a = 10, b = 20;
   printf("a = %d\n", a);
   printf("b = %d\n", b);

   printf("a++ = %d\n", a++);
    printf("a = %d\n", a);
    b--;
    printf("b-- = %d\n", b);
    printf("++a = %d\n", ++a);
    printf("--b = %d\n", --b);
   return 0;
}