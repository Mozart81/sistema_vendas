# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sistema_vendas.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QTableWidget, QTableWidgetItem, QToolBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1247, 748)
        MainWindow.setMinimumSize(QSize(0, 100))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"*{\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	font: Century Gothic;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #FFFFFF;\n"
"    color: #333333;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel#subtexto {\n"
"    color: #666666;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: none;                /* Remove todas as bordas */\n"
"    border-bottom: 1px solid #2E6E25; /* Adiciona apenas borda inferior vermelha */\n"
"    color: black;\n"
"	height: 30px\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-bottom: 2px solid #3A8D2F;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: none;                /* Remove todas as bordas */\n"
"    border-bottom: 1px solid #2E6E25; /* Adiciona apenas borda inferior vermelha */\n"
"    color: black;\n"
"	height: 30px\n"
"}\n"
"\n"
"QGroupBox{\n"
"	background-color: #F5F5F5;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 100))
        self.header.setMaximumSize(QSize(16777215, 100))
        self.header.setStyleSheet(u"QWidget {\n"
"    background-color: #3A8D2F;\n"
"    color: white;\n"
"	}")
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.local_logo = QWidget(self.header)
        self.local_logo.setObjectName(u"local_logo")
        self.local_logo.setMinimumSize(QSize(0, 0))
        self.local_logo.setMaximumSize(QSize(9, 16777215))

        self.horizontalLayout.addWidget(self.local_logo)

        self.widget_2 = QWidget(self.header)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_toggle = QPushButton(self.widget_2)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setMinimumSize(QSize(0, 50))
        self.btn_toggle.setMaximumSize(QSize(50, 16777215))
        self.btn_toggle.setStyleSheet(u"QPushButton {\n"
"    color: #C9A24A;\n"
"	background-color: #2E6E25;\n"
"	\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_toggle)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #C9A24A;\n"
"	font-size: 40px;\n"
"	\n"
"}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.header)

        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"")
        self.main.setFrameShape(QFrame.Shape.StyledPanel)
        self.main.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_lateral = QWidget(self.main)
        self.menu_lateral.setObjectName(u"menu_lateral")
        self.menu_lateral.setMinimumSize(QSize(0, 0))
        self.menu_lateral.setMaximumSize(QSize(9, 16777215))
        self.menu_lateral.setStyleSheet(u"QWidget{\n"
"	color: #2E6E25;\n"
"	background-color: #fdfaec;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.menu_lateral)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.menu_lateral)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMaximumSize(QSize(16777215, 16777215))
        self.toolBox.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3A8D2F;\n"
"    color: white;\n"
"    border-top-left-radius: 27px;\n"
"    padding: 9px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2E6E25;\n"
"}\n"
"\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 105, 429))
        self.page.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, 0, -1)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 0))
        self.btn_home.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_novo_pedido = QPushButton(self.page)
        self.btn_novo_pedido.setObjectName(u"btn_novo_pedido")

        self.verticalLayout_3.addWidget(self.btn_novo_pedido)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page, u"Vendas")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 110, 429))
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.btn_cadastrar_clientes = QPushButton(self.page_4)
        self.btn_cadastrar_clientes.setObjectName(u"btn_cadastrar_clientes")

        self.verticalLayout_4.addWidget(self.btn_cadastrar_clientes)

        self.btn_cadastrar_produtos = QPushButton(self.page_4)
        self.btn_cadastrar_produtos.setObjectName(u"btn_cadastrar_produtos")

        self.verticalLayout_4.addWidget(self.btn_cadastrar_produtos)

        self.btn_cadastrar_fornecedores = QPushButton(self.page_4)
        self.btn_cadastrar_fornecedores.setObjectName(u"btn_cadastrar_fornecedores")

        self.verticalLayout_4.addWidget(self.btn_cadastrar_fornecedores)

        self.btn_cadastrar_usuarios = QPushButton(self.page_4)
        self.btn_cadastrar_usuarios.setObjectName(u"btn_cadastrar_usuarios")

        self.verticalLayout_4.addWidget(self.btn_cadastrar_usuarios)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page_4, u"Cadastro")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 110, 429))
        self.verticalLayout_7 = QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.btn_consultar_pedidos = QPushButton(self.page_3)
        self.btn_consultar_pedidos.setObjectName(u"btn_consultar_pedidos")

        self.verticalLayout_7.addWidget(self.btn_consultar_pedidos)

        self.btn_consultar_clientes = QPushButton(self.page_3)
        self.btn_consultar_clientes.setObjectName(u"btn_consultar_clientes")

        self.verticalLayout_7.addWidget(self.btn_consultar_clientes)

        self.btn_consultar_produtos = QPushButton(self.page_3)
        self.btn_consultar_produtos.setObjectName(u"btn_consultar_produtos")

        self.verticalLayout_7.addWidget(self.btn_consultar_produtos)

        self.btn_consultar_fornecedores = QPushButton(self.page_3)
        self.btn_consultar_fornecedores.setObjectName(u"btn_consultar_fornecedores")

        self.verticalLayout_7.addWidget(self.btn_consultar_fornecedores)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page_3, u"Consulta")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 16, 429))
        self.toolBox.addItem(self.page_7, u"Relat\u00f3rios")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 16, 429))
        self.toolBox.addItem(self.page_2, u"Configura\u00e7\u00f5es")

        self.verticalLayout_2.addWidget(self.toolBox)


        self.horizontalLayout_2.addWidget(self.menu_lateral)

        self.widget_5 = QWidget(self.main)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #3A8D2F;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"	Width: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2E6E25;\n"
