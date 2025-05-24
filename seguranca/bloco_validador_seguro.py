from core.ArKoMatriarca import Block

class ValidadorSeguro(Block):
    symbolic_name = 'validador_seguro'
    BLOCO_ID = "SEG001"
    PROJETO = "ARKONTECH"
    DESCRICAO = "Valida segurança de entradas maliciosas."

    inputs = {'entrada': str}
    outputs = {'seguro': bool}

    def execute(self, entrada):
        proibidos = [";", "--", "DROP", "rm -rf"]
        return {'seguro': not any(p in entrada for p in proibidos)}
