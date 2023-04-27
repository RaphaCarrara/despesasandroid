from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from bannerregistros import BannerRegistros
#import pyodbc
from pymssql import _mssql
from pySql import conn
from datetime import datetime, timedelta
from botoes import *


class HomePage(Screen):
    pass


class DadosEntrada(Screen):
    pass


GUI = Builder.load_file("main.kv")


class MainApp(App):

    def build(self):
        self.title = "Despesas"
        self.icon = 'icones/banco.png'
        return GUI

    def on_start(self):

        # carrega as infos de usuario
        print("On_Start")
        dataAtual = datetime.today()

        self.root.ids.txt_mes.text = dataAtual.strftime("%m")
        self.root.ids.txt_ano.text = dataAtual.strftime("%Y")
        self.carregar_infos()

    def mudar_tela(self, id_tela):
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

    def carregar_infos(self):

        dicDatas = self.calculaIntervaloDatas(int(self.root.ids.txt_mes.text), int(self.root.ids.txt_ano.text))
        dataInicial = dicDatas[0]
        dataFinal = dicDatas[1]

        #conexao = _mssql.connect(conn)
        cursor = conn.cursor()

        comando = f"""SELECT * FROM dbo.movimento Where datavencimento >= '{dataInicial}' And datavencimento <= '{dataFinal}' ORDER BY dataVencimento"""
        cursor.execute(comando)

        # preencher lista de registros
        try:

            pagina_homepage = self.root.ids['homepage']
            lista_registros = pagina_homepage.ids['lista_registros']
            lista_registros.clear_widgets()

            row = cursor.fetchone()

            while row:
                codigo = row[0]
                descricao = row[1]
                datavencimento = row[2]
                datapagamento = row[3]
                valor = row[4]
                valorpago = row[5]
                responsavel = row[6]
                tipo = row[7]
                status = row[8]
                descricaodetalhada = row[9]

                banner = BannerRegistros(codigo=codigo, tipo=tipo, status=status,
                                         descricao=descricao, responsavel=responsavel,
                                         valor=valor, data_vencimento=datavencimento,
                                         valor_pago=valorpago, data_pagamento=datapagamento,
                                         observacao=descricaodetalhada)

                lista_registros.add_widget(banner)

                row = cursor.fetchone()


        except:
            print("Pass")
            pass

    def calculaIntervaloDatas(self, mes, ano):

        print("calculaIntervaloDatas: " + str(mes) + "/" + str(ano))

        dataInicial = datetime(year = ano, month = mes, day = 1)
        dataFinal = datetime(year = ano, month = mes + 1, day = 1)
        dataFinal = dataFinal - timedelta(days = 1)

        return dataInicial, dataFinal

    def somaMes(self):

        proximo_mes = int(self.root.ids.txt_mes.text) + 1
        ano = int(self.root.ids.txt_ano.text)

        print(proximo_mes)
        if proximo_mes > 12:
            self.root.ids.txt_mes.text = "01"
            self.root.ids.txt_ano.text = str(ano + 1)

        elif proximo_mes < 10:
            self.root.ids.txt_mes.text = "0" + str(proximo_mes)

        else:
            self.root.ids.txt_mes.text = str(proximo_mes)

        #self.carregar_infos()

    def diminuiMes(self):

        print("A: " + str(self.root.ids.txt_mes.text))

        proximo_mes = int(self.root.ids.txt_mes.text) - 1
        ano = int(self.root.ids.txt_ano.text)

        print("B: " + str(proximo_mes))
        if proximo_mes < 1:
            self.root.ids.txt_mes.text = "12"
            self.root.ids.txt_ano.text = str(ano - 1)

        elif proximo_mes < 10:
            self.root.ids.txt_mes.text = "0" + str(proximo_mes)

        else:
            self.root.ids.txt_mes.text = str(proximo_mes)

        #self.carregar_infos()

MainApp().run()
