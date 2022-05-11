STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+','o','-'
ZMAGA, PORAZ = 'W', 'X'

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        if self.stevilo_napak() <= 10:
            for crka in self.geslo:
                if crka not in self.pravilne_crke():
                    return False
        return ZMAGA

    def poraz(self):
        if self.stevilo_napak() > 10:
            return PORAZ
        return False 
    
    def pravilni_del_gesla(self):
        output = ''
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                output += crka
            else:
                output += '_'
        return output

    def nepravilni_ugibi(self):
        output = ''
        for crka in self.napacne_crke():
            output += crka + ' '
        return output

    def ugibaj(self, crka):
        velika_crka = crka.upper()
        if crka in self.geslo and crka not in self.pravilne_crke():
            return PRAVILNA_CRKA
        elif crka in self.pravilne_crke() or crka in self.napacne_crke():
            return PONOVLJENA_CRKA
        elif crka not in self.geslo:
            return NAPAC