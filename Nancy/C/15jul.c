#include<stdio.h>

int main()
{
    int n1, n2;
    float n3, answer;
    char choice;
    printf("Enter three numbers: ");
    scanf("%d %d %f", &n1, &n2, &n3);
    printf("Which operation do you want to perform on n1 & n2? +, -, * or /\n");
    // fflush(stdin);
    scanf(" %c", &choice);
    
    switch(choice)      // block title
    {
        case '+':
            answer = n1 + n2;
            printf("%d + %d = %f", n1, n2, answer);
            break;
        case '-':
            answer = n1 - n2;
            printf("%d - %d = %f", n1, n2, answer);
            break;
        case '*':
            answer = n1 * n2;
            printf("%d * %d = %f", n1, n2, answer);
            break;
        case '/':
            answer = (float) n1 / n2
            printf("%d / %d = %0.9f", n1, n2, answer);
            break;
        default:
            printf("Invalid Operation! Please try again...");
    }
    printf("What would you want to do with answer & n3? +, -, * or /\n")
    scanf(" %c", &choice2);
    return 0;
}