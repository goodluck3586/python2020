# 사용자로부터 정수를 입력받아 자릿수를 출력하시오.

#include <stdio.h>
int main() {
    long long n;
    int count = 0;
    printf("Enter an integer: ");
    scanf("%lld", &n);
 
    // iterate until n becomes 0
    // remove last digit from n in each iteration
    // increase count by 1 in each iteration
    while (n != 0) {
        n /= 10;     // n = n/10
        ++count;
    }

    printf("Number of digits: %d", count);
}

<Output>
Enter an integer: 3452
Number of digits: 4