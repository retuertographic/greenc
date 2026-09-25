"""Piezas comunes del generador: iconos, marcado de textos, cabecera, pie y
componentes reutilizables. Replica la maquetación del sitio de Retuerto y
Asociados con los datos de Green Car Service Tenerife."""
import html
import os
import re

from comun import EMPRESA as E, GLOSARIO_TERMINOS, CATEGORIAS_SERVICIO

AQUI = os.path.dirname(os.path.abspath(__file__))
FRAG = os.path.join(AQUI, "fragmentos")
ANIO = 2026


def leer_frag(nombre):
    with open(os.path.join(FRAG, nombre), encoding="utf-8") as f:
        return f.read().strip()


WA_SVG = leer_frag("whatsapp.svg")
IG_SVG = leer_frag("instagram.svg")
COMPARTIR = {"es": leer_frag("compartir-es.html"), "en": leer_frag("compartir-en.html")}

# ---------------------------------------------------------------- Iconos
_P = {
    "car": '<path d="M5 17H3.5v-4.2l1.8-4.9A2 2 0 0 1 7.2 6.5h9.6a2 2 0 0 1 1.9 1.4l1.8 4.9V17H19"/><path d="M3.5 12.5h17"/><circle cx="7.5" cy="17" r="2"/><circle cx="16.5" cy="17" r="2"/><path d="M9.5 17h5"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "paint": '<rect x="2.5" y="2.5" width="15" height="6" rx="2"/><path d="M17.5 5.5h1.5a2 2 0 0 1 2 2V10a2 2 0 0 1-2 2h-7a2 2 0 0 0-2 2v2"/><rect x="8.5" y="16" width="4" height="5.5" rx="1"/>',
    "spray": '<path d="M7 9h6v11.5a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1z"/><path d="M8 9V6.5h4V9"/><path d="M9 6.5V4h2"/><path d="M15.5 4h.01M17.5 2.8h.01M17.5 6h.01M19.5 4.5h.01M19.5 7.8h.01"/>',
    "shield": '<path d="M12 3.2 19 6v6c0 4.4-3 7.6-7 8.8-4-1.2-7-4.4-7-8.8V6Z"/><path d="m9 12 2 2 4-4"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
    "bolt": '<path d="M13 2.5 4 14h7.5l-1 7.5L20 10h-7.5z"/>',
    "battery": '<rect x="2.5" y="7" width="16" height="10" rx="2"/><path d="M21.5 11v2"/><path d="M6.5 10.5v3M10 10.5v3"/>',
    "gauge": '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    "truck": '<path d="M3 6.5h11v10H3z"/><path d="M14 10h4l3 3.5v3h-7"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M9.5 21v-6h5v6"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
    "check": '<path d="m4.5 12.5 4.5 4.5 10.5-10.5"/>',
    "star": '<path d="m12 3.5 2.6 5.5 6 .8-4.4 4.2 1.1 6-5.3-2.9-5.3 2.9 1.1-6L3.4 9.8l6-.8z"/>',
    "phone": '<path d="M6.5 3.5h3l1.5 4-2 1.5a12 12 0 0 0 6 6l1.5-2 4 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.5 5.7 2 2 0 0 1 6.5 3.5Z"/>',
    "mail": '<path d="M3.5 6h17v12h-17z"/><path d="m3.5 7 8.5 6 8.5-6"/>',
    "pin": '<path d="M12 21s6.5-6 6.5-11a6.5 6.5 0 1 0-13 0C5.5 15 12 21 12 21Z"/><circle cx="12" cy="10" r="2.4"/>',
    "doc": '<path d="M5 4.5h9l5 5v10H5z"/><path d="M14 4.5v5h5"/><path d="M8.5 13h7M8.5 16.5h4.5"/>',
    "search": '<circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/>',
    "camera": '<path d="M4 8h3l1.5-2.5h7L17 8h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
    "drop": '<path d="M12 3.5s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11Z"/>',
    "thermo": '<path d="M14 14.8V5a2 2 0 0 0-4 0v9.8a4 4 0 1 0 4 0Z"/>',
    "snow": '<path d="M12 2.5v19M4 7l16 10M4 17 20 7"/><path d="m9.5 4.5 2.5 2 2.5-2M9.5 19.5l2.5-2 2.5 2"/>',
    "wind": '<path d="M3 8h11a3 3 0 1 0-3-3"/><path d="M3 12h16a3 3 0 1 1-3 3"/><path d="M3 16h7"/>',
    "disc": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="2.5"/><path d="M12 5.5v1M12 17.5v1M5.5 12h1M17.5 12h1"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1Z"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="m10.8 12.2 8.7-8.7M16 7l2.5 2.5M18.5 4.5 21 7"/>',
    "sparkle": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16v4M17 18h4"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/>',
    "light": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3Z"/>',
    "eye": '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3"/>',
    "euro": '<path d="M18 7a6.5 6.5 0 1 0 0 10"/><path d="M4 10.5h9M4 13.5h9"/>',
    "users": '<circle cx="9" cy="8" r="3.4"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.8a3.4 3.4 0 0 1 0 6.4M18.5 14.5a6.5 6.5 0 0 1 3 5.5"/>',
    "alert": '<path d="M12 3.5 21.5 20h-19z"/><path d="M12 10v4.5M12 17.2v.3"/>',
    "tool": '<rect x="3" y="8" width="18" height="12" rx="2"/><path d="M8 8V5.5A1.5 1.5 0 0 1 9.5 4h5A1.5 1.5 0 0 1 16 5.5V8"/><path d="M3 13h18M10 13v2h4v-2"/>',
    "recycle": '<path d="M20 11a8 8 0 0 0-14.5-4.5L4 8"/><path d="M4 3.5V8h4.5"/><path d="M4 13a8 8 0 0 0 14.5 4.5L20 16"/><path d="M20 20.5V16h-4.5"/>',
    "plug": '<path d="M9 2.5v5M15 2.5v5"/><path d="M6.5 7.5h11V11a5.5 5.5 0 0 1-11 0z"/><path d="M12 16.5v5"/>',
    "road": '<path d="M8 3 4 21M16 3l4 18"/><path d="M12 4v3M12 10.5v3M12 17v3"/>',
    "info": '<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5.5M12 7.8v.6"/>',
    "chat": '<path d="M20.5 15.5a2 2 0 0 1-2 2H8l-4 3.5v-14a2 2 0 0 1 2-2h12.5a2 2 0 0 1 2 2z"/>',
    "layers": '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
    "hammer": '<path d="m14 12-8.5 8.5a2.1 2.1 0 0 1-3-3L11 9"/><path d="M15 13 9 7l4-4 2.5 2.5L18 5l3 3-2.5 2.5L21 13l-2 2z"/>',
    "clipboard": '<rect x="5" y="4.5" width="14" height="16.5" rx="2"/><path d="M9 4.5V3h6v1.5"/><path d="M8.5 11h7M8.5 15h5"/>',
    "handshake": '<path d="M3 11l4-4 4 2 3-2 7 5-4 4"/><path d="M3 11l6 6 2-1 2 2 2-1"/><path d="M11 9l3 3"/>',
    "award": '<circle cx="12" cy="9" r="5.5"/><path d="m8.5 13.5-1.5 7.5 5-3 5 3-1.5-7.5"/>',
    "map": '<path d="M9 4.5 3.5 6.8v12.7L9 17.2l6 2.3 5.5-2.3V4.5L15 6.8z"/><path d="M9 4.5v12.7M15 6.8v12.7"/>',
    "filter": '<path d="M3.5 5h17l-6.5 8v6l-4 2v-8z"/>',
    "steering": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="2"/><path d="M3.8 10.5 10 12M20.2 10.5 14 12M12 14v6.5"/>',
    "exhaust": '<path d="M2.5 14h11a3 3 0 0 0 0-6h-2"/><path d="M13.5 14h3l1 2"/><path d="M17 8.5c1.5-.5 2.5-1.5 2.5-3M20 12c1-.4 1.5-1 1.5-2"/>',
    "chip": '<rect x="6" y="6" width="12" height="12" rx="1.5"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2.5V6M15 2.5V6M9 18v3.5M15 18v3.5M2.5 9H6M2.5 15H6M18 9h3.5M18 15h3.5"/>',
    # Interfaz
    "arrow": '<path d="M5 12h13"/><path d="m12.5 5.5 6.5 6.5-6.5 6.5"/>',
    "up": '<path d="M12 19V6"/><path d="m5.5 12.5 6.5-6.5 6.5 6.5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "chev": '<path d="m6.5 9.5 5.5 5 5.5-5"/>',
    "book": '<path d="M5 4.5h9.5a2 2 0 0 1 2 2v13H7a2 2 0 0 1-2-2z"/><path d="M16.5 8.5H19v11H7"/>',
    "tag": '<path d="M3.5 12.5V4.5h8l9 9-8 8z"/><circle cx="8" cy="9" r="1.3"/>',
}

