def verificar_edad_para_licencia(edad):
    if edad >= 18:
        return "Puedes sacar el carnet de conducir."
    else:
        return "No puedes sacar el carnet de conducir."


def main():
    try:
        edad = int(input("Introduce tu edad: "))
        print(verificar_edad_para_licencia(edad))
    except ValueError:
        print("Por favor, introduce un número válido.")


if __name__ == "__main__":
    main()