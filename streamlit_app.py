import streamlit as st

# Título da aplicação
st.set_page_config(page_title="Chavruta Digital", layout="centered")
st.title("🕍 Chavruta Digital")

# Introdução
st.markdown("""
Bem-vindo à Chavruta Digital — um espaço para estudo colaborativo da Torá e textos judaicos.  
Aqui você pode compartilhar insights, levantar questões e explorar interpretações com outros estudantes.
""")

# Área de entrada de texto
st.subheader("📖 Texto para estudo")
texto = st.text_area("Cole aqui o trecho que deseja estudar", height=200)

# Área de perguntas e reflexões
st.subheader("💬 Reflexões e perguntas")
reflexoes = st.text_area("Escreva suas reflexões, dúvidas ou comentários", height=150)

# Botão para enviar
if st.button("Enviar contribuição"):
    if texto.strip() == "" or reflexoes.strip() == "":
        st.warning("Por favor, preencha os dois campos antes de enviar.")
    else:
        st.success("Contribuição enviada com sucesso! Obrigado por compartilhar seu estudo.")
        # Aqui você pode adicionar lógica para salvar os dados em um banco ou arquivo

# Rodapé
st.markdown("---")
st.caption("Desenvolvido por Traiffson • Projeto Chavruta Digital © 2025")
