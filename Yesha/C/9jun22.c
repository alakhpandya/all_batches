#include<stdio.h>

int main()
{
    int n;
    FILE *fp;
    printf("Enter n: ");
    scanf("%d", &n);
    // printf("%d", n);
    fp = fopen("first.txt", "w");

    fprintf(fp, "%d", n);

    fclose(fp);
    return 0;
}