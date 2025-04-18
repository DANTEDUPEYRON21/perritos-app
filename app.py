import streamlit as st
import requests

# URL de la API de The Dog API
API_URL = "https://api.thedogapi.com/v1/images/search"
API_KEY = "tu_clave_api_aqui"  # Asegúrate de reemplazar esto por tu API Key real

# Título de la aplicación
st.title("🌸 ¡Bienvenida a los perritos de Hebe! 🌸")

# Función para obtener los datos del perro
def obtener_perrito():
    headers = {"x-api-key": API_KEY}
    response = requests.get(API_URL, headers=headers)
    data = response.json()

    # Extraemos la URL de la imagen y otros detalles del perro
    image_url = data[0]['url']
    breed = data[0]['breeds'][0] if 'breeds' in data[0] else {}
    breed_name = breed.get('name', 'Desconocida')
    temperament = breed.get('temperament', 'Desconocido')
    height = breed.get('height', {}).get('imperial', 'Desconocido')
    weight = breed.get('weight', {}).get('imperial', 'Desconocido')
    life_span = breed.get('life_span', 'Desconocida')
    origin = breed.get('origin', 'Desconocido')
    colors = breed.get('color', 'Desconocido')
    description = breed.get('description', 'No disponible')

    # Mostramos la imagen y los detalles del perro
    st.image(image_url, use_container_width=True)
    st.subheader(f"🐶 Nombre de la raza: {breed_name}")
    st.write(f"🌟 Temperamento: {temperament}")
    st.write(f"📏 Altura: {height} pulgadas")
    st.write(f"⚖️ Peso: {weight} libras")
    st.write(f"💖 Esperanza de vida: {life_span} años")
    st.write(f"🌍 Origen: {origin}")
    st.write(f"🎨 Colores: {colors}")
    st.write(f"📖 Descripción: {description}")
    st.write("¡Qué lindo es este perrito! 😊")

# Botón para mostrar un perrito aleatorio
if st.button("¡Mostrar un perrito adorable!"):
    obtener_perrito()

# Mensaje de bienvenida más cálido
st.write("""
¡Hola querida! 🌸 Esta es una aplicación especial para ti, donde podrás ver perritos adorables y aprender un poco sobre ellos. 
Haz clic en el botón para conocer un perrito nuevo y descubrir todos sus detalles. ¡Disfrútalo mucho! 💖
""")