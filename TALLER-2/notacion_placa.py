class Pila:
    def __init__(self):
        self.body = []

    def isempty(self):
        return len(self.body) == 0
    
    def push(self, new_data):
        self.body.append(new_data)

    def peek(self):
        if not self.isempty():
            return self.body[-1]
        else:
            return None
     
    def pop(self):
        if not self.isempty():
            return self.body.pop()
        else:
            return None

    def size(self):
        return len(self.body)
    
    def __str__(self):
        columna = ""
        for item in reversed (self.body): #reversed = invertir la pila
            columna += str(item) + "\n"
        return columna

class operaciones:
    def __init__(self):
        self.operaciones=Pila()

    def apilar_caracteres(self,string):
        
        caracteres =list(string)

        for i in caracteres:
            self.operaciones.push(i)

    def operar(self):
        pila_auxiliar = Pila()

        while not self.operaciones.isempty():
            elemento_actual = self.operaciones.pop()

            if elemento_actual.isdigit():
                pila_auxiliar.push(int(elemento_actual))

            else:
                operando2 = pila_auxiliar.pop()
                operando1 = pila_auxiliar.pop()

                if operando1 is None or operando2 is None:
                    raise ValueError("No hay suficientes operandos en la pila auxiliar")

                if elemento_actual == '+':
                    pila_auxiliar.push(operando1 + operando2)
                elif elemento_actual == '-':
                    pila_auxiliar.push(operando1 - operando2)
                elif elemento_actual == '*':
                    pila_auxiliar.push(operando1 * operando2)
                elif elemento_actual == '/':
                    pila_auxiliar.push(operando1 / operando2)

        if pila_auxiliar.size() != 1:
            raise ValueError("La expresión no está bien formada")

        return pila_auxiliar.pop()


mi_operacion = operaciones()  # Crear una instancia de la clase operaciones

letra = "42+*"  # Definir la expresión en notación polaca

mi_operacion.apilar_caracteres(letra)  # Apilar los caracteres de la expresión

resultado = mi_operacion.operar()  # Evaluar la expresión y obtener el resultado

print("El resultado de la expresión", letra, "es:", resultado)  # Imprimir el resultado

    


