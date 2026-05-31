from PySide6.QtCore import (QCoreApplication, QTimer)
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from ui_main import Ui_MainWindow
from PySide6.QtGui import QIcon
from ui_function import consulta_cnpj
from database import Data_base
from datetime import datetime
import sys


class MainWindow (QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Vendas Mozart")
        appIcon = QIcon(u"")
        #self.setWidowIcon(appIcon)
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.pesquisar_cliente)
    
        self.itens = []
        self.id_cliente = None
        self.id_pedido = None
        self.total = 0


        

        #############################################
        #TOGLEE BUTTON
        self.btn_toggle.clicked.connect(self.animar_menus)
        #self.btn_toggle.clicked.connect(self.logo_menu)
        #############################################
        #BOTOES DO MENU LATERAL

        pag_pedidos = lambda:self.paginas.setCurrentWidget(self.consulta_pedido)

        self.btn_home.clicked.connect(lambda:self.paginas.setCurrentWidget(self.home))
        self.btn_cadastrar_clientes.clicked.connect(lambda:self.paginas.setCurrentWidget(self.cadastro_cliente))
        self.btn_cadastrar_fornecedores.clicked.connect(lambda:self.paginas.setCurrentWidget(self.cadastro_fornecedor))
        self.btn_cadastrar_produtos.clicked.connect(lambda:self.paginas.setCurrentWidget(self.cadastro_produto))
        self.btn_cadastrar_usuarios.clicked.connect(lambda:self.paginas.setCurrentWidget(self.cadastro_usuario))
        self.btn_consultar_clientes.clicked.connect(lambda:self.paginas.setCurrentWidget(self.consulta_cliente))
        self.btn_inserir_cliente.clicked.connect(lambda:self.paginas.setCurrentWidget(self.consulta_cliente))
        self.btn_consultar_fornecedores.clicked.connect(lambda:self.paginas.setCurrentWidget(self.consulta_fornecedor))
        self.btn_consultar_pedidos.clicked.connect(pag_pedidos)
        self.btn_consultar_produtos.clicked.connect(lambda:self.paginas.setCurrentWidget(self.consulta_produto))
        self.btn_novo_pedido.clicked.connect(lambda:self.paginas.setCurrentWidget(self.pedido))
        self.btn_sair_venda.clicked.connect(lambda:self.paginas.setCurrentWidget(self.home))

        self.txt_pesquisar_cliente.textChanged.connect(self.delay_pesquisa)
        self.txt_pesquisar_tb_produto.textChanged.connect(self.delay_pesquisa)
        self.txt_pesquisar_tb_fornecedores.textChanged.connect(self.delay_pesquisa)
        self.txt_pesquisar_pedido.textChanged.connect(self.delay_pesquisa)
        self.txt_pesquisar_cliente.textChanged.connect(lambda: self.pesquisar_cliente())
        self.txt_pesquisar_tb_produto.textChanged.connect(lambda: self.pesquisar_produto())
        self.txt_pesquisar_tb_fornecedores.textChanged.connect(lambda: self.pesquisar_fornecedor())
        self.txt_pesquisar_pedido.textChanged.connect(lambda: self.pesquisar_pedido())

        #self.tb_clientes.itemDoubleClicked.connect(self.selecionar_com_duplo_clique)
        self.tb_clientes.itemDoubleClicked.connect(lambda item: self.selecionar_com_duplo_clique_teste(
            item, 
            id_selecionado=self.id_cliente, 
            tabela=self.tb_clientes, 
            qlineedit=self.txt_nome_cliente_venda, 
            pagina= self.pedido, 
            column = 1, 
            funcao=self.novo_pedido, 
            funcao_2 = None
            ))
        
        self.tb_pedidos.itemDoubleClicked.connect(lambda item: self.selecionar_com_duplo_clique_teste(
            item, 
            id_selecionado=self.tb_pedidos, 
            tabela=self.tb_pedidos, 
            qlineedit=self.txt_numero_pedido, 
            pagina= self.pedido, 
            column = 0, 
            funcao=self.novo_pedido, 
            funcao_2 = self.carregar_pedido_para_edicao
            ))

        #########################################################################################################
        # PREENCER OS DADOS FO FORNECEDOR 
        #self.txt_cnpj_fornecedor.editingFinished.connect(self.consult_api)
        self.btn_cnpj.clicked.connect(self.consult_api)
        self.cb_selecionar_produto.currentTextChanged.connect(self.completar_vendas)
        #######################################################################################################


        ###############################################################################################
        #BOTOES SALVAR
        self.btn_salvar_fornecedor.clicked.connect(self.cadastrar_fornecedor)
        self.btn_salvar_cliente.clicked.connect(self.cadastrar_cliente)
        self.btn_salvar_produto.clicked.connect(self.cadastrar_produto)
        self.btn_salvar_tb_clientes.clicked.connect(self.atualizar_cliente)
        ###############################################################################################

        #########################################################################################################
        # Ações painel de vendas 
        #self.txt_quantidade.editingFinished.connect(self.multiplica_item)
        
        self.txt_quantidade.textChanged.connect(self.multiplica_item)
        self.btn_finalizar_pedido.clicked.connect(self.salvar_pedido)
        self.btn_inserir_item.clicked.connect(self.inserir_item)
        self.btn_excluir_item.clicked.connect(self.excluir_item)
        self.btn_selecionar_cliente.clicked.connect(self.selecionar_cliente)
        self.btn_nova_venda.clicked.connect(self.novo_pedido)
        self.btn_sair_venda.clicked.connect(self.novo_pedido)
        self.btn_carregar_pedido.clicked.connect(self.carregar_pedido_para_edicao)

        #######################################################################################################



        self.combobox_tipo()
        self.buscar_fornecedor()
        self.buscar_cliente()
        self.buscar_produto()
        self.buscar_pedido()
        
        

    def animar_menus(self):

        width_menu = self.menu_lateral.width()
        width_logo = self.local_logo.width()

        # lógica do toggle (pode usar só um dos widths como referência)
        if width_menu == 9:
            new_width = 200
        else:
            new_width = 9

        # animação do menu lateral
        anim_menu = QtCore.QPropertyAnimation(self.menu_lateral, b"minimumWidth")
        anim_menu.setDuration(500)
        anim_menu.setStartValue(width_menu)
        anim_menu.setEndValue(new_width)
        anim_menu.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # animação do logo
        anim_logo = QtCore.QPropertyAnimation(self.local_logo, b"maximumWidth")
        anim_logo.setDuration(500)
        anim_logo.setStartValue(width_logo)
        anim_logo.setEndValue(new_width)
        anim_logo.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # grupo de animações (executa juntas)
        self.group = QtCore.QParallelAnimationGroup()
        self.group.addAnimation(anim_menu)
        self.group.addAnimation(anim_logo)

        self.group.start()   

    def consult_api(self):
        campos = consulta_cnpj(self.txt_cnpj_fornecedor.text())

        self.txt_cnpj_fornecedor.setText(campos[0])
        self.txt_nome_fornecedor.setText(campos[1])
        self.txt_telefone_fornecedor.setText(campos[2])
        self.txt_email_fornecedor.setText(campos[3])

    def completar_vendas(self, nome_produto):
        db = Data_base()
        db.connect()

        produto = db.buscar_produto_por_nome(nome_produto)

        if produto:
            codigo, tipo, valor = produto

            self.txt_tipo_produto.setText(str(tipo))
            self.txt_codigo_produto.setText(str(codigo))
            self.txt_valor_unitario.setText(str(valor))

    def multiplica_item(self):

        qt = self.txt_quantidade.text()
        valor_u = self.txt_valor_unitario.text()
        

        if qt == 0 or valor_u == "":
            self.txt_subtotal.setText('0.00')
        else:

            st = round(float(qt) * float(valor_u), 2)
            self.txt_subtotal.setText(str(st))

    def inserir_item(self):

        cliente = self.txt_nome_cliente_venda.text()
        quantidade = self.txt_quantidade.text()
        produto = self.cb_selecionar_produto.currentText()

        if cliente == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Aviso")
            msg.setText("Selecione um cliente.")
            msg.exec()
            return

        if quantidade == "":        
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Aviso")
            msg.setText("informe a quantidade.")
            msg.exec()
            return

        if produto =="":        
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Aviso")
            msg.setText("Selecione um produto.")
            msg.exec()
            return


        item = {}

        item['cod_produto'] = self.txt_codigo_produto.text()
        item['produto'] = self.cb_selecionar_produto.currentText()
        item['quantidade'] = self.txt_quantidade.text()
        item['tipo'] = self.txt_tipo_produto.text()
        item['valor'] = self.txt_valor_unitario.text()
        item['subtotal'] = self.txt_subtotal.text()

        self.itens.append(item)
        
        row = self.tb_vendas.rowCount()
        self.tb_vendas.insertRow(row)

        self.tb_vendas.setItem(row, 1, QTableWidgetItem(item['cod_produto']))
        self.tb_vendas.setItem(row, 2, QTableWidgetItem(item['produto']))
        self.tb_vendas.setItem(row, 0, QTableWidgetItem(item['quantidade']))
        self.tb_vendas.setItem(row, 3, QTableWidgetItem(item['tipo']))
        self.tb_vendas.setItem(row, 4, QTableWidgetItem(item['valor']))
        self.tb_vendas.setItem(row, 5, QTableWidgetItem(item['subtotal']))

        self.calcular_total()

        self.txt_codigo_produto.clear()
        self.cb_selecionar_produto.setCurrentIndex(-1)
        self.txt_quantidade.clear()
        self.txt_tipo_produto.clear()
        self.txt_valor_unitario.clear()
        self.txt_subtotal.clear()

    def excluir_item(self):
        row = self.tb_vendas.currentRow()

        if row == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Aviso")
            msg.setText("Selecione um item para excluir.")
            msg.exec()
            return

        # Remove da lista
        del self.itens[row]

        # Remove da tabela
        self.tb_vendas.removeRow(row)

        self.calcular_total()
        

    def calcular_total(self):
        total = 0

        for item in self.itens:
            try:
                total += float(item['subtotal'])
            except:
                pass

        self.txt_total.setText(str(total))

    def selecionar_cliente(self):
        row = self.tb_clientes.currentRow()

        if row == -1:
            QMessageBox.warning(self, "Aviso", "Selecione um cliente.")
            return

        # supondo que:
        # coluna 0 = ID_CLIENTE
        # coluna 1 = NOME
        id_cliente = self.tb_clientes.item(row, 0).text()
        nome_cliente = self.tb_clientes.item(row, 1).text()

        # salva para uso depois
        self.id_cliente = id_cliente

        # mostra no campo
        self.txt_nome_cliente_venda.setText(nome_cliente)
        self.paginas.setCurrentWidget(self.pedido)

    def finalizar_pedido(self):

        self.atualizar_lista_itens_da_tabela()

        # 🔒 validações
        if not self.itens:
            QMessageBox.warning(self, "Aviso", "Adicione itens à venda.")
            return

        if self.id_cliente is None:
            QMessageBox.warning(self, "Aviso", "Selecione um cliente.")
            return

        db = Data_base()
        db.connect()

        cursor = db.connection.cursor()

        try:
            # 🔥 (IMPORTANTE) iniciar transação
            cursor.execute("BEGIN")

            # 🔹 calcular total (recomendado não confiar só no QLineEdit)
            #total = sum(float(item['subtotal']) for item in self.itens)
            self.recalcular_totais()

            # 🔹 data atual
            data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 🔹 1. inserir pedido
            cursor.execute("""
                INSERT INTO Pedidos (ID_CLIENTE, TOTAL, DATA)
                VALUES (?, ?, ?)
            """, (self.id_cliente, self.total, data_atual))

            # 🔹 2. pegar ID gerado
            id_pedido = cursor.lastrowid

            # 🔹 3. inserir itens
            for item in self.itens:
                cursor.execute("""
                    INSERT INTO Itens (
                        COD_PRODUTO, PRODUTO, QUANTIDADE, TIPO,
                        VALOR_UNITARIO, SUBTOTAL, ID_PEDIDO
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    item['cod_produto'],
                    item['produto'],
                    int(item['quantidade']),
                    item['tipo'],
                    float(item['valor']),
                    float(item['subtotal']),
                    id_pedido,
                    
                ))

            # 🔥 confirmar tudo
            db.connection.commit()

            QMessageBox.information(self, "Sucesso", f"Pedido {id_pedido} criado!")

            # 🧹 limpar tela
            self.novo_pedido()
            # self.itens.clear()
            # self.tb_vendas.setRowCount(0)
            # self.txt_total.clear()
            # self.txt_nome_cliente.clear()

        except Exception as e:
            db.connection.rollback()
            QMessageBox.critical(self, "Erro", f"Erro ao finalizar pedido:\n{e}")

        finally:
            db.close_connection()

    def novo_pedido(self):

        self.txt_nome_cliente_venda.clear()
        self.txt_total.clear()
        self.txt_numero_pedido.clear()
        self.txt_codigo_produto.clear()
        self.cb_selecionar_produto.setCurrentIndex(-1)
        self.txt_quantidade.clear()
        self.txt_tipo_produto.clear()
        self.txt_valor_unitario.clear()
        self.txt_subtotal.clear()

        self.id_cliente = None
        self.itens.clear()  # limpa depois de salvar
        self.tb_vendas.setRowCount(0)

    def atualizar_lista_itens_da_tabela(self):
        self.itens.clear()

        for row in range(self.tb_vendas.rowCount()):
            item = {
                'quantidade': self.tb_vendas.item(row, 0).text(),
                'cod_produto': self.tb_vendas.item(row, 1).text(),
                'produto': self.tb_vendas.item(row, 2).text(),
                'tipo': self.tb_vendas.item(row, 3).text(),
                'valor': self.tb_vendas.item(row, 4).text(),
                'subtotal': self.tb_vendas.item(row, 5).text(),
                'id_cliente_': str(self.id_cliente)
            }
            self.itens.append(item)

    def recalcular_totais(self):
        self.total = 0

        for row in range(self.tb_vendas.rowCount()):
            qtd = int(self.tb_vendas.item(row, 0).text())
            valor = float(self.tb_vendas.item(row, 4).text())

            subtotal = qtd * valor
            self.total += subtotal

            self.tb_vendas.setItem(row, 5, QTableWidgetItem(f"{subtotal:.2f}"))

        self.txt_total.setText(f"{self.total:.2f}")

    def toggle_toolbox(self, index):
        if self.currentindex == index:
            # clicou no mesmo → fecha
            self.toolbox.setCurrentIndex(4)
            self.currentindex = -1
        else:
            # clicou em outro → abre
            self.currentindex = index

################ FORNECEDOR ################################

    def cadastrar_fornecedor(self):
        db = Data_base()
        db.connect()

        fullDataSet = (
            self.txt_cnpj_fornecedor.text(),
            self.txt_nome_fornecedor.text(),
            self.txt_telefone_fornecedor.text(),
            self.txt_email_fornecedor.text()
        )
    
        #CADASTRAR NO BANCO DE DADOS
        resp = db.register_fornecedor(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro realizado")
            msg.setText("Cadastro realizado com sucesso")
            msg.exec()
            db.close_connection()
            self.buscar_fornecedor()

            self.txt_cnpj_fornecedor.clear(),
            self.txt_nome_fornecedor.clear(),
            self.txt_telefone_fornecedor.clear(),
            self.txt_email_fornecedor.clear()
        
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("erro ao cadastrar o fornecedor. verifique se as informações foram preenchidas corretamente.")
            msg.exec()
            db.close_connection()
            return        
    
    def buscar_fornecedor(self):
        db = Data_base()
        db.connect()
        result = db.select_all_fornecedor()

        self.tb_fornecedores.clearContents()
        self.tb_fornecedores.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_fornecedores.setItem(row, column, QTableWidgetItem(str(data)))
        
        db.close_connection()

    def pesquisar_fornecedor(self):
        
        busca = self.txt_pesquisar_tb_fornecedores.text()

        db = Data_base()
        db.connect()

        dados = db.pesquisar(busca, "Fornecedor")  # só retorna dados

        db.close_connection()

        self.preencher_tabela_fornecedores(dados)

    def preencher_tabela_fornecedores(self, dados):
        self.tb_fornecedores.setRowCount(0)

        for linha_numero, linha_dados in enumerate(dados):
            self.tb_fornecedores.insertRow(linha_numero)
            for coluna_numero, valor in enumerate(linha_dados):
                self.tb_fornecedores.setItem(
                    linha_numero,
                    coluna_numero,
                    QTableWidgetItem(str(valor))
                )



################ CLIENTE ################################

    def delay_pesquisa(self):
        self.timer.start(300)  # espera 300ms antes de buscar

    def cadastrar_cliente(self):
        db = Data_base()
        db.connect()

        fullDataSet = (
            self.txt_nome_cliente.text(),
            self.txt_cpf_cliente.text(),
            self.txt_logradouro_cliente.text(),
            self.txt_numero_cliente.text(),
            self.txt_complemento_cliente.text(),
            self.txt_bairro_cliente.text(),
            self.txt_telefone_cliente.text(),
            self.txt_email_cliente.text()
        )
    
        #CADASTRAR NO BANCO DE DADOS
        resp = db.register_client(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro realizado")
            msg.setText("Cadastro realizado com sucesso")
            msg.exec()
            self.buscar_cliente()
            db.close_connection()

            self.txt_nome_cliente.clear(),
            self.txt_cpf_cliente.clear(),
            self.txt_logradouro_cliente.clear(),
            self.txt_numero_cliente.clear(),
            self.txt_complemento_cliente.clear(),
            self.txt_bairro_cliente.clear(),
            self.txt_telefone_cliente.clear(),
            self.txt_email_cliente.clear()

            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("erro ao cadastrar o cliente. verifique se as informações foram preenchidas corretamente.")
            msg.exec()
            self.buscar_cliente()
            db.close_connection()
            return

    def buscar_cliente(self):
        db = Data_base()
        db.connect()
        result = db.select_all_clients()

        self.tb_clientes.clearContents()
        self.tb_clientes.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_clientes.setItem(row, column, QTableWidgetItem(str(data)))
        
        db.close_connection()

    def atualizar_cliente(self):

        dados = []
        novos_dados = []

        for row in range(self.tb_clientes.rowCount()):
            for column in range(self.tb_clientes.columnCount()):
                dados.append(self.tb_clientes.item(row,column).text())
            novos_dados.append(dados)
            dados = []

        #ATUALIZAR NO BANCO DE DADOS

        db = Data_base()
        db.connect()

        for cliente in novos_dados:
            db.update_client(tuple(cliente))
        
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização do cliente")
        msg.setText("Dados atualizados com sucesso.")
        msg.exec()

        self.tb_clientes.reset()
        self.buscar_cliente()

    def pesquisar_cliente(self):
        
        busca = self.txt_pesquisar_cliente.text()

        db = Data_base()
        db.connect()

        dados = db.pesquisar(busca, "Clientes")  # só retorna dados

        db.close_connection()

        self.preencher_tabela_clientes(dados)

    def preencher_tabela_clientes(self, dados):
        self.tb_clientes.setRowCount(0)

        for linha_numero, linha_dados in enumerate(dados):
            self.tb_clientes.insertRow(linha_numero)
            for coluna_numero, valor in enumerate(linha_dados):
                self.tb_clientes.setItem(
                    linha_numero,
                    coluna_numero,
                    QTableWidgetItem(str(valor))
                )

################ PRODUTOS ################################

    def cadastrar_produto(self):
        db = Data_base()
        db.connect()

        fullDataSet = (
            self.txt_nome_produto.text(),
            self.cb_tipo_produto.currentText(),
            self.txt_valor_produto.text(),

        )
    
        #CADASTRAR NO BANCO DE DADOS
        resp = db.register_product(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro realizado")
            msg.setText("Cadastro realizado com sucesso")
            msg.exec()
            db.close_connection()
            self.buscar_produto()

            self.txt_nome_produto.clear(),
            self.cb_tipo_produto.currentText(-1),
            self.txt_valor_produto.clear(),
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("erro ao cadastrar o produto. verifique se as informações foram preenchidas corretamente.")
            msg.exec()
            db.close_connection()
            self.buscar_produto()
            return

    def buscar_produto(self):
        db = Data_base()
        db.connect()
        result = db.select_all_product()

        self.tb_produtos.clearContents()
        self.tb_produtos.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_produtos.setItem(row, column, QTableWidgetItem(str(data)))
        
        db.close_connection()

    def atualizar_produto(self):

        dados = []
        novos_dados = []

        for row in range(self.tb_produtos.rowCount()):
            for column in range(self.tb_produtos.columnCount()):
                dados.append(self.tb_produtos.item(row,column).text())
            novos_dados.append(dados)
            dados = []

        #ATUALIZAR NO BANCO DE DADOS

        db = Data_base()
        db.connect()

        for produto in novos_dados:
            db.update_client(tuple(produto))
        
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização do produto")
        msg.setText("Dados atualizados com sucesso.")
        msg.exec()

        self.tb_produtos.reset()
        self.buscar_produto()

    def pesquisar_produto(self):
        
        busca = self.txt_pesquisar_tb_produto.text()

        db = Data_base()
        db.connect()

        dados = db.pesquisar(busca, "Produtos")  # só retorna dados

        db.close_connection()

        self.preencher_tabela_produtos(dados)

    def preencher_tabela_produtos(self, dados):
        self.tb_produtos.setRowCount(0)

        for linha_numero, linha_dados in enumerate(dados):
            self.tb_produtos.insertRow(linha_numero)
            for coluna_numero, valor in enumerate(linha_dados):
                self.tb_produtos.setItem(
                    linha_numero,
                    coluna_numero,
                    QTableWidgetItem(str(valor))
                )


################### COMBOBOX #######################

    def combobox_tipo(self):

        db = Data_base()
        db.connect()
        result_1 = db.select_produtos()
        result_2 = db.select_tipo()

        self.cb_selecionar_produto.clear()
        self.cb_selecionar_produto.addItems(result_1)

        self.cb_tipo_produto.clear()
        self.cb_tipo_produto.addItems(result_2)
        return



################### ITEMS #######################


################### PEDIDO #######################

    def pesquisar_pedido(self):
        
        busca = self.txt_pesquisar_pedido.text()

        db = Data_base()
        db.connect()

        dados = db.pesquisar(busca, "Pedidos")  # só retorna dados

        db.close_connection()

        self.preencher_tabela_pedidos(dados)

    def buscar_pedido(self):
        db = Data_base()
        db.connect()
        result = db.select_all_pedidos() or []

        self.tb_pedidos.clearContents()
        self.tb_pedidos.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_pedidos.setItem(row, column, QTableWidgetItem(str(data)))
        
        db.close_connection()

    def preencher_tabela_pedidos(self, dados):
        self.tb_pedidos.setRowCount(0)

        for linha_numero, linha_dados in enumerate(dados):
            self.tb_pedidos.insertRow(linha_numero)
            for coluna_numero, valor in enumerate(linha_dados):
                self.tb_pedidos.setItem(
                    linha_numero,
                    coluna_numero,
                    QTableWidgetItem(str(valor))
                )

    def carregar_pedido_para_edicao(self):
        id_pedido = self.txt_numero_pedido.text()

        db = Data_base()
        db.connect()

        dados = db.buscar_itens_pedido(id_pedido)

        self.itens.clear()
        self.tb_vendas.setRowCount(0)

        for linha in dados:
            item = {
                'quantidade': str(linha["QUANTIDADE"]),
                'cod_produto': linha["COD_PRODUTO"],
                'produto': linha["PRODUTO"],
                'tipo': linha["TIPO"],
                'valor': str(linha["VALOR_UNITARIO"]),
                'subtotal': str(linha["SUBTOTAL"]),
                'id_cliente_': str(linha["ID_CLIENTE"])                
            }

            self.itens.append(item)

            row = self.tb_vendas.rowCount()
            self.tb_vendas.insertRow(row)

            self.tb_vendas.setItem(row, 0, QTableWidgetItem(str(linha["QUANTIDADE"])))
            self.tb_vendas.setItem(row, 1, QTableWidgetItem(str(linha["COD_PRODUTO"])))
            self.tb_vendas.setItem(row, 2, QTableWidgetItem(str(linha["PRODUTO"])))
            self.tb_vendas.setItem(row, 3, QTableWidgetItem(str(linha["TIPO"])))
            self.tb_vendas.setItem(row, 4, QTableWidgetItem(str(linha["VALOR_UNITARIO"])))
            self.tb_vendas.setItem(row, 5, QTableWidgetItem(str(linha["SUBTOTAL"])))

            self.id_cliente = linha["ID_CLIENTE"]
            self.txt_nome_cliente_venda.setText(linha["NOME"])           

        db.close_connection()
        self.calcular_total()

    def pedido_existe(self, id_pedido):
        db = Data_base()
        db.connect()
        cursor = db.connection.cursor()
        cursor.execute("SELECT ID_PEDIDO FROM Pedidos WHERE ID_PEDIDO = ?", (id_pedido,))
        resultado = cursor.fetchone()
        db.close_connection()
        return resultado is not None

    def salvar_pedido(self):
        id_pedido = self.txt_numero_pedido.text().strip()

        if id_pedido == "":
            self.finalizar_pedido()
        elif self.pedido_existe(id_pedido):
            self.atualizar_pedido_existente()
        else:
            QMessageBox.warning(self, "Aviso", "Número de pedido não encontrado.")

    def atualizar_pedido_existente(self):
        id_pedido = self.txt_numero_pedido.text().strip()

        self.atualizar_lista_itens_da_tabela()

        if not id_pedido:
            QMessageBox.warning(self, "Aviso", "Número do pedido inválido.")
            return

        db = Data_base()
        db.connect()
        cursor = db.connection.cursor()

        try:
            cursor.execute("BEGIN")

            # apagar itens antigos
            cursor.execute("DELETE FROM Itens WHERE ID_PEDIDO = ?", (id_pedido,))

            # recalcular total
            #total = sum(float(item['subtotal']) for item in self.itens)
            self.recalcular_totais()

            # atualizar data da edição
            data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # inserir itens atualizados
            for item in self.itens:
                cursor.execute("""
                    INSERT INTO Itens (
                        COD_PRODUTO, PRODUTO, QUANTIDADE, TIPO,
                        VALOR_UNITARIO, SUBTOTAL, ID_PEDIDO
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    item['cod_produto'],
                    item['produto'],
                    int(item['quantidade']),
                    item['tipo'],
                    float(item['valor']),
                    float(item['subtotal']),
                    id_pedido,
                ))

            # atualizar tabela Pedidos
            cursor.execute("""
                UPDATE Pedidos
                SET ID_CLIENTE = ?, TOTAL = ?, DATA = ?
                WHERE ID_PEDIDO = ?
            """, (
                self.id_cliente,
                self.total,
                data_atual,
                id_pedido
            ))

            db.connection.commit()
            self.novo_pedido()
            QMessageBox.information(self, "Sucesso", f"Pedido {id_pedido} atualizado com sucesso!")

        except Exception as e:
            db.connection.rollback()
            QMessageBox.critical(self, "Erro", str(e))

        finally:
            db.close_connection()

    # def selecionar_com_duplo_clique(self, item):
    #     self.novo_pedido()
    #     row = item.row()

    #     self.id_cliente = self.tb_clientes.item(row, 0).text()
    #     nome_cliente = self.tb_clientes.item(row, 1).text()

    #     self.txt_nome_cliente_venda.setText(nome_cliente)

    #     self.paginas.setCurrentWidget(self.pedido)
    #     QMessageBox.information(self, "Cliente Selecionado", f"{nome_cliente} selecionado com sucesso.")
        
    def selecionar_com_duplo_clique_teste(self, item, id_selecionado, tabela, qlineedit, pagina, column, funcao = None, funcao_2 = None):
               
        if funcao:
            funcao()
        
        row = item.row()

        id_selecionado = tabela.item(row, 0).text()
        resultado = tabela.item(row, column).text()

        qlineedit.setText(resultado)

        self.paginas.setCurrentWidget(pagina)

        if funcao_2:
            funcao_2()

        QMessageBox.information(self, "Selecionado", f"{resultado} selecionado com sucesso.")





