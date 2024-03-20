#CLASIFICAR PASSWORD

#solictar al usuario que ingrese passwrod.
contrasenia = input("Ingrese una contraseña de al menos 6 caracteres\n")

#validar cantidad de caracteres con len-> contar carcteres
if contrasenia.count(" ") > 0:
    print("La contraseña no puede contener espacios!")
elif contrasenia == '12345':
    print("Contraseña incorrecta!")
elif len(contrasenia) < 6:
    print("Contraeña demasiado corta!")
else:
    print("Contraseña validada!")
    
#IF anidado a la antigua.
    """
else:
    if len(contrasenia) < 6:
        print("Contraeña demasiado corta!")
    else:
        print("Contraseña validada!")
    """
print("Fin de programa.")
