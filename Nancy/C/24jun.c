// Loops: To execute a specific instruction/set of instructions again & again without writing them again & again, we use loop.
#include<stdio.h>
int main()
{
    int i;
    for(i = -5; i < 5; i++)//(i=-3;i>0;i++) / (i=0; i<3; i++) / (i=1; i<=10; i++)
    {
        printf("%d. Hello C!\n", i+6);
        // count++;
    }
    return 0;
}
/*  Execute: |||||
i = 1;  i <= 5 ? => True => Execute; 
i = 2;  i <= 5 ? => True => E
i = 3;
i = 4;
i = 5;
i = 6;  i <= 5 ? => False => Don't Execute, Exit the loop
i = 1, 2, 

*/