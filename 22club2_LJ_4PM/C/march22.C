// Take 4 integers p,q,r & s from user. print the total of average of p-q and average of r-s on the screen.
#include<stdio.h>
/*
float average(float a, float b){
    float avg;
    avg = (a + b)/2;
    // printf("Average of %.3f and %.3f = %.3f\n", a, b, avg);
    return avg;
}

int main()
{
    int p, q, r, s;
    float sum;
    printf("Enter 4 integers:\n");
    scanf("%d%d%d%d", &p, &q, &r, &s);
    sum = average(p, q) + average(r, s);
    printf("Final answer = %.3f", sum);
    return 0;
}
*/

// Write a function that checks whether an integer given in its argument is prime or not. Write a main program that asks an integer from user and prints whether it is a prime number or composite.

// Ask two integers from user and print all the prime numbers between them (including both).

int primeCheck(int n){
    int i;
    if(n < 2){
        return 0;
    }
    for(i = 2; i <= n/2; i++){
        if (n % i == 0){
            return 0;
        }
    }
    return 1;
}

int main(){
    int num, lower, upper;
    /*
    printf("Enter n: ");
    scanf("%d", &num);

    if (primeCheck(num) == 1){
        printf("Prime.");
    }
    else{
        printf("Composite.");
    }
    */
    printf("lower limit: ");
    scanf("%d", &lower);
    printf("upper limit: ");
    scanf("%d", &upper);
    for(num = lower; num <= upper; num++){
        if (primeCheck(num)){
            printf("%d\t", num);
        }
    }
    return 0;
}

/*
Functions Examples:
1. Ask two integers from user, add their factroials. Now ask two more integers from user and add their factorials too. calculate average of the factorials you computed. Now finally ask one last integer from user and add its factorial to the average.

2. Write a function that prints whether the number passed in its argument is prime or not. Using a main program pass the number given by the user to that function.

3. Write a function to find average of 5 given numbers and a main program that takes 5 integers from user, uses the factorial function to find factorial of each one of them and using average function prints the average of factorials of them.

4. Make a program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
    ap:
    first term = a = 5
    difference = d = 4
    ap = 5, 9, 13, 17, 21, 25,...
    nth term = a + (n-1)d

5. Develop a program that uses a function to find nth term of an geometric progression whose first term is 'a' & common ratio is 'r'.

6. Make a function that checks whether the given number is a perfect number or not. Make a program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.

7. Write a function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and print all the Prime numbers between those two integers using that function.

8. Write a function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.

*/