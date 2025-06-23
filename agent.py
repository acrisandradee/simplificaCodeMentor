import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


class Agent:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.llm = ChatOpenAI(
            model_name="openai/gpt-3.5-turbo",  
            temperature=0.7,
            openai_api_base="https://openrouter.ai/api/v1",
            openai_api_key=self.api_key,
        )
        
        template = template = """
Você é uma mentora virtual experiente em orientar pessoas na área de tecnologia.

Com base nas informações fornecidas a seguir, elabore um plano de estudos totalmente personalizado, com duração de 12 semanas. O objetivo é ajudar essa pessoa a aprender de forma consistente, respeitando seu tempo disponível e seu nível atual de conhecimento.

Informações do(a) mentorado(a):
- Área de interesse: {area}
- Nível atual: {nivel}
- Tempo disponível por semana: {tempo}
- Conhecimentos prévios: {conhecimentos}
- Escolaridade: {escolaridade}

 Regras para criar o plano:
- Divida o plano em 12 semanas, com tópicos claros para cada semana.
- Sugira fontes de estudo confiáveis: links gratuitos, plataformas acessíveis e, se possível, livros gratuitos ou de baixo custo.
- Adapte a linguagem e o nível de profundidade dos conteúdos à experiência e escolaridade da pessoa.
- Ao final do plano, inclua dicas de temas mais avancadoa ao nivel em que a pessoa esta para que ela evolua mais.
- Ao final de cada semana proponha um exercício prático com foco em construção de portfólio.
"""


        prompt = ChatPromptTemplate.from_template(template)
        self.chain = LLMChain(llm=self.llm, prompt=prompt)

    def get_mentorship(self, input_data: dict) -> str:
        return self.chain.run(input_data)
