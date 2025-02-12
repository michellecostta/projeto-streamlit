import streamlit as st
import pandas as pd
from datetime import date

# Função para gravar os dados no arquivo CSV
def gravar_dados(item_comprado, valor, data_compra):
    if data_compra > date.today():  # Verifica se a data é futura
        st.session_state["erro"] = True  # Define um estado de erro
        st.session_state["sucesso"] = False  # Garante que sucesso seja falso
    else:
        with open("gastos.csv", "a", encoding='utf-8') as file:  # Abre o arquivo no modo append
            file.write(f'{item_comprado};{valor};{data_compra}\n')  # Escreve os dados no CSV
        st.session_state["sucesso"] = True  # Define o estado de sucesso como True
        st.session_state["erro"] = False  # Reseta o estado de erro

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Gastos do mês",
    page_icon='💲'
)

st.title("Gastos do mês")
st.divider()

# Campos de entrada do usuário
item_comprado = st.text_input("Qual item comprado?", key="item_comprado")
valor = st.number_input("Quanto custou?")
data_compra = st.date_input("Data da compra", format="DD/MM/YYYY")

# Resetar erro ao modificar a data
if "erro" in st.session_state and st.session_state["erro"] and data_compra <= date.today():
    st.session_state["erro"] = False

# Botão para confirmar a inserção dos dados
botao = st.button("Confirme", on_click=gravar_dados, args=[item_comprado, valor, data_compra])

# Mensagens de feedback ao usuário
if st.session_state.get("erro", False):  # Verifica se houve erro na data
    st.error("Ei, já está pensando em gastar? Coloque um gasto de dias anteriores", icon="❌")
elif botao and st.session_state.get("sucesso", False):  # Verifica se a gravação foi bem-sucedida
    if valor < 100:
        st.success("Gasto registrado", icon="💸")
    else:
        st.success("Gasto registrado, mas...", icon="⚠")
        st.image("https://th.bing.com/th/id/R.e3318fc180b53a920ee265509904c968?rik=6hvdMQYxYZFqOg&pid=ImgRaw&r=0")
