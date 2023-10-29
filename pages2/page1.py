import streamlit as st
import pandas as pd

class Curso:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome

x = Curso("InfoWeb", "Técnico em Informática para Internet")
y = Curso("Tads", "Tecnologia em Análise e Desenvolvimento de Sistemas")

st.write("Página 01")
z = [ x.__dict__, y.__dict__ ]

df = pd.DataFrame(z)
st.dataframe(df)

