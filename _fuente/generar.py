"""Genera el sitio estático bilingüe de Green Car Service Tenerife.

Uso:  python3 _fuente/generar.py
Escribe los .html en la raíz del repositorio (español) y en en/ (inglés).
"""
import importlib
import json
import os
import sys
from datetime import date

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

import nucleo as N  # noqa: E402
from nucleo import (t, esc, md, plano, ico, bloques, checks_simples, checks_titulados,  # noqa: E402
                    page_head, section_head, card_ico, card_prod, grid, seccion, boton,
                    btn_tel, btn_wa, panel, compartir, faq_html, bloque_aseguradora,
                    mitos, formulario, documento, estrellas, val)
from comun import (EMPRESA as E, GLOSARIO_TERMINOS, CATEGORIAS_SERVICIO,  # noqa: E402
                   SERVICIOS_SLUGS, CATEGORIAS_BLOG, GUIAS_SLUGS)

LANGS = ("es", "en")


# ---------------------------------------------------------------- Contenido
def cargar(nombre, attr, defecto):
    try:
        return getattr(importlib.import_module("contenido." + nombre), attr)
    except ModuleNotFoundError:
        print(f"  (aviso) falta contenido/{nombre}.py")
        return defecto


SERVICIOS = {}
for _m in sorted(f[:-3] for f in os.listdir(os.path.join(AQUI, "contenido")) if f.startswith("servicios_") and f.endswith(".py")):
    for _s in cargar(_m, "SERVICIOS", []):
        SERVICIOS[_s["slug"]] = _s
ARTICULOS = []
for _f in sorted(os.listdir(os.path.join(AQUI, "contenido"))):
    if _f.startswith("articulos") and _f.endswith(".py"):
        ARTICULOS += cargar(_f[:-3], "ARTICULOS", [])
ARTICULOS.sort(key=lambda a: a["fecha"], reverse=True)
GLOSARIO = cargar("glosario", "GLOSARIO", {})
N.GLOSARIO.update(GLOSARIO)
GUIAS = {g["slug"]: g for g in cargar("guias", "GUIAS", [])}
FAQ = cargar("faq", "FAQ", [])
LEGAL = cargar("legal", "LEGAL", {})

with open(os.path.join(AQUI, "datos", "telefonos.json"), encoding="utf-8") as f:
    TELEFONOS = json.load(f)

PAGINAS = []  # (slug, titulo_es, titulo_en, seccion) para el mapa web


