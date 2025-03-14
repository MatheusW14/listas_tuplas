"""
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes.
Mas, um erro foi identificado: um dos nomes está incorreto.
O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.
"""

participantes = ["Ana", "João", "Pedro"]
print(f"Participantes: {participantes}")

nome_incorreto = input("Digite o nome incorreto: ")
novo = input("Digite o nome correto: ")

indice = participantes.index(nome_incorreto)

participantes.remove(nome_incorreto)
participantes.insert(indice, novo)

print(f"O nome {nome_incorreto} foi substituído por {novo}.")
print(f"Lista atualizada: {participantes}")
