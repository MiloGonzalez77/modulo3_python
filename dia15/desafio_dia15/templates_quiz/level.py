def choose_level(n_pregunta, p_level):
    """eleccion de nivel de dificultad

    Args:
        n_pregunta (int): numero de preguntas entre 1 a 3
        p_level (int): numero para nivel de dificultad

    Returns:
        int: valores elejidos
    """
    nivel ="" 
    if n_pregunta <= p_level:
        nivel="Basicas"
    elif n_pregunta <= 2*p_level:
        nivel="Intermedias"
    else:
        nivel ="Avanzadas"
    return nivel

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias