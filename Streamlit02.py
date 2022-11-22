# myFirstStreamlitApp.py
  
#import the library
import streamlit as st
import datetime

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Prof. Massaki de O. Igarashi")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Teste de Cabeçalho")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Bem vindos!")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

st.info("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

st.warning("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

start, end = st.date_input(label='Intervalo de Data: ',
              value=(datetime.datetime(year=2022, month=5, day=20, hour=16, minute=30), 
                     datetime.datetime(year=2022, month=5, day=30, hour=16, minute=30)),
              key='#date_range',
              help="Data e Início e Término",
              on_change=lambda : st.write("Configure a Data de Início e de Término!"))
st.write('Início: ', start, "Término: ", end)