STAR_FILL = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2.8 2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z"/></svg>'


def ico(nombre):
    if nombre == "whatsapp":
        return WA_SVG
    if nombre == "instagram":
        return IG_SVG
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + _P[nombre] + "</svg>")


def estrellas(n=5):
    return '<span class="estrellas" aria-hidden="true">' + STAR_FILL * n + "</span>"


# ---------------------------------------------------------------- Idioma
def t(lang, es, en):
    return es if lang == "es" else en


esc = html.escape


def val(lang):
    """Valoración media con el separador decimal de cada idioma."""
    return E["valoracion"] if lang == "es" else E["valoracion"].replace(",", ".")


# ---------------------------------------------------------------- Marcado
GLOSARIO = {}  # clave -> {"es": def, "en": def}; lo rellena generar.py


def md(texto, lang):
    """Convierte el marcado de contenido en HTML seguro."""
    s = esc(texto, quote=False)

    def dic(m):
        clave, visible = m.group(1), m.group(2)
        nombre = GLOSARIO_TERMINOS[clave][0 if lang == "es" else 1]
        defin = GLOSARIO.get(clave, {}).get(lang, "")
        defin = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", defin).replace("**", "")
        return (f'<a class="dic" href="diccionario-de-chapa-y-pintura.html#t-{clave}" '
                f'data-def="{esc(defin)}" data-term="{esc(nombre)}">{visible}</a>')

    s = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", dic, s)

    def enlace(m):
        visible, destino = m.group(1), m.group(2)
        extra = ' target="_blank" rel="noopener"' if destino.startswith("http") else ""
        return f'<a href="{esc(destino)}"{extra}>{visible}</a>'

    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", enlace, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return s


