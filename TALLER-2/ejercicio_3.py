class pila:
    def __init__(self):
        self.cuerpo=[]
    def isempty(self):
        return len(self.cuerpo)==0
    def push(self,newdata):
        self.cuerpo.append(newdata)
    def peek(self):
        return self.cuerpo[-1]
    def pop(self):
        if not self.isempty():
            self.cuerpo.pop()
        else:
            return None
    def size(self):
        return len(self.body)
    def __str__(self):
        columna=""
        for item in reversed(self.cuerpo):
            columna+= str(item)+ "\n"
        return columna

    
p=pila()
p.push(4)
p.push(9)

print(p)