def calcular_media(p1, p2):
    media = (p1 + p2)/2
    return media

def calcular_prova2(p1, media):
    p2 = (2 * media) - p1
    return p2


class Disciplina:
    def __init__(self, nome, prova1=None, prova2=None, media=None):
        self.nome = nome
        self.prova1 = prova1
        self.prova2 = prova2
        self.media = media
        
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_prova1(self):
        return self.prova1
    
    def set_prova1(self, prova1):
        self.prova1 = prova1

    def get_prova2(self):
        return self.prova2

    def set_prova2(self, prova2):
        self.prova2 = prova2

    def get_media(self):
        return self.media

    def set_media(self, media):
        self.media = media

    def atualizar_prova1(self, p1):
        prova1 = p1
        if prova1 != None:
            self.prova1 = prova1
        elif self.prova2 != None and self.media != None:
            self.prova1 = calcular_prova1(self.prova2, self.media)
        else:
            self.prova1 = None    

    def atualizar_prova2(self, p2):
        prova2 = p2
        if prova2 != None:
            self.prova2 = prova2
        elif self.prova1 != None and self.media != None:
            self.prova2 = calcular_prova2(self.prova1, self.media)
        else:
            self.prova2 = None
    
    def atualizar_media(self, m):
        media = m
        if media:
            self.media = media
        elif self.prova1 and self.prova2:
            self.media = calcular_media(self.prova1, self.prova2)
        else:
            self.media = None
    

    


    

    
