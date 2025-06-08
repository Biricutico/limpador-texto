import streamlit as st
import re
from streamlit_copytoclipboard import st_copy_to_clipboard

st.set_page_config(page_title="Limpador de Texto", layout="centered")

st.title("🧹 Limpador de Texto")

texto_original = st.text_area("Cole aqui o texto que deseja limpar:", height=200)

palavras_personalizadas = st.text_input("Outras palavras/padrões a remover (separadas por vírgula)", value="")

def limpar_texto(texto, palavras_adicionais):
    texto = re.sub(r'Acréscimos:\s*R\$[\s\d\.,]+', '', texto)
    for palavra in palavras_adicionais:
        texto = texto.replace(palavra, "")
    return texto.strip()

texto_limpo = ""

if st.button("Limpar Texto"):
    palavras = [p.strip() for p in palavras_personalizadas.split(",") if p.strip()]
    texto_limpo = limpar_texto(texto_original, palavras)

if texto_limpo:
    st.text_area("Texto Limpo:", value=texto_limpo, height=200)
    st_copy_to_clipboard(texto_limpo, "📋 Copiar Texto Limpo")
