#include<stdio.h>
/*
int main()
{
    // while, do while, for loop
    // int i;
    
    // know no of iterations from the begining: for loop
    // don't know how many iterations are going to take: while loop/do while

    // no of digits in an integer:
    
    while (n > 0)
        1592 / 10   = 159
        159 / 10    = 15
        15 / 10     = 1
        1 / 10      = 0
    

    // Arrays: replacing if-else/switch-case
    
    int s[5], i, sr;
    printf("Enter marks of 5 students:");
    for(i=0; i<5; i++){
        scanf("%d", &s[i]);
    }
    printf("Which student's marks do you want to see?\nEnter the serial no:");
    scanf("%d", &sr);
    printf("Marks: %d", s[sr]);
    

    int a[5] = {12, 15, 43, 88, 75}, b[10] = {0};
    int i;
    for ( i = 0; i < 7; i++)
    {
        printf("%d\t", a[i]);
    }
    printf("\n");
    for ( i = 0; i < 10; i++)
    {
        printf("%d\t", b[i]);
    }
    
    return 0;


}
*/
/*
1. Ask 10 integers from user, store them in an array & print the array in this form:
[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
2. Create two arrays: even & odd. Ask 20 integers from user, store them in appropriate arrays. Print both the arrays.
Store '0' at the empty places of the arrays.
3. Ask 5 numbers from user, store them in one array, ask for another 5 numbers & store them in second array. Add both the arrays and produce result in third array named 'sum'. Print the 'sum'.
4. Take 10 numbers from user & store them in an array. Create an another array named 'reversed' and store the reverse of the first array in it. Print both the arrays.
5. Take 10 numbers from user & store them in an array. Find sum of all the numbers of the array and print the sum.
6. Create 5 arrays each one of size 3 (you may define a constant for that) each one representing angles of a triangle. Ask user to enter 3-3 angles five times and print which of the arrays will form (1) a valid triangle or (2) equilateral triangle or (3) isosceles triangle or (4) will not form a triangle at all.
*/


// Defining Constants
#define PI 3.14
#define AREA PI*r*r
#define SIZE 10

int main(){
    // int r;
    // printf("Enter radius: ");
    // scanf("%d", &r);
    // printf("Area = %.2f", PI*r*r);
    // printf("Area = %.2f", AREA);

    int a[SIZE], b[SIZE];
    int i;
    printf("Enter %d integers:\n", SIZE);
    for ( i = 0; i < SIZE; i++)
    {
        scanf("%d", &a[i]);
    }

    return 0;
}