import datetime
import time

# Definir la fecha y hora especial
fecha_especial = datetime.datetime(2024, 2, 29, 00, 00, 0) 
print("Buenas Buenaaaasss! Bienvenido a la consola:) Me presento soy bipbipbip TiciTerminal brindando un mensaje!")
while True:
    # Obtener la fecha y hora actual
    fecha_actual = datetime.datetime.now()

    # Calcular la diferencia entre la fecha y hora especial y la fecha y hora actual
    diferencia = fecha_especial - fecha_actual

    # Imprimir la cantidad de días, horas, minutos y segundos restantes
    print("Faltan {} días, {} horas, {} minutos y {} segundos para la fecha especial.".format(
        diferencia.days,
        diferencia.seconds // 3600,  # Convertir segundos a horas
        (diferencia.seconds % 3600) // 60,  # Convertir los segundos restantes a minutos
        diferencia.seconds % 60  # Obtener los segundos restantes
    ))

    # Verificar si hoy es la fecha especial
    if fecha_actual >= fecha_especial:
        print("Feliz 2 años y un mes? WOOOOOOOOOOOOOOOOOOOOOW it's insane")
        print("""
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛🟥🟥🟥🟥🟥⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜⬜⬜⬜⬜
⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜⬜⬜⬜
⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜⬜⬜⬜
⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛⬛🟥🟥🟥⬛⬜⬜⬜⬜⬜
⬜⬛🟥🟥🟥🟥🟥🟥⬛⬛⬜⬛🟥🟥🟥⬛⬜⬜⬜⬜⬜
⬜⬛🟥🟥🟥🟥🟥⬛⬜⬜⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟥🟥🟥⬛⬜⬜⬜⬛🟥🟥🟥⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟥🟥⬛⬜⬜⬜⬛🟥🟥🟥🟥⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟥🟥🟥⬛⬛⬛🟥🟥🟥⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥⬛🟥⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟥🟥🟥🟥⬛⬛🟥🟥⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛🟥⬛🟥🟥🟥🟥⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜⬜
⬜⬜⬛🟥⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬜⬛⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟦🟥🟥🟥🟥⬛⬜⬜
⬜⬜⬛⬛⬛🟥⬛🟥⬛⬛🟥🟦🟦🟦🟦🟦🟥🟥🟥⬛⬜
⬜⬛🟥⬛🟥⬛⬛⬛🟥🟥🟥🟦🟦🟦🟦🟦🟦🟥🟥⬛⬜
⬜⬛🟥⬛⬛🟥⬛🟥⬛⬛🟦🟦🟦⬛⬛🟦🟦🟦🟥⬛⬜
⬜⬛🟥⬛🟥⬛⬛⬛🟥🟥🟦🟦⬛⬜⬜⬛🟦🟦🟦🟥⬛
⬜⬛🟥⬛🟥🟥⬛🟥🟥🟦🟦⬛⬜⬜⬜⬛🟦🟦🟦🟥⬛
⬜⬜⬛⬛🟥🟥🟥🟥🟦🟦🟦⬛⬜⬜⬜⬜⬛🟦🟦🟥⬛
⬜⬛🟥⬛🟥🟥🟥🟥🟥🟦🟦⬛⬜⬜⬜⬜⬛🟦🟦🟥⬛
⬜⬛🟥⬛⬛🟥🟥🟥🟥🟦🟦🟦⬛⬜⬜⬜⬛🟦🟦🟥⬛
""")
        break

    # Esperar un segundo antes de volver a verificar
    time.sleep(1)
