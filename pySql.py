import pyodbc

dados_conexao = (
        "Driver={SQL Server};"
        "Server=144.22.217.23\MSSQLSERVER,2866;"
        "Database=Despesas;"
        "UID=GIR;"
        "PWD=Sigimadm#11#09#2001"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida !!!!")
