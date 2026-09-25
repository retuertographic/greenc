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

# Términos del diccionario del automóvil: clave -> (nombre ES, nombre EN).
# Las definiciones están en contenido/glosario.py.
GLOSARIO_TERMINOS = {
    "abs": ("ABS", "ABS"),
    "adas": ("ADAS", "ADAS"),
    "airbag": ("Airbag", "Airbag"),
    "aire-acondicionado": ("Aire acondicionado", "Air conditioning"),
    "alineacion": ("Alineación de la dirección", "Wheel alignment"),
    "amortiguador": ("Amortiguador", "Shock absorber"),
    "anticongelante": ("Anticongelante / refrigerante", "Antifreeze / coolant"),
    "bancada": ("Bancada", "Chassis jig"),
    "barniz": ("Barniz", "Clear coat"),
    "bateria-12v": ("Batería de 12 voltios", "12-volt battery"),
    "bateria-alta-tension": ("Batería de alta tensión", "High-voltage battery"),
    "bujia": ("Bujía", "Spark plug"),
    "cabina-de-pintura": ("Cabina de pintura", "Paint booth"),
    "calibrado-adas": ("Calibrado de ADAS", "ADAS calibration"),
    "carroceria": ("Carrocería", "Bodywork"),
    "catalizador": ("Catalizador", "Catalytic converter"),
    "centralita": ("Centralita (ECU)", "Engine control unit (ECU)"),
    "chasis": ("Chasis", "Chassis"),
    "colorimetria": ("Colorimetría", "Colour matching"),
    "compuestos-organicos-volatiles": ("Compuestos orgánicos volátiles (COV)", "Volatile organic compounds (VOC)"),
    "correa-auxiliar": ("Correa auxiliar", "Auxiliary belt"),
    "correa-de-distribucion": ("Correa de distribución", "Timing belt"),
    "corrosion": ("Corrosión", "Corrosion"),
    "desabollado-sin-pintura": ("Desabollado sin pintura", "Paintless dent repair"),
    "diagnosis-obd": ("Diagnosis OBD", "OBD diagnostics"),
    "disco-de-freno": ("Disco de freno", "Brake disc"),
    "embrague": ("Embrague", "Clutch"),
    "filtro-de-aceite": ("Filtro de aceite", "Oil filter"),
    "filtro-de-aire": ("Filtro de aire", "Air filter"),
    "filtro-de-habitaculo": ("Filtro de habitáculo", "Cabin filter"),
    "filtro-de-particulas": ("Filtro de partículas (FAP)", "Diesel particulate filter (DPF)"),
    "franquicia": ("Franquicia", "Excess"),
    "frenada-regenerativa": ("Frenada regenerativa", "Regenerative braking"),
    "garantia-de-reparacion": ("Garantía de la reparación", "Repair warranty"),
    "hibrido": ("Híbrido", "Hybrid"),
    "hibrido-enchufable": ("Híbrido enchufable (PHEV)", "Plug-in hybrid (PHEV)"),
    "hoja-de-reclamaciones": ("Hoja de reclamaciones", "Complaints form"),
    "imprimacion": ("Imprimación", "Primer"),
    "inyector": ("Inyector", "Injector"),
    "itv": ("ITV", "ITV (MOT)"),
    "libre-eleccion-de-taller": ("Libre elección de taller", "Free choice of repairer"),
    "liquido-de-frenos": ("Líquido de frenos", "Brake fluid"),
    "masilla": ("Masilla", "Body filler"),
    "metalizado": ("Pintura metalizada", "Metallic paint"),
    "nacarado": ("Pintura nacarada o perlada", "Pearlescent paint"),
    "neumatico": ("Neumático", "Tyre"),
    "parte-amistoso": ("Parte amistoso", "Accident report form"),
    "pastillas-de-freno": ("Pastillas de freno", "Brake pads"),
    "perdida-total": ("Pérdida total", "Total loss"),
    "peritacion": ("Peritación", "Loss assessment"),
    "perito": ("Perito", "Loss adjuster"),
    "pintura-al-agua": ("Pintura al agua", "Water-based paint"),
    "presupuesto": ("Presupuesto de reparación", "Repair estimate"),
    "pulido": ("Pulido", "Polishing"),
    "recambio-original": ("Recambio original", "Original part"),
    "recambio-de-calidad-equivalente": ("Recambio de calidad equivalente", "Equivalent-quality part"),
    "resguardo-de-deposito": ("Resguardo de depósito", "Vehicle deposit receipt"),
    "rotula": ("Rótula", "Ball joint"),
    "silentblock": ("Silentblock", "Bushing (silentblock)"),
    "siniestro": ("Siniestro", "Claim event"),
    "sonda-lambda": ("Sonda lambda", "Lambda sensor"),
    "suspension": ("Suspensión", "Suspension"),
    "terceros": ("Seguro a terceros", "Third-party insurance"),
    "testigo-de-averia": ("Testigo de avería", "Warning light"),
    "todo-riesgo": ("Seguro a todo riesgo", "Comprehensive insurance"),
    "turbo": ("Turbocompresor", "Turbocharger"),
    "valvula-egr": ("Válvula EGR", "EGR valve"),
    "vehiculo-de-sustitucion": ("Vehículo de sustitución", "Courtesy car"),
    "vehiculo-electrico": ("Vehículo eléctrico", "Electric vehicle"),
    "volante-bimasa": ("Volante bimasa", "Dual-mass flywheel"),
    "conector-de-recarga": ("Conector de recarga", "Charging connector"),
    "orden-de-reparacion": ("Orden de reparación", "Repair order"),
}

