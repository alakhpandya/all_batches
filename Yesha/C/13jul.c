/*
5. Increment/Decrement operators:
    a = 10
    ++a         pre increment operator
    a++         post increment operator

    --a         pre decrement operator
    a--         post decrement operator

6. Bitwise Operators:
    &   -   bitwise and
        3 : 0 0 1 1
        &   & & & &
        5 : 0 1 0 1
        -----------   
            0 0 0 1 = 1

    |   -   bitwise or
        3 : 0 0 1 1
        |
        5 : 0 1 0 1
        -----------   
            0 1 1 1 = 7

    ~   -   bitwise not
        
        5 : 0 1 0 1
        ~5: 1 0 1 0 = - 6
    
    ^   -   bitwise xor     ( = exclusive or)
        What would you like to have? tea or coffee?
        As the first prize, you can win either a macbook pro or iPhone 12.
                Tea     Coffee  OK?
        Krishna  F         F    F
        Yesha    F         T    T
        Nency    T         F    T
        Alakh    T         T    F
        3 : 0 0 1 1
        ^   ^ ^ ^ ^
        5 : 0 1 0 1
        -----------   
            0 1 1 0 = 6

    <<  -   left shift
        13  :   0 0 0 0 1 1 0 1
        <<  :   0 0 0 1 1 0 1 0 = 26
        <<  :   0 0 1 1 0 1 0 0 = 52
        <<  :   0 1 1 0 1 0 0 0 = 104   (13 << 3)

    >>  -   right shift
        50  :   0 0 1 1 0 0 1 0
        >>  :   0 0 0 1 1 0 0 1 = 25
        >>  :   0 0 0 0 1 1 0 0 = 12
        >>  :   0 0 0 0 0 1 1 0 = 6
*/
#include<stdio.h>

int main()
{
    /*
    int a = 10, b = 20;
    printf("a = %d\tb = %d\n", a, b);
    a++;
    b--;
    printf("a = %d\tb = %d", a, b);
    printf("\na = %d\tb = %d", ++a, --b);
    return 0;
    */
    int a = 3, b = 5;
    printf("3 & 5 = %d\n", a & b);
    printf("3 bitwise or 5 = %d\n", 3 | 5);
    printf("bitwise not of 5 = %d\n", ~5);
    printf("3 xor 5 = %d\n", 3 ^ 5);
    printf("13 << 3 = %d\n", 13 << 3);
    printf("50 >> 3 = %d\n", 50 >> 3);
    return 0;
}