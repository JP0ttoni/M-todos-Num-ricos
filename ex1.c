#include <stdio.h>
#include <math.h>
#include <string.h>

char questao = 'a';

double funcao(double x);
double solve(char metodo[], double erroAb, double ini, double ini2);

int main()
{
    double erro, a, b, result;
    char metodos[10];
    printf("digite a letra da questao: ");
    scanf("%c", &questao);
    printf("parametros: ");
    scanf("%s %lf %lf %lf", metodos, &erro, &a, &b);
    result = (solve(metodos, erro, a, b));
    printf("resultado: %lf", result);
}

double solve(char metodo[], double erroAb, double ini, double ini2)
{
    if(strcmp(metodo, "bs") == 0)
    {
        printf("entrou em bs\n");
        double x0 = ini;
        double x1 = ini2, temp1, temp2;

        while(fabs(x1 - x0) > erroAb)
        {
            x0 = x1;
            x1 = (ini + ini2)/2;
            printf("valores: %lf %lf\n", x0, x1);
            if(funcao(x1) * funcao(ini) < 0)
            {
                ini2 = x1;
            }else{
                ini = x1;
            }

        }
            printf("valores depois: %lf %lf\n", x0, x1);

        return x0;
    }

    if(strcmp(metodo, "sec") == 0)
    {
        printf("entrou em sec\n");
        double EA = 1, x[1000];
        x[0] = ini;
        x[1] = ini2;
        int i;
        for (i = 1;EA > erroAb;i++)
        {
            x[i + 1] = ((x[i - 1] * funcao(x[i])) - (x[i] * funcao(x[i - 1])))/(funcao(x[i]) - funcao(x[i - 1]));
            EA = fabs(x[1] - x[0]);
            x[0] = x[1];
        }

        return x[i];
    }

    return 0.0;
}

double funcao(double x)
{
    if(questao == 'a')
    {
        printf("entrou a: %lf\n", pow(x, 5) - pow(2 * x, 4) - pow(9 * x, 3) + pow(22 * x, 2) + (4 * x) - 24);
        return pow(x, 5) - pow(2 * x, 4) - pow(9 * x, 3) + pow(22 * x, 2) + (4 * x) - 24;
    }

    if(questao == 'b')
    {
        printf("entrou b: %lf\n", cos(x) - sqrt(x));
        return cos(x) - sqrt(x);
    }

    if(questao == 'c')
    {
        printf("entrou c: %lf\n", ((sqrt(x) - 5) * exp(-x)));
        return ((sqrt(x) - 5) * exp(-x));
    }

    return 0.0;
}