CUPONS_DESCONTO = {
    'ASD' : 10,
    'QWE' : 0
}

def obter_desconto(codigo: str):
    if codigo is None:
        return 0
    if codigo not in CUPONS_DESCONTO:
        return 0
    return CUPONS_DESCONTO[codigo]


def calcular_total(itens, desconto_percentual=0):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)
    """
CUPONS_DESCONTO = {
    'DEVOPS10': 10,
}

def obter_desconto(codigo: str|None):
    if codigo is None:
        return 0

    codigo = codigo.strip().upper()
    if codigo not in CUPONS_DESCONTO:
        raise ValueError("Código não está na lista de descontos.")
    return CUPONS_DESCONTO[codigo]

def calcular_total(
    itens, 
    desconto_percentual=0, 
    cupom:str|None=None
):
    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    desconto1 = (subtotal * (desconto_percentual/100))

    desconto_cupom = obter_desconto(cupom)
    desconto2 = (subtotal * (desconto_cupom/100))

    total = subtotal - desconto1 - desconto2

    #teste
    return round(total, 2)