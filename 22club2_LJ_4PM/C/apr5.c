/*
#include<stdio.h>
struct student{
    int marks[3];
    float height;
    char name[50];
};
int main()
{
    // write a program that takes names, marks in 3 subjects & heights of 5 students. Ask user whose result for which subject does she want to see and just print that marks. All marks should be considered as integers & height floats.
    int i, j;
    struct student s[5];
    printf("Enter the following details for ");
    for ( i = 0; i < 5; i++)
    {
        printf("Student-%d:\nName: ", i);
        fflush(stdin);
        gets(s[i].name);
        printf("Height: ");
        scanf("%f", &s[i].height);
        for ( j = 0; j < 3; j++)
        {
            printf("Marks-%d: ", j);
            scanf("%d", &s[i].marks[j]);
        }
    }
    return 0;
}
*/
/*
Write a program to add two distances in inch-feet using structure. The values of the distances is to be taken from the user.
*/

// Passing structure to a function & returning a structure from a function

#include<stdio.h>
struct distance{
    int feet, inch;
};
struct distance add_distances(struct distance a, struct distance b){
    struct distance sum;
    sum.feet = a.feet + b.feet;
    sum.inch = a.inch + b.inch;
    if (sum.inch >= 12){
        sum.feet++;
        sum.inch -= 12;
    }
    // printf("Total Distance:\nFeet: %d\nInch: %d", sum.feet, sum.inch);
    return sum;
}
int main()
{
    // struct distance{
    //     int feet, inch;
    // };
    struct distance d1, d2, total;
    printf("Enter distance-1:\nFeet: ");
    scanf("%d", &d1.feet);
    printf("Inches: ");
    scanf("%d", &d1.inch);
    printf("Enter distance-2:\nFeet: ");
    scanf("%d", &d2.feet);
    printf("Inches: ");
    scanf("%d", &d2.inch);

    total = add_distances(d1, d2);
    printf("Total Distance:\nFeet: %d\nInch: %d", total.feet, total.inch);

    return 0;
}

// HW:
/*
1. Write a program to store and print the roll no., name , age and marks of a student using structures.

2. Write a program to store the roll no. (starting from 1), name and age of 5 students and then print the details of the student with roll no. 2.

3. Write a program to store the roll no. (starting from 1), name and age of 5 students and then print the details of the student with roll no. given by user.

4. Write a program to add two distances in inch-feet using structure. The values of the distances is to be taken from the user.

5. Enter the marks of 5 students in Chemistry, Mathematics and Physics (each out of 100) using a structure named Marks having elements roll no., name, chem_marks, maths_marks and phy_marks and then display the percentage of each student in a tabular form.

6. Write a program to add, subtract and multiply two complex numbers using structures to function.

7. Write a structure to store the roll no., name, age (between 11 to 14) and address of students (more than 10). Store the information of the students.
1 - Print the names of all the students having age 14.
2 - Also print the names of all the students having even roll no.

8. Write a structure to store the name, account number and balance of customers (more than 10) and store their information.
1 - Print the names of all the customers having balance less than $200.
2 - Add $100 in the balance of all the customers having more than $1000 in their balance and then print the incremented value of their balance.

9. Write a program to compare two dates entered by user. Make a structure named Date to store the elements day, month and year (all integers) to store the dates. If the dates are equal, display "Dates are equal" otherwise display "Dates are not equal".
*/