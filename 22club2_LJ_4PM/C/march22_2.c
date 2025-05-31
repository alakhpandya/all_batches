#include<stdio.h>

struct student{
    int marks[3];
    float height;
    char name[50];
};

int main()
{
    // structure
    /*
        // Premitive Data Types
        short int, int, long int, long long int, 
        char, 
        float, double, long double
        // Derived Data Type
        array,
        string
        // User Defined Data Type
        structure
    */

    // write a program that takes names, marks in 3 subjects & heights of 5 students. Ask user whose result for which subject does she want to see and just print that marks. All marks should be considered as integers & height floats.
    int i;
    struct student s1;
    s1.height = 171.5;
    s1.marks[0] = 10;
    s1.marks[1] = 20;
    s1.marks[2] = 30;
    printf("Height = %.2f", s1.height);
    for ( i = 0; i < 3; i++)
    {
        printf("\nSub-%d: %d", i+1, s1.marks[i]);
    }
    
    return 0;
}