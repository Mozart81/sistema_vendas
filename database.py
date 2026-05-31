import sqlite3







class Data_base:

    def __init__(self, name = 'system.db') -> None:
        self.name = name
        
    def connect(self):
        self.connection = sqlite3.connect(self.name)
        self.connection.row_factory = sqlite3.Row

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)

##################### CLIENTE ###################################

    def create_table_client(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes(
            ID_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL UNIQUE,
            CPF TEXT,           
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            TELEFONE TEXT,
            EMAIL TEXT
                       
            );
            """)
    
    def register_client(self, fullDataSet):

        cursor = self.connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO Clientes (NOME, CPF, LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, TELEFONE, EMAIL)
                VALUES (?,?,?,?,?,?,?,?)
            """, fullDataSet)

            self.connection.commit()
            return "OK"

        except Exception as e:
            print("ERRO NO BANCO:", e)
            return "Erro"

    def select_all_clients(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Clientes ORDER BY NOME")
            clientes = cursor.fetchall()
            return clientes
        except:
            pass

    def delete_client(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Clientes WHERE ID = '{id}' ")
            
            self.connection.commit()

            return 'Cadastro do clientes excluido com sucesso'
        except:
            return "Erro ao excluir o cadastro"
        
    def update_client(self, fullDataSet):

        cursor = self.connection.cursor()
        cursor.execute(f"""
            UPDATE Clientes SET
            
            NOME = '{fullDataSet[1]}',
            CPF = '{fullDataSet[2]}',
            LOGRADOURO = '{fullDataSet[3]}',
            NUMERO = '{fullDataSet[4]}',
            COMPLEMENTO = '{fullDataSet[5]}',
            BAIRRO = '{fullDataSet[6]}',
            TELEFONE = '{fullDataSet[7]}',
            EMAIL = '{fullDataSet[8]}'
                       
            WHERE ID_CLIENTE = '{fullDataSet[0]}'""")
        
        self.connection.commit()

##################### FORNECEDOR ###################################

    def create_table_fornecedor(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Fornecedor(
            CNPJ TEXT PRIMARY KEY,
            NOME_FORNECEDOR TEXT,
            TELEFONE TEXT,
            EMAIL TEXT

        );
    """)

    def register_fornecedor(self, fullDataSet):
        cursor = self.connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO Fornecedor (CNPJ, NOME_FORNECEDOR, TELEFONE, EMAIL)
                VALUES (?, ?, ?, ?)
            """, fullDataSet)

            self.connection.commit()
            return "OK"

        except Exception as e:
            print("ERRO NO BANCO:", e)
            return "Erro"

    def select_all_fornecedor(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Fornecedor ORDER BY NOME_FORNECEDOR")
            fornecedores = cursor.fetchall()
            return fornecedores
        except:
            pass

    def delete_fornecedor(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Fornecedor WHERE CNPJ = '{id}' ")
            
            self.connection.commit()

            return 'Cadastro do Fornecedor excluido com sucesso'
        except:
            return "Erro ao excluir o cadastro"
        
    def update_fornecedor(self, fullDataSet):
        
        cursor = self.connection.cursor()
        cursor.execute(f"""
            UPDATE Fornecedor(
            
            CNPJ = '{fullDataSet[0]}',
            NOME FORNECEDOR = '{fullDataSet[1]}',
            TELEFONE = '{fullDataSet[2]}',
            E-MAIL = '{fullDataSet[3]}'
                       
            WHERE CNPJ = '{fullDataSet[0]}',
            """)
        
        self.connection.commit()

##################### produtos ###################################

    def create_table_product(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Produtos(
            ID_PRODUTO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            PRODUTO TEXT NOT NULL UNIQUE,
            TIPO TEXT NOT NULL,           
            VALOR REAL NOT NULL
                      
        );
    """)
    
    def register_product(self, fullDataSet):

        cursor = self.connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO Produtos (PRODUTO, TIPO, VALOR)
                VALUES (?,?,?)
            """, fullDataSet)

            self.connection.commit()
            return "OK"

        except Exception as e:
            print("ERRO NO BANCO:", e)
            return "Erro"

    def select_all_product(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Produtos ORDER BY ID_PRODUTO")
            produtos = cursor.fetchall()
            return produtos
        except:
            pass

    def delete_product(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Produtos WHERE ID = '{id}' ")
            
            self.connection.commit()

            return 'Cadastro do produto excluido com sucesso'
        except:
            return "Erro ao excluir o cadastro"
        
    def update_product(self, fullDataSet):

        cursor = self.connection.cursor()
        cursor.execute(f"""
            UPDATE Produtos SET
            
            PRODUTO = '{fullDataSet[1]}',
            TIPO = '{fullDataSet[2]}',
            VALOR = '{fullDataSet[3]}',
                                   
            WHERE ID = '{fullDataSet[0]}'""")
        
        self.connection.commit()

##################### PEDIDOS ###################################

    def select_all_pedidos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           SELECT
                                Pedidos.ID_PEDIDO,
                                Clientes.NOME,
                                Pedidos.TOTAL,
                                Pedidos.DATA
                            FROM Pedidos
                            INNER JOIN Clientes
                                ON Pedidos.ID_CLIENTE = Clientes.ID_CLIENTE
                            ORDER BY Pedidos.ID_PEDIDO
                           """)
            pedidos = cursor.fetchall()
            return pedidos
        except Exception as e:
            print("ERRO AO BUSCAR PEDIDOS:", e)
            return []

#####################combobox ##########################

    def select_produtos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT PRODUTO FROM Produtos ORDER BY PRODUTO")
            produtos = cursor.fetchall()
            resultado = [item[0] for item in produtos]
            return resultado
        except:
            pass
    
    def select_tipo(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT MEDIDA FROM Medidas ORDER BY MEDIDA")
            tipo = cursor.fetchall()
            resultado = [item[0] for item in tipo]
            return resultado
        except:
            pass

    def buscar_produto_por_nome(self, nome):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT ID_PRODUTO PRODUTO, TIPO, VALOR 
                FROM Produtos 
                WHERE PRODUTO = ?
            """, (nome,))
            
            return cursor.fetchone()
        except Exception as e:
            print(e)

############################ TESTE GENERICO ##################
    def register(self, nome_tabela, cabecalho, fullDataSet):
        
        placeholders = "(" + ",".join(["?"] * len(cabecalho)) + ")"
        cursor = self.connection.cursor()

        try:
            cursor.execute(F"""
                INSERT INTO {nome_tabela} {cabecalho}""", fullDataSet)

            self.connection.commit()
            return "OK"

        except Exception as e:
            print("ERRO NO BANCO:", e)
            return "Erro"
        
    def create_table(self,nome_tabela, colunas):
        cursor = self.connection.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {nome_tabela}(
            {colunas}                      
        );
    """)
        
    def pesquisar_2(self, busca, tabela):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM {tabela} WHERE NOME LIKE ?", (f"%{busca}%",))
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao pesquisar: {e}")
            return []
        
    def pesquisar(self, busca, tabela):
        try:
            cursor = self.connection.cursor()

            # pega nomes das colunas
            cursor.execute(f"PRAGMA table_info({tabela})")
            colunas = [col[1] for col in cursor.fetchall()]

            # monta WHERE dinamicamente
            condicoes = " OR ".join([f"{col} LIKE ?" for col in colunas])

            query = f"SELECT * FROM {tabela} WHERE {condicoes}"

            valor = f"%{busca}%"
            parametros = [valor] * len(colunas)

            cursor.execute(query, parametros)

            return cursor.fetchall()

        except Exception as e:
            print(f"Erro ao pesquisar: {e}")
            return []

    def buscar_itens_pedido_old(self, id_pedido):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT 
                    COD_PRODUTO,
                    PRODUTO,
                    QUANTIDADE,
                    TIPO,
                    VALOR_UNITARIO,
                    SUBTOTAL,
                    ID_CLIENTE
                FROM Itens
                WHERE ID_PEDIDO = ?
            """, (id_pedido,))
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def buscar_itens_pedido(self, id_pedido):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT 
                    Itens.COD_PRODUTO,
                    Itens.PRODUTO,
                    Itens.QUANTIDADE,
                    Itens.TIPO,
                    Itens.VALOR_UNITARIO,
                    Itens.SUBTOTAL,
                    Pedidos.ID_CLIENTE,
                    Clientes.NOME
                FROM Itens
                INNER JOIN Pedidos
                    ON Itens.ID_PEDIDO = Pedidos.ID_PEDIDO
                INNER JOIN Clientes
                    ON Pedidos.ID_CLIENTE = Clientes.ID_CLIENTE
                WHERE Itens.ID_PEDIDO = ?
            """, (id_pedido,))

            return cursor.fetchall()
        except Exception as e:
            print(e)
            return []