"""
Por ser uma linguagem de alto nível, ou seja, mais próxima à linguagem humana
que à linguagem de máquina como a linguage C, por exemplo, não há necessidade
de definir tipos nem tamanho para ser alocado em memória.
""" 


class Contato:
    # Classes é outra forma de estruturar dados
    def __init__(self, nome, sobrenome, telefone, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.email = email


