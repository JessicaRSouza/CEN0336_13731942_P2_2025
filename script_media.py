#!/usr/bin/env python3

# Inicializamos com as duas variáveis zeradas, exatamente como no pseudocódigo.
total = 0
contador_notas = 0


# Loop que pede as notas. Na versão aqui descrita, são pedidas 10 notas, e o contador é incrementado, dois pontos que corrigem problemas do pseudocódigo, como discutido na prova.
while contador_notas < 10:  # No pseudocódigo, é escrito "while contador_notas <= 10:", o que geraria 11 inputs, trazendo um erro de cálculo de média mais à frente.

	nota = int(input("Insira a nota que deseja somar: "))  # Momento que o programa pede ao usuário uma nota. O input é convertido para int(), para possibilitar sua soma ao total.

	total += nota  # Momento em que o valor inserido é somado ao TOTAL, como previsto.

	contador_notas += 1  # Incremento em relação ao pseudocódigo. Sem ele, CONTADOR_NOTAS nunca mudaria e o loop seria infinito.


# Cálculo da média após término do loop.
media = total/10  # A divisão por 10 é mantida, pois foi ajustado o loop, que agora pede 10 notas, ao invés de 11.


# Exibição da média calculada.
print(media)
