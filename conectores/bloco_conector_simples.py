from core.ArKoMatriarca import Block

class BlocoConectorSimples(Block):
    symbolic_name = 'conector_simples'
    BLOCO_ID = "CON001"
    PROJETO = "ARKONTECH"
    DESCRICAO = "Conecta dois blocos sequencialmente."

    inputs = {'entrada_1': str, 'entrada_2': str}
    outputs = {'saida_conectada': str}

    def execute(self, entrada_1, entrada_2):
        return {'saida_conectada': f"{entrada_1} >> {entrada_2}"}
