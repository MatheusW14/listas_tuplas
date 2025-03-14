"""
Uma escola está organizando os dados dos alunos para criar um relatório resumido.
Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre.
"""

dados = input(
    "Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: "
).split(", ")

for i in range(0, len(dados), 3):
    nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")
