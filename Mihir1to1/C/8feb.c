/*
1.Arithmetic Operators:
    +   Addition/Binary Plus
    -   Subtraction/Binary Minus
    *   Multiplication/Binary Multiplication
    /   Division
        int num1 = 11, num2 = 4;
        float division;
        division = (float) num1/num2;
        printf("Division = %f", division);

    %   Modulo - Returns remainder of division
        11 / 4 = 2 (Quotient)
        11 % 4 = 3 (Remainder)

2.Inc/Dec Operators: ++, --
    a) Pre Inc/ Post Inc
        int a = 10, b;
        //b = ++a     //a = 11, b = 11
        b = a++     //b = 10, a = 11
    b) Pre Dec/ Post Dec
        int a = 10, b;
        b = --a     //a = 9, b = 9
        b = a--     //b =10, a = 9

3.Assignment Operators:
    =   Equals to
        a = 10
         <--
        a + b = c
             <--
        c = a + b
         <--
    +=
        a = a + 10  --> a += 10
    -=
        a = a - 10  --> a -= 10
    *=
        a = a * 10  --> a *= 10
    /=
        a = a / 10  --> a /= 10
    %=
        a = a % 10  --> a %= 10

4. Relational Operators/ Comparision Operators/ Conditional Operators
    Intro to True (1) & False (0)
    ==      Equality    5 == 3 :: False
        x = 5 : Assignment: store value 5 into x.
        x == 5: Question: Is value of x 5?  True/False
        printf("%d", 5==3);

    >       Greater than
    <       Less than
    >=      Greater than or equals to
    <=      Less than or equals to 

5. Logical Operators:
    a < b < c
        a < b and b < c
    
    &&  :   logical and
        a < b && b < c
        To complete the HW, you need to do ex1 & ex2.
        Ex1     Ex2     H.W?
        F       F       F
        F       T       F
        T       F       F
        T       T       T

    ||  :   logical or
        Answer Q1 or Q2.
        Q1      Q2      OK?
        F       F       F
        F       T       T
        T       F       T
        T       T       T

    !   :   logical not
        Do not write your name on question paper.
        Name    OK?
        F       T
        T       F
6.Bitwise Operators:
    &   Bitwise and
        0 0 1 1 =   3
        & & & &     &
        0 1 0 1 =   5
        -------------
        0 0 0 1 =   1
    |   Bitwise or
        0 0 1 1 =   3
        | | | |     |
        0 1 0 1 =   5
        -------------
        0 1 1 1 =   7

    ~   Bitwise not (1's complement)
        printf("%d", ~3); 
    ^   Bitwise xor
        What would you like to have? Tea or Coffee?
        Tea     Coffee  OK?
        F       F       F
        F       T       T
        T       F       T
        T       T       F
    <<  Left shift
    >>  Right shift

7.Sizeof Operator
    int a = 5;
    printf("%d", sizeof(a));
HW: Make a C program to print multiplicative table of integer given by user.
*/