"}\n"
"\n"
"QIcon {\n"
"	color: white;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.paginas = QStackedWidget(self.widget_5)
        self.paginas.setObjectName(u"paginas")
        self.paginas.setEnabled(True)
        self.paginas.setMinimumSize(QSize(0, 75))
        self.paginas.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.paginas.setAcceptDrops(False)
        self.paginas.setStyleSheet(u"QHeaderView{\n"
"	\n"
"	color: #fdfaec;\n"
"	background-color: #2E6E25;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: #fdfaec;\n"
"}")
        self.cadastro_fornecedor = QWidget()
        self.cadastro_fornecedor.setObjectName(u"cadastro_fornecedor")
        self.verticalLayout_15 = QVBoxLayout(self.cadastro_fornecedor)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_17 = QWidget(self.cadastro_fornecedor)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 100))
        self.widget_17.setMaximumSize(QSize(16777215, 100))
        self.widget_17.setStyleSheet(u"QFrame {\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 8px;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.widget_17)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_5 = QLabel(self.widget_17)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 75))
        self.label_5.setMaximumSize(QSize(16777215, 75))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setIndent(0)

        self.verticalLayout_14.addWidget(self.label_5)


        self.verticalLayout_15.addWidget(self.widget_17)

        self.widget_16 = QWidget(self.cadastro_fornecedor)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_4 = QGridLayout(self.widget_16)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter_8 = QSplitter(self.widget_16)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Orientation.Horizontal)
        self.txt_cnpj_fornecedor = QLineEdit(self.splitter_8)
        self.txt_cnpj_fornecedor.setObjectName(u"txt_cnpj_fornecedor")
        self.txt_cnpj_fornecedor.setMinimumSize(QSize(0, 31))
        self.txt_cnpj_fornecedor.setMaximumSize(QSize(300, 16777215))
        self.splitter_8.addWidget(self.txt_cnpj_fornecedor)
        self.btn_cnpj = QPushButton(self.splitter_8)
        self.btn_cnpj.setObjectName(u"btn_cnpj")
        self.btn_cnpj.setMinimumSize(QSize(0, 30))
        self.btn_cnpj.setMaximumSize(QSize(40, 30))
        self.btn_cnpj.setStyleSheet(u"")
        self.btn_cnpj.setAutoDefault(False)
        self.btn_cnpj.setFlat(False)
        self.splitter_8.addWidget(self.btn_cnpj)

        self.gridLayout_4.addWidget(self.splitter_8, 0, 0, 1, 1)

        self.splitter_6 = QSplitter(self.widget_16)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Orientation.Horizontal)
        self.txt_nome_fornecedor = QLineEdit(self.splitter_6)
        self.txt_nome_fornecedor.setObjectName(u"txt_nome_fornecedor")
        self.txt_nome_fornecedor.setMinimumSize(QSize(0, 31))
        self.txt_nome_fornecedor.setMaximumSize(QSize(500, 16777215))
        self.splitter_6.addWidget(self.txt_nome_fornecedor)
        self.txt_telefone_fornecedor = QLineEdit(self.splitter_6)
        self.txt_telefone_fornecedor.setObjectName(u"txt_telefone_fornecedor")
        self.txt_telefone_fornecedor.setMinimumSize(QSize(0, 31))
        self.txt_telefone_fornecedor.setMaximumSize(QSize(200, 16777215))
        self.splitter_6.addWidget(self.txt_telefone_fornecedor)
        self.txt_email_fornecedor = QLineEdit(self.splitter_6)
        self.txt_email_fornecedor.setObjectName(u"txt_email_fornecedor")
        self.txt_email_fornecedor.setMinimumSize(QSize(0, 31))
        self.txt_email_fornecedor.setMaximumSize(QSize(200, 16777215))
        self.splitter_6.addWidget(self.txt_email_fornecedor)

        self.gridLayout_4.addWidget(self.splitter_6, 1, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.widget_16)

        self.widget_15 = QWidget(self.cadastro_fornecedor)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 75))
        self.widget_15.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_5 = QSpacerItem(1110, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.btn_salvar_fornecedor = QPushButton(self.widget_15)
        self.btn_salvar_fornecedor.setObjectName(u"btn_salvar_fornecedor")
        self.btn_salvar_fornecedor.setMinimumSize(QSize(80, 31))
        self.btn_salvar_fornecedor.setMaximumSize(QSize(80, 31))

        self.horizontalLayout_9.addWidget(self.btn_salvar_fornecedor)


        self.verticalLayout_15.addWidget(self.widget_15)

        self.paginas.addWidget(self.cadastro_fornecedor)
        self.cadastro_usuario = QWidget()
        self.cadastro_usuario.setObjectName(u"cadastro_usuario")
        self.verticalLayout_12 = QVBoxLayout(self.cadastro_usuario)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_18 = QWidget(self.cadastro_usuario)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 100))
        self.widget_18.setMaximumSize(QSize(16777215, 100))
        self.widget_18.setStyleSheet(u"QFrame {\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 8px;\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.widget_18)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_6 = QLabel(self.widget_18)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 75))
        self.label_6.setMaximumSize(QSize(16777215, 75))
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setIndent(0)

        self.verticalLayout_16.addWidget(self.label_6)


        self.verticalLayout_12.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.cadastro_usuario)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_5 = QGridLayout(self.widget_19)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.splitter_10 = QSplitter(self.widget_19)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setOrientation(Qt.Orientation.Horizontal)
        self.txt_nome_usuario = QLineEdit(self.splitter_10)
        self.txt_nome_usuario.setObjectName(u"txt_nome_usuario")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_nome_usuario.sizePolicy().hasHeightForWidth())
        self.txt_nome_usuario.setSizePolicy(sizePolicy)
        self.txt_nome_usuario.setMinimumSize(QSize(0, 31))
        self.txt_nome_usuario.setMaximumSize(QSize(500, 16777215))
        self.splitter_10.addWidget(self.txt_nome_usuario)
        self.txt_email_usuario = QLineEdit(self.splitter_10)
        self.txt_email_usuario.setObjectName(u"txt_email_usuario")
        self.txt_email_usuario.setMinimumSize(QSize(0, 31))
        self.txt_email_usuario.setMaximumSize(QSize(300, 16777215))
        self.splitter_10.addWidget(self.txt_email_usuario)

        self.gridLayout_5.addWidget(self.splitter_10, 0, 0, 1, 1)

        self.splitter_9 = QSplitter(self.widget_19)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setOrientation(Qt.Orientation.Vertical)
        self.txt_cpf_usuario = QLineEdit(self.splitter_9)
        self.txt_cpf_usuario.setObjectName(u"txt_cpf_usuario")
        self.txt_cpf_usuario.setMinimumSize(QSize(0, 31))
        self.txt_cpf_usuario.setMaximumSize(QSize(200, 16777215))
        self.splitter_9.addWidget(self.txt_cpf_usuario)
        self.txt_criar_senha = QLineEdit(self.splitter_9)
        self.txt_criar_senha.setObjectName(u"txt_criar_senha")
        self.txt_criar_senha.setMinimumSize(QSize(0, 31))
        self.txt_criar_senha.setMaximumSize(QSize(200, 16777215))
        self.txt_criar_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.splitter_9.addWidget(self.txt_criar_senha)
        self.txt_repetir_senha = QLineEdit(self.splitter_9)
        self.txt_repetir_senha.setObjectName(u"txt_repetir_senha")
        self.txt_repetir_senha.setMinimumSize(QSize(0, 31))
        self.txt_repetir_senha.setMaximumSize(QSize(200, 16777215))
        self.txt_repetir_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.splitter_9.addWidget(self.txt_repetir_senha)

        self.gridLayout_5.addWidget(self.splitter_9, 1, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.cadastro_usuario)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(0, 75))
        self.widget_20.setMaximumSize(QSize(16777215, 75))
        self.widget_20.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_7 = QSpacerItem(1126, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.pushButton_16 = QPushButton(self.widget_20)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(80, 31))
        self.pushButton_16.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_11.addWidget(self.pushButton_16)


        self.verticalLayout_12.addWidget(self.widget_20)

        self.paginas.addWidget(self.cadastro_usuario)
        self.cadastro_cliente = QWidget()
        self.cadastro_cliente.setObjectName(u"cadastro_cliente")
        self.verticalLayout_8 = QVBoxLayout(self.cadastro_cliente)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_8 = QWidget(self.cadastro_cliente)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 100))
        self.widget_8.setMaximumSize(QSize(16777215, 100))
        self.widget_8.setStyleSheet(u"QFrame {\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 8px;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.widget_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.widget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 75))
        self.label_2.setMaximumSize(QSize(16777215, 75))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setIndent(0)

        self.verticalLayout_9.addWidget(self.label_2)


        self.verticalLayout_8.addWidget(self.widget_8)

        self.widget_6 = QWidget(self.cadastro_cliente)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_12 = QSplitter(self.widget_6)
        self.splitter_12.setObjectName(u"splitter_12")
        self.splitter_12.setOrientation(Qt.Orientation.Horizontal)
        self.txt_nome_cliente = QLineEdit(self.splitter_12)
        self.txt_nome_cliente.setObjectName(u"txt_nome_cliente")
        self.txt_nome_cliente.setMinimumSize(QSize(0, 31))
        self.txt_nome_cliente.setMaximumSize(QSize(500, 16777215))
        self.splitter_12.addWidget(self.txt_nome_cliente)
        self.txt_cpf_cliente = QLineEdit(self.splitter_12)
        self.txt_cpf_cliente.setObjectName(u"txt_cpf_cliente")
        self.txt_cpf_cliente.setMinimumSize(QSize(0, 31))
        self.txt_cpf_cliente.setMaximumSize(QSize(200, 16777215))
        self.splitter_12.addWidget(self.txt_cpf_cliente)

        self.gridLayout.addWidget(self.splitter_12, 0, 0, 1, 1)

        self.splitter_11 = QSplitter(self.widget_6)
        self.splitter_11.setObjectName(u"splitter_11")
        self.splitter_11.setOrientation(Qt.Orientation.Horizontal)
        self.txt_logradouro_cliente = QLineEdit(self.splitter_11)
        self.txt_logradouro_cliente.setObjectName(u"txt_logradouro_cliente")
        self.txt_logradouro_cliente.setMinimumSize(QSize(0, 31))
        self.txt_logradouro_cliente.setMaximumSize(QSize(600, 16777215))
        self.splitter_11.addWidget(self.txt_logradouro_cliente)
        self.txt_numero_cliente = QLineEdit(self.splitter_11)
        self.txt_numero_cliente.setObjectName(u"txt_numero_cliente")
        self.txt_numero_cliente.setMinimumSize(QSize(0, 31))
        self.txt_numero_cliente.setMaximumSize(QSize(100, 16777215))
        self.splitter_11.addWidget(self.txt_numero_cliente)

        self.gridLayout.addWidget(self.splitter_11, 1, 0, 1, 1)

        self.splitter_14 = QSplitter(self.widget_6)
        self.splitter_14.setObjectName(u"splitter_14")
        self.splitter_14.setOrientation(Qt.Orientation.Horizontal)
        self.txt_complemento_cliente = QLineEdit(self.splitter_14)
        self.txt_complemento_cliente.setObjectName(u"txt_complemento_cliente")
        self.txt_complemento_cliente.setMinimumSize(QSize(0, 31))
        self.txt_complemento_cliente.setMaximumSize(QSize(400, 16777215))
        self.splitter_14.addWidget(self.txt_complemento_cliente)
        self.txt_bairro_cliente = QLineEdit(self.splitter_14)
        self.txt_bairro_cliente.setObjectName(u"txt_bairro_cliente")
        self.txt_bairro_cliente.setMinimumSize(QSize(0, 31))
        self.txt_bairro_cliente.setMaximumSize(QSize(300, 16777215))
        self.splitter_14.addWidget(self.txt_bairro_cliente)

        self.gridLayout.addWidget(self.splitter_14, 2, 0, 1, 1)

        self.splitter_13 = QSplitter(self.widget_6)
        self.splitter_13.setObjectName(u"splitter_13")
        self.splitter_13.setOrientation(Qt.Orientation.Horizontal)
        self.txt_telefone_cliente = QLineEdit(self.splitter_13)
        self.txt_telefone_cliente.setObjectName(u"txt_telefone_cliente")
        self.txt_telefone_cliente.setMinimumSize(QSize(0, 31))
        self.txt_telefone_cliente.setMaximumSize(QSize(200, 16777215))
        self.splitter_13.addWidget(self.txt_telefone_cliente)
        self.txt_email_cliente = QLineEdit(self.splitter_13)
        self.txt_email_cliente.setObjectName(u"txt_email_cliente")
        self.txt_email_cliente.setMinimumSize(QSize(0, 31))
        self.txt_email_cliente.setMaximumSize(QSize(300, 16777215))
        self.splitter_13.addWidget(self.txt_email_cliente)

        self.gridLayout.addWidget(self.splitter_13, 3, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.cadastro_cliente)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 75))
        self.widget_7.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_8 = QSpacerItem(1126, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.btn_salvar_cliente = QPushButton(self.widget_7)
        self.btn_salvar_cliente.setObjectName(u"btn_salvar_cliente")
        self.btn_salvar_cliente.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_12.addWidget(self.btn_salvar_cliente)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.paginas.addWidget(self.cadastro_cliente)
        self.cadastro_produto = QWidget()
        self.cadastro_produto.setObjectName(u"cadastro_produto")
        self.verticalLayout_11 = QVBoxLayout(self.cadastro_produto)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_11 = QWidget(self.cadastro_produto)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 100))
        self.widget_11.setMaximumSize(QSize(16777215, 100))
        self.widget_11.setStyleSheet(u"QFrame {\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 8px;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.widget_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.widget_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 75))
        self.label_3.setMaximumSize(QSize(16777215, 75))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setIndent(0)

        self.verticalLayout_10.addWidget(self.label_3)


        self.verticalLayout_11.addWidget(self.widget_11)

        self.widget_10 = QWidget(self.cadastro_produto)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_2 = QGridLayout(self.widget_10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_nome_produto = QLineEdit(self.widget_10)
        self.txt_nome_produto.setObjectName(u"txt_nome_produto")
        self.txt_nome_produto.setMinimumSize(QSize(0, 31))
        self.txt_nome_produto.setMaximumSize(QSize(900, 16777215))

        self.gridLayout_2.addWidget(self.txt_nome_produto, 1, 0, 1, 1)

        self.splitter_4 = QSplitter(self.widget_10)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Horizontal)
        self.cb_tipo_produto = QComboBox(self.splitter_4)
        self.cb_tipo_produto.setObjectName(u"cb_tipo_produto")
        self.cb_tipo_produto.setMinimumSize(QSize(0, 31))
        self.cb_tipo_produto.setMaximumSize(QSize(300, 16777215))
        self.splitter_4.addWidget(self.cb_tipo_produto)
        self.txt_valor_produto = QLineEdit(self.splitter_4)
        self.txt_valor_produto.setObjectName(u"txt_valor_produto")
        self.txt_valor_produto.setMinimumSize(QSize(0, 31))
        self.txt_valor_produto.setMaximumSize(QSize(300, 16777215))
        self.splitter_4.addWidget(self.txt_valor_produto)

        self.gridLayout_2.addWidget(self.splitter_4, 2, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.widget_10)

        self.widget_9 = QWidget(self.cadastro_produto)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 75))
        self.widget_9.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(919, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_salvar_produto = QPushButton(self.widget_9)
        self.btn_salvar_produto.setObjectName(u"btn_salvar_produto")
        self.btn_salvar_produto.setMinimumSize(QSize(80, 31))
        self.btn_salvar_produto.setMaximumSize(QSize(80, 31))

        self.horizontalLayout_3.addWidget(self.btn_salvar_produto)


        self.verticalLayout_11.addWidget(self.widget_9)

        self.paginas.addWidget(self.cadastro_produto)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_23 = QVBoxLayout(self.home)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_7 = QLabel(self.home)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: #C9A24A;\n"
"	font-size: 80px;\n"
"	\n"
"}")

        self.verticalLayout_23.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.paginas.addWidget(self.home)
        self.pedido = QWidget()
        self.pedido.setObjectName(u"pedido")
        self.verticalLayout_22 = QVBoxLayout(self.pedido)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_21 = QWidget(self.pedido)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(0, 100))
        self.widget_21.setMaximumSize(QSize(16777215, 100))
        self.widget_21.setStyleSheet(u"QFrame {\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 8px;\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.widget_21)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_8 = QLabel(self.widget_21)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 75))
        self.label_8.setMaximumSize(QSize(16777215, 75))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setIndent(0)

        self.verticalLayout_21.addWidget(self.label_8)


        self.verticalLayout_22.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.pedido)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"QFrame {\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 12px;\n"
