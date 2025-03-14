"""
A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma.
Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber se a turma está indo bem.
"""

notas = input("Digite as notas dos alunos separadas por vírgula: ").split(",")

notas = [float(nota) for nota in notas]
media = sum(notas) / len(notas)
print(f"Média final da turma: {media:.2f}")
