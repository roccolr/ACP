from classi.Persona import persona

class studente(persona):
    tag = 1
    def __init__(self, nome = "Mario", cognome = "Rossi", universita = "", cds = ""):
        persona.__init__(self,nome, cognome)
        self.universita = universita
        self.cds = cds
        self.id = studente.tag
        studente.tag += 1
    
    def __str__(self):
        return f"[Nome] {self.nome}; [Cognome] {self.cognome}; [Universita] {self.universita}; [Corso di Studi] {self.cds}; [Tag] {self.id}"
    
    def get_universita(self):
        return self.universita
    
    def get_cds(self):
        return self.cds
    
    def set_universita(self, universita):
        self.universita = universita
    
    def set_cds(self, cds):
        self.cds = cds

    def test(self, str):
        print("test: "+ str)

    @staticmethod
    def static_test(str):
        print("test static: " + str + f" {studente.tag}")
    

