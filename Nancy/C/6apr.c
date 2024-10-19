/*
Functions: Assistants
1. Without argument, without return
2. With argument, without return
3. Without argument, with return
4. With arguments, with return
*/
/*
#include<stdio.h>
void kameshwar()
{
    printf("Smart and A.C Classrooms with CCTV.\nHi Tech Computer Lab, Maths & Science Laboratory and well stocked Library Music, Drawing and Dance classes along with Kids club.\nSuitable uniform, Study Materials, Course Books.\n\n");
}

int main()
{
    int a, b;
    printf("Enter two integers:\n");
    scanf("%d%d", &a, &b);  //  a = 10, b = 5
    if (a>b){
        kameshwar();
    }
    if (a*b > 0){
        kameshwar();
    }
    if (a/b > 1){
        kameshwar();
    }
    if (a > (b+1)){
        kameshwar();
    }
}

*/
/*
int main()
{
    int a, b;
    printf("Enter two integers:\n");
    scanf("%d%d", &a, &b);  //  a = 10, b = 5
    if (a>b){
        printf("Smart and A.C Classrooms with CCTV.Hi Tech Computer Lab, Maths & Science Laboratory and well stocked Library Music, Drawing and Dance classes along with Kids club. Suitable uniform, Study Materials, Course Books.");
    }
    if (a*b > 0){
        printf("Smart and A.C Classrooms with CCTV.Hi Tech Computer Lab, Maths & Science Laboratory and well stocked Library Music, Drawing and Dance classes along with Kids club. Suitable uniform, Study Materials, Course Books.");
    }
    if (a/b > 1){
        printf("Smart and A.C Classrooms with CCTV.Hi Tech Computer Lab, Maths & Science Laboratory and well stocked Library Music, Drawing and Dance classes along with Kids club. Suitable uniform, Study Materials, Course Books.");
    }
    if (a > (b + 1)){
        printf("Smart and A.C Classrooms with CCTV.Hi Tech Computer Lab, Maths & Science Laboratory and well stocked Library Music, Drawing and Dance classes along with Kids club. Suitable uniform, Study Materials, Course Books.");
    }
    return 0;
}
*/
#include<stdio.h>
void average(int n1, int n2)
{
    float ans;
    ans = (n1 + n2)/2.0;
    printf("The average of %d and %d = %0.3f", n1, n2, ans);
}
int main()
{
    int a, b;
    printf("Enter two integers:\n");
    scanf("%d%d", &a, &b);  //  a = 25, b = 35
    // average(5, 20);
    average(a, b);
    return 0;
}

// Functions with argument and with return