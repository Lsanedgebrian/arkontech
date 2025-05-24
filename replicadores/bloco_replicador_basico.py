from core.ArKoMatriarca import Block

class BlocoReplicadorBasico(Block):
    symbolic_name = 'replicador_basico'
    BLOCO_ID = "REP001"
    PROJETO = "ARKONTECH"
    DESCRICAO = "Replica blocos com base em padrão simbólico."

    inputs = {'bloco_base': dict}
    outputs = {'replicas': list}

    def execute(self, bloco_base):
        return {'replicas': [bloco_base.copy() for _ in range(3)]}
