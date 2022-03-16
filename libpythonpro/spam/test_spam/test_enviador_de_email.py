from libpythonpro.spam.enviador_de_email import Enviador
import pytest


def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario', 
    ['tof1@email.com', 'foor@bar.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario, #Destino
        'tof2@email.com', #Origem_Enviador
        'Curso pytools', #Assunto
        'Refazendo o curso pytools', #Corpo
    )
    assert destinatario in resultado
