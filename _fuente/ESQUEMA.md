# Esquema de contenido — Green Car Service Tenerife

Todo el contenido vive en `_fuente/contenido/*.py` como datos Python puros (sin imports salvo nada).
Cada texto existe en español (`"es"`) y en inglés (`"en"`). Tras escribir, valida con:

    cd /home/user/greenc && python3 _fuente/validar.py NOMBRE_MODULO

## Datos reales de la empresa (NO inventes otros)
- Green Car Service Tenerife: taller de CHAPA Y PINTURA en Las Chafiras (San Miguel de Abona, sur de Tenerife). Da servicio a particulares, a empresas (flotas, vehículos comerciales, renting, rent a car) y a siniestros de compañías de seguros. También revisa coches antes de su compra o su venta (carrocería, pintura, estructura, documentación) y vende coches de segunda mano.
- **PROHIBIDO mencionar** mecánica, diagnosis/electrónica, vehículos eléctricos o híbridos, ni trabajos de motor, frenos, aceite, filtros, neumáticos, suspensión, embrague, batería, aire acondicionado, etc. El sitio habla solo de chapa, pintura, estructura/carrocería, lunas/faros/plásticos exteriores, siniestros, revisión de compraventa y las ventajas del taller.
- Empezó en 2019 con el propósito de ganarse la confianza de clientes que buscan "algo más que un simple taller". Objetivo: servicio integral y sostenible.
- Tres pilares: calidad, confianza y compromiso. Compromiso con el medio ambiente y la actividad sostenible.
- Instalaciones amplias: taller de chapa, pintura y almacén de recambios; bancadas y todo el equipamiento para trabajar con los estándares que exigen todas las marcas.
- Pintura ecológica «eco-balance», con beneficios directos para el medio ambiente. Colores sólidos y metalizados.
- Servicios: recogida y entrega a domicilio, garantía vitalicia en pintura, estado del vehículo en tiempo real. Trabajan con tu compañía de seguros. Los clientes destacan que entregan el coche limpio (por dentro también), presupuestos rápidos y vehículo de sustitución.
- También venden coches de segunda mano.
- Horario: lunes a viernes 07:00–16:00. Tel. 922 73 64 47 · WhatsApp 674 06 13 71 · info@greencarservicetenerife.com
- Dirección: Av. Siete Islas Canarias, 34, Pol. Ind. Llano del Camello, 38639 Las Chafiras.
- Valoración 4,8/5 con 177 opiniones en Google.
- Titular web: T Mas T Summerfeeling, S.L., CIF B38553269.

NO inventes: precios, marcas de pintura o de equipos, número de empleados, certificaciones, nombres de personas, aseguradoras concretas con las que trabajan, plazos garantizados, porcentajes o estadísticas. Cuando algo dependa del caso, dilo ("te lo confirmamos en el presupuesto"). Nada de promesas absolutas.
Tono: cercano y claro, tuteo (España), frases cortas, sin relleno comercial ni tecnicismos sin explicar. Inglés: natural, británico-neutro (tyre, colour), dirigido a residentes y visitantes extranjeros del sur de Tenerife.
Contexto útil: sur de Tenerife (sol intenso, salitre/ambiente marino, calima, carreteras de montaña como la TF-1 y subidas al Teide, muchos coches de alquiler y residentes extranjeros). Normativa española real se puede citar con prudencia (p. ej. Real Decreto 1457/1986 sobre talleres: derecho a presupuesto por escrito y resguardo de depósito; garantía mínima de reparaciones de 3 meses o 2.000 km; Reglamento UE 461/2010 que permite mantener el coche en un taller independiente sin perder la garantía del fabricante si se siguen sus especificaciones; baremo; parte amistoso/Declaración Amistosa de Accidente; ITV).

## Marcado dentro de los textos (NUNCA HTML)
- `[[clave|texto visible]]` → enlace al diccionario (clave de `GLOSARIO_TERMINOS` en `_fuente/comun.py`). Úsalo 2–5 veces por página, en la primera aparición del término, en entradilla/párrafos/respuestas. No en títulos.
- `[texto](pagina.html)` → enlace interno. Solo a páginas de `comun.todas_las_paginas()` (fijas, servicios, guías). NO enlaces a artículos del blog (`articulo-*`) desde otros módulos. En inglés se usa el mismo nombre de archivo.
- `**negrita**`.

## Iconos
Solo nombres de `comun.ICONOS`.

## Tipos de módulo
### SERVICIOS (fichas de servicio)
```python
SERVICIOS = [{
  "slug": "servicio-reparacion-de-chapa", "cat": "chapa-pintura", "icon": "hammer",
  "es": {
    "titulo": "Reparación de chapa",
    "corto": "Una frase (máx. ~140 caracteres) para la tarjeta del listado.",
    "entradilla": "1–2 frases bajo el H1.",
    "por_que_titulo": "Por qué ...",
    "por_que": [("icono", "Título", "Texto 1–3 frases"), ... exactamente 3],
    "incluye_titulo": "Qué incluye",
    "incluye_intro": "1–2 frases.",
    "incluye": [("icono", "Título", "Texto"), ... entre 4 y 6],
    "nota": "Una aclaración honesta (límites, depende del caso...).",
    "texto": [("h2", "Título"), ("p", "Párrafo"), ("checks", ["punto", "punto"]), ...],  # 350–600 palabras, 2–4 h2
    "faq": [("¿Pregunta?", "Respuesta 1–3 frases."), ... 4–5],
  },
  "en": { ...mismas claves... },
}]
```
### ARTICULOS (blog)
```python
ARTICULOS = [{
  "slug": "articulo-...", "cat": "mantenimiento", "fecha": "2025-03-14",  # fechas entre 2023-01 y 2026-09
  "es": {"titulo": "...", "resumen": "1–2 frases",
         "cuerpo": [("p", ...), ("h2", ...), ("ul", [..]), ("ol", [..]), ("quote", ...), ("nota", ...)]},  # 500–800 palabras
  "en": {...},
}]
```
Categorías: chapa-pintura, particulares, empresas-flotas, seguros-siniestros, compraventa, tenerife, seguridad-vial.
