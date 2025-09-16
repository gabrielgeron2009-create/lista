
from altair import Order


numeros = []


numeros.append(10)
numeros.append(20)
numeros.append(30)


numeros.insert(1, 15)


print("Lista final:", numeros)

Lista final: [10, 15, 20, 30]


lista = [5, 10, 15, 20, 25]

lista.remove(10)


lista.pop()


lista.pop(0)

print("Lista após remoções:", lista)


valores = [8, 3, 10, 1, 7]


print("Lista original:", valores)


valores.sort()
print("Ordem crescente:", valores)


valores.sort(reverse=True)
print("Ordem decrescente:", valores)


valores.reverse()
print("Lista invertida:", valores)

lista original: [8, 3, 10, 1, 7]
Order crescente: [1, 3, 7, 8, 10]
Order decrescente: [10, 8, 7, 3, 1]
lista invertida: [1, 3, 7, 8, 10]


notas = [7.5, 8.0, 6.5, 9.0, 5.5]

print("Quantidade de notas:", len(notas))


print("Maior nota:", max(notas))
print("Menor nota:", min(notas))

Quantidade de notas: 5
Maior nota: 9.0
Menor nota: 5.5