############################ COLUNAS PARA SQLITE###############################
colunas_pedido = """
    ID_PEDIDO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ID_CLIENTE INTEGER NOT NULL,
    TOTAL REAL NOT NULL,
    DATA TEXT NOT NULL,

    FOREIGN KEY (ID_CLIENTE) REFERENCES Clientes(ID_CLIENTE)
"""

cabecalho_pedido = ('(ID_CLIENTE, TOTAL, DATA) VALUES (?,?,?)')

colunas_item = """
    ID_ITEM INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    COD_PRODUTO TEXT NOT NULL,
    PRODUTO TEXT NOT NULL,
    QUANTIDADE INTEGER NOT NULL,
    TIPO TEXT NOT NULL,
    VALOR_UNITARIO REAL NOT NULL,
    SUBTOTAL REAL NOT NULL,
    ID_PEDIDO INTEGER NOT NULL,

    FOREIGN KEY (ID_PEDIDO) REFERENCES Pedidos(ID_PEDIDO)
"""

cabecalho_item = ('(COD_PRODUTO, PRODUTO, QUANTIDADE, TIPO, VALOR_UNITARIO, SUBTOTAL, ID_PEDIDO) VALUES (?,?,?,?,?,?,?)')

############################ COLUNAS PARA SQLITE###############################


if __name__== "__main__":

    db = Data_base()
    db.connect()
    db.create_table_fornecedor()
    db.create_table_product()
    db.create_table_client()
    db.create_table('Pedidos', colunas_pedido)
    db.create_table('Itens', colunas_item)
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    app.exec()