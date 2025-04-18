import streamlit as st
import requests
import random

# Configurar la clave de la API
api_key = "live_EpKs1MVg387J3r0Jy3VkHJpAjjTxOCuKAb1gqFW8yjjWGTYB4KfxCgVUlHXDUSWr"  

# URL base de la API
url = "https://api.thedogapi.com/v1/images/search"

# Función para obtener un perrito aleatorio
def obtener_perrito():
    headers = {
        'x-api-key': api_key
    }
    response = requests.get(url, headers=headers)
    
    # Si la respuesta es exitosa, obtenemos la información
    if response.status_code == 200:
        datos = response.json()
        imagen_url = datos[0]['url']
        descripcion = "Este es un perrito aleatorio."
        
        # Agregar datos adicionales si lo deseas
        return imagen_url, descripcion
    else:
        return None, "No se pudo obtener un perrito."

# Título de la página
st.title("PERROS HEBE")

# Botón para mostrar un perrito aleatorio
if st.button("Perrito"):
    imagen_url, descripcion = obtener_perrito()
    if imagen_url:
        # Mostrar la imagen y la descripción
        st.image(imagen_url, caption="Un perrito bonito", use_column_width=True)
        st.write(descripcion)
    else:
        st.write("Hubo un error al obtener la imagen del perrito.")