# 2 - Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios
#    para resolver las siguientes tareas:a. cada vértice debe almacenar el nombre de un personaje,
#    las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
#   b. hallar el árbol de expansión mínimo desde el vértice que contiene a C_3PO, Yoda y la princesa Leia;
#   c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
#   d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C_3PO, Leia,
#       Rey, Kylo Ren, Chewbacca, Han Solo, R2_D2, Obi_Wan kenobi; BB_8;
#   e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.

from grafo import Grafo

g = Grafo(dirigido=False)

g.insertar_vertice('Luke Skywalker')
g.insertar_vertice('Darth Vader')
g.insertar_vertice('Yoda')
g.insertar_vertice('Boba Fett')
g.insertar_vertice('C_3PO')
g.insertar_vertice('Leia')
g.insertar_vertice('Rey')
g.insertar_vertice('Kylo Ren')
g.insertar_vertice('Chewbacca')
g.insertar_vertice('Han Solo')
g.insertar_vertice('R2_D2')
g.insertar_vertice('Obi_Wan kenobi')
g.insertar_vertice('BB_8')

g.insertar_arista('Luke Skywalker', 'Chewbacca', 5)
g.insertar_arista('Leia', 'Obi_Wan kenobi', 4)
g.insertar_arista('Leia', 'Luke Skywalker', 4)
g.insertar_arista('Leia', 'Rey', 2)
g.insertar_arista('Leia', 'Darth Vader', 2)
g.insertar_arista('Yoda', 'BB_8', 3)
g.insertar_arista('Yoda', 'Han Solo', 4)
g.insertar_arista('Yoda', 'Kylo Ren', 4)
g.insertar_arista('C_3PO', 'R2_D2', 4)
g.insertar_arista('C_3PO', 'Boba Fett', 1)

# # Punto B
# for nodo in g.kruskal():
#     print()
#     if 'Yoda' in nodo:
#         print('Arbol de expansion minima de Yoda')
#         print(nodo)
#     elif 'Leia' in nodo:
#         print('Arbol de expansion minima de Leia')
#         print(nodo)
#     elif 'C_3PO' in nodo:
#         print('Arbol de expansion minima de C_3PO')
#         print(nodo)

# print()

# # Punto C
# comp = g.contar_compartidos()
# print('Los personajes que comparten dos o mas episodios son:')
# for k in comp:
#     if (comp[k] > 1):
#         print(k, comp[k])

# print()

# # Punto E
# compartidos = g.contar_personajes_compartidos()
# mayor = 0
# personaje = None
# for pers in compartidos:
#     if (mayor < compartidos[pers]):
#         personaje = pers
#         mayor = compartidos[pers]

# print('El personaje que mas ha compartido es',
#       personaje, 'con mayor', mayor, 'puliculas')
# print(personaje)
