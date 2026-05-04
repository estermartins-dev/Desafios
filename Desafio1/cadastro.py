def cadastrar_produto(produtos):
   
    print("\n--- Cadastrar Produto ---")

    while True:
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("Erro: O nome não pode ser vazio.")
            continue
        if any(p["nome"].lower() == nome.lower() for p in produtos):
            print(f"Erro: Já existe um produto chamado '{nome}'. Escolha um nome diferente.")
            continue
        break

    while True:
        try:
            preco = float(input("Preço (R$): ").replace(",", "."))
            if preco <= 0:
                print("Erro: O preço deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Erro: Digite um valor numérico válido para o preço.")

    while True:
        try:
            estoque = int(input("Estoque inicial: "))
            if estoque < 0:
                print("Erro: O estoque não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Erro: O estoque deve ser um número inteiro.")

    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }
    produtos.append(produto)
    print(f"\nProduto '{nome}' cadastrado com sucesso!")
    return produtos


def listar_produtos(produtos):
   
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return False

    print("\n--- Produtos Disponíveis ---")
    for i, produto in enumerate(produtos, start=1):
        print(f"  {i}. {produto['nome']} - R$ {produto['preco']:.2f} - Estoque: {produto['estoque']}")
    return True


def atualizar_estoque(produtos):
    
    if not listar_produtos(produtos):
        return produtos

    while True:
        try:
            indice = int(input("\nDigite o número do produto para atualizar o estoque: ")) - 1
            if indice < 0 or indice >= len(produtos):
                print("Erro: Índice inválido. Tente novamente.")
                continue
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

    produto = produtos[indice]
    print(f"Produto selecionado: {produto['nome']} | Estoque atual: {produto['estoque']}")

    while True:
        try:
            novo_estoque = int(input("Novo estoque: "))
            if novo_estoque < 0:
                print("Erro: O estoque não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Erro: O estoque deve ser um número inteiro.")

    produto["estoque"] = novo_estoque
    print(f"Estoque de '{produto['nome']}' atualizado para {novo_estoque} unidades.")
    return produtos
