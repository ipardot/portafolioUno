import streamlit as st
from PIL import Image

st.set_page_config(page_title="Interfaces Multimodales", page_icon="🎙️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

:root{
  --bg:#0b1020; --card:#141a33; --card2:#1b2347; --line:#2a3563;
  --violet:#8b7bff; --cyan:#4de1ff; --coral:#ff6b81; --text:#e8ecff; --muted:#aab3d9;
}

/* Fondo con brillos suaves */
.stApp{
  background:
    radial-gradient(900px 500px at 10% -10%, rgba(139,123,255,.25), transparent 60%),
    radial-gradient(800px 500px at 100% 0%, rgba(77,225,255,.18), transparent 60%),
    var(--bg);
  color:var(--text);
  font-family:'Poppins',sans-serif;
}
header[data-testid="stHeader"]{background:transparent;}

/* Título principal con degradado */
h1{
  font-family:'Poppins',sans-serif !important; font-weight:700 !important;
  background:linear-gradient(90deg,var(--cyan),var(--violet) 55%,var(--coral));
  -webkit-background-clip:text; background-clip:text; color:transparent !important;
  padding-bottom:.2rem;
}

/* Subtítulos */
h2,h3{font-family:'Poppins',sans-serif !important; color:var(--text) !important; font-weight:600 !important;}
h3{font-size:1.1rem !important; line-height:1.35 !important; min-height:3rem;}  /* 2 líneas reservadas */
h1 a, h2 a, h3 a{display:none !important;}  /* oculta el ícono de ancla */

/* Texto */
p, li, label, [data-testid="stMarkdownContainer"]{color:var(--muted);}
[data-testid="stMarkdownContainer"] p{font-size:.92rem; line-height:1.5;}

/* Enlaces */
a{color:var(--cyan) !important; text-decoration:none !important; font-weight:600;}
a:hover{color:var(--coral) !important; text-decoration:underline !important;}

/* Cada columna se convierte en una tarjeta */
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"],
[data-testid="stHorizontalBlock"] > [data-testid="column"]{
  background:linear-gradient(180deg,var(--card),var(--card2));
  border:1px solid var(--line);
  border-radius:20px;
  padding:1.2rem 1.2rem 1.4rem;
  box-shadow:0 10px 30px rgba(0,0,0,.35);
  transition:transform .25s ease, border-color .25s ease, box-shadow .25s ease;
}
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:hover,
[data-testid="stHorizontalBlock"] > [data-testid="column"]:hover{
  transform:translateY(-4px);
  border-color:var(--violet);
  box-shadow:0 16px 40px rgba(139,123,255,.25);
}

/* Imágenes centradas, con bordes redondeados (también compensa 190 vs 200 px) */
[data-testid="stImage"]{display:flex; justify-content:center; margin:.4rem 0 .8rem;}
[data-testid="stImage"] img{
  border-radius:16px;
  border:1px solid var(--line);
  box-shadow:0 6px 18px rgba(0,0,0,.4);
}

/* Barra lateral */
section[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#10163a,#0b1020);
  border-right:1px solid var(--line);
}
section[data-testid="stSidebar"] h3{min-height:0; color:var(--cyan) !important;}
</style>
""", unsafe_allow_html=True)

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

 st.subheader("Primera app multimodal")
 image = Image.open('Inter1.png')
 st.image(image, width=190)
 st.write("Clase 6. Nuestra primera app con Streamlit: texto, imagen, columnas, casillas y selectores en una sola interfaz.")
 url = "https://intro-a-interfaces-multimodales-7wefpdompzu8vap2tdsjxg.streamlit.app/#pantalla-de-seleccion-2-ranuras"
 st.write(f"Intro: [Enlace]({url})")

 st.subheader("Conversión de texto a voz")
 image = Image.open('textovoz.png')
 st.image(image, width=200)
 st.write("Clase 6. App que convierte el texto que escribes en audio con gTTS, la base de las interfaces multimodales.")
 url = "https://au3bnnhwkgd5myvtms6dfm.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Traductor por voz")
 image = Image.open('traductor.png')
 st.image(image, width=200)
 st.write("Clase 7. Convierte tu voz en texto, lo traduce a otro idioma y lo reproduce en audio con el acento elegido.")
 url = "https://traductor-mcnljjfcbyyqgygapvgpfs.streamlit.app/"
 st.write(f"Traductor: [Enlace]({url})")

with col2:
 st.subheader("Lectura de texto con OCR")
 image = Image.open('OCR.png')
 st.image(image, width=200)
 st.write("Clase 7. Extrae el texto de una imagen con OCR y lo deja listo para copiar o analizar. OCR con audio: [Enlace](https://ocr-audio-973gqmmbmmxenjkvrkzard.streamlit.app/)")
 url = "https://agxi6ywcfrblrj2ndtdnmz.streamlit.app/"
 st.write(f"OCR: [Enlace]({url})")

 st.subheader("Análisis de sentimientos")
 image = Image.open('emociones.png')
 st.image(image, width=190)
 st.write("Clase 8. Mide la polaridad y la subjetividad de un texto y reacciona con una animación según el resultado.")
 url = "https://sentimientosc8-fxe4fkwgdulxpkg5jwxu9k.streamlit.app/"
 st.write(f"Sentimientos: [Enlace]({url})")

 st.subheader("Nube de palabras")
 image = Image.open('nube.png')
 st.image(image, width=200)
 st.write("Clase 8. Muestra con una nube de palabras cuáles términos se repiten más en un texto y qué tan frecuentes son.")
 url = "https://wordcloudc8-ee6oaebcyqvww7fnennmva.streamlit.app/"
 st.write(f"Nube de palabras: [Enlace]({url})")


with col3:
 st.subheader("Análisis de texto TF-IDF")
 image = Image.open('tf.png')
 st.image(image, width=190)
 st.write("Clase 8. Calcula TF-IDF para medir qué tan importantes son los términos en textos escritos en español.")
 url = "https://tdfespc8-6nbr9smosu5gbih2cphtuz.streamlit.app/"
 st.write(f"TF-IDF: [Enlace]({url})")

 st.subheader("Reconocimiento de objetos")
 image = Image.open('reconocimientoObj.png')
 st.image(image, width=200)
 st.write("Clase 9. YOLO detecta y clasifica todos los objetos de una imagen en una sola pasada y los marca en la foto.")
 url = "https://yolov5c9-uzcaomnbwg4wbok958iq9t.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Entrenando modelos")
 image = Image.open('entrenamiento.png')
 st.image(image, width=200)
 st.write("Clase 9. Usa un modelo de Teachable Machine para reconocer patrones en fotos tomadas con la cámara.")
 url = "https://er58appxjtynyhlnj8f6qme.streamlit.app/"
 st.write(f"Teachable Machine: [Enlace]({url})")
