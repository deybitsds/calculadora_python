
# modulo para verificar si los parentesis estan correctos en cadena
def verificar_parentesis(cadena):
    # Diccionario de pares de paréntesis

    pares = {')': '(', ']': '[', '}': '{'}
    # Pila para almacenar los paréntesis abiertos
    pila = []

    for char in cadena:
        if char in pares.values():  # Si es un paréntesis de apertura
            pila.append(char)
        elif char in pares.keys():  # Si es un paréntesis de cierre
            if not pila or pila[-1] != pares[char]:  # Verifica si la pila está vacía o el paréntesis no coincide
                return False
            else:
                pila.pop()  # Elimina el paréntesis coincidente de la pila

    return not pila  # Verifica si la pila está vacía al final


# funcion para predecir el siguiente caracter
def determinar_siguiente_caracter(cadena, caracter_apertura, caracter_cierre):

    # inicializar el balance en 0
    balance = 0

    # recorrer toda la cadena anterior
    for char in cadena:
        
        # caso se lea un caracter_apertura sumar al balance 1
        if char == caracter_apertura:
            balance += 1
        
        # caso se lea un caracter_cierre restar al balance 1
        elif char == caracter_cierre:
            balance -= 1
        
    # si el balance es 0 se abre un nuevo bloque 
    return caracter_apertura if balance == 0 else caracter_cierre


# funcion para determinar la prioridad o nivel de una operacion
def valPreced(s):

    if s == "^":
        return 4
    elif s == "*" or s == "/":
        return 3
    elif s == "+" or s == "-":
        return 2
    else:
        return 1


# funcion para ver si un parentesis esta abierto o no
def parentesisAbierto(s):

    if s == ")":
        return "("
    elif s == "]":
        return "["
    else:
        return "{"


# modulo para convertir una expresion de infija a postfija
def infijoPostfija(expresion):

    # Convertir la expresión en una lista de tokens
    infijo = []
    numero = ''
    
    for char in expresion:
        if char.isdigit() or char == '.':  # Verificar si el carácter es un dígito o un punto decimal
            numero += char
        else:
            if numero:
                infijo.append(numero)
                numero = ''
            if char.strip():  # Asegurarse de no agregar espacios como tokens
                infijo.append(char)
    
    if numero:
        infijo.append(numero)
    
    # Pila para guardar operadores y paréntesis izquierdos
    pila = []
    salida = []

    for s in infijo:
        # Si el elemento es un operando, añádelo a la salida
        if s.replace('.', '', 1).isdigit():  # Verifica si el símbolo es un número, permitiendo un solo punto decimal
            salida.append(s)
        # Verificamos si el elemento actual es un operador
        elif s in "+-*/^":
            # Mientras haya operadores en la pila con mayor o igual precedencia que el actual
            while pila and pila[-1] != '(' and valPreced(s) <= valPreced(pila[-1]):
                salida.append(pila.pop())
            # Apilamos el operador actual
            pila.append(s)
        # Si es un paréntesis abierto, simplemente lo apilamos
        elif s in "([{":
            pila.append(s)
        # Si es un paréntesis cerrado, desapilamos hasta encontrar su paréntesis abierto
        elif s in ")]}":
            while pila and pila[-1] != parentesisAbierto(s):
                salida.append(pila.pop())
            # Desapilamos el paréntesis abierto correspondiente
            pila.pop()
        else:
            return "MATH ERROR"

    # Desapilamos cualquier operador restante en la pila
    while pila:
        salida.append(pila.pop())

    return salida


# modulo para calcular el resultado de una expresion postfija
def eval_postfija(expresion):

    pila = []

    postfijo = expresion

    for s in postfijo:
        if s == "+":
            opnd2 = pila.pop()
            opnd1 = pila.pop()
            pila.append(opnd1 + opnd2)
        elif s == "-":
            opnd2 = pila.pop()
            opnd1 = pila.pop()
            pila.append(opnd1 - opnd2)
        elif s == "*":
            opnd2 = pila.pop()
            opnd1 = pila.pop()
            pila.append(opnd1 * opnd2)
        elif s == "/":
            opnd2 = pila.pop()
            if opnd2 == 0:
                return "MATH ERROR"
            opnd1 = pila.pop()
            pila.append(opnd1 / opnd2)
        elif s == "^":
            opnd2 = pila.pop()
            opnd1 = pila.pop()
            pila.append(opnd1 ** opnd2) 
        else:
            pila.append(float(s))

    return pila[-1]


# funcion que devuelve si una cadena posee numeros o no
def contiene_numeros(cadena):

    for caracter in cadena:
        if caracter.isdigit():
            return True
    return False


if __name__ == "__main__":

    probar_modulo(infijoPostfija)