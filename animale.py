from gestione import *

class Animale:
    def __init__(self, gestione, nome, eta):
        self.gestione= gestione
        self.__nome= nome
        self.__eta= eta
        self.__tipoAnimale= None
        self.__descrizione= None
        self.__habitat= None
        self.__alimento= None


    def setTipoAnimale(self):
        # mostro le specie possibili
        print("specie disponibili: ")
        for tipo in gestione.getSpecie().keys():
            print(f"  - {tipo}")

        # faccio sciegliere il tipo di animale
        tipoAnimale= input("Inserisci il tipo di animale: ")
        if tipoAnimale in gestione.getSpecie(): 
            # se esiste la specie: imposto i valori dovuti ad essa
            self.__tipoAnimale= tipoAnimale
            self.__habitat= gestione.getSpecie()[tipoAnimale][0]
            self.__alimento= gestione.getSpecie()[tipoAnimale][1]
            self.__descrizione= gestione.getSpecie()[tipoAnimale][2]
            return True
            
        #altrimenti do un segnale di errore
        print(f"Il tipo di animale {tipoAnimale} non è disponibile")
        return False

    def info(self):
        print(self.__descrizione)

    def parla(self):
        pass
    
    def muovi(self):
        pass

    def mangia(self):
        pass

    def bevi(self):
        pass

    def dormi(self):
        pass

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome= nome

    def getEta(self):
        return self.__eta
    
    def setEta(self, eta):
        self.__eta= eta