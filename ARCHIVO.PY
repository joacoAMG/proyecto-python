
lista=[15,"nombre",3.1415,True]
#      (0)   (1)    (2)   (3)
print(lista[1])

usuario=["usernametest1","pass123","correo@correo.cl"]

numeros=[10,50,100,255,500]
#append= agrega un valor a la lista 
numeros.append(1000)
print(numeros)
#extends= agrega un arreglo al final de nuestra lista (fusiona listas )
extra=[75,350,999]
numeros.extend(extra)
print(numeros)
#insert= agrega valor en posicion especifica
numeros.insert(6,5000)
print(numeros)
#remove= entrega valor , se busca y se elimina 
numeros.remove(50)
print(numeros)
#pop= elimina el ultimo registro
#pop()= elimina la posicion del numero
numeros.pop()
print(numeros)
numeros.pop(3)
print(numeros)
#reverse= invierte el orden de la lista 
numeros.reverse()
print(numeros)
#sort= ordena los valore de menor a mayor 
#sort(reverse=true)= ordena los valores de mayor a menor 
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)
