# Green Car Service Tenerife — Taller de chapa, pintura y mecánica

Sitio web estático y bilingüe de Green Car Service Tenerife (105 páginas en español y 105 en inglés), con la estructura y la maquetación del sitio de Retuerto y Asociados: inicio, empresa, servicios por especialidad con fichas detalladas, siniestros y guías, teléfonos de asistencia, coches de ocasión, blog, diccionario del motor, preguntas frecuentes, formularios de cita y presupuesto y páginas legales.

- `*.html` — versión en español (raíz del sitio).
- `en/*.html` — versión en inglés, con los mismos nombres de archivo.
- `assets/` — estilos, script y logotipos (SVG) compartidos. `site.js` adapta sus textos al idioma de la página (`<html lang>`).
- Cada página enlaza a su equivalente con el selector ES · EN de la barra superior y con `hreflang`. Incluye `sitemap.xml` y `robots.txt`.
- Publicado con GitHub Pages (Deploy from a branch) en https://retuertographic.github.io/greenc/ y https://retuertographic.github.io/greenc/en/

## Cómo editar

Las páginas se generan; no se editan a mano.

- `_fuente/comun.py` — datos de la empresa (teléfonos, dirección, horario…), listas de páginas y términos del diccionario.
- `_fuente/contenido/*.py` — textos (ES/EN): fichas de servicio, artículos del blog, guías, glosario, FAQ y textos legales. El marcado admitido se explica en `_fuente/ESQUEMA.md`.
- `_fuente/generar.py` y `_fuente/nucleo.py` — plantillas.

```
python3 _fuente/validar.py    # comprueba el contenido
python3 _fuente/generar.py    # regenera todas las páginas
```
