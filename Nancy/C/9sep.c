/*
Solution of classwork:
2. Ask an integer from user & print sum of all the natural numbers till that integer.
input: 5
output: 15 (1+2+3+4+5)
*/
#include<stdio.h>

int main()
{
    int n, sum = 0, i;
    printf("Enter any number: ");
    scanf("%d", &n);            //5
    for (i = 1; i <= n; i++)    //i = 1     2       3       4       5
    {
        sum = sum + i;          //sum=0+1   =1+2    =3+3    =6+4    =10+5
    }                           //sum=1     3       6       10      15
    printf("sum = %d", sum);
    return 0;
}
/*
3. Ask an integer from user & print sum of all the even natural numbers till that integer.
4. Ask an integer from the user & print all the whole squres till that number.
*/