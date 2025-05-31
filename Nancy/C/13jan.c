/*
Class work:
Write a C program that takes marks, height and fees of 5 students (all integers) and print all the details (Marks, Height and Fees) of the student given by user.
*/
/*
#include<stdio.h>

int main()
{
    int marks[5], height[5], fees[5], i, sr_no;
    for(i=0; i<5; i++)
    {
        printf("Enter marks, height and fees for student-%d\n", i);
        scanf("%d %d %d", &marks[i], &height[i], &fees[i]);
    }
    printf("Which student's details do you want to see? Enter student number: ");
    scanf("%d", &sr_no);
    printf("Details of student-%d:\n", sr_no);
    printf("Marks: %d\n", marks[sr_no]);
    printf("Height: %d\n", height[sr_no]);
    printf("Fees: %d\n", fees[sr_no]);
    return 0;
}
*/
/*
Write a C program that takes 12 parameters (all integers, like: cc, mileage, ground clearance, length, width, height, weight, engine hp etc) for 10 cars. Finally print all the parameter of specific car given by user.
*/
#include<stdio.h>
int main()
{
    int cc[10], mileage[10], gc[10], l[10], w[10], h[10], weight[10], hp[10], torque[10], airbags[10];
    int i;
    for ( i = 0; i < 10; i++)
    {
        printf("Enter cc, mileage, gc, l, w, h, weight, hp, torque and airbags for car-%d\n", i);
        scanf("%d %d %d %d %d %d %d %d %d %d", &cc[i])
    }
    
}
/*
Multidimensional Arrays
*/