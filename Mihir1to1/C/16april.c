#include<stdio.h>
#define RANK 3
void changeRows(int x, int y, float *ptr)
{
    float *p1, *p2, temp;
    int i;
    p1 = ptr + (RANK*x);
    p2 = ptr + (RANK*y);
    for ( i = 0; i < RANK; i++)
    {
        temp = *p1;
        *p1 = *p2;
        *p2 = temp;
        p1++;
        p2++;
    }
}
void divideRow(int x, float d, float *ptr)
{
    float *p;
    int i;
    p = ptr + (RANK*x);
    for ( i = 0; i < RANK; i++)
    {
        *p /= d;
        p++;
    }
}
void printArray(float *ptr)
{
    // This function should be recursive to generalise
    int i, j;
    for ( i = 0; i < RANK; i++)
    {
        for ( j = 0; j < RANK; j++)
        {
            printf("%0.3f\t", *ptr);
            ptr++;
        }
        printf("\n");
    }
}
void addRow(int sr, float multiplyer, int dr, float *ptr)
{
    float *psource, *pdestination;
    int i;
    psource = ptr + RANK*sr;
    pdestination = ptr + RANK*dr;
    for ( i = 0; i < RANK; i++)
    {
        *pdestination += *psource*multiplyer;
        psource++;
        pdestination++;
    }
}
int main()
{
    float a[RANK][RANK], id[RANK][RANK] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    float *pa, *pid, temp;
    int i, j;
    pa = &a[0][0];
    pid = &id[0][0];
    //Taking input
    // printf("Enter Rank of your matrix:")
    printf("Enter %d elements:", RANK*RANK);
    for ( i = 0; i < RANK; i++)
    {
        for (j = 0; j < RANK; j++)
        {
            scanf("%f", &a[i][j]);
        }
    }
    printf("Array:\n");
    printArray(pa);
    for ( j = 0; j < RANK; j++)
    {
        //making a[j][j] non-zero
        if (a[j][j] == 0)
        {
            for (i = 0; i < RANK; i++)
            {
                if (a[i][j] != 0)
                {
                    changeRows(j, i, pa);
                    changeRows(j, i, pid);
                    break;
                }
            }
        }
        // printf("\n");
        // printArray(pa);
        // making a[0][0] = 1
        temp = a[j][j];
        divideRow(j, temp, pa);
        divideRow(j, temp, pid);
        // printf("\n");
        // printArray(pa);
        // getting 0 at a[1][0] & a[2][0]
        // row1 = row0*(-a[1][0]) + row1 & row2 = row0*(-a[2][0]) + row2
        for (i = 0; i < RANK; i++)
        {
            if (i != j)
            {
                temp = -a[i][j];
                addRow(j, temp, i, pa);
                addRow(j, temp, i, pid);
            }
        }
    }
    printf("\nInverse Matrix:\n");
    // printArray(pa);
    printArray(pid);
    return 0;
}