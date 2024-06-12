from unittest import result
from cv2 import sqrt
import streamlit as st
import pandas as pd


#Estrutura básica de uma aplicação

st.title('Titulo da aplicação')

st.header('Cabeçalho Secundário')

st.subheader('Subcabeçalho Terciário')

st.text('Este é um texto simples.')

st.markdown('**Este é um texto em negrito usando Markdown.**')



st.sidebar.title('Título na Barra Lateral')
st.sidebar.markdown('Texto na barra lateral.')


#Widgets interativos


col1, col2 = st.columns(2)
col1.write('Este é o conteúdo da primeira coluna.')
col2.write('Este é o conteúdo da segunda coluna.')


#botões
if col1.button('Clique aqui'):
    col1.write('Botão clicado!')


#Caixa de seleção
if col2.checkbox('Marque-me'):
    	    col2.write('Caixa marcada!')


#Sliders
age = col1.slider('Selecione sua idade', 0, 100, 18)
col1.write(f'Sua idade é: {age}')
#inputs
nome = col2.text_input('Digite seu nome')
col2.write(f'Seu nome é: {nome}')



# Exibição de texto e dados

#DataFrames
data = {'Coluna 1': [1, 2, 3], 'Coluna 2': [4, 5, 6]}
df = pd.DataFrame(data)
st.write(df)

#Tabela do Streamlit, não sofre alterações
st.table(df)




#Calculadora
numero1 = st.number_input("Digite um número")
numero2 = st.number_input("Digite outro número")

operacao = st.selectbox("Escolha a operação (+, -, *, **, sqrt)", ("+", "-","*", "**", "sqrt"))

if operacao == "+":
        resultado = numero1 + numero2
elif operacao == "-":
        resultado = numero1 - numero2
elif operacao == "*":
        resultado = numero1 * numero2
elif operacao == "**":
        resultado = numero1 ** numero2
elif operacao == "/":
    if numero2 == 0:
        resultado = "Não é possível dividir por 0"
    else:
        resultado =  numero1 / numero2      
elif operacao == "sqrt":
        #Não exite raiz par de numero negativo
        if numero2%2 == 0 and numero1 < 0:
               erro = "Não é possivel raiz par de n° negativo"
               st.write(erro)
        else:
            resultado = numero1 ** (1/numero2)

st.write(resultado)