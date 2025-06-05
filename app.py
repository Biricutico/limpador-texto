import streamlit as st
import re
from st_copy_to_clipboard import st_copy_to_clipboard # Importa o componente

st.set_page_config(page_title="Limpador de Texto", layout="centered")

st.title("🧹 Limpador de Texto")

texto_original = st.text_area("Cole aqui o texto que deseja limpar:", height=200)

palavras_personalizadas = st.text_input("Outras palavras/padrões a remover (separadas por vírgula)", value="")

def limpar_texto(texto, palavras_adicionais):
    texto_limpo = re.sub(r'Acréscimos: R\$ [\d\.,]+', '', texto)

    for palavra in palavras_adicionais:
        texto_limpo = texto_limpo.replace(palavra, "")
    return texto_limpo

if st.button("Limpar Texto"):
    palavras = [p.strip() for p in palavras_personalizadas.split(",") if p.strip()]
    texto_limpo = limpar_texto(texto_original, palavras)

    st.text_area("Texto Limpo:", value=texto_limpo, height=200, key="cleaned_text_area")

    # Usar o componente st_copy_to_clipboard
    st_copy_to_clipboard(texto_limpo, label="📋 Copiar Texto Limpo")

    # Opcional: Feedback ao usuário (Streamlit pode não atualizar instantaneamente após a cópia pelo componente)
    # st.success("Texto copiado para a área de transferência!")
