#include<stdio.h>

int main()
{
    int number1, number2;
    char choice;
    printf("Enter two numbers:\n");
    scanf("%i %i", &number1, &number2);
    printf("Which Operation do you want to perform? +, -, * or /?");
    printf("\nEnter your choice: ");
    // fflush(stdin);
    scanf(" %c", &choice);
    switch(choice)
    {
        case '+':
            printf("%d + %d = %d", number1, number2, number1+number2);
            break;
        case '-':
            printf("%d - %d = %d", number1, number2, number1-number2);
            break;
        case '*':
            printf("%d x %d = %d", number1, number2, number1*number2);
            break;
        case '/':
            printf("%d / %d = %0.10f", number1, number2, (float)number1/number2);
            break;
        default:
            printf("Oops! Invalid Operation, Please try again...");
    }
    return 0;
}

/*
Datatype    Keyword         Size                Format Specifier    Range
integer     int             4 B                     %d, %i          -2,147,483,648 to 2,147,483,647
            long int        4 B                     %ld, %li            
            long long int   8 B                     %lld, %lli

decimals    float           4 B                     %f              
            double          8 B                     %lf
            long double     10, 12 or 16 Bytes      %Lf

character   char            1 B                     %c      
*/