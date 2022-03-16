from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente', 
    ['tof1@email.com', 'foor@bar.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente, #Destino
        'tof2@email.com', #Origem_Enviador
        'Curso pytools', #Assunto
        'Refazendo o curso pytools', #Corpo
    )
    assert remetente in resultado

@pytest.mark.parametrize(
    'remetente', 
    ['', 'foor']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente, #Destino
            'tof2@email.com', #Origem_Enviador
            'Curso pytools', #Assunto
            'Refazendo o curso pytools', #Corpo
        )
