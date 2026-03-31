class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


class Sistema:
    def __init__(self):
        self.db = []

    def cadastrar(self, nome, valor):
        # verificar duplicado
        for p in self.db:
            if p.nome == nome:
                print("Produto já cadastrado!")
                return
              
        
                
              

        novo = Produto(nome, valor)
        self.db.append(novo)
        print("Produto cadastrado!")

    def remover(self, nome):
        for p in self.db:
            if p.nome == nome:
                self.db.remove(p)
                print("Produto removido!")
                return
        
        print("Produto não encontrado!")

    def listar(self):
        for p in self.db:
            print(f"{p.nome} - R$ {p.valor}")

sistema = Sistema()

while True:
    op = int (input((f"\n====== MENU ======\n"
    "\n1 = Cadastrar Produto\n"
    "\n2 - Remover produto\n"
    "\n3 - Listar Produtos\n"
    "\n4 - Sair do Sistema\n" \
      "\nOque deseja fazer :  "
    )))
    if op == 1:
        
        nome = input ("digite o nome do produto: ")
        valor = float (input("digite o valor do produto: "))

        sistema.cadastrar(nome, valor)
    elif op == 2:
        nome = input("digite o produto que deseja remover: ")
        sistema.remover(nome)
    elif op == 3:
        sistema.listar()
    elif op == 4:
        break