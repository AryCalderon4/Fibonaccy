import json

arreglo = {}
a, b = 0, 1

num=input('Introduzca un numero del 1 al 20')
c=0
while c < int(num):
	arreglo['num'+str(c)]=a
	a, b = b, a+b
	c=c+1
fjson=json.dumps(arreglo)
print(fjson)
