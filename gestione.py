class Gestione:
    def __init__(self):
        self.__specie= {"rinoceronte" : ["savana", "15Kg_vegetale", "Rinoceronte di Giava\nIl rinoceronte di Giava, fa parte dei rinoceronti asiatici. La pelle è ricoperta da spesse pieghe che sembrano quasi formare una sorta di armatura."], \
                        "leone" : ["savana", "6Kg_carne", "Il leone, noto come re della foresta, è un grande felino che abita le zone aride di Africa e India. Si tratta di un predatore rapido e veloce, che vive in branco di più esemplari e in cui la caccia spetta alle femmine."], \
                        "giraffa" : ["savana", "", ""], \
                        "gazzella" : "", \
                        "gnu" : "not iunix", \
                        "elefante" : "", \
                        "leone" : "", \
                        "pesce" : "", \
                        "rana" : "", \
                        "tartaruga" : "", \
                        "cormorano" : "", \
                        "ippopotamo" : "", \
                        "coccodrillo" : "", \
                        "bisonte" : "", \
                        "panda" : "", \
                        "scimmia" : "", \
                        "pitone" : "", \
                        "leopardo" : "", \
                        "giaguaro" : "", \
                        "formica" : "", \
                        "leocorno" : "", \
                        "mucca" : "", 
                        "cavallo" : "", \
                        "capra": "", \
                        "maiale" : ""}

    def getSpecie(self):
        return self.__specie