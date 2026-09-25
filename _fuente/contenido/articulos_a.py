"""Artículos del blog (ES/EN), primera tanda."""

ARTICULOS = [{'slug': 'articulo-que-hacer-con-un-aranazo',
  'cat': 'chapa-pintura',
  'fecha': '2023-04-18',
  'es': {'titulo': 'Qué hacer con un arañazo en la pintura',
         'resumen': 'No todos los arañazos son iguales. Te enseñamos a saber cuánto de profundo es y cuándo '
                    'basta con un pulido y cuándo hay que repintar.',
         'cuerpo': [('p',
                     'Un roce con una columna del garaje, una rama en un camino estrecho o alguien que pasa '
                     'demasiado cerca con el carro de la compra. Los arañazos son casi inevitables. La '
                     'pregunta es qué hacer con ellos, y la respuesta depende de lo profundo que sea.'),
                    ('h2', 'Las capas de la pintura'),
                    ('p',
                     'La pintura de un coche no es una sola capa. Sobre la chapa hay una protección '
                     'anticorrosión y una [[imprimacion|imprimación]]; encima, la capa de color; y por '
                     'último el [[barniz|barniz]], transparente, que da brillo y protege el color del sol y '
                     'la intemperie. Cuanto más abajo llegue el arañazo, más trabajo tiene arreglarlo.'),
                    ('h2', 'Cómo saber lo profundo que es'),
                    ('ol',
                     ['**Lava y seca la zona.** Muchas marcas son restos de pintura o goma de otro objeto y '
                      'salen con agua o con un limpiador suave.',
                      '**Pasa la uña suavemente** en perpendicular al arañazo. Si no se engancha, '
                      'probablemente solo afecta al barniz.',
                      '**Mira el color del fondo.** Si ves el mismo color del coche, está en barniz o color. '
                      'Si ves un tono gris o blanquecino, ha llegado a la imprimación. Si ves metal '
                      'brillante, ha llegado a la chapa.']),
                    ('h2', 'Qué se puede hacer en cada caso'),
                    ('ul',
                     ['**Arañazo superficial en el barniz**: a menudo se mejora mucho, o desaparece, con un '
                      '[[pulido|pulido]] profesional. El pulido elimina una capa muy fina de barniz, así que '
                      'no conviene abusar de él.',
                      '**Arañazo que llega al color**: el pulido lo disimula pero no lo borra. Suele '
                      'necesitar un retoque o repintar la zona.',
                      '**Arañazo hasta la imprimación o la chapa**: hay que preparar la superficie, aplicar '
                      'imprimación, color y barniz. Si se ve metal, conviene no dejarlo mucho tiempo.']),
                    ('h2', 'Por qué no dejarlo para más adelante'),
                    ('p',
                     'Un arañazo que deja la chapa a la vista es una puerta abierta a la '
                     '[[corrosion|corrosión]]. En zonas de costa, con humedad y salitre, el óxido puede '
                     'empezar antes de lo que parece y extenderse por debajo de la pintura sana. Lo que hoy '
                     'es una línea fina puede convertirse en una burbuja de óxido que obliga a reparar una '
                     'superficie mucho mayor.'),
                    ('h2', 'Con los productos de bricolaje, cuidado'),
                    ('p',
                     'Los lápices de retoque y los pulimentos de gran superficie pueden servir para una '
                     'marca pequeña, sobre todo para proteger el metal mientras llevas el coche al taller. '
                     'Pero conviene tener en cuenta algunas cosas:'),
                    ('ul',
                     ['Un pulimento muy abrasivo, aplicado a mano sin experiencia, puede dejar la zona mate '
                      'o con marcas circulares.',
                      'Un lápiz de retoque rara vez iguala el tono exacto, sobre todo en colores '
                      'metalizados.',
                      'Si luego se repinta la zona, hay que retirar esos productos y el trabajo es algo '
                      'mayor.']),
                    ('h2', 'Repintar solo una parte'),
                    ('p',
                     'Cuando hay que repintar, no siempre es necesario pintar la pieza entera. A veces se '
                     'puede reparar la zona y difuminar el color y el barniz hacia las zonas vecinas para '
                     'que la transición no se note. Si es posible o no depende del tamaño del daño, de dónde '
                     'esté y del color.'),
                    ('quote',
                     'Un arañazo pequeño y reciente casi siempre se arregla mejor, y con menos trabajo, que '
                     'uno que lleva meses a la intemperie.'),
                    ('nota',
                     'Solo viendo el arañazo se puede decir qué solución tiene. Lo que aquí contamos es '
                     'orientativo.'),
                    ('p',
                     'En Green Car Service Tenerife valoramos el daño y te decimos si basta con un [pulido y '
                     'abrillantado](servicio-pulido-y-abrillantado.html) o conviene una [pintura '
                     'parcial](servicio-pintura-parcial.html). Mándanos una foto por WhatsApp o [pide un '
                     'presupuesto](presupuesto.html).')]},
  'en': {'titulo': 'What to do about a scratch in your paint',
         'resumen': 'Not all scratches are the same. Here is how to tell how deep one is, and when polishing '
                    'is enough and when it needs repainting.',
         'cuerpo': [('p',
                     'A brush against a pillar in the car park, a branch on a narrow track or someone '
                     'passing too close with a shopping trolley. Scratches are almost unavoidable. The '
                     'question is what to do about them, and the answer depends on how deep they go.'),
                    ('h2', 'The layers of paint'),
                    ('p',
                     'Car paint is not a single layer. On top of the metal there is anti-corrosion '
                     'protection and a [[imprimacion|primer]]; above that, the colour coat; and finally the '
                     'transparent [[barniz|clear coat]], which gives gloss and protects the colour from sun '
                     'and weather. The deeper a scratch goes, the more work it takes to fix.'),
                    ('h2', 'How to tell how deep it is'),
                    ('ol',
                     ['**Wash and dry the area.** Many marks are paint or rubber transferred from another '
                      'object and come off with water or a mild cleaner.',
                      '**Run a fingernail gently** across the scratch. If it does not catch, it probably '
                      'only affects the clear coat.',
                      "**Look at the colour at the bottom.** If you see the car's own colour, it is in the "
                      'clear coat or colour coat. If you see grey or whitish, it has reached the primer. If '
                      'you see shiny metal, it has reached the panel.']),
                    ('h2', 'What can be done in each case'),
                    ('ul',
                     ['**Light scratch in the clear coat**: it can often be greatly reduced, or removed, '
                      'with professional [[pulido|polishing]]. Polishing removes a very thin layer of clear '
                      'coat, so it should not be overdone.',
                      '**Scratch into the colour coat**: polishing disguises it but does not remove it. It '
                      'usually needs a touch-up or repainting of the area.',
                      '**Scratch down to primer or metal**: the surface has to be prepared and primer, '
                      'colour and clear coat applied. If metal is showing, do not leave it for long.']),
                    ('h2', 'Why not to leave it'),
                    ('p',
                     'A scratch that exposes bare metal is an open door to [[corrosion|corrosion]]. In '
                     'coastal areas, with humidity and salt in the air, rust can start sooner than you might '
                     "think and spread beneath healthy paint. Today's thin line can become a rust bubble "
                     'that means repairing a much larger area.'),
                    ('h2', 'Be careful with DIY products'),
                    ('p',
                     'Touch-up pens and supermarket polishes can help with a small mark, especially to '
                     'protect bare metal until you get the car to a workshop. But bear a few things in '
                     'mind:'),
                    ('ul',
                     ['A very abrasive polish, applied by hand without experience, can leave the area dull '
                      'or with swirl marks.',
                      'A touch-up pen rarely matches the exact shade, especially with metallic colours.',
                      'If the area is repainted later, those products have to be removed first, which adds a '
                      'little work.']),
                    ('h2', 'Repainting only part of a panel'),
                    ('p',
                     'When repainting is needed, it is not always necessary to paint the whole panel. '
                     'Sometimes the damaged area can be repaired and the colour and clear coat blended into '
                     'the surrounding area so the transition does not show. Whether that is possible depends '
                     'on the size of the damage, where it is and the colour.'),
                    ('quote',
                     'A small, recent scratch is nearly always easier, and less work, to fix than one that '
                     'has been out in the weather for months.'),
                    ('nota',
                     'Only by seeing the scratch can we tell you the right fix. What we describe here is a '
                     'general guide.'),
                    ('p',
                     'At Green Car Service Tenerife we assess the damage and tell you whether '
                     '[polishing](servicio-pulido-y-abrillantado.html) is enough or a [partial '
                     'respray](servicio-pintura-parcial.html) makes more sense. Send us a photo on WhatsApp '
                     'or [ask for an estimate](presupuesto.html).')]}},
 {'slug': 'articulo-por-que-el-color-debe-igualarse',
  'cat': 'chapa-pintura',
  'fecha': '2024-05-27',
  'es': {'titulo': 'Por qué el color de una pieza repintada debe igualarse',
         'resumen': 'El código de color del coche es solo el punto de partida. Te contamos qué es la '
                    'colorimetría y por qué una puerta repintada puede no casar si no se ajusta el tono.',
         'cuerpo': [('p',
                     'Seguro que alguna vez has visto un coche con una puerta o un paragolpes de un tono '
                     'ligeramente distinto al resto. Con cierta luz apenas se nota; con otra, salta a la '
                     'vista. Casi siempre es una reparación en la que el color no se igualó bien. Evitarlo '
                     'es el trabajo de la [[colorimetria|colorimetría]].'),
                    ('h2', 'El código de color no basta'),
                    ('p',
                     'Todos los coches tienen un código de color de fábrica, normalmente en una etiqueta en '
                     'el marco de la puerta, bajo el capó o en la documentación. Ese código indica la '
                     'fórmula original. El problema es que el coche que tienes delante ya no es exactamente '
                     'igual al que salió de fábrica, por varias razones:'),
                    ('ul',
                     ['**Variaciones de fabricación**: un mismo código puede tener pequeñas diferencias de '
                      'tono entre lotes o plantas de producción.',
                      '**Envejecimiento**: el sol, la lluvia, los lavados y los años cambian ligeramente el '
                      'aspecto de la pintura. En un clima con tanta radiación como el de Tenerife, se nota.',
                      '**Reparaciones anteriores**: si el coche ya se ha pintado antes, puede haber zonas '
                      'con matices distintos.']),
                    ('h2', 'Cómo se iguala el color'),
                    ('p', 'El proceso combina medición, experiencia y pruebas. A grandes rasgos:'),
                    ('ol',
                     ['Se parte del código de color y de sus posibles variantes.',
                      'Se compara con el coche real, a menudo con ayuda de equipos de medición y cartas de '
                      'color, y siempre bajo buena luz.',
                      'Se ajusta la mezcla y se pinta una muestra de prueba que se compara con la pieza, '
                      'desde varios ángulos.',
                      'Si hace falta, se corrige la fórmula hasta que el tono encaja.']),
                    ('h2', 'Los metalizados y nacarados, más delicados'),
                    ('p',
                     'En una [[metalizado|pintura metalizada]] el color lleva pequeñas partículas que '
                     'reflejan la luz. En una [[nacarado|pintura nacarada]], los pigmentos dan reflejos que '
                     'cambian con el ángulo. En estos acabados no solo importa el tono: también cómo se '
                     'orientan esas partículas, que depende de la forma de aplicar la pintura. Por eso una '
                     'pieza metalizada puede verse igual de frente y distinta de lado si no se trabaja con '
                     'cuidado.'),
                    ('h2', 'El difuminado'),
                    ('p',
                     'Aunque el color esté bien ajustado, el ojo es muy sensible a los cambios bruscos. Por '
                     'eso, a menudo, en lugar de pintar solo la pieza dañada se difumina el color hacia las '
                     'piezas vecinas. Así la transición es gradual y no se aprecia un corte. Es una técnica '
                     'habitual, especialmente en colores metalizados y claros, y es la razón por la que a '
                     'veces el presupuesto incluye trabajo en una pieza que no estaba dañada.'),
                    ('h2', 'La luz también cuenta'),
                    ('p',
                     'Un mismo color puede verse distinto bajo luz de taller, a la sombra o a pleno sol. Por '
                     'eso las comparaciones se hacen con buena iluminación y, cuando es posible, revisando '
                     'el resultado con luz natural. Un taller bien equipado, con [[cabina-de-pintura|cabina '
                     'de pintura]] e iluminación adecuada, trabaja con más garantías.'),
                    ('quote',
                     'Un color bien igualado es el que nadie nota. Si el cliente no sabe decir qué pieza se '
                     'ha pintado, el trabajo está bien hecho.'),
                    ('nota',
                     'En algunos casos, sobre todo en coches muy envejecidos o con colores especiales, la '
                     'igualación perfecta es difícil. Si es así, te lo explicamos antes de empezar.'),
                    ('p',
                     'En Green Car Service Tenerife trabajamos colores sólidos y metalizados con pintura '
                     'ecológica «eco-balance». Puedes ver más en [colores y '
                     'acabados](servicio-colores-y-acabados.html) o [pedir un presupuesto](presupuesto.html) '
                     'para tu reparación.')]},
  'en': {'titulo': 'Why a repainted panel has to be colour-matched',
         'resumen': "Your car's paint code is only the starting point. Here is what colour matching "
                    'involves, and why a repainted door may not match unless the shade is adjusted.',
         'cuerpo': [('p',
                     'You have probably seen a car with a door or bumper in a slightly different shade from '
                     'the rest. In some light it barely shows; in other light it stands out a mile. It is '
                     'almost always a repair where the colour was not matched properly. Avoiding that is the '
                     'job of [[colorimetria|colour matching]].'),
                    ('h2', 'The paint code is not enough'),
                    ('p',
                     'Every car has a factory paint code, usually on a label in the door frame, in the '
                     'bonnet or in the paperwork. That code gives the original formula. The problem is '
                     'that the car in front of you is no longer exactly the same as the one that left the '
                     'factory, for several reasons:'),
                    ('ul',
                     ['**Production variation**: the same code can show small differences in shade between '
                      'batches or factories.',
                      '**Ageing**: sun, rain, washing and time slightly change the look of the paint. In a '
                      "climate with as much sunshine as Tenerife's, it shows.",
                      '**Previous repairs**: if the car has been painted before, some areas may have a '
                      'different tint.']),
                    ('h2', 'How the colour is matched'),
                    ('p', 'The process combines measurement, experience and testing. Broadly speaking:'),
                    ('ol',
                     ['It starts from the paint code and its possible variants.',
                      'This is compared with the actual car, often with the help of measuring equipment and '
                      'colour charts, and always in good light.',
                      'The mix is adjusted and a test card is sprayed and compared with the panel from '
                      'several angles.',
                      'If needed, the formula is corrected until the shade matches.']),
                    ('h2', 'Metallic and pearlescent paints are trickier'),
                    ('p',
                     'In [[metalizado|metallic paint]] the colour contains tiny particles that reflect '
                     'light. In [[nacarado|pearlescent paint]], the pigments give reflections that change '
                     'with the viewing angle. With these finishes it is not only the shade that matters, but '
                     'also how those particles lie, which depends on how the paint is applied. That is why a '
                     'metallic panel can look right head-on and different from the side if it is not done '
                     'carefully.'),
                    ('h2', 'Blending'),
                    ('p',
                     'Even when the colour is well matched, the eye is very sensitive to sudden changes. So '
                     'rather than painting only the damaged panel, the colour is often blended into the '
                     'neighbouring panels. That makes the transition gradual, with no visible edge. It is a '
                     'standard technique, especially with metallic and light colours, and it is why an '
                     'estimate sometimes includes work on a panel that was not damaged.'),
                    ('h2', 'Light matters too'),
                    ('p',
                     'The same colour can look different under workshop lighting, in the shade or in full '
                     'sun. That is why comparisons are made in good light and, where possible, the result is '
                     'checked in daylight. A well-equipped workshop, with a [[cabina-de-pintura|paint '
                     'booth]] and proper lighting, can work with more confidence.'),
                    ('quote',
                     'A well-matched colour is one nobody notices. If the customer cannot tell which panel '
                     'was painted, the job has been done right.'),
                    ('nota',
                     'In some cases, especially with heavily aged cars or special colours, a perfect match '
                     'is hard to achieve. If that applies, we will explain it before we start.'),
                    ('p',
                     'At Green Car Service Tenerife we work with solid and metallic colours using '
                     'eco-friendly «eco-balance» paint. Find out more about [colours and '
                     'finishes](servicio-colores-y-acabados.html) or [ask for an estimate](presupuesto.html) '
                     'for your repair.')]}},
 {'slug': 'articulo-proteger-la-pintura-del-sol',
  'cat': 'chapa-pintura',
  'fecha': '2025-07-15',
  'es': {'titulo': 'Cómo proteger la pintura del sol de Tenerife',
         'resumen': 'La radiación solar intensa apaga el brillo y puede llegar a pelar el barniz. Hábitos '
                    'sencillos para que la pintura de tu coche aguante más años.',
         'cuerpo': [('p',
                     'El sol es una de las grandes razones para vivir en el sur de Tenerife, pero para la '
                     'pintura del coche es un enemigo constante. La radiación ultravioleta y el calor '
                     'trabajan todos los días sobre el techo, el capó y el maletero, que son las superficies '
                     'más horizontales y las que más castigo reciben.'),
                    ('h2', 'Qué le hace el sol a la pintura'),
                    ('p',
                     'La capa que da la cara es el [[barniz|barniz]]. Está pensado precisamente para '
                     'proteger el color, pero con los años la radiación lo va degradando. El proceso suele '
                     'seguir unas fases reconocibles:'),
                    ('ol',
                     ['**Pérdida de brillo**: la pintura se ve más apagada, como sin vida.',
                      '**Decoloración**: el color pierde intensidad. Se nota mucho en rojos y en tonos '
                      'oscuros.',
                      '**Barniz cuarteado o pelado**: aparecen manchas blanquecinas o zonas donde el barniz '
                      'se levanta en escamas.']),
                    ('p',
                     'En las dos primeras fases, un [[pulido|pulido]] y una buena protección pueden '
                     'recuperar bastante el aspecto. Cuando el barniz ya se ha pelado, no hay pulido que lo '
                     'arregle: hay que repintar la zona.'),
                    ('h2', 'Aparcar con cabeza'),
                    ('p', 'Es el consejo más sencillo y el que más ayuda:'),
                    ('ul',
                     ['Si puedes, usa garaje o aparcamiento cubierto.',
                      'En la calle, busca sombra, pero cuidado con algunos árboles: la resina y los '
                      'excrementos de pájaro son agresivos con la pintura.',
                      'Si aparcas siempre en el mismo sitio y orientación, ten en cuenta hacia dónde da el '
                      'sol las horas centrales.',
                      'Una funda de calidad, transpirable y bien ajustada, puede ayudar si el coche pasa '
                      'mucho tiempo parado. Una funda que roce o atrape polvo puede hacer más mal que '
                      'bien.']),
                    ('h2', 'Lavar bien, y a tiempo'),
                    ('p',
                     'Los restos que se quedan sobre la pintura se «cuecen» con el calor. Excrementos de '
                     'pájaro, insectos, resina o polvo de calima con humedad pueden marcar el barniz si se '
                     'dejan días al sol. Retíralos pronto, con agua abundante y sin frotar en seco.'),
                    ('ul',
                     ['Lava a la sombra y con la carrocería fría, no a mediodía con el capó ardiendo.',
                      'Usa champú específico para coches, no lavavajillas: quita las protecciones de la '
                      'pintura.',
                      'Aclara primero para arrastrar el polvo y evitar rayar al pasar la esponja.',
                      'Seca con una microfibra limpia para evitar marcas de cal.']),
                    ('h2', 'Ceras y protecciones'),
                    ('p',
                     'Una cera o un sellante crean una capa sacrificable sobre el barniz: se desgastan ellos '
                     'antes que la pintura. Hay productos de muchos tipos y duraciones, así que sigue las '
                     'indicaciones del fabricante del producto. Lo importante es la constancia: una '
                     'protección aplicada cada cierto tiempo protege más que un tratamiento puntual que '
                     'luego se olvida.'),
                    ('h2', 'No te olvides de faros y plásticos'),
                    ('p',
                     'El sol no solo afecta a la pintura. Los faros de policarbonato se amarillean y se '
                     'vuelven opacos, y los plásticos exteriores negros se quedan grisáceos. Los faros '
                     'opacos iluminan peor, lo que ya es un tema de seguridad y puede dar problemas en la '
                     '[[itv|ITV]].'),
                    ('nota',
                     'Si el barniz ya está pelado, conviene no esperar: sin esa capa, el color queda '
                     'expuesto y el deterioro se acelera.'),
                    ('p',
                     'En Green Car Service Tenerife podemos devolver el brillo con un [pulido y '
                     'abrillantado](servicio-pulido-y-abrillantado.html), [restaurar los '
                     'faros](servicio-restauracion-de-faros.html) o repintar la zona dañada. Nuestra pintura '
                     'cuenta con [garantía vitalicia](servicio-garantia-vitalicia-en-pintura.html).')]},
  'en': {'titulo': 'Protecting your paint from the Tenerife sun',
         'resumen': 'Strong sunshine dulls the shine and can eventually make the clear coat peel. Simple '
                    "habits to help your car's paint last longer.",
         'cuerpo': [('p',
                     'The sun is one of the big reasons for living in the south of Tenerife, but for your '
                     "car's paint it is a constant enemy. Ultraviolet radiation and heat work every day on "
                     'the roof, bonnet and boot lid, which are the most horizontal surfaces and take the '
                     'most punishment.'),
                    ('h2', 'What the sun does to paint'),
                    ('p',
                     'The outermost layer is the [[barniz|clear coat]]. It is designed precisely to protect '
                     'the colour, but over the years sunlight breaks it down. The process usually follows '
                     'recognisable stages:'),
                    ('ol',
                     ['**Loss of gloss**: the paint looks duller, lifeless.',
                      '**Fading**: the colour loses intensity. It is very noticeable on reds and dark '
                      'shades.',
                      '**Cracked or peeling clear coat**: whitish patches appear, or areas where the clear '
                      'coat lifts in flakes.']),
                    ('p',
                     'In the first two stages, [[pulido|polishing]] and good protection can bring back much '
                     'of the look. Once the clear coat has peeled, no amount of polishing will fix it: the '
                     'area has to be repainted.'),
                    ('h2', 'Park wisely'),
                    ('p', 'It is the simplest tip and the one that helps most:'),
                    ('ul',
                     ['Use a garage or covered parking if you can.',
                      'On the street, look for shade, but be careful with some trees: sap and bird droppings '
                      'are harsh on paint.',
                      'If you always park in the same spot and direction, think about where the sun falls in '
                      'the middle of the day.',
                      'A good-quality cover, breathable and well fitted, can help if the car is left unused '
                      'for long periods. A cover that rubs or traps dust can do more harm than good.']),
                    ('h2', 'Wash properly, and promptly'),
                    ('p',
                     "Whatever sits on the paint gets 'baked' by the heat. Bird droppings, insects, sap or "
                     'calima dust mixed with moisture can mark the clear coat if left for days in the sun. '
                     'Remove them quickly, with plenty of water and without rubbing them dry.'),
                    ('ul',
                     ['Wash in the shade with the bodywork cool, not at midday with a scorching bonnet.',
                      "Use a proper car shampoo, not washing-up liquid: it strips the paint's protection.",
                      'Rinse first to lift the dust so the sponge does not scratch.',
                      'Dry with a clean microfibre cloth to avoid water spots.']),
                    ('h2', 'Waxes and sealants'),
                    ('p',
                     'A wax or sealant creates a sacrificial layer on top of the clear coat: it wears away '
                     'before the paint does. There are many types with different lifespans, so follow the '
                     "product maker's instructions. What matters is consistency: protection applied "
                     'regularly does more than a one-off treatment that is then forgotten. A simple test: if '
                     'water no longer beads on the paint after a wash, the protection has probably worn '
                     'off.'),
                    ('h2', 'Do not forget headlights and plastics'),
                    ('p',
                     'The sun does not only affect paint. Polycarbonate headlights turn yellow and cloudy, '
                     'and black exterior plastics go grey. Cloudy headlights give less light, which is a '
                     'safety matter and can cause problems at the [[itv|ITV (MOT)]].'),
                    ('nota',
                     'If the clear coat is already peeling, do not wait: without that layer the colour is '
                     'exposed and deterioration speeds up.'),
                    ('p',
                     'At Green Car Service Tenerife we can bring back the shine with '
                     '[polishing](servicio-pulido-y-abrillantado.html), [restore your '
                     'headlights](servicio-restauracion-de-faros.html) or repaint the damaged area. Our '
                     'paintwork comes with a [lifetime paint '
                     'warranty](servicio-garantia-vitalicia-en-pintura.html).')]}},
 {'slug': 'articulo-salitre-y-corrosion-en-coches-de-costa',
  'cat': 'chapa-pintura',
  'fecha': '2026-02-03',
  'es': {'titulo': 'El salitre y la corrosión en coches de costa',
         'resumen': 'Vivir cerca del mar tiene un precio para la chapa. Dónde ataca el salitre, cómo '
                    'detectar el óxido a tiempo y qué puedes hacer para frenarlo.',
         'cuerpo': [('p',
                     'Buena parte de la vida en el sur de Tenerife pasa cerca del mar. Y el ambiente marino, '
                     'con su humedad y las partículas de sal que lleva el viento, es uno de los factores que '
                     'más aceleran la [[corrosion|corrosión]] de un coche. No hace falta aparcar en primera '
                     'línea de playa: el salitre llega bastante hacia el interior.'),
                    ('h2', 'Por qué la sal acelera el óxido'),
                    ('p',
                     'El óxido aparece cuando el acero está en contacto con oxígeno y humedad. La sal '
                     'disuelta en esa humedad hace que la reacción vaya más rápido. Además, la sal atrae la '
                     'humedad del aire, así que las superficies con restos de salitre tardan más en secarse. '
                     'Es la combinación perfecta para que el metal se deteriore.'),
                    ('h2', 'Dónde suele empezar'),
                    ('ul',
                     ['**Bajos del coche**: suelo, largueros, travesaños y uniones con '
                      '[[sellador|sellador]].',
                      '**Pasos de rueda**: se acumulan barro, arena y sal.',
                      '**Bordes inferiores de puertas y portón**, donde se queda el agua si los desagües '
                      'están tapados.',
                      '**Zonas con la pintura dañada**: arañazos, picotazos de piedras o golpes que dejan la '
                      'chapa a la vista.',
                      '**Tornillería, soportes y elementos metálicos** sin pintar.']),
                    ('h2', 'Cómo detectarlo a tiempo'),
                    ('p', 'La corrosión suele avisar antes de ser grave. Fíjate en:'),
                    ('ul',
                     ['Pequeñas burbujas o ampollas bajo la pintura: suele ser óxido avanzando por debajo.',
                      'Manchas marrones o anaranjadas en bordes, juntas o alrededor de molduras.',
                      'Pintura que se levanta en escamas en los bajos de las puertas.',
                      'Sellador de juntas agrietado o despegado, que deja pasar agua a la chapa.']),
                    ('p',
                     'Cuanto antes se trate, más sencilla es la reparación. Una burbuja pequeña se puede '
                     'sanear; una zona perforada puede requerir cambiar o soldar chapa.'),
                    ('h2', 'Hábitos que ayudan'),
                    ('ol',
                     ['**Lava el coche con regularidad**, incluidos los bajos y los pasos de rueda, sobre '
                      'todo después de ir a la playa o de circular por la costa con viento.',
                      '**Aclara con agua dulce abundante**. Un lavado sin aclarado deja restos de sal.',
                      '**Revisa los desagües** de puertas y del hueco del techo solar si lo tienes, para que '
                      'el agua no se quede dentro.',
                      '**Repara pronto los arañazos** que llegan a la chapa. Mientras tanto, protégelos para '
                      'que no les dé la humedad.',
                      '**Aspira la arena del interior**: la que entra con toallas y sillas de playa acaba en '
                      'moquetas y rincones y retiene humedad.']),
                    ('h2', 'Tratamientos de protección'),
                    ('p',
                     'Además de la protección de fábrica, se pueden aplicar tratamientos anticorrosión en '
                     'bajos y en cavidades interiores de la [[carroceria|carrocería]], como los huecos de '
                     'largueros y puertas. Crean una barrera frente a la humedad y la sal. No hacen al coche '
                     'inmune, pero ayudan a alargar la vida de la chapa, sobre todo en coches que viven '
                     'junto al mar. Qué tratamiento conviene depende del coche, de su edad y de su estado.'),
                    ('quote',
                     'El óxido no descansa. Lo que hoy es una mancha en el bajo de una puerta, en unos meses '
                     'puede ser un agujero.'),
                    ('nota',
                     'Si la corrosión afecta a elementos estructurales o de anclaje, no es solo estética: '
                     'puede afectar a la seguridad del coche y conviene revisarla cuanto antes.'),
                    ('p',
                     'En Green Car Service Tenerife revisamos el estado de la chapa y aplicamos el '
                     '[tratamiento anticorrosión](servicio-tratamiento-anticorrosion.html) adecuado a cada '
                     'caso. Si ya hay daños, nos encargamos de la [reparación de '
                     'chapa](servicio-reparacion-de-chapa.html). [Pide cita](pedir-cita.html) y le echamos '
                     'un vistazo.')]},
  'en': {'titulo': 'Salt air and corrosion on coastal cars',
         'resumen': 'Living near the sea comes at a price for your bodywork. Where salt attacks, how to spot '
                    'rust early and what you can do to slow it down.',
         'cuerpo': [('p',
                     'Much of life in the south of Tenerife happens close to the sea. And the marine '
                     'environment, with its humidity and the salt particles carried by the wind, is one of '
                     'the factors that most speeds up [[corrosion|corrosion]] on a car. You do not need to '
                     'park on the seafront: salt air travels a fair way inland.'),
                    ('h2', 'Why salt speeds up rust'),
                    ('p',
                     'Rust forms when steel is in contact with oxygen and moisture. Salt dissolved in that '
                     'moisture makes the reaction go faster. Salt also draws moisture from the air, so '
                     'surfaces with salt residue take longer to dry. It is the perfect combination for metal '
                     'to deteriorate.'),
                    ('h2', 'Where it usually starts'),
                    ('ul',
                     ['**Underside**: floor pan, chassis rails, crossmembers and joints with '
                      '[[sellador|seam sealer]].',
                      '**Wheel arches**: mud, sand and salt build up there.',
                      '**Bottom edges of doors and tailgate**, where water collects if the drain holes are '
                      'blocked.',
                      '**Areas with damaged paint**: scratches, stone chips or dents that leave bare metal.',
                      '**Bolts, brackets and unpainted metal parts.**']),
                    ('h2', 'How to spot it early'),
                    ('p', 'Corrosion usually gives warning before it becomes serious. Look out for:'),
                    ('ul',
                     ['Small bubbles or blisters under the paint: often rust creeping underneath.',
                      'Brown or orange stains on edges, seams or around trims.',
                      'Paint flaking off along the bottom of the doors.',
                      'Cracked or lifting seam sealer that lets water reach the metal.']),
                    ('p',
                     'The sooner it is dealt with, the simpler the repair. A small bubble can be treated; a '
                     'rusted-through area may need metal replaced or welded.'),
                    ('h2', 'Habits that help'),
                    ('ol',
                     ['**Wash the car regularly**, including the underside and wheel arches, especially '
                      'after a trip to the beach or driving along the coast on a windy day.',
                      '**Rinse with plenty of fresh water.** A wash without a proper rinse leaves salt '
                      'behind.',
                      '**Check the drain holes** in the doors and around the sunroof if you have one, so '
                      'water does not collect inside.',
                      '**Repair scratches down to bare metal promptly.** In the meantime, protect them from '
                      'moisture.',
                      '**Vacuum sand out of the interior**: sand brought in on towels and beach chairs ends '
                      'up in carpets and corners and holds moisture.']),
                    ('h2', 'Protective treatments'),
                    ('p',
                     'On top of factory protection, anti-corrosion treatments can be applied to the '
                     'underside and to inner cavities of the [[carroceria|bodywork]], such as inside chassis '
                     'rails and doors. They create a barrier against moisture and salt. They do not make the '
                     'car immune, but they help extend the life of the metal, especially on cars that live '
                     'by the sea. Which treatment suits depends on the car, its age and its condition.'),
                    ('quote',
                     "Rust never rests. Today's stain at the bottom of a door can be a hole in a few "
                     'months.'),
                    ('nota',
                     'If corrosion affects structural parts or mountings, it is not just cosmetic: it can '
                     "affect the car's safety and should be checked as soon as possible."),
                    ('p',
                     'At Green Car Service Tenerife we check the condition of the bodywork and apply the '
                     'right [anti-corrosion treatment](servicio-tratamiento-anticorrosion.html) for each '
                     'case. If there is already damage, we take care of the [panel '
                     'repair](servicio-reparacion-de-chapa.html). [Book an appointment](pedir-cita.html) and '
                     'we will take a look.')]}},
 {'slug': 'articulo-ninos-en-el-coche-sistemas-de-retencion',
  'cat': 'seguridad-vial',
  'fecha': '2025-01-20',
  'es': {'titulo': 'Niños en el coche: sistemas de retención infantil',
         'resumen': 'Qué dice la norma en España, cómo elegir la silla adecuada y los errores de instalación '
                    'más comunes. También si vienes de visita y alquilas coche.',
         'cuerpo': [('p',
                     'El cinturón de seguridad está diseñado para adultos. En un niño, la banda puede quedar '
                     'a la altura del cuello o del abdomen y, en un impacto, hacer más daño que bien. Por '
                     'eso existen los sistemas de retención infantil, conocidos como sillitas, elevadores o '
                     'capazos. Usarlos bien es una de las cosas que más protegen a los pequeños en el '
                     'coche.'),
                    ('h2', 'Qué dice la norma en España'),
                    ('p',
                     'La regla general es que los menores de **135 cm de estatura** deben viajar en un '
                     'sistema de retención adecuado a su talla y peso, y hacerlo en los asientos traseros. '
                     'Hay excepciones concretas, por ejemplo cuando el coche no tiene asientos traseros o '
                     'cuando estos ya están ocupados por otros niños con su propio sistema. Si un niño va '
                     'delante en una silla orientada hacia atrás, el airbag frontal del '
                     'acompañante debe estar desactivado.'),
                    ('p',
                     'Entre 135 y 150 cm pueden usar el cinturón del coche o seguir en un sistema de '
                     'retención. Muchas veces conviene seguir con el elevador hasta que el cinturón quede '
                     'bien colocado: por encima de la clavícula, no del cuello, y sobre la cadera, no sobre '
                     'la tripa.'),
                    ('h2', 'Cómo elegir la silla'),
                    ('ul',
                     ['Debe estar **homologada** según la normativa europea. En la etiqueta verás la '
                      'referencia de homologación; las más recientes siguen la norma i-Size (R129), que '
                      'clasifica las sillas por estatura.',
                      'Elige según la **estatura y el peso** del niño, no solo la edad.',
                      'Comprueba que es **compatible con tu coche**. No todas las sillas encajan bien en '
                      'todos los asientos.',
                      'Si el coche tiene anclajes **ISOFIX**, facilitan una instalación correcta y reducen '
                      'errores.']),
                    ('h2', 'A contramarcha, mejor'),
                    ('p',
                     'Para los más pequeños, viajar mirando hacia atrás es la opción más protectora: en un '
                     'choque frontal, el respaldo reparte la fuerza por toda la espalda y sujeta la cabeza, '
                     'que en los bebés pesa mucho en proporción al cuerpo. Las recomendaciones de seguridad '
                     'vial aconsejan mantener la contramarcha el mayor tiempo posible, dentro de los límites '
                     'de la silla.'),
                    ('h2', 'Errores frecuentes'),
                    ('ol',
                     ['**Arneses flojos.** Si puedes pellizcar la cinta a la altura del hombro, está '
                      'demasiado suelta.',
                      '**Abrigos gruesos** debajo del arnés: crean holgura. Mejor quitar el abrigo y taparlo '
                      'encima.',
                      '**Silla mal anclada**, que se mueve más de lo que indica el fabricante.',
                      '**Cinturón mal pasado** por las guías del elevador.',
                      '**Pasar al niño a la siguiente etapa demasiado pronto.**',
                      '**Objetos sueltos** en el habitáculo: en un frenazo, cualquier cosa puede convertirse '
                      'en un proyectil.']),
                    ('h2', 'Si vienes de visita y alquilas coche'),
                    ('p',
                     'Muchos visitantes del sur de Tenerife alquilan coche con niños. Reserva la silla con '
                     'antelación, revisa al recogerla que es adecuada para la talla de tu hijo y que está en '
                     'buen estado, y tómate unos minutos para instalarla con calma siguiendo el manual. Si '
                     'traes tu propia silla, comprueba que es compatible con el coche de alquiler.'),
                    ('nota',
                     'La normativa puede cambiar y cada silla tiene sus propias instrucciones. Ante la duda, '
                     'consulta la información de la DGT y el manual del fabricante de la silla y del coche.'),
                    ('h2', 'El airbag del acompañante'),
                    ('p',
                     'Si alguna vez necesitas llevar una silla a contramarcha delante, aprende cómo se '
                     'desactiva el airbag en tu coche: en unos es un interruptor con llave, en otros se hace '
                     'desde el menú. Comprueba siempre en el cuadro el indicador que confirma que está '
                     'desactivado, y vuelve a activarlo cuando viaje un adulto. Si tienes dudas, el manual '
                     'del coche explica el procedimiento exacto para tu modelo.'),
                    ('p',
                     'Si dejas tu coche en Green Car Service Tenerife y usas nuestro '
                     '[[vehiculo-de-sustitucion|vehículo de sustitución]], recuerda pasar la silla de un '
                     'coche a otro. Y si tu coche ha tenido un accidente con la silla instalada, consulta el '
                     'manual de la silla: muchos fabricantes recomiendan sustituirla aunque no se vean daños. '
                     'Para todo lo relacionado con el golpe, tienes información en '
                     '[siniestros](siniestros.html) y puedes [pedir cita](pedir-cita.html) por teléfono o '
                     'WhatsApp.')]},
  'en': {'titulo': 'Children in the car: child restraint systems',
         'resumen': 'What Spanish rules say, how to choose the right seat and the most common fitting '
                    'mistakes. Plus tips if you are visiting and hiring a car.',
         'cuerpo': [('p',
                     'Seatbelts are designed for adults. On a child, the belt can sit across the neck or the '
                     'stomach and, in a crash, do more harm than good. That is why child restraint systems '
                     'exist: child seats, booster seats and baby carriers. Using them properly is one of the '
                     'things that best protects children in the car.'),
                    ('h2', 'What the rules say in Spain'),
                    ('p',
                     'The general rule is that children under **135 cm tall** must travel in a restraint '
                     'system suited to their height and weight, and must sit in the rear seats. There are '
                     'specific exceptions, for example when the car has no rear seats or when they are '
                     'already occupied by other children in their own restraints. If a child travels in the '
                     "front in a rear-facing seat, the passenger's front airbag must be switched "
                     'off.'),
                    ('p',
                     "Between 135 and 150 cm, children can use the car's seatbelt or stay in a restraint "
                     'system. It is often best to keep using a booster until the belt fits properly: across '
                     'the collarbone, not the neck, and over the hips, not the tummy.'),
                    ('h2', 'Choosing a seat'),
                    ('ul',
                     ['It must be **approved** under European rules. The label shows the approval reference; '
                      'the most recent seats follow the i-Size standard (R129), which classifies seats by '
                      "the child's height.",
                      "Choose according to the child's **height and weight**, not just age.",
                      'Check it is **compatible with your car**. Not every seat fits well in every vehicle.',
                      'If your car has **ISOFIX** anchor points, they make correct fitting easier and reduce '
                      'mistakes.']),
                    ('h2', 'Rear-facing is safer'),
                    ('p',
                     'For the youngest children, travelling rear-facing is the most protective option: in a '
                     'frontal crash, the seat back spreads the force across the whole back and supports the '
                     'head, which in babies is heavy relative to the body. Road safety advice is to keep '
                     "children rear-facing for as long as possible, within the seat's limits."),
                    ('h2', 'Common mistakes'),
                    ('ol',
                     ['**Loose harness straps.** If you can pinch the strap at shoulder height, it is too '
                      'loose.',
                      '**Thick coats** under the harness: they create slack. Take the coat off and put it '
                      'over the child instead.',
                      '**Seat not firmly fitted**, moving more than the manufacturer allows.',
                      "**Seatbelt routed wrongly** through the booster's guides.",
                      '**Moving the child up to the next stage too early.**',
                      '**Loose objects** in the cabin: under hard braking, anything can become a '
                      'projectile.']),
                    ('h2', 'Visiting and hiring a car'),
                    ('p',
                     'Many visitors to the south of Tenerife hire a car and travel with children. Book the '
                     "seat in advance, check when you collect it that it suits your child's size and is in "
                     'good condition, and take a few minutes to fit it calmly following the instructions. If '
                     'you bring your own seat, check it is compatible with the hire car.'),
                    ('nota',
                     'Rules can change and every seat has its own instructions. If in doubt, check the DGT '
                     '(Spanish traffic authority) information and the manuals for both the seat and the '
                     'car.'),
                    ('h2', 'The passenger airbag'),
                    ('p',
                     'If you ever need to fit a rear-facing seat in the front, learn how the airbag is '
                     'switched off in your car: on some it is a key switch, on others it is done through the '
                     'menu. Always check the dashboard indicator confirming it is off, and switch it back on '
                     'when an adult sits there. If in doubt, the car\'s handbook explains the exact procedure '
                     'for your model.'),
                    ('p',
                     'If you leave your car with Green Car Service Tenerife and use our '
                     '[[vehiculo-de-sustitucion|courtesy car]], remember to move the child seat across. And '
                     'if your car has been in an accident with the seat fitted, check the seat\'s manual: many '
                     'manufacturers recommend replacing it even if no damage is visible. For everything to '
                     'do with the accident itself, see our [claims](siniestros.html) page, and you can [book '
                     'an appointment](pedir-cita.html) by phone or WhatsApp.')]}},
 {'slug': 'articulo-fatiga-al-volante',
  'cat': 'seguridad-vial',
  'fecha': '2026-09-08',
  'es': {'titulo': 'Fatiga al volante: cómo reconocerla y evitarla',
         'resumen': 'El cansancio llega poco a poco y engaña. Las señales de alarma, los mitos que no '
                    'funcionan y lo único que de verdad lo soluciona: parar y descansar.',
         'cuerpo': [('p',
                     'La fatiga es traicionera porque no se nota de golpe. Empiezas un trayecto bien y, sin '
                     'darte cuenta, tus reacciones se vuelven más lentas, te cuesta mantener la atención y '
                     'tomas peores decisiones. En el peor de los casos llega el microsueño: unos segundos en '
                     'los que el cerebro se «desconecta» con los ojos casi abiertos. A velocidad de autovía, '
                     'en esos segundos el coche recorre muchos metros sin control.'),
                    ('h2', 'Señales de alarma'),
                    ('p', 'Si notas cualquiera de estas señales, tu cuerpo te está pidiendo parar:'),
                    ('ul',
                     ['Bostezos frecuentes y parpadeo pesado.',
                      'Picor de ojos o sensación de tener que frotártelos.',
                      'Te cuesta mantener la cabeza erguida.',
                      'No recuerdas los últimos kilómetros.',
                      'Te pasas una salida o no ves una señal.',
                      'Te desvías del carril o pisas la línea sin querer.',
                      'Cambias de velocidad sin motivo o te acercas demasiado al coche de delante.']),
                    ('h2', 'Situaciones de más riesgo'),
                    ('ul',
                     ['Conducir después de dormir poco o mal.',
                      'Las primeras horas de la tarde, después de comer, y la madrugada.',
                      'Trayectos largos y monótonos, como una autovía recta con poco tráfico.',
                      'Volver de un día de playa o de montaña: el sol, el calor y el esfuerzo cansan más de '
                      'lo que parece.',
                      'Después de un vuelo largo o con cambio de hora, algo habitual en quien acaba de '
                      'aterrizar en el aeropuerto del sur y recoge un coche de alquiler.',
                      'Tomar medicamentos que producen somnolencia. Mira el prospecto: muchos llevan un '
                      'pictograma de advertencia para la conducción.']),
                    ('h2', 'Lo que no funciona'),
                    ('p',
                     'Bajar la ventanilla, subir la música o poner el aire frío te despejan unos minutos, '
                     'pero no quitan el sueño. El café o las bebidas con cafeína pueden ayudar un rato, '
                     'aunque tardan en hacer efecto y no sustituyen al descanso. Hablar con el acompañante '
                     'ayuda, pero tampoco es la solución si el cuerpo pide dormir.'),
                    ('h2', 'Lo que sí funciona'),
                    ('ol',
                     ['**Descansar bien antes de salir**, sobre todo si el viaje es largo.',
                      '**Parar con regularidad.** La recomendación habitual de la DGT es hacer una pausa '
                      'cada dos horas o unos 200 km, aunque no te sientas cansado.',
                      '**Si notas las señales, para ya**, en un lugar seguro. Una siesta corta, de unos 15 o '
                      '20 minutos, puede marcar la diferencia.',
                      '**Comer ligero** y beber agua. Las comidas copiosas dan sueño.',
                      '**Compartir la conducción** en trayectos largos, si es posible.']),
                    ('h2', 'Un coche en buen estado también ayuda'),
                    ('p',
                     'Conducir cansado ya es difícil; hacerlo viendo mal lo es más. Unos faros amarillentos '
                     'y opacos iluminan menos y dispersan la luz, así que de noche obligan a forzar la vista. '
                     'Una luna con impactos o rayada por la calima deslumbra con el sol bajo, y unos '
                     'retrovisores sucios o mal ajustados te hacen girar la cabeza más de la cuenta. Todo '
                     'eso suma cansancio. Y muchos coches recientes incorporan avisos de salida de carril o '
                     'detectores de fatiga: son una ayuda útil, pero no sustituyen a tu atención ni a una '
                     'parada a tiempo.'),
                    ('quote', 'Llegar diez minutos más tarde no es un problema. No llegar sí lo es.'),
                    ('nota',
                     'Si tienes somnolencia frecuente durante el día aunque duermas suficiente, coméntalo '
                     'con tu médico: algunos trastornos del sueño afectan a la conducción y tienen '
                     'tratamiento.'),
                    ('p',
                     'Si tus faros han perdido transparencia con el sol, en Green Car Service Tenerife los '
                     'pulimos y protegemos con nuestra [restauración de faros](servicio-restauracion-de-faros.html), '
                     'y si el frontal ha sufrido un golpe, lo reparamos en nuestro taller de [chapa y '
                     'pintura](chapa-y-pintura.html). [Pide cita](pedir-cita.html) cuando lo necesites.')]},
  'en': {'titulo': 'Driver fatigue: how to recognise and avoid it',
         'resumen': 'Tiredness creeps up on you and is deceptive. The warning signs, the myths that do not '
                    'work, and the only thing that really helps: stopping to rest.',
         'cuerpo': [('p',
                     'Fatigue is treacherous because it does not hit you all at once. You start a journey '
                     'feeling fine and, without noticing, your reactions slow down, it gets harder to stay '
                     'focused and you make worse decisions. At worst comes the microsleep: a few seconds '
                     "when the brain 'switches off' with the eyes almost open. At dual-carriageway speed, the car "
                     'covers a long distance out of control in those seconds.'),
                    ('h2', 'Warning signs'),
                    ('p', 'If you notice any of these signs, your body is telling you to stop:'),
                    ('ul',
                     ['Frequent yawning and heavy blinking.',
                      'Itchy eyes or wanting to rub them.',
                      'Struggling to keep your head up.',
                      'Not remembering the last few kilometres.',
                      'Missing an exit or a road sign.',
                      'Drifting out of your lane or touching the line without meaning to.',
                      'Changing speed for no reason or getting too close to the car in front.']),
                    ('h2', 'Higher-risk situations'),
                    ('ul',
                     ['Driving after too little or poor sleep.',
                      'Early afternoon, after lunch, and the small hours of the night.',
                      'Long, monotonous drives, such as a straight dual carriageway with little traffic.',
                      'Coming back from a day at the beach or in the mountains: sun, heat and exercise are '
                      'more tiring than they seem.',
                      'After a long flight or a time-zone change, common for anyone landing at Tenerife '
                      'South airport and picking up a hire car.',
                      'Taking medicines that cause drowsiness. Check the leaflet: in Spain many carry a '
                      'warning pictogram about driving.']),
                    ('h2', 'What does not work'),
                    ('p',
                     'Opening the window, turning up the music or blasting cold air will perk you up for a '
                     'few minutes, but they do not cure sleepiness. Coffee or caffeinated drinks can help '
                     'for a while, although they take time to kick in and are no substitute for rest. '
                     'Chatting to a passenger helps, but it is not the answer if your body needs sleep.'),
                    ('h2', 'What does work'),
                    ('ol',
                     ['**Get a good rest before setting off**, especially for a long trip.',
                      "**Stop regularly.** The usual advice from the DGT, Spain's traffic authority, is to "
                      'take a break every two hours or around 200 km, even if you do not feel tired.',
                      '**If you notice the signs, stop now**, somewhere safe. A short nap of around 15 to 20 '
                      'minutes can make all the difference.',
                      '**Eat light** and drink water. Heavy meals make you drowsy.',
                      '**Share the driving** on long journeys if you can.']),
                    ('h2', 'A car in good condition helps too'),
                    ('p',
                     'Driving tired is hard enough; doing it when you cannot see well is harder. Yellowed, '
                     'cloudy headlights give less light and scatter the beam, so at night you strain your '
                     'eyes. A windscreen with chips or scratched by calima dust dazzles you when the sun is '
                     'low, and dirty or badly adjusted mirrors make you turn your head more than you should. '
                     'It all adds to fatigue. Many recent cars also include lane departure warnings or '
                     'fatigue detection: they are a useful aid, but they do not replace your attention or a '
                     'timely stop.'),
                    ('quote', 'Arriving ten minutes late is not a problem. Not arriving at all is.'),
                    ('nota',
                     'If you often feel sleepy during the day despite getting enough sleep, talk to your '
                     'doctor: some sleep disorders affect driving and can be treated.'),
                    ('p',
                     'If your headlights have gone cloudy in the sun, at Green Car Service Tenerife we polish '
                     'and protect them with our [headlight restoration](servicio-restauracion-de-faros.html) '
                     'service, and if the front end has taken a knock, we repair it in our [bodywork and '
                     'paint](chapa-y-pintura.html) workshop. [Book an appointment](pedir-cita.html) whenever '
                     'you need to.')]}},
 {'slug': 'articulo-que-hacer-justo-despues-de-un-accidente',
  'cat': 'seguros-siniestros',
  'fecha': '2026-01-27',
  'es': {'titulo': 'Qué hacer justo después de un accidente',
         'resumen': 'Los primeros minutos tras un accidente son de nervios. Tener claro el orden de los '
                    'pasos te ayuda a protegerte y a que después el seguro funcione sin sorpresas.',
         'cuerpo': [('p',
                     'Nadie sale de casa pensando en tener un accidente, y por eso cuando ocurre es fácil '
                     'bloquearse. Aunque sea un golpe pequeño en una rotonda de Las Américas o un alcance en '
                     'la TF-1, seguir un orden sencillo evita errores que luego complican el '
                     '[[siniestro|siniestro]]. Primero la seguridad, después los datos y, por último, el '
                     'seguro.'),
                    ('h2', '1. Protégete y protege a los demás'),
                    ('ol',
                     ['Enciende las luces de emergencia.',
                      'Ponte el chaleco reflectante antes de salir del coche.',
                      'Señaliza el vehículo. En España, desde enero de 2026 la señal obligatoria es la '
                      'baliza luminosa V-16 conectada, que se coloca en el techo sin tener que caminar por '
                      'la calzada.',
                      'Si el coche puede moverse y no hay heridos, apártalo a un lugar seguro. Si no, sal '
                      'por el lado contrario al tráfico y ponte detrás de la barrera o fuera de la vía.']),
                    ('h2', '2. Comprueba si hay heridos'),
                    ('p',
                     'Si alguien está herido, aunque parezca leve, llama al 112. No muevas a un herido salvo '
                     'que corra un peligro inmediato. También conviene llamar si el accidente bloquea la '
                     'vía, si hay implicados que no colaboran o si sospechas que algún conductor va bajo los '
                     'efectos del alcohol u otras sustancias. En esos casos, la actuación de los agentes '
                     'deja constancia oficial de lo ocurrido.'),
                    ('h2', '3. Recoge información'),
                    ('p', 'Con todos a salvo, toca documentar. Hazlo con calma y con el móvil:'),
                    ('ul',
                     ['Fotos de los vehículos, de los daños, de las matrículas y de la posición en la que '
                      'quedaron.',
                      'Fotos de la vía: señales, marcas de frenada, visibilidad.',
                      'Nombre, teléfono, DNI o pasaporte y permiso de conducir del otro conductor.',
                      'Aseguradora y número de póliza del otro vehículo.',
                      'Datos de contacto de testigos, si los hay.']),
                    ('p',
                     'Si el otro vehículo es de alquiler, algo muy habitual en el sur de la isla, anota '
                     'también la empresa de alquiler: su contrato suele indicar la aseguradora.'),
                    ('h2', '4. Rellena el parte amistoso'),
                    ('p',
                     'Si hay acuerdo sobre lo ocurrido, el [[parte-amistoso|parte amistoso]] (Declaración '
                     'Amistosa de Accidente) es la forma más rápida de que las aseguradoras gestionen el '
                     'caso. Rellenadlo juntos, revisadlo antes de firmar y quedaos cada uno con su copia. Si '
                     'no hay acuerdo, no firmes: cada uno comunica su versión a su aseguradora y, si hace '
                     'falta, se pide la intervención de los agentes.'),
                    ('h2', '5. Evita lo que complica las cosas'),
                    ('ul',
                     ['No discutas ni reconozcas culpas de palabra: lo que cuenta es lo que queda por '
                      'escrito.',
                      'No firmes documentos que no entiendas; si el otro conductor no habla tu idioma, '
                      'buscad una versión del parte en el idioma de cada uno, que tiene el mismo formato.',
                      'No abandones el lugar sin haber intercambiado los datos.']),
                    ('h2', '6. Avisa a tu aseguradora'),
                    ('p',
                     'Comunica el siniestro cuanto antes. La ley y las pólizas fijan un plazo de pocos días '
                     'para hacerlo. Envía el parte y las fotos, y pregunta por los pasos siguientes: grúa si '
                     'la necesitas, [[peritacion|peritación]] y taller. Recuerda que, en general, puedes '
                     'elegir dónde reparar tu coche; revisa lo que dice tu póliza.'),
                    ('nota',
                     'Si te duele algo en los días siguientes, acude al médico aunque en el momento te '
                     'encontraras bien. Algunas lesiones leves aparecen más tarde y es importante que queden '
                     'documentadas.'),
                    ('p',
                     'En Green Car Service Tenerife te ayudamos después del accidente: coordinamos la '
                     'peritación, tramitamos la reparación con tu compañía y, cuando es posible, te '
                     'ofrecemos vehículo de sustitución. Consulta nuestra [guía de qué hacer tras un '
                     'accidente](guia-que-hacer-tras-un-accidente.html), los [teléfonos de '
                     'asistencia](telefonos-de-asistencia.html) y nuestro servicio de [gestión con '
                     'aseguradoras](servicio-gestion-con-aseguradoras.html).')]},
  'en': {'titulo': 'What to do straight after an accident',
         'resumen': 'The first minutes after an accident are stressful. Knowing the order of the steps helps '
                    'you stay safe and makes sure the insurance works without surprises later.',
         'cuerpo': [('p',
                     'Nobody leaves home expecting to have an accident, which is why it’s easy to freeze '
                     'when it happens. Whether it’s a small knock on a roundabout in Las Américas or a '
                     'rear-end shunt on the TF-1, following a simple order avoids mistakes that later '
                     'complicate the [[siniestro|claim]]. Safety first, then information, and finally the '
                     'insurance.'),
                    ('h2', '1. Protect yourself and others'),
                    ('ol',
                     ['Switch on your hazard lights.',
                      'Put on your reflective vest before getting out of the car.',
                      'Signal the vehicle. In Spain, since January 2026 the mandatory warning device is the '
                      'connected V-16 beacon, which goes on the roof so you don’t have to walk along the '
                      'carriageway.',
                      'If the car can be moved and nobody is hurt, move it somewhere safe. If not, get out '
                      'on the side away from traffic and stand behind the barrier or off the road.']),
                    ('h2', '2. Check for injuries'),
                    ('p',
                     'If anyone is injured, even if it seems minor, call 112. Don’t move an injured person '
                     'unless they are in immediate danger. It’s also worth calling if the accident blocks '
                     'the road, if someone involved won’t cooperate, or if you suspect a driver is under the '
                     'influence of alcohol or other substances. In those cases, the police attendance '
                     'creates an official record of what happened.'),
                    ('h2', '3. Gather information'),
                    ('p', 'Once everyone is safe, it’s time to document. Take your time and use your phone:'),
                    ('ul',
                     ['Photos of the vehicles, the damage, the number plates and where the cars ended up.',
                      'Photos of the road: signs, skid marks, visibility.',
                      'The other driver’s name, phone number, ID or passport and driving licence.',
                      'The other vehicle’s insurer and policy number.',
                      'Contact details of any witnesses.']),
                    ('p',
                     'If the other car is a hire car, which is very common in the south of the island, also '
                     'note the rental company: its contract usually names the insurer.'),
                    ('h2', '4. Fill in the accident report form'),
                    ('p',
                     'If you agree on what happened, the [[parte-amistoso|accident report form]] (the '
                     'European Accident Statement, known in Spain as the ‘parte amistoso’) is the quickest '
                     'way for the insurers to handle the case. Fill it in together, check it before signing '
                     'and each keep your copy. If you don’t agree, don’t sign: each driver reports their '
                     'version to their own insurer and, if necessary, the police are called.'),
                    ('h2', '5. Avoid what makes things harder'),
                    ('ul',
                     ['Don’t argue or admit fault verbally: what counts is what is written down.',
                      'Don’t sign anything you don’t understand; if the other driver doesn’t speak your '
                      'language, use a version of the form in each language, which has the same layout.',
                      'Don’t leave the scene without exchanging details.']),
                    ('h2', '6. Tell your insurer'),
                    ('p',
                     'Report the claim as soon as possible. The law and policies set a deadline of just a '
                     'few days. Send the form and the photos, and ask about the next steps: recovery truck '
                     'if you need one, [[peritacion|loss assessment]] and garage. Remember that, in general, '
                     'you can choose where your car is repaired; check what your policy says.'),
                    ('nota',
                     'If you feel pain in the following days, see a doctor even if you felt fine at the '
                     'time. Some minor injuries appear later and it’s important they are documented.'),
                    ('p',
                     'At Green Car Service Tenerife we help you after an accident: we coordinate the '
                     'assessment, handle the repair with your insurer and, where possible, offer a courtesy '
                     'car. See our [guide on what to do after an '
                     'accident](guia-que-hacer-tras-un-accidente.html), the [assistance phone '
                     'numbers](telefonos-de-asistencia.html) and our [insurance handling '
                     'service](servicio-gestion-con-aseguradoras.html).')]}},
 {'slug': 'articulo-como-rellenar-el-parte-amistoso',
  'cat': 'seguros-siniestros',
  'fecha': '2023-11-07',
  'es': {'titulo': 'Cómo rellenar el parte amistoso sin errores',
         'resumen': 'El parte amistoso es sencillo, pero un par de casillas mal marcadas pueden cambiar cómo '
                    'se reparte la responsabilidad. Lo repasamos apartado por apartado.',
         'cuerpo': [('p',
                     'El [[parte-amistoso|parte amistoso]], cuyo nombre oficial es Declaración Amistosa de '
                     'Accidente, es un documento con el mismo formato en toda Europa. Sirve para que los dos '
                     'conductores implicados en un accidente describan juntos lo ocurrido y lo firmen. Con '
                     'él, las aseguradoras pueden resolver el [[siniestro|siniestro]] mucho más rápido. '
                     'Lleva siempre uno en la guantera, y si vas a alquilar, comprueba que el coche también '
                     'lo tiene.'),
                    ('h2', 'Antes de empezar'),
                    ('ul',
                     ['Usa un solo juego: es un documento autocopiativo, con una hoja para cada conductor.',
                      'Escribe con bolígrafo y apretando, para que se lea bien la copia.',
                      'Cada conductor rellena su columna: el vehículo A a un lado y el B al otro. No importa '
                      'quién sea A o B.',
                      'Si no habláis el mismo idioma, las casillas numeradas son iguales en todas las '
                      'versiones, lo que ayuda a entenderse.']),
                    ('h2', 'Los datos comunes'),
                    ('p',
                     'La parte superior recoge la fecha, la hora, el lugar exacto, si hubo heridos, si hubo '
                     'daños a otros vehículos u objetos y los datos de los testigos. Sé preciso con el '
                     'lugar: nombre de la calle o carretera, punto kilométrico si lo sabes, y municipio.'),
                    ('h2', 'Tu columna'),
                    ('p',
                     'Cada conductor anota los datos del tomador del seguro, del vehículo, de la aseguradora '
                     '(nombre, número de póliza y validez) y del conductor (permiso de conducir). Tenlo a '
                     'mano: la documentación del coche y el recibo o certificado del seguro facilitan mucho '
                     'este paso.'),
                    ('h2', 'Las circunstancias: la parte más importante'),
                    ('p',
                     'En el centro hay una lista de situaciones numeradas: estaba estacionado, salía de un '
                     'aparcamiento, cambiaba de carril, circulaba en el mismo sentido, no respetó un stop, '
                     'etc. Cada conductor marca las que describen lo que hacía en el momento del choque. Al '
                     'final se anota el número total de casillas marcadas en cada columna.'),
                    ('p',
                     'Ese número evita que alguien añada cruces después. Y esas casillas son lo primero que '
                     'miran las aseguradoras para repartir responsabilidades, así que tómate tu tiempo. Si '
                     'ninguna encaja del todo, no marques una que no corresponde.'),
                    ('h2', 'El croquis'),
                    ('p',
                     'Dibuja la vía, los carriles, el sentido de circulación de cada coche con flechas, la '
                     'posición en el momento del choque y las señales de tráfico relevantes. No hace falta '
                     'ser un artista, pero sí que se entienda. Indica también el punto de impacto inicial en '
                     'cada vehículo, en el pequeño dibujo del coche.'),
                    ('h2', 'Daños y observaciones'),
                    ('p',
                     'Describe los daños visibles de tu vehículo. En observaciones puedes añadir lo que '
                     'consideres importante, por ejemplo que el otro conductor reconoce que no respetó la '
                     'preferencia. Evita opiniones o frases largas.'),
                    ('h2', 'Firmar y repartir'),
                    ('ol',
                     ['Revisa todo antes de firmar. Una vez firmado, no se debe modificar.',
                      'Firman los dos conductores.',
                      'Separad las hojas: cada uno se queda con una.',
                      'Haz una foto del parte por si acaso.',
                      'Envíalo a tu aseguradora en el plazo de pocos días que marca tu póliza.']),
                    ('quote',
                     'Si no estás de acuerdo con lo que el otro quiere escribir, no firmes. Es mejor que '
                     'cada uno dé su versión por separado que firmar algo que no refleja lo ocurrido.'),
                    ('nota',
                     'El parte amistoso está pensado sobre todo para accidentes sin heridos entre dos '
                     'vehículos. Si hay heridos, llama al 112.'),
                    ('p',
                     'Tienes una explicación más detallada en nuestra [guía del parte '
                     'amistoso](guia-parte-amistoso.html). Y si tu coche ha sufrido daños, en Green Car '
                     'Service Tenerife nos encargamos de la [peritación](guia-peritacion.html) y de la '
                     '[gestión con tu aseguradora](servicio-gestion-con-aseguradoras.html).')]},
  'en': {'titulo': 'How to fill in the accident report form correctly',
         'resumen': 'The Spanish accident report form is simple, but a couple of wrongly ticked boxes can '
                    'change how liability is shared. We go through it section by section.',
         'cuerpo': [('p',
                     'The [[parte-amistoso|accident report form]], known in Spain as the ‘parte amistoso’ '
                     'and officially the ‘Declaración Amistosa de Accidente’, uses the same layout '
                     'throughout Europe. It lets the two drivers involved in an accident describe together '
                     'what happened and sign it. With it, the insurers can settle the [[siniestro|claim]] '
                     'much faster. Always keep one in the glovebox, and if you hire a car, check it has one '
                     'too.'),
                    ('h2', 'Before you start'),
                    ('ul',
                     ['Use a single set: it is a carbonless form, with one sheet for each driver.',
                      'Write in ballpoint pen and press firmly so the copy is legible.',
                      'Each driver fills in their own column: vehicle A on one side and B on the other. It '
                      'doesn’t matter who is A or B.',
                      'If you don’t share a language, the numbered boxes are the same in every version, '
                      'which helps you understand each other.']),
                    ('h2', 'Shared details'),
                    ('p',
                     'The top section records the date, time, exact location, whether anyone was hurt, '
                     'whether other vehicles or objects were damaged, and witness details. Be precise about '
                     'the location: street or road name, kilometre marker if you know it, and municipality.'),
                    ('h2', 'Your column'),
                    ('p',
                     'Each driver writes down the details of the policyholder, the vehicle, the insurer '
                     '(name, policy number and validity) and the driver (driving licence). Keep them to '
                     'hand: the car’s documents and the insurance receipt or certificate make this step much '
                     'easier.'),
                    ('h2', 'Circumstances: the most important part'),
                    ('p',
                     'In the middle there is a list of numbered situations: parked, leaving a car park, '
                     'changing lanes, travelling in the same direction, failed to stop at a stop sign, and '
                     'so on. Each driver ticks the ones that describe what they were doing at the moment of '
                     'impact. At the end, the total number of boxes ticked in each column is written down.'),
                    ('p',
                     'That number prevents anyone adding crosses later. And those boxes are the first thing '
                     'insurers look at to share out liability, so take your time. If none fits exactly, '
                     'don’t tick one that doesn’t apply.'),
                    ('h2', 'The sketch'),
                    ('p',
                     'Draw the road, the lanes, each car’s direction of travel with arrows, their positions '
                     'at the moment of impact and any relevant road signs. You don’t need to be an artist, '
                     'but it does need to be clear. Also mark the initial point of impact on each vehicle, '
                     'on the small drawing of the car.'),
                    ('h2', 'Damage and remarks'),
                    ('p',
                     'Describe the visible damage to your vehicle. Under remarks you can add anything you '
                     'consider important, for example that the other driver accepts they failed to give way. '
                     'Avoid opinions or long sentences.'),
                    ('h2', 'Signing and splitting'),
                    ('ol',
                     ['Check everything before signing. Once signed, it should not be changed.',
                      'Both drivers sign.',
                      'Separate the sheets: each keeps one.',
                      'Take a photo of the form just in case.',
                      'Send it to your insurer within the few days your policy allows.']),
                    ('quote',
                     'If you don’t agree with what the other driver wants to write, don’t sign. It’s better '
                     'for each of you to give your own version separately than to sign something that '
                     'doesn’t reflect what happened.'),
                    ('nota',
                     'The form is mainly intended for accidents between two vehicles with no injuries. If '
                     'anyone is hurt, call 112.'),
                    ('p',
                     'You’ll find a more detailed explanation in our [accident report form '
                     'guide](guia-parte-amistoso.html). And if your car has been damaged, at Green Car '
                     'Service Tenerife we take care of the [loss assessment](guia-peritacion.html) and '
                     '[dealing with your insurer](servicio-gestion-con-aseguradoras.html).')]}},
 {'slug': 'articulo-puedo-elegir-taller',
  'cat': 'seguros-siniestros',
  'fecha': '2024-02-27',
  'es': {'titulo': '¿Puedo elegir taller aunque la aseguradora me mande a otro?',
         'resumen': 'Tras un siniestro, muchas compañías te proponen un taller concertado. En la mayoría de '
                    'los casos puedes elegir otro. Te explicamos cuándo y qué conviene revisar en tu póliza.',
         'cuerpo': [('p',
                     'Es una escena habitual: llamas a tu aseguradora para dar parte y, casi en la misma '
                     'frase, te indican a qué taller debes llevar el coche. Muchos conductores entienden que '
                     'es obligatorio. En general no lo es. La [[libre-eleccion-de-taller|libre elección de '
                     'taller]] es un principio muy extendido en los seguros de automóvil, aunque cómo se '
                     'aplica depende de tu póliza y de quién tenga la culpa del accidente.'),
                    ('h2', 'Si la culpa es del otro'),
                    ('p',
                     'Cuando el accidente lo causa otro conductor, reclamas los daños a su aseguradora. En '
                     'ese caso, lo razonable es que puedas reparar donde tú decidas: la compañía contraria '
                     'debe indemnizarte por los daños, no imponerte dónde se arreglan. Un [[perito|perito]] '
                     'valorará la reparación y el taller que elijas trabajará sobre esa valoración.'),
                    ('h2', 'Si reclamas a tu propio seguro'),
                    ('p',
                     'Cuando el daño lo cubre tu propia póliza, por ejemplo un [[todo-riesgo|seguro a todo '
                     'riesgo]] en un golpe en el que la culpa es tuya, lo que manda es el contrato. Hay '
                     'pólizas que dejan elegir cualquier taller sin condiciones. Otras ofrecen ventajas si '
                     'usas su red de talleres, como no pagar la franquicia o recibir un coche de '
                     'sustitución. Y algunas, sobre todo las más económicas, limitan la reparación a '
                     'talleres concertados o reducen la cobertura si vas a otro.'),
                    ('p',
                     'Por eso merece la pena buscar en las condiciones de tu póliza frases como «libre '
                     'elección de taller», «talleres concertados» o «red de talleres». Si no lo encuentras o '
                     'no lo entiendes, pregunta a tu mediador o a la compañía y pide la respuesta por '
                     'escrito.'),
                    ('h2', 'Por qué te proponen un taller'),
                    ('p',
                     'Las aseguradoras tienen acuerdos con talleres para agilizar trámites y controlar '
                     'costes. No tiene nada de malo y puede ser una buena opción. Pero tú eres quien conoce '
                     'tu coche y quien va a convivir con la reparación. Puede que prefieras un taller de '
                     'confianza, más cerca de casa o con servicios que te interesan.'),
                    ('h2', 'Qué hacer si quieres ir a tu taller'),
                    ('ol',
                     ['Comunica el siniestro a tu aseguradora como siempre, dentro de plazo.',
                      'Indica que quieres reparar en el taller que tú elijas y facilita sus datos.',
                      'Lleva el coche al taller: desde allí se coordina la visita del perito.',
                      'Revisa el presupuesto y la valoración antes de autorizar la reparación.']),
                    ('h2', 'Preguntas que conviene hacer'),
                    ('ul',
                     ['¿Mi póliza permite la libre elección de taller? ¿Con alguna condición?',
                      '¿Pierdo alguna ventaja, como el vehículo de sustitución, si no voy al concertado?',
                      '¿Tengo franquicia? ¿Se aplica igual en cualquier taller?',
                      '¿Quién paga al taller: la aseguradora directamente o yo, y luego me reembolsan?']),
                    ('nota',
                     'Las condiciones varían entre compañías y pólizas. Lo que te contamos aquí es general; '
                     'la referencia es siempre tu contrato.'),
                    ('p',
                     'En Green Car Service Tenerife trabajamos con tu compañía de seguros y nos encargamos '
                     'de coordinar la peritación y los trámites. Lee nuestra [guía de libre elección de '
                     'taller](guia-libre-eleccion-de-taller.html) y conoce nuestro servicio de [gestión con '
                     'aseguradoras](servicio-gestion-con-aseguradoras.html).')]},
  'en': {'titulo': 'Can I choose my garage if the insurer sends me elsewhere?',
         'resumen': 'After a claim, many insurers suggest one of their approved garages. In most cases you '
                    'can choose another. We explain when, and what to check in your policy.',
         'cuerpo': [('p',
                     'It’s a familiar scene: you call your insurer to report an accident and, almost in the '
                     'same breath, they tell you which garage to take the car to. Many drivers assume it’s '
                     'compulsory. Generally, it isn’t. [[libre-eleccion-de-taller|Free choice of repairer]] '
                     'is a widespread principle in Spanish car insurance, although how it applies depends '
                     'on your policy and on who was at fault.'),
                    ('h2', 'If the other driver was at fault'),
                    ('p',
                     'When another driver causes the accident, you claim for the damage from their insurer. '
                     'In that case, it’s reasonable that you should be able to have the repair done wherever '
                     'you choose: the other insurer has to compensate you for the damage, not dictate where '
                     'it gets fixed. A [[perito|loss adjuster]] will assess the repair and the garage you '
                     'choose works from that assessment.'),
                    ('h2', 'If you claim on your own policy'),
                    ('p',
                     'When the damage is covered by your own policy, for example [[todo-riesgo|comprehensive '
                     'insurance]] after a bump that was your fault, the contract is what counts. Some '
                     'policies let you use any garage without conditions. Others offer advantages if you use '
                     'their network, such as not paying the excess or getting a courtesy car. And some, '
                     'especially the cheaper ones, limit repairs to approved garages or reduce cover if you '
                     'go elsewhere.'),
                    ('p',
                     'So it’s worth searching your policy terms for phrases like ‘libre elección de taller’ '
                     '(free choice of repairer), ‘talleres concertados’ (approved garages) or ‘red de '
                     'talleres’ (garage network). If you can’t find it or don’t understand it, ask your '
                     'broker or the insurer and get the answer in writing.'),
                    ('h2', 'Why they suggest a garage'),
                    ('p',
                     'Insurers have agreements with garages to speed up paperwork and control costs. There’s '
                     'nothing wrong with that and it can be a good option. But you’re the one who knows your '
                     'car and who will live with the repair. You may prefer a garage you trust, one closer '
                     'to home or one offering services you value.'),
                    ('h2', 'What to do if you want to use your garage'),
                    ('ol',
                     ['Report the claim to your insurer as usual, within the deadline.',
                      'Say that you want the repair done at the garage of your choice and give its details.',
                      'Take the car to the garage: the adjuster’s visit is arranged from there.',
                      'Check the estimate and the assessment before authorising the repair.']),
                    ('h2', 'Questions worth asking'),
                    ('ul',
                     ['Does my policy allow free choice of repairer? Are there conditions?',
                      'Do I lose any benefits, such as a courtesy car, if I don’t use an approved garage?',
                      'Do I have an excess? Does it apply the same at any garage?',
                      'Who pays the garage: the insurer directly, or me with a refund later?']),
                    ('nota',
                     'Terms vary between insurers and policies. What we describe here is general; your '
                     'contract is always the reference.'),
                    ('p',
                     'At Green Car Service Tenerife we work with your insurance company and take care of '
                     'coordinating the assessment and paperwork. Read our [free choice of repairer '
                     'guide](guia-libre-eleccion-de-taller.html) and find out about our [insurance handling '
                     'service](servicio-gestion-con-aseguradoras.html).')]}},
 {'slug': 'articulo-franquicia-cuando-compensa',
  'cat': 'seguros-siniestros',
  'fecha': '2024-10-15',
  'es': {'titulo': 'Qué es la franquicia y cuándo compensa',
         'resumen': 'El seguro a todo riesgo con franquicia es más barato, pero cada siniestro te cuesta '
                    'algo. Te explicamos cómo funciona y cómo decidir si te conviene.',
         'cuerpo': [('p',
                     'Cuando comparas seguros de coche aparece enseguida la palabra '
                     '[[franquicia|franquicia]]. Es la parte de cada siniestro que pagas tú. Si tu póliza '
                     'tiene una franquicia de una cantidad determinada y la reparación cuesta más, tú pagas '
                     'esa cantidad y la aseguradora el resto. Si la reparación cuesta menos, la pagas entera '
                     'tú y normalmente no merece la pena dar parte.'),
                    ('h2', 'Dónde se aplica'),
                    ('p',
                     'La franquicia es típica de los seguros a todo riesgo, y se aplica sobre todo a los '
                     'daños propios, es decir, a la reparación de tu coche cuando la culpa es tuya o no hay '
                     'un tercero identificado. No afecta a la responsabilidad civil: si dañas otro coche, la '
                     'aseguradora paga al perjudicado completo. Y si el accidente lo causa otro conductor, '
                     'reclamas a su seguro y no deberías pagar franquicia por tu reparación.'),
                    ('p',
                     'Algunas pólizas tienen franquicias distintas según la cobertura (lunas, robo, daños '
                     'propios) o la reducen si reparas en un taller de su red. Revisa las condiciones para '
                     'saber exactamente cuánto y cuándo pagas.'),
                    ('h2', 'Por qué es más barato'),
                    ('p',
                     'Al asumir tú los daños pequeños, la aseguradora se ahorra gestionar muchos partes de '
                     'poco importe. Por eso el precio del [[todo-riesgo|todo riesgo]] con franquicia suele '
                     'ser bastante menor que el del todo riesgo sin ella, y suele quedar por encima del '
                     'seguro a terceros ampliado.'),
                    ('h2', 'Cuándo compensa'),
                    ('ul',
                     ['Si conduces con cuidado y rara vez tienes golpes, porque pagarás la franquicia pocas '
                      'veces.',
                      'Si tu coche tiene cierto valor y quieres protección ante un siniestro grande, sin '
                      'pagar el todo riesgo completo.',
                      'Si tienes margen para asumir la franquicia de una vez si hace falta.',
                      'Si aparcas en la calle y te preocupan daños importantes, más que los pequeños '
                      'roces.']),
                    ('h2', 'Cuándo quizá no'),
                    ('ul',
                     ['Si tienes pequeños golpes con frecuencia, por ejemplo aparcando en zonas muy '
                      'concurridas.',
                      'Si pagar la franquicia de golpe te supondría un problema.',
                      'Si el coche es antiguo y de poco valor: a veces es más razonable un seguro a terceros '
                      'ampliado.']),
                    ('h2', 'Un cálculo sencillo'),
                    ('p',
                     'Compara la diferencia anual entre el todo riesgo sin franquicia y el que la tiene. '
                     'Luego piensa cuántos siniestros con culpa propia sueles tener al año. Si la diferencia '
                     'de precio es mayor que lo que te costaría pagar la franquicia en esos siniestros, la '
                     'franquicia te compensa. No es una ciencia exacta, pero ayuda a decidir con datos '
                     'propios y no por intuición.'),
                    ('h2', 'En el taller'),
                    ('p',
                     'Cuando llega el momento de reparar, el taller cobra a la aseguradora lo que le '
                     'corresponde y a ti la franquicia. Pide que la cantidad quede clara en el '
                     '[[presupuesto|presupuesto]] y en la factura. Si el daño es pequeño y quizá no compense '
                     'dar parte, pide un presupuesto antes de decidir: así sabrás si la reparación supera o '
                     'no tu franquicia.'),
                    ('nota',
                     'Dar parte de un siniestro puede afectar a tu bonificación en la renovación, según la '
                     'política de cada compañía. Pregunta antes si tienes dudas.'),
                    ('p',
                     'En Green Car Service Tenerife te damos un [presupuesto](presupuesto.html) claro para '
                     'que decidas con información si dar parte o no, y cuando lo das, nos encargamos de la '
                     '[gestión con tu aseguradora](servicio-gestion-con-aseguradoras.html).')]},
  'en': {'titulo': 'What an insurance excess is and when it pays off',
         'resumen': 'Comprehensive cover with an excess is cheaper, but every claim costs you something. We '
                    'explain how it works and how to decide whether it suits you.',
         'cuerpo': [('p',
                     'When you compare car insurance, the word [[franquicia|excess]] (‘franquicia’ in '
                     'Spanish) crops up straight away. It’s the part of each claim you pay yourself. If your '
                     'policy has an excess of a certain amount and the repair costs more, you pay that '
                     'amount and the insurer pays the rest. If the repair costs less, you pay it all '
                     'yourself and it usually isn’t worth making a claim.'),
                    ('h2', 'Where it applies'),
                    ('p',
                     'An excess is typical of comprehensive policies, and applies mainly to own damage, '
                     'meaning the repair of your car when you were at fault or there is no identified third '
                     'party. It doesn’t affect third-party liability: if you damage another car, the insurer '
                     'pays the other party in full. And if another driver causes the accident, you claim on '
                     'their insurance and shouldn’t pay an excess for your repair.'),
                    ('p',
                     'Some policies have different excesses depending on the cover (glass, theft, own '
                     'damage) or reduce it if you use one of their network garages. Check the terms to know '
                     'exactly how much and when you pay.'),
                    ('h2', 'Why it’s cheaper'),
                    ('p',
                     'Because you take on the small damage, the insurer avoids handling lots of low-value '
                     'claims. That’s why [[todo-riesgo|comprehensive insurance]] with an excess is usually '
                     'noticeably cheaper than without one, and usually sits above extended third-party '
                     'cover.'),
                    ('h2', 'When it pays off'),
                    ('ul',
                     ['If you drive carefully and rarely have bumps, because you’ll seldom pay the excess.',
                      'If your car has some value and you want protection against a major claim without '
                      'paying for full comprehensive.',
                      'If you could afford to pay the excess in one go if needed.',
                      'If you park on the street and worry more about serious damage than small scrapes.']),
                    ('h2', 'When it might not'),
                    ('ul',
                     ['If you often have small knocks, for example parking in very busy areas.',
                      'If paying the excess all at once would be a problem.',
                      'If the car is old and worth little: sometimes extended third-party cover makes more '
                      'sense.']),
                    ('h2', 'A simple calculation'),
                    ('p',
                     'Compare the yearly difference between comprehensive with no excess and with one. Then '
                     'think about how many at-fault claims you usually have per year. If the price '
                     'difference is greater than what you would pay in excess for those claims, the excess '
                     'pays off. It isn’t an exact science, but it helps you decide based on your own figures '
                     'rather than gut feeling.'),
                    ('h2', 'At the garage'),
                    ('p',
                     'When it comes to the repair, the garage charges the insurer its share and charges you '
                     'the excess. Ask for the amount to be clear on the [[presupuesto|repair estimate]] and '
                     'the invoice. If the damage is small and a claim may not be worth it, ask for an '
                     'estimate before deciding: you’ll know whether the repair exceeds your excess or not.'),
                    ('nota',
                     'Making a claim can affect your no-claims discount at renewal, depending on each '
                     'insurer’s policy. Ask beforehand if in doubt.'),
                    ('p',
                     'At Green Car Service Tenerife we give you a clear [estimate](presupuesto.html) so you '
                     'can make an informed decision about claiming, and when you do claim, we take care of '
                     '[dealing with your insurer](servicio-gestion-con-aseguradoras.html).')]}},
 {'slug': 'articulo-que-es-la-perdida-total',
  'cat': 'seguros-siniestros',
  'fecha': '2025-05-06',
  'es': {'titulo': 'Qué es la pérdida total y qué opciones tienes',
         'resumen': 'Que la aseguradora declare tu coche siniestro total no siempre significa que no se '
                    'pueda reparar. Te explicamos cómo se decide, qué te pagan y qué puedes hacer.',
         'cuerpo': [('p',
                     'Pocas llamadas sientan peor que la de la aseguradora diciendo que tu coche es '
                     '[[perdida-total|pérdida total]], también llamado siniestro total. Mucha gente entiende '
                     'que el coche ha quedado destrozado, pero no siempre es así. En la mayoría de los casos '
                     'es una decisión económica: repararlo costaría más de lo que la compañía considera que '
                     'vale el coche.'),
                    ('h2', 'Cómo se decide'),
                    ('p',
                     'Tras el accidente, un [[perito|perito]] valora los daños y calcula cuánto costaría la '
                     'reparación. Esa cifra se compara con el valor que se atribuye al vehículo. Si la '
                     'reparación supera ese valor, o el porcentaje de él que marque tu póliza, se declara la '
                     'pérdida total. También puede declararse cuando el daño afecta a la estructura de tal '
                     'forma que no es seguro repararlo.'),
                    ('h2', 'Qué valor tiene tu coche para el seguro'),
                    ('p', 'Aquí está la clave, y depende de quién tenga la culpa y de tu contrato:'),
                    ('ul',
                     ['**Valor venal:** lo que costaría comprar un coche igual, de la misma antigüedad y en '
                      'estado parecido, justo antes del accidente. Es el valor más bajo.',
                      '**Valor de mercado:** similar, basado en lo que se paga por coches equivalentes en el '
                      'mercado de segunda mano.',
                      '**Valor a nuevo:** algunas pólizas de todo riesgo lo pagan durante los primeros años '
                      'del coche.']),
                    ('p',
                     'Cuando el accidente lo causa otro y reclamas a su seguro, es habitual que la '
                     'indemnización incluya el valor venal más una cantidad adicional por los perjuicios de '
                     'tener que buscar otro coche, lo que se conoce como valor de afección. Cómo se calcula '
                     'depende del caso; si no estás de acuerdo con la cifra, puedes discutirla.'),
                    ('h2', 'Tus opciones'),
                    ('ol',
                     ['**Aceptar la indemnización y entregar el coche.** La aseguradora se queda con el '
                      'vehículo y gestiona su baja o su venta como restos.',
                      '**Aceptar la indemnización y quedarte el coche.** Muchas compañías lo permiten '
                      'descontando el valor de los restos. Luego puedes repararlo por tu cuenta si te '
                      'compensa.',
                      '**No estar de acuerdo con la valoración.** Puedes aportar pruebas del valor real de '
                      'tu coche: anuncios de coches equivalentes, facturas de mantenimiento, extras, estado '
                      'general. Y, si hace falta, pedir una segunda valoración con un perito propio.']),
                    ('h2', '¿Cuándo tiene sentido repararlo igualmente?'),
                    ('p',
                     'A veces la cifra de la aseguradora se queda corta respecto a lo que te costaría '
                     'encontrar un coche igual de fiable, sobre todo si el tuyo está muy cuidado o tiene '
                     'pocos kilómetros. Si te quedas con el coche, conviene pedir un '
                     '[[presupuesto|presupuesto]] realista y valorar si la reparación, con recambios nuevos '
                     'o de calidad equivalente, deja el coche en condiciones seguras. Si la estructura está '
                     'afectada, la reparación debe hacerse en [[bancada|bancada]] y con garantías.'),
                    ('h2', 'Qué no hacer'),
                    ('ul',
                     ['No firmes el finiquito sin leer bien qué cantidad aceptas y qué pasa con el coche.',
                      'No des por buena la primera cifra si te parece baja: pregunta cómo se ha calculado.',
                      'No olvides retirar tus objetos personales del coche y, si hay equipamiento añadido, '
                      'avisar a la compañía.']),
                    ('nota',
                     'Las condiciones concretas dependen de tu póliza y de si reclamas a tu aseguradora o a '
                     'la del contrario. Cada caso es distinto.'),
                    ('p',
                     'En Green Car Service Tenerife te ayudamos a entender la valoración, te damos un '
                     'presupuesto independiente y, si decides reparar, lo hacemos con bancada y equipamiento '
                     'adecuados. Tienes más detalles en nuestra [guía de pérdida '
                     'total](guia-perdida-total.html) y en nuestra [guía de la '
                     'peritación](guia-peritacion.html).')]},
  'en': {'titulo': 'What a total loss is and what your options are',
         'resumen': 'An insurer writing your car off doesn’t always mean it can’t be repaired. We explain '
                    'how the decision is made, what you get paid and what you can do.',
         'cuerpo': [('p',
                     'Few phone calls feel worse than the insurer telling you your car is a '
                     '[[perdida-total|total loss]], or a write-off. Many people assume the car has been '
                     'wrecked, but that isn’t always the case. Usually it’s an economic decision: repairing '
                     'it would cost more than the insurer considers the car to be worth.'),
                    ('h2', 'How it’s decided'),
                    ('p',
                     'After the accident, a [[perito|loss adjuster]] assesses the damage and works out what '
                     'the repair would cost. That figure is compared with the value attributed to the '
                     'vehicle. If the repair exceeds that value, or the percentage of it set in your policy, '
                     'the car is declared a total loss. It can also be declared when the damage affects the '
                     'structure in a way that makes repair unsafe.'),
                    ('h2', 'What your car is worth to the insurer'),
                    ('p', 'This is the key point, and it depends on who was at fault and on your contract:'),
                    ('ul',
                     ['**Pre-accident value (‘valor venal’):** what it would cost to buy an identical car of '
                      'the same age and in similar condition just before the accident. It is the lowest '
                      'value.',
                      '**Market value:** similar, based on what equivalent cars sell for on the used market.',
                      '**New-for-old value:** some comprehensive policies pay this during the first few '
                      'years of the car’s life.']),
                    ('p',
                     'When another driver caused the accident and you claim on their insurance, compensation '
                     'commonly includes the pre-accident value plus an additional amount for the '
                     'inconvenience of having to find another car, known in Spain as ‘valor de afección’. '
                     'How it’s worked out depends on the case; if you don’t agree with the figure, you can '
                     'challenge it.'),
                    ('h2', 'Your options'),
                    ('ol',
                     ['**Accept the payout and hand over the car.** The insurer keeps the vehicle and '
                      'handles its deregistration or sale as salvage.',
                      '**Accept the payout and keep the car.** Many insurers allow this, deducting the '
                      'salvage value. You can then repair it yourself if it’s worth it.',
                      '**Dispute the valuation.** You can provide evidence of your car’s real value: adverts '
                      'for equivalent cars, service invoices, extras, overall condition. And, if necessary, '
                      'ask for a second assessment by your own adjuster.']),
                    ('h2', 'When does it still make sense to repair?'),
                    ('p',
                     'Sometimes the insurer’s figure falls short of what it would cost to find an equally '
                     'reliable car, especially if yours is well looked after or has low mileage. If you keep '
                     'the car, get a realistic [[presupuesto|repair estimate]] and consider whether the '
                     'repair, with new or equivalent-quality parts, leaves the car safe. If the structure is '
                     'affected, the repair must be done on a [[bancada|chassis jig]] and with proper '
                     'guarantees.'),
                    ('h2', 'What not to do'),
                    ('ul',
                     ['Don’t sign the settlement without reading carefully what amount you’re accepting and '
                      'what happens to the car.',
                      'Don’t accept the first figure if it seems low: ask how it was calculated.',
                      'Don’t forget to remove your personal belongings and, if you’ve added equipment, tell '
                      'the insurer.']),
                    ('nota',
                     'The exact terms depend on your policy and on whether you’re claiming from your own '
                     'insurer or the other party’s. Every case is different.'),
                    ('p',
                     'At Green Car Service Tenerife we help you understand the valuation, give you an '
                     'independent estimate and, if you decide to repair, do it with the right jig and '
                     'equipment. There’s more detail in our [total loss guide](guia-perdida-total.html) and '
                     'our [loss assessment guide](guia-peritacion.html).')]}},
 {'slug': 'articulo-que-hace-el-perito',
  'cat': 'seguros-siniestros',
  'fecha': '2025-11-25',
  'es': {'titulo': 'Qué hace el perito del seguro y cómo prepararte',
         'resumen': 'El perito decide qué se repara y cómo tras un siniestro. Entender su trabajo te ayuda a '
                    'que la valoración sea completa y a saber qué hacer si no estás de acuerdo.',
         'cuerpo': [('p',
                     'Después de dar parte de un accidente, casi siempre aparece una figura clave: el '
                     '[[perito|perito]]. Es un profesional especializado en valorar daños de vehículos que, '
                     'normalmente, trabaja para la aseguradora. Su informe determina qué piezas se reparan o '
                     'se cambian, cuántas horas de mano de obra se reconocen y, en los casos graves, si el '
                     'coche es pérdida total.'),
                    ('h2', 'Qué hace exactamente'),
                    ('ul',
                     ['Inspecciona el vehículo, normalmente en el taller, y en algunos casos de forma remota '
                      'a partir de fotos y vídeos.',
                      'Comprueba que los daños son coherentes con el accidente declarado.',
                      'Decide qué piezas se reparan y cuáles se sustituyen.',
                      'Valora la mano de obra de chapa y pintura según [[baremo|baremos]] y tiempos de '
                      'referencia.',
                      'Emite un informe que la aseguradora usa para autorizar la reparación o la '
                      'indemnización.']),
                    ('h2', 'Por qué es mejor que el coche esté en el taller'),
                    ('p',
                     'Muchos daños no se ven a simple vista. Tras un golpe en el paragolpes delantero, por '
                     'ejemplo, puede haber soportes rotos, refuerzos doblados o el frente interior deformado. Si la '
                     '[[peritacion|peritación]] se hace con el coche en el taller, se pueden desmontar '
                     'piezas y enseñar al perito todo lo que hay detrás. Si aparecen daños ocultos después, '
                     'el taller informa a la aseguradora y se hace una ampliación de la peritación.'),
                    ('h2', 'Cómo prepararte'),
                    ('ol',
                     ['Guarda las fotos que hiciste en el lugar del accidente y el parte amistoso.',
                      'Anota todo lo que notes raro desde el golpe: puertas que cierran mal, ruidos de '
                      'carrocería, piezas sueltas.',
                      'Si tu coche tiene extras o equipamiento especial, tenlo documentado.',
                      'Si tenías daños previos sin relación con el accidente, dilo con claridad. Evita '
                      'malentendidos.',
                      'Lleva el coche a tu taller de confianza: sabe qué revisar y habla el mismo idioma '
                      'técnico que el perito.']),
                    ('h2', 'Recambios: original o equivalente'),
                    ('p',
                     'El perito puede valorar la reparación con [[recambio-original|recambios originales]] o '
                     'con recambios de calidad equivalente, según la póliza y el tipo de pieza. Pregunta qué '
                     'se ha previsto en tu caso, sobre todo en coches nuevos o en piezas de seguridad.'),
                    ('h2', 'Si no estás de acuerdo'),
                    ('p',
                     'Puede ocurrir que la valoración te parezca insuficiente: que no se reconozca una pieza '
                     'dañada, que se proponga reparar algo que crees que debería cambiarse o que el valor '
                     'del coche en una pérdida total te parezca bajo. En ese caso:'),
                    ('ul',
                     ['Pide que te expliquen el criterio y, si es posible, el informe por escrito.',
                      'Aporta pruebas: fotos, presupuesto del taller, facturas o anuncios de coches '
                      'equivalentes.',
                      'Si no hay acuerdo, la ley permite en muchos casos acudir a una peritación '
                      'contradictoria con un perito designado por ti. Consulta las condiciones y costes en '
                      'tu póliza.']),
                    ('nota',
                     'El perito valora los daños; la decisión de cómo se repara con calidad es del taller. '
                     'Un buen diálogo entre los dos es lo que mejor protege tu coche.'),
                    ('p',
                     'En Green Car Service Tenerife trabajamos a diario con peritos: preparamos el coche, '
                     'mostramos los daños y defendemos una reparación correcta. Lee nuestra [guía de la '
                     'peritación](guia-peritacion.html) y conoce nuestro servicio de [gestión con '
                     'aseguradoras](servicio-gestion-con-aseguradoras.html).')]},
  'en': {'titulo': 'What the insurance loss adjuster does and how to prepare',
         'resumen': 'The loss adjuster decides what gets repaired and how after a claim. Understanding their '
                    'job helps you get a complete assessment and know what to do if you disagree.',
         'cuerpo': [('p',
                     'After you report an accident, a key figure almost always appears: the [[perito|loss '
                     'adjuster]] (‘perito’). They are a specialist in assessing vehicle damage and normally '
                     'work for the insurer. Their report determines which parts are repaired or replaced, '
                     'how many hours of labour are accepted and, in serious cases, whether the car is a '
                     'total loss.'),
                    ('h2', 'What exactly they do'),
                    ('ul',
                     ['Inspect the vehicle, usually at the garage and sometimes remotely using photos and '
                      'videos.',
                      'Check that the damage is consistent with the reported accident.',
                      'Decide which parts are repaired and which are replaced.',
                      'Assess bodywork and paint labour using [[baremo|standard schedules]] and reference '
                      'times.',
                      'Issue a report the insurer uses to authorise the repair or payout.']),
                    ('h2', 'Why it’s better for the car to be at the garage'),
                    ('p',
                     'A lot of damage can’t be seen at a glance. After a hit on the front bumper, for '
                     'example, there may be broken brackets, bent reinforcements or a distorted inner front panel. If '
                     'the [[peritacion|loss assessment]] is done with the car at the garage, parts can be '
                     'removed to show the adjuster everything behind them. If hidden damage turns up later, '
                     'the garage informs the insurer and the assessment is extended.'),
                    ('h2', 'How to prepare'),
                    ('ol',
                     ['Keep the photos you took at the scene and the accident report form.',
                      'Note anything odd since the impact: doors that do not shut properly, body rattles, loose parts.',
                      'If your car has extras or special equipment, have it documented.',
                      'If there was previous damage unrelated to the accident, say so clearly. It avoids '
                      'misunderstandings.',
                      'Take the car to a garage you trust: it knows what to check and speaks the same '
                      'technical language as the adjuster.']),
                    ('h2', 'Parts: original or equivalent'),
                    ('p',
                     'The adjuster may base the repair on [[recambio-original|original parts]] or on '
                     'equivalent-quality parts, depending on the policy and the type of part. Ask what has '
                     'been allowed in your case, especially on newer cars or safety-related parts.'),
                    ('h2', 'If you disagree'),
                    ('p',
                     'The assessment may seem insufficient to you: a damaged part not accepted, a repair '
                     'proposed where you think a replacement is needed, or the value given to your car in a '
                     'total loss seems low. In that case:'),
                    ('ul',
                     ['Ask them to explain their reasoning and, if possible, to give you the report in '
                      'writing.',
                      'Provide evidence: photos, the garage’s estimate, invoices or adverts for equivalent '
                      'cars.',
                      'If you still can’t agree, Spanish law in many cases allows an independent '
                      'counter-assessment with an adjuster you appoint. Check the conditions and costs in '
                      'your policy.']),
                    ('nota',
                     'The adjuster assesses the damage; how to carry out a quality repair is the garage’s '
                     'call. Good communication between the two is what best protects your car.'),
                    ('p',
                     'At Green Car Service Tenerife we work with loss adjusters every day: we prepare the '
                     'car, show the damage and argue for a proper repair. Read our [loss assessment '
                     'guide](guia-peritacion.html) and find out about our [insurance handling '
                     'service](servicio-gestion-con-aseguradoras.html).')]}},
 {'slug': 'articulo-tus-derechos-en-el-taller',
  'cat': 'particulares',
  'fecha': '2024-05-14',
  'es': {'titulo': 'Tus derechos en el taller: presupuesto, resguardo y garantía',
         'resumen': 'La normativa sobre talleres te da derecho a un presupuesto por escrito, a un resguardo '
                    'cuando dejas el coche y a una garantía mínima en la reparación. Te lo contamos en '
                    'claro.',
         'cuerpo': [('p',
                     'Dejar el coche en un taller implica confiar. Pero esa confianza no tiene por qué ser a '
                     'ciegas: en España, el Real Decreto 1457/1986, que regula la actividad de los talleres '
                     'de reparación, reconoce una serie de derechos a los usuarios. Las comunidades '
                     'autónomas pueden desarrollarlo con normas propias, pero lo esencial es común. '
                     'Conocerlo te ayuda a saber qué pedir y qué esperar.'),
                    ('h2', 'Derecho a un presupuesto por escrito'),
                    ('p',
                     'Antes de que el taller empiece a trabajar, tienes derecho a un '
                     '[[presupuesto|presupuesto]] por escrito que detalle las operaciones, las piezas y la '
                     'mano de obra. Solo puedes renunciar a él de forma expresa, también por escrito, por '
                     'ejemplo firmando esa renuncia en la orden de trabajo. Si aceptas el presupuesto, lo '
                     'normal es que lo firmes para dar tu conformidad.'),
                    ('p',
                     'Hacer un presupuesto puede requerir desmontar piezas para ver el daño completo. En ese '
                     'caso, el taller puede cobrarlo si te lo advierte antes. Pregunta siempre.'),
                    ('h2', 'Derecho al resguardo de depósito'),
                    ('p',
                     'Cuando dejas el coche en el taller, te deben entregar un '
                     '[[resguardo-de-deposito|resguardo de depósito]]. Es el documento que acredita que el '
                     'vehículo está allí y en qué condiciones lo dejaste. Suele incluir tus datos, los del '
                     'coche, la fecha, los kilómetros y el trabajo solicitado. Guárdalo: lo necesitarás para '
                     'recoger el coche y te protege ante cualquier discrepancia.'),
                    ('h2', 'Qué pasa si surge algo nuevo'),
                    ('p',
                     'A veces, al desmontar, aparece un daño que no estaba previsto. El taller no debería '
                     'hacer trabajos no incluidos en el presupuesto aceptado sin tu autorización. Lo '
                     'correcto es que te avise, te explique qué ha encontrado y te pida conformidad antes de '
                     'continuar.'),
                    ('h2', 'La factura'),
                    ('p',
                     'Al terminar, el taller debe entregarte una factura detallada, con las piezas, la mano '
                     'de obra y los precios desglosados, que se corresponda con el presupuesto aceptado. '
                     'También puedes pedir que te entreguen las piezas sustituidas, salvo en los casos en '
                     'que deban devolverse al fabricante o gestionarse como residuo; indícalo al dejar el '
                     'coche.'),
                    ('h2', 'Garantía de la reparación'),
                    ('p',
                     'Las reparaciones tienen una [[garantia-de-reparacion|garantía]] mínima de tres meses o '
                     '2.000 kilómetros, lo que ocurra antes, en condiciones normales de uso. Cubre la mano '
                     'de obra y las piezas que se hayan puesto. Algunos talleres ofrecen más. Si el fallo '
                     'vuelve a aparecer dentro de ese periodo, vuelve al mismo taller con tu factura.'),
                    ('h2', 'Resumen práctico'),
                    ('ul',
                     ['Pide siempre presupuesto por escrito y léelo antes de firmar.',
                      'Guarda el resguardo de depósito hasta recoger el coche.',
                      'No autorices trabajos por teléfono sin que te expliquen el motivo y el coste.',
                      'Revisa la factura y compárala con el presupuesto.',
                      'Guarda la factura: es tu garantía.']),
                    ('p',
                     'Si algo no se cumple, habla primero con el taller. Si no se resuelve, los talleres '
                     'deben tener a tu disposición la hoja de reclamaciones.'),
                    ('nota',
                     'Esta es una explicación general. La normativa de talleres puede tener desarrollos '
                     'autonómicos y detalles que dependen de cada caso.'),
                    ('p',
                     'En Green Car Service Tenerife te damos presupuesto por escrito y te mantenemos '
                     'informado del estado de tu coche. Puedes solicitar un [presupuesto](presupuesto.html) '
                     'o conocer nuestro [presupuesto sin '
                     'compromiso](servicio-presupuesto-sin-compromiso.html).')]},
  'en': {'titulo': 'Your rights at the garage: estimate, receipt and warranty',
         'resumen': 'Spanish garage regulations give you the right to a written estimate, a receipt when you '
                    'leave your car and a minimum warranty on the repair. Here it is in plain terms.',
         'cuerpo': [('p',
                     'Leaving your car at a garage involves trust. But that trust doesn’t have to be blind: '
                     'in Spain, Royal Decree 1457/1986, which regulates vehicle repair workshops, gives '
                     'customers a series of rights. The regional governments can add their own rules, but '
                     'the essentials are the same everywhere. Knowing them helps you know what to ask for '
                     'and what to expect.'),
                    ('h2', 'The right to a written estimate'),
                    ('p',
                     'Before the garage starts work, you are entitled to a written [[presupuesto|repair '
                     'estimate]] detailing the operations, parts and labour. You can only waive it '
                     'expressly, also in writing, for example by signing that waiver on the work order. If '
                     'you accept the estimate, you normally sign it to show your agreement.'),
                    ('p',
                     'Preparing an estimate may require removing parts to see the full damage. In that case, '
                     'the garage can charge for it if it tells you beforehand. Always ask.'),
                    ('h2', 'The right to a deposit receipt'),
                    ('p',
                     'When you leave the car at the garage, you should be given a '
                     '[[resguardo-de-deposito|vehicle deposit receipt]]. It proves that the vehicle is there '
                     'and in what condition you left it. It usually includes your details, the car’s '
                     'details, the date, the mileage and the work requested. Keep it: you’ll need it to '
                     'collect the car and it protects you if there is any disagreement.'),
                    ('h2', 'If something new comes up'),
                    ('p',
                     'Sometimes, when parts are removed, unexpected damage appears. The garage should not '
                     'carry out work not included in the accepted estimate without your authorisation. The '
                     'right thing is to let you know, explain what they’ve found and ask for your agreement '
                     'before going on.'),
                    ('h2', 'The invoice'),
                    ('p',
                     'When the job is finished, the garage must give you a detailed invoice with parts, '
                     'labour and prices broken down, matching the accepted estimate. You can also ask for '
                     'the replaced parts to be returned to you, except where they have to go back to the '
                     'manufacturer or be disposed of as waste; say so when you drop off the car.'),
                    ('h2', 'Repair warranty'),
                    ('p',
                     'Repairs carry a minimum [[garantia-de-reparacion|repair warranty]] of three months or '
                     '2,000 kilometres, whichever comes first, under normal use. It covers the labour and '
                     'the parts fitted. Some garages offer more. If the fault returns within that period, go '
                     'back to the same garage with your invoice.'),
                    ('h2', 'Practical summary'),
                    ('ul',
                     ['Always ask for a written estimate and read it before signing.',
                      'Keep the deposit receipt until you collect the car.',
                      'Don’t authorise work over the phone without being told why it’s needed and what it '
                      'costs.',
                      'Check the invoice against the estimate.',
                      'Keep the invoice: it’s your warranty.']),
                    ('p',
                     'If something isn’t respected, talk to the garage first. If it isn’t resolved, garages '
                     'must have an official complaints form available to you.'),
                    ('nota',
                     'This is a general explanation. Garage regulations may have regional variations and '
                     'details that depend on each case.'),
                    ('p',
                     'At Green Car Service Tenerife we give you a written estimate and keep you informed '
                     'about your car’s progress. You can request an [estimate](presupuesto.html) or find out '
                     'about our [no-obligation estimate](servicio-presupuesto-sin-compromiso.html).')]}},
 {'slug': 'articulo-alquiler-o-coche-propio-en-tenerife',
  'cat': 'tenerife',
  'fecha': '2025-08-12',
  'es': {'titulo': 'Coche de alquiler o coche propio si vives en Tenerife',
         'resumen': 'Si pasas temporadas largas en la isla o acabas de mudarte, tarde o temprano te planteas '
                    'si seguir alquilando o comprar un coche. Estas son las cuestiones que conviene pesar.',
         'cuerpo': [('p',
                     'El sur de Tenerife está lleno de coches de alquiler, y muchos residentes extranjeros '
                     'empiezan así: alquilan unas semanas, luego unos meses, y un día se dan cuenta de que '
                     'llevan un año pagando alquiler. No hay una respuesta única, pero sí una forma ordenada '
                     'de decidir.'),
                    ('h2', 'Lo que te da el alquiler'),
                    ('ul',
                     ['Flexibilidad total: lo devuelves cuando te vas y no te preocupas de nada más.',
                      'El seguro, la [[itv|ITV]], los papeles y las reparaciones son cosa de la empresa.',
                      'Puedes cambiar de tamaño de coche según la temporada o las visitas.']),
                    ('p',
                     'A cambio, el coste se acumula mes a mes, en temporada alta los precios y la '
                     'disponibilidad empeoran, y hay condiciones que conviene leer: kilometraje, conductores '
                     'autorizados, qué cubre el seguro y qué franquicia se aplica en caso de daños, o si '
                     'puedes llevarlo en ferry a otra isla.'),
                    ('h2', 'Lo que te da el coche propio'),
                    ('ul',
                     ['A partir de cierto tiempo de uso, suele salir más a cuenta que alquilar de forma '
                      'continua.',
                      'Lo eliges a tu medida y lo cuidas a tu manera.',
                      'No dependes de la disponibilidad de las empresas de alquiler.']),
                    ('p',
                     'A cambio, asumes tú el seguro, la ITV, los impuestos municipales, el cuidado del coche y '
                     'las reparaciones. Y cuando te vas una temporada, el coche se queda parado, algo que '
                     'también requiere cuidados.'),
                    ('h2', 'Preguntas para decidir'),
                    ('ol',
                     ['¿Cuántos meses al año vas a estar en la isla? Cuanto más tiempo, más sentido tiene el '
                      'coche propio.',
                      '¿Vas a residir legalmente en España? Si es así, infórmate de tus obligaciones con el '
                      'permiso de conducir y, si traes un coche con matrícula extranjera, sobre su '
                      'matriculación en España.',
                      '¿Tienes dónde aparcarlo de forma segura, sobre todo si pasas temporadas fuera?',
                      '¿Tienes a alguien de confianza que lo mueva o lo revise cuando no estás?']),
                    ('h2', 'Si te decides por comprar'),
                    ('p',
                     'Un coche de segunda mano bien revisado es una opción muy habitual. Antes de comprar, '
                     'pide las facturas de reparaciones anteriores, comprueba que la ITV está en vigor y que no '
                     'tiene cargas, y haz que un taller revise su carrocería y su estructura. Al contratar el seguro, compara coberturas: un '
                     '[[terceros|seguro a terceros]] ampliado puede ser suficiente para un coche de cierta '
                     'edad, mientras que en uno más nuevo quizá te interese un todo riesgo con '
                     '[[franquicia|franquicia]].'),
                    ('h2', 'Si te vas temporadas'),
                    ('ul',
                     ['Déjalo a cubierto si puedes, o con una funda transpirable: el sol y el salitre '
                      'castigan la pintura aunque el coche no se mueva.',
                      'Lávalo antes de irte, incluidos los bajos, para que no se quede sal pegada a la chapa.',
                      'Pide a alguien de confianza que le eche un vistazo y lo mueva de vez en cuando.',
                      'Revisa la fecha de la ITV y del seguro para que no caduquen mientras estás fuera.',
                      'A la vuelta, lava cuanto antes la resina, los excrementos de pájaro o el polvo de '
                      'calima: al sol, pueden marcar el barniz.']),
                    ('nota',
                     'Las obligaciones administrativas para residentes extranjeros dependen de tu '
                     'nacionalidad y de tu situación. Consulta con la administración o con un gestor.'),
                    ('p',
                     'En Green Car Service Tenerife vendemos [coches de ocasión](coches-de-ocasion.html) y '
                     'cuidamos la chapa y la pintura de tu coche en Las Chafiras, con [recogida y '
                     'entrega](servicio-recogida-y-entrega.html). Si dudas entre varios coches, podemos '
                     'revisar su carrocería con nuestra [revisión antes de '
                     'comprar](revision-antes-de-comprar.html).')]},
  'en': {'titulo': 'Hire car or your own car if you live in Tenerife',
         'resumen': 'If you spend long stretches on the island or have just moved here, sooner or later '
                    'you’ll wonder whether to keep renting or buy a car. These are the questions worth '
                    'weighing up.',
         'cuerpo': [('p',
                     'The south of Tenerife is full of hire cars, and many foreign residents start that way: '
                     'they rent for a few weeks, then a few months, and one day realise they’ve been paying '
                     'rental for a year. There’s no single answer, but there is an orderly way to decide.'),
                    ('h2', 'What renting gives you'),
                    ('ul',
                     ['Complete flexibility: you hand it back when you leave and don’t worry about anything '
                      'else.',
                      'Insurance, the [[itv|ITV (MOT)]], paperwork and repairs are the company’s '
                      'problem.',
                      'You can change the size of car depending on the season or visitors.']),
                    ('p',
                     'On the other hand, the cost adds up month after month, prices and availability get '
                     'worse in high season, and there are conditions worth reading: mileage, authorised '
                     'drivers, what the insurance covers and what excess applies if there’s damage, or '
                     'whether you can take it on a ferry to another island.'),
                    ('h2', 'What your own car gives you'),
                    ('ul',
                     ['After a certain amount of use, it usually works out cheaper than renting '
                      'continuously.',
                      'You choose it to suit you and look after it your way.',
                      'You don’t depend on rental companies’ availability.']),
                    ('p',
                     'In return, you take on the insurance, ITV, local vehicle tax, upkeep and repairs. '
                     'And when you’re away for a while, the car sits unused, which also needs looking '
                     'after.'),
                    ('h2', 'Questions to help you decide'),
                    ('ol',
                     ['How many months a year will you be on the island? The longer, the more sense your own '
                      'car makes.',
                      'Will you be legally resident in Spain? If so, find out about your obligations '
                      'regarding your driving licence and, if you bring a foreign-registered car, about '
                      'registering it in Spain.',
                      'Do you have somewhere safe to park it, especially if you spend time away?',
                      'Is there someone you trust who can move it or check it while you’re gone?']),
                    ('h2', 'If you decide to buy'),
                    ('p',
                     'A well-checked used car is a very common choice. Before buying, ask for invoices for '
                     'previous repairs, check that the ITV is valid and that there are no outstanding charges '
                     'on it, and have a garage inspect its bodywork and structure. When taking out insurance, compare cover: extended '
                     '[[terceros|third-party insurance]] may be enough for an older car, while for a newer '
                     'one comprehensive cover with an [[franquicia|excess]] may suit you better.'),
                    ('h2', 'If you’re away for long periods'),
                    ('ul',
                     ['Leave it under cover if you can, or use a breathable cover: sun and salt air wear '
                      'down the paint even when the car is not moving.',
                      'Wash it before you leave, underbody included, so no salt is left on the metal.',
                      'Ask someone you trust to keep an eye on it and move it now and then.',
                      'Check the ITV and insurance dates so they don’t expire while you’re away.',
                      'When you’re back, wash off tree sap, bird droppings or calima dust as soon as you can: '
                      'left in the sun, they can mark the clear coat.']),
                    ('nota',
                     'Administrative obligations for foreign residents depend on your nationality and '
                     'circumstances. Check with the authorities or a ‘gestor’ (administrative agent).'),
                    ('p',
                     'At Green Car Service Tenerife we sell [used cars](coches-de-ocasion.html) and look '
                     'after your car’s bodywork and paint in Las Chafiras, with [collection and '
                     'delivery](servicio-recogida-y-entrega.html). If you’re torn between several cars, we '
                     'can check their bodywork with our [pre-purchase '
                     'inspection](revision-antes-de-comprar.html).')]}}]
