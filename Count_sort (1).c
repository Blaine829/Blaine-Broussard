
#include <stdio.h>
#include <omp.h>
#include <sched.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

void Count_sort(int a[], int n,int threads) {
    int i, j, k, l, count;
    int* temp = malloc(n*sizeof(int));
    #pragma omp parallel for num_threads(threads) default(none) shared(n,temp,a) private(i,j,count)
    for (i = 0; i < n; i++) {
        count = 0;
        for (j = 0; j < n; j++){
            if (a[j] < a[i]) {
                count++;
            } else if (a[j] == a[i] && j < i){
                 count++;
            }
//          printf("\nWorking on %d on thread %d", j, omp_get_thread_num());
        }
        temp[count] = a[i];
    }
    #pragma omp parallel for num_threads(threads) default(none) shared(n,a,temp) private(k)
    for (k = 0; k <= n; k++){
        a[k] = temp[k];
    }
    for (l = 0; l < n; l++){
        printf("\n%d", temp[l]);
    }

    free(temp);
}
int main(int argc, char *argv[]) {
    int t = 1;
    int n = 100;
    if (argc == 3) {
        if (strcmp(argv[1], "-t") == 0) {
            t = strtol(argv[2], NULL, 10);

        }
        if (strcmp(argv[1], "-n") == 0) {
            n = strtol(argv[2], NULL, 10);
        }
    } else if (argc == 5) {
        if (strcmp(argv[1], "-t") == 0) {
            t = strtol(argv[2], NULL, 10);

        }
        if (strcmp(argv[1], "-n") == 0) {
            n = strtol(argv[2], NULL, 10);
        }
        if (strcmp(argv[3], "-n") == 0) {
            n = strtol(argv[4], NULL, 10);
        }
        if (strcmp(argv[3], "-t") == 0) {
            t = strtol(argv[4], NULL, 10);
        }
    }
    int rand_array[n];
    int c;
    for (c = 0; c < n; c++){
        rand_array[c] = rand();
    }

    Count_sort(rand_array,n,t);
    return 0;
}

