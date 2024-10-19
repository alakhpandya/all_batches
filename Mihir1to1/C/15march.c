#include<stdio.h>

int main()
{
    FILE *fp;
    char ch;
    fp = fopen("D:\\C Programs\\.vscode\\Mihir1to1\\mihir2.txt", "w");
    fprintf(fp, "\n");
    while ((ch = getchar()) != '\n')
    {
        putc(ch, fp);
    }
    fclose(fp);
    return 0;
}
/*
Mode    Name        Details
w       write       Opens file for writing. Creates file if it does not exist. Clears
                    all the content of the file & then starts writing from 1st line.

r       read        
a       append      Opens file for writing. Creates file if it does not exist. It does
                    not clears the content of the file & starts writing from last line.        
        
w+      write plus  read + write
                    clears the existing file first/creates new file

r+      read plus   read + write
a+      append plus read + append
                    reading starts with first line
                    writing starts with last line.
                    Creates new file if it does not exist
*/