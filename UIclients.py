import streamlit as st
import pandas as pd
from CRUDServClienAgend import NCliente
from CRUDServClienAgend import Client
class ClienteUI:
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            st.header("Lista de clientes")
            clientes = NCliente.listar()
            dic = []
            for c in clientes:
                dic.append(c.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)
        with tab2:
            st.header("Insira um cliente")
            nome = st.text_input("informe o seu nome")
            email = st.text_input("Informe o seu email")
            fone = st.text_input("Informe o seu fone")
            if st.button("Inserir"):
                cliente = Client(0, nome, email, fone)
                NCliente.inserir(cliente)
        with tab3:
            st.header("Atualize um cliente")
            clientes = NCliente.listar()
            dic = []
            for c in clientes:
                dic.append(c)
            df = pd.DataFrame(dic)
            option = st.selectbox(
                "Atualize",(df)
            )
            name = st.text_input("Edite o nome", option.get_nome())
            email = st.text_input("Edite o email", option.get_email())
            fone = st.text_input("Edite o fone", option.get_fone())
            if st.button("Atualizar"):
                cliente = Client(option.get_id(), name, email, fone)
                NCliente.atualizar(cliente)
        with tab4:
            st.header("Exclua um cliente")
            clientes = NCliente.listar()
            dic = []
            for c in clientes:
                dic.append(c)
            liste = pd.DataFrame(dic)
            opcaoexcluir = st.selectbox(
                "Exclua ou morra",(liste)
            )
            if st.button("Excluir"):
                NCliente.excluir(opcaoexcluir)