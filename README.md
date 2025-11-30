# projeto-final-python-Alisson
# O projeto final do ano é um sistema de cadastro de produtos 
# Esse projeto possui cinco funções que permite o cadastro, listagem, atualização e remoção de items dentro de um dicionário
# A função principal é a função 'menu()' que permite o acesso de todas as outras funções 
# No menu a primeira opção é a opção de 'sair' que serve para desligar o sistema quando o usuário estiver terminado
# A segunda opção ativa a função 'cadastrar_item()'
# Essa função permite que o usuário insira um item em um dicionário
# Quando a função começa a rodar ela pede para o usuário digitar o nome, preço e o estoque desse item
# O sistema possui segurança para o usuario não inserir dados inválidos, como preço e estoque negativo
# Depois desses informações serem digitadas o sistema salva o item dentro da lista de 'produtos'
# A tercerira opção ativa a função 'listar_itens()'
# Essa função mostra a lista de itens salvos no programa
# A quarta opção ativa a função 'atualizar_item()'
# Essa função cria um sub-menu que permite a atualização dos dados de um item
# O usuário pode escolher entre alterar o nome, preço ou estoque de um item ou sair do sub-menu quando terminar
# A última opção ativa a função 'remover_item()'
# Essa função permite que o usuário remova um item da lista de produtos escrevendo o nome dele
# Esse sistema pode ser utilizado principlamente para listar os produtos de uma loja
# Com os dados de estoque também pode ser útil para determinar quais itens precisam ser reposto devido a estoque baixo
