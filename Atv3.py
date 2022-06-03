listaCompetidores = []

def mediaPonderada(quimica, fisica):
    pesoQuimica = 4
    pesoFisica = 6
    formula = (quimica*pesoQuimica + fisica*pesoFisica) / pesoQuimica + pesoFisica
    return formula

for i in range (3):
    listaCompetidores.append(mediaPonderada(int(input('Qual a nota em Quimica: ')), int(input('Qual a nota em fisica: '))))
    if i < 2:
        print('Proximo Aluno')
    else:
        print('O resultado é ...')

mediaVencedora = max(listaCompetidores)
alunoVencedor = listaCompetidores.index(mediaVencedora)

if alunoVencedor == 0:
    print('O vencedor é o Aluno X')
elif alunoVencedor == 1:
    print('O vencedor é o Aluno Y')
else:
    print('O vencedor é o Aluno Z')

print(f'A media ponderada dos alunos - Aluno X: {listaCompetidores[0]}, Aluno Y: {listaCompetidores[1]} e Aluno Z: {listaCompetidores[2]}')