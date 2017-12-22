#include <stdio.h>
#include <stdlib.h>

typedef struct carro{
    int portas;
    char cor[50];
    float potencia;
}carro;

void main(){
    carro celta[3] = {
        {2, "vermelha", 1.0},
        {3, "azul", 1.2},
        {2, "verde", 1.9}
    };
    printf("\n%d, %s, %f\n", celta[1].portas, celta[2].cor, celta[2].potencia);
}
