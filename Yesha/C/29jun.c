#include<stdio.h>
int main()
{
    int number1, number2, choice;
    printf("Enter two numbers:\n");
    scanf("%d %d", &number1, &number2);
    printf("Which Operation do you want to perform?");
    printf("\nPress 1 for addition");
    printf("\nPress 2 for subtraction");
    printf("\nPress 3 for multiplication");
    printf("\nPress 4 for division\n");
    scanf("%d", &choice);
    switch(choice)
    {
        case 1:
            printf("%d + %d = %d", number1, number2, number1+number2);
            break;
        case 2:
            printf("%d - %d = %d", number1, number2, number1-number2);
            break;
        case 3:
            printf("%d x %d = %d", number1, number2, number1*number2);
            break;
        case 4:
            printf("%d / %d = %d", number1, number2, number1/number2);
            break;
        default:
            printf("Oops! Invalid Operation, Please try again...");
    }
    return 0;
}