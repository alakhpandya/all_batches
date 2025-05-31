#include<stdio.h>
struct complex
{
    int real;
    int imag;
};
struct complex scanComplex()
{
    struct complex c;
    printf("Real part: ");
    scanf("%d", &c.real);
    printf("Imaginary part: ");
    scanf("%d", &c.imag);
    return c;
}
struct complex summation(struct complex num1, struct complex num2)
{
    struct complex addition;
    addition.real = num1.real + num2.real;
    addition.imag = num1.imag + num2.imag;
    return addition;
}

struct complex diff(struct complex num1, struct complex num2)
{
    struct complex subtrction;
    subtrction.real = num1.real - num2.real;
    subtrction.imag = num1.imag - num2.imag;
    return subtrction;
}

struct complex multiply(struct complex num1, struct complex num2)
{
    struct complex mul;
    mul.real = (num1.real * num2.real) - (num1.imag * num2.imag);
    mul.imag = (num1.real * num2.imag) + (num2.real * num1.imag);
    return mul;
}

void printComplex(struct complex number)
{
    printf("\n%d + %di", number.real, number.imag);
}

int main()
{
    struct complex c1, c2, sum, difference, product;
    printf("Please enter first complex number:\n");
    c1 = scanComplex();
    printf("\nPlease enter second complex number:\n");
    c2 = scanComplex();
    sum = summation(c1, c2);
    difference = diff(c1, c2);
    product = multiply(c1, c2);
    printComplex(c1);
    printf(" + ");
    printComplex(c2);
    printf(" = ");
    printComplex(sum);
    printf("\n");

    printComplex(c1);
    printf(" - ");
    printComplex(c2);
    printf(" = ");
    printComplex(difference);
    printf("\n");

    printComplex(c1);
    printf(" * ");
    printComplex(c2);
    printf(" = ");
    printComplex(product);
    printf("\n");
    return 0;
}

/*
r1 + i1j
r2 + i2j
add: (r1 + r2) + (i1 + i2)j
sub: (r1 + i1j) - (r2 + i2j) = (r1 - r2) + (i1 - i2)j
mul: (r1 + i1j) * (r2 + i2j)
 = r1r2 + r1i2 j + r2i1 j - i1i2
 = (r1r2 - i1i2) + (r1i2 + r2i1) j
*/