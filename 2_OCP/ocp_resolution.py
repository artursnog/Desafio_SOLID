from abc import ABC, abstractmethod

class AprovaExame(ABC):

    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass

    @abstractmethod
    def verificar_condicoes_exame(self, exame):
        pass

class AprovarExameSangue(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verificar_condicoes_exame(exame):
            print("Exame de sangue aprovado")

    def verificar_condicoes_exame(self, exame):
        pass

class AprovaExameRaioX(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verificar_condicoes_exame(exame):
            print("Exame Raio-X aprovado")

    def verificar_condicoes_exame(self, exame):
        pass

class Exame:
    def __init__(self, tipo) -> None:
        self.tipo = tipo

exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovador_sangue = AprovarExameSangue()
aprovador_raio_x = AprovaExameRaioX()

aprovador_sangue.aprovar_solicitacao_exame(exame_sangue)
aprovador_raio_x.aprovar_solicitacao_exame(exame_raio_x)