#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
t = input().split()
t_T = tuple(int(x) if x.isdigit() else x for x in t)
t_inversa=tuple(reversed(t_T))
print(t_inversa)

