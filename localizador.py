import geocoder

class Localizador:
    
    def obtener_coordenadas_actual(self):
        coordenadas = []
        location = geocoder.ipinfo("me")
        if location.ok:
            latitud = location.latlng[0]
            longitud = location.latlng[1]
            coordenadas.append(latitud)
            coordenadas.append(longitud)
            return coordenadas
        else:
            print(f"Error al obtener la ubicación: {location}")
    