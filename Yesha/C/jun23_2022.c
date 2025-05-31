/*
Ask 20 numbers from user and store them in a file named "even.txt" if they are even, if they are odd, store them in "odd.txt" and if they are prime, store them in "prime.txt"
*/
/*
#include<stdio.h>
#define N 10

int primeCheck(int n){
    int i;
    if (n == 1){
        return 0;
    }
    for(i=2; i<n; i++){
        if (n % i == 0){
            return 0;
        }
    }
    return 1;
}

int main(){
    int i, a[N], even=0, odd=0, prime=0, b;
    FILE *f_even, *f_odd, *f_prime;
    f_even = fopen("even.txt", "w+");
    f_odd = fopen("odd.txt", "w+");
    f_prime = fopen("prime.txt", "w+");
    printf("Enter %d integers:\n", N);
    
    for(i=0; i<N; i++){
        scanf("%d", &a[i]);
    }

    for(i=0; i<N; i++){
        if (a[i] % 2 == 0){
            fprintf(f_even, "%d\n", a[i]);
            even++;
        }
        else{
            fprintf(f_odd, "%d\n", a[i]);
            odd++;
        }
        if (primeCheck(a[i])){
            fprintf(f_prime, "%d\n", a[i]);
            prime++;
        }
    }

    rewind(f_even);
    rewind(f_odd);
    rewind(f_prime);

    printf("\nContent of 'even.txt':-\n");
    for(i=0; i<even; i++){
        fscanf(f_even, "%d", &b);
        printf("%d\n", b);
    }
    
    printf("\nContent of 'odd.txt':-\n");
    for(i=0; i<odd; i++){
        fscanf(f_odd, "%d", &b);
        printf("%d\n", b);
    }

    printf("\nContent of 'prime.txt':-\n");
    for(i=0; i<prime; i++){
        fscanf(f_prime, "%d", &b);
        printf("%d\n", b);
    }

    fclose(f_even);
    fclose(f_odd);
    fclose(f_prime);
    return 0;
}
*/

#include<stdio.h>

#define N 10

int primeCheck(int n){
    int i;
    if (n == 1){
        return 0;
    }
    for(i=2; i<n; i++){
        if (n % i == 0){
            return 0;
        }
    }
    return 1;
}

int main(){
    int i, a[N];
    char b;
    FILE *f_even, *f_odd, *f_prime;
    f_even = fopen("even.txt", "a+");
    f_odd = fopen("odd.txt", "a+");
    f_prime = fopen("prime.txt", "a+");
    
    printf("Enter %d integers:\n", N);
    
    for(i=0; i<N; i++){
        scanf("%d", &a[i]);
    }

    for(i=0; i<N; i++){
        if (a[i] % 2 == 0){
            fprintf(f_even, "%d\n", a[i]);
        }
        else{
            fprintf(f_odd, "%d\n", a[i]);
        }
        if (primeCheck(a[i])){
            fprintf(f_prime, "%d\n", a[i]);
        }
    }

    rewind(f_even);
    rewind(f_odd);
    rewind(f_prime);

    /*
    b = fgetc(f_even);
    while (b != EOF){
        printf("%c", b);
        b = fgetc(f_even);
    }
    */
    printf("\nContent of 'even.txt':-\n");
    while ((b = fgetc(f_even)) != EOF){
        printf("%c", b);
    }

    printf("\nContent of 'odd.txt':-\n");
    while ((b = fgetc(f_odd)) != EOF){
        printf("%c", b);
    }

    printf("\nContent of 'prime.txt':-\n");
    while ((b = fgetc(f_prime)) != EOF){
        printf("%c", b);
    }


    fclose(f_even);
    fclose(f_odd);
    fclose(f_prime);
    return 0;
}