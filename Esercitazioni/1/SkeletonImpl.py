from IMagazzino import IMagazzino
import threading


class SkeletonImpl(IMagazzino):
    def __init__(self, dim ,codaSmartphone:list, codaLaptop:list, cv_cons_l:threading.Condition, cv_prod_l:threading.Condition,cv_cons_s:threading.Condition, cv_prod_s:threading.Condition):
        self.codaSmartphone = codaSmartphone
        self.codaLaptop = codaLaptop
        self.cv_prod_l = cv_prod_l
        self.cv_cons_l = cv_cons_l
        self.cv_prod_s = cv_prod_s
        self.cv_cons_s = cv_cons_s
        self.dim = dim

    def deposita(self, articolo:str , id:int)->None:
        if (articolo == 'smartphone'):
            with self.cv_prod_s:
                while(len(self.codaSmartphone) == self.dim):
                    self.cv_prod_s.wait()
                self.codaSmartphone.append(id)

                self.cv_cons_s.notify()
        else: 
            with self.cv_prod_l:
                while(len(self.codaLaptop) == self.dim):
                    self.cv_prod_l.wait()
                self.codaLaptop.append(id)
                self.cv_cons_l.notify()
            

    def preleva(self, articolo:str) ->int:
        res = -1
        if (articolo == 'smartphone'):
            with self.cv_cons_s:
                while(len(self.codaSmartphone) == 0):
                    self.cv_cons_s.wait()
                res = self.codaSmartphone.pop(0)
                self.cv_prod_s.notify()
            
            with open('/home/studente/Desktop/acp/preparazione_finale/1/smartphone.txt', 'a') as file:
                file.write(f'prelevato [id = {res}]\n')
            
        else:
            with self.cv_cons_l:
                while(len(self.codaLaptop) == 0):
                    self.cv_cons_l.wait()
                res = self.codaLaptop.pop(0)
                self.cv_prod_l.notify()

            with open('/home/studente/Desktop/acp/preparazione_finale/1/laptop.txt', 'a') as file:
                file.write(f'prelevato [id = {res}]\n')
        return res
        