def plano(texto):
    """Texto sin marcado (para meta descripciones y atributos)."""
    s = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", texto)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s.replace("**", "")


def bloques(lista, lang):
    """Renderiza bloques (tipo, valor) de texto largo."""
    out = []
    for tipo, v in lista:
        if tipo == "h2":
            out.append(f"<h2>{md(v, lang)}</h2>")
        elif tipo == "h3":
            out.append(f"<h3>{md(v, lang)}</h3>")
        elif tipo == "p":
            out.append(f"<p>{md(v, lang)}</p>")
        elif tipo == "checks":
            out.append(checks_simples(v, lang))
        elif tipo == "ul":
            out.append("<ul>" + "".join(f"<li>{md(x, lang)}</li>" for x in v) + "</ul>")
        elif tipo == "ol":
            out.append("<ol>" + "".join(f"<li>{md(x, lang)}</li>" for x in v) + "</ol>")
        elif tipo == "quote":
            out.append(f"<blockquote><p>{md(v, lang)}</p></blockquote>")
        elif tipo == "nota":
            out.append(f'<div class="note"><p>{md(v, lang)}</p></div>')
        elif tipo == "tabla":
            filas = [[c.strip() for c in f.split("|")] for f in v]
            cab = "".join(f"<th>{md(c, lang)}</th>" for c in filas[0])
            cuerpo = "".join(
                "<tr>" + "".join(f'<td data-col="{esc(plano(filas[0][i]) if i < len(filas[0]) else "")}">{md(c, lang)}</td>'
                                 for i, c in enumerate(f)) + "</tr>" for f in filas[1:])
            out.append(f'<div class="tabla-scroll"><table class="datos pares"><thead><tr>{cab}</tr></thead>'
                       f"<tbody>{cuerpo}</tbody></table></div>")
    return "".join(out)


def checks_simples(items, lang, estilo=""):
    st = f' style="{estilo}"' if estilo else ""
    return (f'<ul class="checks"{st}>' + "".join(
        f"<li>{ico('check')}<span>{md(x, lang)}</span></li>" for x in items) + "</ul>")


def checks_titulados(items, lang):
    """items: [(titulo, texto)]"""
    return ('<ul class="checks">' + "".join(
        f"<li>{ico('check')}<span><b>{md(a, lang)}</b>{md(b, lang)}</span></li>" for a, b in items)
        + "</ul>")


# ---------------------------------------------------------------- Componentes
def page_head(lang, migas, titulo, entradilla="", extra=""):
    partes = [f'<a href="index.html">{t(lang, "Inicio", "Home")}</a>']
    for texto, href in migas:
        partes.append(f'<a href="{href}">{esc(texto)}</a>')
    partes.append(esc(titulo))
    crumbs = "<span>/</span>".join(partes)
    p = f"\n  <p>{md(entradilla, lang)}</p>" if entradilla else ""
    return (f'<div class="page-head"><div class="wrap">\n  <div class="crumbs">{crumbs}</div>\n'
            f"  <h1>{esc(titulo)}</h1>{p}{extra}\n</div></div>\n")


def section_head(titulo, texto="", lang="es", eyebrow=""):
    eb = f'\n    <span class="eyebrow-dark">{esc(eyebrow)}</span>' if eyebrow else ""
    p = f"\n    <p>{md(texto, lang)}</p>" if texto else ""
    return f'  <div class="section-head">{eb}\n    <h2>{md(titulo, lang)}</h2>{p}\n  </div>\n'


def card_ico(icono, titulo, texto, lang, href=None, mas=None, clase="card"):
    if href:
        # Dentro de una tarjeta enlazada no puede haber otros enlaces.
        cuerpo = (f'\n  <span class="ico">{ico(icono)}</span>\n  <h3>{esc(plano(titulo))}</h3>'
                  f"<p>{esc(plano(texto))}</p>")
        mas_html = f'\n  <span class="more">{esc(mas or t(lang, "Saber más", "Learn more"))} {ico("arrow")}</span>'
        return f'<a class="{clase}" href="{href}">{cuerpo}{mas_html}</a>'
    cuerpo = (f'\n  <span class="ico">{ico(icono)}</span>\n  <h3>{md(titulo, lang)}</h3>'
              f"<p>{md(texto, lang)}</p>")
    return f'<div class="{clase}">{cuerpo}\n</div>'


