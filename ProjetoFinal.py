produtos = []
atualizacoes =("Terminar", "Nome", "Preço", "Quantidade")
selecoes = ("Sair", "Cadastrar produto", "Listar produtos", "Atualizar produto", "Excluir produto")
def cadastrar_item():
  while True:
    nome = str(input("insira o nome do produto: "))
    if not nome:
      print("Erro! O espaço do nome não pode ser deixado em branco. Por favor, tente novamente.")
    elif nome in produtos:
      print("Erro! Produto já existe no estoque. Por favor, escolha um nome diferente.")
    else:
      break
  while True:
    preco= float(input("Insira o preço do seu produto: "))
    if not preco:
      print("Erro! O espaço do preço não pode ser deixado em branco. Por favor, tente novamente.")
    elif preco<0:
      print("Erro! O preço não pode ser menor que zero. Por favor, tente novamente.")
    else:
      break
  while True:
    estoque= int(input("Insira a quantia do seu produto: ")
    if not estoque:
      print("Erro! O espaço do estoque não pode ser deixado em branco. Por favor, tente novamente.")
    elif estoque<0:
      print("Erro! O estoque não pode ser menor que zero. Por favor, tente novamente.")
    else:
      break  
   produto = {
     "nome": nome,
     "preco": preco,
     "estoque": estoque
   }
   produtos.append(produto)
   print("Produto adicionado com sucesso!")

def listar_items():
  if not produtos:
        print("Nenhum produto disponível.")
    else:
        print("\n--- Lista de Produtos ---")
        for produto in produtos: 
            print(f" Nome: {produto['nome']}, Preço: {produto['preco']:.2f}, Quantia: {produto['quantidade']}")
        print("--------------------\n")

def atualizar_item():
  while True:
        nome_buscar = input("Digite código de produto para atualizar: ")
        if not nome_buscar:
            print("Erro: Espaço do código não pode estar vazio. Por favor tente de novo.")
        else:
            break
  achado= False
  for produto in produtos:
    if produto["nome"] == nome_buscar:
      print(f"Atualizando: {produto['nome']}")
      print("//////Escolha a Atualização\\\\\\")
      for i, atualizacao in enumerate(atualizacoes):
        print(f"{i}. {atualizacao}")
        alternativa = input("Escolha uma atualização: ")
        if alternativa == '1':
          while True:
            nome = input("Digite novo nome: ")
            if not nome:
              print("Erro: Nome do produto não pode estar vazio. Por favor tente de novo.")
            else:
              print("Produto atualizado com sucesso!")
              break
            produto["nome"] = nome
        elif alternativa == '2':
          while True:
            preco = float(input("Digite o preço do produto."))
            if not preco:
              print("Erro: Espaço do preço não pode estar vazio. Por favor tente de novo.")
            elif preco < 0:
              print("Erro: Preço não pode ser negativo. Por favor tente de novo")
            else:
              print("Produto atualizado com sucesso!")
              break
            produto["preco"] = preco
        elif alternativa == '3':
          while True:
            estoque = int(input("Digite estoque do produto: "))
            if not estoque:
              print("Erro! Espaço de estoque não pode estar vazio. Por favor tente de novo.")
            elif estoque < 0:
              print("Erro! Estoque não pode ser negativo. Por favor tente de novo.")
            else:
              print("Produto atualizado com sucesso!")
              break
            produto["estoque"] = estoque
        elif alternativa == '0':
          print("Terminando processo de atualização.")
          achado = True
          break
        else:
          print("Por favor insira um número disponível")
          
def remover_item():
  while True:
    nome_deletar = input("Digite o nome de produto para deletar: ")
    if not nome_deletar:
      print("Erro! Espaço do nome não pode estar vazio. Por favor tente de novo.")
        else:
            break
  achado = False
    for i, produto in enumerate(produtos):
        if produto["nome"] == nome_deletar:
            del produtos[i]
            produtos.remove(nome_deletar)
            print("Produto deletado com sucesso!")
            achado = True
            break
    if not achado:
        print("Produto não foi encontrado.")
      
def menu():
  while True:
    print("//////MENU PRINCIPAL\\\\\\")
    for i, selecao in enumerate(selecoes):
      print(f"{i}. {selecao}")

    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
      cadastrar_item()
    elif opcao == '2':
      listar_items()
    elif opcao == '3':
      atualizar_item()
    elif opcao == '4':
      remover_item()
    elif opcao == '0':
      print("Finalizando o sistema.")
      break
      
    else:
      print("Por favor, escolha uma das opções listadas.")
