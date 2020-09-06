from Disciplina import Disciplina
import Dados

erro = 'Nem ideia do que isso significa!'
creditos_disciplinas = []
dados_por_linha = Dados.importar_arquivo('exemplo1')
disciplinas_cadastradas = []

log_matematica = 4
eng_software = 6
teor_computacao = 3
banco_dados = 6
arq_software = 4

creditos_disciplinas.append(log_matematica)
creditos_disciplinas.append(eng_software)
creditos_disciplinas.append(teor_computacao)
creditos_disciplinas.append(banco_dados)
creditos_disciplinas.append(arq_software)

def total_creditos():
    total = sum(disciplinas)
    return total

def aprovacao(media):
    if media >= 5:
        return True
    return False

def check_disciplina(nome):
    for i,e in enumerate(disciplinas_cadastradas):
        if nome == e.get_nome():
            return e
    return None


for i,e in enumerate(dados_por_linha):
    nome = None
    p1 = None
    p2 = None
    media = None
    palavras = Dados.split_linha(dados_por_linha[i])
    tipo = Dados.definir_tipo(palavras)
    if tipo == 'disciplina':
        dados = Dados.se_disciplina(palavras)
        nome = dados[0]
        disciplina = check_disciplina(nome)
        if disciplina == None:
            if dados[1] == 'Media':
                media = dados[2]
            elif dados[1] == 'Prova1':
                p1 = dados[2]
            elif dados[1] == 'Prova2':
                p2 = dados[2]
            nova = Disciplina(nome, p1, p2, media)
            disciplinas_cadastradas.append(nova)
        else:
            if dados[1] == 'Media':
                disciplina.set_media(dados[2])
            elif dados[1] == 'Prova1':
                disciplina.set_prova1(dados[2])
            elif dados[1] == 'Prova2':
                disciplina.set_prova2(dados[2])  
    elif tipo == 'questao':
        pass
    
    
    
    
    # print(disciplinas_cadastradas)
    for i,disc in enumerate(disciplinas_cadastradas):
        print(i, disc.nome, disc.prova1, disc.prova2, disc.media)
        pass
    

    


#print(str(converter_para_eua(input('digite a nota: '))))
test = Disciplina('Logica matematica', 3, None, 5)
print(test.get_nome()+' - media: '+str(test.get_media())+' - prova1: '+str(test.get_prova1())+' - prova2: '+str(test.get_prova2()))
#print(test.get_prova2())

    