def card_prod(titulo, texto, href, mas, lang, eyebrow="", fecha=""):
    eb = f'<span class="eyebrow-dark">{esc(eyebrow)}</span>' if eyebrow else ""
    fe = f'<span class="fecha-card">{esc(fecha)}</span>' if fecha else ""
    p = f"<p>{esc(plano(texto))}</p>" if texto else ""
    return (f'<a class="card prod" href="{href}">{eb}<h3>{esc(titulo)}</h3>{fe}{p}'
            f'<span class="more">{esc(mas)} {ico("arrow")}</span></a>')


def grid(clase, items):
    return f'  <div class="grid {clase}">' + "".join(items) + "</div>\n"


def seccion(contenido, clase=""):
    c = f' class="{clase}"' if clase else ""
    return f"<section{c}><div class=\"wrap\">\n{contenido}</div></section>\n"


def boton(clase, href, texto, icono=None, externo=False):
    i = ico(icono) if icono else ""
    ext = ' target="_blank" rel="noopener"' if externo else ""
    return f'<a class="btn {clase}" href="{href}"{ext}>{i}{esc(texto)}</a>'


def btn_tel(clase="btn-line"):
    return boton(clase, f"tel:{E['telefono_tel']}", E["telefono"], "phone")


def btn_wa(clase="btn-line", lang="es", largo=False):
    txt = f"WhatsApp {E['whatsapp']}" if largo else "WhatsApp"
    return boton(clase, f"https://wa.me/{E['whatsapp_wa']}", txt, "whatsapp", externo=True)


def panel(lang, titulo, texto, primario=("pedir-cita.html", None)):
    href, txt = primario
    txt = txt or t(lang, "Pedir cita", "Book an appointment")
    return (f'<section class="tight"><div class="wrap"><div class="panel">\n  <h2>{esc(titulo)}</h2>\n'
            f"  <p>{md(texto, lang)}</p>\n  <div class=\"actions\">\n    "
            f"{boton('btn-primary', href, txt, 'calendar')}\n    {btn_tel()}\n    {btn_wa(lang=lang)}\n"
            "  </div>\n</div></div></section>\n")


def compartir(lang):
    return COMPARTIR[lang]


def faq_html(preguntas, lang):
    out = []
    for q, a in preguntas:
        out.append(f'<details class="faq-item">\n  <summary>{md(q, lang)}{ico("chev")}</summary>\n'
                   f'  <div class="faq-r"><p>{md(a, lang)}</p></div>\n</details>')
    return '  <div class="faq">' + "".join(out) + "</div>\n"


def bloque_aseguradora(lang, con_boton=True):
    """Equivalente al bloque «Lo que realmente es un Corredor» de Retuerto."""
    btn = (f'\n      {boton("btn-ghost", "servicio-gestion-con-aseguradoras.html", t(lang, "Cómo lo gestionamos", "How we handle it"))}'
           if con_boton else "")
    btn = btn.replace("</a>", f" {ico('arrow')}</a>")
    items = [
        (t(lang, "Tú eliges el taller", "You choose the garage"),
         t(lang, "En general puedes llevar el coche al taller que prefieras; te ayudamos a revisar qué dice tu póliza.",
           "As a rule you can take your car to the garage you prefer; we help you check what your policy says.")),
        (t(lang, "Hablamos con el perito", "We deal with the loss adjuster"),
         t(lang, "Preparamos la valoración de daños y la comentamos con el perito de tu compañía.",
           "We prepare the damage assessment and go through it with your insurer's loss adjuster.")),
        (t(lang, "Recogemos y entregamos", "We collect and deliver"),
         t(lang, "Si te viene mejor, pasamos a por el coche y te lo devolvemos reparado.",
           "If it suits you better, we pick the car up and bring it back repaired.")),
        (t(lang, "Te mantenemos informado", "We keep you posted"),
         t(lang, "Sabes en todo momento en qué punto está la reparación.",
           "You always know what stage the repair is at.")),
    ]
    return seccion(f"""  <div class="grid g2" style="align-items:start;gap:44px">
    <div>
      <span class="eyebrow-dark">{t(lang, "Lo que debes saber", "Good to know")}</span>
      <h2>{t(lang, "Trabajamos con tu compañía de seguros", "We work with your insurance company")}</h2>
      <p style="color:var(--muted)">{md(t(lang, "Si tu coche ha sufrido un [[siniestro|siniestro]] cubierto por el seguro, no tienes que hacer de intermediario: nos coordinamos con tu aseguradora y con su [[perito|perito]] para que la reparación se autorice y se haga bien.", "If your car has suffered an [[siniestro|incident]] covered by your insurance, you don't have to be the go-between: we coordinate with your insurer and its [[perito|loss adjuster]] so the repair is authorised and done properly."), lang)}</p>
      <p style="color:var(--muted)">{t(lang, "Es una de las razones por las que muchos clientes nos buscan: menos gestiones, menos llamadas y el coche de vuelta como tiene que estar.", "It's one of the reasons many customers come to us: less paperwork, fewer phone calls and the car back the way it should be.")}</p>{btn}
    </div>
    {checks_titulados(items, lang)}
  </div>
""", "alt")


