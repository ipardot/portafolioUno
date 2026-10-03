import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Conversión de texto a voz")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos la app de interfaces multimodales que convierte el texto que escribes en audio usando gTTS (clase 6).") 
 url = "https://au3bnnhwkgd5myvtms6dfm.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Primera App: Interfaces Multimodales")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos nuestra primera app con Streamlit: texto, imagen, columnas, casillas y selectores (clase 6).") 
 url = "https://intro-a-interfaces-multimodales-7wefpdompzu8vap2tdsjxg.streamlit.app/#pantalla-de-seleccion-2-ranuras"
 st.write(f"Intro: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo usar un modelo entrenado con Teachable Machine para reconocer patrones en fotos tomadas con la cámara (clase 9).") 
 url = "https://er58appxjtynyhlnj8f6qme.streamlit.app/"
 st.write(f"Teachable Machine: [Enlace]({url})")

with col2: 
 st.subheader("Traductor por voz")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos una aplicación que convierte la voz en texto, lo traduce a otro idioma y lo reproduce en audio (clase 7).") 
 url = "https://traductor-mcnljjfcbyyqgygapvgpfs.streamlit.app/"
 st.write(f"Traductor: [Enlace]({url})")

 st.subheader("Nube de Palabras")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos cómo visualizar la frecuencia de las palabras de un texto con una nube de palabras (clase 8).") 
 url = "https://wordcloudc8-ee6oaebcyqvww7fnennmva.streamlit.app/"
 st.write(f"Nube de palabras: [Enlace]({url})")

 st.subheader("Reconocimiento Óptico de Caracteres")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En los siguientes enlaces veremos cómo extraer texto de imágenes con OCR y cómo combinarlo con la conversión de texto a audio (clase 7).") 
 url = "https://agxi6ywcfrblrj2ndtdnmz.streamlit.app/"
 st.write(f"OCR: [Enlace]({url}) · OCR con audio: [Enlace](https://ocr-audio-973gqmmbmmxenjkvrkzard.streamlit.app/)")


with col3: 
 st.subheader("Análisis de Texto: TF-IDF")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos cómo calcular TF-IDF para medir la importancia de los términos en textos en español (clase 8).") 
 url = "https://tdfespc8-6nbr9smosu5gbih2cphtuz.streamlit.app/"
 st.write(f"TF-IDF: [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo YOLO detecta y clasifica los objetos de una imagen en una sola pasada (clase 9).") 
 url = "https://yolov5c9-uzcaomnbwg4wbok958iq9t.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")
 
 st.subheader("Análisis de Sentimientos")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo analizar la polaridad y la subjetividad de un texto y reaccionar con una animación (clase 8).") 
 url = "https://sentimientosc8-fxe4fkwgdulxpkg5jwxu9k.streamlit.app/"
 st.write(f"Sentimientos: [Enlace]({url})")
