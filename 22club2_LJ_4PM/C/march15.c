#include<stdio.h>
#include<string.h>

// Defining the function
void printFullName(char name1[20]){
    printf("\nYour first name: %s", name1);
    // printf("\nYour full name is: Kalp Patni\n");
}

void average(float a, float b){
    printf("Average of %.3f and %.3f = %.3f", a, b, (a + b)/2);
}


int main()
{
    /*
    char firstName[20], lastName[20], fullName[40];
    
    printf("Enter first name: ");
    gets(firstName);
    
    printf("Enter last name: ");
    gets(lastName);
    */
    // Comparing two strings
    // printf("%d", strcmp(firstName, lastName));
    /*
    if(strcmp(firstName, lastName) == 0){
        printf("It looks like you have same first name & last name!");
    }
    */
    
    // length of a string
    // printf("The length of your first name is: %d", strlen(firstName));

    // concatenate two strings
    /*
    strcat(fullName, firstName);
    strcat(fullName, " ");
    strcat(fullName, lastName);
    printf("Hello %s!", fullName);
    */

    // copying a string into another
    /*
    strcpy(fullName, firstName);
    strcat(fullName, " ");
    strcat(fullName, lastName);
    printf("Hello %s!", fullName);
    */

    // Functions
    // printFullName(firstName);        // calling the function


    float p, q, r;
    printf("p: ");      
    scanf("%f", &p);    // 10
    printf("q: ");
    scanf("%f", &q);    // 20
    printf("r: ");
    scanf("%f", &r);    // 30
    // average(10, 20);
    average(p, q);
    average(q, r);
    return 0;
}