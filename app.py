import streamlit as st
import google.generativeai as genai

st.title("Chavruta Digital 🤝📖")

api_key = st.text_input("Cole sua chave da API Gemini aqui", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    pergunta = st.text_area("Digite sua pergunta sobre o texto sagrado:")
    
    if st.button("Perguntar"):
        resposta = model.generate_content(pergunta)
        st.markdown("### Resposta:")
        st.write(resposta.text)
