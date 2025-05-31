// Write a program that gives choice to user whether they want to add, subtract, multiply or divide two complex numbers.

#include<stdio.h>
#include<math.h>

struct complex{
    float img, real;
};

struct complex scanComplex(){
    struct complex c;
    printf("Real part: ");
    scanf("%f", &c.real);
    printf("Imaginary part: ");
    scanf("%f", &c.img);
    return c;
}

struct complex addComplex(struct complex n1, struct complex n2){
    struct complex sum;
    sum.real = n1.real + n2.real;
    sum.img = n1.img + n2.img;
    return sum;
}

struct complex subComplex(struct complex n1, struct complex n2){
    struct complex diff;
    diff.real = n1.real - n2.real;
    diff.img = n1.img - n2.img;
    return diff;
}

struct complex multiplyComplex(struct complex n1, struct complex n2){
    struct complex product;
    /*
    n1 = r1 + c1*i
    n1 * n2 = (r1 + c1i) * (r2 + c2i)
            = r1r2 + r1c2i + r2c1i + c1c2i*i
            = r1r2 + (r1c2 + r2c1)i - c1c2
            = (r1r2 - c1c2) + (r1c2 + r2c1)i
    */
    product.real = n1.real*n2.real - n1.img*n2.img;
    product.img = n1.real*n2.img + n2.real*n1.img;
    return product;
}

struct complex divideComplex(struct complex n1, struct complex n2){
    struct complex division, temp;
    /*
              r1 + c1 * i       (r2 - c2 * i)
    n1 / n2 = ------------  X   -------------
              (r2 + c2 * i)     (r2 - c2 * i)

             (r1 + c1 * i) * (r2 - c2 * i)
            ------------------------------
                   (r2)^2 - (c2*i)^2

            r1r2 - r1c2 i + r2c1 i + c1c2
            ------------------------------
                    (r2)^2 + (c2)^2

            (r1r2 + c1c2) + (r2c1 - r1c2)i
            ------------------------------
                    (r2)^2 + (c2)^2

            (r1r2 + c1c2)           (r2c1 - r1c2)
            ---------------     +   --------------- * i
            (r2)^2 + (c2)^2         (r2)^2 + (c2)^2
    */
    division.real = (n1.real*n2.real + n1.img*n2.img) / (pow(n2.real, 2) + pow(n2.img, 2));
    division.img = (n2.real*n1.img - n1.real*n2.img) / (pow(n2.real, 2) + pow(n2.img, 2));
    return division;
}

int main()
{
    struct complex c1, c2, ans;
    char choice;
    printf("Enter complex no-1:\n");
    c1 = scanComplex();
    printf("\nEnter complex no-2:\n");
    c2 = scanComplex();
    printf("Enter operation: +, -, * or / : ");
    scanf(" %c", &choice);
    switch(choice){
        case '+':
            ans = addComplex(c1, c2);
            break;
        case '-':
            ans = subComplex(c1, c2);
            break;
        case '*':
            ans = multiplyComplex(c1, c2);
            break;
        case '/':
            ans = divideComplex(c1, c2);
            break;
        default:
            printf("Invalid operation, please try again...");
    }
    printf("Answer = %.3f + (%.3f)i", ans.real, ans.img);
    return 0;
}