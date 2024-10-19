/*
Make a C program that takes slaries of 5 employees from the user, then asks which employee's salary to be printed and prints the salary of that employee. 
*/
/*
#include<stdio.h>
int main()
{
    int a,b,c,d,e,n;
    printf("Enter five salaries:");
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
    printf("Whose salary do you want to be printed?\n");
    scanf("%d", &n);
    if(n==1)
    {
        printf("%d", a);
    }
    else if(n==2)
    {
        printf("%d", b);
    }
    else if(n==3)
    {
        printf("%d", c);
    }
     else if(n==4)
    {
        printf("%d", d);
    }
    else if(n==5)
    {
        printf("%d", e);
    }
    else  
    {
        printf("n/a");
    }
    
    
    return 0;
}

*/
// Arrays: Collection of same type of data
#include<stdio.h>

int main()
{
    // int s[5]={5000, 6000, 7000, 8000, 9000}, n;
    int s[5], n, i;
    printf("Enter 5 employee's salaries:\n");
    for(i=0; i<5; i++)
    {
        scanf("%d", &s[i]); //scanf("%d", &s[0]); scanf("%d", &s[1]); scanf("%d", &s[2]); scanf("%d", &s[3]); scanf("%d", &s[4]);
    }
    printf("Which employee's salary do you want to see? ");
    scanf("%d", &n);    //n = 3
    printf("%d", s[n]); // printf("%d", s[3])
    return 0;
}