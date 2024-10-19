#include<stdio.h>

/*
int main()
{
    char firstName[20], lastName[20];
    int i, len1, len2;
    printf("Enter length of your first name: ");
    scanf("%d", &len1);
    printf("First Name: ");
    for ( i = 0; i < len1; i++)
    {
        scanf(" %c", &firstName[i]);
    }
    printf("Enter length of your last name: ");
    scanf("%d", &len2);
    printf("Last Name: ");
    for ( i = 0; i < len2; i++)
    {
        scanf(" %c", &lastName[i]);
    }
    

    printf("Your Full Name: ");
    for ( i = 0; i < len1; i++)
    {
        printf("%c", firstName[i]);
    }
    printf(" ");
    for ( i = 0; i < len2; i++)
    {
        printf("%c", lastName[i]);
    }
    return 0;
}
*/

/*
int main(){
    char firstName[20], lastName[20];

    printf("First Name: ");
    scanf("%s", firstName);
    
    printf("Last Name: ");
    scanf("%s", lastName);

    printf("Your Full Name: %s %s", firstName, lastName);
    return 0;
}
*/
#include<string.h>
/*
int main(){
    char firstName[20], lastName[20], fullName[40];
    int i, result;

    printf("First Name: ");
    gets(firstName);

    printf("Last Name: ");
    gets(lastName);

    result = strcmp(firstName, lastName);
    if (result == 0){
        printf("Strange! You've got the same first & last names!");
    }
    else{
        printf("Got it!");
    }
    // printf("%d", result);

    printf("\nYour Full Name: %s %s\n\n", firstName, lastName);
    
    for ( i = 0; i < 20; i++)
    {
        printf("%c", firstName[i]);
    }
    
    return 0;
}
*/

int main(){
    char firstName[20], lastName[20], fullName[40];
    int i, len1;

    printf("Enter length of your first name: ");
    scanf("%d", &len1);
    printf("Your First Name: ");
    for ( i = 0; i < len1; i++)
    {
        scanf(" %c", &firstName[i]);
    }
    firstName[i] = '\0';

    printf("%s", firstName);

    return 0;
}
