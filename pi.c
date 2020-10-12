#include <stdio.h>
#include <omp.h>
#include <sched.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int n = 30;
    int i;
    int t = 2;
    if (argc == 3){
        if (strcmp(argv[1], "-t") == 0) {
            t = strtol(argv[2], NULL, 10);

        }else if (strcmp(argv[1], "-n") == 0) {
            n = strtol(argv[2], NULL, 10);
        }
    }else if(argc == 5) {
        if (strcmp(argv[1], "-t") == 0) {
            t = strtol(argv[2], NULL, 10);

        }if (strcmp(argv[1], "-n") == 0) {
            n = strtol(argv[2], NULL, 10);
        }if (strcmp(argv[3], "-n") == 0) {
            n = strtol(argv[4], NULL, 10);
        }if (strcmp(argv[3], "-t") == 0) {
            t = strtol(argv[4], NULL, 10);
        }
    }
    double sum = 0;
    double calc1 = 0;
    double calc2 = 0;
    #pragma omp parallel for num_threads(t) default(none) shared(n,sum) private(i,calc1,calc2)
    for (i=0; i <= n; i++) {
        calc1 = (pow(-1, i));
        calc2 = ((2 * i) + 1);
        #pragma omp critical
        sum = sum + (calc1/calc2);
        printf("\nCurrent sum is %f working on thread %d", sum, omp_get_thread_num());
    }
    sum = sum*4;
    printf("\nInputs are %s %d, number of inputs is:%d ",argv[1],strtol(argv[2],NULL,10),argc);
    printf("\nThreads are %d", t);
    printf("\nIterations is %d",n);
    printf("\nApproximation is %f", sum);
    return 0;

}
