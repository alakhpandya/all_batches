// Constants in C
#include<stdio.h>
#define PI 3.14
#define AREA PI*radius*radius

int main()
{
    float radius;
    printf("Enter radius: ");
    scanf("%f", &radius);
    printf("Area = %0.3f", AREA);
    return 0;
    /*
    float radius, area;
    printf("Enter radius: ");
    scanf("%f", &radius);
    area = PI*radius*radius;
    printf("Area = %0.3f", area);
    return 0;
    */
}
// Sorting an array
/*
#include<stdio.h>
#define SIZE 6

int main()
{
    int i, j;
    float a[SIZE], temp;
    // SIZE++;
    printf("Enter %d numbers:\n", SIZE);
    for(i=0; i<SIZE; i++)
    {
        scanf("%f", &a[i]);
    }
    for(j=0; j<(SIZE-1); j++)
    {
        for(i=0; i<(SIZE-1)-j; i++)
        {
            if (a[i] > a[i+1])
            {
                // swap a[i] & a[i+1]
                temp = a[i];
                a[i] = a[i+1];
                a[i+1] = temp;
            }
        }
    }
    // printing the sorted array
    printf("Sorted array: [\t");
    for(i=0; i<SIZE; i++)
    {
        printf("%0.2f\t", a[i]);
    }
    printf("]\n");
    return 0;
}
*/
/*
    if (a[0] > a[1])
    {
        // swap a0 & a1
    }
    if (a[1] > a[2])
    {
        // swap a1 and a2
    }

    if (a[4] > a[5])
    {
        // swap a4 and a5
    }
    for(i=0; i<5; i++)
    {
        if (a[i] > a[i+1])
        {
            // swap a[i] & a[i+1]
        }
    }
*/