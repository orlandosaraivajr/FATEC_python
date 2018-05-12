#!/usr/bin/env python

arquivo = open('nomes.txt', 'r')
lista = []
for line in arquivo:
    line = line.replace('\n', '')
    lista.append(line.upper())
arquivo.close()

arquivo = open('nomeSeparado.txt', 'w')
for nome in lista:
    nome_separados = list(nome)
    for letra in nome_separados:
        arquivo.write(" | ")
        arquivo.write(letra)
    arquivo.write(" | \n")
arquivo.close()