def escribir(lang, slug, html):
    carpeta = RAIZ if lang == "es" else os.path.join(RAIZ, "en")
    os.makedirs(carpeta, exist_ok=True)
    with open(os.path.join(carpeta, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(html)


def registrar(slug, tes, ten, sec):
    if not any(p[0] == slug for p in PAGINAS):
        PAGINAS.append((slug, tes, ten, sec))


# ---------------------------------------------------------------- Utilidades
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]


def fecha_txt(iso, lang):
    d = date.fromisoformat(iso)
    if lang == "es":
        return f"{d.day} de {MESES[d.month - 1]} de {d.year}"
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


def cat_nombre(cat, lang):
    c = CATEGORIAS_SERVICIO[cat]
    return c[1] if lang == "es" else c[2]


def serv(slug, lang):
    return SERVICIOS[slug][lang] if slug in SERVICIOS else None


def opciones_servicio(lang):
    return [t(lang, "Golpe, abolladura o arañazo", "Dent, knock or scratch"), t(lang, "Pintura completa o parcial", "Full or partial respray"),
            t(lang, "Reparación tras accidente", "Accident repair"), t(lang, "Reparación a cargo del seguro", "Insurance repair"),
            t(lang, "Pulido, faros o tratamiento anticorrosión", "Polishing, headlights or anti-corrosion"),
            t(lang, "Revisión antes de comprar o vender", "Pre-purchase or pre-sale check"),
            t(lang, "Empresa o flota", "Business or fleet"),
            t(lang, "Coches de ocasión", "Used cars"), t(lang, "Otro", "Other")]


def seccion_form(lang, titulo, entradilla, tipo="presupuesto", sel=None):
    L = lambda es, en: t(lang, es, en)
    izq = f"""  <div>
    <h2>{esc(titulo)}</h2>
    <p class="entradilla">{md(entradilla, lang)}</p>
    <div class="btn-par" style="margin-top:18px">
  {btn_tel("btn-navy")}
  {btn_wa("btn-ghost", lang)}
</div>
    {checks_titulados([
        (L("Presupuesto por escrito", "Written estimate"), L("Antes de empezar sabes qué se va a hacer y cuánto cuesta.", "Before we start you know what will be done and what it costs.")),
        (L("Sin compromiso", "No obligation"), L("Te damos el presupuesto; decides tú.", "We give you the estimate; you decide.")),
        (L("Recogida y entrega", "Collection & delivery"), L("Si te viene mejor, pasamos a por el coche.", "If it suits you, we come and pick up the car.")),
    ], lang).replace('<ul class="checks">', '<ul class="checks" style="margin-top:26px">')}
  </div>
"""
    return seccion(f'<div class="grid g2" style="gap:44px;align-items:start">\n{izq}  {formulario(lang, tipo, sel, opciones_servicio(lang))}\n</div>', "alt")


def ventajas_cards(lang, n=6, clase="card gold"):
    orden = ["servicio-recogida-y-entrega", "servicio-garantia-vitalicia-en-pintura",
             "servicio-estado-en-tiempo-real", "servicio-vehiculo-de-sustitucion",
             "servicio-gestion-con-aseguradoras", "servicio-presupuesto-sin-compromiso",
             "servicio-limpieza-del-vehiculo"]
    out = []
    for s in orden[:n]:
        if s in SERVICIOS:
            L = SERVICIOS[s][lang]
            out.append(card_ico(SERVICIOS[s]["icon"], L["titulo"], L["corto"], lang, f"{s}.html",
                                t(lang, "Saber más", "Learn more"), clase))
    return out


# ---------------------------------------------------------------- Inicio
def pagina_inicio(lang):
    L = lambda es, en: t(lang, es, en)
    hero = f"""<div class="hero"><div class="wrap">
  <span class="eyebrow">{L("Chapa y pintura · Particulares · Empresas · Aseguradoras", "Bodywork & paint · Private · Business · Insurers")}</span>
  <h1>{L("Tu taller de chapa y pintura en el sur de Tenerife", "Your body and paint shop in the south of Tenerife")}</h1>
  <p class="lead">{md(L("Desde 2019 reparamos la [[carroceria|carrocería]] de particulares, empresas y siniestros de compañías de seguros con un servicio integral y sostenible: [[pintura-al-agua|pintura ecológica]], garantía vitalicia en pintura, recogida y entrega a domicilio e información en tiempo real.", "Since 2019 we have repaired the [[carroceria|bodywork]] of private customers, businesses and insurance claims with a complete, sustainable service: [[pintura-al-agua|eco-friendly paint]], a lifetime paint warranty, collection and delivery and real-time updates."), lang)}</p>
  <div class="actions">
    {boton("btn-primary", "pedir-cita.html", L("Pedir cita", "Book an appointment"), "calendar")}
    {boton("btn-line", "presupuesto.html", L("Presupuesto sin compromiso", "Free estimate"), "doc")}
  </div>
  <span class="respaldo">{L("Más que un simple taller", "More than just a garage")}</span>
  <div class="hero-stats">
    <div><b>{L("Desde 2019", "Since 2019")}</b><span>{L("cuidando coches en el sur de la isla", "looking after cars in the south of the island")}</span></div>
    <div><b>{val(lang)} ★</b><span>{L(f"con {E['resenas']} opiniones en Google", f"from {E['resenas']} Google reviews")}</span></div>
    <div><b>{L("De por vida", "For life")}</b><span>{L("garantía en los trabajos de pintura", "warranty on paintwork")}</span></div>
    <div><b>{L("Puerta a puerta", "Door to door")}</b><span>{L("recogida y entrega a domicilio", "collection and delivery")}</span></div>
  </div>
</div></div>
"""
    cats = [
        ("spray", "chapa-y-pintura.html", L("Chapa y pintura", "Bodywork & paint"),
         L("Golpes, abolladuras, reparación tras accidente, bancada, pintura completa o parcial, pulido y faros.", "Dents, accident repair, chassis jig, full or partial resprays, polishing and headlights."), L("Ver servicios", "See services")),
        ("users", "particulares.html", L("Particulares", "Private customers"),
         L("Tu coche reparado sin complicaciones: pagas tú o lo cubre tu seguro, y lo recogemos en casa.", "Your car repaired without hassle: you pay or your insurer does, and we collect it from home."), L("Saber más", "Learn more")),
        ("truck", "empresas-y-flotas.html", L("Empresas y flotas", "Businesses & fleets"),
         L("Flotas, furgonetas, renting y rent a car: menos tiempo parados y una imagen impecable.", "Fleets, vans, leasing and rent-a-car: less downtime and a spotless image."), L("Saber más", "Learn more")),
        ("shield", "aseguradoras.html", L("Aseguradoras", "Insurers"),
         L("Reparación de siniestros para compañías, peritos y mediadores, coordinada de principio a fin.", "Claims repairs for insurers, loss adjusters and brokers, coordinated from start to finish."), L("Saber más", "Learn more")),
    ]
    s1 = seccion(section_head(L("¿Qué necesita tu coche?", "What does your car need?"),
                              L("Reparamos la carrocería de particulares, empresas y siniestros de compañías de seguros. Entra en cada apartado para ver cómo trabajamos.", "We repair bodywork for private customers, businesses and insurance claims. Open each section to see how we work."), lang)
                 + grid("g4", [card_ico(i, a, b, lang, h, m) for i, h, a, b, m in cats]))
    s1b = seccion(f"""  <div class="grid g2" style="align-items:center;gap:40px">
    <div>
      <span class="eyebrow-dark">{L("¿Vas a comprar o vender un coche?", "Buying or selling a car?")}</span>
      <h2>{L("Revisión de carrocería antes de la compraventa", "Bodywork check before you buy or sell")}</h2>
      <p style="color:var(--muted);font-size:17px">{md(L("Revisamos carrocería, pintura, estructura y documentación del coche que te interesa, o del que quieres vender, y te entregamos un informe con fotos. Con un [[medidor-de-espesores|medidor de espesores]] sabemos qué piezas se han repintado.", "We check the bodywork, paint, structure and paperwork of the car you're interested in, or the one you want to sell, and give you a report with photos. With a [[medidor-de-espesores|paint thickness gauge]] we can tell which panels have been resprayed."), lang)}</p>
      <div class="actions" style="display:flex;gap:12px;flex-wrap:wrap">
        {boton("btn-navy", "revision-compraventa.html", L("Ver la revisión", "See the inspection"), "search")}
        {boton("btn-ghost", "revision-antes-de-comprar.html", L("Antes de comprar", "Before buying"))}
      </div>
    </div>
    {checks_titulados([
        (L("Antes de comprar", "Before buying"), L("Descubre golpes y repintados antes de pagar.", "Uncover crash damage and resprays before you pay.")),
        (L("Antes de vender", "Before selling"), L("Un informe que da confianza al comprador.", "A report that gives the buyer confidence.")),
        (L("Puesta a punto estética", "Cosmetic refresh"), L("Pulido, faros y pequeños golpes, sin ocultar nada.", "Polishing, headlights and small dents, hiding nothing.")),
        (L("Informe con fotos", "Report with photos"), L("Y te lo explicamos en persona.", "And we explain it in person.")),
    ], lang)}
  </div>
""", "alt")
    s2 = bloque_aseguradora(lang)
    s3 = seccion(section_head(L("Ventajas Green Car", "The Green Car advantage"),
                              L("Lo que nos diferencia de un taller convencional y lo que más valoran nuestros clientes.", "What sets us apart from a conventional garage, and what our customers value most."), lang)
                 + grid("g3", ventajas_cards(lang, 6)), "alt")
    s4 = seccion(f"""  <div class="grid g2" style="align-items:center;gap:40px">
    <div>
      <span class="eyebrow-dark">{L("¿Has tenido un accidente?", "Had an accident?")}</span>
      <h2>{L("Te ayudamos desde el primer momento", "We help you from the very first moment")}</h2>
      <p style="color:var(--muted);font-size:17px">{md(L("Qué hacer en el lugar del accidente, cómo rellenar el [[parte-amistoso|parte amistoso]], a quién llamar y cómo funciona la [[peritacion|peritación]]. Y cuando el coche tenga que pasar por el taller, nos encargamos de la gestión con tu aseguradora.", "What to do at the scene, how to fill in the [[parte-amistoso|accident report form]], who to call and how the [[peritacion|loss assessment]] works. And when the car needs repairing, we handle things with your insurer."), lang)}</p>
      <div class="actions" style="display:flex;gap:12px;flex-wrap:wrap">
        {boton("btn-navy", "siniestros.html", L("Guía de siniestros", "Accident guide"), "alert")}
        {boton("btn-ghost", "telefonos-de-asistencia.html", L("Teléfonos de asistencia", "Assistance numbers"))}
      </div>
    </div>
    {checks_titulados([
        (L("Qué hacer tras un accidente", "What to do after an accident"), L("Los primeros pasos, en orden.", "The first steps, in order.")),
        (L("El parte amistoso", "The accident report form"), L("Casilla a casilla, sin errores.", "Box by box, without mistakes.")),
        (L("Libre elección de taller", "Free choice of garage"), L("Tus derechos frente a la aseguradora.", "Your rights with your insurer.")),
        (L("Teléfonos de asistencia", "Assistance numbers"), L("Grúa y asistencia en carretera de las principales compañías.", "Towing and roadside assistance from the main insurers.")),
    ], lang)}
  </div>
""")
    # Opiniones
    s5 = seccion(section_head(L("Lo que dicen nuestros clientes", "What our customers say"),
                              L(f"Una valoración media de {val(lang)} sobre 5 con {E['resenas']} opiniones en Google. Esto es lo que más se repite.", f"An average rating of {val(lang)} out of 5 from {E['resenas']} Google reviews. This is what comes up most."), lang)
                 + grid("g3", destacados(lang)) + f'  <div style="margin-top:26px">{boton("btn-ghost", "opiniones.html", L("Ver opiniones", "See reviews"))}</div>\n'.replace("</a>", f" {ico('arrow')}</a>"), "alt")
    # Blog
    ult = [card_prod(a[lang]["titulo"], a[lang]["resumen"], f"{a['slug']}.html", L("Leer", "Read"), lang,
                     CATEGORIAS_BLOG[a["cat"]][0 if lang == "es" else 1]) for a in ARTICULOS[:6]]
    s6 = seccion(section_head(L("Lo último en nuestro Blog", "Latest from our Blog"),
                              L("Consejos prácticos para cuidar tu coche, entender la reparación y saber qué hacer si tienes un percance.", "Practical tips to look after your car, understand repairs and know what to do if something happens."), lang)
                 + grid("g3-blog", ult) + f'  <div style="margin-top:26px">{boton("btn-ghost", "blog.html", L("Ver todo el blog", "See the whole blog"))}</div>\n'.replace("</a>", f" {ico('arrow')}</a>")) if ult else ""
    s7 = seccion(f"""  <div class="grid g2" style="align-items:center;gap:40px">
    <div>
      <span class="eyebrow-dark">{L("También vendemos coches", "We also sell cars")}</span>
      <h2>{L("Coches de ocasión en Tenerife", "Used cars in Tenerife")}</h2>
      <p style="color:var(--muted);font-size:17px">{L("Turismos, SUV y pick-up de segunda mano que puedes ver en el taller, con toda la información antes de decidir y un taller de confianza para después.", "Second-hand cars, SUVs and pick-ups you can see at the workshop, with all the information before you decide and a trusted garage afterwards.")}</p>
      <div class="actions" style="display:flex;gap:12px;flex-wrap:wrap">{boton("btn-navy", "coches-de-ocasion.html", L("Ver coches de ocasión", "See used cars"), "car")}{boton("btn-ghost", "guia-comprar-coche-de-ocasion.html", L("Guía para comprar", "Buying guide"))}</div>
    </div>
    {checks_titulados([
        (L("Los ves en persona", "See them in person"), L("En nuestras instalaciones de Las Chafiras.", "At our premises in Las Chafiras.")),
        (L("Pregunta lo que quieras", "Ask anything"), L("Historial, estado y documentación antes de comprar.", "History, condition and paperwork before you buy.")),
        (L("Revisión de carrocería", "Bodywork check"), L("Si el coche no es nuestro, también te lo revisamos.", "If the car isn't ours, we'll check it for you too.")),
    ], lang)}
  </div>
""", "alt")
    cuerpo = hero + s1 + s1b + s2.replace('<section class="alt">', '<section>') + s3 + s4 + s5 + s6 + s7 + mitos(lang, "") + panel(
        lang, L("¿Le echamos un vistazo a tu coche?", "Shall we take a look at your car?"),
        L("Pide cita o presupuesto sin compromiso. Si te viene mejor, pasamos a recogerlo.", "Book an appointment or ask for a free estimate. If it suits you, we'll come and collect it."))
    return documento(lang, "index", L("Green Car Service Tenerife | Taller de chapa y pintura en Las Chafiras", "Green Car Service Tenerife | Body & paint shop in Las Chafiras"),
                     L("Taller de chapa y pintura en Las Chafiras (sur de Tenerife) para particulares, empresas y aseguradoras. Pintura ecológica, garantía vitalicia en pintura, recogida y entrega y revisión antes de comprar o vender.", "Body and paint shop in Las Chafiras (south Tenerife) for private customers, businesses and insurers. Eco-friendly paint, lifetime paint warranty, collection and delivery, and pre-purchase checks."),
                     cuerpo, "index")


def destacados(lang):
    L = lambda es, en: t(lang, es, en)
    D = [
        (L("El coche, como nuevo", "The car looks like new"),
         L("Clientes que recomiendan el taller de chapa y pintura porque el coche vuelve impecable, y además limpio por dentro.", "Customers recommend the body and paint shop because the car comes back spotless, and clean inside too.")),
        (L("Trato de principio a fin", "Great service from start to finish"),
         L("El trato del equipo durante toda la reparación y la sensación de haber encontrado un taller de confianza.", "How the team treats you throughout the repair, and the feeling of having found a garage you can trust.")),
        (L("Rapidez y facilidades", "Speed and flexibility"),
         L("Presupuestos rápidos, ajuste de agenda para dar cita y vehículo de sustitución cuando hace falta.", "Quick estimates, fitting appointments into the schedule and a courtesy car when it's needed.")),
    ]
    return [f'<div class="destaca">{estrellas()}<h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for a, b in D]


# ---------------------------------------------------------------- Empresa
def pagina_conocenos(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [], L("Conócenos", "About us"),
                       L("Green Car Service Tenerife empezó su andadura en 2019 con un propósito firme: ganarse la confianza de quienes buscan algo más que un simple taller.", "Green Car Service Tenerife started out in 2019 with a clear purpose: to earn the trust of people looking for more than just a garage."))
    cuerpo += seccion(f"""  <div class="grid g2" style="gap:44px;align-items:center">
    <div>
      <h2>{L("Un taller integral y sostenible", "A complete, sustainable workshop")}</h2>
      <p style="color:var(--muted);font-size:18px">{L("Chapa y pintura bajo el mismo techo, en Las Chafiras.", "Bodywork and paint under one roof, in Las Chafiras.")}</p>
      <p style="color:var(--muted)">{md(L("Nacimos con el objetivo de ofrecer un servicio integral: que puedas dejar el coche en un solo sitio, sea un roce, un golpe o un accidente, y recuperarlo reparado, limpio y con todas las explicaciones. Y hacerlo de forma sostenible, con [[pintura-al-agua|pintura ecológica]] y procesos que cuidan el entorno.", "We were set up to offer a complete service: you leave your car in one place, whether it's a scrape, a dent or an accident, and get it back repaired, clean and fully explained. And to do it sustainably, with [[pintura-al-agua|eco-friendly paint]] and processes that respect the environment."), lang)}</p>
    </div>
    <div class="hero-stats" style="margin-top:0">
      <div class="card"><b style="font-size:26px;color:var(--green-dark)">2019</b><br><span style="color:var(--muted)">{L("año en que abrimos", "the year we opened")}</span></div>
      <div class="card"><b style="font-size:26px;color:var(--green-dark)">{val(lang)} ★</b><br><span style="color:var(--muted)">{L(f"{E['resenas']} opiniones en Google", f"{E['resenas']} Google reviews")}</span></div>
      <div class="card"><b style="font-size:26px;color:var(--green-dark)">3</b><br><span style="color:var(--muted)">{L("tipos de cliente: particulares, empresas y aseguradoras", "kinds of customer: private, business and insurers")}</span></div>
      <div class="card"><b style="font-size:26px;color:var(--green-dark)">{L("Eco", "Eco")}</b><br><span style="color:var(--muted)">{L("pintura con beneficios para el medio ambiente", "paint with environmental benefits")}</span></div>
    </div>
  </div>
""", "alt")
    cuerpo += seccion(section_head(L("Nuestros tres pilares", "Our three pillars"),
                                   L("Nuestro compromiso con el medio ambiente se conjuga con la calidad, la confianza y el compromiso, que son los tres pilares sobre los que se basa nuestra estructura.", "Our commitment to the environment goes hand in hand with quality, trust and commitment: the three pillars our business is built on."), lang)
                      + grid("g3", [
                          card_ico("award", L("Calidad", "Quality"), L("Instalaciones y equipos para trabajar con los estándares que exige cada marca: bancadas, taller de chapa y área de pintura.", "Premises and equipment to work to each manufacturer's standards: chassis jigs, a body shop and a paint area."), lang),
                          card_ico("handshake", L("Confianza", "Trust"), L("Presupuesto claro antes de empezar, información en tiempo real durante la reparación y explicaciones al entregar el coche.", "A clear estimate before we start, real-time updates during the repair and explanations when you collect your car."), lang),
                          card_ico("leaf", L("Compromiso", "Commitment"), L("Con cada cliente y con el entorno: pintura ecológica, reparación antes que sustitución cuando es posible y gestión responsable de residuos.", "With each customer and with the environment: eco-friendly paint, repairing rather than replacing where possible, and responsible waste handling."), lang),
                      ]))
    cuerpo += seccion(section_head(L("Por qué elegirnos", "Why choose us"), "", lang) + grid("g3", ventajas_cards(lang, 6)), "alt")
    cuerpo += seccion(grid("g3", [
        card_ico("tool", L("Nuestras instalaciones", "Our premises"), L("Taller de chapa, pintura, bancadas y almacén de recambios en el polígono Llano del Camello.", "Body shop, paint shop, chassis jigs and parts store on the Llano del Camello industrial estate."), lang, "instalaciones.html"),
        card_ico("leaf", L("Sostenibilidad", "Sustainability"), L("Cómo reducimos el impacto ambiental de cada reparación.", "How we reduce the environmental impact of every repair."), lang, "sostenibilidad.html"),
        card_ico("star", L("Opiniones", "Reviews"), L(f"{val(lang)} sobre 5 con {E['resenas']} opiniones de clientes en Google.", f"{val(lang)} out of 5 from {E['resenas']} customer reviews on Google."), lang, "opiniones.html"),
    ]))
    cuerpo += panel(lang, L("¿Nos conocemos en persona?", "Shall we meet in person?"),
                    L("Ven a vernos a Las Chafiras o pide cita y nos cuentas qué necesita tu coche.", "Come and see us in Las Chafiras, or book an appointment and tell us what your car needs."))
    return documento(lang, "conocenos", L("Conócenos", "About us"),
                     L("Green Car Service Tenerife: taller de chapa y pintura en Las Chafiras desde 2019. Calidad, confianza y compromiso.", "Green Car Service Tenerife: body and paint shop in Las Chafiras since 2019. Quality, trust and commitment."),
                     cuerpo, "conocenos")


def mapa_iframe(lang, alto=320):
    q = "Green+Car+Service+Tenerife,+Av.+7+Islas+Canarias+34,+38639+Las+Chafiras"
    return f"""<div style="border-radius:12px;overflow:hidden;border:1px solid var(--line)">
      <iframe title="{t(lang, "Mapa del taller", "Map of the workshop")}" width="100%" height="{alto}" style="border:0;display:block" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        src="https://www.google.com/maps?q={q}&amp;output=embed"></iframe>
    </div>"""


def pagina_instalaciones(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [(L("Conócenos", "About us"), "conocenos.html")], L("Instalaciones", "Our premises"),
                       L("Amplias instalaciones en el polígono industrial Llano del Camello, en Las Chafiras, con todo lo necesario para reparar tu coche en un solo sitio.", "Spacious premises on the Llano del Camello industrial estate in Las Chafiras, with everything needed to repair your car in one place."))
    cuerpo += seccion(section_head(L("Qué encontrarás en el taller", "What you'll find at the workshop"), "", lang) + grid("g3", [
        card_ico("hammer", L("Taller de chapa", "Body shop"), md(L("Zona de reparación de [[carroceria|carrocería]] para golpes, abolladuras y daños por accidente.", "Area for [[carroceria|bodywork]] repairs: dents, knocks and accident damage."), lang).replace('<a', '<span').replace('</a>', '</span>') and L("Zona de reparación de carrocería para golpes, abolladuras y daños por accidente.", "Area for bodywork repairs: dents, knocks and accident damage."), lang),
        card_ico("spray", L("Taller de pintura", "Paint shop"), L("Preparación y pintado con pintura ecológica, en colores sólidos y metalizados.", "Preparation and painting with eco-friendly paint, in solid and metallic colours."), lang),
        card_ico("layers", L("Bancadas", "Chassis jigs"), L("Bancadas y equipamiento para devolver la estructura del vehículo a las medidas que exige cada marca.", "Chassis jigs and equipment to bring the vehicle's structure back to each manufacturer's measurements."), lang),
        card_ico("tool", L("Almacén de recambios", "Parts store"), L("Almacén propio de recambios para agilizar las reparaciones.", "Our own parts store to speed up repairs."), lang),
        card_ico("truck", L("Recogida y entrega", "Collection & delivery"), L("Si no puedes acercarte, pasamos a por el coche y te lo devolvemos reparado.", "If you can't come in, we pick up the car and bring it back repaired."), lang, "servicio-recogida-y-entrega.html"),
    ]))
    cuerpo += seccion(f"""  <div class="grid g2" style="gap:44px;align-items:start">
    <div>
      <h2>{L("Cómo llegar", "How to find us")}</h2>
      <ul class="info-list" style="margin-bottom:24px">
        <li><span class="ico">{ico("pin")}</span><div><b>{L("Dirección", "Address")}</b><span>{esc(E["direccion"])}<br>{esc(E["cp_ciudad"])}</span></div></li>
        <li><span class="ico">{ico("road")}</span><div><b>{L("Acceso", "Access")}</b><span>{L("En el polígono industrial de Las Chafiras (San Miguel de Abona), con acceso rápido desde la autopista TF-1.", "On the Las Chafiras industrial estate (San Miguel de Abona), with quick access from the TF-1 motorway.")}</span></div></li>
        <li><span class="ico">{ico("clock")}</span><div><b>{L("Horario", "Opening hours")}</b><span>{L("Lunes a viernes, de 07:00 a 16:00", "Monday to Friday, 07:00 to 16:00")}</span></div></li>
        <li><span class="ico">{ico("truck")}</span><div><b>{L("¿No puedes venir?", "Can't come in?")}</b><span><a href="servicio-recogida-y-entrega.html">{L("Recogemos y entregamos tu coche a domicilio", "We collect and deliver your car")}</a></span></div></li>
      </ul>
    </div>
    {mapa_iframe(lang)}
  </div>
""", "alt")
    cuerpo += panel(lang, L("Ven a vernos", "Come and see us"), L("Te enseñamos el taller y valoramos tu coche sin compromiso.", "We'll show you around and assess your car with no obligation."))
    return documento(lang, "instalaciones", L("Instalaciones", "Our premises"),
                     L("Instalaciones de Green Car Service Tenerife en Las Chafiras: taller de chapa, pintura, bancadas y almacén de recambios.", "Green Car Service Tenerife premises in Las Chafiras: body shop, paint shop, chassis jigs and parts store."),
                     cuerpo, "conocenos")


def pagina_sostenibilidad(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [(L("Conócenos", "About us"), "conocenos.html")], L("Sostenibilidad", "Sustainability"),
                       L("El «green» de nuestro nombre no es decoración: desarrollar la actividad de forma sostenible forma parte de cómo trabajamos desde el primer día.", "The “green” in our name isn't just decoration: running our business sustainably has been part of how we work from day one."))
    cuerpo += seccion(section_head(L("Cómo lo llevamos a la práctica", "How we put it into practice"), "", lang) + grid("g2", [
        card_ico("leaf", L("Pintura ecológica eco-balance", "Eco-balance eco-friendly paint"), md(L("Usamos una pintura ecológica con beneficios directos para el medio ambiente, con menos [[compuestos-organicos-volatiles|compuestos orgánicos volátiles]] que las pinturas tradicionales al disolvente.", "We use an eco-friendly paint with direct environmental benefits and fewer [[compuestos-organicos-volatiles|volatile organic compounds]] than traditional solvent-based paints."), lang), lang),
        card_ico("hammer", L("Reparar antes que sustituir", "Repair rather than replace"), L("Cuando una pieza se puede reparar con garantías, la reparamos. Se ahorra material, transporte y residuos.", "When a part can be reliably repaired, we repair it. That saves material, transport and waste."), lang),
        card_ico("recycle", L("Residuos bien gestionados", "Waste handled properly"), L("Restos de pintura, disolventes, abrasivos, plásticos y envases necesitan un tratamiento específico. Los separamos y los entregamos a gestores autorizados.", "Paint residue, solvents, abrasives, plastics and containers need specific treatment. We separate them and hand them to authorised waste managers."), lang),
        card_ico("sparkle", L("Recuperar antes que repintar", "Restore before respraying"), L("Un pulido bien hecho o una restauración de faros alargan la vida de la pintura y de las piezas sin tener que sustituirlas.", "A proper polish or headlight restoration extends the life of paint and parts without replacing them."), lang, "servicio-pulido-y-abrillantado.html"),
    ]))
    cuerpo += seccion(f"""  <div class="texto-largo">
    <h2>{L("Una carrocería cuidada dura más", "Well-kept bodywork lasts longer")}</h2>
    <p>{md(L("La forma más sostenible de reparar es no tener que sustituir. Tratar a tiempo un arañazo que deja la chapa al aire evita que la [[corrosion|corrosión]] avance; proteger las zonas reparadas con [[cera-de-cavidades|cera de cavidades]] y [[antigravilla|antigravilla]] evita volver a abrirlas; y pulir un barniz castigado por el sol puede ahorrar un repintado.", "The most sustainable repair is the one that avoids replacing parts. Dealing promptly with a scratch that leaves bare metal stops [[corrosion|corrosion]] spreading; protecting repaired areas with [[cera-de-cavidades|cavity wax]] and [[antigravilla|stone-chip coating]] means they don't have to be reopened; and polishing sun-damaged clear coat can save a respray."), lang)}</p>
    {checks_simples([L("Te explicamos qué conviene reparar y qué puede esperar.", "We explain what should be repaired and what can wait."), L("Reparamos piezas cuando se puede hacer con garantías.", "We repair parts when it can be done reliably."), L("Te devolvemos las piezas sustituidas si las quieres ver.", "We give you back replaced parts if you want to see them.")], lang)}
  </div>
""", "alt")
    cuerpo += panel(lang, L("¿Reparamos tu coche de forma sostenible?", "Shall we repair your car sustainably?"), L("Pide presupuesto sin compromiso.", "Ask for a free estimate."), ("presupuesto.html", L("Pedir presupuesto", "Get an estimate")))
    return documento(lang, "sostenibilidad", L("Sostenibilidad", "Sustainability"),
                     L("Pintura ecológica, reparar antes que sustituir y gestión responsable de residuos: el compromiso medioambiental de Green Car Service Tenerife.", "Eco-friendly paint, repair before replacement and responsible waste handling: Green Car Service Tenerife's environmental commitment."),
                     cuerpo, "conocenos")


def pagina_opiniones(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [(L("Conócenos", "About us"), "conocenos.html")], L("Opiniones de clientes", "Customer reviews"),
                       L("Lo que dicen de nosotros quienes ya han dejado su coche en el taller.", "What people who have already brought their car to us say."))
    gmaps = "https://www.google.com/maps/search/?api=1&query=Green+Car+Service+Tenerife+Las+Chafiras"
    cuerpo += seccion(f"""  <div class="valoracion">
    <div class="cifra">{val(lang)}</div>
    <div>{estrellas()}<p>{L(f"Valoración media sobre 5 con {E['resenas']} opiniones en Google.", f"Average rating out of 5 from {E['resenas']} Google reviews.")}</p></div>
    <div style="margin-left:auto">{boton("btn-ghost", gmaps, L("Leer todas en Google", "Read them all on Google"), None, True)}</div>
  </div>
{section_head(L("Lo que más destacan", "What they highlight most"), L("Un resumen de lo que más se repite en las opiniones publicadas.", "A summary of what comes up most in published reviews."), lang)}{grid("g3", destacados(lang))}""")
    cuerpo += seccion(section_head(L("¿Ya eres cliente?", "Already a customer?"), L("Tu opinión nos ayuda a mejorar y ayuda a otros conductores a encontrar un taller de confianza. Si te hemos reparado el coche, cuéntanos qué tal en Google.", "Your review helps us improve and helps other drivers find a garage they can trust. If we've repaired your car, tell us how it went on Google."), lang)
                      + f'  <div class="actions" style="display:flex;gap:12px;flex-wrap:wrap">{boton("btn-primary", gmaps, L("Dejar una opinión", "Leave a review"), "star", True)}</div>\n', "alt")
    cuerpo += panel(lang, L("¿Quieres comprobarlo tú?", "Want to see for yourself?"), L("Pide cita y juzga por ti mismo.", "Book an appointment and judge for yourself."))
    return documento(lang, "opiniones", L("Opiniones de clientes", "Customer reviews"),
                     L(f"Green Car Service Tenerife tiene una valoración de {val(lang)} sobre 5 con {E['resenas']} opiniones en Google.", f"Green Car Service Tenerife is rated {val(lang)} out of 5 from {E['resenas']} Google reviews."),
                     cuerpo, "conocenos")


# ---------------------------------------------------------------- Servicios
def pagina_servicios(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [], L("Servicios", "Services"),
                       L("Chapa, pintura, revisión para compraventa y todas nuestras ventajas, para particulares, empresas y aseguradoras.", "Bodywork, paint, pre-sale and pre-purchase checks and all our advantages, for private customers, businesses and insurers."))
    for i, (cat, (hub, nes, nen)) in enumerate(CATEGORIAS_SERVICIO.items()):
        tarjetas = [card_prod(serv(s, lang)["titulo"], serv(s, lang)["corto"], f"{s}.html", L("Ver servicio", "See service"), lang)
                    for s in SERVICIOS_SLUGS[cat] if s in SERVICIOS]
        nombre = nes if lang == "es" else nen
        cuerpo += seccion(f'  <div class="section-head" id="{cat}"><h2>{esc(nombre)}</h2><p>{md(INTRO_CAT[cat][lang], lang)}</p></div>\n'
                          + grid("g3", tarjetas)
                          + f'  <div style="margin-top:22px">{boton("btn-ghost", hub, L("Ver la sección", "See the section"))}</div>\n'.replace("</a>", f" {ico('arrow')}</a>"),
                          "alt" if i % 2 else "")
    cuerpo += panel(lang, L("¿No encuentras lo que buscas?", "Can't find what you're looking for?"), L("Llámanos o escríbenos y te decimos si podemos ayudarte.", "Call or message us and we'll tell you if we can help."))
    return documento(lang, "servicios", L("Servicios", "Services"),
                     L("Todos los servicios de Green Car Service Tenerife: chapa y pintura, revisión antes de comprar o vender, particulares, empresas y aseguradoras.", "All Green Car Service Tenerife services: bodywork and paint, pre-purchase and pre-sale checks, private customers, businesses and insurers."),
                     cuerpo, "servicios")


INTRO_CAT = {
    "chapa-pintura": {"es": "Desde un roce en el paragolpes hasta la reparación de un accidente con [[bancada|bancada]], con [[pintura-al-agua|pintura ecológica]] y garantía vitalicia en pintura.",
                      "en": "From a scuffed bumper to accident repair on a [[bancada|chassis jig]], with [[pintura-al-agua|eco-friendly paint]] and a lifetime paint warranty."},
    "revision": {"es": "Antes de comprar o vender un coche, revisamos su carrocería, su pintura con [[medidor-de-espesores|medidor de espesores]], su estructura y su documentación, y te entregamos un informe con fotos.",
                 "en": "Before you buy or sell a car, we check its bodywork, its paint with a [[medidor-de-espesores|paint thickness gauge]], its structure and its paperwork, and give you a report with photos."},
    "clientes": {"es": "Reparamos la carrocería de particulares, de empresas con [[flota|flotas]] y vehículos comerciales, y de los [[siniestro|siniestros]] que nos confían las compañías de seguros.",
                 "en": "We repair bodywork for private customers, for businesses with [[flota|fleets]] and commercial vehicles, and for the [[siniestro|claims]] insurers entrust to us."},
    "ventajas": {"es": "Lo que hace distinto a nuestro taller: recogida y entrega, garantía vitalicia en pintura, información en tiempo real y gestión con tu aseguradora.",
                 "en": "What makes our garage different: collection and delivery, a lifetime paint warranty, real-time updates and handling your insurer for you."},
}

HUB_TIT = {
    "chapa-pintura": ("Chapa y pintura", "Bodywork & paint"),
    "revision": ("Revisión para compraventa", "Pre-purchase & pre-sale inspection"),
    "clientes": ("A quién damos servicio", "Who we work for"),
    "ventajas": ("Ventajas Green Car", "The Green Car advantage"),
}
TIT_LISTA = {
    "chapa-pintura": ("Todos los servicios de chapa y pintura", "All bodywork and paint services"),
    "revision": ("Revisión para comprar y para vender", "Checks for buying and for selling"),
    "clientes": ("Particulares, empresas y aseguradoras", "Private customers, businesses and insurers"),
    "ventajas": ("Todas nuestras ventajas", "All our advantages"),
}
TIT_OTROS = {
    "chapa-pintura": ("Otros servicios de chapa y pintura", "Other bodywork and paint services"),
    "revision": ("Más sobre la revisión para compraventa", "More on pre-purchase and pre-sale checks"),
    "clientes": ("También trabajamos para", "We also work for"),
    "ventajas": ("Otras ventajas Green Car", "More Green Car advantages"),
}
HUB_NAV = {"chapa-pintura": "chapa-y-pintura", "revision": "revision-compraventa", "clientes": "servicios",
           "ventajas": "servicios"}


def pagina_hub(cat, lang):
    L = lambda es, en: t(lang, es, en)
    hub = CATEGORIAS_SERVICIO[cat][0][:-5]
    titulo = HUB_TIT[cat][0 if lang == "es" else 1]
    cuerpo = page_head(lang, [(L("Servicios", "Services"), "servicios.html")], titulo, INTRO_CAT[cat][lang],
                       f'\n  <div class="actions">{boton("btn-primary", "pedir-cita.html", L("Pedir cita", "Book an appointment"), "calendar")}{boton("btn-line", "presupuesto.html", L("Presupuesto", "Estimate"), "doc")}</div>')
    tarjetas = [card_prod(serv(s, lang)["titulo"], serv(s, lang)["corto"], f"{s}.html", L("Ver servicio", "See service"), lang)
                for s in SERVICIOS_SLUGS[cat] if s in SERVICIOS]
    cuerpo += seccion(section_head(TIT_LISTA[cat][0 if lang == "es" else 1],
                                   L("Entra en cada servicio para ver en detalle qué hacemos y cómo trabajamos. Cuando lo tengas claro, pide cita o presupuesto.", "Open each service to see what we do and how we work. When you're ready, book an appointment or ask for an estimate."), lang)
                      + grid("g3", tarjetas))
    if cat in ("chapa-pintura", "clientes"):
        cuerpo += bloque_aseguradora(lang)
    if cat != "ventajas":
        cuerpo += seccion(section_head(L("Ventajas Green Car", "The Green Car advantage"), "", lang) + grid("g3", ventajas_cards(lang, 3)),
                          "" if cat in ("chapa-pintura", "clientes") else "alt")
    cuerpo += mitos(lang, "alt" if cat in ("chapa-pintura", "clientes") else "")
    cuerpo += panel(lang, L("¿Le echamos un vistazo?", "Shall we take a look?"), L("Pide cita o presupuesto sin compromiso.", "Book an appointment or ask for a free estimate."))
    return documento(lang, hub, titulo, plano(INTRO_CAT[cat][lang]), cuerpo, HUB_NAV[cat])


def pagina_servicio(s, lang):
    S = SERVICIOS[s]
    C = S[lang]
    L = lambda es, en: t(lang, es, en)
    cat = S["cat"]
    hub = CATEGORIAS_SERVICIO[cat][0]
    cuerpo = page_head(lang, [(L("Servicios", "Services"), "servicios.html"), (cat_nombre(cat, lang), hub)], C["titulo"], C["entradilla"])
    cuerpo += seccion(section_head(C["por_que_titulo"], "", lang)
                      + grid("g3", [card_ico(i, a, b, lang) for i, a, b in C["por_que"]]))
    cuerpo += seccion(section_head(C["incluye_titulo"], C["incluye_intro"], lang)
                      + grid("g3", [card_ico(i, a, b, lang, clase="card cob") for i, a, b in C["incluye"]])
                      + f'  <div class="note" style="margin-top:26px"><p>{md(C["nota"], lang)}</p></div>\n', "alt")
    cuerpo += seccion(f'<div class="texto-largo">{bloques(C["texto"], lang)}</div>\n')
    cuerpo += seccion(section_head(L("Preguntas frecuentes", "Frequently asked questions"), "", lang) + faq_html(C["faq"], lang), "alt")
    if cat in ("chapa-pintura", "clientes"):
        cuerpo += bloque_aseguradora(lang).replace('<section class="alt">', "<section>")
    otros = [x for x in SERVICIOS_SLUGS[cat] if x != s and x in SERVICIOS]
    tarjetas = [card_prod(serv(x, lang)["titulo"], serv(x, lang)["corto"], f"{x}.html", L("Ver servicio", "See service"), lang) for x in otros[:6]]
    cuerpo += seccion(section_head(TIT_OTROS[cat][0 if lang == "es" else 1], "", lang)
                      + grid("g3", tarjetas)
                      + f"""  <div class="pie-seccion">
    {boton("btn-ghost", hub, L("Ver todos", "See all"))}
    {compartir(lang)}
  </div>
""".replace("</a>\n    <div", f" {ico('arrow')}</a>\n    <div", 1), "alt" if cat == "ventajas" else "")
    cuerpo += mitos(lang, "alt" if cat != "ventajas" else "")
    cuerpo += seccion_form(lang, L(f"¿Te preparamos un presupuesto?", "Shall we prepare an estimate?"),
                           L("Cuéntanos qué necesita tu coche y te respondemos con un presupuesto por escrito, sin compromiso.", "Tell us what your car needs and we'll reply with a written estimate, with no obligation."))
    return documento(lang, s, C["titulo"], C["entradilla"], cuerpo, s if cat == "clientes" else HUB_NAV[cat])


# ---------------------------------------------------------------- Siniestros
def pagina_siniestros(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [], L("Siniestros y accidentes", "Accidents & claims"),
                       L("Qué hacer si tienes un accidente o un golpe, cómo funciona la reparación a cargo del seguro y a quién llamar.", "What to do if you have an accident or a knock, how insurance repairs work and who to call."))
    cuerpo += seccion(f"""  <div class="panel" style="margin-bottom:34px">
    <h2>{L("¿Tu coche necesita reparación tras un siniestro?", "Does your car need repairing after an incident?")}</h2>
    <p>{md(L("Llámanos. Te decimos cómo dar el parte, nos coordinamos con tu aseguradora y con el [[perito|perito]] y, si lo necesitas, recogemos el coche.", "Call us. We'll tell you how to report it, coordinate with your insurer and the [[perito|loss adjuster]] and, if you need it, collect the car."), lang).replace('class="dic"', 'class="dic" style="color:#fff"')}</p>
    <div class="actions">{btn_tel("btn-navy")}{btn_wa("btn-line", lang, True)}{boton("btn-primary", "presupuesto.html", L("Pedir presupuesto", "Get an estimate"), "doc")}</div>
  </div>
""" + section_head(L("Guías prácticas", "Practical guides"), L("Todo lo que conviene saber, explicado paso a paso.", "Everything you need to know, explained step by step."), lang)
                      + grid("g3", [card_ico(GUIAS[g]["icon"], GUIAS[g][lang]["titulo"], GUIAS[g][lang]["corto"], lang, f"{g}.html", L("Leer la guía", "Read the guide"))
                                    for g in GUIAS_SLUGS if g in GUIAS and g != "guia-comprar-coche-de-ocasion"]
                             + [card_ico("phone", L("Teléfonos de asistencia", "Assistance numbers"), L("Grúa y asistencia en carretera de las principales aseguradoras.", "Towing and roadside assistance from the main insurers."), lang, "telefonos-de-asistencia.html", L("Ver teléfonos", "See numbers"))]))
    cuerpo += seccion(f"""  <div class="grid g2" style="align-items:start;gap:44px">
    <div>
      <h2>{L("En el lugar del accidente", "At the scene of the accident")}</h2>
      <p style="color:var(--muted)">{L("Lo más importante es la seguridad. Después, la documentación.", "Safety comes first. Paperwork comes second.")}</p>
      {boton("btn-ghost", "guia-que-hacer-tras-un-accidente.html", L("Guía completa", "Full guide")).replace("</a>", f" {ico('arrow')}</a>")}
    </div>
    <ol class="pasos">
      <li><b>{L("Protégete", "Stay safe")}</b><span>{L("Chaleco reflectante, señaliza el vehículo y apártate de la calzada.", "Hi-vis vest, signal the vehicle and get off the road.")}</span></li>
      <li><b>{L("Si hay heridos, 112", "If anyone is hurt, 112")}</b><span>{L("No muevas a los heridos salvo peligro inminente.", "Don't move injured people unless they are in immediate danger.")}</span></li>
      <li><b>{L("Parte y fotos", "Report form and photos")}</b><span>{md(L("Rellena el [[parte-amistoso|parte amistoso]] y fotografía daños, matrículas y posición.", "Fill in the [[parte-amistoso|accident report form]] and photograph damage, plates and positions."), lang)}</span></li>
      <li><b>{L("Avisa y llámanos", "Report it and call us")}</b><span>{L("Comunica el siniestro a tu aseguradora y cuéntanos qué ha pasado.", "Notify your insurer and tell us what happened.")}</span></li>
    </ol>
  </div>
""", "alt")
    cuerpo += bloque_aseguradora(lang).replace('<section class="alt">', "<section>")
    cuerpo += panel(lang, L("¿Hablamos de tu siniestro?", "Shall we talk about your claim?"), L("Te orientamos sin compromiso.", "We'll advise you with no obligation."), ("presupuesto.html", L("Pedir presupuesto", "Get an estimate")))
    return documento(lang, "siniestros", L("Siniestros y accidentes", "Accidents & claims"),
                     L("Qué hacer tras un accidente, parte amistoso, libre elección de taller, peritación y teléfonos de asistencia. Green Car Service Tenerife trabaja con tu aseguradora.", "What to do after an accident, accident report form, free choice of garage, loss assessment and assistance numbers. Green Car Service Tenerife works with your insurer."),
                     cuerpo, "siniestros")


def pagina_guia(g, lang):
    G = GUIAS[g]
    C = G[lang]
    L = lambda es, en: t(lang, es, en)
    if g == "guia-comprar-coche-de-ocasion":
        migas, nav = [(L("Coches de ocasión", "Used cars"), "coches-de-ocasion.html")], "coches-de-ocasion"
    else:
        migas, nav = [(L("Siniestros", "Accidents"), "siniestros.html")], "siniestros"
    cuerpo = page_head(lang, migas, C["titulo"], C["entradilla"])
    cuerpo += seccion(f'<div class="texto-largo">{bloques(C["texto"], lang)}</div>\n'
                      + f'  <div class="articulo-pie">{compartir(lang)}\n    {boton("btn-ghost", migas[0][1], L("Volver", "Back"))}\n  </div>\n')
    cuerpo += seccion(section_head(L("Preguntas frecuentes", "Frequently asked questions"), "", lang) + faq_html(C["faq"], lang), "alt")
    otras = [x for x in GUIAS_SLUGS if x != g and x in GUIAS]
    cuerpo += seccion(section_head(L("Otras guías", "Other guides"), "", lang)
                      + grid("g3", [card_prod(GUIAS[x][lang]["titulo"], GUIAS[x][lang]["corto"], f"{x}.html", L("Leer", "Read"), lang) for x in otras]))
    cuerpo += seccion_form(lang, L("¿Te ayudamos con tu caso?", "Can we help with your case?"),
                           L("Cuéntanos qué ha pasado y te decimos cómo seguir.", "Tell us what happened and we'll tell you how to proceed."))
    return documento(lang, g, C["titulo"], C["entradilla"], cuerpo, nav, "article")


def pagina_telefonos(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [(L("Siniestros", "Accidents"), "siniestros.html")], L("Teléfonos de asistencia en carretera", "Roadside assistance numbers"),
                       L("Si tu coche se queda parado o has tenido un accidente, el primer paso es llamar a la asistencia de tu compañía. Aquí tienes los teléfonos de autos de las principales aseguradoras.", "If your car breaks down or you've had an accident, the first step is to call your insurer's assistance line. Here are the car insurance numbers of the main insurers."))
    fichas = []
    for nombre, lineas in TELEFONOS:
        busca = (nombre + " " + " ".join(l[0] for l in lineas)).lower()
        li = "".join(f'<li><span class="ramo">{esc(l[0] if lang == "es" else l[3])}</span><a class="tel" href="tel:{l[1]}">{ico("phone")}{esc(l[2])}</a></li>' for l in lineas)
        fichas.append(f'<article class="tel-comp" data-busca="{esc(busca)}">\n  <h3>{esc(nombre)}</h3>\n  <ul class="tel-lineas">{li}</ul>\n</article>')
    cuerpo += seccion(f"""  <div class="panel" style="margin-bottom:34px">
    <h2>{L("Después de la grúa, llámanos", "After the tow truck, call us")}</h2>
    <p>{L("Pide que lleven el coche a Green Car Service Tenerife, en Las Chafiras. Nos encargamos del resto con tu aseguradora.", "Ask for the car to be taken to Green Car Service Tenerife in Las Chafiras. We'll handle the rest with your insurer.")}</p>
    <div class="actions">{btn_tel("btn-navy")}{btn_wa("btn-line", lang, True)}</div>
  </div>
  <div class="grid g2">{card_ico("road", L("Antes de llamar", "Before you call"), L("Ten a mano la matrícula, el número de póliza y la ubicación exacta (punto kilométrico o dirección). El teléfono de asistencia aparece también en tu póliza y en el recibo.", "Have the registration, your policy number and the exact location (kilometre marker or address) ready. The assistance number also appears on your policy and receipt."), lang)}{card_ico("alert", L("Si hay heridos", "If anyone is hurt"), L("Llama primero al 112. Señaliza el vehículo, ponte el chaleco y sal de la calzada por el lado seguro.", "Call 112 first. Signal the vehicle, put on your vest and get off the road on the safe side."), lang)}</div>
  <div class="tel-buscador">{ico("search")}<input id="buscaTel" type="search" placeholder="{L("Busca tu compañía…", "Search your insurer…")}" aria-label="{L("Buscar compañía", "Search insurer")}"></div>
  <p class="tel-conteo" id="conteoTel">{len(fichas)} {L("compañías", "insurers")}</p>
  <div class="tel-dir" id="dirTel">{"".join(fichas)}</div>
  <p class="tel-vacio" id="vacioTel" hidden>{L("No hay ninguna compañía con ese nombre.", "No insurer matches that name.")}</p>
  <div class="note" style="margin-top:26px"><p>{L("Los teléfonos pueden cambiar. Comprueba siempre el que figura en tu póliza.", "Numbers may change. Always check the one shown on your policy.")}</p></div>
""")
    cuerpo += panel(lang, L("¿Necesitas reparar el coche?", "Need your car repaired?"), L("Trabajamos con tu aseguradora.", "We work with your insurer."), ("presupuesto.html", L("Pedir presupuesto", "Get an estimate")))
    return documento(lang, "telefonos-de-asistencia", L("Teléfonos de asistencia en carretera", "Roadside assistance numbers"),
                     L("Teléfonos de asistencia en carretera y de autos de las principales aseguradoras.", "Roadside assistance and car claims numbers of the main insurers."), cuerpo, "siniestros")


# ---------------------------------------------------------------- Ocasión
def pagina_ocasion(lang):
    L = lambda es, en: t(lang, es, en)
    web = E["web_actual"] + "coches-de-segunda-mano-tenerife2/"
    cuerpo = page_head(lang, [], L("Coches de ocasión", "Used cars"),
                       L("Coches de segunda mano en el sur de Tenerife que puedes ver en nuestro taller de Las Chafiras.", "Second-hand cars in the south of Tenerife that you can see at our workshop in Las Chafiras."),
                       f'\n  <div class="actions">{boton("btn-primary", web + "category/view/1", L("Ver el stock actual", "See current stock"), "car", True)}{btn_wa("btn-line", lang)}</div>')
    cuerpo += seccion(section_head(L("Por tipo de vehículo", "By vehicle type"), L("El stock cambia a menudo. Consulta los coches disponibles en cada categoría o pregúntanos por lo que buscas.", "Stock changes often. Check the cars available in each category or ask us for what you're looking for."), lang)
                      + grid("g3", [
                          card_ico("car", L("Turismos", "Cars"), L("Utilitarios, compactos y berlinas para el día a día en la isla.", "City cars, hatchbacks and saloons for everyday driving on the island."), lang, web + "category/view/1", L("Ver turismos", "See cars"), "card coche-cat"),
                          card_ico("road", L("SUV y todoterreno", "SUVs & 4x4s"), L("Más altura y espacio para subir al monte o cargar el equipaje.", "More height and space for mountain roads or luggage."), lang, web + "category/view/1", L("Consultar", "Enquire"), "card coche-cat"),
                          card_ico("truck", "Pick-up", L("Vehículos pick-up para trabajo y ocio.", "Pick-ups for work and leisure."), lang, web + "category/view/4", L("Ver pick-up", "See pick-ups"), "card coche-cat"),
                      ]).replace('href="http', 'target="_blank" rel="noopener" href="http'))
    cuerpo += seccion(f"""  <div class="grid g2" style="align-items:start;gap:44px">
    <div>
      <span class="eyebrow-dark">{L("Comprar con tranquilidad", "Buy with peace of mind")}</span>
      <h2>{L("Un coche de ocasión con un taller detrás", "A used car with a garage behind it")}</h2>
      <p style="color:var(--muted)">{md(L("Comprar a un taller tiene ventajas: puedes ver el coche en persona, preguntar por su historial y, después de la compra, tienes quien lo mantenga. Además, la compra a un profesional incluye la garantía legal que marca la normativa de consumo.", "Buying from a garage has its advantages: you can see the car in person, ask about its history and, after the purchase, you have someone to look after it. Buying from a business also includes the legal guarantee required by consumer law."), lang)}</p>
      {boton("btn-ghost", "guia-comprar-coche-de-ocasion.html", L("Guía para comprar un coche de ocasión", "Guide to buying a used car")).replace("</a>", f" {ico('arrow')}</a>")}
    </div>
    {checks_titulados([
        (L("Lo ves en persona", "See it in person"), L("En nuestras instalaciones de Las Chafiras, de lunes a viernes.", "At our premises in Las Chafiras, Monday to Friday.")),
        (L("Toda la información", "All the information"), L("Documentación, [[itv|ITV]] e historial antes de decidir.", "Paperwork, [[itv|ITV]] and history before you decide.")),
        (L("Revisión de carrocería", "Bodywork check"), L("Pintura, estructura y documentación, con informe.", "Paint, structure and paperwork, with a report.")),
        (L("Te lo ponemos fácil", "We make it easy"), L("Pregunta por WhatsApp o ven a verlo sin cita.", "Ask on WhatsApp or come and see it without an appointment.")),
    ], lang)}
  </div>
""", "alt")
    cuerpo += panel(lang, L("¿Buscas un coche concreto?", "Looking for a specific car?"), L("Dinos qué necesitas y te avisamos si entra algo que encaje.", "Tell us what you need and we'll let you know if something suitable comes in."), ("contacto.html", L("Escríbenos", "Get in touch")))
    return documento(lang, "coches-de-ocasion", L("Coches de ocasión", "Used cars"),
                     L("Coches de segunda mano en Tenerife sur: turismos, SUV y pick-up en Green Car Service Tenerife, Las Chafiras.", "Second-hand cars in south Tenerife: cars, SUVs and pick-ups at Green Car Service Tenerife, Las Chafiras."),
                     cuerpo, "coches-de-ocasion")


# ---------------------------------------------------------------- Blog
def pagina_blog(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [], "Blog", L("Consejos prácticos para cuidar tu coche, entender cada reparación y saber qué hacer si tienes un percance.", "Practical tips to look after your car, understand each repair and know what to do if something happens."))
    navc = "".join(f'<a class="btn btn-ghost" href="#{c}">{esc(v[0 if lang == "es" else 1])} <span class="cuenta">{sum(1 for a in ARTICULOS if a["cat"] == c)}</span></a>'
                   for c, v in CATEGORIAS_BLOG.items())
    secs = ""
    for c, v in CATEGORIAS_BLOG.items():
        arts = [a for a in ARTICULOS if a["cat"] == c]
        if not arts:
            continue
        tarjetas = "".join(card_prod(a[lang]["titulo"], a[lang]["resumen"], f"{a['slug']}.html", L("Leer", "Read"), lang, fecha=fecha_txt(a["fecha"], lang)) for a in arts[:3])
        secs += (f'  <div class="blog-sec" id="{c}"><div class="section-head" style="margin-bottom:18px"><h2>{esc(v[0 if lang == "es" else 1])} <span class="cuenta">{len(arts)}</span></h2></div>'
                 f'<div class="grid g3-blog">{tarjetas}</div>'
                 f'<div class="mas-entradas">{boton("btn-ghost", f"categoria-{c}.html", L("Ver todos", "See all"))}</div></div>\n'.replace("</a></div></div>", f" {ico('arrow')}</a></div></div>"))
    cuerpo += seccion(f'  <nav class="blog-nav" aria-label="{L("Categorías del blog", "Blog categories")}">{navc}</nav>\n{secs}')
    cuerpo += panel(lang, L("¿Te resolvemos una duda concreta?", "Can we answer a specific question?"), L("Escríbenos y te contestamos sin tecnicismos.", "Write to us and we'll answer without jargon."), ("contacto.html", L("Escríbenos", "Get in touch")))
    return documento(lang, "blog", "Blog", L("Blog de Green Car Service Tenerife: chapa y pintura, particulares, empresas y flotas, seguros y siniestros, compraventa y tu coche en Tenerife.", "Green Car Service Tenerife blog: bodywork and paint, private customers, businesses and fleets, insurance and claims, buying and selling, and your car in Tenerife."), cuerpo, "blog")


def pagina_categoria(c, lang):
    L = lambda es, en: t(lang, es, en)
    nombre = CATEGORIAS_BLOG[c][0 if lang == "es" else 1]
    arts = [a for a in ARTICULOS if a["cat"] == c]
    cuerpo = page_head(lang, [("Blog", "blog.html")], nombre, L(f"{len(arts)} artículos sobre {nombre.lower()}.", f"{len(arts)} articles about {nombre.lower()}."))
    tarjetas = "".join(card_prod(a[lang]["titulo"], a[lang]["resumen"], f"{a['slug']}.html", L("Leer", "Read"), lang, fecha=fecha_txt(a["fecha"], lang)) for a in arts)
    otras = "".join(f'<a class="btn btn-ghost" href="categoria-{x}.html">{esc(v[0 if lang == "es" else 1])}</a>' for x, v in CATEGORIAS_BLOG.items() if x != c)
    cuerpo += seccion(f'  <div class="grid g3-blog">{tarjetas}</div>\n  <div class="section-head" style="margin-top:44px"><h2>{L("Otras categorías", "Other categories")}</h2></div>\n  <div class="sub-cats">{otras}</div>\n')
    cuerpo += panel(lang, L("¿Te resolvemos una duda concreta?", "Can we answer a specific question?"), L("Escríbenos y te contestamos sin tecnicismos.", "Write to us and we'll answer without jargon."), ("contacto.html", L("Escríbenos", "Get in touch")))
    return documento(lang, f"categoria-{c}", nombre, L(f"Artículos de {nombre.lower()} del blog de Green Car Service Tenerife.", f"{nombre} articles from the Green Car Service Tenerife blog."), cuerpo, "blog")


def pagina_articulo(a, lang):
    L = lambda es, en: t(lang, es, en)
    C = a[lang]
    c = a["cat"]
    nombre = CATEGORIAS_BLOG[c][0 if lang == "es" else 1]
    meta = (f'\n  <div class="art-meta"><span>{ico("calendar")}{fecha_txt(a["fecha"], lang)}</span>'
            f'<span>{ico("tag")}<a href="categoria-{c}.html" style="color:inherit">{esc(nombre)}</a></span></div>')
    cuerpo = page_head(lang, [("Blog", "blog.html"), (nombre, f"categoria-{c}.html")], C["titulo"], C["resumen"], meta)
    cuerpo += seccion(f'  <div class="articulo-body">{bloques(C["cuerpo"], lang)}</div>\n'
                      f'  <div class="articulo-pie">\n    {compartir(lang)}\n    {boton("btn-ghost", f"categoria-{c}.html", L(f"Volver a {nombre}", f"Back to {nombre}"))}\n  </div>\n')
    rel = [x for x in ARTICULOS if x["cat"] == c and x["slug"] != a["slug"]][:3]
    if len(rel) < 3:
        rel += [x for x in ARTICULOS if x["slug"] != a["slug"] and x not in rel][:3 - len(rel)]
    cuerpo += seccion(section_head(L("Sigue leyendo", "Keep reading"), "", lang)
                      + grid("g3-blog", [card_prod(x[lang]["titulo"], x[lang]["resumen"], f"{x['slug']}.html", L("Leer", "Read"), lang,
                                                   CATEGORIAS_BLOG[x["cat"]][0 if lang == "es" else 1]) for x in rel]), "alt")
    cuerpo += panel(lang, L("¿Tu coche necesita una revisión?", "Does your car need a check-up?"), L("Pide cita y lo vemos sin compromiso.", "Book an appointment and we'll take a look with no obligation."))
    return documento(lang, a["slug"], C["titulo"], C["resumen"], cuerpo, "blog", "article")


# ---------------------------------------------------------------- Ayuda
def pagina_diccionario(lang):
    L = lambda es, en: t(lang, es, en)
    idx = 0 if lang == "es" else 1
    terminos = sorted(GLOSARIO_TERMINOS.items(), key=lambda kv: _norm(kv[1][idx]))
    letras = {}
    for k, v in terminos:
        letras.setdefault(_norm(v[idx])[0].upper(), []).append((k, v[idx]))
    abc = "".join(f'<a href="#letra-{l}">{l}</a>' for l in letras)
    bloques_html = ""
    for l, items in letras.items():
        fichas = "".join(f'<div class="term" id="t-{k}"><h3>{esc(n)}</h3><p>{md(GLOSARIO.get(k, {}).get(lang, ""), lang)}</p></div>' for k, n in items)
        bloques_html += f'  <div class="letra-bloque" id="letra-{l}"><h2 class="letra">{l}</h2><div class="terms">{fichas}</div></div>\n'
    cuerpo = page_head(lang, [], L("Diccionario de chapa y pintura", "Bodywork & paint glossary"),
                       L("Los términos que aparecen en un presupuesto, una factura del taller o un parte del seguro, explicados en lenguaje claro.", "The terms you'll find in a garage estimate, an invoice or an insurance claim, explained in plain language."))
    cuerpo += seccion(f'  <nav class="abc" aria-label="{L("Índice alfabético", "Alphabetical index")}">{abc}</nav>\n{bloques_html}')
    cuerpo += panel(lang, L("¿Sigue habiendo algo que no está claro?", "Still something unclear?"), L("Pregúntanos y te lo explicamos con el coche delante.", "Ask us and we'll explain it with the car in front of us."), ("contacto.html", L("Escríbenos", "Get in touch")))
    return documento(lang, "diccionario-de-chapa-y-pintura", L("Diccionario de chapa y pintura", "Bodywork & paint glossary"),
                     L("Glosario de términos de chapa, pintura, compraventa y seguros del automóvil explicados en lenguaje claro.", "Glossary of bodywork, paint, car buying and insurance terms explained in plain language."), cuerpo, "blog")


def _norm(s):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def pagina_faq(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [], L("Preguntas frecuentes", "Frequently asked questions"),
                       L("Las dudas que más nos plantean en el taller, respondidas.", "The questions we're asked most often at the garage, answered."))
    navf = "".join(f'<a class="btn btn-ghost" href="#faq-{b["id"]}">{esc(b[lang]["titulo"])}</a>' for b in FAQ)
    secs = "".join(f'  <div class="blog-sec" id="faq-{b["id"]}"><div class="section-head" style="margin-bottom:18px"><h2>{esc(b[lang]["titulo"])}</h2></div>\n{faq_html(b[lang]["preguntas"], lang)}  </div>\n' for b in FAQ)
    cuerpo += seccion(f'  <nav class="blog-nav">{navf}</nav>\n{secs}')
    cuerpo += panel(lang, L("¿No está tu pregunta?", "Your question isn't here?"), L("Llámanos o escríbenos por WhatsApp.", "Call us or message us on WhatsApp."), ("contacto.html", L("Escríbenos", "Get in touch")))
    return documento(lang, "preguntas-frecuentes", L("Preguntas frecuentes", "Frequently asked questions"),
                     L("Preguntas frecuentes sobre citas, reparaciones de chapa y pintura, seguros, revisión para compraventa y coches de ocasión en Green Car Service Tenerife.", "FAQ about appointments, body and paint repairs, insurance, pre-purchase checks and used cars at Green Car Service Tenerife."), cuerpo, "contacto")


# ---------------------------------------------------------------- Contacto y formularios
def datos_contacto(lang):
    L = lambda es, en: t(lang, es, en)
    return f"""  <div>
    <h2 style="font-size:23px">{L("Dónde estamos", "Where we are")}</h2>
    <ul class="info-list" style="margin-bottom:28px">
      <li><span class="ico">{ico("pin")}</span><div><b>{L("Taller", "Workshop")}</b><span>{esc(E["direccion"])}<br>{esc(E["cp_ciudad"])}</span></div></li>
      <li><span class="ico">{ico("phone")}</span><div><b>{L("Teléfono", "Phone")}</b><span><a href="tel:{E["telefono_tel"]}">{E["telefono"]}</a></span></div></li>
      <li><span class="ico">{ico("whatsapp")}</span><div><b>WhatsApp</b><span><a href="https://wa.me/{E["whatsapp_wa"]}" target="_blank" rel="noopener">{E["whatsapp"]}</a></span></div></li>
      <li><span class="ico">{ico("mail")}</span><div><b>{L("Correo", "Email")}</b><span><a href="mailto:{E["email"]}">{E["email"]}</a></span></div></li>
      <li><span class="ico">{ico("instagram")}</span><div><b>Instagram</b><span><a href="{E["instagram"]}" target="_blank" rel="noopener">@greencarservicetenerife6</a></span></div></li>
    </ul>
    <h3>{ico("clock")} {L("Horario", "Opening hours")}</h3>
    <table class="hours"><tbody><tr><td>{L("Lunes a viernes", "Monday to Friday")}</td><td>07:00 – 16:00</td></tr><tr><td>{L("Sábados, domingos y festivos", "Weekends and public holidays")}</td><td>{L("Cerrado", "Closed")}</td></tr></tbody></table>
    <div style="margin-top:24px">{mapa_iframe(lang, 280)}</div>
  </div>
"""


def pagina_contacto(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [], L("Contacto", "Contact"), L("Llámanos, escríbenos por WhatsApp o ven a vernos a Las Chafiras. Te respondemos lo antes posible.", "Call us, message us on WhatsApp or come and see us in Las Chafiras. We'll get back to you as soon as possible."))
    cuerpo += seccion(f'<div class="grid g2" style="gap:44px;align-items:start">\n  {formulario(lang, "contacto", None, opciones_servicio(lang))}\n{datos_contacto(lang)}</div>\n')
    return documento(lang, "contacto", L("Contacto", "Contact"), L(f"Contacta con Green Car Service Tenerife: {E['telefono']}, WhatsApp {E['whatsapp']}, {E['email']}. Av. 7 Islas Canarias 34, Las Chafiras.", f"Contact Green Car Service Tenerife: {E['telefono']}, WhatsApp {E['whatsapp']}, {E['email']}. Av. 7 Islas Canarias 34, Las Chafiras."), cuerpo, "contacto")


def pagina_cita(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [(L("Contacto", "Contact"), "contacto.html")], L("Pedir cita", "Book an appointment"),
                       L("Elige el día que te viene bien y te llamamos para confirmarlo. Si lo prefieres, recogemos el coche en tu casa o en tu trabajo.", "Choose a day that suits you and we'll call to confirm. If you prefer, we'll collect the car from your home or workplace."))
    cuerpo += seccion(f'<div class="grid g2" style="gap:44px;align-items:start">\n  {formulario(lang, "cita", None, opciones_servicio(lang))}\n{datos_contacto(lang)}</div>\n')
    cuerpo += seccion(section_head(L("Cómo funciona", "How it works"), "", lang) + f"""  <ol class="pasos">
      <li><b>{L("Nos pides cita", "You request an appointment")}</b><span>{L("Por el formulario, por teléfono o por WhatsApp.", "Via the form, by phone or on WhatsApp.")}</span></li>
      <li><b>{L("Te confirmamos", "We confirm")}</b><span>{L("Te llamamos para cerrar día, hora y, si quieres, la recogida.", "We call to agree the day, time and, if you like, collection.")}</span></li>
      <li><b>{L("Presupuesto por escrito", "Written estimate")}</b><span>{md(L("Antes de reparar nada, te damos el [[presupuesto|presupuesto]] para que lo apruebes.", "Before any repair, we give you the [[presupuesto|estimate]] to approve."), lang)}</span></li>
      <li><b>{L("Te informamos y entregamos", "We keep you posted and deliver")}</b><span>{L("Sigues el estado del coche y te lo devolvemos limpio.", "You follow the car's progress and we return it clean.")}</span></li>
    </ol>
""", "alt")
    return documento(lang, "pedir-cita", L("Pedir cita", "Book an appointment"), L("Pide cita en Green Car Service Tenerife, taller en Las Chafiras. Recogida y entrega a domicilio.", "Book an appointment at Green Car Service Tenerife, garage in Las Chafiras. Collection and delivery available."), cuerpo, None)


def pagina_presupuesto(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [(L("Contacto", "Contact"), "contacto.html")], L("Presupuesto sin compromiso", "Free, no-obligation estimate"),
                       L("Cuéntanos qué le pasa a tu coche y te preparamos un presupuesto por escrito. Si es chapa o pintura, envíanos fotos por WhatsApp y te orientamos antes de que vengas.", "Tell us what's wrong with your car and we'll prepare a written estimate. For bodywork or paint, send us photos on WhatsApp and we'll give you an idea before you come in."))
    cuerpo += seccion(f"""<div class="grid g2" style="gap:44px;align-items:start">
  {formulario(lang, "presupuesto", None, opciones_servicio(lang))}
  <div>
    <h2 style="font-size:23px">{L("Fotos que nos ayudan", "Photos that help us")}</h2>
    {checks_simples([L("Una foto general del coche donde se vea la zona dañada.", "An overall photo of the car showing the damaged area."), L("Fotos de cerca del golpe, desde dos ángulos.", "Close-ups of the damage from two angles."), L("La etiqueta del código de color, si la localizas (suele estar en el marco de la puerta).", "The paint code label, if you can find it (usually in the door frame)."), L("La matrícula o el número de bastidor.", "The registration or VIN.")], lang)}
    <div class="btn-par" style="margin-top:22px">{btn_wa("btn-primary", lang, True)}{btn_tel("btn-ghost")}</div>
    <div class="note" style="margin-top:22px"><p>{md(L("Por fotos podemos orientarte, pero el [[presupuesto|presupuesto]] definitivo se hace con el coche en el taller: a veces un golpe esconde daños que no se ven a simple vista.", "Photos let us give you a rough idea, but the final [[presupuesto|estimate]] is made with the car at the workshop: sometimes a knock hides damage you can't see at first glance."), lang)}</p></div>
  </div>
</div>
""")
    cuerpo += bloque_aseguradora(lang)
    return documento(lang, "presupuesto", L("Presupuesto sin compromiso", "Free estimate"), L("Pide presupuesto sin compromiso para chapa y pintura en Green Car Service Tenerife.", "Ask for a free, no-obligation estimate for bodywork and paint at Green Car Service Tenerife."), cuerpo, None)


# ---------------------------------------------------------------- Legal y mapa
LEGAL_TIT = {"aviso-legal": ("Aviso legal", "Legal notice"), "politica-de-privacidad": ("Política de privacidad", "Privacy policy"), "cookies": ("Política de cookies", "Cookie policy")}


def _slug(s):
    import re
    return re.sub(r"[^a-z0-9]+", "-", _norm(s)).strip("-")


def pagina_legal_doc(slug, lang):
    L = lambda es, en: t(lang, es, en)
    D = LEGAL[slug][lang]
    idx = "".join(f'<li><a href="#{_slug(s[0])}">{ico("arrow")}<span>{esc(plano(s[0]))}</span></a></li>' for s in D["secciones"])
    otros = "".join(f'<li><a href="{k}.html">{ico("doc")}<span>{v[0] if lang == "es" else v[1]}</span></a></li>' for k, v in LEGAL_TIT.items() if k != slug)
    secs = "".join(f'<div class="legal-sec" id="{_slug(s[0])}"><h2>{md(s[0], lang)}</h2>{bloques(s[1], lang)}</div>' for s in D["secciones"])
    cuerpo = page_head(lang, [(L("Información legal", "Legal information"), "legal.html")], D["titulo"], D["entradilla"])
    cuerpo += seccion(f"""<div class="legal-layout">
  <aside class="legal-nav">
    <h3>{L("En esta página", "On this page")}</h3>
    <ul class="foot-links dark">{idx}</ul>
    <h3 style="margin-top:26px">{L("Otros documentos", "Other documents")}</h3>
    <ul class="foot-links dark">{otros}</ul>
  </aside>
  <div class="legal-body">{secs}<p class="legal-version">{L("Última actualización: septiembre de 2026.", "Last updated: September 2026.")}</p></div>
</div>
""")
    return documento(lang, slug, D["titulo"], D["entradilla"], cuerpo, None)


def pagina_legal(lang):
    L = lambda es, en: t(lang, es, en)
    cuerpo = page_head(lang, [], L("Información legal", "Legal information"), L("Condiciones de uso del sitio y tratamiento de datos personales.", "Terms of use of the site and processing of personal data."))
    cuerpo += seccion(grid("g3", [card_ico("doc", v[0] if lang == "es" else v[1], plano(LEGAL[k][lang]["entradilla"]) if k in LEGAL else "", lang, f"{k}.html", L("Leer", "Read")) for k, v in LEGAL_TIT.items()]))
    return documento(lang, "legal", L("Información legal", "Legal information"), L("Aviso legal, política de privacidad y política de cookies de Green Car Service Tenerife.", "Legal notice, privacy policy and cookie policy of Green Car Service Tenerife."), cuerpo, None)


def pagina_mapa(lang):
    L = lambda es, en: t(lang, es, en)
    grupos = {}
    for slug, tes, ten, sec in PAGINAS:
        grupos.setdefault(sec, []).append((slug, tes if lang == "es" else ten))
    nombres = {"principal": L("Principales", "Main pages"), "chapa-pintura": L("Chapa y pintura", "Bodywork & paint"), "revision": L("Revisión para compraventa", "Pre-purchase & pre-sale inspection"),
               "clientes": L("A quién damos servicio", "Who we work for"),
               "ventajas": L("Ventajas Green Car", "The Green Car advantage"), "guias": L("Siniestros y guías", "Accidents & guides"),
               "blog": "Blog", "legal": L("Información legal", "Legal information")}
    cards = ""
    for sec, items in grupos.items():
        li = "".join(f'<li><a href="{s}.html">{ico("arrow")}<span>{esc(n)}</span></a></li>' for s, n in items)
        cards += f'<div class="card"><h3>{esc(nombres.get(sec, sec))}</h3><ul class="foot-links dark">{li}</ul></div>'
    cuerpo = page_head(lang, [], L("Mapa web", "Sitemap"), L("Todas las páginas del sitio, ordenadas por sección.", "All the pages on the site, organised by section."))
    cuerpo += seccion(f'<div class="grid g3">{cards}</div>\n')
    return documento(lang, "mapa-web", L("Mapa web", "Sitemap"), L("Mapa del sitio web de Green Car Service Tenerife.", "Green Car Service Tenerife sitemap."), cuerpo, None)


# ---------------------------------------------------------------- Principal
def main():
    trabajos = []  # (slug, fn, tes, ten, seccion)
    P = lambda slug, fn, tes, ten, sec: trabajos.append((slug, fn, tes, ten, sec))
    P("index", pagina_inicio, "Inicio", "Home", "principal")
    P("conocenos", pagina_conocenos, "Conócenos", "About us", "principal")
    P("instalaciones", pagina_instalaciones, "Instalaciones", "Our premises", "principal")
    P("sostenibilidad", pagina_sostenibilidad, "Sostenibilidad", "Sustainability", "principal")
    P("opiniones", pagina_opiniones, "Opiniones de clientes", "Customer reviews", "principal")
    P("servicios", pagina_servicios, "Servicios", "Services", "principal")
    P("coches-de-ocasion", pagina_ocasion, "Coches de ocasión", "Used cars", "principal")
    P("pedir-cita", pagina_cita, "Pedir cita", "Book an appointment", "principal")
    P("presupuesto", pagina_presupuesto, "Presupuesto sin compromiso", "Free estimate", "principal")
    P("contacto", pagina_contacto, "Contacto", "Contact", "principal")
    P("preguntas-frecuentes", pagina_faq, "Preguntas frecuentes", "FAQ", "principal")
    P("diccionario-de-chapa-y-pintura", pagina_diccionario, "Diccionario de chapa y pintura", "Bodywork & paint glossary", "principal")
    for cat in CATEGORIAS_SERVICIO:
        hub = CATEGORIAS_SERVICIO[cat][0][:-5]
        P(hub, lambda lang, c=cat: pagina_hub(c, lang), HUB_TIT[cat][0], HUB_TIT[cat][1], cat)
        for s in SERVICIOS_SLUGS[cat]:
            if s in SERVICIOS:
                P(s, lambda lang, s=s: pagina_servicio(s, lang), SERVICIOS[s]["es"]["titulo"], SERVICIOS[s]["en"]["titulo"], cat)
    P("siniestros", pagina_siniestros, "Siniestros y accidentes", "Accidents & claims", "guias")
    P("telefonos-de-asistencia", pagina_telefonos, "Teléfonos de asistencia", "Assistance numbers", "guias")
    for g in GUIAS_SLUGS:
        if g in GUIAS:
            P(g, lambda lang, g=g: pagina_guia(g, lang), GUIAS[g]["es"]["titulo"], GUIAS[g]["en"]["titulo"], "guias")
    P("blog", pagina_blog, "Blog", "Blog", "blog")
    for c, v in CATEGORIAS_BLOG.items():
        P(f"categoria-{c}", lambda lang, c=c: pagina_categoria(c, lang), f"Blog: {v[0]}", f"Blog: {v[1]}", "blog")
    for a in sorted(ARTICULOS, key=lambda a: a["es"]["titulo"]):
        P(a["slug"], lambda lang, a=a: pagina_articulo(a, lang), a["es"]["titulo"], a["en"]["titulo"], "blog")
    P("legal", pagina_legal, "Información legal", "Legal information", "legal")
    for k, v in LEGAL_TIT.items():
        if k in LEGAL:
            P(k, lambda lang, k=k: pagina_legal_doc(k, lang), v[0], v[1], "legal")
    P("mapa-web", pagina_mapa, "Mapa web", "Sitemap", "legal")

    for slug, fn, tes, ten, sec in trabajos:
        registrar(slug, tes, ten, sec)
    # Todas las páginas son generadas: se borran las anteriores para no dejar huérfanas.
    for carpeta in (RAIZ, os.path.join(RAIZ, "en")):
        if os.path.isdir(carpeta):
            for f in os.listdir(carpeta):
                if f.endswith(".html"):
                    os.remove(os.path.join(carpeta, f))
    n = 0
    for slug, fn, *_ in trabajos:
        for lang in LANGS:
            escribir(lang, slug, fn(lang))
            n += 1
    # sitemap.xml
    base = E["base_url"]
    urls = "".join(
        f'<url><loc>{base}{s}.html</loc><xhtml:link rel="alternate" hreflang="es" href="{base}{s}.html"/>'
        f'<xhtml:link rel="alternate" hreflang="en" href="{base}en/{s}.html"/></url>\n'
        f'<url><loc>{base}en/{s}.html</loc><xhtml:link rel="alternate" hreflang="es" href="{base}{s}.html"/>'
        f'<xhtml:link rel="alternate" hreflang="en" href="{base}en/{s}.html"/></url>\n'
        for s, *_ in trabajos)
    with open(os.path.join(RAIZ, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n")
    with open(os.path.join(RAIZ, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n")
    print(f"{n} páginas generadas ({len(trabajos)} por idioma).")


if __name__ == "__main__":
    main()
