/*
Write a C program that takes names, population (integer) and literacy rate (float) of 5 cities and print them all.
*/
/*
Premitive/Basic Datatypes: int, long int, long long int, float, double, long double, char
Derived Datatypes: Arrays, Strings
User Defined Datatype: Structure
*/
#include<stdio.h>
#include<stdlib.h>

struct City{
    char name[20];
    int pop;
    float literacy_rate;
};
int main()
{
    // int a, b;
    // printf("Enter two numbers: ");
    // scanf("%d %d", &a, &b);

    // struct City c0, c1;
    // printf("Enter name of c0: ");
    // gets(c0.name);
    // printf("Enter the population of c0: ");
    // scanf("%d", &c0.pop);
    // printf("Enter the literacy rate of c0: ");
    // scanf("%f", &c0.literacy_rate);
    // printf("Details of city c0:\n");
    // printf("Name: %s\nPopulation: %d\nLiteracy Rate: %.2f\n", c0.name, c0.pop, c0.literacy_rate);

    struct City c[5];
    int i, choice;
    for(i=0; i<5; i++)
    {
        printf("Enter details of c%d:\n", i);
        printf("Name: ");
        fflush(stdin);
        gets(c[i].name);
        printf("Population: ");
        scanf("%d", &c[i].pop);
        printf("Literacy Rate: ");
        scanf("%f", &c[i].literacy_rate);
    }
    printf("Which city's details do you want to see? Enter city number: ");
    scanf("%d", &choice);
    printf("-----Details of city C%d-----\n", choice);
    printf("Name: %s\nPopulation: %d\nLiteracy Rate: %.2f\n", c[choice].name, c[choice].pop, c[choice].literacy_rate);
    return 0;
}

/*
Classwork:
1. Write a C program that takes names, marks (integer) and height (float) of a student using structure and print all of them.
2. Write a C program that takes names, marks (integer) and height (float) of 5 students using structure and print all of them in the form of a table as below:
Sr.No.  Name        Marks   Heigh
1       Jignesh     75      168.5
2       Dipti       92      165
3       Vishva      77      152
4       Parth       97      160.5
5       Rushir      82      171.5
*/