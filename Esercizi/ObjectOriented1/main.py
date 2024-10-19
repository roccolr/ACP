from classi.Persona import persona
from classi.Studente import studente

if __name__ == '__main__':
    # p = persona("Rocco", "Lo Russo")
    # print(p.get_nome(), p.get_cognome(), p)
    s1 = studente("Mario", "Rossi", "Federico II", "Filosofia")
    # s.madre = "Sofia"
    s2 = studente("Rocco", "Barocco", "Federico II", "Ingegneria Informatica")
    s3 = studente("Marco", "Iodice", "UniFisciano", "Ingegneria Aerospaziale")
    s = []
    s.append(s1)
    s.append(s2)
    s.append(s3)

    for e in s:
        print(e)

    studente.test(s1, "CIAO")
    studente.static_test("CIAO")


    
