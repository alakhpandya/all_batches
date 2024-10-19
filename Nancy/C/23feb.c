/*
Premitive/Basic Datatypes: 
int (2 or 4 Byte), long int (4 Byte), long long int (8 Bytes), char, float (4 Bytes), double (8 Bytes), long double (10, 12 or 16 Bytes)

1 Byte = 8 bits
4 Byte = 32 bits - 1 sign bit = 31
(2^31 - 1) = 2,14,74,83,647

8 Byte = 64 bits - 1 bit for sign = 63
(2^63 - 1) = 

Derived Datatypes:
Arrays, Strings

User Defined Datatype:
Structure
*/
#include<stdio.h>
/*
int main()
{
    long long int a = 2000000000, b = 1000000000;
    long double c;
    // printf("a + b = %lld", a + b);
    printf("Size of C = %d", sizeof(c));
    return 0;
}
*/
/*
Write a C code that takes names, marks & height of 5 students and prints all the data of the student given by user.
*/
struct Student{
    char name[50];
    int marks;
    float height;
};
int main()
{
    struct Student s0;
    // s0.marks = 94;
    printf("Enter following details of s0:\n");
    printf("Name: ");
    gets(s0.name);
    printf("Marks: ");
    scanf("%d", &s0.marks);
    printf("Height: ");
    scanf("%f", &s0.height);
    printf("Name of s0: %s\n", s0.name);
    printf("Marks of s0: %d\n", s0.marks);
    printf("Height of s0: %.2f\n", s0.height);
    return 0;
}
/*
1. Write a C structure that stores name, salary (integer) and increment (percentage - in float) of an employee. Create 3 employees in this structure and print all the details of all the employees.
*/