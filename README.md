# Verificación de Edad para Licencia de Conducir

Este programa en Python solicita la edad del usuario y determina si cumple con la edad mínima (18 años) para obtener una licencia de conducir.

## Instalación

1. **Instala Python 3.x** desde [python.org](https://www.python.org/downloads/) y marca la opción **Add Python to PATH**.
2. **Instala VSCode** desde [code.visualstudio.com](https://code.visualstudio.com/) y agrega la extensión de Python.

## Ejecución del Programa

Para ejecutar el programa, abre `main.py` en VSCode y presiona el botón de **Play**, o usa el comando:

```bash
python main.py
```

## Pruebas Unitarias
El archivo test_main.py contiene pruebas unitarias para validar el funcionamiento del programa. Se incluyen tres pruebas:

1. Prueba de edad mayor o igual a 18: verifica que el programa permita obtener el carnet para edades de 18 o más.
2. Prueba de edad menor a 18: verifica que el programa niegue el carnet para edades menores de 18.
3. Prueba con edad negativa: esta prueba está diseñada para fallar, mostrando cómo el programa no maneja este caso de entrada no válida.
## Ejecución de las Pruebas
Para ejecutar las pruebas unitarias, en una terminal de VSCode usar el siguiente comando:

```bash
python -m unittest test_main.py
```