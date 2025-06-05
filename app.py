import streamlit as st
import re # Importa o módulo re para expressões regulares

st.set_page_config(page_title="Limpador de Texto", layout="centered")

st.title("🧹 Limpador de Texto")

texto_original = st.text_area("Cole aqui o texto que deseja limpar:", height=200)

# Não precisamos mais de palavras_personalizadas se usarmos regex para o caso específico de "Acréscimos"
# palavras_personalizadas = st.text_input("Palavras/padrões a remover (separadas por vírgula)", value="Acréscimos:")

def limpar_texto(texto):
    # Expressão regular para encontrar "Acréscimos: " seguido por R$ e um valor numérico (com vírgula e ponto)
    # e substituir por uma string vazia
    texto_limpo = re.sub(r'Acréscimos: R\$ [\d\.,]+', '', texto)
    return texto_limpo

if st.button("Limpar Texto"):
    # Chamamos a função sem as palavras personalizadas, pois a regex já lida com "Acréscimos"
    texto_limpo = limpar_texto(texto_original)
    st.text_area("Texto Limpo:", value=texto_limpo, height=200)

    st.download_button("📋 Copiar texto limpo", texto_limpo, file_name="texto_limpo.txt")
