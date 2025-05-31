/*
#include<stdio.h>

int main()
{
    FILE *fp;
    int i = 1, temp;
    fp = fopen("D:\\C Programs\\.vscode\\Mihir1to1\\mihir1.txt", "r");
    // for (i=0; i<=5; i++)
    // {
    //     fscanf(fp, "%d", &temp);
    //     printf("Number%d: %d\n", i+1, temp);
    // }
    while (!feof(fp))
    {
        fscanf(fp, "%d", &temp);
        printf("Number%d: %d\n", i, temp);
        i++;
    }
    fclose(fp);
    return 0;
}

#include<stdio.h>

int main()
{
    FILE *fp;
    char ch;
    printf("Enter a character: ");
    fflush(stdin);
    scanf("%c", &ch);
    fp = fopen("D:\\C Programs\\.vscode\\Mihir1to1\\mihir2.txt", "w");
    putc(ch, fp);
    fclose(fp);
    return 0;
}
*/
#include<stdio.h>

int main()
{
    FILE *fp;
    char ch;
    int i;
    fp = fopen("D:\\C Programs\\.vscode\\Mihir1to1\\mihir2.txt", "w");
    while ((ch = getchar()) != '\n')
    {
        putc(ch, fp);
    }
    fclose(fp);
    fp = fopen("D:\\C Programs\\.vscode\\Mihir1to1\\mihir2.txt", "r");
    while (!feof(fp))
    {
        ch = getc(fp);
        printf("%c", ch);
    }
    fclose(fp);
    return 0;
}