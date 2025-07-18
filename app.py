import streamlit as st
import cv2
import numpy as np
from skimage import measure, color, io
from scipy import ndimage
import pandas as pd
from matplotlib import pyplot as plt
from io import BytesIO

# Configuração inicial da página
st.set_page_config(layout="wide")
st.title("🔬 Análise de Tamanho de Grãos com Python")

# Parâmetro de conversão
microns_por_pixel = st.sidebar.number_input("Micrômetros por pixel:", value=0.5)

# Upload da imagem
imagem_upload = st.file_uploader("Envie uma imagem de microestrutura", type=["jpg", "png", "jpeg"])

if imagem_upload:
    # Leitura da imagem em escala de cinza
    file_bytes = np.asarray(bytearray(imagem_upload.read()), dtype=np.uint8)
    imagem = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    st.image(imagem, caption="Imagem original (escala de cinza)", use_container_width=True)

    # Binarização automática com Otsu
    limiar, binarizada = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    st.image(binarizada, caption=f"Binarização com Otsu (limiar: {limiar:.2f})", use_container_width=True)

    # Operações morfológicas
    kernel = np.ones((3, 3), np.uint8)
    limpa = cv2.dilate(cv2.erode(binarizada, kernel, iterations=1), kernel, iterations=1)
    mascara = limpa == 255

    st.image(mascara.astype(np.uint8)*255, caption="Máscara final após erosão/dilatação", use_container_width=True)

    # Etiquetagem dos grãos
    estrutura = np.ones((3, 3))
    rotulada, n_grãos = ndimage.label(mascara, structure=estrutura)
    st.success(f"🔍 {n_grãos} grãos detectados")

    imagem_colorida = color.label2rgb(rotulada, bg_label=0)
    st.image(imagem_colorida, caption="Imagem com grãos rotulados", use_container_width=True)

    # Medição das propriedades
    props = measure.regionprops(rotulada, intensity_image=imagem)

    propriedades = [
        "area", "equivalent_diameter", "orientation",
        "major_axis_length", "minor_axis_length",
        "perimeter", "min_intensity", "mean_intensity", "max_intensity"
    ]

    dados = []
    for prop in props:
        linha = {}
        for nome in propriedades:
            valor = getattr(prop, nome)
            if nome == "area":
                valor *= microns_por_pixel ** 2
            elif nome == "orientation":
                valor = np.degrees(valor)
            elif "intensity" not in nome:
                valor *= microns_por_pixel
            linha[nome] = valor
        dados.append(linha)

    df = pd.DataFrame(dados)
    st.dataframe(df.head())

    # Download do CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Baixar CSV com dados", csv, "medidas_graos.csv", "text/csv")
