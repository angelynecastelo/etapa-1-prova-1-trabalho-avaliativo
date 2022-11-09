class Professor:
    def __init__(self,nome,matricula,subarea,campus_atual,campus_removido,tempo_de_ifce,idade,nota_concurso):
        self.__nome = nome
        # nome,
        self.__matricula = matricula
        # matricula 
        self.__subarea = subarea
        # subarea
        self.__campus_atual = campus_atual
        # campus_atual
        self.__campus_removido = campus_removido
        # campus_removido
        self.__tempo_de_ifce = tempo_de_ifce
        # tempo_de_ifce
        self.__idade = idade
        # idade,
        self.__nota_concurso = nota_concurso
        # nota_concurso
        
    def tempo_de_ifce(self):
        return self.__tempo_de_ifce
    
    def nome(self):
        return self.__nome
        
    def __str__(self):
        return self.__nome