#clase Locomotora
class Locomotora:
	def __init__(self, peso=0, velocidadMaxima=0):
		self.__peso = peso
		self.__velocidadMaxima = velocidadMaxima
	
	def __str__(self):
		return 'Peso: ' + str(self.get_peso()) + '\nVelocidad Maxima: ' + str(self.get_velocidadMaxima())
		
	def get_peso(self):
		return self.__peso
		
	def set_peso(self, peso):
		self.__peso = peso
		
	def get_velocidadMaxima(self):
		return self.__velocidadMaxima
		
	def set_velocidadMaxima(self, vm):
		self.__velocidadMaxima = vm
		
	