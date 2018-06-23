class Aluno:
    def notas(self):
        self.n1 = int(input("Informe a primeira nota do Aluno:"))
        self.n2 = int(input("Informe a primeira nota do Aluno:"))
        self.media = (self.n1 + self.n2) / 2
        return self.media

    def nome(self):
        self.nome = str(input("Informe nome do Aluno:"))


aluno1 = Aluno()
aluno2 = Aluno()
aluno3 = Aluno()

aluno1.nome()
media = aluno1.notas()
print('Media = ' + str(media))
