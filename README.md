# Green Car Service Tenerife — Taller de chapa y pintura

Sitio web estático y bilingüe de Green Car Service Tenerife (104 páginas en español y 104 en inglés), con la estructura y la maquetación del sitio de Retuerto y Asociados: inicio, empresa, fichas de chapa y pintura, páginas para particulares, empresas y flotas y aseguradoras, revisión de coches antes de comprar o vender, siniestros y guías, teléfonos de asistencia, coches de ocasión, blog (41 artículos), diccionario de chapa y pintura, preguntas frecuentes, formularios de cita y presupuesto y páginas legales.

- `*.html` — versión en español (raíz del sitio).
- `en/*.html` — versión en inglés, con los mismos nombres de archivo.
- `assets/` — estilos, script, logotipos (SVG) y fuentes (`assets/fuentes/`, alojadas aquí para no cargar Google Fonts) compartidos. `assets/video/` guarda el vídeo de fondo de la portada (WebM y MP4 comprimidos a 1280×720) y su imagen fija. `site.js` adapta sus textos al idioma de la página (`<html lang>`).
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

## Posicionamiento, analítica y accesibilidad

Ya incluido en todas las páginas: etiqueta canónica, `hreflang`, Open Graph y tarjeta de Twitter, datos estructurados JSON-LD (taller `AutoBodyShop` en inicio y contacto, migas de pan, artículos y preguntas frecuentes), `sitemap.xml`, `robots.txt`, página `404.html`, manifiesto web con iconos y enlace «Saltar al contenido». La web pasa la auditoría automática de accesibilidad axe (WCAG 2 A/AA) sin errores.

Pendiente de datos del taller, todo en `_fuente/comun.py` (después, `python3 _fuente/generar.py`):

- **Google Search Console** — añadir la propiedad con la URL de la web, elegir verificación por «Etiqueta HTML» y copiar el valor de `content` en `EMPRESA["search_console"]`. Una vez verificada, enviar `sitemap.xml` desde «Sitemaps».
- **Ficha de Google** — `EMPRESA["google_ficha"]`: enlace de la ficha (Google Maps > ficha > Compartir). `EMPRESA["google_resena"]`: enlace para dejar reseña (`https://search.google.com/local/writereview?placeid=ID`, el ID sale del panel de Google Business > «Pedir reseñas»).
- **Analítica sin cookies** — `ANALITICA`: proveedor `plausible`, `umami` o `goatcounter` y su identificador. Se registran como eventos las llamadas, los WhatsApp, los correos y los envíos de formulario.
- **Dominio propio** — cambiar `EMPRESA["base_url"]` y añadir un archivo `CNAME` con el dominio.

## Publicación

GitHub Pages construye el sitio con Jekyll. Las páginas no llevan front matter, así que se copian tal cual; `_config.yml` excluye `_fuente/` y este README para que no se publiquen. El generador escribe también `sitemap.xml`, `robots.txt` y `llms.txt` (resumen del negocio para asistentes de IA).

No se carga ningún recurso de terceros al navegar: las fuentes son propias y el mapa de Google Maps solo se carga al pulsar «Ver el mapa».
