#include<stdio.h>
/*
int main(int argc, char const *argv[])
{
    int temp=5;
    int* p;
    p = &temp;
    // int* p1, p2;
    // int *p;
    // int * p;
    *p = 1;
    printf("temp = %d", temp);
    printf("\nAddress of temp: %d", p);
    return 0;
}

0061FECC=0000 0000 0110 0001 1111 1110 1100 1100
*/

int main(int argc, char const *argv[])
{
    int *pc, c, d;
    c = 5;
    d = -15;
    pc = &c;
    printf("%d", *pc);  //Value of C
    printf("\n%d", pc); //Address of C
    pc = &d;
    printf("\n%d", *pc);  //Value of d
    printf("\n%d", pc); //Address of D
    printf("\n%p", &pc);    //Address of PC
    return 0;
}
