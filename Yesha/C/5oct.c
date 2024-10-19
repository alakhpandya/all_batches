/*
HW:
Make use of nested for loops to produce following patterns on the output:
1.
    *****
    ****
    ***
    **
    *

*/
/*
#include<stdio.h>

int main()
{
    int i, j, n;
    printf("Enter number of rows: ");
    scanf("%d", &n);
    for (i=1; i<=n; i++)
    {
        for (j=1; j<=n+1-i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
*/

/*
2.
     *
    **
   ***
  ****
 *****
*/
/*
#include<stdio.h>

int main()
{
    int i, j, n;
    printf("Enter number of rows: ");
    scanf("%d", &n);
    for (i=1; i<=n; i++)
    {
        for (j=1; j<=n+1-i; j++)
        {
            printf(" ");
        }
        for(j=1; j<=i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
*/
/*
2.
     *
    * *
   * * *
  * * * *
 * * * * *
*/
#include<stdio.h>

int main()
{
    int i, j, n;
    printf("Enter number of rows: ");
    scanf("%d", &n);
    for (i=1; i<=n; i++)
    {
        for (j=1; j<=n+1-i; j++)
        {
            printf(" ");
        }
        for(j=1; j<=i; j++)
        {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}

/*
3.
 * * * * *
  * * * *
   * * *
    * *
     *

4. 
     *
    * *
   * * *
  * * * *
 * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *

*/