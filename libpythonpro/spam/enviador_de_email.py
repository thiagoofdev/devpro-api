class Enviador:
    def enviar(self, remetente, destinatario, assunto, corop):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido. {remetente}')
        return remetente

class EmailInvalido(Exception):
    pass