def mitos(lang, clase="alt"):
    M = [
        (t(lang, "«Un coche que ha tenido un accidente nunca vuelve a quedar bien.»", "“A car that's been in an accident is never right again.”"),
         t(lang, "Si la estructura se devuelve a sus medidas en bancada y las uniones, sellados y protecciones se reproducen como en fábrica, la reparación queda correcta y segura.",
           "If the structure is brought back to its measurements on a jig and joints, sealing and protection are reproduced as at the factory, the repair is sound and safe.")),
        (t(lang, "«La aseguradora decide dónde se repara mi coche.»", "“My insurer decides where my car is repaired.”"),
         t(lang, "Por regla general puedes elegir taller. Algunas pólizas ofrecen ventajas en sus talleres concertados: te ayudamos a leer la tuya antes de decidir.",
           "As a rule you can choose the garage. Some policies offer perks at their partner garages: we help you read yours before you decide.")),
        (t(lang, "«Un golpe pequeño puede esperar.»", "“A small dent can wait.”"),
         t(lang, "Un roce que levanta la pintura deja la chapa expuesta. Con el sol y el salitre del sur de la isla, la corrosión avanza antes de lo que parece.",
           "A scrape that lifts the paint leaves bare metal exposed. With the sun and salty air in the south of the island, corrosion sets in sooner than you think.")),
        (t(lang, "«La pintura ecológica es de peor calidad.»", "“Eco-friendly paint is lower quality.”"),
         t(lang, "Una pintura con menos disolventes puede dar un acabado igual de duradero. Lo que marca la diferencia es la preparación y la aplicación.",
           "A paint with fewer solvents can give an equally durable finish. What makes the difference is the preparation and the application.")),
        (t(lang, "«Un coche de segunda mano con buena pinta no ha tenido golpes.»", "“A used car that looks good has never been in a crash.”"),
         t(lang, "Un repintado bien pulido puede pasar desapercibido a simple vista. Un medidor de espesores y una revisión de holguras, sellados y soldaduras lo delatan.",
           "A well-polished respray can go unnoticed at first glance. A paint thickness gauge and a check of panel gaps, sealing and welds give it away.")),
        (t(lang, "«Da igual dónde se pinte: pintura es pintura.»", "“It doesn't matter where it's painted: paint is paint.”"),
         t(lang, "Lo que no se ve —preparación de fondos, protección anticorrosiva y pintado en cabina— es lo que decide cuánto dura la reparación.",
           "What you can't see —surface preparation, anti-corrosion protection and painting in a booth— is what decides how long the repair lasts.")),
    ]
    items = "".join(f'<div class="mito"><p class="mito-falso">{esc(a)}</p><p class="mito-real">{esc(b)}</p></div>' for a, b in M)
    return seccion(section_head(
        t(lang, "Lo que se suele creer y lo que de verdad ocurre", "What people often believe, and what actually happens"),
        t(lang, "Seis ideas que oímos a menudo en el taller y que conviene aclarar.", "Six ideas we often hear at the garage that are worth clearing up."),
        lang, t(lang, "Pensamientos equivocados", "Common misconceptions"))
        + f'  <div class="grid g3">{items}</div>\n', clase)


