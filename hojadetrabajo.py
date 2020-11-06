def jugar(intento=1):
    respuesta = input("De que color es la fruta?: \n")
    if respuesta != "naranja":
        if intento <3: 
            print("\n Fallaste, intentalo de nuevo")
            intento +=1
            jugar(intento) #Llamada recursiva
        else:
            print("\n Perdiste, intentalo de nuevo")
    else:
        print("\n Ganaste, eres lo maximo!")

jugar()

