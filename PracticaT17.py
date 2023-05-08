class Media:
    arrayNumeros=[]
    
    def array(self):
        return self.arrayNumeros
    
    def inp(self):
        print("introduzca un numero")
        return int(input())
    
    def add(self, n):
        self.arrayNumeros.append(n)
    def media(self):
        suma = 0
        for i in self.arrayNumeros:
            suma += i
        m = suma/len(self.arrayNumeros)
        print("La media es "+str(m))
        return m