# ---------------------------------------------------------------- Formularios
def formulario(lang, tipo="contacto", servicio_sel=None, opciones_servicio=()):
    """tipo: contacto | cita | presupuesto"""
    asunto = {
        "contacto": t(lang, "Consulta desde la web", "Enquiry from the website"),
        "cita": t(lang, "Solicitud de cita", "Appointment request"),
        "presupuesto": t(lang, "Solicitud de presupuesto", "Estimate request"),
    }[tipo]
    titulo = {
        "contacto": t(lang, "¿En qué podemos ayudarte?", "How can we help?"),
        "cita": t(lang, "Pide tu cita", "Request an appointment"),
        "presupuesto": t(lang, "Pide tu presupuesto", "Request an estimate"),
    }[tipo]
    intro = {
        "contacto": t(lang, "Rellena el formulario y te respondemos lo antes posible.", "Fill in the form and we'll get back to you as soon as possible."),
        "cita": t(lang, "Dinos qué necesita tu coche y cuándo te viene bien. Te llamamos para confirmar la cita.", "Tell us what your car needs and when suits you. We'll call you to confirm."),
        "presupuesto": t(lang, "Cuéntanos qué le pasa al coche. Si es chapa o pintura, las fotos por WhatsApp nos ayudan mucho.", "Tell us what's wrong with the car. For bodywork or paint, photos via WhatsApp help a lot."),
    }[tipo]
    L = lambda es, en: t(lang, es, en)
    opts = "".join(
        f"<option{' selected' if o == servicio_sel else ''}>{esc(o)}</option>" for o in opciones_servicio)
    campos = f"""    <div class="row2">
      <div class="field"><label for="nombre">{L("Nombre y apellidos", "Full name")}</label><input id="nombre" name="nombre" data-label="{L("Nombre", "Name")}" required></div>
      <div class="field"><label for="tel">{L("Teléfono", "Phone")}</label><input id="tel" name="telefono" type="tel" data-label="{L("Teléfono", "Phone")}" required></div>
    </div>
    <div class="field"><label for="email">{L("Correo electrónico", "Email")}</label><input id="email" name="email" type="email" data-label="{L("Correo", "Email")}" required></div>
"""
    if tipo in ("cita", "presupuesto"):
        campos += f"""    <div class="row2">
      <div class="field"><label for="vehiculo">{L("Marca y modelo", "Make and model")}</label><input id="vehiculo" name="vehiculo" data-label="{L("Vehículo", "Vehicle")}" placeholder="{L("Ej.: Toyota Corolla", "e.g. Toyota Corolla")}"></div>
      <div class="field"><label for="matricula">{L("Matrícula", "Registration")}</label><input id="matricula" name="matricula" data-label="{L("Matrícula", "Registration")}"></div>
    </div>
"""
    campos += f"""    <div class="field"><label for="servicio">{L("¿Qué necesitas?", "What do you need?")}</label>
      <select id="servicio" name="servicio" data-label="{L("Servicio", "Service")}"><option value="">{L("Selecciona una opción", "Choose an option")}</option>{opts}</select>
    </div>
"""
    if tipo == "cita":
        campos += f"""    <div class="row2">
      <div class="field"><label for="fecha">{L("Día preferido", "Preferred day")}</label><input id="fecha" name="fecha" type="date" data-label="{L("Día preferido", "Preferred day")}"></div>
      <div class="field"><label for="franja">{L("Franja horaria", "Time slot")}</label><select id="franja" name="franja" data-label="{L("Franja", "Time slot")}"><option>{L("Indiferente", "Any time")}</option><option>07:00 – 10:00</option><option>10:00 – 13:00</option><option>13:00 – 16:00</option></select></div>
    </div>
    <label class="check-linea"><input type="checkbox" name="recogida" data-label="{L("Recogida y entrega a domicilio", "Collection and delivery")}"> <span>{L("Quiero que recojáis y entreguéis el coche a domicilio", "I'd like you to collect and deliver the car")}</span></label>
"""
    if tipo == "presupuesto":
        campos += f"""    <label class="check-linea"><input type="checkbox" name="seguro" data-label="{L("Reparación a cargo del seguro", "Repair covered by insurance")}"> <span>{L("La reparación la cubre mi seguro", "My insurance covers the repair")}</span></label>
"""
    campos += f"""    <div class="field"><label for="msg">{L("Cuéntanos", "Tell us more")}</label><textarea id="msg" name="mensaje" placeholder="{L("Qué le pasa al coche, desde cuándo, dónde está el golpe, cómo ocurrió…", "What happened, where the damage is, since when…")}"></textarea></div>
    <label class="consent"><input type="checkbox" name="consent" required> <span>{L("He leído y acepto la", "I have read and accept the")} <a href="politica-de-privacidad.html">{L("política de privacidad", "privacy policy")}</a> {L("y el tratamiento de mis datos para responder a esta solicitud.", "and the processing of my data to answer this request.")}</span></label>
    <button class="btn btn-primary" type="submit">{ico("mail")}{L("Enviar solicitud", "Send request")}</button>
    <p class="form-msg">{L("Se abrirá tu programa de correo con la solicitud ya redactada. Si no ocurre nada, escríbenos a", "Your email program will open with the request ready to send. If nothing happens, write to us at")} <a href="mailto:{E["email"]}">{E["email"]}</a>.</p>
"""
    return f"""<div class="card form-card" id="escribenos">
  <span class="eyebrow-dark">{L("Te atiende el equipo del taller", "Our workshop team will reply")}</span>
  <h2 style="font-size:24px">{titulo}</h2>
  <p style="color:var(--muted);font-size:15px">{intro}</p>
  <form class="contact" data-to="{E["email"]}" data-asunto="{esc(asunto)}" action="mailto:{E["email"]}" method="post" enctype="text/plain">
{campos}  </form>
  <div class="note" style="margin-top:18px"><p>{L("¿Prefieres hablar? Llámanos al", "Rather talk? Call us on")} <a href="tel:{E["telefono_tel"]}">{E["telefono"]}</a> {L("o escríbenos por WhatsApp al", "or message us on WhatsApp at")} <a href="https://wa.me/{E["whatsapp_wa"]}" target="_blank" rel="noopener">{E["whatsapp"]}</a>.</p></div>
</div>
"""


# ---------------------------------------------------------------- Plantilla
NAV = [
    ("index", "Inicio", "Home"),
    ("conocenos", "Conócenos", "About us"),
    ("servicios", "Servicios", "Services"),
    ("chapa-y-pintura", "Chapa y pintura", "Bodywork & paint"),
    ("particulares", "Particulares", "Private"),
    ("empresas-y-flotas", "Empresas", "Businesses"),
    ("aseguradoras", "Aseguradoras", "Insurers"),
    ("revision-compraventa", "Compraventa", "Buy & sell check"),
    ("coches-de-ocasion", "Ocasión", "Used cars"),
    ("siniestros", "Siniestros", "Accidents"),
    ("blog", "Blog", "Blog"),
    ("contacto", "Contacto", "Contact"),
]


