#testFormacion
from Vagon import *
from Locomotora import *
from Formacion import *
import os

def main():
	os.system('cls')
	print 'Ingresar "punto 1" para ver la resolucion del punto 1, "punto 2" para la resolucion\n del punto 2'
	print 'y asi sucesivamente hasta el 11, con "?" ves esta ayuda y con "exit" salis del programa'
	
	while True:
		a = raw_input('> ')
		if a == 'exit':
			break
		elif a == '?':
			print 'Ingresar "punto 1" para ver la resolucion del punto 1, "punto 2" para la resolucion\n del punto 2'
			print 'y asi sucesivamente hasta el 11, con "?" ves esta ayuda y con "exit" salis del programa'
			print 'punto 1'
			print 'punto 2'
			print 'punto 3'
			print 'punto 4'
			print 'punto 5'
			print 'punto 6'
			print 'punto 7'
			print 'punto 8'
			print 'punto 9'
			print 'punto 10'
			print 'punto 11'
		elif a == 'punto 1':
			print 'se inicializa el objeto nuevaLocomotora = Locomotora(188000, 140) #(kg, km/h)'
			nuevaLocomotora = Locomotora(188000, 140) #(kg, km/h)
		elif a == 'punto 2':
			print 'se inicializan los objetos \nvagon1 = VagonDePasajeros(30, 25,0, 0, 15000)\nvagonCarga = VagonDeCarga(55000)\nvagon = VagonDePasajeros(50, 50, 0,0,15000)'
			vagon1 = VagonDePasajeros(30, 25,0, 0, 15000)
			vagonCarga = VagonDeCarga(55000)
			vagon = VagonDePasajeros(50, 50, 0,0,15000)
		elif a == 'punto 3':
			print 'Se inicializa el objeto formacionNueva = Formacion(nuevaLocomotora, [vagon1, vagonCarga, vagon], 4)'
			formacionNueva = Formacion(nuevaLocomotora, [vagon1, vagonCarga, vagon], 4)
		elif a == 'punto 4':
			pasajeros = 6
			print 'Se incorporaran %i pasajeros.' % (pasajeros)
			if formacionNueva.incorporarPasajeroFormacion(6):
				print 'Los pasajeros pudieron entrar.'
			else:
				print 'No hay espacio para todos los pasajeros.'
		elif a == 'punto 5' or a == 'punto 11':
			print '*****\nvagon1\n*****'
			print vagon1
			print '*****\nvagonCarga\n*****'
			print vagonCarga
			print '*****\nvagon\n*****'
			print vagon
		elif a == 'punto 6':
			print 'formacionNueva.incorporarPasajeroFormacion(14)'
			print formacionNueva.incorporarPasajeroFormacion(14)
		elif a == 'punto 7':
			print 'formacionNueva.cantidadPasajerosFormacion()'
			print formacionNueva.cantidadPasajerosFormacion()
		elif a == 'punto 8':
			print 'nuevaLocomotora'
			print nuevaLocomotora
		elif a == 'punto 9':
			print 'formacionNueva.promedioPasajeroVagon()'
			print formacionNueva.promedioPasajeroVagon()
		elif a == 'punto 10':
			print 'formacionNueva.pesoFormacion()'
			print formacionNueva.pesoFormacion()
		
		
main()		