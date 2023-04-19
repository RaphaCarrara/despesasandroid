from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle


class BannerRegistros(GridLayout):

    def __init__(self, **kwargs):
        self.rows = 1
        super().__init__()

        with self.canvas:
            Color(rgb = (0, 0, 0, 1))
            self.rec = Rectangle(size = self.size, pos = self.pos)
        self.bind(pos = self.atualizar_rec, size = self.atualizar_rec)

        codigo = kwargs["codigo"]
        tipo = kwargs["tipo"]
        status = kwargs["status"]
        descricao = kwargs["descricao"]
        responsavel = kwargs["responsavel"]
        valor = kwargs["valor"]
        data_vencimento = kwargs["data_vencimento"]
        data_vencimento = data_vencimento.strftime('%d/%m/%Y')
        valor_pago = kwargs["valor_pago"]
        data_pagamento = kwargs["data_pagamento"]
        if (data_pagamento) != None:
            data_pagamento = data_pagamento.strftime('%d/%m/%Y')
        else:
            data_pagamento = ""
        observacao = kwargs["observacao"]



        print("Esquerda")

        coluna1 = FloatLayout()
        esquerda_label_codigo = Label(text=f"{codigo}", pos_hint={"right": 0.55, "top": 0.95}, size_hint=(0.33, 0.33), font_size = 12)
        esquerda_label_tipo = Label(text=tipo, pos_hint={"right": 0.55, "top": 0.75}, size_hint=(0.33, 0.33), font_size = 12)
        esquerda_label_vencimento = Label(text=f"V: {data_vencimento}", pos_hint={"right": 0.55, "top": 0.55}, size_hint=(0.33, 0.33), font_size = 12)
        coluna1.add_widget(esquerda_label_codigo)
        coluna1.add_widget(esquerda_label_tipo)
        coluna1.add_widget(esquerda_label_vencimento)

        print("Centro")

        centro = FloatLayout()
        centro_imagem = Label(text=descricao, pos_hint={"right": 1, "top": 0.95}, size_hint=(0.66, 0.33), font_size = 12, halign = 'right')
        centro_label = Label(text=f"{status} / {responsavel}", pos_hint={"right": 0.6, "top": 0.75}, size_hint=(0.66, 0.33), font_size = 12)
        centro_label_data_pagamento = Label(text=f"P: {data_pagamento}", pos_hint={"right": 0.6, "top": 0.55}, size_hint=(0.66, 0.33), font_size = 12)
        centro.add_widget(centro_imagem)
        centro.add_widget(centro_label)
        centro.add_widget(centro_label_data_pagamento)


        print("Direita")

        direita = FloatLayout()
        #direita_label_vencimento = Label(text=f"Pagto: {data_pagamento}", pos_hint={"right": 1, "top": 0.95}, size_hint=(1, 0.33))
        direita_label_valor = Label(text=f"Valor: R$ {valor:,.2F}", pos_hint={"right": 1, "top": 0.75}, size_hint=(1, 0.33), font_size = 12)
        direita_label_valor_pago = Label(text=f"Pago: R$ {valor_pago:,.2F}", pos_hint={"right": 1, "top": 0.55}, size_hint = (1, 0.33), font_size = 12)
        #direita.add_widget(direita_label_vencimento)
        direita.add_widget(direita_label_valor)
        direita.add_widget(direita_label_valor_pago)

        self.add_widget(coluna1)
        self.add_widget(centro)
        self.add_widget(direita)

    def atualizar_rec(self, *args):
        self.rec.pos = self.pos
        self.rec.size = self.size






