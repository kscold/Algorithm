#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>


int q1(int S, int N, int skills[][100], int nskills[])
{
    // your code is here
    // ----------------------------------------------
    // ----------------------------------------------
}


void compare_output(char *, char *);

int main()
{
    // DO NOT EDIT main() function

    int K, S, N, result;
    int i, j, m;
    int skills[101][100], nskills[101];
    char line[1025], tmp[32], *s1;
    char *token;
    clock_t start_time, end_time;

    FILE *input;
    FILE *output;

    input = fopen("input.txt", "r");          // input data
    output = fopen("output.txt", "w");        // your answer

    start_time = clock();

    for(m=0; m<100; m++) nskills[m] = 0;

    fgets(line, 1024, input);
    sscanf(line, "%i", &K);
    for(i=0; i<K; i++) {
        fgets(line, 1024, input);
        sscanf(line, "%s %i %i", tmp, &S, &N);
        for(j=0; j<N; j++) {
            fgets(line, 1024, input);
            s1 = line;
            while(*s1 == ' ') s1++;
            while(s1[strlen(s1)-1] == ' ' || s1[strlen(s1)-1] == '\n' || s1[strlen(s1)-1] == '\r') s1[strlen(s1)-1] = '\0';
            for(m=0; m<100; m++) skills[j][m] = -1;
            m = 0;
            token = strtok(s1, " ");
            while(token != NULL) {
                skills[j][m] = atoi(token);
                token = strtok(NULL, " ");
                m = m + 1;
            }
            nskills[j] = m;
        }
        result = q1(S, N, skills, nskills);
        printf("%d\n", result);
        fprintf(output, "%d\n", result);
    }
    end_time = clock();

    // Checking answers
    fclose(input);
    fclose(output);
    printf("Elapsed time: %.2f seconds.\n", ((double) (end_time - start_time)) / CLOCKS_PER_SEC);
    compare_output("output.txt", "expected.txt");
}

void compare_output(char *file1, char *file2)
{
    FILE *f1 = fopen(file1, "r");
    FILE *f2 = fopen(file2, "r");
    char line1[10000], line2[10000];
    char *s1, *s2;
    int i = 1;
    int success = 1;

    while(!feof(f1) && !feof(f2)) {
        fgets(line1, 10000, f1);
        fgets(line2, 10000, f2);
        s1 = line1;
        s2 = line2;
        while(*s1 == ' ') s1++;
        while(s1[strlen(s1)-1] == ' ' || s1[strlen(s1)-1] == '\n' || s1[strlen(s1)-1] == '\r') s1[strlen(s1)-1] = '\0';
        while(*s2 == ' ') s2++;
        while(s2[strlen(s2)-1] == ' ' || s2[strlen(s2)-1] == '\n' || s2[strlen(s2)-1] == '\r') s2[strlen(s2)-1] = '\0';
        if (strcmp(s1, s2)) {
            printf("[%i] Wrong answer: Yours=\'%s\', Expected=\'%s\'\n", i, s1, s2);
            success = 0;
            break;
        }
        i++;
    }
    if (feof(f2) && success) printf("Success!\n");
    fclose(f1);
    fclose(f2);
}
