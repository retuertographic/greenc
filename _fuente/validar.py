"""Comprueba que los módulos de contenido cumplen el esquema.

Uso: python3 _fuente/validar.py [modulo ...]   (sin argumentos: todos)
"""
import importlib, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from comun import (ICONOS, GLOSARIO_TERMINOS, SERVICIOS_SLUGS, CATEGORIAS_BLOG,
                   GUIAS_SLUGS, todas_las_paginas)

CONT = os.path.join(os.path.dirname(__file__), "contenido")
errores = []


def err(donde, msg):
    errores.append(f"{donde}: {msg}")


def cargar(nombre):
    try:
        return importlib.import_module("contenido." + nombre)
    except FileNotFoundError:
        return None


def articulos_definidos():
    slugs = []
    for f in sorted(os.listdir(CONT)):
        if f.startswith("articulos") and f.endswith(".py"):
            m = importlib.import_module("contenido." + f[:-3])
            slugs += [a["slug"] for a in m.ARTICULOS]
    return slugs


PAGS = None


def revisar_texto(donde, t):
    if not isinstance(t, str):
        err(donde, f"se esperaba texto, hay {type(t).__name__}")
        return
    for m in re.finditer(r"\[\[([^\]|]+)\|([^\]]+)\]\]", t):
        if m.group(1) not in GLOSARIO_TERMINOS:
            err(donde, f"término de glosario desconocido: {m.group(1)}")
    resto = re.sub(r"\[\[[^\]]+\]\]", "", t)
    if "[[" in resto or "]]" in resto:
        err(donde, "marcado [[...]] mal formado")
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", resto):
        destino = m.group(2)
        if destino.startswith(("http://", "https://", "tel:", "mailto:")):
            continue
        pag = destino.split("#")[0]
        if not pag.endswith(".html") or pag[:-5] not in PAGS:
            err(donde, f"enlace interno a página inexistente: {destino}")
    if re.search(r"</?[a-z][^>]*>", t):
        err(donde, "no uses HTML en el contenido; usa el marcado del esquema")


def revisar_bloques(donde, bloques, tipos):
    if not isinstance(bloques, list) or not bloques:
        err(donde, "lista de bloques vacía o no es lista")
        return
    for i, b in enumerate(bloques):
        if not (isinstance(b, tuple) and len(b) == 2 and b[0] in tipos):
            err(f"{donde}[{i}]", f"bloque debe ser (tipo, valor) con tipo en {tipos}")
            continue
        if isinstance(b[1], list):
            for j, x in enumerate(b[1]):
                revisar_texto(f"{donde}[{i}][{j}]", x)
        else:
            revisar_texto(f"{donde}[{i}]", b[1])


def revisar_tarjetas(donde, lista, minimo, maximo):
    if not (minimo <= len(lista) <= maximo):
        err(donde, f"se esperaban entre {minimo} y {maximo} elementos, hay {len(lista)}")
    for i, c in enumerate(lista):
        if not (isinstance(c, tuple) and len(c) == 3):
            err(f"{donde}[{i}]", "debe ser (icono, titulo, texto)")
            continue
        if c[0] not in ICONOS:
            err(f"{donde}[{i}]", f"icono desconocido: {c[0]}")
        revisar_texto(f"{donde}[{i}]", c[1])
        revisar_texto(f"{donde}[{i}]", c[2])


def revisar_faq(donde, faq, minimo=3):
    if len(faq) < minimo:
        err(donde, f"al menos {minimo} preguntas")
    for i, qa in enumerate(faq):
        if not (isinstance(qa, tuple) and len(qa) == 2):
            err(f"{donde}[{i}]", "debe ser (pregunta, respuesta)")
            continue
        revisar_texto(f"{donde}[{i}]", qa[0])
        revisar_texto(f"{donde}[{i}]", qa[1])


CLAVES_SERV = ["titulo", "corto", "entradilla", "por_que_titulo", "por_que",
               "incluye_titulo", "incluye_intro", "incluye", "nota", "texto", "faq"]


def revisar_servicios(mod, nombre):
    todos = {s for l in SERVICIOS_SLUGS.values() for s in l}
    for s in mod.SERVICIOS:
        d = f"{nombre}:{s.get('slug')}"
        if s.get("slug") not in todos:
            err(d, "slug no previsto en comun.SERVICIOS_SLUGS")
        elif s["slug"] not in SERVICIOS_SLUGS.get(s.get("cat"), []):
            err(d, "categoría no coincide con comun.SERVICIOS_SLUGS")
        if s.get("icon") not in ICONOS:
            err(d, f"icono desconocido: {s.get('icon')}")
        for lang in ("es", "en"):
            L = s.get(lang, {})
            for k in CLAVES_SERV:
                if k not in L:
                    err(f"{d}:{lang}", f"falta la clave {k}")
            if any(k not in L for k in CLAVES_SERV):
                continue
            for k in ("titulo", "corto", "entradilla", "por_que_titulo",
                      "incluye_titulo", "incluye_intro", "nota"):
                revisar_texto(f"{d}:{lang}:{k}", L[k])
            revisar_tarjetas(f"{d}:{lang}:por_que", L["por_que"], 3, 3)
            revisar_tarjetas(f"{d}:{lang}:incluye", L["incluye"], 4, 6)
            revisar_bloques(f"{d}:{lang}:texto", L["texto"], ("h2", "p", "checks"))
            revisar_faq(f"{d}:{lang}:faq", L["faq"], 4)


