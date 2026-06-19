#Ejercicio Etapas de la vida 

edad = int(input("Escriba su edad: "))
if 0 <= edad < 10: 
    mensaje = "Infancia"
elif 10 <= edad < 20: 
    mensaje = "Adolescencia"
elif 20 <= edad < 30:
    mensaje = "juventud"
elif 30 <= edad < 40:
    mensaje = "adultez"
elif 40 <= edad < 50:
    mensaje = "adultez"
elif 50 <= edad < 60:
    mensaje = "madurez"
elif 60 <= edad < 70:
    mensaje = "vejez"
elif 70 <= edad < 80:
    mensaje = "vejez"
elif 80 <= edad < 90:
    mensaje = "vejez"
elif 90 <= edad < 100:
    mensaje = "longevidad"
else:
    mensaje = "Error, etapa de vida no reconocida"
print(f"Tu edad es: {edad}, {mensaje}")


