class Bruker:
    """ Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte. 
    
    Attributes
        epost: En string med brukers epost
        fornavn: En string med brukers etternavn
        etternavn: En string med brukers etternavn

    """
    def __init__(self, epost, fornavn, etternavn):
        self._epost = epost
        self._fornavn = fornavn
        self._etternavn = etternavn

    def logg_inn(self):
        print(f'{self._epost} logget inn')
    
    def logg_ut(self):
        print(f'{self._epost} logget ut')
    
class Lærer(Bruker):
    """ Superklasse for Faglærer og Kontaktlærer og subklasse for Bruker.

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers etternavn
        etternavn: En string med brukers etternavn
        lonnskonto: En integer med lærerens lønningskonto
    
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn)
        self._lonnskonto = lønnskonto

class Kontaktlærer(Lærer):
    """ Subklasse for Lærere.

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers etternavn
        etternavn: En string med brukers etternavn
        klasse: En string med klassen læreren er kontaklærer til
        trinn: En integer med trinnet læreren er kontaktlærer til
    
    """
    def __init__(self, epost, fornavn, etternavn, lonnskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, lonnskonto)
        self._klasse = klasse
        self._trinn = trinn

class Faglærer(Lærer):
    """ Subklasse for Lærere.

    Inneholder en liste om lærerens kompetanse.
    Inneholder en liste med hvilke klasser læreren underviser i.

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers etternavn
        etternavn: En string med brukers etternavn
    
    """
    def __init__(self, epost, fornavn, etternavn, lonnskonto):
        super().__init__(epost, fornavn, etternavn, lonnskonto)
        self._kompetanse = []
        self._klasser = []

class Elev(Bruker):
    """ En subklasse for Bruker.

    Innholder en liste med fagene til eleven.

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers etternavn
        etternavn: En string med brukers etternavn
        trinn: En integer med trinnet eleven går i.
        klasse: En string mde klassen eleven går i.

    """
    def __init__(self, epost, fornavn, etternvan, trinn, klasse):
        super().__init__(epost, fornavn, etternvan)
        self._trinn = trinn
        self._klasse = klasse
        self._fag = []

# Denne brukes for testing, betyr at koden inne i if-setningen kun kjøres hvis vi "trykker play" på denne filen eller kjører denne fila i terminal
if __name__ == "__main__":
    ravi = Lærer("ravim@viken.no", "David Ravi", "Manikarnika", 970034056654)
    ravi.logg_inn()
    ravi.logg_ut()

    julia = Elev("juliaha@viken.no", "Julia", "Hanssen", 3, "STC")
    julia.logg_inn()
    julia.logg_ut()

