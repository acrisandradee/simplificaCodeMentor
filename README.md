# simplificaCodeMentor

# 🧠 Mentor Virtual com IA

Aplicação desenvolvida com  Streamlit, LangChain e OpenRouter para gerar planos de estudos personalizados diversas áreas da tecnologia.

## 🚀 Funcionalidades

- Interface interativa via Streamlit
- Geração de plano de estudo de 12 semanas com base em:
  - Área de interesse
  - Nível atual
  - Tempo disponível
  - Escolaridade
  - Conhecimentos prévios
- Sugestão de fontes para estudo gratuitas e acessíveis
- Exercícios práticos com foco em construção de portfólio

## 🛠️ Tecnologias Utilizadas
  <p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />

  <img src="https://img.shields.io/badge/LangChain-1C3C3C.svg?style=for-the-badge&logo=LangChain&logoColor=white" />
  
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
 <img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" />

  
</p>

## 📦 Como executar

1. Clone este repositório
   ```bash
   git clone https://github.com/seu-usuario/mentor-virtual.git
   cd mentor-virtual

2. Crie e ative um ambiente virtual
   ```bash
   python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate

 3. Instale as dependências
   ```bash
pip install -r requirements.txt
```

4. Configure sua chave da API
   ```bash
    OPENROUTER_API_KEY=sk-xxxxxxx
5. Instale o Streamlit dentro do ambiente virtual
   ```bash
   pip install streamlit
 
6. Instale o langChain dentro do ambiente virtual
   ```bash
  pip install langchain

▶️ Como executar
   ```bash
streamlit run app.py
````
 ```bash
#📁 Estrutura do Projeto
simplificaCodeMentor/
├── .venv                Ambiente virtual Python 
├── app.py               Configuração da Interface Streamlit
├── agent.py             Classe Agent com LangChain e integração LLM
├── .env                 Chave da API do OpenRouter 
├── .gitignore          Arquivos e pastas ignoradas no Git 
├── requirements.txt     Lista de dependências Python do projeto
└── README.md            Documentação do projeto

````
 
---

<div align="center">

✨ Desenvolvido por **Cristina Andrade** – 2025  

Engenheira da Computação - CREA 2024107872

Aplicação de LLMs com Streamlit para mentoria inteligente personalizada
Construído com LangChain, OpenRouter, Streamlit e boas práticas de IA aplicada.



</div>
