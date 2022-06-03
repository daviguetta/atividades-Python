from statistics import mean, pstdev, pvariance


nota = []

for i in range(20):
    nota.append(int(input('Qual a sua nota: ')))

mediaNotas = mean(nota)
desvioPadrao = pstdev(nota)
varianciaNota = pvariance(nota)
print(f'Media de notas: {mediaNotas}')
print(f'Desvio Padrão das notas: {desvioPadrao}')
print(f'Variância das notas: {varianciaNota}')