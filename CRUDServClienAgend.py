import os, json
class Client:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_fone(self, fone):
        self.__fone = fone
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def __str__(self):
        return f"{self.get_id()} {self.get_nome()} {self.get_email()} {self.get_fone()}"
class Servico:
    def __init__(self, id, descricao, valor, duracao):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
        self.__duracao = duracao
    def set_id(self, id):
        self.__id = id
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_valor(self, valor):
        self.__valor = valor
    def set_duracao(self, duracao):
        self.__duracao = duracao
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_valor(self):
        return self.__valor
    def get_duracao(self):
        return self.__duracao 
    def __str__(self): 
        return f"{self.get_id()} {self.get_descricao()} {self.get_valor()} {self.get_duracao()}"
class Agenda:
  def __init__(self, id, data, confirmado, id_cliente, id_servico):
    self.__id = id
    self.__data = data
    self.__confirmado = confirmado
    self.__id_cliente = id_cliente
    self.__id_servico = id_servico

  def get_id(self): return self.__id
  def get_data(self): return self.__data
  def get_confirmado(self): return self.__confirmado
  def get_id_cliente(self): return self.__id_cliente
  def get_id_servico(self): return self.__id_servico

  def set_id(self, id): self.__id = id
  def set_data(self, data): self.__data = data
  def set_confirmado(self, confirmado): self.__confirmado = confirmado
  def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
  def set_id_servico(self, id_servico): self.__id_servico = id_servico

  def __eq__(self, x):
    if self.__id == x.__id and self.__data == x.__data and self.__confirmado == x.__confirmado and self.__id_cliente == x.__id_cliente and self.__id_servico == x.__id_servico:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado} - {self.__id_cliente} - {self.__id_servico}"

  def to_json(self):
    return {
      'id': self.__id,
      'data': self.__data.strftime('%d/%m/%Y %H:%M'),
      'confirmado': self.__confirmado,
      'id_cliente': self.__id_cliente,
      'id_servico': self.__id_servico}
