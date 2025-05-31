#include<stdio.h>

int main()
{
    FILE *fp;
    int i, temp;
    fp = fopen("D:\\C Programs\\.vscode\\Mihir1to1\\mihir1.txt", "w");
    fprintf(fp, "%d", 7);
    printf("Enter 5 numbers: ");
    for ( i = 0; i < 5; i++)
    {
        scanf("%d", &temp);
        fprintf(fp, "\n%d", temp);
    }
    fclose(fp);
    // fp = fopen("D:\\C Programs\\.vscode\\Mihir1to1\\mihir1.txt", "w");
    // fprintf(fp, "%d", 2);
    // fclose(fp);
    return 0;
}
/*
Make a C program to take 10 numbers from user and save them as following:
if number is odd, save it in a file named odd.txt
if number is even, save it in a file named even.txt
if number is prime, save it in a file named prime.txt
Use a function to find if a number is prime or not.
*/