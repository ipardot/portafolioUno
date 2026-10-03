import streamlit as st
from PIL import Image
st.title("Aplicaciones de Interfaces Multimodales.")

with st.sidebar:
  st.subheader("Interfaces Multimodales.")
  parrafo = (
    "Una interfaz multimodal permite interactuar con un sistema por varios canales a la vez, "
    "como la voz, el texto, las imágenes y los gestos. En estas clases las construimos con "
    "Python y Streamlit y las desplegamos en la nube, desde convertir texto en audio hasta reconocer objetos en imágenes."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/interfacesmultimodales/p%C3%A1gina-principal"
st.subheader("En el siguiente enlace puedes encontrar el material y los ejercicios de las clases")
st.write(f"Sitio de Interfaces Multimodales: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:

 st.subheader("Primera App: Interfaces Multimodales")
 image = Image.open('Inter1.png')
 st.image(image, width=200)
 st.write("Clase 6. En el siguiente enlace veremos nuestra primera app con Streamlit: texto, imagen, columnas, casillas y selectores.")
 url = "https://intro-a-interfaces-multimodales-7wefpdompzu8vap2tdsjxg.streamlit.app/#pantalla-de-seleccion-2-ranuras"
 st.write(f"Intro: [Enlace]({url})")

 st.subheader("Conversión de texto a voz")
 image = Image.open('textovoz.png')
 st.image(image, width=200)
 st.write("Clase 6. En el siguiente enlace veremos la app de interfaces multimodales que convierte el texto que escribes en audio usando gTTS.")
 url = "https://au3bnnhwkgd5myvtms6dfm.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Traductor por voz")
 image = Image.open('traductor.png')
 st.image(image, width=200)
 st.write("Clase 7. En el siguiente enlace veremos una aplicación que convierte la voz en texto, lo traduce a otro idioma y lo reproduce en audio.")
 url = "https://traductor-mcnljjfcbyyqgygapvgpfs.streamlit.app/"
 st.write(f"Traductor: [Enlace]({url})")

with col2:
 st.subheader("Reconocimiento Óptico de Caracteres")
 image = Image.open('OCR.png')
 st.image(image, width=200)
 st.write("Clase 7. En los siguientes enlaces veremos cómo extraer texto de imágenes con OCR y cómo combinarlo con la conversión de texto a audio.")
 url = "https://agxi6ywcfrblrj2ndtdnmz.streamlit.app/"
 st.write(f"OCR: [Enlace]({url}) · OCR con audio: [Enlace](https://ocr-audio-973gqmmbmmxenjkvrkzard.streamlit.app/)")

 st.subheader("Análisis de Sentimientos")
 image = Image.open('emociones.png')
 st.image(image, width=200)
 st.write("Clase 8. En el siguiente enlace veremos cómo analizar la polaridad y la subjetividad de un texto y reaccionar con una animación.")
 url = "https://sentimientosc8-fxe4fkwgdulxpkg5jwxu9k.streamlit.app/"
 st.write(f"Sentimientos: [Enlace]({url})")

 st.subheader("Nube de Palabras")
 image = Image.open('nube.png')
 st.image(image, width=200)
 st.write("Clase 8. En el siguiente enlace veremos cómo visualizar la frecuencia de las palabras de un texto con una nube de palabras.")
 url = "https://wordcloudc8-ee6oaebcyqvww7fnennmva.streamlit.app/"
 st.write(f"Nube de palabras: [Enlace]({url})")


with col3:
 st.subheader("Análisis de Texto: TF-IDF")
 image = Image.open('tf.png')
 st.image(image, width=200)
 st.write("Clase 8. En el siguiente enlace veremos cómo calcular TF-IDF para medir la importancia de los términos en textos en español.")
 url = "https://tdfespc8-6nbr9smosu5gbih2cphtuz.streamlit.app/"
 st.write(f"TF-IDF: [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos")
 image = Image.open('reconocimientoObj.png')
 st.image(image, width=200)
 st.write("Clase 9. En el siguiente enlace veremos cómo YOLO detecta y clasifica los objetos de una imagen en una sola pasada.")
 url = "https://yolov5c9-uzcaomnbwg4wbok958iq9t.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('entrenamiento.png')
 st.image(image, width=200)
 st.write("Clase 9. En el siguiente enlace veremos cómo usar un modelo entrenado con Teachable Machine para reconocer patrones en fotos tomadas con la cámara.")
 url = "https://er58appxjtynyhlnj8f6qme.streamlit.app/"
 st.write(f"Teachable Machine: [Enlace]({url})")
