from libpythonpro.spam.enviador_de_email import Enviador

def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None

def test_remetente():
    enviador=Enviador()
    resultado = enviador.enviar(
        'tof1@email.com', #Origem
        'tof2@email.com', #Destino
        'Curso pytools', #Assunto
        'Refazendo o curso pytools', #Corpo
    )
    assert 'tof1@email.com' in resultado