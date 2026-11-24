# produtos/almoxarifado.py — a classe Almoxarifado guarda os produtos de uma unidade

class Almoxarifado:
    # Construtor: o almoxarifado nasce com o nome da unidade e sem produtos
    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []

    # Guarda um objeto Produto no fim da lista
    def adicionar(self, produto):
        self.produtos.append(produto)

    # Busca um produto pelo código
    def buscar(self, codigo):
        for p in self.produtos:
            if p.codigo == codigo:
                return p
        return None

    # Registra a entrada de produtos no estoque
    def entrada(self, codigo, qtd):
        p = self.buscar(codigo)

        if p is None:
            return False

        p.entrada(qtd)
        return True

    # Registra a saída de produtos do estoque
    def saida(self, codigo, qtd):
        p = self.buscar(codigo)

        if p is None:
            return False

        return p.saida(qtd)

    # Devolve uma lista de dicionários com todos os produtos
    def listar(self):
        lista = []

        for p in self.produtos:
            lista.append(p.listar_produtos())

        return lista

    # Devolve somente os produtos que precisam ser repostos
    def solicitacao_compra(self):
        lista = []

        for p in self.produtos:
            if p.situacao() != "OK":
                lista.append({
                    "codigo": p.codigo,
                    "nome": p.nome,
                    "situacao": p.situacao()
                })

        return lista

    # Calcula o valor total dos produtos em estoque
    def valor_estoque(self):
        total = 0

        for p in self.produtos:
            total = total + (p.quantidade * p.preco)

        return total

    # Devolve os dados completos do almoxarifado em um dicionário
    def para_dicionario(self):
        return {
            "unidade": self.unidade,
            "total_produtos": len(self.produtos),
            "produtos": self.listar()
        }