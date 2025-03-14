"""
Camila adora receber amigos para jantares temáticos.
Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados.
Camila quer adicionar novos nomes e organizá-los em posições específicas.
"""

convidados = ["Ana", "Pedro", "Carlos"]
print(f"lista atual de convidados: {convidados}")

convidado = input("Digite o nome do novo convidado: ")
posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))

convidados.insert(posicao, convidado)
print(f"Lista atualizada de convidados: {convidados}")
