import preguntas as p


def verificar(alternativas, eleccion):
    """_summary_

    Args:
        alternativas (string): letras entre la "a" a la "d"
        eleccion (int): validacion numerica si es correcta o no.

    Returns:
        bolean: mensaje se respuesta correcta o incorrecta
    """
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    # print(eleccion)
    # print(alternativas)
    if  eleccion == 1:
        print("respuesta correcta\n")
        return True
    else:
        print("Respuesta inCorrecta\n")
        return False



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