class NCliente:
  __clientes = []         # lista de clientes inicia vazia
  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0 # encontrar o maior id já usado
    for cliente in cls.__clientes:
      if cliente.get_id() > id: id = cliente.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)  # insere um cliente (obj) na lista
    NCliente.salvar()
  @classmethod
  def listar(cls):
    NCliente.abrir()    
    return cls.__clientes       # retorna a lista de clientes
  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for cliente in cls.__clientes:
      if cliente.get_id() == id: return cliente
    return None
  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
    NCliente.salvar()
  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cls.__clientes.remove(cliente)    
    NCliente.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("clientes.json", mode="r") as f:
        s = json.load(f)
        for cliente in s:
          c = Client(cliente["_Client__id"], cliente["_Client__nome"], cliente["_Client__email"], cliente["_Client__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as f:
      json.dump(cls.__clientes, f, default=vars)
import json
import datetime




class NAgenda:
  __agendas = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__agendas:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__agendas.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__agendas

  @classmethod
  def listar_nao_confirmados(cls):
    cls.abrir()
    nao_confirmados = []
    aux = datetime.datetime.now()
    hoje = datetime.datetime(aux.year, aux.month, aux.day)
    for aux in cls.__agendas:
      if not aux.__confirmado and aux.__data > hoje:
        nao_confirmados.append(aux)
    return nao_confirmados

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__agendas:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_data(obj.get_data())
      aux.set_confirmado(obj.get_confirmado())
      aux.set_id_cliente(obj.get_id_cliente())
      aux.set_id_servico(obj.get_id_servico())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__agendas.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__agendas = []
    try:
      with open("agendas.json", mode="r") as arquivo:
        agendas_json = json.load(arquivo)
        for obj in agendas_json:
          aux = Agenda(
            obj["id"],
            datetime.datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"),
            obj["confirmado"], obj["id_cliente"], obj["id_servico"])
          cls.__agendas.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("agendas.json", mode="w") as arquivo:
      json.dump(cls.__agendas, arquivo, default=Agenda.to_json)
# class UI:
#     @classmethod
#     def main(cls):
#         op = 0
#         while op != 99:
#            op = UI.Menu()
#            if op == 1: UI.ClientInserir()
#            elif op == 2: UI.ClientListar()
#            elif op == 3: UI.ClientAtualizar()
#            elif op == 4: UI.ClientExcluir()
#            elif op == 5: UI.ServicoInsert()
#            elif op == 6: UI.ServicoList()
#            elif op == 7: UI.ServicoAtualizar()
#            elif op == 8: UI.ServicoExcluir()
#            elif op == 9: UI.AgendaInserir()
#            elif op == 10: UI.AgendaListar()
#            elif op == 11: UI.AgendaAtualizar()
#            elif op == 12: UI.AgendaExcluir()
       
#     @classmethod
#     def Menu(cls):
#         print("1-inserir cliente 2-listar clientes 3-atualizar cliente 4-excluir cliente")
#         print("5-inserir Servico 6-listar Servicos 7-atualizar Servico 8-excluir Servico")
#         print("9-inserir Agenda 10-listar Agenda 11-atualizar Agenda 12-excluir Agenda")
#         return int(input())
#     @classmethod
#     def ClientInserir(cls):
#         id = input("Id = ")
#         Nome = input("Nome = ")
#         Email = input("Email = ")
#         Fone = input("Fone = ")
#         A = Client(id, Nome, Email, Fone)
#         NCliente.insert(A)
#     @classmethod
#     def ClientListar(cls):
#         for i in NCliente.listar(): print(i)

#     @classmethod
#     def ClientAtualizar(cls):
#         id = input("Id = ")
#         Nome = input("Nome = ")
#         Email = input("Email = ")
#         Fone = input("Fone = ")
#         A = Client(id, Nome, Email, Fone)
#         NCliente.atualizar(A)
#     @classmethod
#     def ClientExcluir(cls):
#         Idtoremove = input("Id para remover = ")
#         A = Client(Idtoremove, "", "", "")
#         NCliente.excluir(A)

#     @classmethod
#     def AgendaInserir(cls):
#         id = input("Id = ")
#         Data = input("Data = ")
#         Confirmacao = input("Confirmacao = ")
#         Iddocliente = input("Id do cliente = ")
#         Iddoservico = input("Id do servico = ")
#         A = Agenda(id, Data, Confirmacao, Iddocliente, Iddoservico)
#         NAgenda.insert(A)
#     @classmethod
#     def AgendaListar(cls):
#         for i in NAgenda.listar(): print(i)

#     @classmethod
#     def AgendaAtualizar(cls):
#         id = input("Id = ")
#         Data = input("Data = ")
#         Confirmacao = input("Confirmacao = ")
#         Iddocliente = input("Id do cliente = ")
#         Iddoservico = input("Id do servico = ")
#         A = Agenda(id, Data, Confirmacao, Iddocliente, Iddoservico)
#         NAgenda.atualizar(A)
#     @classmethod
#     def AgendaExcluir(cls):
#         Idtoremove = input("Id para remover = ")
#         A = Agenda(Idtoremove, "", "", "")
#         NAgenda.excluir(A)
#     @classmethod
#     def ServicoInsert(cls):
#         id = input("Id = ")
#         descricao = input("descricao = ")
#         valor = input("valor = ")
#         duracao = input("duracao = ")
#         A = Servico(id, descricao, valor, duracao)
#         NServico.insert(A)
#     @classmethod
#     def ServicoList(cls):
#         for i in NServico.listar(): print(i)

#     @classmethod
#     def ServicoAtualizar(cls):
#         id = input("Id = ")
#         decricao = input("descricao = ")
#         valor = input("valor = ")
#         duracao = input("duracao = ")
#         A = Servico(id, decricao, valor, duracao)
#         NServico.atualizar(A)
#     @classmethod
#     def ServicoExcluir(cls):
#         Idtoremove = input("Id para remover = ")
#         A = Servico(Idtoremove, "", "", "")
#         NServico.excluir(A)
# UI.main()