// Array: Sequence of members of same datatype
#include<stdio.h>

int main()
{
    // int s[5] = {4000, 6000, 3000, 2500, 12000}, choice;
    int s[5], choice, i;
    printf("Enter salaries of 5 employees:\n");
    for(i = 0; i < 5; i++)
    {
        scanf("%d", &s[i]);
    }
    // printf("Which employee's salary do you want to see? Enter the serial no of employee starting from 0: ");
    // scanf("%d", &choice);
    // printf("%d", s[choice]);
    // printing the entire array:
    
    return 0;
}