#include<stdio.h>

/*
int main(){
    float a;
    int i;
    FILE *first;
    printf("Enter a number:\n");
    // for(i=0; i<5; i++){
        scanf("%f", &a);
    // }
    first = fopen("second.txt", "w");
    // for(i=0; i<5; i++){
        fprintf(first, "%f\n", a);
    // }
    fclose(first);
    return 0;
}
*/
/*
int main(){
    int a, i;
    FILE *first;
    first = fopen("first.txt", "r");
    for(i=0; i<6; i++)
    {
        printf("Cursor position: %d\n", ftell(first));
        fscanf(first, "%d", &a);        // a = 10, 20
        printf("number - %d: %d\n", i+1, a);
    }

    fseek(first, 6, SEEK_SET);
    fscanf(first, "%d", &a);
    printf("number - after cursor set to 6: %d\n", a);

    rewind(first);    // same as: fseek(first, 0, SEEK_SET);
    fscanf(first, "%d", &a);
    printf("number - after cursor reset: %d\n", a);

    fclose(first);
    return 0;
}
*/
/*
Mode    Name            Functions
w       write           Opens the file for writing only.
                        Creates new file if the file does not exist.
                        Erase the entire content of the file as soon as it opens that file.
                        Writing starts from the begining of the file.

r       read            Opens the file for reading only.
                        Does not create new file if the file does not exist.
                        Does not erase the content of the file.
                        Reading starts from the begining of the file.

a       append          Opens the file for writing only.
                        Creates new file if the file does not exist.
                        Does not erase the content of the file.
                        Cursor is placed at the end of the file.

r+      read plus       Opens the file for reading and writing both.
                        Does not create new file if the file does not exist.
                        Does not erase the content of the file.
                        Places the cursor at the begining of the file.

w+      write plus      Opens the file for writing and reading both.
                        Creates new file if the file does not exist.
                        Erase the entire content of the file as soon as it opens that file.
                        Places the cursor at the begining of the file.

a+      append plus     Opens the file for writing and reading.
                        Creates new file if the file does not exist.
                        Does not erase the content of the file.
                        Cursor is placed at the end of the file.
*/
#include<stdlib.h>

int main(){
    int i, age;
    float height;
    char name[20], gender;
    FILE *user;
    user = fopen("user_data.txt", "a");

    printf("Enter the following details of user:\n");
    printf("Name: ");
    gets(name);
    printf("Age: ");
    scanf("%d", &age);
    printf("Gender (M/F): ");
    fflush(stdin);
    scanf("%c", &gender);
    printf("Height: ");
    scanf("%f", &height);

    // fprintf(user, "Name\tAge\tGender\tHeight\n");
    fprintf(user, "%s\t%d\t%c\t%0.2f\n", name, age, gender, height);


    fclose(user);
    return 0;
}