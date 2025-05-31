#include<stdio.h>
int main()
{
    int n1, n2, choice;
    printf("Enter two integers:");
    scanf("%d %d", &n1, &n2);
    printf("Which operation do you want to perform?\n");
    printf("Press 1 for addition\n");
    printf("Press 2 for subtraction\n");
    printf("Press 3 for multiplication\n");
    printf("Press 4 for division\n");
    scanf("%d", &choice);
    switch(choice)
    {
        case 1:
            printf("sum = %d", n1 + n2);
            break;

        case 2:
            printf("diff = %d", n1 - n2);
            break;

        case 3:
            printf("multiplication = %d", n1 * n2);
            break;

        case 4:
            printf("division = %d", n1 / n2);
            break;

        default:
            printf("Invalid Operation! Please try again...");
    }
    return 0;
}