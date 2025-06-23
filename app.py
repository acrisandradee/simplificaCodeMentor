import streamlit as st
from agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

st.set_page_config(page_title="Simplifica.Code Mentor", layout="centered")
st.title("🧠 Simplifica.Code Mentor Virtual")


agent = Agent(api_key=API_KEY)

st.markdown("Preencha os dados abaixo para receber um plano de estudos personalizado com base no seu perfil.")

with st.form("form_mentor"):
    area = st.selectbox("📚 Qual sua area de Interesse", ["Front-end", "Back-end", "Dados", "IA/ML"])
    nivel = st.selectbox("📈 Qual o seu nível", ["Iniciante", "Intermediário", "Avançado"])
    tempo = st.selectbox("⏳ Tempo disponível por semana", ["<5h", "5-10h", "10-20h"])
    conhecimentos = st.text_area("🧠 Diga quais seus conhecimentos prévios")
    escolaridade = st.selectbox("🎓Qual o seu nivel de escolaridade", ["Ensino Médio", "Técnico", "Superior"])
    submitted = st.form_submit_button("Gerar plano de estudo 🔍 ")

if submitted:
    with st.spinner("🔍 Gerando seu plano de estudos..."):
        resposta = agent.get_mentorship({
            "area": area,
            "nivel": nivel,
            "tempo": tempo,
            "conhecimentos": conhecimentos,
            "escolaridade": escolaridade
        })
        st.success("✅ Plano gerado com sucesso!")
        st.markdown("---")
        st.markdown("### 📋 Seu Plano de Estudos Personalizado")
        st.markdown(resposta)
