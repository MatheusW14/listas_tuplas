"""
Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação.
À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.
"""

voluntarios = []

while True:
    voluntario = input("Digite o nome do voluntário (ou sair para encerrar): ")
    if voluntario.lower() == "sair":
        break
    voluntarios.append(voluntario)

print("\nVoluntários registrados:", voluntarios)
