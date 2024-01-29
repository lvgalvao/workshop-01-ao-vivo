import pytest
from datetime import datetime
from src.contrato import Vendas
from pydantic import ValidationError

def test_vendas_com_dados_validos():
    """
    Testa a criação de uma instância da classe Vendas com dados válidos.

    Este teste verifica se a classe Vendas aceita e armazena corretamente os dados válidos fornecidos.
    Dados válidos incluem um email correto, data atual, valor positivo, nome do produto, quantidade positiva
    e uma categoria existente. O teste confirma se os valores armazenados na instância correspondem aos dados fornecidos.
    """
    dados_validos = {
            "email": "comprador@example.com",
            "data": datetime.now(),
            "valor": 100.50,
            "produto": "Produto X",
            "quantidade": 3,
            "categoria": "categoria3",
        }

    venda = Vendas(**dados_validos)

    assert venda.email == dados_validos["email"]
    assert venda.data == dados_validos["data"]
    assert venda.valor == dados_validos["valor"]
    assert venda.produto == dados_validos["produto"]
    assert venda.quantidade == dados_validos["quantidade"]
    assert venda.categoria == dados_validos["categoria"]

def test_vendas_com_dados_invalidos():
    """
    Testa a criação de uma instância da classe Vendas com dados inválidos.

    Este teste verifica a validação de dados na classe Vendas. Dados inválidos incluem um email incorreto, 
    data em formato inválido, valor negativo, nome do produto vazio, quantidade negativa, e uma categoria válida.
    Espera-se que a classe Vendas gere uma exceção ValidationError quando dados inválidos são fornecidos.
    """
    dados_invalidos = {
        "email": "comprador",
        "data": "não é uma data",
        "valor": -100,
        "produto": "",
        "quantidade": -1,
        "categoria": "categoria3"
    }

    with pytest.raises(ValidationError):
        Vendas(**dados_invalidos)

def test_validacao_categoria():
    """
    Testa a validação da categoria na criação de uma instância da classe Vendas.

    Este teste especificamente verifica se a classe Vendas valida a categoria do produto. 
    Ele utiliza dados válidos para todos os campos, exceto pela categoria, que é definida como uma categoria inexistente.
    Espera-se que a classe Vendas gere uma exceção ValidationError devido à categoria inválida.
    
    args:
        dados = {
        email: comprador@example.com
        data: datetime.now()
        valor: 100.50
        produto: Produto Y
        quantidade: 1
        categoria: categoria inexistente
    }
    """
    dados = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto Y",
        "quantidade": 1,
        "categoria": "categoria inexistente",
    }

    with pytest.raises(ValidationError):
        Vendas(**dados)