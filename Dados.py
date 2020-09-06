min = 0.0
max = 0.0

def converter_para_br(conceito):
    if conceito.upper() == 'A':
        min = 9.0
        max = 10.0
        return max
    elif conceito.upper() == 'B':
        min = 7.0
        max = 8.9
        return max 
    elif conceito.upper() == 'C':
        min = 5.0
        max = 6.9
        return max   
    elif conceito.upper() == 'D':
        min= 3.0
        max = 4.9
        return max
    elif conceito.upper() == 'F':
        min= 0.0
        max = 2.9
        return max
    else:
        return 'Erro'

def converter_para_eua(nota):
    if 9 <= float(nota) <= 10:
        return 'A'
    elif 7 <= float(nota) < 9:
        return 'B'
    elif 5 <= float(nota) < 7:
        return 'C'
    elif 3 <= float(nota) < 5:
        return 'D'
    elif 0 <= float(nota) < 3:
        return 'F'
    else:
        return 'Erro'

def importar_arquivo(nome_arquivo):
    array_dados = []
    arquivo = open('./{}.txt'.format(nome_arquivo), 'r')
    for linha in arquivo:
        array_dados.append(linha)
    arquivo.close()
    return array_dados

def split_linha(linha):
    palavras = linha.rstrip().split(' ')
    return palavras

def definir_tipo(palavras):
    info = palavras
    if info[-2] in ('Media', 'Prova1', 'Prova2'):
        return 'disciplina'
    else:
        return 'questao'

def se_disciplina(lista):
    nota = converter_para_br(lista.pop())     
    tipo = lista.pop()
    nome = ''
    for x in lista:
        nome = nome+x+' '
    dados = [nome.strip(), tipo, nota]
    return dados

def se_pergunta(linha):
    if linha.lower().startswith('qual'):
        questoes.append(linha)




