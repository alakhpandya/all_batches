/*
Write a program that takes marks, height and fees of 5 students and then ask user what does she want to do:
to print the details of the student with highest marks or
to print the details of the tallest student or
to print the details of the student paying highest fees.
Print the output accordingly.
*/
/*
#include<stdio.h>

int main()
{
    int s[5][3], i, j, choice, max, stu;

    for ( i = 0; i < 5; i++)
    {
        printf("Enter marks, height and fees of student-%d:\n", i);
        for ( j = 0; j < 3; j++)
        {
            scanf("%d", &s[i][j]);
        }
    }
    printf("Values entered successfully! What do you want to do now?\n");
    printf("Press 1 to print the details of the student with highest marks\n");
    printf("Press 2 to print the details of the tallest student\n");
    printf("Press 3 to print the details of the student paying highest fees\n");
    scanf("%d", &choice);
    switch(choice){
        case 1 :
            max = s[0][0];
            stu = 0;
            for ( i = 1; i < 5; i++)
            {
                if (s[i][0] > max)
                {
                    max = s[i][0];
                    stu = i;
                }
            }
            printf("Details of student with highest marks:\n");
            printf("Marks: %d\n", s[stu][0]);
            printf("Height: %d\n", s[stu][1]);
            printf("Fees: %d\n", s[stu][2]);
            break;
        case 2: 
            //code
            break;
        case 3:
            //code
            break;
        default:
            printf("Invalid operation, please try again");
    }
    return 0;
}
*/
/*
Write a C program to store name of a student & print it.
*/
#include<stdio.h>
#include<stdlib.h>
// Way - 1 using %c
/*
int main()
{
    char name[30];
    int i, l;
    // int s[5];
    printf("Enter length of your name: ");
    scanf("%d", &l);
    printf("Enter name: ");
    for(i=0; i<l; i++)
    {
        scanf(" %c", &name[i]);
        // fflush(stdin);
        // scanf("%c", &name[i]);
    }
    printf("Your name is: ");
    for ( i = 0; i < l; i++)
    {
        printf("%c", name[i]);
    }
    
    return 0;
}
*/
// Way - 2 using %s
/*
int main()
{
    char name[30];
    printf("Enter your name: ");
    scanf("%s", name);
    printf("Your name is: %s", name);
    return 0;
}
*/
// Way - 3 using gets and %s
int main()
{
    char name[20];
    printf("Enter your name: ");
    gets(name);
    printf("Your name is: %s", name);
    return 0;
}
// Next class: null character: how does 'C' know your string is ended?, taking names of 5 students