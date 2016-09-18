# -*- coding: utf-8 -*- 
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from datetime import *

class Ventana(QtGui.QWidget):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent)
		dia = "null"
		self.setGeometry(500, 500, 350, 250)
		self.setWindowTitle("!Viva Mexico!")
		self.setWindowIcon(QtGui.QIcon('icono.png'))
		texto = "\n   Personajes importantes de la independecia de mexico:\n\n     * Miguel Hidalgo y Costilla (1753 a 1811)\n     * Ignacio Allende (1769 a 1811)\n     *Josefa Ortiz de Domínguez (1768 a 1829)"
		self.label = QtGui.QLabel(texto, self)
		self.boton = QtGui.QPushButton('Aprietame', self)
		self.botonDia = QtGui.QPushButton('Aprietame', self)
		self.boton.setGeometry(125, 100, 100, 50)
		self.botonDia.setGeometry(10, 150, 100, 50)
		self.boton.clicked.connect(self.calcula_proximo_15)
		self.botonDia.clicked.connect(self.calcula_dia)

	def calcula_proximo_15(self):
		fecha_actual = datetime.now() #Fecha y hora actual.
		#Si en el año actual aún no ha pasado el 15 de septiembre.
		if fecha_actual.month < 9 or (fecha_actual == 9 and fecha_actual < 15):
			proximo_15 = datetime(fecha_actual.year, 9, 15, 0, 0, 0)
		else:
		#Si ya paso el 15 de septiembre en el año actual.
			proximo_15 = datetime(fecha_actual.year + 1, 9, 15, 0, 0, 0)
		diferencia = proximo_15 - fecha_actual
		self.boton.setText("Faltan " + str(diferencia.days) + " dias, para el proximo 15 de septiembre.")
		self.boton.resize(self.boton.sizeHint())
		self.boton.move(15, 100)

	def calcula_dia(self):
		fecha_actual = datetime.now() #Fecha y hora actual.
		dias = {'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves', \
		'FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo'}
		if fecha_actual.month < 9 or (fecha_actual == 9 and fecha_actual < 15):
			year = fecha_actual.year
		else:
			year = fecha_actual.year + 1
		fecha = date(year, 9, 15)
		dia = str(dias[fecha.strftime('%A').upper()])
		self.botonDia.setText("Calculando...\nSegun el calendario cae en dia " + dia)
		self.botonDia.resize(self.botonDia.sizeHint())

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	empieza = Ventana()
	empieza.show()
