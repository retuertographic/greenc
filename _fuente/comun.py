"""Datos compartidos por el generador y por los módulos de contenido.

Marcado admitido dentro de cualquier texto de contenido:
  [[termino|texto visible]]  -> enlace al diccionario con definición emergente.
                                 `termino` debe ser una clave de GLOSARIO_TERMINOS.
  [texto visible](pagina.html) -> enlace interno. `pagina` debe estar en PAGINAS
                                 (se admite un ancla: pagina.html#algo).
  **texto**                  -> negrita.
"""

EMPRESA = {
    "nombre": "Green Car Service Tenerife",
    "razon_social": "T Mas T Summerfeeling, S.L.",
    "cif": "B38553269",
    "direccion": "Avenida Siete Islas Canarias, 34, Pol. Ind. Llano del Camello",
    "cp_ciudad": "38639 Las Chafiras, San Miguel de Abona (Santa Cruz de Tenerife)",
    "direccion_corta": "Av. 7 Islas Canarias, 34 · Pol. Ind. Llano del Camello, 38639 Las Chafiras",
    "telefono": "922 73 64 47",
    "telefono_tel": "+34922736447",
    "whatsapp": "674 06 13 71",
    "whatsapp_wa": "34674061371",
    "email": "info@greencarservicetenerife.com",
    "instagram": "https://www.instagram.com/greencarservicetenerife6/",
    "web_actual": "https://www.greencarservicetenerife.com/",
    "fundacion": 2019,
    "valoracion": "4,8",
    "resenas": "177",
    "base_url": "https://retuertographic.github.io/greenc/",
}

# Iconos disponibles (nombre -> se definen en generar.py)
ICONOS = [
    "car", "wrench", "paint", "spray", "shield", "leaf", "bolt", "battery", "gauge",
    "clock", "truck", "home", "calendar", "check", "star", "phone", "mail", "pin",
    "doc", "search", "camera", "drop", "thermo", "snow", "wind", "disc", "gear",
    "key", "sparkle", "sun", "light", "eye", "euro", "users", "alert", "tool",
    "recycle", "plug", "road", "info", "chat", "layers", "hammer", "clipboard",
    "handshake", "award", "map", "filter", "steering", "exhaust", "chip",
]

# Términos del diccionario de chapa y pintura: clave -> (nombre ES, nombre EN).
# Las definiciones están en contenido/glosario.py.
GLOSARIO_TERMINOS = {
    "antigravilla": ("Antigravilla", "Stone-chip coating"),
    "aparejo": ("Aparejo", "Primer surfacer"),
    "bancada": ("Bancada", "Chassis jig"),
    "baremo": ("Baremo de reparación", "Repair time schedule"),
    "barniz": ("Barniz", "Clear coat"),
    "bicapa": ("Pintura bicapa", "Two-stage paint"),
    "cabina-de-pintura": ("Cabina de pintura", "Paint booth"),
    "carroceria": ("Carrocería", "Bodywork"),
    "cataforesis": ("Cataforesis", "Cathodic e-coat"),
    "cera-de-cavidades": ("Cera de cavidades", "Cavity wax"),
    "chasis": ("Chasis", "Chassis"),
    "codigo-de-color": ("Código de color", "Paint code"),
    "colorimetria": ("Colorimetría", "Colour matching"),
    "compuestos-organicos-volatiles": ("Compuestos orgánicos volátiles (COV)", "Volatile organic compounds (VOC)"),
    "corrosion": ("Corrosión", "Corrosion"),
    "corrosion-galvanica": ("Corrosión galvánica", "Galvanic corrosion"),
    "desabollado-sin-pintura": ("Desabollado sin pintura", "Paintless dent repair"),
    "difuminado": ("Difuminado", "Blending"),
    "enmascarado": ("Enmascarado", "Masking"),
    "estructura-deformable": ("Estructura de deformación programada", "Crumple zone"),
    "flota": ("Flota de vehículos", "Vehicle fleet"),
    "franquicia": ("Franquicia", "Excess"),
    "galvanizado": ("Galvanizado", "Galvanising"),
    "garantia-de-reparacion": ("Garantía de la reparación", "Repair warranty"),
    "hoja-de-reclamaciones": ("Hoja de reclamaciones", "Complaints form"),
    "imprimacion": ("Imprimación", "Primer"),
    "informe-dgt": ("Informe de vehículo de la DGT", "DGT vehicle report"),
    "itv": ("ITV", "ITV (MOT)"),
    "libre-eleccion-de-taller": ("Libre elección de taller", "Free choice of repairer"),
    "lijado": ("Lijado", "Sanding"),
    "masilla": ("Masilla", "Body filler"),
    "matizado": ("Matizado", "Keying (scuffing)"),
    "medidor-de-espesores": ("Medidor de espesores de pintura", "Paint thickness gauge"),
    "metalizado": ("Pintura metalizada", "Metallic paint"),
    "monocapa": ("Pintura monocapa", "Single-stage paint"),
    "nacarado": ("Pintura nacarada o perlada", "Pearlescent paint"),
    "orden-de-reparacion": ("Orden de reparación", "Repair order"),
    "paragolpes": ("Paragolpes", "Bumper"),
    "parte-amistoso": ("Parte amistoso", "Accident report form"),
    "perdida-total": ("Pérdida total", "Total loss"),
    "peritacion": ("Peritación", "Loss assessment"),
    "perito": ("Perito", "Loss adjuster"),
    "piel-de-naranja": ("Piel de naranja", "Orange peel"),
    "pintura-al-agua": ("Pintura al agua", "Water-based paint"),
    "presupuesto": ("Presupuesto de reparación", "Repair estimate"),
    "promotor-de-adherencia": ("Promotor de adherencia", "Adhesion promoter"),
    "pulido": ("Pulido", "Polishing"),
    "recambio-de-calidad-equivalente": ("Recambio de calidad equivalente", "Equivalent-quality part"),
    "recambio-original": ("Recambio original", "Original part"),
    "remachado": ("Remachado", "Riveting"),
    "renting": ("Renting", "Leasing (renting)"),
    "resguardo-de-deposito": ("Resguardo de depósito", "Vehicle deposit receipt"),
    "sellador": ("Sellador", "Seam sealer"),
    "siniestro": ("Siniestro", "Claim event"),
    "soldadura-por-puntos": ("Soldadura por puntos", "Spot welding"),
    "terceros": ("Seguro a terceros", "Third-party insurance"),
    "todo-riesgo": ("Seguro a todo riesgo", "Comprehensive insurance"),
    "valor-venal": ("Valor venal", "Pre-accident value"),
    "vehiculo-de-sustitucion": ("Vehículo de sustitución", "Courtesy car"),
}

