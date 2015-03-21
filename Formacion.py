#clase Formacion
from Vagon import *
class Formacion:
	def __init__(self, locomotora=None, vagones = [], topeDeVagones=0):
		self.__cabecera = locomotora
		if isinstance(vagones, list):
			self.__vagones = vagones
		else:
			raise TypeError ('se debe ingresar una lista para los vagones')
		self.__topeDeVagones = topeDeVagones
		pass
		
		
	def get_locomotora(self):
		return self.__cabecera
		
	def set_locomotora(self, locomotora):	
		self.__cabecera = locomotora
		
	def get_vagones(self):
		return self.__vagones
		
	def set_vagones(self, vagones):
		self.__vagones = vagones
		
	def get_topeDeVagones(self):
		return self.__topeDeVagones
		
	def set_topeDeVagones(self, topeDeVagones):
		self.__topeDeVagones = topeDeVagones
		
	
	def incorporarPasajeroFormacion(self, pasajeros):
		for vagon in self.get_vagones():
			if pasajeros + vagon.get_pasajerosABordo() < vagon.get_capacidadDePasajeros():
				vagon.set_pasajerosABordo(pasajeros + vagon.get_pasajerosABordo())
				return True
			else:
				return False
			
		
	
	def incorporarVagonFormacion(self, vagon):
		if len(self.get_vagones()) + 1 < self.get_topeDeVagones():
			self.get_vagones.append(vagon)
			return True
			
		else:
			return False
	
	def promedioPasajeroVagon(self):
		suma_parcial = 0
		cantidadVagonesDePasajeros = 0
		for vagon in self.get_vagones():
			if isinstance(vagon, VagonDePasajeros):
				suma_parcial += vagon.get_pasajerosABordo()
				cantidadVagonesDePasajeros += 1
			
		return suma_parcial / cantidadVagonesDePasajeros		
	
	def cantidadPasajerosFormacion(self):
		suma_parcial = 0
		
		for vagon in self.get_vagones():
			if isinstance(vagon, VagonDePasajeros):
				suma_parcial += vagon.get_pasajerosABordo()
				
			
		return suma_parcial 
	
	def pesoFormacion(self):
		peso_parcial = self.get_locomotora().get_peso()
		for vagon in self.get_vagones():
			peso_parcial += vagon.calcularPesoVagon()
			
		return peso_parcial
		
		
		
	