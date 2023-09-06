#include <stdio.h>
#include <string.h>

void reverseWords(char *s) {
    int n;
    int i, j;
    char c;

    n = strlen(s);

    // reverse by char
    for (i = 0; i < n / 2; i++) {
        c = s[i];
        s[i] = s[n - i-1];
        s[n - i-1] = c;
    }

    // reverse by word
    int start = 0;
    int end = 0;
    for (j = 0; j <= n ; j++) {
        if (s[j] == ' ' || j == n) {
            if (s[j] == ' ') end = j - 1;
            else end = j - 1;
            for (i = 0; i <= (end - start) / 2; i++) {
                c = s[start + i];
                s[start + i] = s[end - i];
                s[end - i] = c;
            }
            start = j + 1;
        }
    }
}

int main()
{
    char s[] = "This is an example for debugging practice";

    printf("before: %s\n", s);
    reverseWords(s);
    printf("after: %s\n", s);
    printf("correct result is: \'%s\'\n", "practice debugging for example an is This");
}
