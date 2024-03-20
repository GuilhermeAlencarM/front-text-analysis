import streamlit as st
import requests
import json

# Configurando a página
st.set_page_config(page_title="Análise de Texto", page_icon=":memo:", layout="wide")

# Título da aplicação
st.title(':memo: Análise de Texto')

# Introdução
st.markdown("""
Bem-vindo ao Analisador de Texto! Esta ferramenta permite que você faça análise de sentimentos e detecção de idioma em textos.
""")

# Dividindo a página em duas colunas para análise de sentimentos e detecção de idioma
col1, col2 = st.columns(2)

with col1:
    # Seção de análise de sentimentos
    st.header(":smiley: Analisador de Sentimentos")
    user_input_sentiment = st.text_area("Insira o texto para análise de sentimento:", height=120, key="sentiment")

    # Botão para enviar a requisição de análise de sentimento
    if st.button('Analisar Sentimento', key="analyze_sentiment"):
        # URL da API para análise de sentimento
        url_sentiment = 'http://127.0.0.1:8000/api/detect/sentiment'

        # Corpo da requisição
        payload_sentiment = {"text": user_input_sentiment}
        
        # Realizando a requisição POST para a análise de sentimento
        response_sentiment = requests.post(url_sentiment, data=json.dumps(payload_sentiment), headers={'Content-Type': 'application/json'})

        # Verificando a resposta da análise de sentimento
        if response_sentiment.status_code == 200:
            result_sentiment = response_sentiment.json()
            st.success('Análise concluída:')
            st.json(result_sentiment)
        else:
            st.error('Falha na análise de sentimento. Verifique a API.')

with col2:
    # Seção de detecção de idioma
    st.header(":speech_balloon: Detector de Idioma")
    user_input_language = st.text_area("Insira o texto para detecção de idioma:", height=120, key="language")

    # Botão para enviar a requisição de detecção de idioma
    if st.button('Detectar Idioma', key="detect_language"):
        # URL da API para detecção de idioma
        url_language = 'http://127.0.0.1:8000/api/detect/language'

        # Corpo da requisição
        payload_language = {"text": user_input_language}
        
        # Realizando a requisição POST para a detecção de idioma
        response_language = requests.post(url_language, data=json.dumps(payload_language), headers={'Content-Type': 'application/json'})

        # Verificando a resposta da detecção de idioma
        if response_language.status_code == 200:
            result_language = response_language.json()
            st.success('Detecção concluída:')
            st.json(result_language)
        else:
            st.error('Falha na detecção de idioma. Verifique a API.')

# Espaço no final da página
st.markdown("---")
st.markdown("*Obrigado por usar nossa ferramenta de análise de texto!*")