# Categorías de servicio: clave -> (página hub, nombre ES, nombre EN)
CATEGORIAS_SERVICIO = {
    "chapa-pintura": ("chapa-y-pintura.html", "Chapa y pintura", "Bodywork & paint"),
    "revision": ("revision-compraventa.html", "Revisión para compraventa", "Pre-sale & pre-purchase inspection"),
    "clientes": ("a-quien-servimos.html", "A quién damos servicio", "Who we work for"),
    "ventajas": ("ventajas.html", "Ventajas Green Car", "Why Green Car"),
}

SERVICIOS_SLUGS = {
    "chapa-pintura": [
        "servicio-reparacion-de-chapa", "servicio-golpes-y-abolladuras",
        "servicio-reparacion-tras-accidente", "servicio-bancada-y-estructura",
        "servicio-pintura-completa", "servicio-pintura-parcial",
        "servicio-colores-y-acabados", "servicio-pintura-ecologica",
        "servicio-paragolpes-y-plasticos", "servicio-pulido-y-abrillantado",
        "servicio-restauracion-de-faros", "servicio-tratamiento-anticorrosion",
    ],
    "revision": [
        "revision-antes-de-comprar", "revision-antes-de-vender",
        "informe-de-carroceria-y-pintura", "puesta-a-punto-para-vender",
    ],
    "clientes": [
        "particulares", "empresas-y-flotas", "aseguradoras",
    ],
    "ventajas": [
        "servicio-recogida-y-entrega", "servicio-garantia-vitalicia-en-pintura",
        "servicio-estado-en-tiempo-real", "servicio-vehiculo-de-sustitucion",
        "servicio-gestion-con-aseguradoras", "servicio-presupuesto-sin-compromiso",
        "servicio-limpieza-del-vehiculo",
    ],
}

# Categorías del blog: clave -> (nombre ES, nombre EN)
CATEGORIAS_BLOG = {
    "chapa-pintura": ("Chapa y pintura", "Bodywork & paint"),
    "particulares": ("Particulares", "Private customers"),
    "empresas-flotas": ("Empresas y flotas", "Businesses & fleets"),
    "seguros-siniestros": ("Seguros y siniestros", "Insurance & claims"),
    "compraventa": ("Comprar y vender", "Buying & selling"),
    "tenerife": ("Tu coche en Tenerife", "Your car in Tenerife"),
    "seguridad-vial": ("Seguridad vial", "Road safety"),
}

GUIAS_SLUGS = [
    "guia-que-hacer-tras-un-accidente", "guia-parte-amistoso",
    "guia-libre-eleccion-de-taller", "guia-peritacion", "guia-perdida-total",
    "guia-comprar-coche-de-ocasion",
]

PAGINAS_FIJAS = [
    "index", "conocenos", "instalaciones", "sostenibilidad", "opiniones", "servicios",
    "chapa-y-pintura", "revision-compraventa", "a-quien-servimos", "ventajas", "siniestros", "telefonos-de-asistencia", "coches-de-ocasion", "blog",
    "diccionario-de-chapa-y-pintura", "preguntas-frecuentes", "pedir-cita", "presupuesto",
    "contacto", "mapa-web", "legal", "aviso-legal", "politica-de-privacidad", "cookies",
] + ["categoria-" + c for c in CATEGORIAS_BLOG]


def todas_las_paginas(articulos=()):
    """Nombres de archivo (sin .html) de todo el sitio."""
    p = list(PAGINAS_FIJAS) + list(GUIAS_SLUGS)
    for lista in SERVICIOS_SLUGS.values():
        p += lista
    p += [a for a in articulos]
    return p
