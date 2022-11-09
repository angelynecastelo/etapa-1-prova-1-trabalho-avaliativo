class Fila:
    def __init__(self):
        self.__fila_prioridade = []
        # self.professores_na_lista = 0

        

    def push(self,addprofessor):
        # if self.empty() == True:
        #     self.__fila_prioridade.append(addprofessor)
        #     self.professores_na_lista = self.professores_na_lista +1
        #     print(self.__fila_prioridade)
        # else:
        self.__fila_prioridade.sort(reverse = True)
        #organiza a fila de prioridade em ordem de decrescente
        for indice in range(0,len(self.__fila_prioridade)):
            #lê os indices da fila
            if self.__fila_prioridade[indice].tempo_de_ifce >= addprofessor.tempo_de_ifce:
                #compara para saber se o addprofessor é maior que indice para colocar no final da lista
                self.__fila_prioridade.append(addprofessor)
            else:
                self.__fila_de_prioridade.insert(indice)
                #coloca o addprofessor na posição que esta o indice
    def pop(self):
        self.__fila_prioridade.remove([0])
        #remove o primeiro da fila

    def empty(self):
        #encontra o tamanho da fila e retorna o resultado em buliano
        if len(self.__fila_prioridade) == 0:
            return True
        return False

    
    def __str__(self):
        #chama a função buliana e retorna os indices na lista de forma organizada
        if self.empty == True: 
            return '[]'
        ret = ', '.join(str(indice) for indice in self.__fila_prioridade) 
        return ret




    
# A Fila de Prioridades a ser implementada deve priorizar objetos da classe professor pelo atributo tempo_de_ifce.

# Implemente os seguintes métodos na Fila de Prioridades:

# push(professor): insere de forma decrescente pela prioridade.
# pop(): remove o primeiro elemento.
# empty(): verifica se a Fila está vazia.
# __str__(): imprime a Fila de Prioridade.

# Métodos adicionais (e relevantes) para a nova estrutura serão bem-vindos e recompensados.