while True:
    produto = input('Digite o produto:')
    if produto =='':
        print('Digite um produto valido')
    else:
        break

categorias = ('Vestidos', 'Blusas', 'Conjuntos', 'Bolsas', 'Cintos')
print('categorias disponíveis: ', *categorias, sep='\n')

while True:

    categoria = input("Digite uma categoria: ").strip()

    if categoria in categorias:
        print(f"Sucesso! '{categoria}' é uma opção válida.")
        break

    print(f"Categoria inválida. Tente novamente com uma opção válida: presente ao lado {categorias}.\n")
else:
    pass

while True:
    qtde = input('Qual a quantidade atual do produto?')
    if qtde =='':
        print('Digite uma quantidade valida')
    else:
        break

if produto and categorias and qtde:
    qtde = int(qtde)
    if categoria == 'Vestidos':
        if qtde < 10:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(categoria, qtde))
    elif categoria == 'Blusas':
        if qtde < 30:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(categoria, qtde))
    elif categoria == 'Conjuntos':
        if qtde < 10:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(categoria, qtde))
    elif categoria == 'Bolsas':
        if qtde < 10:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(categoria, qtde))
    elif categoria == 'Cintos':
        if qtde < 10:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(categoria, qtde))
else:
    print('Não foi possível realizar a verificação de estoque, pois algum dos campos não foi preenchido corretamente.')

if qtde < 10 or categoria == 'Blusas' and qtde < 30:
    pass
else:
    print('estoque acima de {}, não será necessário realizar a compra de mais {}'.format(qtde, categoria))