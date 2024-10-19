/*
#include<stdio.h>

int main()
{
    int i;
    for (i = 1; i <= 10; i++)
    printf("%d) Nency is a good girl.\n", i);
    printf("Thanks!");
    return 0;
}
*/
//Classwork
/*
1. Make a C program to print "I love C!" 13 times with serial number.
2. What would be the output of the following piece of code?

#include <stdio.h>
int main(){
    for(int i = 0;1;i++){
        printf("%d\n",i);
    }
    return 0;
}

3. What would be the output of the following piece of code?
*/
#include <stdio.h>
int main( )
{
    int x = 10, y = 3, z;
    for(z = 0; z<x; )   //z=0, 4, 8, 12
    z = z++ +y; 
    printf("%d\n", z) ;
    return 0;
}

/*
Output:

*/