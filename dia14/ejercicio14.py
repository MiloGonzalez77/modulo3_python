###DOCSTRING###

#Calcular el factorial de un numero:
def factorial(numero):#5! = 5*4*3*2*1
    """Calcular el factorial de un numero

    Args:
        numero (int): numero a usar para calcular factorial

    Returns:
        int: resultado del factorial de un numero
    """
    valor = 1 # variable acumuladora
    for n in range(1,numero+1):#1,2,3,4,5
        valor = valor * n
    return valor

print(factorial(4))
print("--Fin--")

###REFACTORIZACION###
#Slide 15 ppt dia 14.
def cuadrado_cubo(valor):
    return valor**2 + valor**3
def mult_234(valor):
    return valor*2 + valor*3 + valor*4
def op_combinada(valor):
    var_intermedia = cuadrado_cubo(valor)
    return mult_234(var_intermedia)

def compose(f, n):
    def fn(x):
        for _ in range(n):
            x = f(x)
            return x
    return fn

valor_entrada = 10
valor_6 = compose(op_combinada, 3)(valor_entrada)
print(valor_6)
print("-------")

###