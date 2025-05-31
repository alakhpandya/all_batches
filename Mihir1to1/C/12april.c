// Inverse of a matrix using Gauss Elimination Method
#include<stdio.h>
#define DIM 3

void changeRows(int x, int y, int *ptr)
{
    int i, *ptr1, *ptr2, temp;
    ptr1 = ptr;
    ptr2 = ptr;
    for (i = 0; i < x*3; i++)
    {
        ptr1++;
    }
    for (i = 0; i < y*3; i++)
    {
        ptr2++;
    }
    for (i = 0; i < 3; i++)
    {
        temp = *ptr1;
        *ptr1 = *ptr2;
        *ptr2 = temp;
        ptr1++;
        ptr2++;
    }
}

void printArray(int *ptr)
{
    int i, j;
    for (i = 0; i < DIM; i++)
    {
        for (j = 0; j < DIM; j++)
        {
            printf("%d\t", *ptr);
            ptr++;
        }
        printf("\n");
    }
}

int main()
{
    int a[DIM][DIM], i, j, identity[3][3] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    int *ap, *ip;
    ap = &a[0][0];       // ap = &arr[0][0]
    ip = &identity[0][0];
    printf("Enter the elements of %dx%d matrix: ", DIM, DIM);
    for (i = 0; i < DIM; i++)
    {
        for (j = 0; j < DIM; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }
    printArray(ap);
    // Making Pivot elements non-zero
    for (i = 0; i < DIM; i++)
    {
        if (a[0][0] == 0 && a[i][0] != 0)
        {
            changeRows(0, i, ap);
            changeRows(0, i, ip);
        }
    }
    for (i = 0; i < DIM; i++)
    {
        if (a[1][1] == 0 && a[2][1] != 0)
        {
            changeRows(1, 2, ap);
            changeRows(1, 2, ip);
        }
    }
    printf("\n");
    printArray(ap);
    return 0;
}