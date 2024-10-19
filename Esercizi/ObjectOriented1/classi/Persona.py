class persona(object):
    def __init__(self, nome = "Mario", cognome = "Rossi"):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return f"[Nome] {self.nome}; [Cognome] {self.cognome}"
    
    def get_nome(self):
        return str(self.nome)
    
    def get_cognome(self):
        return self.cognome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_cognome(self, cognome):
        self.cognome = cognome
    