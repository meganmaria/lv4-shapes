import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *


class GrafObj:	
	def __init__(self, boja, tocka):
		self.boja = boja	
		self.tocka = tocka	
	def SetColor(self, boja):
		self.boja = boja
	def GetColor(self):
		return self.boja
	def Crtaj(self, canvas):
		pass

class Linija(GrafObj):
	def __init__(self, boja, tocke):
		super().__init__(boja, tocke[:2])	
		self.drugaTocka = tocke[2:]	
		
	def Crtaj(self, canvas):
		canvas.create_line(self.tocka[0], self.tocka[1], self.drugaTocka[0], self.drugaTocka[1], fill=self.boja)

class Trokut(Linija):	
	def __init__(self, boja, tocke):
		super().__init__(boja, tocke[:4])	
		self.trecaTocka = tocke[4:]	

	def Crtaj(self, canvas):
		canvas.create_line(self.tocka[0], self.tocka[1], self.drugaTocka[0], self.drugaTocka[1], self.trecaTocka[0], self.trecaTocka[1], self.tocka[0], self.tocka[1], fill=self.boja)


class Pravokutnik(GrafObj):
	def __init__(self, color, tocke):
		super().__init__(color, tocke[:2])
		self.visina = tocke[2]	
		self.sirina = tocke[3]	
	
	def Crtaj(self, canvas):
		canvas.create_rectangle(self.tocka[0], self.tocka[1], self.tocka[0]+self.sirina, self.tocka[1]+self.visina, outline=self.boja, fill="")

class Poligon(GrafObj):	
	def __init__(self, boja, tocke):
		super().__init__(boja, tocke)	
	
	def Crtaj(self, canvas):
		canvas.create_polygon(self.tocka, outline=self.boja, fill="")

class Kruznica(GrafObj):	
	def __init__(self, boja, tocke):
		super().__init__(boja, tocke[:2])	
		if(len(tocke)>2):
			self.radius = tocke[2]	
	
	def Crtaj(self, canvas):
		canvas.create_oval(self.tocka[0]-self.radius, self.tocka[1]-self.radius, self.tocka[0]+self.radius, self.tocka[1]+self.radius, outline=self.boja, fill="")

class Elipsa(Kruznica):
	def __init__(self, boja, tocke):
		super().__init__(boja, tocke[:2])	
		self.x_os = tocke[2]	
		self.y_os = tocke[3]	
	
	def Crtaj(self, canvas):
		canvas.create_oval(self.tocka[0]-self.x_os, self.tocka[1]-self.y_os, self.tocka[0]+self.x_os, self.tocka[1]+self.y_os, outline=self.boja, fill="")

def Ucitaj(path, canvas):
	file = open(path, 'r')	
	data = []		
	for line in file.readlines():
		data.append(line.strip().split())	
	for shape in data:
		temp = []	
		obj = None	
		for tocka in shape[2:]:
			temp.append(float(tocka))		
		if(shape[0]=="Line"):
			obj = Linija(shape[1], temp)		
		elif(shape[0]=="Triangle"):
			obj = Trokut(shape[1], temp)		
		elif(shape[0]=="Rectangle"):
			obj = Pravokutnik(shape[1], temp)	
		elif(shape[0]=="Polygon"):
			obj = Poligon(shape[1], temp)		
		elif(shape[0]=="Circle"):
			obj = Kruznica(shape[1], temp)	
		elif(shape[0]=="Ellipse"):
			obj = Elipsa(shape[1], temp)	
		if(obj!=None):
			obj.Crtaj(canvas)

class Aplikacija:	
	def __init__(self):
		self.window = tk.Tk()	
		self.window.minsize(850, 650)
		button = Button(text="Otvori", command=self.Otvori).pack()
		exitButton = Button(text="Izlaz", command=self.window.destroy).pack()	
		self.Canv()
		self.window.mainloop()
	def Otvori(self):
		file = fd.askopenfilename()
		Ucitaj(file, self.canvas)		
	def Canv(self):
		self.canvas = tk.Canvas(self.window, width=850, height=650, background="#505050")
		self.canvas.pack()			
Aplikacija()
	

	
