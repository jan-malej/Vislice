import bottle
import model


TIPKOVNICA = [
    "QWERTZUIOPŠ",
    "ASDFGHJKLČŽ",
    "YXCVBNM"
]
SUPER_SIFRA = 'skrivnost'

vislice = model.Vislice()


@bottle.get("/img/<file>")
def staticne_slike(file):
    return bottle.static_file(file, root="img")


@bottle.get("/favicon.ico")
def favicon():
    """
    Poskrbimo za ikonico, ki se pokaže v brskalniku v zavihku levo od imena.
    """
    return bottle.static_file("favicon.ico", root="img")


@bottle.get("/oblikovanje/<file>")
def staticni_css(file):
    return bottle.static_file(file, root="oblikovanje")


@bottle.get("/")
def osnovno():
    count = int(
        bottle.request.cookies.get('counter', '0')
    )
    count += 1
    bottle.response.set_cookie('counter', str(count))
    return bottle.template("index", stevec=count)


@bottle.route("/igra/", method=['GET', 'POST'])
def nova_igra():
    trenutni_id = int(
        bottle.request.get_cookie('trenutna_igra', secret=SUPER_SIFRA)
    )
    crka = bottle.request.forms.getunicode('crka')
    if crka:
        crka = crka.upper()
        if preveri_vnos(crka):
            vislice.ugibaj(trenutni_id, crka)
        else:
            return f"<p>To ni dovoljena črka: {crka}</p>"
    
    return bottle.template(
        'igra',
        id_igre=trenutni_id,
        igra=vislice.igre[trenutni_id][0],
        tipkovnica=TIPKOVNICA
    )

@bottle.post('/nova_igra/')
def nova_igra_s_piskotom():
    nov_id = vislice.nova_igra()
    bottle.response.set_cookie(
        'trenutna_igra', str(nov_id),
        path='/',
        secret=SUPER_SIFRA
    )
    return bottle.redirect('/igra/')

@bottle.get("/igra/<id_igre:int>")
def pokazi_igro(id_igre):
    return bottle.template("igra", id_igre=id_igre, igra=vislice.igre[id_igre][0], tipkovnica=TIPKOVNICA)


def preveri_vnos(crka):
    return len(crka) == 1 and ("A" <= crka <= "Z" or crka in "ČŽŠ")


@bottle.post('/igra/<id_igre:int>')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka').upper()
    if preveri_vnos(crka):
        vislice.ugibaj(id_igre, crka)
        return pokazi_igro(id_igre)
    else:
        return f"<p>To ni dovoljena črka: {crka}</p>"


# @bottle.get("/pretekle_igre/")
@bottle.post("/pretekle_igre/")
def pokazi_pretekle_igre():
    koncane = []
    for id_igre, (_, status) in vislice.igre.items():
        if status in [model.ZMAGA, model.PORAZ]:
            koncane.append(id_igre)
    return bottle.template("pretekle_igre", koncane_igre=koncane)


bottle.run(reloader=True, debug=True)
