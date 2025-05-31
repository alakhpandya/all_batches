#include<stdio.h>

int main()
{
    FILE *fp;
    char myString[51], yourString[51];
    printf("Please enter a string upto length 50");
    // scanf("%s", myString);
    fgets(myString, sizeof(myString), stdin);
    fp = fopen("D:\\C Programs\\.vscode\\Mihir1to1\\mihir3.txt", "w+");
    fputs(myString, fp);
    printf("%d", ftell(fp));
    // rewind(fp);
    fseek(fp, 6, SEEK_SET);
    fgets(yourString, 51, fp);
    printf("\n%s", yourString);
    fclose(fp);
    return 0;
}