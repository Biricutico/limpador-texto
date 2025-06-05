import streamlit as st
import re # Importa o módulo re para expressões regulares

st.set_page_config(page_title="Limpador de Texto", layout="centered")

st.title("🧹 Limpador de Texto")

texto_original = st.text_area("Cole aqui o texto que deseja limpar:", height=200)

# O campo "Palavras/padrões a remover" ainda pode ser útil para outras remoções,
# mas para "Acréscimos" usaremos uma lógica específica na função.
palavras_personalizadas = st.text_input("Outras palavras/padrões a remover (separadas por vírgula)", value="")

def limpar_texto(texto, palavras_adicionais):
    # 1. Remover "Acréscimos: " e o valor subsequente (R$ e o número)
    # A regex 'Acréscimos: R\$ [\d\.,]+' busca "Acréscimos: R$", seguido por um espaço,
    # e então um ou mais dígitos, pontos ou vírgulas (que representam o valor monetário).
    texto_limpo = re.sub(r'Acréscimos: R\$ [\d\.,]+', '', texto)

    # 2. Remover outras palavras/padrões especificados pelo usuário
    for palavra in palavras_adicionais:
        texto_limpo = texto_limpo.replace(palavra, "")

    return texto_limpo

if st.button("Limpar Texto"):
    # Prepara as palavras adicionais para remoção
    palavras = [p.strip() for p in palavras_personalizadas.split(",") if p.strip()]
    
    # Chama a função de limpeza
    texto_limpo = limpar_texto(texto_original, palavras)
    
    st.text_area("Texto Limpo:", value=texto_limpo, height=200, key="cleaned_text_area")

    # Adiciona o botão de cópia usando HTML e JavaScript
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
    " style="
        background-color: #4CAF50; /* Verde */
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    ">📋 Copiar Texto Limpo</button>
    """
    st.markdown(copy_button_html, unsafe_allow_html=True)