# Categorías de servicios: clave -> (página hub, nombre ES, nombre EN)
CATEGORIAS_SERVICIO = {
    "chapa-pintura": ("chapa-y-pintura.html", "Chapa y pintura", "Bodywork & paint"),
    "mecanica": ("mecanica.html", "Mecánica", "Mechanics"),
    "diagnosis": ("diagnosis-y-electronica.html", "Diagnosis y electrónica", "Diagnostics & electronics"),
    "electricos": ("electricos-e-hibridos.html", "Eléctricos e híbridos", "Electric & hybrid"),
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
    "mecanica": [
        "servicio-mecanica-general", "servicio-revision-y-mantenimiento",
        "servicio-cambio-de-aceite-y-filtros", "servicio-frenos",
        "servicio-suspension-y-direccion", "servicio-embrague-y-transmision",
        "servicio-distribucion", "servicio-aire-acondicionado", "servicio-pre-itv",
        "servicio-escape-y-emisiones", "servicio-refrigeracion-del-motor",
    ],
    "diagnosis": [
        "servicio-diagnosis-electronica", "servicio-electricidad-del-automovil",
        "servicio-baterias-y-arranque", "servicio-testigos-de-averia",
    ],
    "electricos": [
        "servicio-reparacion-de-vehiculos-electricos", "servicio-mantenimiento-de-electricos",
        "servicio-hibridos-e-hibridos-enchufables", "servicio-chapa-y-pintura-en-electricos",
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
    "mantenimiento": ("Mantenimiento", "Maintenance"),
    "chapa-pintura": ("Chapa y pintura", "Bodywork & paint"),
    "electricos": ("Eléctricos e híbridos", "Electric & hybrid"),
    "seguridad-vial": ("Seguridad vial", "Road safety"),
    "seguros-siniestros": ("Seguros y siniestros", "Insurance & claims"),
    "tenerife": ("Conducir en Tenerife", "Driving in Tenerife"),
}

GUIAS_SLUGS = [
    "guia-que-hacer-tras-un-accidente", "guia-parte-amistoso",
    "guia-libre-eleccion-de-taller", "guia-peritacion", "guia-perdida-total",
    "guia-comprar-coche-de-ocasion",
]

PAGINAS_FIJAS = [
    "index", "conocenos", "instalaciones", "sostenibilidad", "opiniones", "servicios",
    "chapa-y-pintura", "mecanica", "diagnosis-y-electronica", "electricos-e-hibridos",
    "ventajas", "siniestros", "telefonos-de-asistencia", "coches-de-ocasion", "blog",
    "diccionario-del-motor", "preguntas-frecuentes", "pedir-cita", "presupuesto",
    "contacto", "mapa-web", "legal", "aviso-legal", "politica-de-privacidad", "cookies",
] + ["categoria-" + c for c in CATEGORIAS_BLOG]


def todas_las_paginas(articulos=()):
    """Nombres de archivo (sin .html) de todo el sitio."""
    p = list(PAGINAS_FIJAS) + list(GUIAS_SLUGS)
    for lista in SERVICIOS_SLUGS.values():
        p += lista
    p += [a for a in articulos]
    return p
