#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*

Created by CyberCoral
Version Tue/02/Jan/2024

-----------------
Github:
https://github.com/CyberCoral
-----------------
*/

/* A structure simulating complex numbers */
struct complex_reduced{
    long double real;
    long double imag;
};

/* Modular arithmetic functions */

double real_mod(double a, double b){

    double variable[1];

    double a1 = a;
    double b1 = b;

    if (b1 == 0){
        printf("\nb1 cannot be zero.");
        exit(1);
    };

    double f1 = (a1 / b1 - floor( a1 / b1 )) * b1;
    variable[0] = f1;

    return *variable;
};

double one_mod(double a){

    double one_module[1];

    double a1 = a;

    one_module[0] = a1 - floor(a1);

    return *one_module;
};

int floor0(double a){
    int floor = a - one_mod(a);
    return floor;
};

double* complex_mod(double a[2], double b[2]){

    //double complex_module[2];
    double* complex_module = malloc(16);

    double a1 = a[0];
    double a2 = a[1];
    double b1 = b[0];
    double b2 = b[1];
    double dem = pow(b1,2) + pow(b2,2);
    double c_dem = pow(b1,2) - pow(b2,2);

    if(dem == 0){
        printf("\nThe denominator cannot be zero.");
        exit(1);
    };

    double f1 = floor(((a1 * b1) + (a2 * b2)) / dem);
    double f2 = floor(((a1 * b2) - (b1 * a2)) / dem);
    double g1 = (a1 * c_dem - (2 * a2 * b1 * b2)) / dem;
    double g2 = (a2 * c_dem - (2 * a1 * b1 * b2)) / dem;

    complex_module[0] = g1 - (f1 * b1) + (f2 * b2);
    complex_module[1] = g2 + (f2 * b2) + (f1 * b1);

    return complex_module;

};

double* MOD(double a[2], double* r_arr, double* i_arr){
    double* arr = malloc(16);
    arr[0] = a[0];
    arr[1] = a[1];

    double check[2];
    check[0] = sizeof(r_arr) / sizeof(r_arr[0]);
    check[1] = sizeof(i_arr) / sizeof(i_arr[0]);

    if(check[0] != check[1]){
        printf("\nr_arr and i_arr do not have the same number of elements.\n");
        exit(1);
    };

    double next[2];
    next[0] = r_arr[0];
    next[1] = i_arr[0];

    arr[0] = complex_mod(arr,next)[0];
    arr[1] = complex_mod(arr,next)[1];

    for (int i=1;i<check[0];i++){
        next[0] = r_arr[i];
        next[1] = i_arr[i];

        arr[0] = complex_mod(arr,next)[0];
        arr[1] = complex_mod(arr,next)[1];
    };
    return arr;
};

/*You gotta start out of something :) */


int example(void){

    printf("Some examples of modular arithmetic operations:\n");

    double x = 45;
    double y = 999;

    double a = real_mod(x,y);

    printf("\nreal mod: ");
    printf("%lf",a);

    double z = 5.4321;

    int z0 = floor0(z);

    double b = one_mod(z);

    printf("\none_mod: ");
    printf("%lf",b);

    printf("\nfloor function: ");
    printf("%i",z0);

    double a1[2];
    a1[0] = 1;
    a1[1] = 1;

    double a2[2];
    a2[0] = 2;
    a2[1] = 2;

    double* c;
    c = complex_mod(a1,a2);

    printf("\ncomplex_mod: ");
    printf("%lf%+lfi", c[0],c[1]);

    free(c);

    double r_arr[1] = {1};
    double i_arr[1] = {0};

    double comp[2] = {4,5};

    double* d = MOD(comp, r_arr,i_arr);

    printf("\ncomplex_MOD: ");
    printf("%lf%+lfi", d[0],d[1]);

    free(d);

    printf("\nThe program finished successfully :D");

    return 0;

}

int main(){
    example();
    // Pause till enter is pressed.
    getchar();
};
