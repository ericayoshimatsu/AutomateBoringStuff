# importing a module (pip install pyperclip)
import pyperclip
import copy
print('Hello World!')

pyperclip.copy('Copy')
print(pyperclip.paste())

# Trying to sync with GitHub

# Lists
lista = ['spam', 'bacon', 'eggs']
print(lista[-1])
lista[0] = 'monty'
print(lista[:2])
lista2 = 2*lista
del lista2[4]
print(lista2)

for i in range(len(lista2)):
    print('Index ' + str(i) + ' is: ' + lista2[i])

a1, a2, a3, a4, a5 = lista2

print(a3)


# list is mutable -> reference
lista3 = lista2
copyLista = copy.deepcopy(lista2)

lista3.append('SPAM')
print(lista2)

copyLista.append('COPY')
print(lista2)

# line continuation
print('Once upon a time, there was a story so looooo \
      ooooooooooooooooong')

# dictionary -> mutable by reference
dicionario = {'key':  'value', 'color': 'blue'}
print(dicionario['key'])

for k,v in dicionario.items():
    print(k + ' ' + v)

