import pycep_correios
from validate_docbr import CNPJ

def valid_cep(cep):
    return pycep_correios.validar_cep(cep)

def valid_cnpj(document):
    cnpj = CNPJ()
    return cnpj.validate(document)