def revisar_articulos(mod, nombre):
    for a in mod.ARTICULOS:
        d = f"{nombre}:{a.get('slug')}"
        if not str(a.get("slug", "")).startswith("articulo-"):
            err(d, "el slug debe empezar por articulo-")
        if a.get("cat") not in CATEGORIAS_BLOG:
            err(d, f"categoría desconocida {a.get('cat')}")
        if not re.fullmatch(r"20\d\d-\d\d-\d\d", str(a.get("fecha", ""))):
            err(d, "fecha AAAA-MM-DD")
        for lang in ("es", "en"):
            L = a.get(lang, {})
            for k in ("titulo", "resumen", "cuerpo"):
                if k not in L:
                    err(f"{d}:{lang}", f"falta {k}")
            if "cuerpo" in L:
                revisar_texto(f"{d}:{lang}:titulo", L["titulo"])
                revisar_texto(f"{d}:{lang}:resumen", L["resumen"])
                revisar_bloques(f"{d}:{lang}:cuerpo", L["cuerpo"],
                                ("h2", "p", "ul", "ol", "quote", "nota"))


def revisar_glosario(mod, nombre):
    G = mod.GLOSARIO
    for k in GLOSARIO_TERMINOS:
        if k not in G:
            err(nombre, f"falta la definición de {k}")
    for k, v in G.items():
        if k not in GLOSARIO_TERMINOS:
            err(nombre, f"término no previsto: {k}")
        for lang in ("es", "en"):
            if lang not in v:
                err(f"{nombre}:{k}", f"falta {lang}")
            elif "[[" in v[lang]:
                err(f"{nombre}:{k}", "las definiciones no llevan enlaces al glosario")
            else:
                revisar_texto(f"{nombre}:{k}:{lang}", v[lang])


def revisar_guias(mod, nombre):
    for g in mod.GUIAS:
        d = f"{nombre}:{g.get('slug')}"
        if g.get("slug") not in GUIAS_SLUGS:
            err(d, "slug no previsto en comun.GUIAS_SLUGS")
        if g.get("icon") not in ICONOS:
            err(d, "icono desconocido")
        for lang in ("es", "en"):
            L = g.get(lang, {})
            for k in ("titulo", "corto", "entradilla", "texto", "faq"):
                if k not in L:
                    err(f"{d}:{lang}", f"falta {k}")
            if "texto" in L:
                revisar_bloques(f"{d}:{lang}:texto", L["texto"],
                                ("h2", "p", "checks", "ol", "nota"))
                revisar_faq(f"{d}:{lang}:faq", L["faq"], 3)
                for k in ("titulo", "corto", "entradilla"):
                    revisar_texto(f"{d}:{lang}:{k}", L[k])


def revisar_faq_general(mod, nombre):
    for bloque in mod.FAQ:
        for lang in ("es", "en"):
            revisar_texto(f"{nombre}:{lang}", bloque[lang]["titulo"])
            revisar_faq(f"{nombre}:{bloque['id']}:{lang}", bloque[lang]["preguntas"], 3)


def revisar_legal(mod, nombre):
    for slug, doc in mod.LEGAL.items():
        if slug not in ("aviso-legal", "politica-de-privacidad", "cookies"):
            err(nombre, f"documento no previsto {slug}")
        for lang in ("es", "en"):
            L = doc[lang]
            for k in ("titulo", "entradilla", "secciones"):
                if k not in L:
                    err(f"{nombre}:{slug}:{lang}", f"falta {k}")
            for i, sec in enumerate(L.get("secciones", [])):
                if not (isinstance(sec, tuple) and len(sec) == 2):
                    err(f"{nombre}:{slug}:{lang}:{i}", "sección = (titulo, bloques)")
                    continue
                revisar_texto(f"{nombre}:{slug}:{lang}:{i}", sec[0])
                revisar_bloques(f"{nombre}:{slug}:{lang}:{i}", sec[1],
                                ("h3", "p", "ul", "tabla"))


def main():
    global PAGS
    sys.path.insert(0, os.path.dirname(__file__))
    PAGS = set(todas_las_paginas(articulos_definidos()))
    nombres = sys.argv[1:] or [f[:-3] for f in sorted(os.listdir(CONT))
                               if f.endswith(".py") and f != "__init__.py"]
    for n in nombres:
        mod = importlib.import_module("contenido." + n)
        if hasattr(mod, "SERVICIOS"): revisar_servicios(mod, n)
        if hasattr(mod, "ARTICULOS"): revisar_articulos(mod, n)
        if hasattr(mod, "GLOSARIO"): revisar_glosario(mod, n)
        if hasattr(mod, "GUIAS"): revisar_guias(mod, n)
        if hasattr(mod, "FAQ"): revisar_faq_general(mod, n)
        if hasattr(mod, "LEGAL"): revisar_legal(mod, n)
    if errores:
        print("\n".join(errores))
        print(f"\n{len(errores)} errores")
        sys.exit(1)
    print("OK:", ", ".join(nombres))


if __name__ == "__main__":
    main()
