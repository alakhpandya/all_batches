// Defining Constants in C
#include<stdio.h>
#define PI 3.14
#define AREA PI*radius*radius

int main()
{
    float radius;
    // PI++;
    printf("Enter radius: ");
    scanf("%f", &radius);
    printf("Area = %0.2f", AREA);
    return 0;
    /*
    float radius, area;
    // PI++;
    printf("Enter radius: ");
    scanf("%f", &radius);
    area = PI * radius * radius;
    printf("Area = %0.2f", area);
    return 0;
    */
}