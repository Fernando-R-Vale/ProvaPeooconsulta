import streamlit as st
import pandas as pd
from CRUDServClienAgend import NAgenda
from CRUDServClienAgend import Agenda
class AgendaUI:
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            st.header("Lista de horarios")
            clientes = NAgenda.listar()
            dic = []
            for c in clientes:
                dic.append(c.__dict__)
            df = pd.DataFrame(dic)
            
            st.dataframe(df, hide_index=True)
        with tab2:
            st.header("Insira um Compromisso")
            nome = st.text_input('informe a data no seguinte formato DD/MM/YY HH:mm')
            email = st.text_input("Informe se está confirmado")
            fone = st.text_input("Informe o id do cliente")
            fone2 = st.text_input("Informe o id do serviço")
            if st.button("Inserir"):
                cliente = Agenda(0, nome, email, fone, fone2)
                NAgenda.inserir(cliente)
                st.success("Cliente excluído com sucesso")
                st.time.sleep(2)
                st.experimental_rerun()
        with tab3:
            st.header("Atualize um cliente")
            clientes = NAgenda.listar()
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
                cliente = Agenda(option.get_id(), name, email, fone)
                NAgenda.atualizar(cliente)
                st.success("Cliente excluído com sucesso")
                st.time.sleep(2)
                st.experimental_rerun()
        with tab4:
            st.header("Exclua um cliente")
            clientes = NAgenda.listar()
            dic = []
            for c in clientes:
                dic.append(c)
            liste = pd.DataFrame(dic)
            opcaoexcluir = st.selectbox(
                "Exclua ou morra",(liste)
            )
            if st.button("Excluir"):
                NAgenda.excluir(opcaoexcluir)
                st.success("Cliente excluído com sucesso")
                st.time.sleep(2)
                st.experimental_rerun()