estudante = {}  


for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    estudante[nome] = nota

soma = 0  


for nota in estudante.values():
    soma += nota

media = soma / len(estudante) 

print("A média das notas dos estudantes é:", media)