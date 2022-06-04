"""
Por ser uma linguagem de alto nível, ou seja, mais próxima à linguagem humana
que à linguagem de máquina como a linguage C, por exemplo, não há necessidade
de definir tipos nem tamanho para ser alocado em memória.
"""


def estrutura_de_contato(nome, sobrenome, telefone, email):
    # Função que retorna um `dict`
    # (dicionário: estrutura de dados nativa da linguagem Python)
    # É uma forma estruturar dados
    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "email": email,
        "telefone": telefone,
    }


def adicionar_contato(agenda, nome, sobrenome, telefone, email):
    # Supoe-se que `agenda` é do tipo `list` (lista, tipo nativo do python)
    # agenda é do tipo `list` que é um tipo mutável,
    # logo é um ponteiro para a memória ou
    # em outras palavras seria considerado passagem de parâmetro por referência
    # Os tipos `str` são passagem por valor pois são tipo imutáveis
    # então ao modificar internamente na função não vai modificá-la após a
    # execução da função

    # cria uma estrutura de contato
    contato = estrutura_de_contato(nome, sobrenome, telefone, email)

    # acrescenta o contato na agenda
    agenda.append(contato)

    # agenda é do tipo `list` que é um tipo mutável, logo funciona como
    # um ponteiro para a memória ou em outras linguagens seria considerado
    # passagem por referência
    # e o `return agenda` é desncessário, pois
    # a agenda já está modificada após acrescentado o item do contato
    return agenda


def remover_contato_pelo_indice(agenda, indice):
    # remove item pelo indice e retorna o `contato`
    return agenda.pop(indice)


def remover_contato_pelo_email(agenda, email_do_contato_para_remover):
    # remove item pelo indice e retorna o `contato`
    for contato in agenda:
        if contato['email'] == email_do_contato_para_remover:
            return agenda.remove(contato)


def listar_contatos(agenda):
    # Esta lista não está ordenada
    # enumerate() atribui um índice a cada item da lista
    for i, contato in enumerate(agenda):
        # print(contato)
        # ou
        print('-'*10)
        print(f'índice: {i}')
        print(f'Nome: {contato["nome"]}')
        print(f'Sobrenome: {contato["sobrenome"]}')
        print(f'📞 {contato["telefone"]}')
        print(f'📧 {contato["email"]}')


def cargar_dados_gravados_no_arquivo(arq):
    # Aqui depende de como o dado está gravado no arquivo
    # Em um arquivo .txt, exigirá algum caracter separador qualquer para
    # identificar os campos
    # Em um arquivo .jsonl praticamente fica na mesma estrutura que um
    # dicionário
    # Em um arquivo .csv fica em formato de `planilha`, ou seja,
    # os dados são tabulares, separado por `vírgula` (c = comma)
    caracter_separador = "#"
    agenda = []

    # tenta executar o conteúdo do bloco
    try:
        # abre o arquivo para leitura (r)
        with open(arq, "r") as fp:
            for row in fp.readlines():
                row = row.strip()
                nome, sobrenome, telefone, email = row.split(caracter_separador)
                adicionar_contato(agenda, nome, sobrenome, telefone, email)
    except IOError:
        # exceto se houve erro de I/O (entrada/saída)
        # nao faz nada se não existir o arquivo
        pass

    return agenda


def gravar_dados_no_arquivo(arq, agenda):
    # Aqui depende de como o dado está gravado no arquivo
    # Em um arquivo .txt, exigirá algum caracter separador qualquer para
    # identificar os campos
    # Em um arquivo .jsonl praticamente fica na mesma estrutura que um
    # dicionário
    # Em um arquivo .csv fica em formato de `planilha`, ou seja,
    # os dados são tabulares, separado por `vírgula` (c = comma)
    sep = "#"

    # abre o arquivo para escrita (write)
    with open(arq, "w") as fp:

        # itera (ou seja, passa por cada item) da agenda
        for contato in agenda:
            # este trecho monta uma `list` com os dados do contato
            partes_do_contato = [
                contato['nome'],
                contato['sobrenome'],
                contato['telefone'],
                contato['email']
            ]
            # para ser usado no join, que insere o caracter separador `sep`
            # entre cada item
            row = sep.join(partes_do_contato)

            # grava no arquivo (um contato por linha `\n` quebra a linha)
            fp.write(row + "\n")


def menu():
    arquivo = "agenda.txt"

    agenda = cargar_dados_gravados_no_arquivo(arquivo)

    while True:
        # loop infinito até alguma condição interrompa
        print(
            ""
            "***********************************"
            "Digite a opção correspondente:\n\n"
            "+ para adicionar\n"
            "- para remover contato pelo índice\n"
            "x para remover contato pelo email\n"
            "v para listar contatos\n"
            "f para finalizar o programa\n"
        )
        # a função `input` imprime texto e pega aquilo que o usuário digitar
        # que é um `str` (string ou cadeia de caracteres)
        # se desejável que seja de outro tipo, é necessário usar o tipo como
        # função para converter para o tipo correspondente
        # ex.: int(opcao) ou bool(opcao) ...
        opcao = input("Opção: ")
        if opcao == "+":
            nome = input("nome: ")
            sobrenome = input("sobrenome: ")
            telefone = input("telefone: ")
            email = input("email: ")
            adicionar_contato(agenda, nome, sobrenome, telefone, email)
        elif opcao == "v":
            listar_contatos(agenda)
        elif opcao == "f":
            # guardar os contatos em arquivo
            gravar_dados_no_arquivo(arquivo, agenda)

            print("Fim")
            # break interrompe o loop infinito
            break


if __name__ == '__main__':
    menu()
