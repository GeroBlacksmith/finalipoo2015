#clase Vagon

class Vagon:
	def __init__(self, anioDeInstalacion=0, largo=0, ancho=0, peso=0):
		self.__anioDeInstalacion = anioDeInstalacion
		self.__largo = largo
		self.__ancho = ancho
		self.__peso = peso
	
	
	def __str__(self):
		a = ''
		if self.get_anioDeInstalacion == 0:
			a += 'Anio de instalacion no definido'
		else:
			a += 'Anio de instalacion: ' + str(self.get_anioDeInstalacion())
		if self.get_largo == 0:
			a += '\nEl largo no esta definido'
		else:
			a += '\nEl largo es de '  +	str(self.get_largo())
		if self.get_ancho == 0:
			a += '\nEl ancho no esta definido'
		else:
			a += '\nEl ancho es de '  +	str(self.get_ancho())
		if self.get_peso == 0:
			a += '\nEl peso no esta definido'
		else:
			a += '\nEl peso es de '  +	str(self.get_peso())
		return a
		
	def get_anioDeInstalacion(self):
		return self.__anioDeInstalacion
		
	def set_anioDeInstalacion(self, anio):
		self.__anioDeInstalacion = anio
		
	def get_largo(self):
		return self.__largo
		
	def set_largo(self, largo):
		self.__largo = largo
		
	def get_peso(self):
		return self.__peso
		
	def set_peso(self):
		self.__peso = self.calcularPesoVagon()
	
	def get_ancho(self):
		return self.__ancho
		
	def set_ancho(self, ancho):
		self.__ancho = ancho
		
	
	def calcularPesoVagon(self):
		pass
		
class VagonDeCarga(Vagon):
	def __init__(self, carga, pesoMaximo=100000, anioDeInstalacion=0, largo=0, ancho=0, peso=0):
		Vagon.__init__(self, anioDeInstalacion, largo, ancho, peso)
		self.__pesoMaximo = pesoMaximo
		self.__pesoTransporte = carga
		
	def __str__(self):
		a = Vagon.__str__ (self)
		a += '\nPeso maximo soportado: ' + str(self.get_pesoMaximo())
		a += '\nPeso de lo que actualmente se transporta: ' + str(self.get_pesoTransporte())
		return a
		
	def get_pesoMaximo(self):
		return self.__pesoMaximo
		
	def set_pesoMaximo(self, pm):
		self.__pesoMaximo = pm
		
	def get_pesoTransporte(self):
		return self.__pesoTransporte
		
	def set_pesoTransporte(self, pt):
		self.__pesoTransporte = pt
		
	def calcularPesoVagon(self):
		return self.get_pesoTransporte() * 1,2
	
class VagonDePasajeros(Vagon):
	def __init__(self, capacidadDePasajeros=0, pasajerosABordo=0, anioDeInstalacion=0, largo=0, ancho=0, peso=0):
		Vagon.__init__(self,  anioDeInstalacion, largo, ancho, peso)
		self.__capacidadDePasajeros = capacidadDePasajeros
		self.__pasajerosABordo = pasajerosABordo
		
	def __str__(self):
		a = Vagon.__str__ (self)
		a += '\nCapacidad maxima de pasajeros: ' + str(self.get_capacidadDePasajeros())
		a += '\nCapacidad de pasajeros a bordo: ' + str(self.get_pasajerosABordo())
		return a
		
	def calcularPesoVagon(self):
		return (self.get_pasajerosABordo() * 50)
	
	def get_pasajerosABordo(self):
		return self.__pasajerosABordo
		
	def set_pasajerosABordo(self, pab):
		self.__pasajerosABordo = pab
		
	def get_capacidadDePasajeros(self):
		return self.__capacidadDePasajeros
		
	def set_capacidadDePasajeros(self, cdp):
		self.__capacidadDePasajeros = cdp
		
	def incorporarPasajeroVagon(self, cantidadDePasajeros):
		p = self.get_pasajerosABordo()
		if p + cantidadDePasajeros < self.get_capacidadDePasajeros():
			self.set_pasajerosABordo(p)
			self.set_peso(self.calcularPesoVagon())
		else: 
			raise BaseException('No se pueden poner mas pasajeros')
			
		