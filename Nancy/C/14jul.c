#include<stdio.h>

int main()
{
    int n1, n2;
    char choice;
    printf("Enter two integers: ");
    scanf("%d %d", &n1, &n2);
    printf("Which operation do you want to perform? +, -, * or /\n");
    // fflush(stdin);
    scanf(" %c", &choice);
    switch(choice)      // block title
    {
        case '+':
            printf("%d + %d = %d", n1, n2, n1 + n2);
            break;
        case '-':
            printf("%d - %d = %d", n1, n2, n1 - n2);
            break;
        case '*':
            printf("%d x %d = %d", n1, n2, n1 * n2);
            break;
        case '/':
            printf("%d / %d = %d", n1, n2, n1 / n2);
            break;
        default:
            printf("Invalid Operation! Please try again...");
    }
    return 0;
}