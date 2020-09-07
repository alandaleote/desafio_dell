from Disciplina import Disciplina
import Dados

def total_creditos(disciplinas):
    total = 0
    for key, value in disciplinas.items():
        nome, cred = value
        total += cred
    return total

def creditos_inconcluidos(dicionario, lista):
    total = 0
    for i,e in enumerate(lista):
        if e.get_media() < 5:
            for key, value in dicionario.items():
                nome, cred = value
                if e.get_nome() == nome:
                    total += cred
    return total

def qual_disciplina(frase):
    for key, value in disciplinas_cursadas.items():
        nome, cred = value
        if nome in frase:
            return nome
    return None    

def reprovado(media):
    if media < 5:
        return True
    return False

def esta_cadastrada(nome):
    for i,e in enumerate(disciplinas_cadastradas):
        if nome == e.get_nome():
            return e
    return False

def adicionar_disciplina(dados, nome, p1, p2, media):
    if dados[1] == 'media':
        media = dados[2]
    elif dados[1] == 'prova1':
        p1 = dados[2]
    elif dados[1] == 'prova2':
        p2 = dados[2]
    nova = Disciplina(nome, p1, p2, media)
    disciplinas_cadastradas.append(nova)

def atualizar_disciplina(dados):
    if dados[1] == 'media':
        disciplina.set_media(dados[2])
    elif dados[1] == 'prova1':
        disciplina.set_prova1(dados[2])
    elif dados[1] == 'prova2':
        disciplina.set_prova2(dados[2])
    disciplina.atualizar_obj()


disciplinas_cursadas = {}
disciplinas_cursadas['logica'] = ['logica matematica', 4]
disciplinas_cursadas['engenharia'] = ['engenharia de software', 6]
disciplinas_cursadas['teoria'] = ['teoria da computacao', 3]
disciplinas_cursadas['banco'] = ['banco de dados', 6]
disciplinas_cursadas['arquitetura'] = ['arquitetura de software', 4]
erro = 'Nem ideia do que isso significa!'
disciplinas_cadastradas = []
lista_respostas = []
nome_arquivo = input('Digite o nome do arquivo: ')
lista_dados = Dados.importar_arquivo(nome_arquivo)

if lista_dados == 'erro':
    print('Erro, arquivo não encontrado')
else:
    for i,elem in enumerate(lista_dados):
        nome = None
        p1 = None
        p2 = None
        media = None
        palavras = Dados.split_linha(elem)
        tipo = Dados.definir_tipo(palavras)
        if tipo == 'disciplina':
            dados = Dados.se_disciplina(palavras)
            nome = dados[0]
            disciplina = esta_cadastrada(nome)
            if disciplina == False:
                adicionar_disciplina(dados, nome, p1, p2, media)
            else:
                atualizar_disciplina(dados)
    for i,elem in enumerate(lista_dados):
        nome = None
        p1 = None
        p2 = None
        media = None
        palavras = Dados.split_linha(elem)
        tipo = Dados.definir_tipo(palavras)
        if tipo == 'questao':
            resposta = ''
            frase = Dados.lista_to_string(palavras)
            nome = qual_disciplina(frase)
            obj_disciplina = esta_cadastrada(nome) 
            if 'quantos creditos' in frase:
                total = total_creditos(disciplinas_cursadas)
                if 'cursou' in frase:
                    resposta = ('No semestre cursei {} creditos'.format(total))  
                elif 'concluiu' in frase:
                    concluidos = total - creditos_inconcluidos(disciplinas_cursadas, disciplinas_cadastradas)
                    resposta = ('Conclui {} creditos'.format(concluidos))
                else:
                    resposta = erro
            elif 'voce foi aprovado' in frase:
                if 'todas' in frase:
                    reprovadas = ''
                    for i,e in enumerate(disciplinas_cadastradas):
                        if reprovado(e.get_media()):
                            reprovadas = reprovadas.join(e.get_nome().title()+'')
                    if reprovadas:
                        resposta = ('Não, fui reprovado em '+reprovadas)      
                else:
                    resposta = erro
            elif nome and obj_disciplina:
                if 'qual a media' in frase:
                    media = obj_disciplina.get_media()
                    resposta = ('A media em {} é {}'.format(nome.title(), round(media, 1)))
                elif 'qual a nota' in frase:
                    if 'preciso' or 'deve ser' not in frase:
                        if 'prova1' in frase:
                            prova1 = obj_disciplina.get_prova1()
                            resposta = ('A nota da prova1 em {} é {}'.format(nome.title(), round(prova1, 1)))
                        elif 'prova2' in frase:
                            prova2 = obj_disciplina.get_prova2()
                            resposta = ('A nota da prova2 em {} é {}'.format(nome.title(), round(prova2, 1)))
                        else:
                            resposta = erro 
            else:
                resposta = erro
            lista_respostas.append(resposta)
               
Dados.exportar_resultados(nome_arquivo, lista_respostas)