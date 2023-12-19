import geocoder



def obtener_coordenadas_actual():
    # Usa el proveedor 'ipinfo' para obtener la ubicación basada en la dirección IP
    location = geocoder.ipinfo("me")
    cor = []
    # Verifica si la solicitud fue exitosa
    if location.ok:
        # Obtiene las coordenadas (latitud y longitud)
        latitud = location.latlng[0]
        longitud = location.latlng[1]
        cor.append(latitud)
        cor.append(longitud)
        return cor
    else:
        print(f"Error al obtener la ubicación: {location}")

# Obtiene las coordenadas de la ubicación actual
coordenadas_actuales = obtener_coordenadas_actual()

print(f"Coordenadas actuales: {coordenadas_actuales[0], coordenadas_actuales[1] }")
