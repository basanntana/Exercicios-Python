def inserir():
    codigo = input().split()
    return codigo

# adicionar: inclui o código de um novo produto à lista;
def adicionar(var):
    listaCodigos.append(var)

# remover: remove o código de um produto da lista;
def remover(var):
    validar = var in listaCodigos
    if validar == True: listaCodigos.remove(var)
    else: print(f'código {var} não encontrado')

# exibir: exibe os itens da lista em ordem crescente;
def exibir(lista):
    lista = sorted(list(map(int, lista)))
    print(*lista)
    return lista

# encerrar: exibe os itens da lista, assim como no 
# comando exibir, em ordem crescente, e encerra o programa.

listaCodigos = input().split()
decisao = inserir()

while decisao[0] != 'encerrar':
    if decisao[0] == 'adicionar':
        adicionar(int(decisao[1]))
    elif decisao[0] == 'remover': 
        remover(int(decisao[1]))
    elif decisao[0] == 'exibir': 
        listaCodigos = exibir(listaCodigos)
    decisao = inserir()

listaCodigos = exibir(listaCodigos)
