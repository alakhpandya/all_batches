#include<stdio.h>
#define SIZE 5
void main(){

    int a[SIZE],i,sum=0,oddSum=0,evenSum=0,oddCount=0,evenCount=0;

    for(i=0;i<SIZE;i++){
        printf("Enter number");
        scanf("%d",&a[i]);//a[0]
    }

    for(i=0;i<SIZE;i++){
        printf("\n%d",a[i]);

        //sum of all the elements in an array
        sum = sum  + a[i];

        if(a[i]%2 == 0){
            evenSum += a[i];
            evenCount++;
        }else{
            oddSum += a[i];
            oddCount++;
        }
    }

    printf("\nSum = %d",sum);
    printf("\nEvenSum = %d",evenSum);
    printf("\nOddSum = %d",oddSum);
    printf("\nTotalOddNumbers = %d",oddCount);
    printf("\nTotalEvenNumbers = %d",evenCount);



}
