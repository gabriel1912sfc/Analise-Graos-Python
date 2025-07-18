# 🔬 Análise de Tamanho de Grãos com Python e Visão Computacional

Este projeto utiliza técnicas de **visão computacional** e **processamento de imagens com Python** para identificar, medir e exportar dados sobre o tamanho de grãos metálicos presentes em fotomicrografias. Uma interface interativa foi criada com **Streamlit** para facilitar o uso.

---

## 🚀 Funcionalidades

- Upload de imagens de microestruturas
- Binarização automática com método de Otsu
- Operações morfológicas (erosão e dilatação) para limpeza
- Segmentação por rotulagem (labeling)
- Medição automática de propriedades de cada grão:
  - Área (µm²)
  - Perímetro (µm)
  - Diâmetro equivalente
  - Eixos maior e menor
  - Intensidade mínima, média e máxima (tons de cinza)
- Geração de arquivo CSV com os dados extraídos
- Visualização colorida com identificação de grãos

---

## 🧠 Tecnologias e Bibliotecas

- `Python 3.10+`
- [`Streamlit`](https://streamlit.io/) — Interface interativa
- `OpenCV (opencv-python-headless)` — Processamento de imagem
- `NumPy` — Operações numéricas
- `SciPy` — Rotulagem de regiões conectadas
- `Scikit-image` — Extração de propriedades e manipulação de imagens
- `Pandas` — Exportação de dados em CSV
- `Matplotlib` — Visualização de dados (opcional)

---

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/analise-graos-python.git
   cd analise-graos-python

---

## 📊 Exemplo de Resultado
Após o upload da imagem, você verá:

- A imagem original em tons de cinza

- Máscara binarizada e processada

- Grãos rotulados em cores diferentes

- Tabela com propriedades geométricas

- Botão para baixar os dados em CSV

---


## 📚 Base Científica
Este projeto segue princípios da norma ASTM E112 para determinação do tamanho médio de grãos metálicos, e compara resultados obtidos com Python com os de softwares como ImageJ.

🧾 Reconhecimento: Este trabalho foi aceito e apresentado no
📍 CBECiMat 2022 – Congresso Brasileiro de Engenharia e Ciência dos Materiais, consolidando sua importância acadêmica na caracterização de materiais.