from produto import Produto

#Ordenando lista de números no Python
numeros = [5,2,6,1,3,4,9,8]
numeros_ordenados = sorted(numeros)

print(numeros)
print(numeros_ordenados)

#Ordenando lista de strings no Python
palavras = ["pão","queijo","chocolate","bolo","tomate","biscoito", "cafe", "refrigerante","suco", "feijao","sal","arroz"]
palavras_ordenadas = sorted(palavras)

print(palavras)
print(palavras_ordenadas)

#Ordenando lista de objetos no Python

p1 = Produto("pão",0.60)
p2 = Produto("queijo",9.98)
p3 = Produto("chocolate",6.78)
p4 = Produto("bolo",11.56)
p5 = Produto("tomate",4.55)
p6 = Produto("biscoito",3.60)
p7 = Produto("cafe",10.35)
p8 = Produto("refrigerante",5.50)
p9 = Produto("suco",4.50)
p10 = Produto("feijão",7.50)
p11 = Produto("arroz",20.00)

produtos = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]

#Ordenado por valor
produtos_ordenados = sorted(produtos, key = Produto.get_valor)
print(produtos_ordenados)

#Ordenado por nome
produtos_ordenados = sorted(produtos, key = Produto.get_nome)
print(produtos_ordenados)

#reverso

produtos_ordenados = sorted(produtos, key = Produto.get_valor, reverse=True)
print(produtos_ordenados)

produtos_ordenados = sorted(produtos, key = Produto.get_nome, reverse=True)
print(produtos_ordenados)