"}")
        self.gridLayout_9 = QGridLayout(self.widget_22)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame = QFrame(self.widget_22)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(9)
        self.gridLayout_7.setContentsMargins(9, 9, 9, 9)
        self.txt_nome_cliente_venda = QLineEdit(self.frame)
        self.txt_nome_cliente_venda.setObjectName(u"txt_nome_cliente_venda")
        self.txt_nome_cliente_venda.setMinimumSize(QSize(300, 0))
        self.txt_nome_cliente_venda.setMaximumSize(QSize(16777215, 16777215))
        self.txt_nome_cliente_venda.setReadOnly(True)

        self.gridLayout_7.addWidget(self.txt_nome_cliente_venda, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(15)
        self.gridLayout_6.setContentsMargins(15, 15, 15, 15)
        self.txt_codigo_produto = QLineEdit(self.groupBox)
        self.txt_codigo_produto.setObjectName(u"txt_codigo_produto")
        self.txt_codigo_produto.setReadOnly(True)

        self.gridLayout_6.addWidget(self.txt_codigo_produto, 0, 0, 1, 2)

        self.txt_quantidade = QLineEdit(self.groupBox)
        self.txt_quantidade.setObjectName(u"txt_quantidade")
        self.txt_quantidade.setMinimumSize(QSize(0, 31))
        self.txt_quantidade.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_6.addWidget(self.txt_quantidade, 2, 0, 1, 1)

        self.txt_tipo_produto = QLineEdit(self.groupBox)
        self.txt_tipo_produto.setObjectName(u"txt_tipo_produto")
        self.txt_tipo_produto.setReadOnly(True)

        self.gridLayout_6.addWidget(self.txt_tipo_produto, 2, 1, 1, 2)

        self.txt_valor_unitario = QLineEdit(self.groupBox)
        self.txt_valor_unitario.setObjectName(u"txt_valor_unitario")
        self.txt_valor_unitario.setMinimumSize(QSize(0, 31))
        self.txt_valor_unitario.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_6.addWidget(self.txt_valor_unitario, 2, 3, 1, 1)

        self.txt_subtotal = QLineEdit(self.groupBox)
        self.txt_subtotal.setObjectName(u"txt_subtotal")
        self.txt_subtotal.setMinimumSize(QSize(0, 31))
        self.txt_subtotal.setMaximumSize(QSize(200, 16777215))
        self.txt_subtotal.setReadOnly(True)

        self.gridLayout_6.addWidget(self.txt_subtotal, 2, 4, 1, 1)

        self.cb_selecionar_produto = QComboBox(self.groupBox)
        self.cb_selecionar_produto.setObjectName(u"cb_selecionar_produto")
        self.cb_selecionar_produto.setMinimumSize(QSize(400, 31))
        self.cb_selecionar_produto.setMaximumSize(QSize(600, 16777215))

        self.gridLayout_6.addWidget(self.cb_selecionar_produto, 0, 2, 1, 3)


        self.gridLayout_7.addWidget(self.groupBox, 1, 0, 1, 4)

        self.btn_inserir_item = QPushButton(self.frame)
        self.btn_inserir_item.setObjectName(u"btn_inserir_item")
        self.btn_inserir_item.setMinimumSize(QSize(80, 0))
        self.btn_inserir_item.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_7.addWidget(self.btn_inserir_item, 2, 3, 1, 1)

        self.btn_inserir_cliente = QPushButton(self.frame)
        self.btn_inserir_cliente.setObjectName(u"btn_inserir_cliente")
        self.btn_inserir_cliente.setMinimumSize(QSize(80, 0))
        self.btn_inserir_cliente.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_7.addWidget(self.btn_inserir_cliente, 0, 3, 1, 1)


        self.gridLayout_9.addWidget(self.frame, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.widget_22)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.txt_numero_pedido = QLineEdit(self.frame_2)
        self.txt_numero_pedido.setObjectName(u"txt_numero_pedido")
        self.txt_numero_pedido.setMinimumSize(QSize(100, 31))
        self.txt_numero_pedido.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_8.addWidget(self.txt_numero_pedido, 0, 0, 1, 1)

        self.btn_carregar_pedido = QPushButton(self.frame_2)
        self.btn_carregar_pedido.setObjectName(u"btn_carregar_pedido")
        self.btn_carregar_pedido.setMinimumSize(QSize(80, 31))
        self.btn_carregar_pedido.setMaximumSize(QSize(80, 31))

        self.gridLayout_8.addWidget(self.btn_carregar_pedido, 0, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_24.addLayout(self.gridLayout_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tb_vendas = QTableWidget(self.frame_2)
        if (self.tb_vendas.columnCount() < 6):
            self.tb_vendas.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_vendas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_vendas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_vendas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_vendas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_vendas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_vendas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tb_vendas.setObjectName(u"tb_vendas")
        self.tb_vendas.setStyleSheet(u"QHeaderView{\n"
"	font: 7pt \"Segoe UI\";\n"
"	color: #fdfaec;\n"
"	background-color: #2E6E25;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	font: 7pt \"Segoe UI\";\n"
"	background-color: #fdfaec;\n"
"	\n"
"}")
        self.tb_vendas.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tb_vendas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tb_vendas.setSortingEnabled(True)
        self.tb_vendas.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_vendas.horizontalHeader().setDefaultSectionSize(80)
        self.tb_vendas.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.tb_vendas)

        self.txt_total = QLineEdit(self.frame_2)
        self.txt_total.setObjectName(u"txt_total")
        self.txt_total.setMinimumSize(QSize(200, 31))
        self.txt_total.setMaximumSize(QSize(200, 16777215))
        self.txt_total.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.txt_total, 0, Qt.AlignmentFlag.AlignRight)

        self.btn_excluir_item = QPushButton(self.frame_2)
        self.btn_excluir_item.setObjectName(u"btn_excluir_item")
        self.btn_excluir_item.setMinimumSize(QSize(80, 0))
        self.btn_excluir_item.setMaximumSize(QSize(80, 16777215))

        self.verticalLayout_5.addWidget(self.btn_excluir_item, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_24.addLayout(self.verticalLayout_5)


        self.gridLayout_9.addWidget(self.frame_2, 0, 2, 1, 1)


        self.verticalLayout_22.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.pedido)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(0, 75))
        self.widget_23.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btn_sair_venda = QPushButton(self.widget_23)
        self.btn_sair_venda.setObjectName(u"btn_sair_venda")
        self.btn_sair_venda.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_5.addWidget(self.btn_sair_venda)

        self.btn_nova_venda = QPushButton(self.widget_23)
        self.btn_nova_venda.setObjectName(u"btn_nova_venda")
        self.btn_nova_venda.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_5.addWidget(self.btn_nova_venda)

        self.btn_finalizar_pedido = QPushButton(self.widget_23)
        self.btn_finalizar_pedido.setObjectName(u"btn_finalizar_pedido")
        self.btn_finalizar_pedido.setMinimumSize(QSize(80, 31))
        self.btn_finalizar_pedido.setMaximumSize(QSize(80, 31))

        self.horizontalLayout_5.addWidget(self.btn_finalizar_pedido)


        self.verticalLayout_22.addWidget(self.widget_23)

        self.paginas.addWidget(self.pedido)
        self.consulta_cliente = QWidget()
        self.consulta_cliente.setObjectName(u"consulta_cliente")
        self.verticalLayout_19 = QVBoxLayout(self.consulta_cliente)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_33 = QWidget(self.consulta_cliente)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMinimumSize(QSize(0, 75))
        self.widget_33.setMaximumSize(QSize(16777215, 75))
        self.widget_33.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_33.setStyleSheet(u"QFrame {\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 8px;\n"
"}")
        self.gridLayout_10 = QGridLayout(self.widget_33)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_11 = QLabel(self.widget_33)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_11, 0, 0, 1, 1)


        self.verticalLayout_19.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.consulta_cliente)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMinimumSize(QSize(0, 0))
        self.widget_34.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_27 = QVBoxLayout(self.widget_34)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.splitter_2 = QSplitter(self.widget_34)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.txt_pesquisar_cliente = QLineEdit(self.splitter_2)
        self.txt_pesquisar_cliente.setObjectName(u"txt_pesquisar_cliente")
        self.txt_pesquisar_cliente.setMinimumSize(QSize(200, 0))
        self.txt_pesquisar_cliente.setMaximumSize(QSize(400, 16777215))
        self.splitter_2.addWidget(self.txt_pesquisar_cliente)

        self.verticalLayout_27.addWidget(self.splitter_2)

        self.tb_clientes = QTableWidget(self.widget_34)
        if (self.tb_clientes.columnCount() < 9):
            self.tb_clientes.setColumnCount(9)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.tb_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.tb_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.tb_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.tb_clientes.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.tb_clientes.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.tb_clientes.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.tb_clientes.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.tb_clientes.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font);
        self.tb_clientes.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        self.tb_clientes.setObjectName(u"tb_clientes")
        self.tb_clientes.setStyleSheet(u"QHeaderView{\n"
"	\n"
"	color: #fdfaec;\n"
"	background-color: #2E6E25;\n"
"}")
        self.tb_clientes.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tb_clientes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tb_clientes.setSortingEnabled(True)
        self.tb_clientes.setRowCount(0)
        self.tb_clientes.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_clientes.horizontalHeader().setDefaultSectionSize(150)
        self.tb_clientes.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_27.addWidget(self.tb_clientes)


        self.verticalLayout_19.addWidget(self.widget_34)

        self.widget_35 = QWidget(self.consulta_cliente)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMinimumSize(QSize(0, 50))
        self.widget_35.setMaximumSize(QSize(16777215, 50))
        self.widget_35.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_salvar_tb_clientes = QPushButton(self.widget_35)
        self.btn_salvar_tb_clientes.setObjectName(u"btn_salvar_tb_clientes")
        self.btn_salvar_tb_clientes.setEnabled(True)
        self.btn_salvar_tb_clientes.setMinimumSize(QSize(80, 31))
        self.btn_salvar_tb_clientes.setMaximumSize(QSize(80, 31))

        self.horizontalLayout_6.addWidget(self.btn_salvar_tb_clientes)

        self.btn_excel_tb_clientes = QPushButton(self.widget_35)
        self.btn_excel_tb_clientes.setObjectName(u"btn_excel_tb_clientes")
        self.btn_excel_tb_clientes.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_6.addWidget(self.btn_excel_tb_clientes)

        self.btn_excluir_tb_clientes = QPushButton(self.widget_35)
        self.btn_excluir_tb_clientes.setObjectName(u"btn_excluir_tb_clientes")
        self.btn_excluir_tb_clientes.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_6.addWidget(self.btn_excluir_tb_clientes)

        self.pushButton_3 = QPushButton(self.widget_35)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.btn_selecionar_cliente = QPushButton(self.widget_35)
        self.btn_selecionar_cliente.setObjectName(u"btn_selecionar_cliente")
        self.btn_selecionar_cliente.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_6.addWidget(self.btn_selecionar_cliente)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_19.addWidget(self.widget_35)

        self.paginas.addWidget(self.consulta_cliente)
        self.consulta_produto = QWidget()
        self.consulta_produto.setObjectName(u"consulta_produto")
        self.verticalLayout_18 = QVBoxLayout(self.consulta_produto)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_48 = QWidget(self.consulta_produto)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(0, 75))
        self.widget_48.setMaximumSize(QSize(16777215, 75))
        self.widget_48.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_48.setStyleSheet(u"QFrame {\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 8px;\n"
"}")
        self.gridLayout_15 = QGridLayout(self.widget_48)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_16 = QLabel(self.widget_48)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_16, 0, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.widget_48)

        self.widget_49 = QWidget(self.consulta_produto)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMinimumSize(QSize(0, 0))
        self.widget_49.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_37 = QVBoxLayout(self.widget_49)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.splitter_3 = QSplitter(self.widget_49)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.txt_pesquisar_tb_produto = QLineEdit(self.splitter_3)
        self.txt_pesquisar_tb_produto.setObjectName(u"txt_pesquisar_tb_produto")
        self.txt_pesquisar_tb_produto.setMinimumSize(QSize(200, 0))
        self.txt_pesquisar_tb_produto.setMaximumSize(QSize(400, 16777215))
        self.splitter_3.addWidget(self.txt_pesquisar_tb_produto)

        self.verticalLayout_37.addWidget(self.splitter_3)

        self.tb_produtos = QTableWidget(self.widget_49)
        if (self.tb_produtos.columnCount() < 4):
            self.tb_produtos.setColumnCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font);
        self.tb_produtos.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font);
        self.tb_produtos.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font);
        self.tb_produtos.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font);
        self.tb_produtos.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        if (self.tb_produtos.rowCount() < 1):
            self.tb_produtos.setRowCount(1)
        self.tb_produtos.setObjectName(u"tb_produtos")
        self.tb_produtos.setStyleSheet(u"QHeaderView{\n"
"	\n"
"	color: #fdfaec;\n"
"	background-color: #2E6E25;\n"
"}")
        self.tb_produtos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tb_produtos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tb_produtos.setSortingEnabled(True)
        self.tb_produtos.setRowCount(1)
        self.tb_produtos.setColumnCount(4)
        self.tb_produtos.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_produtos.horizontalHeader().setDefaultSectionSize(200)
        self.tb_produtos.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_37.addWidget(self.tb_produtos)


        self.verticalLayout_18.addWidget(self.widget_49)

        self.widget_50 = QWidget(self.consulta_produto)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMinimumSize(QSize(0, 50))
        self.widget_50.setMaximumSize(QSize(16777215, 50))
        self.widget_50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_salvar_tb_produto = QPushButton(self.widget_50)
        self.btn_salvar_tb_produto.setObjectName(u"btn_salvar_tb_produto")
        self.btn_salvar_tb_produto.setEnabled(False)
        self.btn_salvar_tb_produto.setMinimumSize(QSize(80, 31))
        self.btn_salvar_tb_produto.setMaximumSize(QSize(80, 31))

        self.horizontalLayout_8.addWidget(self.btn_salvar_tb_produto)

        self.btn_excel_tb_produto = QPushButton(self.widget_50)
        self.btn_excel_tb_produto.setObjectName(u"btn_excel_tb_produto")
        self.btn_excel_tb_produto.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_8.addWidget(self.btn_excel_tb_produto)

        self.btn_excluir_tb_produto = QPushButton(self.widget_50)
        self.btn_excluir_tb_produto.setObjectName(u"btn_excluir_tb_produto")
        self.btn_excluir_tb_produto.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_8.addWidget(self.btn_excluir_tb_produto)

        self.btn_alterar_tb_produto = QPushButton(self.widget_50)
        self.btn_alterar_tb_produto.setObjectName(u"btn_alterar_tb_produto")
        self.btn_alterar_tb_produto.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_8.addWidget(self.btn_alterar_tb_produto)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_18.addWidget(self.widget_50)

        self.paginas.addWidget(self.consulta_produto)
        self.consulta_pedido = QWidget()
        self.consulta_pedido.setObjectName(u"consulta_pedido")
        self.verticalLayout_13 = QVBoxLayout(self.consulta_pedido)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_13 = QWidget(self.consulta_pedido)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 75))
        self.widget_13.setMaximumSize(QSize(16777215, 75))
        self.widget_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_13.setStyleSheet(u"QFrame {\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 8px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget_13)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.widget_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.widget_13)

        self.widget_12 = QWidget(self.consulta_pedido)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 0))
        self.widget_12.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_17 = QVBoxLayout(self.widget_12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.splitter = QSplitter(self.widget_12)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.txt_pesquisar_pedido = QLineEdit(self.splitter)
        self.txt_pesquisar_pedido.setObjectName(u"txt_pesquisar_pedido")
        self.txt_pesquisar_pedido.setMinimumSize(QSize(200, 0))
        self.txt_pesquisar_pedido.setMaximumSize(QSize(400, 16777215))
        self.splitter.addWidget(self.txt_pesquisar_pedido)

        self.verticalLayout_17.addWidget(self.splitter)

        self.tb_pedidos = QTableWidget(self.widget_12)
        if (self.tb_pedidos.columnCount() < 4):
            self.tb_pedidos.setColumnCount(4)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font);
        self.tb_pedidos.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font);
        self.tb_pedidos.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font);
        self.tb_pedidos.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font);
        self.tb_pedidos.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        if (self.tb_pedidos.rowCount() < 1):
            self.tb_pedidos.setRowCount(1)
        self.tb_pedidos.setObjectName(u"tb_pedidos")
        self.tb_pedidos.setStyleSheet(u"")
        self.tb_pedidos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tb_pedidos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tb_pedidos.setSortingEnabled(True)
        self.tb_pedidos.setRowCount(1)
        self.tb_pedidos.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_pedidos.horizontalHeader().setDefaultSectionSize(150)
        self.tb_pedidos.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_17.addWidget(self.tb_pedidos)


        self.verticalLayout_13.addWidget(self.widget_12)

        self.widget_14 = QWidget(self.consulta_pedido)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 50))
        self.widget_14.setMaximumSize(QSize(16777215, 50))
        self.widget_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_salvar_tb_pedidos = QPushButton(self.widget_14)
        self.btn_salvar_tb_pedidos.setObjectName(u"btn_salvar_tb_pedidos")
        self.btn_salvar_tb_pedidos.setEnabled(False)
        self.btn_salvar_tb_pedidos.setMinimumSize(QSize(80, 31))
        self.btn_salvar_tb_pedidos.setMaximumSize(QSize(80, 31))

        self.horizontalLayout_4.addWidget(self.btn_salvar_tb_pedidos)

        self.btn_imprimir_tb_pedidos = QPushButton(self.widget_14)
        self.btn_imprimir_tb_pedidos.setObjectName(u"btn_imprimir_tb_pedidos")
        self.btn_imprimir_tb_pedidos.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_4.addWidget(self.btn_imprimir_tb_pedidos)

        self.btn_excluir_tb_pedidos = QPushButton(self.widget_14)
        self.btn_excluir_tb_pedidos.setObjectName(u"btn_excluir_tb_pedidos")
        self.btn_excluir_tb_pedidos.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_4.addWidget(self.btn_excluir_tb_pedidos)

        self.btn_alterar_tb_pedidos = QPushButton(self.widget_14)
        self.btn_alterar_tb_pedidos.setObjectName(u"btn_alterar_tb_pedidos")
        self.btn_alterar_tb_pedidos.setMinimumSize(QSize(80, 31))
        self.btn_alterar_tb_pedidos.setMaximumSize(QSize(80, 31))

        self.horizontalLayout_4.addWidget(self.btn_alterar_tb_pedidos)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_13.addWidget(self.widget_14)

        self.paginas.addWidget(self.consulta_pedido)
        self.consulta_fornecedor = QWidget()
        self.consulta_fornecedor.setObjectName(u"consulta_fornecedor")
        self.verticalLayout_20 = QVBoxLayout(self.consulta_fornecedor)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_97 = QWidget(self.consulta_fornecedor)
        self.widget_97.setObjectName(u"widget_97")
        self.widget_97.setMinimumSize(QSize(0, 75))
        self.widget_97.setMaximumSize(QSize(16777215, 75))
        self.widget_97.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_97.setStyleSheet(u"QFrame {\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 8px;\n"
"}")
        self.gridLayout_31 = QGridLayout(self.widget_97)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_32 = QLabel(self.widget_97)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_31.addWidget(self.label_32, 0, 0, 1, 1)


        self.verticalLayout_20.addWidget(self.widget_97)

        self.widget_98 = QWidget(self.consulta_fornecedor)
        self.widget_98.setObjectName(u"widget_98")
        self.widget_98.setMinimumSize(QSize(0, 0))
        self.widget_98.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_68 = QVBoxLayout(self.widget_98)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.splitter_7 = QSplitter(self.widget_98)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Orientation.Horizontal)
        self.txt_pesquisar_tb_fornecedores = QLineEdit(self.splitter_7)
        self.txt_pesquisar_tb_fornecedores.setObjectName(u"txt_pesquisar_tb_fornecedores")
        self.txt_pesquisar_tb_fornecedores.setMinimumSize(QSize(200, 0))
        self.txt_pesquisar_tb_fornecedores.setMaximumSize(QSize(400, 16777215))
        self.splitter_7.addWidget(self.txt_pesquisar_tb_fornecedores)

        self.verticalLayout_68.addWidget(self.splitter_7)

        self.tb_fornecedores = QTableWidget(self.widget_98)
        if (self.tb_fornecedores.columnCount() < 4):
            self.tb_fornecedores.setColumnCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font);
        self.tb_fornecedores.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font);
        self.tb_fornecedores.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font);
        self.tb_fornecedores.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font);
        self.tb_fornecedores.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        if (self.tb_fornecedores.rowCount() < 1):
            self.tb_fornecedores.setRowCount(1)
        self.tb_fornecedores.setObjectName(u"tb_fornecedores")
        self.tb_fornecedores.setStyleSheet(u"")
        self.tb_fornecedores.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tb_fornecedores.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tb_fornecedores.setSortingEnabled(True)
        self.tb_fornecedores.setRowCount(1)
        self.tb_fornecedores.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_fornecedores.horizontalHeader().setDefaultSectionSize(200)
        self.tb_fornecedores.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_68.addWidget(self.tb_fornecedores)


        self.verticalLayout_20.addWidget(self.widget_98)

        self.widget_96 = QWidget(self.consulta_fornecedor)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setMinimumSize(QSize(0, 50))
        self.widget_96.setMaximumSize(QSize(16777215, 50))
        self.widget_96.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_96)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_salvar_tb_fornecedores = QPushButton(self.widget_96)
        self.btn_salvar_tb_fornecedores.setObjectName(u"btn_salvar_tb_fornecedores")
        self.btn_salvar_tb_fornecedores.setEnabled(True)
        self.btn_salvar_tb_fornecedores.setMinimumSize(QSize(80, 31))
        self.btn_salvar_tb_fornecedores.setMaximumSize(QSize(80, 31))

        self.horizontalLayout_15.addWidget(self.btn_salvar_tb_fornecedores)

        self.btn_excel_tb_fornecedores = QPushButton(self.widget_96)
        self.btn_excel_tb_fornecedores.setObjectName(u"btn_excel_tb_fornecedores")
        self.btn_excel_tb_fornecedores.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_15.addWidget(self.btn_excel_tb_fornecedores)

        self.pushButton_51 = QPushButton(self.widget_96)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setMinimumSize(QSize(80, 31))

        self.horizontalLayout_15.addWidget(self.pushButton_51)

        self.btn_alterar_tb_fornecedores = QPushButton(self.widget_96)
        self.btn_alterar_tb_fornecedores.setObjectName(u"btn_alterar_tb_fornecedores")
        self.btn_alterar_tb_fornecedores.setMinimumSize(QSize(80, 31))
        self.btn_alterar_tb_fornecedores.setMaximumSize(QSize(80, 31))

        self.horizontalLayout_15.addWidget(self.btn_alterar_tb_fornecedores)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_13)


        self.verticalLayout_20.addWidget(self.widget_96)

        self.paginas.addWidget(self.consulta_fornecedor)

        self.verticalLayout_6.addWidget(self.paginas)


        self.horizontalLayout_2.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.main)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 50))
        self.footer.setMaximumSize(QSize(16777215, 50))
        self.footer.setStyleSheet(u"QWidget {\n"
"    background-color: #3A8D2F;\n"
"    color: white;\n"
"}")
        self.footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)
        self.widget_4 = QWidget(self.footer)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(160, 70, 120, 80))

        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(4)
        self.toolBox.layout().setSpacing(6)
        self.paginas.setCurrentIndex(4)
        self.btn_cnpj.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de Vendas", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_novo_pedido.setText(QCoreApplication.translate("MainWindow", u"Novo Pedido", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Vendas", None))
        self.btn_cadastrar_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_cadastrar_produtos.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.btn_cadastrar_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Fornecedores", None))
        self.btn_cadastrar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.btn_consultar_pedidos.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.btn_consultar_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_consultar_produtos.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.btn_consultar_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Fornecedores", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Consulta", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"Relat\u00f3rios", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE FORNECEDORES", None))
        self.txt_cnpj_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF / CNPJ", None))
        self.btn_cnpj.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.txt_nome_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO FORNECEDOR", None))
        self.txt_telefone_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.txt_email_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.btn_salvar_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE USU\u00c1RIO", None))
        self.txt_nome_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.txt_email_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.txt_cpf_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.txt_criar_senha.setText("")
        self.txt_criar_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CRIAR SENHA", None))
        self.txt_repetir_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"REPETIR SENHA", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE CLIENTES", None))
        self.txt_nome_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.txt_cpf_cliente.setText("")
        self.txt_cpf_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_logradouro_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.txt_numero_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        self.txt_complemento_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.txt_bairro_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.txt_telefone_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.txt_email_cliente.setText("")
        self.txt_email_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.btn_salvar_cliente.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE PRODUTOS", None))
        self.txt_nome_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PRODUTO", None))
        self.cb_tipo_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TIPO", None))
        self.txt_valor_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR DE VENDA", None))
        self.btn_salvar_produto.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"KORIN", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE VENDAS", None))
        self.txt_nome_cliente_venda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO CLIENTE", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"CADASTRO DE PRODUTO", None))
        self.txt_codigo_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C\u00d3DIGO", None))
        self.txt_quantidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None))
        self.txt_tipo_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MEDIDA", None))
        self.txt_valor_unitario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR UNIT\u00c1RIO", None))
        self.txt_subtotal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SUBTOTAL", None))
        self.cb_selecionar_produto.setCurrentText("")
        self.cb_selecionar_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SELECIONE O PRODUTO", None))
        self.btn_inserir_item.setText(QCoreApplication.translate("MainWindow", u"Inserir", None))
        self.btn_inserir_cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.txt_numero_pedido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba DO PEDIDO", None))
        self.btn_carregar_pedido.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))
        ___qtablewidgetitem = self.tb_vendas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtablewidgetitem1 = self.tb_vendas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None));
        ___qtablewidgetitem2 = self.tb_vendas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None));
        ___qtablewidgetitem3 = self.tb_vendas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"TIPO", None));
        ___qtablewidgetitem4 = self.tb_vendas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"VALOR", None));
        ___qtablewidgetitem5 = self.tb_vendas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"SUBTOTAL", None));
        self.txt_total.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TOTAL", None))
        self.btn_excluir_item.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_sair_venda.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.btn_nova_venda.setText(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.btn_finalizar_pedido.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.txt_pesquisar_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        ___qtablewidgetitem6 = self.tb_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.tb_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem8 = self.tb_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem9 = self.tb_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"LUGRADOURO", None));
        ___qtablewidgetitem10 = self.tb_clientes.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem11 = self.tb_clientes.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem12 = self.tb_clientes.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem13 = self.tb_clientes.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem14 = self.tb_clientes.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_salvar_tb_clientes.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_excel_tb_clientes.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.btn_excluir_tb_clientes.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_selecionar_cliente.setText(QCoreApplication.translate("MainWindow", u"Venda", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"PRODUTOS", None))
        self.txt_pesquisar_tb_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        ___qtablewidgetitem15 = self.tb_produtos.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem16 = self.tb_produtos.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"NOME DO PRODUTO", None));
        ___qtablewidgetitem17 = self.tb_produtos.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"TIPO", None));
        ___qtablewidgetitem18 = self.tb_produtos.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"VALOR DE VENDA", None));
        self.btn_salvar_tb_produto.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_excel_tb_produto.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.btn_excluir_tb_produto.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_alterar_tb_produto.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PEDIDOS", None))
        self.txt_pesquisar_pedido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        ___qtablewidgetitem19 = self.tb_pedidos.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"PEDIDO", None));
        ___qtablewidgetitem20 = self.tb_pedidos.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None));
        ___qtablewidgetitem21 = self.tb_pedidos.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"VALOR", None));
        ___qtablewidgetitem22 = self.tb_pedidos.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        self.btn_salvar_tb_pedidos.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_imprimir_tb_pedidos.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.btn_excluir_tb_pedidos.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_alterar_tb_pedidos.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"FORNECEDORES", None))
        self.txt_pesquisar_tb_fornecedores.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        ___qtablewidgetitem23 = self.tb_fornecedores.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"CNPJ/CPF", None));
        ___qtablewidgetitem24 = self.tb_fornecedores.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"NOME DO FORNECEDOR", None));
        ___qtablewidgetitem25 = self.tb_fornecedores.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem26 = self.tb_fornecedores.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_salvar_tb_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_excel_tb_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_alterar_tb_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
    # retranslateUi

