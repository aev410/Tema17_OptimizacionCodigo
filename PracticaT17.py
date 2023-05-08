class Media:
    array_numeros=[]
    
    def array(self):
        return self.array_numeros
    
    def inp(self):
        print("introduzca un numero")
        return int(input())
    
    def add(self, n):
        self.array_numeros.append(n)
    def media(self):
        suma = 0
        for i in self.array_numeros:
            suma += i
        m = suma/len(self.array_numeros)
        print("La media es "+str(m))
        return m
