# 1 - Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas de personajes
#   de la saga de Star Wars, de los cuales se sabe su nombre, altura y peso.
#   Además deberá contemplar los siguientes requerimientos (debe cargar al menos 20 personajes):
#   a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
#   b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
#   c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
#   d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
#   e. mostrar un listado por nivel de los personajes del árbol;
#   f. determinar si Grogu esta en el árbol y responder lo siguiente:
#   mostrar toda su información;
#   en que tipo de nodo esta (hoja, intermedio o raíz);
#   que altura tiene el nodo dentro del árbol.

from arbol import *

arbol = nodoArbol()

insertar_nodo(arbol, 'qui-gon jin', {'altura': 1.93, 'peso': 90})
insertar_nodo(arbol, 'obi-wan kenobi', {'altura': 1.82, 'peso': 85})
insertar_nodo(arbol, 'quinlan vos', {'altura': 1.91, 'peso': 95})
insertar_nodo(arbol, 'yoda', {'altura': 0.66, 'peso': 35})
insertar_nodo(arbol, 'adi gallia', {'altura': 1.84, 'peso': 92.5})
insertar_nodo(arbol, 'mace windu', {'altura': 1.92, 'peso': 92})
insertar_nodo(arbol, 'luke skywalker', {'altura': 1.75, 'peso': 72})
insertar_nodo(arbol, 'oppo rancisis', {'altura': 1.38, 'peso': 65})
insertar_nodo(arbol, 'ki-adi-mundi', {'altura': 1.98, 'peso': 105})
insertar_nodo(arbol, 'plo koon', {'altura': 1.88, 'peso': 82})
insertar_nodo(arbol, 'mandalorian', {'altura': 1.83, 'peso': 95})
insertar_nodo(arbol, 'yarael poof', {'altura': 2.64, 'peso': 156})
insertar_nodo(arbol, 'saesee tiin', {'altura': 1.93, 'peso': 91})
insertar_nodo(arbol, 'yaddle', {'altura': 0.61, 'peso': 25})
insertar_nodo(arbol, 'anakin skywalker', {'altura': 1.88, 'peso': 87})
insertar_nodo(arbol, 'even pieli', {'altura': 1.22, 'peso': 56})
insertar_nodo(arbol, 'eeth koth', {'altura': 1.71, 'peso': 76})
insertar_nodo(arbol, 'grogu', {'altura': 0.35, 'peso': 20})
insertar_nodo(arbol, 'count dooku', {'altura': 1.93, 'peso': 82.5})
insertar_nodo(arbol, 'asajj ventress', {'altura': 1.80, 'peso': 90})
insertar_nodo(arbol, 'pong krell', {'altura': 2.36, 'peso': 160})

# Punto A
print('Cargue un nuevo personaje')
print('Ingrese el nombre:')
nombre = input()
print('Ingrese la altura:')
altura = float(input())
print('Ingrese el peso:')
peso = float(input())

insertar_nodo(arbol, nombre, {'altura': altura, 'peso': peso})

print('Modifique un personaje')
nombreBuscado = input('Ingrese el nombre:')
personaje = busqueda(arbol, nombreBuscado)

if personaje is not None:
    opcionN = input('Desea modificar el nombre? (s/n)')
    if (opcionN == 's'):
        nombre = input('Ingrese el nuevo nombre: ')

    opcion = input('Desea modificar la altura? (s/n)')
    if (opcion == 's'):
        altura = input('Ingrese la nueva altura: ')
        personaje['datos']['altura'] = altura

    opcion = input('Desea modificar el peso? (s/n)')
    if (opcion == 's'):
        peso = input('Ingrese el nuevo peso: ')
        personaje['datos']['peso'] = peso

    if (opcionN == 's'):
        eliminar_nodo(arbol, nombreBuscado)
        insertar_nodo(arbol, nombre, {
                      'altura': personaje['datos']['altura'], 'peso': personaje['datos']['peso']})

else:
    print('No se ha encontrado el personaje')

print('Elimine un personaje')
print('Ingrese el nombre:')
nombreBuscado = input()
if (busqueda(arbol, nombreBuscado) is not None):
    eliminar_nodo(arbol, nombreBuscado)
else:
    print('No se ha encontrado el personaje')

print()

# Punto B
print('Yoda: ', busqueda(arbol, 'yoda')['datos'])
print('Mandalorian: ', busqueda(arbol, 'mandalorian')['datos'])
print('Luke Skywalker: ', busqueda(arbol, 'luke skywalker')['datos'])

print()

# Punto C
print('Personajes con altura menor que 0.9')
inordenAlturaMenorQue(arbol, 0.9)

print()

# Punto D
print('Personajes que pesan mas de 75kg')
inordenPesoMayorQue(arbol, 75)

print()

# Punto E
por_nivel(arbol)

print()

# Punto F
personaje = busqueda(arbol, 'grogu')
print(personaje)
if (personaje is not None):
    print('Info de Grogu: ', personaje['datos'])
    if (arbol['info'] == 'Grogu'):
        print('Está en un nodo hoja')
    elif ((personaje['der'] is None) & (personaje['izq'] is None)):
        print('Está en un nodo hoja')
    else:
        print('Está en un nodo intermedio')
    print('La altura del nodo es: ', personaje['altura'])
else:
    print('Grogu no está en el arbol')
