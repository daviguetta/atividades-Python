totalGenero = 0
totalIdade = 0
totalSalario = 0

for i in range(30):
    salario = int(input('Qual o seu salário: '))
    idade = int(input('Qual a sua idade: '))
    genero = input('Qual o seu gênero (Masculino – M ou Feminino – F): ')
    if genero == 'M':
        genero = 1
        totalSalario +=salario
        totalGenero +=genero
    else:
        totalSalario
    totalIdade +=idade
    
mediaSalariosMasculino = totalSalario / totalGenero
mediaIdades = totalIdade / 30
print(f'A media de salários é: {mediaSalariosMasculino}')
print(f'A media de idades é: {mediaIdades}')