/*
Make a C program to store & display names, marks & heights of 3
students.
*/
/*
#include<stdio.h>

int main(int argc, char const *argv[])
{
    int studentData[3][2], i, j, k, length;
    char studentName[3][25];
    for ( i = 0; i < 3; i++)
    {
        printf("Enter the length of name of student%d: ", i);
        scanf("%d", &length);
        printf("Enter the name of student%d: ", i);
        for ( j = 0; j < length; j++)
        {
            printf("charcter%d: ", j);
            scanf(" %c", &studentName[i][j]);
        }    
    }
    for ( i = 0; i < 3; i++)
    {
        printf("Enter data of student%d", i);
        printf("\nmarks: ");
        scanf("%d", &studentData[i][0]);
        printf("\nheight: ");
        scanf("%d", &studentData[i][1]);
    }
        
    return 0;
}
*/
//Structure:: is a user-defined data type.
#include<stdio.h>
struct Student
{
    char name[50];
    int marks;
    float height;
};
int main(int argc, char const *argv[])
{
    int length, i, j;
    struct Student stu[3];
    for(j=0; j<3; j++)
    {
        printf("Please enter marks of stu%d: ", j);
        scanf("%d", &stu[j].marks);
        printf("Please enter height of stu%d: ", j);
        scanf("%f", &stu[j].height);
        printf("Please enter length of name of stu%d: ", j);
        scanf("%d", &length);
        printf("\nEnter the name of stu%d: ", j);
        for ( i = 0; i < length; i++)
        {
            printf("character%d: ", i);
            scanf(" %c", &stu[j].name[i]);
        }
    }
    return 0;
}
