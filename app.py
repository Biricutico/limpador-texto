import streamlit as st

st.set_page_config(page_title="Limpador de Texto", layout="centered")

st.title("🧹 Limpador de Texto")

texto_original = st.text_area("Cole aqui o texto que deseja limpar:", height=200)

palavras_personalizadas = st.text_input("Palavras/padrões a remover (separadas por vírgula)", value="Acréscimos:")

def limpar_texto(texto, palavras):
    for palavra in palavras:
        texto = texto.replace(palavra, "")
    return texto

if st.button("Limpar Texto"):
    palavras = [p.strip() for p in palavras_personalizadas.split(",") if p.strip()]
    texto_limpo = limpar_texto(texto_original, palavras)
    st.text_area("Texto Limpo:", value=texto_limpo, height=200)
    
    st.download_button("📋 Copiar texto limpo", texto_limpo, file_name="texto_limpo.txt")