def horario(lang):
    return t(lang, "L-V 07:00 – 16:00", "Mon–Fri 07:00 – 16:00")


def topbar(lang, slug):
    otro = "en" if lang == "es" else "es"
    if lang == "es":
        lang_html = (f'<a href="{slug}.html" hreflang="es" lang="es" aria-current="true">ES</a> · '
                     f'<a href="en/{slug}.html" hreflang="en" lang="en" title="English">EN</a>')
    else:
        lang_html = (f'<a href="../{slug}.html" hreflang="es" lang="es" title="Español">ES</a> · '
                     f'<a href="{slug}.html" hreflang="en" lang="en" aria-current="true">EN</a>')
    return f"""<div class="topbar"><div class="wrap">
  <div class="tb-items">
    <span>{ico("phone")}<a href="tel:{E["telefono_tel"]}">{E["telefono"]}</a> · <a href="https://wa.me/{E["whatsapp_wa"]}" target="_blank" rel="noopener">WhatsApp {E["whatsapp"]}</a></span>
    <span>{ico("mail")}<a href="mailto:{E["email"]}">{E["email"]}</a></span>
  </div>
  <div class="tb-items">
    <span>{ico("pin")}{esc(E["direccion_corta"])}</span>
    <span>{ico("clock")}{horario(lang)}</span>
    <span class="nota-google">{estrellas()}<a href="opiniones.html">{val(lang)} · {E["resenas"]} {t(lang, "opiniones", "reviews")}</a></span>
    <span class="lang">{lang_html}</span>
    <span class="social"><a href="{E["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram">{IG_SVG}</a></span>
  </div>
</div></div>
"""


ACT = ' class="active"'


def cabecera(lang, activo):
    items = "".join(
        f'<li><a href="{s}.html"{ACT if s == activo else ""}>{t(lang, es, en)}</a></li>'
        for s, es, en in NAV)
    a = "../" if lang == "en" else ""
    return f"""<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html">
    <img src="{a}assets/logo.svg" alt="Green Car Service Tenerife" width="182" height="74">
  </a>
  <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="mainNav" aria-label="{t(lang, "Abrir menú", "Open menu")}">{ico("menu")}</button>
  <nav class="main-nav" id="mainNav" aria-label="{t(lang, "Navegación principal", "Main navigation")}">
    <ul>
      {items}
      <li class="nav-mas" hidden>
        <button type="button" aria-expanded="false" aria-haspopup="true">{t(lang, "Más", "More")} {ico("chev")}</button>
        <ul class="nav-drop"></ul>
      </li>
      <li class="cta"><a class="btn btn-primary" href="pedir-cita.html">{ico("calendar")}{t(lang, "Pedir cita", "Book now")}</a></li>
    </ul>
  </nav>
</div></header>
"""


def _fl(href, icono, texto, externo=False):
    ext = ' target="_blank" rel="noopener"' if externo else ""
    return f'<li><a href="{href}"{ext}>{ico(icono)}<span>{esc(texto)}</span></a></li>'


