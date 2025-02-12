import streamlit as st
import pandas as pd

#dados = pd.read_csv("gastos.csv") #não estou colocando decoratir pq não é um grande volume de dados
dados = pd.read_csv("gastos.csv", names=["Item", "Valor", "Data"], sep=";", engine="python")

#pode copiar o caminho que esta o arquivo tbm,maso streamlit sabe onde esta o arquivo

#MAS CUIDADO ONDE COLOCA SEU ARQUIVO, COLOQUE NAS PASTAS CERTAS

# Garantir que a coluna 'Valor' seja numérica
dados["Valor"] = pd.to_numeric(dados["Valor"], errors="coerce")  # Isso converte valores inválidos para NaN


st.title("Gastos anotados")
st.divider()

st.dataframe(dados)

st.divider()
st.title("Soma dos gastos")
# Exibir soma total
total_gastos = dados["Valor"].sum()
st.markdown(f"**Total: R$ {total_gastos:.2f}**")


#aqui eu poderia colocar pra editar eu arquivo direto na pagina, colocar mais guias, colocar mais campos, colocar validação dos campos

#melhor coloca ; do que virgula na leitura dos campos