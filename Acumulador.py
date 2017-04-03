# -*- coding: utf-8 -*-
#Acumulador de meses y generador de inserts para base de datos msql
import os

def creartxt():
    archi=open('acumulados.txt','w')
    archi.close()

def grabartxt(nombrearchivo,linea):
    archi=open(nombrearchivo,'a')
    archi.write(linea+'\n')
    archi.close()

def generacalendariosql(nombrearchivo,aniodesde,aniohasta,nombre_tabla,nombre_campo1,nombre_campo2):
	print('Generando calendario')
	i = aniodesde
	m = 0
	linea = 'a'
	acum = 0
	insert = 'pepe'

	while i <= aniohasta:
		print('Procesando'+str(i))
		print('Proceso de meses')
		for m in [1,2,3,4,5,6,7,8,9,10,11,12]:
			if m == 1:
				linea = str(i)+'0'+str(m)+','+str(i)+'0'+str(m)
				insert = 'INSERT INTO'+'['+nombre_tabla+'] ( ['+nombre_campo1+'],['+nombre_campo2+'] ) VALUES ('+linea+')'
				grabartxt(nombrearchivo,insert)
			else:
				acum = 1
				while acum <= m:
					if acum < 10:
						if m < 10:
							linea = str(i)+'0'+str(m)+','+str(i)+'0'+str(acum)
						else:
							linea = str(i)+str(m)+','+str(i)+'0'+str(acum)
					else:
						linea = str(i)+str(m)+','+str(i)+str(acum)
					insert = 'INSERT INTO'+'['+nombre_tabla+'] ( ['+nombre_campo1+'],['+nombre_campo2+'] ) VALUES ('+linea+')'
					grabartxt(nombrearchivo,insert)
					acum=acum+1
		i=i+1
		print('Fin proceso para anio'+str(i))
	print('Finalizacion del proceso completo')

def generacalendarionormal(nombrearchivo,aniodesde,aniohasta):
	print('Generando calendario')
	i = aniodesde
	m = 0
	linea = 'a'
	acum = 0
	while i <= aniohasta:
		print('Procesando'+str(i))
		print('Proceso de meses')
		for m in [1,2,3,4,5,6,7,8,9,10,11,12]:
			if m == 1:
				linea = str(i)+'0'+str(m)+','+str(i)+'0'+str(m)+'\n'
				grabartxt(nombrearchivo,linea)
			else:
				acum = 1
				while acum <= m:
					if acum < 10:
						if m < 10:
							linea = str(i)+'0'+str(m)+','+str(i)+'0'+str(acum)+'\n'
						else:
							linea = str(i)+str(m)+','+str(i)+'0'+str(acum)+'\n'
					else:
						linea = str(i)+str(m)+','+str(i)+str(acum)+'\n'
					grabartxt(nombrearchivo,linea)
					acum=acum+1
		i=i+1
		print('Fin proceso para anio'+str(i))
	print('Finalizacion del proceso completo')

#Declaracion de variables
aniodesde = 0
aniohasta = 0
nombre_tabla = 'noname'
nombre_campo1 = 'campo1'
nombre_campo2 = 'campo2'
nombrearchivo = 'archivo'

generainsert = False

print('Bienvenido al Generador de meses acumulados')
print('Siga las instrucciones :')

#print('Ingrese el nombre que quiere darle al archivo:')
#nombrearchivo = input()

print('Ingrese el anio de inicio del calendario :')
aniodesde = 2016 #int(input())

print('Ingrese el anio de finalizacion del calendario')
aniohasta = 2020 #int(input())

print('Desea que se generen los insert para la tabla ? Y/N ')
generainsert = True #input()

if generainsert == True :

	print('Ingrese el nombre de la tabla :')
	nombre_tabla = 'tr_Acumulamescal' #input()

	print('Ingrese el nombre del campo del mes actual:')
	nombre_campo1 = 'ID_MESAÑO' #input()

	print('Ingrese el nombre del campo de mes acumulado:')
	nombre_campo2 = 'ID_MESAÑO_ACUM'#input()


if generainsert == True :
	generacalendariosql(nombrearchivo,aniodesde,aniohasta,nombre_tabla,nombre_campo1,nombre_campo2)
else:
	generacalendarionormal(nombrearchivo,aniodesde,aniohasta)