def pie(lang):
    a = "../" if lang == "en" else ""
    L = lambda es, en: t(lang, es, en)
    contacto = "".join([
        _fl("contacto.html", "pin", f'{E["direccion"]}, {E["cp_ciudad"]}'),
        _fl(f"tel:{E['telefono_tel']}", "phone", E["telefono"]),
        _fl(f"https://wa.me/{E['whatsapp_wa']}", "whatsapp", f"WhatsApp {E['whatsapp']}", True),
        _fl(f"mailto:{E['email']}", "mail", E["email"]),
        _fl("contacto.html", "clock", L("Lunes a viernes, 07:00 – 16:00", "Monday to Friday, 07:00 – 16:00")),
    ])
    servicios = "".join([
        _fl("chapa-y-pintura.html", "spray", L("Chapa y pintura", "Bodywork & paint")),
        _fl("servicio-reparacion-tras-accidente.html", "hammer", L("Reparación tras accidente", "Accident repair")),
        _fl("particulares.html", "users", L("Particulares", "Private customers")),
        _fl("empresas-y-flotas.html", "truck", L("Empresas y flotas", "Businesses & fleets")),
        _fl("aseguradoras.html", "shield", L("Aseguradoras y peritos", "Insurers & adjusters")),
        _fl("revision-compraventa.html", "search", L("Revisión antes de comprar o vender", "Pre-purchase & pre-sale check")),
        _fl("servicio-pintura-ecologica.html", "leaf", L("Pintura ecológica", "Eco-friendly paint")),
        _fl("servicio-garantia-vitalicia-en-pintura.html", "award", L("Garantía vitalicia en pintura", "Lifetime paint warranty")),
        _fl("servicio-recogida-y-entrega.html", "truck", L("Recogida y entrega a domicilio", "Collection & delivery")),
        _fl("servicio-gestion-con-aseguradoras.html", "handshake", L("Trabajamos con tu aseguradora", "We work with your insurer")),
        _fl("coches-de-ocasion.html", "car", L("Coches de ocasión", "Used cars")),
        _fl("sostenibilidad.html", "recycle", L("Sostenibilidad", "Sustainability")),
    ])
    directo = "".join([
        _fl("pedir-cita.html", "calendar", L("Pedir cita", "Book an appointment")),
        _fl("presupuesto.html", "doc", L("Presupuesto sin compromiso", "Free estimate")),
        _fl("siniestros.html", "alert", L("¿Has tenido un accidente?", "Had an accident?")),
        _fl("telefonos-de-asistencia.html", "phone", L("Teléfonos de asistencia en carretera", "Roadside assistance numbers")),
        _fl("diccionario-de-chapa-y-pintura.html", "book", L("Diccionario de chapa y pintura", "Bodywork & paint glossary")),
        _fl("preguntas-frecuentes.html", "info", L("Preguntas frecuentes", "FAQ")),
        _fl("opiniones.html", "star", L("Opiniones de clientes", "Customer reviews")),
        _fl("blog.html", "chat", "Blog"),
        _fl("mapa-web.html", "map", L("Mapa web", "Sitemap")),
        _fl("aviso-legal.html", "info", L("Aviso legal", "Legal notice")),
        _fl("politica-de-privacidad.html", "info", L("Política de privacidad", "Privacy policy")),
        _fl("cookies.html", "info", L("Cookies", "Cookies")),
    ])
    return f"""<footer class="site"><div class="wrap">
  <div class="foot-grid">
    <div>
      <img class="foot-logo" src="{a}assets/logo-blanco.svg" alt="Green Car Service Tenerife" width="182" height="74">
      <div class="foot-social"><a class="foot-social-link" href="{E["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram">{IG_SVG}</a><a class="foot-social-link" href="https://wa.me/{E["whatsapp_wa"]}" target="_blank" rel="noopener" aria-label="WhatsApp" title="WhatsApp">{WA_SVG}</a></div>
      <p>{L("Taller de chapa y pintura en Las Chafiras, en el sur de Tenerife, desde 2019, para particulares, empresas y compañías de seguros. Un servicio integral y sostenible: más que un simple taller.", "Body and paint shop in Las Chafiras, in the south of Tenerife, since 2019, for private customers, businesses and insurers. A complete, sustainable service: more than just a garage.")}</p>
      <ul class="foot-links">{contacto}</ul>
    </div>
    <div><h4>{L("Servicios", "Services")}</h4><ul class="foot-links">{servicios}</ul></div>
    <div><h4>{L("Acceso directo", "Quick links")}</h4><ul class="foot-links">{directo}</ul></div>
  </div>
  <div class="foot-bottom">
    <p class="foot-legal-text">Copyright © {ANIO} Green Car Service Tenerife. {E["razon_social"]} · CIF {E["cif"]} · {esc(E["direccion"])}, {esc(E["cp_ciudad"])}.</p>
    <p class="foot-credit">{L("Desarrollado por", "Developed by")} Retuerto Graphic Design. Ricardo Retuerto Barrera | Spain-Germany | <a href="tel:0034922971723">0034 922 971 723</a> · <a href="tel:00493031878629">0049 30 31878629</a></p>
  </div>
</div></footer>
<button class="arriba" type="button" id="irArriba" hidden aria-label="{L("Volver arriba", "Back to top")}" title="{L("Volver arriba", "Back to top")}">{ico("up")}</button>
<a class="wa" href="https://wa.me/{E["whatsapp_wa"]}" target="_blank" rel="noopener" aria-label="{L("Escríbenos por WhatsApp", "Message us on WhatsApp")}">{WA_SVG}</a>
"""


def documento(lang, slug, titulo, descripcion, cuerpo, activo=None, og_tipo="website"):
    base = E["base_url"]
    a = "../" if lang == "en" else ""
    tit = f"{titulo} | Green Car Service Tenerife" if slug != "index" else titulo
    desc = esc(plano(descripcion))
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(tit)}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{esc(tit)}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{og_tipo}">
<meta property="og:image" content="{base}assets/og.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600&family=Playfair+Display:wght@600;700&family=Caveat:wght@600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{a}assets/styles.css">
<link rel="icon" href="{a}assets/favicon.ico" sizes="32x32">
<link rel="icon" href="{a}assets/isotipo.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{a}assets/favicon.png">
<meta name="theme-color" content="#3D8625">
<link rel="alternate" hreflang="es" href="{base}{slug}.html">
<link rel="alternate" hreflang="en" href="{base}en/{slug}.html">
<link rel="alternate" hreflang="x-default" href="{base}{slug}.html">
</head>
<body>
{topbar(lang, slug)}
{cabecera(lang, activo)}
<main>

{cuerpo}
</main>
{pie(lang)}
<script src="{a}assets/site.js"></script>
</body>
</html>
"""
