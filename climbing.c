#include <stdio.h>

int main(void)
{
    int n;
    printf("Enter Number of steps: ");
    if (scanf("%d", &n) != 1)
    {
        printf("Invalid input\n");
        return 1 ;
    }

    if(n <= 0)
    {
        printf("wrong input\n");
        return 1;
    }

    int m = n / 2;
    int steps = 0;

    for (int i = 0; i < (m + 1); i++)
    {
        int a = i;
        int b = 1;
        int d = 1;
        int l = n;
        long product = 1;
        long product1 = 1;

        while (a > 0)
        {
            b++;
            a--;
        }

         while (l > 0)
        {
            product = product * b;
            product1 = product1 * d;
            d++;
            b++;
            l--;
        }

        int o = product / product1;
        steps = steps + o;
        n = n - 2;
    }

    printf("Number of ways: %i\n", steps);
    return 0;
}
