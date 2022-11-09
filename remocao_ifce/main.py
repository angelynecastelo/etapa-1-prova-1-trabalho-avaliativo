from professor import Professor
from fila_de_prioridade import Fila

p1=Professor('maria', 100, 'redes', 'cedro', 'jaguaribe', 900, 45, 7.5)
p2=Professor('joao', 10, 'redes', 'cedro', 'jaguaribe', 1000, 45, 7.5)
p3=Professor('mvila', 1, 'redes', 'cedro', 'jaguaribe', 9008, 49, 7.5)
p4=Professor('arrozino', 109, 'redes', 'cedro', 'jaguaribe', 10800, 45, 7.5)
fila=Fila()
fila.push(p1)
fila.push(p2)
fila.push(p3)
fila.push(p4)
print(fila)
print(fila.empty())

#o codigo não roda 100%



# Nessa nova estrutura você deverá ordenar professor. A entidade professor deve conter os seguintes atributos.
# nome,
# matricula (matrícula do docente no IFCE - inteiro),
# subarea (Metodologia e Técnicas de Computação, Sistemas de Computação, etc - String),
# campus_atual (Jaguaribe, Cedro, Canindé, etc. - String),
# campus_removido (Jaguaribe, Cedro, Canindé, etc. - String),
# tempo_de_ifce (157, 756, 873, etc - dias - inteiro),
# idade,
# nota_concurso

# A Fila de Prioridades a ser implementada deve priorizar objetos da classe professor pelo atributo tempo_de_ifce.

# Implemente os seguintes métodos na Fila de Prioridades:

# push(professor): insere de forma decrescente pela prioridade.
# pop(): remove o primeiro elemento.
# empty(): verifica se a Fila está vazia.
# __str__(): imprime a Fila de Prioridade.

# Métodos adicionais (e relevantes) para a nova estrutura serão bem-vindos e recompensados.
