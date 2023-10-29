import streamlit as st
from UIclients import ClienteUI
from UIservicos import ServicoUI
from UIagenda import AgendaUI
#from XXXX import AbrirAgendaUI

class IndexUI:
  
  def sidebar():
      op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda"])
      if op == "Manter Clientes": st.session_state["page"] = "manter_clienteUI"
      if op == "Manter Serviços": st.session_state["page"] = "manter_servicoUI"
      if op == "Manter Agenda": st.session_state["page"] = "manter_agendaUI"
      # if op == "Abrir Agenda do Dia": st.session_state["page"] = "abrir_agendaUI"


  def main():
      IndexUI.sidebar()
      if "page" not in st.session_state: st.session_state["page"] = "manter_clienteUI"
      if st.session_state["page"] == "manter_clienteUI": ClienteUI.main()
      if st.session_state["page"] == "manter_servicoUI": ServicoUI.main()
      if st.session_state["page"] == "manter_agendaUI": AgendaUI.main()
      # if st.session_state["page"] == "abrir_agendaUI": AbrirAgendaUI.main()
