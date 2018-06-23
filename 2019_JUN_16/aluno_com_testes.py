class Aluno:
    def __init__(self, nome=None):
        if nome is None:
            self.nome = "Abacaxi"
        else:
            self.nome = nome

    def notas(self, nota1, nota2):
        try:
            nota1 = int(nota1)
            nota2 = int(nota2)
        except ValueError:
            return ""
        if nota1 > 10:
            nota1 = 10
        if nota2 > 10:
            nota2 = 10
        self.nota1 = int(nota1)
        self.nota2 = int(nota2)
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def setar_faculdade(self, nome_faculdade):
        self.faculdade = nome_faculdade

    def altera_nome(self, nome):
        self.nome = nome


aluno1 = Aluno('José')
aluno2 = Aluno()
assert(aluno2.nome == "Abacaxi")
assert(aluno1.nome == "José")
assert(aluno1.notas(5, 7) == 6)
assert(aluno1.notas(5, 9) == 7)
assert(aluno1.notas(0, 0) == 0)
assert(aluno1.notas(11, 11) == 10)
assert(aluno1.notas('11', 11) == 10)
assert(aluno1.notas('a', 11) == "")
assert(aluno1.notas(7, "7") == 7)
aluno1.altera_nome('Orlando')
assert("Orlando" == aluno1.nome)
aluno1.setar_faculdade('FATEC')
assert("FATEC" == aluno1.faculdade)
