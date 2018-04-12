class No:
	def __init__(self,item=None,prox=None):
		self.item = item
		self.prox = prox

class Lista:
	def __init__(self):
		self.primeiro = self.ultimo = No()

	
	def vazia(self):
		return self.primeiro == self.ultimo


	
	def inserir(self,item):
		self.ultimo.prox = No(item,None)
		self.ultimo = self.ultimo.prox

	
	def inserirInicio(self,item):
		self.primeiro.prox = No(item,self.primeiro.prox)
		if self.vazia():
			self.ultimo = self.primeiro.prox
			

	def inserirOrdenado(self,item):
		if self.vazia() == True:
			self.inserir(item)
			return 
		else:
			anterior = self.primeiro
			atual = self.primeiro.prox
			while atual is not None and atual.item < item:
				anterior = atual
				atual = anterior.prox
			anterior.prox = No(item,atual)
			if atual is None:
				self.ultimo = anterior.prox

		
	
	def mostrar(self):
		if self.vazia() == True:
			print('[]')
		else:
			aux = self.primeiro.prox
			string = '['
			while aux is not None:
				string = string + str(aux.item)                  #is not == !=
				if aux.prox is not None:                 #is == comparar referencia
					string = string + ','
				aux = aux.prox
			string += ']'
			return(string)
	
	
	def lenght(self):
		if self.vazia() == True:
			print('0')
		else:
			aux = self.primeiro.prox
			cont = 0
			while aux is not None:
				cont += 1
				aux = aux.prox
			print(cont)
		
	
	def search(self,item):
		if self.vazia() == True:
			return False
		else:
			aux = self.primeiro.prox
			while aux is not None and aux.item != item:
				aux = aux.prox
			try:
				if aux.item == item:
					return True
			
			except:
				return False
	
	def removerInicio(self):
		if self.vazia() == True:
			return None
		aux = self.primeiro.prox
		self.primeiro.prox = aux.prox
		item = aux.item
		if self.ultimo == aux:
			self.ultimo == self.primeiro
		aux.prox = None
		del aux
		return item

	def removerFim(self):
		if self.vazia() == True:
			return None
		aux = self.primeiro.prox
		while aux.prox != self.ultimo:
			aux = aux.prox
		item = self.ultimo.item
		ultimo = aux
		aux2 = ultimo.prox
		ultimo.prox = None
		del aux2
		return item

				
				
				 

if __name__ == "__main__":
	a = Lista()
	a.inserir(2)
	a.inserir(5)
	a.inserirInicio(80)
	a.inserirOrdenado(2)
	a.inserirOrdenado(6)
	a.inserirOrdenado(43)
	a.inserirOrdenado(7)
	a.mostrar()
	a.removerInicio()
	a.removerFim()
	a.mostrar()
	a.lenght()
	a.search(58)
	
	


def teste():
        lista = a.mostrar()
        for x in lista:
                print(x)





