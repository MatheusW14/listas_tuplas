"""
Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.
Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa.
Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.
"""

dispensa = ["abacaxi", "banana", "arroz", "feijao"]

item = str(input("Digite o item que você quer verificar: "))


if item in dispensa:
    print(f"O item {item} esta na lista.")
else:
    print(f"O item {item} precisa ser comprado.")
print(dispensa)
