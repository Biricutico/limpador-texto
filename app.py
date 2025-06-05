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
    st.text_area("Texto Limpo:", value=texto_limpo, height=200, key="cleaned_text_area") # Adicionei um key aqui

    # Remove o botão de download
    # st.download_button("📋 Copiar texto limpo", texto_limpo, file_name="texto_limpo.txt")

    # Adiciona o botão de cópia usando HTML e JavaScript
    # O JavaScript copiará o conteúdo do st.text_area com a key "cleaned_text_area"
    copy_button_html = f"""
    <button onclick="
        var textArea = document.getElementById('cleaned_text_area');
        if (textArea) {{
            textArea.select();
            document.execCommand('copy');
            alert('Texto copiado para a área de transferência!');
        }} else {{
            alert('Erro: Área de texto limpa não encontrada.');
        }}
    ">📋 Copiar Texto Limpo</button>
    """
    st.markdown(copy_button_html, unsafe_allow_html=True)

    # Nota: A mensagem de "Texto copiado..." aparecerá como um alerta do navegador.
    # Você pode personalizar o feedback ao usuário se quiser (ex: um st.success)
    # mas o copy para a área de transferência só é garantido pelo JavaScript.
