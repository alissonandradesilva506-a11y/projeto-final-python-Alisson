produtos = []
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
