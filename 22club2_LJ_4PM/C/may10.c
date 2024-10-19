/*
Modes:
r: read mode
w: write mode
a: append mode

r+: read + write - cursor is placed at the begining (at 0)
w+: write + read - cursor is placed at the begining (at 0)
a+: append + read - cursor is placed at the end of the file
*/
#include<stdio.h>

int main()
{
    FILE *fTemp;
    char name[20], name_in_file[20];
    // printf("Name: ");
    // gets(name);
    
    // fTemp = fopen("temp.txt", "w");
    // fputs(name, fTemp);
    // fclose(fTemp);

    // fTemp = fopen("temp.txt", "r");
    // fgets(name_in_file, 20, fTemp);
    // fclose(fTemp);

    fTemp = fopen("temp.txt", "w+");
    printf("Next Name: ");
    gets(name);
    fputs(name, fTemp);

    fseek(fTemp, 0, SEEK_SET);
    fgets(name_in_file, 20, fTemp);
    printf("\nName in file: %s", name_in_file);

    fclose(fTemp);
    return 0;
}

/*
HW:

*/












