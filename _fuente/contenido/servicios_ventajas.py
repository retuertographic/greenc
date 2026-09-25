"""Fichas de las ventajas del taller (ES/EN)."""

SERVICIOS = [{'slug': 'servicio-recogida-y-entrega',
  'cat': 'ventajas',
  'icon': 'truck',
  'es': {'titulo': 'Recogida y entrega a domicilio',
         'corto': 'Vamos a por tu coche y te lo devolvemos reparado, para que no tengas que cuadrar horarios '
                  'ni buscar quien te lleve.',
         'entradilla': 'Llevar el coche al taller suele costar una mañana. Con la recogida y entrega a '
                       'domicilio, nos ocupamos nosotros del trayecto y tú sigues con tu día.',
         'por_que_titulo': 'Por qué pedir la recogida',
         'por_que': [('clock',
                      'Ganas tiempo',
                      'Nuestro horario es de lunes a viernes de 07:00 a 16:00. Si trabajas en ese horario, '
                      'no tienes que pedir permiso para traer el coche.'),
                     ('home',
                      'Sin desplazamientos',
                      'No necesitas que nadie te acompañe al taller ni buscar cómo volver a casa o al '
                      'trabajo desde el polígono.'),
                     ('handshake',
                      'Un solo interlocutor',
                      'Te recogemos el coche, te mantenemos informado y te lo devolvemos. Todo con el mismo '
                      'equipo.')],
         'incluye_titulo': 'Cómo funciona',
         'incluye_intro': 'Lo organizamos contigo por teléfono, WhatsApp o correo, adaptándonos en lo '
                          'posible a tu día.',
         'incluye': [('calendar',
                      'Acordamos día y lugar',
                      'Nos dices dónde está el coche y cuándo te viene bien. Te confirmamos si podemos y en '
                      'qué franja.'),
                     ('clipboard',
                      'Recogida con documentación',
                      'Al recoger el coche anotamos su estado y te dejamos constancia del depósito.'),
                     ('wrench',
                      'Valoración y presupuesto',
                      'Ya en el taller lo revisamos y te enviamos el presupuesto. No hacemos nada sin tu '
                      'aprobación.'),
                     ('eye',
                      'Te mantenemos informado',
                      'Sabes en qué fase está la reparación sin tener que llamar.'),
                     ('truck',
                      'Entrega',
                      'Cuando está listo, te lo devolvemos donde hayamos acordado, y limpio.')],
         'nota': 'La recogida y entrega depende de la zona, de la disponibilidad y del tipo de trabajo. Te '
                 'confirmamos las condiciones al pedirla, sin sorpresas.',
         'texto': [('h2', 'Para quién es útil este servicio'),
                   ('p',
                    'Nuestro taller está en el polígono de Llano del Camello, en Las Chafiras. Está bien '
                    'comunicado, pero no todo el mundo puede acercarse en horario de taller. La recogida y '
                    'entrega a domicilio pensamos que encaja especialmente en estos casos:'),
                   ('checks',
                    ['Trabajas de mañana y no puedes dejar el coche y volver a por él.',
                     'Solo tienes un coche en casa y no hay nadie que te pueda recoger.',
                     'Tienes movilidad reducida o prefieres no desplazarte.',
                     'Vives en el sur de la isla parte del año y quieres dejar la carrocería lista sin '
                     'complicarte.',
                     'Tu coche ha tenido un golpe y prefieres no conducirlo más de lo necesario, si está en '
                     'condiciones de circular.']),
                   ('h2', 'Paso a paso'),
                   ('p',
                    'Nos escribes o llamas, nos cuentas qué le pasa al coche y dónde está. Acordamos una '
                    'franja para recogerlo. Al recogerlo revisamos contigo el estado del vehículo y dejamos '
                    'constancia del depósito con su [[resguardo-de-deposito|resguardo de depósito]], como '
                    'marca la normativa de talleres. Una vez en el taller, lo revisamos y te enviamos el '
                    '[[presupuesto]] para que decidas.'),
                   ('p',
                    'Mientras está en reparación, te mantenemos informado del [estado en tiempo '
                    'real](servicio-estado-en-tiempo-real.html). Cuando está terminado, te lo llevamos, te '
                    'explicamos lo que se ha hecho y te entregamos la factura y la '
                    '[[garantia-de-reparacion|garantía de la reparación]].'),
                   ('h2', 'Si el coche no puede circular'),
                   ('p',
                    'Si el coche no está en condiciones de circular, lo normal es trasladarlo con la '
                    'asistencia en carretera de tu seguro. Tienes los teléfonos de las principales compañías '
                    'en nuestra página de [teléfonos de asistencia](telefonos-de-asistencia.html). Si nos '
                    'avisas, lo coordinamos para que llegue directamente a nuestro taller.'),
                   ('h2', 'Combinado con otras ventajas'),
                   ('p',
                    'La recogida se combina bien con el [vehículo de '
                    'sustitución](servicio-vehiculo-de-sustitucion.html), cuando hay disponibilidad o lo '
                    'cubre tu póliza, y con la [gestión con tu '
                    'aseguradora](servicio-gestion-con-aseguradoras.html) si la reparación va por el seguro. '
                    'Así te ocupas de lo mínimo.'),
                   ('p',
                    'Un consejo: antes de la recogida, retira del coche objetos de valor y documentos '
                    'personales que no sean necesarios, y deja las llaves de repuesto en casa. Si el coche '
                    'tiene algún detalle de funcionamiento que debamos conocer, como un cierre que falla o '
                    'una rueda con poca presión, avísanos. Todo eso nos ayuda a trasladarlo con seguridad y '
                    'a revisarlo con más precisión.'),
                   ('p',
                    'Para pedirla, [contacta con nosotros](contacto.html) o indícalo al [pedir '
                    'cita](pedir-cita.html).')],
         'faq': [('¿La recogida tiene coste?',
                  'Depende de la zona y del trabajo. Te lo confirmamos al pedirla, antes de mover el coche.'),
                 ('¿Hasta dónde llegáis?',
                  'Trabajamos principalmente en el sur de Tenerife. Cuéntanos dónde está el coche y te '
                  'decimos si podemos.'),
                 ('¿Tengo que estar presente al recoger el coche?',
                  'Lo ideal es que sí, para revisar juntos su estado y entregarte el resguardo. Si no '
                  'puedes, lo hablamos y buscamos una alternativa segura.'),
                 ('¿Qué documentación debe llevar el coche?',
                  'La habitual para circular: permiso de circulación, ficha técnica y justificante del '
                  'seguro. Si falta algo, te avisamos.')]},
  'en': {'titulo': 'Collection and delivery',
         'corto': "We collect your car and bring it back repaired, so you don't have to juggle schedules or "
                  'find someone to give you a lift.',
         'entradilla': 'Taking the car to the garage usually eats up a morning. With collection and '
                       'delivery, we handle the journey and you get on with your day.',
         'por_que_titulo': 'Why ask for collection',
         'por_que': [('clock',
                      'Save time',
                      "We're open Monday to Friday, 07:00 to 16:00. If you work those hours, you don't need "
                      'time off to bring the car in.'),
                     ('home',
                      'No trips',
                      "You don't need anyone to follow you to the workshop or to work out how to get home or "
                      'to work from the industrial estate.'),
                     ('handshake',
                      'One point of contact',
                      'We collect the car, keep you informed and bring it back. All with the same team.')],
         'incluye_titulo': 'How it works',
         'incluye_intro': 'We arrange it with you by phone, WhatsApp or email, fitting in with your day as '
                          'far as we can.',
         'incluye': [('calendar',
                      'We agree day and place',
                      "Tell us where the car is and when suits you. We'll confirm whether we can and at what "
                      'time.'),
                     ('clipboard',
                      'Collection with paperwork',
                      'When we collect the car we note its condition and give you proof of deposit.'),
                     ('wrench',
                      'Assessment and estimate',
                      'At the workshop we inspect it and send you the estimate. Nothing is done without your '
                      'approval.'),
                     ('eye',
                      'We keep you informed',
                      'You know what stage the repair is at without having to call.'),
                     ('truck',
                      'Delivery',
                      "When it's ready, we bring it back to the agreed place, and clean.")],
         'nota': "Collection and delivery depends on the area, availability and type of work. We'll confirm "
                 'the conditions when you ask, with no surprises.',
         'texto': [('h2', 'Who this service suits'),
                   ('p',
                    "Our workshop is on the Llano del Camello industrial estate in Las Chafiras. It's well "
                    'connected, but not everyone can get there during opening hours. We think collection and '
                    'delivery is especially useful if:'),
                   ('checks',
                    ["You work mornings and can't drop the car off and come back for it.",
                     'You only have one car at home and nobody can pick you up.',
                     'You have reduced mobility or would rather not travel.',
                     'You live in the south of the island part of the year and want the car sorted without '
                     'hassle.',
                     "Your car has had a knock and you'd rather not drive it more than necessary, provided "
                     "it's roadworthy."]),
                   ('h2', 'Step by step'),
                   ('p',
                    "You message or call us, tell us what's wrong with the car and where it is. We agree a "
                    "time slot for collection. When we collect it, we go over the car's condition with you "
                    'and record the deposit with a [[resguardo-de-deposito|vehicle deposit receipt]], as '
                    'Spanish workshop regulations require. Once at the workshop, we inspect it and send you '
                    'the [[presupuesto|repair estimate]] so you can decide.'),
                   ('p',
                    "While it's being repaired, we keep you informed of its [real-time "
                    "status](servicio-estado-en-tiempo-real.html). When it's finished, we bring it to you, "
                    'explain what was done and hand over the invoice and the [[garantia-de-reparacion|repair '
                    'warranty]].'),
                   ('h2', "If the car isn't roadworthy"),
                   ('p',
                    "If the car can't be driven, the usual route is your insurer's roadside assistance. "
                    "You'll find the numbers for the main companies on our [assistance phone "
                    "numbers](telefonos-de-asistencia.html) page. Let us know and we'll coordinate so it "
                    'comes straight to our workshop.'),
                   ('h2', 'Combined with our other services'),
                   ('p',
                    'Collection works well alongside a [courtesy '
                    'car](servicio-vehiculo-de-sustitucion.html), when one is available or your policy '
                    'covers it, and with [insurance handling](servicio-gestion-con-aseguradoras.html) if the '
                    'repair goes through your insurer. That way you do as little as possible.'),
                   ('p',
                    "A tip: before collection, remove valuables and any personal documents you don't need "
                    'from the car, and keep the spare keys at home. If the car has any quirks we should know '
                    'about, such as a lock that sticks or a door that is hard to close, let us know. All of this helps '
                    'us move it safely and inspect it more accurately.'),
                   ('p',
                    'To request it, [get in touch](contacto.html) or mention it when you [book an '
                    'appointment](pedir-cita.html).')],
         'faq': [('Is there a charge for collection?',
                  "It depends on the area and the job. We'll confirm when you ask, before the car is moved."),
                 ('How far do you go?',
                  "We mainly work in the south of Tenerife. Tell us where the car is and we'll let you know "
                  'if we can.'),
                 ('Do I need to be there when the car is collected?',
                  'Ideally yes, so we can check its condition together and give you the receipt. If you '
                  "can't, we'll talk it through and find a safe alternative."),
                 ('What documents should be in the car?',
                  'The usual ones for driving: registration certificate, technical inspection card and proof '
                  "of insurance. If anything's missing, we'll let you know.")]}},
 {'slug': 'servicio-garantia-vitalicia-en-pintura',
  'cat': 'ventajas',
  'icon': 'award',
  'es': {'titulo': 'Garantía vitalicia en pintura',
         'corto': 'Las reparaciones de pintura que hacemos tienen garantía vitalicia. Te entregamos las '
                  'condiciones por escrito con cada trabajo.',
         'entradilla': 'Pintar bien lleva su tiempo: preparar, igualar el color, aplicar y secar en las '
                       'condiciones adecuadas. Por eso respaldamos nuestras reparaciones de pintura con una '
                       'garantía vitalicia.',
         'por_que_titulo': 'Por qué ofrecemos esta garantía',
         'por_que': [('award',
                      'Confianza en nuestro trabajo',
                      'Una garantía larga solo tiene sentido si el proceso de pintura está bien hecho desde '
                      'la preparación.'),
                     ('sun',
                      'Pensada para el clima de la isla',
                      'El sol intenso, el salitre y la calima castigan la pintura. Queremos que la '
                      'reparación aguante con el paso de los años.'),
                     ('doc',
                      'Todo por escrito',
                      'Las condiciones concretas te las damos por escrito junto con la reparación, para que '
                      'sepas exactamente qué cubre.')],
         'incluye_titulo': 'Qué cubre, en términos generales',
         'incluye_intro': 'Una garantía de pintura protege frente a defectos del propio trabajo de pintura. '
                          'Estos son los aspectos que suele abarcar; el detalle está en tu documento.',
         'incluye': [('layers',
                      'Adherencia',
                      'Que la pintura no se despegue ni se levante en la zona reparada por un defecto de '
                      'aplicación.'),
                     ('sparkle',
                      'Acabado',
                      'Defectos como burbujas, cuarteado o pérdida anormal de brillo atribuibles al trabajo '
                      'realizado.'),
                     ('paint',
                      'Zona reparada',
                      'Se refiere a las piezas o superficies que hemos pintado nosotros, identificadas en la '
                      'reparación.'),
                     ('doc',
                      'Condiciones escritas',
                      'Te entregamos el documento con las condiciones y lo que debes conservar para hacerla '
                      'valer.')],
         'nota': 'La garantía cubre defectos del trabajo de pintura realizado, no daños nuevos. Las '
                 'condiciones exactas son las que figuran en el documento que te entregamos con la '
                 'reparación.',
         'texto': [('h2', 'Qué significa «vitalicia» en una garantía de pintura'),
                   ('p',
                    'Una garantía vitalicia en pintura quiere decir que respaldamos el trabajo de pintura '
                    'que hemos hecho en tu coche sin un plazo de caducidad corto. Si la pintura aplicada '
                    'presenta un defecto atribuible a la reparación, como que se despegue o se cuartee, nos '
                    'ocupamos de corregirlo según las condiciones que te entregamos por escrito.'),
                   ('p',
                    'Es independiente de la [[garantia-de-reparacion|garantía legal de la reparación]], que '
                    'en España es de al menos tres meses o 2.000 kilómetros para cualquier reparación en '
                    'taller. La nuestra va más allá en el caso concreto de la pintura.'),
                   ('h2', 'Por qué podemos ofrecerla'),
                   ('p',
                    'Una buena pintura empieza mucho antes de la pistola. Se prepara la superficie, se '
                    'aplica [[imprimacion|imprimación]] donde hace falta, se iguala el color, se pinta y se '
                    'protege con [[barniz]]. Trabajamos con pintura ecológica «eco-balance» en colores '
                    'sólidos y metalizados, y con el equipamiento de nuestras instalaciones de chapa y '
                    'pintura. Si alguno de esos pasos se hace mal, el defecto aparece con el tiempo. Por eso '
                    'garantizarlo a largo plazo nos obliga a hacerlo bien.'),
                   ('h2', 'Qué suele quedar fuera de cualquier garantía de pintura'),
                   ('p',
                    'Con prudencia, y sin sustituir a tu documento, estas son situaciones que normalmente no '
                    'cubre ninguna garantía de pintura porque no dependen del trabajo realizado:'),
                   ('checks',
                    ['Daños nuevos: golpes, arañazos, rozaduras o impactos de piedras posteriores a la '
                     'reparación.',
                     'Daños causados por agentes externos, como productos químicos agresivos o actos '
                     'vandálicos.',
                     'Zonas del coche que no hemos pintado nosotros.',
                     'Reparaciones posteriores hechas en otro sitio sobre la misma zona.']),
                   ('p',
                    'Lo que sí te recomendamos es cuidar la pintura como la de cualquier coche: lavados sin '
                    'productos abrasivos y, si aparcas al sol, algo de protección de vez en cuando. Si te '
                    'interesa, mira nuestro servicio de [pulido y '
                    'abrillantado](servicio-pulido-y-abrillantado.html).'),
                   ('p',
                    'Nuestro consejo es que, al recoger el coche, revises la zona pintada a la luz del día y '
                    'con calma. Si algo no te convence, dínoslo en ese momento. Y si con el tiempo notas '
                    'cualquier cambio en esa zona, no esperes: cuanto antes lo veamos, más fácil será saber '
                    'si se trata de un defecto de la reparación o de otra causa.'),
                   ('h2', 'Cómo hacerla valer'),
                   ('p',
                    'Guarda la factura y el documento de garantía. Si notas algún defecto en la zona '
                    'reparada, [contacta con nosotros](contacto.html), revisamos el coche y te decimos cómo '
                    'lo resolvemos. Tienes más información sobre nuestro trabajo en [chapa y '
                    'pintura](chapa-y-pintura.html) y en [pintura '
                    'ecológica](servicio-pintura-ecologica.html).')],
         'faq': [('¿La garantía vitalicia cubre cualquier daño en la pintura?',
                  'No. Cubre defectos del trabajo de pintura que hemos realizado, según las condiciones '
                  'escritas. Un golpe o un arañazo nuevo no es un defecto de la reparación.'),
                 ('¿Se aplica también si la reparación la paga el seguro?',
                  'La garantía va ligada a nuestro trabajo de pintura. Las condiciones concretas figuran en '
                  'el documento que te entregamos con la reparación.'),
                 ('¿Y si vendo el coche?',
                  'Consulta el documento de garantía, donde se indican sus condiciones. Si tienes dudas, '
                  'pregúntanos.'),
                 ('¿Qué tengo que conservar?',
                  'La factura de la reparación y el documento de garantía que te entregamos.')]},
  'en': {'titulo': 'Lifetime paint guarantee',
         'corto': 'Our paint repairs come with a lifetime guarantee. The conditions are given to you in '
                  'writing with every job.',
         'entradilla': 'Painting properly takes time: preparation, colour matching, application and curing '
                       "in the right conditions. That's why we back our paint repairs with a lifetime "
                       'guarantee.',
         'por_que_titulo': 'Why we offer this guarantee',
         'por_que': [('award',
                      'Confidence in our work',
                      'A long guarantee only makes sense if the paint process is done right from the '
                      'preparation stage.'),
                     ('sun',
                      "Built for the island's climate",
                      'Strong sun, salty air and calima dust are hard on paint. We want the repair to last '
                      'over the years.'),
                     ('doc',
                      'Everything in writing',
                      'The specific conditions are given to you in writing with the repair, so you know '
                      "exactly what's covered.")],
         'incluye_titulo': 'What it covers, in general terms',
         'incluye_intro': 'A paint guarantee protects against defects in the paintwork itself. These are the '
                          'areas it usually covers; the detail is in your document.',
         'incluye': [('layers',
                      'Adhesion',
                      'The paint not peeling or lifting in the repaired area due to an application defect.'),
                     ('sparkle',
                      'Finish',
                      'Defects such as bubbling, cracking or abnormal loss of gloss attributable to the work '
                      'done.'),
                     ('paint',
                      'Repaired area',
                      'It refers to the panels or surfaces we painted, as identified in the repair.'),
                     ('doc',
                      'Written conditions',
                      'We give you the document with the conditions and what you need to keep to claim under '
                      'it.')],
         'nota': 'The guarantee covers defects in the paintwork carried out, not new damage. The exact '
                 'conditions are those stated in the document we give you with the repair.',
         'texto': [('h2', 'What «lifetime» means in a paint guarantee'),
                   ('p',
                    "A lifetime paint guarantee means we stand behind the paintwork we've done on your car "
                    'without a short expiry date. If the paint we applied shows a defect attributable to the '
                    "repair, such as peeling or cracking, we'll put it right according to the conditions we "
                    'give you in writing.'),
                   ('p',
                    "It's separate from the [[garantia-de-reparacion|legal repair warranty]], which in Spain "
                    'is at least three months or 2,000 km for any workshop repair. Ours goes further in the '
                    'specific case of paint.'),
                   ('h2', 'Why we can offer it'),
                   ('p',
                    'Good paintwork starts long before the spray gun. The surface is prepared, '
                    '[[imprimacion|primer]] is applied where needed, the colour is matched, the paint goes '
                    'on and is protected with [[barniz|clear coat]]. We work with eco-friendly «eco-balance» '
                    'paint in solid and metallic colours, using the equipment in our bodywork and paint '
                    'facilities. If any of those steps is done badly, the defect shows up over time. '
                    'Guaranteeing it long term forces us to do it right.'),
                   ('h2', 'What usually falls outside any paint guarantee'),
                   ('p',
                    'With caution, and without replacing your document, these are situations that normally '
                    "aren't covered by any paint guarantee because they don't depend on the work done:"),
                   ('checks',
                    ['New damage: knocks, scratches, scuffs or stone chips after the repair.',
                     'Damage caused by external agents, such as harsh chemicals or vandalism.',
                     "Areas of the car we didn't paint.",
                     'Later repairs carried out elsewhere on the same area.']),
                   ('p',
                    'What we do recommend is looking after the paint as you would on any car: washing '
                    'without abrasive products and, if you park in the sun, adding some protection now and '
                    "then. If you're interested, see our [polishing](servicio-pulido-y-abrillantado.html) "
                    'service.'),
                   ('p',
                    'Our advice is that when you collect the car, you look over the painted area calmly and '
                    "in daylight. If something doesn't look right, tell us there and then. And if you notice "
                    "any change in that area over time, don't wait: the sooner we see it, the easier it is "
                    "to tell whether it's a defect in the repair or something else."),
                   ('h2', 'How to claim'),
                   ('p',
                    'Keep the invoice and the guarantee document. If you notice a defect in the repaired '
                    "area, [get in touch](contacto.html); we'll inspect the car and tell you how we'll "
                    "resolve it. There's more about our work under [bodywork and "
                    'paint](chapa-y-pintura.html) and [eco-friendly '
                    'paint](servicio-pintura-ecologica.html).')],
         'faq': [('Does the lifetime guarantee cover any paint damage?',
                  'No. It covers defects in the paintwork we carried out, under the written conditions. A '
                  "new knock or scratch isn't a defect in the repair."),
                 ('Does it apply if the insurer pays for the repair?',
                  'The guarantee is tied to our paintwork. The specific conditions are in the document we '
                  'give you with the repair.'),
                 ('What if I sell the car?',
                  'Check the guarantee document, which sets out its conditions. If in doubt, ask us.'),
                 ('What do I need to keep?', 'The repair invoice and the guarantee document we give you.')]}},
 {'slug': 'servicio-estado-en-tiempo-real',
  'cat': 'ventajas',
  'icon': 'eye',
  'es': {'titulo': 'Estado del vehículo en tiempo real',
         'corto': 'Sabes en qué fase está la reparación de tu coche sin tener que llamar para preguntar.',
         'entradilla': 'Dejar el coche en el taller y no saber nada durante días genera incertidumbre. Te '
                       'mantenemos informado en tiempo real del estado de la reparación.',
         'por_que_titulo': 'Por qué te mantenemos informado',
         'por_que': [('eye',
                      'Tranquilidad',
                      'Saber en qué punto está tu coche te quita la duda de si alguien lo está atendiendo.'),
                     ('calendar',
                      'Te organizas mejor',
                      'Si sabes cómo avanza la reparación, puedes planificar mejor cuándo lo vas a necesitar '
                      'de nuevo.'),
                     ('handshake',
                      'Transparencia',
                      'Forma parte de nuestra manera de trabajar: calidad, confianza y compromiso.')],
         'incluye_titulo': 'Qué te contamos',
         'incluye_intro': 'La información que de verdad te interesa mientras tu coche está con nosotros.',
         'incluye': [('clipboard',
                      'Recepción',
                      'Te confirmamos que el coche ha llegado y está registrado en el taller.'),
                     ('doc',
                      'Presupuesto y aprobación',
                      'Sabes cuándo está listo el presupuesto y, si va por seguro, en qué punto está la '
                      'peritación.'),
                     ('wrench',
                      'Reparación en curso',
                      'Te informamos de la fase en que se encuentra el trabajo.'),
                     ('alert',
                      'Imprevistos',
                      'Si aparece algo nuevo al desmontar, te lo contamos antes de continuar.'),
                     ('check',
                      'Listo para entregar',
                      'Te avisamos en cuanto el coche está terminado y listo para recoger o llevártelo.')],
         'nota': 'El avance depende de cada reparación, de la llegada de recambios y, en su caso, de la '
                 'aseguradora. Te informamos del estado real, sin prometer plazos que no dependen solo de '
                 'nosotros.',
         'texto': [('h2', 'Qué es y para qué sirve'),
                   ('p',
                    'Una reparación tiene varias fases, y no todas se ven desde fuera. Hay días en que el '
                    'coche parece parado y en realidad está esperando una pieza o la visita del [[perito]]. '
                    'Por eso te mantenemos informado en tiempo real del estado de la reparación: sabes en '
                    'qué fase está tu coche sin tener que llamar para preguntar.'),
                   ('h2', 'Las fases habituales de una reparación'),
                   ('checks',
                    ['Recepción del vehículo y firma de la [[orden-de-reparacion|orden de reparación]].',
                     'Valoración del daño y elaboración del presupuesto.',
                     'Aprobación por tu parte o, si va por seguro, [[peritacion|peritación]] y autorización '
                     'de la compañía.',
                     'Pedido y recepción de recambios.',
                     'Reparación: chapa, estructura, preparación y pintura, según el caso.',
                     'Montaje, control de calidad, limpieza y aviso de entrega.']),
                   ('h2', 'Cuando surge un imprevisto'),
                   ('p',
                    'A veces, al desmontar una pieza, aparece un daño que no se veía: un soporte roto detrás '
                    'de un paragolpes o un refuerzo doblado. Si pasa, no seguimos por nuestra cuenta. '
                    'Te lo contamos, te explicamos las opciones y, si hace falta, ampliamos el '
                    '[presupuesto](servicio-presupuesto-sin-compromiso.html) para que lo apruebes. En '
                    'reparaciones por seguro, lo comunicamos también a la compañía.'),
                   ('h2', 'Plazos: lo que depende de nosotros y lo que no'),
                   ('p',
                    'Hay factores que no controlamos del todo: la llegada de recambios a la isla, la agenda '
                    'del perito o la autorización de la aseguradora. No te vamos a prometer una fecha que no '
                    'dependa de nosotros. Lo que sí te garantizamos es que sabrás en todo momento qué está '
                    'pasando y en qué punto está tu coche.'),
                   ('p',
                    'Mantenerte informado también sirve para que decidas a tiempo. Si una pieza tarda más de '
                    'lo previsto, puedes valorar si te interesa pedir un [vehículo de '
                    'sustitución](servicio-vehiculo-de-sustitucion.html) o reorganizar tus planes. Y si en '
                    'algún momento algo no te queda claro, pregúntanos: preferimos explicarlo dos veces a '
                    'que te quedes con la duda.'),
                   ('h2', 'Cómo nos comunicamos'),
                   ('p',
                    'Te informamos por el canal que te resulte más cómodo y, si tienes cualquier duda, '
                    'puedes escribirnos por WhatsApp al 674 06 13 71 o llamarnos al 922 73 64 47 en horario '
                    'de lunes a viernes de 07:00 a 16:00.'),
                   ('p',
                    'Este servicio se combina con la [recogida y entrega](servicio-recogida-y-entrega.html) '
                    'y con la [gestión con tu aseguradora](servicio-gestion-con-aseguradoras.html). Si tu '
                    'coche ha tenido un siniestro, consulta también la [guía de '
                    'peritación](guia-peritacion.html). Para empezar, [pide cita](pedir-cita.html).')],
         'faq': [('¿Tengo que llamar para saber cómo va mi coche?',
                  'No hace falta. Te mantenemos informado del estado de la reparación. Si aun así quieres '
                  'preguntar algo, estamos a tu disposición.'),
                 ('¿Me avisáis si hay que hacer algo que no estaba en el presupuesto?',
                  'Siempre. No hacemos trabajos adicionales sin contártelo y sin tu aprobación.'),
                 ('¿Por qué mi coche lleva días sin avanzar?',
                  'Suele deberse a que espera una pieza, al perito o a la autorización del seguro. Te '
                  'informamos de cuál es el motivo.'),
                 ('¿Podéis darme una fecha exacta de entrega?',
                  'Te damos una previsión realista y la actualizamos si algo cambia. No prometemos fechas '
                  'que dependen de terceros.')]},
  'en': {'titulo': 'Real-time vehicle status',
         'corto': "You know what stage your car's repair is at without having to call and ask.",
         'entradilla': 'Leaving your car at the garage and hearing nothing for days is unsettling. We keep '
                       'you informed in real time of the status of the repair.',
         'por_que_titulo': 'Why we keep you informed',
         'por_que': [('eye',
                      'Peace of mind',
                      'Knowing where your car is up to removes the worry about whether anyone is working on '
                      'it.'),
                     ('calendar',
                      'Plan ahead',
                      "If you know how the repair is progressing, you can plan better for when you'll need "
                      'the car again.'),
                     ('handshake',
                      'Transparency',
                      "It's part of how we work: quality, trust and commitment.")],
         'incluye_titulo': 'What we tell you',
         'incluye_intro': 'The information you really want while your car is with us.',
         'incluye': [('clipboard',
                      'Check-in',
                      'We confirm the car has arrived and is logged at the workshop.'),
                     ('doc',
                      'Estimate and approval',
                      "You know when the estimate is ready and, if it's an insurance job, where the "
                      'assessment is up to.'),
                     ('wrench', 'Repair in progress', 'We let you know what stage the work is at.'),
                     ('alert',
                      'Unexpected findings',
                      'If something new turns up during dismantling, we tell you before carrying on.'),
                     ('check',
                      'Ready to go',
                      'We let you know as soon as the car is finished and ready to collect or be '
                      'delivered.')],
         'nota': 'Progress depends on each repair, on parts arriving and, where relevant, on the insurer. We '
                 "tell you the real status, without promising timescales that don't depend on us alone.",
         'texto': [('h2', 'What it is and why it helps'),
                   ('p',
                    'A repair goes through several stages, and not all of them are visible from outside. '
                    "Some days the car seems idle when in fact it's waiting for a part or for the "
                    "[[perito|loss adjuster]] to visit. That's why we keep you informed in real time of the "
                    'status of the repair: you know what stage your car is at without having to call.'),
                   ('h2', 'The usual stages of a repair'),
                   ('checks',
                    ['Vehicle check-in and signing of the [[orden-de-reparacion|repair order]].',
                     'Damage assessment and preparation of the estimate.',
                     'Your approval or, for insurance jobs, [[peritacion|loss assessment]] and authorisation '
                     'from the insurer.',
                     'Ordering and receiving parts.',
                     'Repair: bodywork, structure, preparation and paint, as needed.',
                     "Reassembly, quality check, cleaning and notice that it's ready."]),
                   ('h2', 'When something unexpected comes up'),
                   ('p',
                    'Sometimes, when a part is removed, hidden damage appears: a broken bracket behind a '
                    "bumper or a bent reinforcement. If that happens, we don't carry on regardless. We tell you, "
                    'explain the options and, if needed, extend the '
                    '[estimate](servicio-presupuesto-sin-compromiso.html) for your approval. On insurance '
                    'jobs, we also inform the insurer.'),
                   ('h2', "Timescales: what depends on us and what doesn't"),
                   ('p',
                    'Some factors are not fully in our hands: parts arriving on the island, the loss '
                    "adjuster's schedule or the insurer's authorisation. We won't promise you a date that "
                    "doesn't depend on us. What we do guarantee is that you'll know what's happening and "
                    'where your car is up to.'),
                   ('p',
                    'Keeping you informed also helps you decide in time. If a part is taking longer than '
                    'expected, you can consider asking for a [courtesy '
                    'car](servicio-vehiculo-de-sustitucion.html) or rearranging your plans. And if anything '
                    "isn't clear at any point, ask us: we'd rather explain twice than leave you unsure."),
                   ('h2', 'How we keep in touch'),
                   ('p',
                    'We update you through whichever channel suits you best and, if you have any questions, '
                    'you can WhatsApp us on 674 06 13 71 or call 922 73 64 47, Monday to Friday from 07:00 '
                    'to 16:00.'),
                   ('p',
                    'This service combines with [collection and delivery](servicio-recogida-y-entrega.html) '
                    'and [insurance handling](servicio-gestion-con-aseguradoras.html). If your car has had a '
                    'claim event, see our [loss assessment guide](guia-peritacion.html) too. To get started, '
                    '[book an appointment](pedir-cita.html).')],
         'faq': [('Do I need to call to find out how my car is doing?',
                  "No need. We keep you informed of the repair's status. If you still want to ask something, "
                  "we're here."),
                 ('Will you tell me if something not in the estimate needs doing?',
                  "Always. We don't do extra work without telling you and getting your approval."),
                 ("Why hasn't my car moved on for days?",
                  "It's usually waiting for a part, the loss adjuster or the insurer's authorisation. We'll "
                  'tell you which.'),
                 ('Can you give me an exact delivery date?',
                  "We give you a realistic forecast and update it if anything changes. We don't promise "
                  'dates that depend on third parties.')]}},
 {'slug': 'servicio-vehiculo-de-sustitucion',
  'cat': 'ventajas',
  'icon': 'key',
  'es': {'titulo': 'Vehículo de sustitución',
         'corto': 'Mientras reparamos tu coche, te ayudamos a seguir moviéndote con un vehículo de '
                  'sustitución, según disponibilidad o tu póliza.',
         'entradilla': 'Quedarse sin coche en el sur de Tenerife complica el día a día. Cuando es posible, '
                       'te facilitamos un vehículo de sustitución mientras el tuyo está en el taller.',
         'por_que_titulo': 'Por qué importa',
         'por_que': [('road',
                      'La isla se mueve en coche',
                      'Para muchos trabajos y trayectos del sur de Tenerife el transporte público no siempre '
                      'llega a tiempo. Un coche marca la diferencia.'),
                     ('clock',
                      'Sin prisas en la reparación',
                      'Si tienes con qué moverte, la reparación se puede hacer con el tiempo que necesita, '
                      'sin atajos.'),
                     ('doc',
                      'Aprovecha tu póliza',
                      'Muchas pólizas incluyen vehículo de sustitución en caso de siniestro. Te '
                      'ayudamos a comprobarlo.')],
         'incluye_titulo': 'Cómo funciona',
         'incluye_intro': 'Hay dos vías principales para tener coche mientras reparamos el tuyo.',
         'incluye': [('shield',
                      'A través de tu seguro',
                      'Si tu póliza incluye vehículo de sustitución, lo gestionamos contigo según las '
                      'condiciones de tu compañía.'),
                     ('key',
                      'Del taller, según disponibilidad',
                      'Cuando tenemos un vehículo disponible y el tipo de reparación lo justifica, te lo '
                      'ofrecemos.'),
                     ('calendar',
                      'Reserva con la cita',
                      'Pídelo al pedir cita para que podamos organizarlo con antelación.'),
                     ('clipboard',
                      'Entrega y devolución',
                      'Revisamos juntos el estado del vehículo de sustitución al entregártelo y al '
                      'devolverlo.')],
         'nota': 'El vehículo de sustitución depende de la disponibilidad en cada momento y, si va por '
                 'seguro, de lo que cubra tu póliza. Te confirmamos las condiciones antes de la reparación.',
         'texto': [('h2', 'Seguro o taller: dos caminos'),
                   ('p',
                    'Cuando la reparación va por el seguro, lo primero es revisar tu póliza. Muchas incluyen '
                    'un [[vehiculo-de-sustitucion|vehículo de sustitución]] tras un '
                    '[[siniestro|siniestro]], pero cada compañía fija sus condiciones: número de días, tipo de coche, si '
                    'depende de la culpa o de la modalidad contratada. Una póliza a [[todo-riesgo|todo '
                    'riesgo]] no siempre lo incluye, y una a terceros a veces sí, como garantía adicional. '
                    'Hay que leer la letra.'),
                   ('p',
                    'Si no tienes esa cobertura, o la reparación no va por el seguro, también puedes '
                    'preguntarnos. Cuando tenemos un vehículo disponible y el trabajo lo justifica, te lo '
                    'ofrecemos. Lo que no podemos es asegurar que siempre habrá uno libre, por eso conviene '
                    'pedirlo con tiempo.'),
                   ('h2', 'Qué necesitas'),
                   ('checks',
                    ['Carné de conducir en vigor.',
                     'Si va por seguro, los datos de tu póliza y el número de siniestro.',
                     'Pedirlo con antelación, idealmente al [pedir cita](pedir-cita.html).',
                     'Revisar el estado del vehículo al recogerlo y al devolverlo.']),
                   ('h2', 'Consejos para aprovecharlo bien'),
                   ('p',
                    'Pregunta a tu compañía cuántos días cubre y desde cuándo cuentan: algunas empiezan '
                    'cuando el coche entra en el taller y otras desde la autorización de la reparación. Si '
                    'la reparación se alarga por la llegada de piezas, es útil saberlo. Nosotros te '
                    'mantenemos informado del [estado de la reparación](servicio-estado-en-tiempo-real.html) '
                    'para que puedas prever cuándo devolver el vehículo.'),
                   ('p',
                    'Si la reparación la cubre el seguro del otro conductor porque no tuviste la culpa, en '
                    'algunos casos puedes reclamar también los gastos de movilidad. Consulta con tu compañía '
                    'cómo proceder. Tienes información útil en nuestra página de '
                    '[siniestros](siniestros.html) y en la [guía de qué hacer tras un '
                    'accidente](guia-que-hacer-tras-un-accidente.html).'),
                   ('p',
                    'Si eres residente extranjero o visitas la isla con frecuencia, recuerda que para '
                    'conducir un vehículo de sustitución necesitas un permiso de conducir válido en España. '
                    'Si tienes dudas sobre tu caso, consúltalo antes de la reparación. Y si tu seguro es de '
                    'otro país, revisa con tu compañía qué cubre en caso de siniestro en España.'),
                   ('h2', 'Combínalo con otras ventajas'),
                   ('p',
                    'Si además pides la [recogida y entrega](servicio-recogida-y-entrega.html), puedes '
                    'organizarte para no pasar por el taller en todo el proceso. Y si el trabajo va por '
                    'seguro, nos ocupamos de la [gestión con tu '
                    'aseguradora](servicio-gestion-con-aseguradoras.html). Para cualquier duda, [contacta '
                    'con nosotros](contacto.html).')],
         'faq': [('¿Siempre tenéis coche de sustitución?',
                  'No podemos garantizarlo: depende de la disponibilidad. Por eso te recomendamos pedirlo '
                  'con antelación.'),
                 ('¿Mi seguro me da coche de sustitución?',
                  'Depende de tu póliza. Revisa las condiciones o pregúntanos y te ayudamos a comprobarlo '
                  'con tu compañía.'),
                 ('¿Cuántos días puedo tenerlo?',
                  'Si va por seguro, los que marque tu póliza. Si es del taller, lo acordamos según la '
                  'reparación.'),
                 ('¿Qué pasa si el vehículo de sustitución sufre un daño?',
                  'Las condiciones de uso te las explicamos al entregártelo. Por eso revisamos juntos su '
                  'estado al principio y al final.')]},
  'en': {'titulo': 'Courtesy car',
         'corto': 'While we repair your car, we help you keep moving with a courtesy car, subject to '
                  'availability or your policy.',
         'entradilla': 'Being without a car in the south of Tenerife makes daily life hard. Whenever '
                       'possible, we provide a courtesy car while yours is in the workshop.',
         'por_que_titulo': 'Why it matters',
         'por_que': [('road',
                      'The island runs on cars',
                      "For many jobs and journeys in the south of Tenerife, public transport doesn't always "
                      'get you there on time. A car makes the difference.'),
                     ('clock',
                      'No rushing the repair',
                      'If you have a way to get around, the repair can take the time it needs, with no '
                      'shortcuts.'),
                     ('doc',
                      'Make use of your policy',
                      "Many policies include a courtesy car after a claim event. We'll help you "
                      'check.')],
         'incluye_titulo': 'How it works',
         'incluye_intro': 'There are two main ways to have a car while we fix yours.',
         'incluye': [('shield',
                      'Through your insurer',
                      "If your policy includes a courtesy car, we arrange it with you under your insurer's "
                      'conditions.'),
                     ('key',
                      'From us, subject to availability',
                      "When we have a vehicle available and the repair justifies it, we'll offer it to you."),
                     ('calendar',
                      'Book it with the appointment',
                      'Ask for it when you book so we can plan ahead.'),
                     ('clipboard',
                      'Handover and return',
                      "We check the courtesy car's condition together when you collect it and when you "
                      'return it.')],
         'nota': 'A courtesy car depends on availability at the time and, for insurance jobs, on what your '
                 'policy covers. We confirm the conditions before the repair.',
         'texto': [('h2', 'Insurer or workshop: two routes'),
                   ('p',
                    'When the repair goes through insurance, the first step is to check your policy. Many '
                    'include a [[vehiculo-de-sustitucion|courtesy car]] after a [[siniestro|claim event]], '
                    'but each insurer sets its own conditions: number of days, type of car, '
                    "whether it depends on fault or on the cover you've taken out. A "
                    "[[todo-riesgo|comprehensive]] policy doesn't always include one, and a third-party "
                    "policy sometimes does as an add-on. It's worth reading the small print."),
                   ('p',
                    "If you don't have that cover, or the repair isn't going through insurance, you can "
                    "still ask us. When we have a vehicle available and the job justifies it, we'll offer "
                    "it. What we can't do is promise there'll always be one free, so it's best to ask in "
                    'good time.'),
                   ('h2', "What you'll need"),
                   ('checks',
                    ['A valid driving licence.',
                     'For insurance jobs, your policy details and claim number.',
                     'To ask in advance, ideally when you [book an appointment](pedir-cita.html).',
                     "To check the vehicle's condition on collection and return."]),
                   ('h2', 'Tips to make the most of it'),
                   ('p',
                    'Ask your insurer how many days are covered and when they start counting: some start '
                    'when the car enters the workshop and others from repair authorisation. If the repair is '
                    "delayed by parts arriving, that's useful to know. We keep you informed of the [repair "
                    'status](servicio-estado-en-tiempo-real.html) so you can plan when to return the '
                    'vehicle.'),
                   ('p',
                    "If the other driver's insurer is covering the repair because you weren't at fault, in "
                    'some cases you can also claim mobility costs. Check with your insurer how to proceed. '
                    "There's useful information on our [claims](siniestros.html) page and in the [what to do "
                    'after an accident](guia-que-hacer-tras-un-accidente.html) guide.'),
                   ('p',
                    "If you're a foreign resident or visit the island often, remember that to drive a "
                    "courtesy car you need a driving licence valid in Spain. If you're unsure about your "
                    'case, check before the repair. And if your insurance is from another country, check '
                    "with your insurer what's covered for a claim in Spain."),
                   ('h2', 'Combine it with our other services'),
                   ('p',
                    'If you also ask for [collection and delivery](servicio-recogida-y-entrega.html), you '
                    'can arrange things so you never have to come to the workshop. And if the job goes '
                    'through insurance, we take care of [insurance '
                    'handling](servicio-gestion-con-aseguradoras.html). Any questions, [get in '
                    'touch](contacto.html).')],
         'faq': [('Do you always have a courtesy car?',
                  "We can't guarantee it: it depends on availability. That's why we recommend asking in "
                  'advance.'),
                 ('Does my insurance give me a courtesy car?',
                  "It depends on your policy. Check the conditions or ask us and we'll help you confirm with "
                  'your insurer.'),
                 ('How many days can I keep it?',
                  "For insurance jobs, whatever your policy says. If it's ours, we agree it based on the "
                  'repair.'),
                 ('What if the courtesy car gets damaged?',
                  "We explain the conditions of use when we hand it over. That's why we check its condition "
                  'together at the start and end.')]}},
 {'slug': 'servicio-gestion-con-aseguradoras',
  'cat': 'ventajas',
  'icon': 'handshake',
  'es': {'titulo': 'Gestión con aseguradoras',
         'corto': 'Trabajamos con tu compañía de seguros: te acompañamos en la peritación y en los trámites '
                  'para que tú te ocupes de lo mínimo.',
         'entradilla': 'Tras un golpe, el papeleo con el seguro puede agobiar más que el propio daño. '
                       'Trabajamos con tu compañía y te ayudamos en cada paso, desde el parte hasta la '
                       'entrega.',
         'por_que_titulo': 'Por qué dejarnos la gestión',
         'por_que': [('handshake',
                      'Trabajamos con tu compañía',
                      'Coordinamos con tu aseguradora la peritación y la autorización de la reparación.'),
                     ('shield',
                      'Tu derecho a elegir taller',
                      'Aunque tu compañía te sugiera otro taller, en general puedes elegir dónde reparar tu '
                      'coche.'),
                     ('eye',
                      'Informado en todo momento',
                      'Sabes en qué punto está el expediente y la reparación sin tener que perseguir a '
                      'nadie.')],
         'incluye_titulo': 'Qué hacemos por ti',
         'incluye_intro': 'Nos encargamos de la parte técnica y de la comunicación con el taller, mientras '
                          'tú mantienes tu relación con la compañía.',
         'incluye': [('doc',
                      'Orientación con el parte',
                      'Te ayudamos a entender qué datos necesita el parte amistoso o la comunicación del '
                      'siniestro.'),
                     ('search',
                      'Valoración del daño',
                      'Revisamos el coche y preparamos la información técnica para la peritación.'),
                     ('users',
                      'Coordinación con el perito',
                      'Facilitamos el acceso al coche y al detalle del daño para que la valoración sea '
                      'completa.'),
                     ('wrench',
                      'Reparación autorizada',
                      'Una vez autorizada, reparamos y te mantenemos informado.'),
                     ('euro',
                      'Claridad en la franquicia',
                      'Si tu póliza tiene franquicia, te explicamos qué parte corresponde pagar a ti.')],
         'nota': 'La cobertura, la franquicia y la decisión final sobre el siniestro dependen de tu póliza y '
                 'de tu compañía. Nosotros te acompañamos y te informamos, pero no podemos decidir por la '
                 'aseguradora.',
         'texto': [('h2', 'El recorrido de un siniestro, paso a paso'),
                   ('checks',
                    ['Tras el accidente, rellenáis el [[parte-amistoso|parte amistoso]] si hay otro vehículo '
                     'implicado, o comunicas el siniestro a tu compañía.',
                     'Nos traes el coche o pedimos que llegue con la asistencia en carretera.',
                     'Revisamos el daño y avisamos a la compañía para la [[peritacion|peritación]].',
                     'El [[perito]] valora el daño y la compañía autoriza la reparación.',
                     'Reparamos el coche y te mantenemos informado.',
                     'Te lo entregamos; si hay [[franquicia]], abonas solo esa parte según tu póliza.']),
                   ('h2', 'Libre elección de taller'),
                   ('p',
                    'Es una de las dudas más habituales. Tu compañía puede recomendarte talleres '
                    'concertados, pero en general la [[libre-eleccion-de-taller|libre elección de taller]] '
                    'te permite llevar el coche al que tú prefieras. Lo que puede variar según la póliza es '
                    'cómo se paga la reparación o si hay alguna condición adicional. Te lo explicamos con '
                    'detalle en la [guía de libre elección de taller](guia-libre-eleccion-de-taller.html).'),
                   ('h2', 'La peritación, sin misterio'),
                   ('p',
                    'El perito es un profesional que valora el daño para la aseguradora. Nuestro papel es '
                    'asegurarnos de que ve todo lo necesario: daños visibles y daños que aparecen al '
                    'desmontar. Si tras la primera valoración surge algo nuevo, lo comunicamos para que se '
                    'amplíe. Tienes más detalle en la [guía de peritación](guia-peritacion.html).'),
                   ('h2', 'Si el daño es grande'),
                   ('p',
                    'Cuando el coste de la reparación se acerca o supera el valor del coche, la compañía '
                    'puede declarar la pérdida total. Es una situación delicada y conviene conocer tus '
                    'derechos. Te lo explicamos en la [guía de pérdida total](guia-perdida-total.html).'),
                   ('p',
                    'Un consejo tras un golpe: haz fotos del daño y del lugar antes de mover el coche si es '
                    'seguro hacerlo, guarda una copia del parte y anota el número de siniestro que te dé tu '
                    'compañía. Esa información agiliza la peritación y evita malentendidos. Si el coche no '
                    'puede circular, llama a la asistencia en carretera de tu póliza y pide que lo traigan a '
                    'nuestro taller.'),
                   ('h2', 'Lo que no hacemos'),
                   ('p',
                    'No decidimos por tu aseguradora ni podemos garantizar lo que va a cubrir: eso depende '
                    'de tu póliza. Tampoco te pedimos que firmes nada que no entiendas. Te explicamos cada '
                    'paso para que tomes las decisiones con información.'),
                   ('p',
                    'Si acabas de tener un accidente, empieza por nuestra página de '
                    '[siniestros](siniestros.html). Si ya tienes el número de siniestro, [pide '
                    'cita](pedir-cita.html) o [contacta con nosotros](contacto.html).')],
         'faq': [('¿Con qué aseguradoras trabajáis?',
                  'Trabajamos con tu compañía de seguros. Si tienes dudas sobre tu caso concreto, llámanos '
                  'con los datos de tu póliza y lo vemos.'),
                 ('Mi seguro me ha dicho que vaya a otro taller. ¿Puedo ir al vuestro?',
                  'En general sí, gracias a la libre elección de taller. Revisa las condiciones de tu póliza '
                  'por si hay alguna particularidad y, si quieres, las vemos juntos.'),
                 ('¿Tengo que pagar algo?',
                  'Depende de la cobertura y de si tu póliza tiene franquicia. Te lo explicamos antes de '
                  'empezar.'),
                 ('¿Qué pasa si el perito no ve un daño?',
                  'Si al desmontar aparece un daño que no estaba valorado, lo comunicamos a la compañía para '
                  'que lo revise.')]},
  'en': {'titulo': 'Insurance handling',
         'corto': 'We work with your insurance company: we support you through the assessment and paperwork '
                  'so you have as little to do as possible.',
         'entradilla': 'After a knock, dealing with the insurer can be more stressful than the damage '
                       'itself. We work with your company and help you at every step, from the accident '
                       'report to delivery.',
         'por_que_titulo': 'Why leave the handling to us',
         'por_que': [('handshake',
                      'We work with your insurer',
                      'We coordinate the loss assessment and repair authorisation with your insurance '
                      'company.'),
                     ('shield',
                      'Your right to choose',
                      'Even if your insurer suggests another workshop, you can generally choose where your '
                      'car is repaired.'),
                     ('eye',
                      'Informed throughout',
                      'You know where the claim and the repair are up to without chasing anyone.')],
         'incluye_titulo': 'What we do for you',
         'incluye_intro': "We handle the technical side and the workshop's communication, while you keep "
                          'your relationship with the insurer.',
         'incluye': [('doc',
                      'Help with the report',
                      'We help you understand what details the accident report form or claim notification '
                      'needs.'),
                     ('search',
                      'Damage assessment',
                      'We inspect the car and prepare the technical information for the loss assessment.'),
                     ('users',
                      'Coordination with the adjuster',
                      'We give access to the car and the details of the damage so the assessment is '
                      'complete.'),
                     ('wrench',
                      'Authorised repair',
                      'Once authorised, we carry out the repair and keep you informed.'),
                     ('euro',
                      'Clarity on the excess',
                      'If your policy has an excess, we explain which part you pay.')],
         'nota': 'Cover, excess and the final decision on the claim depend on your policy and your insurer. '
                 "We support and inform you, but we can't decide on the insurer's behalf.",
         'texto': [('h2', 'A claim, step by step'),
                   ('checks',
                    ['After the accident, you fill in the [[parte-amistoso|accident report form]] if another '
                     'vehicle is involved, or notify your insurer of the claim.',
                     'You bring us the car or ask for it to be delivered by roadside assistance.',
                     'We inspect the damage and notify the insurer for the [[peritacion|loss assessment]].',
                     'The [[perito|loss adjuster]] assesses the damage and the insurer authorises the '
                     'repair.',
                     'We repair the car and keep you informed.',
                     "We hand it back; if there's an [[franquicia|excess]], you only pay that part according "
                     'to your policy.']),
                   ('h2', 'Free choice of repairer'),
                   ('p',
                    "It's one of the most common questions. Your insurer may recommend approved workshops, "
                    'but as a general rule the [[libre-eleccion-de-taller|free choice of repairer]] lets you '
                    'take the car wherever you prefer. What can vary by policy is how the repair is paid for '
                    'or whether there are extra conditions. We explain it in detail in our [free choice of '
                    'repairer guide](guia-libre-eleccion-de-taller.html).'),
                   ('h2', 'Loss assessment, demystified'),
                   ('p',
                    'The loss adjuster is a professional who assesses the damage for the insurer. Our role '
                    'is to make sure they see everything they need: visible damage and damage that appears '
                    'once parts are removed. If something new turns up after the first assessment, we report '
                    "it so it can be extended. There's more in our [loss assessment "
                    'guide](guia-peritacion.html).'),
                   ('h2', 'If the damage is serious'),
                   ('p',
                    "When the repair cost approaches or exceeds the car's value, the insurer may declare it "
                    "a total loss. It's a delicate situation and it pays to know your rights. We explain it "
                    'in our [total loss guide](guia-perdida-total.html).'),
                   ('p',
                    'A tip after a knock: take photos of the damage and the scene before moving the car if '
                    "it's safe to do so, keep a copy of the accident report and note the claim number your "
                    'insurer gives you. That information speeds up the assessment and avoids '
                    "misunderstandings. If the car can't be driven, call your policy's roadside assistance "
                    'and ask them to bring it to our workshop.'),
                   ('h2', "What we don't do"),
                   ('p',
                    "We don't decide for your insurer and we can't guarantee what it will cover: that "
                    "depends on your policy. Nor will we ask you to sign anything you don't understand. We "
                    'explain every step so you can make informed decisions.'),
                   ('p',
                    "If you've just had an accident, start with our [claims](siniestros.html) page. If you "
                    'already have a claim number, [book an appointment](pedir-cita.html) or [get in '
                    'touch](contacto.html).')],
         'faq': [('Which insurers do you work with?',
                  'We work with your insurance company. If you have questions about your particular case, '
                  "call us with your policy details and we'll look into it."),
                 ('My insurer told me to go to another workshop. Can I come to you?',
                  'Generally yes, thanks to the free choice of repairer. Check your policy conditions in '
                  "case there's anything specific and, if you like, we'll go through them together."),
                 ('Will I have to pay anything?',
                  "It depends on your cover and whether your policy has an excess. We'll explain before we "
                  'start.'),
                 ('What if the adjuster misses some damage?',
                  'If hidden damage appears when parts are removed, we report it to the insurer so it can be '
                  'reviewed.')]}},
 {'slug': 'servicio-presupuesto-sin-compromiso',
  'cat': 'ventajas',
  'icon': 'doc',
  'es': {'titulo': 'Presupuesto sin compromiso',
         'corto': 'Presupuesto por escrito y claro antes de reparar. Tú decides si seguimos adelante, sin '
                  'presiones.',
         'entradilla': 'Antes de tocar tu coche, sabrás qué vamos a hacer y cuánto va a costar. Te damos el '
                       'presupuesto por escrito y tú decides con calma.',
         'por_que_titulo': 'Por qué un presupuesto por escrito',
         'por_que': [('doc',
                      'Es tu derecho',
                      'La normativa de talleres reconoce tu derecho a recibir un presupuesto por escrito '
                      'antes de la reparación.'),
                     ('euro',
                      'Sin sorpresas en la factura',
                      'Sabes de antemano qué incluye el trabajo, las piezas y la mano de obra.'),
                     ('check',
                      'Decides tú',
                      'Puedes aceptarlo, pedir aclaraciones o pensarlo. Sin presiones.')],
         'incluye_titulo': 'Qué incluye nuestro presupuesto',
         'incluye_intro': 'Un documento claro, con lo necesario para que entiendas la reparación y puedas '
                          'compararla.',
         'incluye': [('search',
                      'Descripción del trabajo',
                      'Qué le pasa al coche y qué vamos a hacer para solucionarlo, con palabras claras.'),
                     ('tool',
                      'Piezas y mano de obra',
                      'Detalle de recambios y del tiempo de trabajo previsto.'),
                     ('calendar', 'Validez', 'Hasta cuándo es válido el presupuesto.'),
                     ('clock',
                      'Previsión de entrega',
                      'Una estimación orientativa del tiempo de reparación, que depende también de la '
                      'llegada de piezas.'),
                     ('chat',
                      'Explicación en persona',
                      'Si quieres, te lo explicamos punto por punto por teléfono o en el taller.')],
         'nota': 'Algunas valoraciones que requieren desmontar piezas o dedicar bastante tiempo pueden tener '
                 'coste. Si es tu caso, te lo decimos antes de empezar, para que lo aceptes o no.',
         'texto': [('h2', 'Lo que dice la normativa'),
                   ('p',
                    'El Real Decreto 1457/1986, que regula la actividad de los talleres de reparación de '
                    'vehículos, reconoce el derecho del cliente a recibir un [[presupuesto|presupuesto]] por '
                    'escrito antes de que se realice la reparación. Solo puedes renunciar a él de forma '
                    'expresa. Una vez aceptado, el taller no debería cobrarte trabajos que no estén en él '
                    'sin tu autorización.'),
                   ('p',
                    'La misma norma recoge el [[resguardo-de-deposito|resguardo de depósito]] cuando dejas '
                    'el coche, la [[garantia-de-reparacion|garantía de la reparación]] y el derecho a una '
                    '[[hoja-de-reclamaciones|hoja de reclamaciones]]. Son garantías para ti y para nosotros: '
                    'todo queda claro desde el principio.'),
                   ('h2', 'Cómo lo hacemos'),
                   ('checks',
                    ['Revisamos el coche o el daño, en el taller o con fotos si es algo sencillo de valorar.',
                     'Te explicamos qué hemos visto y qué opciones hay.',
                     'Te entregamos el presupuesto por escrito con el detalle del trabajo.',
                     'Tú decides si lo aceptas. Sin prisas.',
                     'Si al desmontar aparece algo nuevo, te lo contamos y ampliamos el presupuesto antes de '
                     'seguir.']),
                   ('h2', 'Presupuestos rápidos'),
                   ('p',
                    'Nuestros clientes destacan que damos presupuestos rápidos. Para golpes y daños de '
                    'carrocería, a veces unas fotos bastan para darte una primera orientación, que luego '
                    'confirmamos al ver el coche. Si el golpe ha podido llegar a piezas interiores, hace falta '
                    'verlo en el taller, porque por fuera no siempre se aprecia todo el daño.'),
                   ('h2', 'Si va por el seguro'),
                   ('p',
                    'En las reparaciones por seguro, la valoración la hace el perito de la compañía. '
                    'Nosotros preparamos la información técnica y te explicamos qué cubre y qué no. Más '
                    'detalles en [gestión con aseguradoras](servicio-gestion-con-aseguradoras.html).'),
                   ('h2', 'Compara con tranquilidad'),
                   ('p',
                    'Un presupuesto por escrito te permite comparar. Te recomendamos fijarte no solo en el '
                    'precio final, sino en lo que incluye: tipo de recambio, trabajos de preparación, '
                    'garantía. Un precio más bajo puede incluir menos cosas.'),
                   ('p',
                    'Cuando pidas presupuesto, cuéntanos lo que sepas: matrícula o modelo exacto, qué notas '
                    'y desde cuándo, si el coche ha tenido reparaciones recientes. Con daños de carrocería, '
                    'envía fotos de cerca y de lejos, con buena luz. Así la primera orientación será más '
                    'ajustada y habrá menos diferencias cuando veamos el coche en el taller.'),
                   ('p',
                    'Puedes solicitarlo desde nuestra página de [presupuesto](presupuesto.html), [pedir '
                    'cita](pedir-cita.html) para que veamos el coche o [contactar con '
                    'nosotros](contacto.html).')],
         'faq': [('¿El presupuesto es gratis?',
                  'Pedir presupuesto no te compromete a nada. Si la valoración exige desmontar piezas o '
                  'mucho tiempo, te avisamos antes de si tiene coste.'),
                 ('¿Puedo pedir presupuesto por WhatsApp?',
                  'Sí, envíanos fotos del daño al 674 06 13 71 y te damos una primera orientación. Para '
                  'cerrarlo, normalmente tenemos que ver el coche.'),
                 ('¿Y si la reparación cuesta más de lo presupuestado?',
                  'No hacemos trabajos fuera del presupuesto sin tu autorización. Si aparece algo nuevo, te '
                  'lo contamos antes.'),
                 ('¿Cuánto tiempo es válido?', 'Lo indicamos en el propio presupuesto.')]},
  'en': {'titulo': 'No-obligation estimate',
         'corto': 'A clear written estimate before any repair. You decide whether we go ahead, with no '
                  'pressure.',
         'entradilla': "Before we touch your car, you'll know what we plan to do and what it will cost. We "
                       'give you the estimate in writing and you decide in your own time.',
         'por_que_titulo': 'Why a written estimate',
         'por_que': [('doc',
                      "It's your right",
                      'Spanish workshop regulations recognise your right to a written estimate before the '
                      'repair.'),
                     ('euro',
                      'No surprises on the invoice',
                      'You know in advance what the job, parts and labour include.'),
                     ('check',
                      'You decide',
                      'You can accept it, ask questions or think it over. No pressure.')],
         'incluye_titulo': 'What our estimate includes',
         'incluye_intro': 'A clear document with everything you need to understand the repair and compare '
                          'it.',
         'incluye': [('search',
                      'Description of the work',
                      "What's wrong with the car and what we'll do to fix it, in plain words."),
                     ('tool', 'Parts and labour', 'A breakdown of parts and expected labour time.'),
                     ('calendar', 'Validity', 'How long the estimate is valid for.'),
                     ('clock',
                      'Expected turnaround',
                      'An approximate repair time, which also depends on parts arriving.'),
                     ('chat',
                      'Explained in person',
                      "If you like, we'll go through it point by point by phone or at the workshop.")],
         'nota': 'Some assessments that require removing parts or a lot of time may carry a charge. If '
                 "so, we'll tell you before starting so you can decide.",
         'texto': [('h2', 'What the regulations say'),
                   ('p',
                    'Royal Decree 1457/1986, which regulates vehicle repair workshops in Spain, recognises '
                    "the customer's right to a written [[presupuesto|repair estimate]] before the repair is "
                    "carried out. You can only waive it expressly. Once accepted, the workshop shouldn't "
                    'charge you for work not included without your authorisation.'),
                   ('p',
                    'The same regulation covers the [[resguardo-de-deposito|vehicle deposit receipt]] when '
                    'you leave the car, the [[garantia-de-reparacion|repair warranty]] and the right to a '
                    '[[hoja-de-reclamaciones|complaints form]]. These are safeguards for you and for us: '
                    'everything is clear from the start.'),
                   ('h2', 'How we do it'),
                   ('checks',
                    ["We inspect the car or the damage, at the workshop or from photos if it's simple to "
                     'assess.',
                     "We explain what we've found and what the options are.",
                     'We give you a written estimate with details of the work.',
                     'You decide whether to accept. No rush.',
                     'If something new appears during dismantling, we tell you and extend the estimate '
                     'before carrying on.']),
                   ('h2', 'Quick estimates'),
                   ('p',
                    'Our customers often mention how quickly we provide estimates. For knocks and body '
                    'damage, a few photos are sometimes enough for an initial idea, which we then confirm '
                    'when we see the car. If the impact may have reached inner parts, we need to see it at '
                    "the workshop, because not all the damage shows from outside."),
                   ('h2', "If it's an insurance job"),
                   ('p',
                    "On insurance repairs, the assessment is done by the insurer's loss adjuster. We prepare "
                    "the technical information and explain what's covered and what isn't. More details under "
                    '[insurance handling](servicio-gestion-con-aseguradoras.html).'),
                   ('h2', 'Compare with confidence'),
                   ('p',
                    'A written estimate lets you compare. We suggest looking not just at the final price but '
                    "at what's included: type of part, preparation work, guarantee. A lower price may "
                    'include less.'),
                   ('p',
                    'When you ask for an estimate, tell us what you know: registration or exact model, what '
                    "you've noticed and since when, and whether the car has had recent repairs. For body "
                    'damage, send close-up and wider photos in good light. That way the initial idea will be '
                    "more accurate and there'll be fewer differences once we see the car at the workshop."),
                   ('p',
                    'You can request one from our [estimate](presupuesto.html) page, [book an '
                    'appointment](pedir-cita.html) so we can see the car, or [get in '
                    'touch](contacto.html).')],
         'faq': [('Is the estimate free?',
                  "Asking for an estimate doesn't commit you to anything. If the assessment requires "
                  "removing parts or a lot of time, we'll tell you beforehand whether there's a charge."),
                 ('Can I ask for an estimate on WhatsApp?',
                  "Yes, send photos of the damage to 674 06 13 71 and we'll give you an initial idea. To "
                  'finalise it, we usually need to see the car.'),
                 ('What if the repair costs more than the estimate?',
                  "We don't do work outside the estimate without your authorisation. If something new comes "
                  'up, we tell you first.'),
                 ('How long is it valid?', 'We state it on the estimate itself.')]}},
 {'slug': 'servicio-limpieza-del-vehiculo',
  'cat': 'ventajas',
  'icon': 'sparkle',
  'es': {'titulo': 'Limpieza del vehículo',
         'corto': 'Te devolvemos el coche limpio por dentro y por fuera. Un detalle que nuestros clientes '
                  'valoran mucho.',
         'entradilla': 'Una reparación bien hecha merece una entrega a la altura. Por eso te devolvemos el '
                       'coche limpio, por dentro y por fuera.',
         'por_que_titulo': 'Por qué lo hacemos',
         'por_que': [('star',
                      'Lo destacan nuestros clientes',
                      'Es uno de los detalles que más se repite en las opiniones: recibir el coche limpio, '
                      'también por dentro.'),
                     ('eye',
                      'Ves bien el resultado',
                      'Con el coche limpio es más fácil apreciar la reparación, sobre todo en chapa y '
                      'pintura.'),
                     ('handshake',
                      'Respeto por tu coche',
                      'Tu coche es tuyo. Queremos que vuelva a ti mejor de lo que llegó.')],
         'incluye_titulo': 'Qué incluye',
         'incluye_intro': 'Una limpieza de cortesía con la entrega de tu coche tras la reparación.',
         'incluye': [('drop',
                      'Exterior',
                      'Lavado exterior para retirar polvo, restos del taller y la calima acumulada.'),
                     ('car',
                      'Interior',
                      'Limpieza del habitáculo: aspirado y repaso de las superficies principales.'),
                     ('check',
                      'Revisión final',
                      'Comprobamos que no quedan restos de la reparación en el coche.'),
                     ('shield',
                      'Protección durante el trabajo',
                      'Protegemos asientos, volante y suelo mientras el coche está en el taller.')],
         'nota': 'Es una limpieza de cortesía, no un servicio de detallado o de limpieza profunda de '
                 'tapicerías. Si buscas un tratamiento específico para la pintura, consulta el pulido y '
                 'abrillantado.',
         'texto': [('h2', 'Un detalle que marca la diferencia'),
                   ('p',
                    'Desde que empezamos en 2019 quisimos ser algo más que un simple taller. Parte de eso '
                    'está en los detalles, y uno de los que más valoran nuestros clientes en sus '
                    '[opiniones](opiniones.html) es recibir el coche limpio por dentro y por fuera tras la '
                    'reparación. No es lo principal de nuestro trabajo, pero dice mucho de cómo lo hacemos.'),
                   ('h2', 'Qué hacemos'),
                   ('checks',
                    ['Protegemos asientos, volante y suelo durante la reparación para no ensuciar el '
                     'interior.',
                     'Lavamos el exterior antes de la entrega para quitar polvo, calima y restos del taller.',
                     'Aspiramos el interior y repasamos las superficies principales.',
                     'Revisamos que no quede polvo de lijado ni restos de [[masilla]] en juntas y huecos.']),
                   ('h2', 'Especialmente útil tras chapa y pintura'),
                   ('p',
                    'En los trabajos de [[carroceria|carrocería]] se lija, se aplica masilla y se pinta. '
                    'Aunque la pintura se aplica en la [[cabina-de-pintura|cabina de pintura]], el polvo del '
                    'proceso puede depositarse en otras zonas del coche. Una buena limpieza final permite '
                    'que veas la reparación como es y que no te lleves restos a casa.'),
                   ('h2', 'El clima del sur y tu coche'),
                   ('p',
                    'En el sur de Tenerife el coche acumula polvo, salitre y, en días de calima, una capa '
                    'fina de arena. Te dejamos algunos consejos para mantenerlo entre visitas:'),
                   ('checks',
                    ['Lava el coche con más frecuencia si aparcas cerca del mar: el salitre favorece la '
                     'corrosión.',
                     'Tras un episodio de calima, aclara con abundante agua antes de frotar, para no rayar '
                     'la pintura.',
                     'Evita lavar al sol del mediodía: el agua se seca rápido y deja marcas.',
                     'Usa parasol en el parabrisas para proteger el salpicadero del sol intenso.']),
                   ('p',
                    'Si hay algo en el interior que prefieras que no toquemos, como una sillita infantil ya '
                    'instalada o objetos personales en la guantera, avísanos al dejar el coche. Y si notas '
                    'cualquier cosa en la entrega que no te convence, dínoslo en ese momento. Queremos que '
                    'salgas del taller contento con la reparación y también con cómo te devolvemos el '
                    'coche.'),
                   ('h2', '¿Buscas algo más?'),
                   ('p',
                    'Si quieres devolverle el brillo a la pintura, eliminar pequeños arañazos superficiales '
                    'o proteger el acabado, consulta nuestro servicio de [pulido y '
                    'abrillantado](servicio-pulido-y-abrillantado.html). Si tus faros están amarillentos, '
                    'mira la [restauración de faros](servicio-restauracion-de-faros.html). Para cualquier '
                    'otra consulta, [contacta con nosotros](contacto.html).')],
         'faq': [('¿La limpieza tiene coste?',
                  'Forma parte de cómo te entregamos el coche tras la reparación. Si tienes dudas sobre tu '
                  'caso, te lo confirmamos en el presupuesto.'),
                 ('¿Limpiáis la tapicería a fondo?',
                  'No. Es una limpieza de cortesía, no un tratamiento profundo de tapicerías.'),
                 ('¿Puedo pedir que no laven el coche?',
                  'Claro. Si prefieres lavarlo tú o tienes algún motivo, dínoslo al dejarlo.'),
                 ('¿También limpiáis el coche si solo es un retoque pequeño?',
                  'Nuestro objetivo es devolverte siempre el coche en buen estado. Si tienes alguna '
                  'preferencia, coméntanosla.')]},
  'en': {'titulo': 'Vehicle cleaning',
         'corto': 'We hand your car back clean inside and out. A detail our customers really appreciate.',
         'entradilla': "A job well done deserves a handover to match. That's why we return your car clean, "
                       'inside and out.',
         'por_que_titulo': 'Why we do it',
         'por_que': [('star',
                      'Our customers mention it',
                      "It's one of the details that comes up most in reviews: getting the car back clean, "
                      'inside too.'),
                     ('eye',
                      'You can see the result',
                      "With a clean car it's easier to appreciate the repair, especially bodywork and "
                      'paint.'),
                     ('handshake',
                      'Respect for your car',
                      'Your car is yours. We want it to come back better than it arrived.')],
         'incluye_titulo': "What's included",
         'incluye_intro': 'A courtesy clean when your car is handed back after the repair.',
         'incluye': [('drop',
                      'Exterior',
                      'An exterior wash to remove dust, workshop residue and built-up calima dust.'),
                     ('car', 'Interior', 'Cleaning the cabin: vacuuming and a wipe of the main surfaces.'),
                     ('check', 'Final check', 'We make sure no traces of the repair are left in the car.'),
                     ('shield',
                      'Protection during work',
                      'We cover seats, steering wheel and floor while the car is in the workshop.')],
         'nota': "It's a courtesy clean, not a detailing service or deep upholstery clean. If you're after a "
                 'specific paint treatment, see polishing.',
         'texto': [('h2', 'A detail that makes a difference'),
                   ('p',
                    "Since we started in 2019 we've wanted to be more than just a garage. Part of that is in "
                    'the details, and one our customers value most in their [reviews](opiniones.html) is '
                    "getting the car back clean inside and out after the repair. It isn't the core of our "
                    'work, but it says a lot about how we do it.'),
                   ('h2', 'What we do'),
                   ('checks',
                    ['We cover seats, steering wheel and floor during the repair so the interior stays '
                     'clean.',
                     'We wash the exterior before handover to remove dust, calima and workshop residue.',
                     'We vacuum the interior and wipe the main surfaces.',
                     'We check no sanding dust or [[masilla|body filler]] residue is left in seams and '
                     'gaps.']),
                   ('h2', 'Especially useful after bodywork and paint'),
                   ('p',
                    '[[carroceria|Bodywork]] jobs involve sanding, filler and paint. Even though painting is '
                    'done in the [[cabina-de-pintura|paint booth]], dust from the process can settle '
                    'elsewhere on the car. A good final clean lets you see the repair as it really is and '
                    "means you don't take any residue home."),
                   ('h2', 'The southern climate and your car'),
                   ('p',
                    'In the south of Tenerife cars collect dust, salt and, on calima days, a fine layer of '
                    'sand. Here are a few tips to keep yours in shape between visits:'),
                   ('checks',
                    ['Wash the car more often if you park near the sea: salt encourages corrosion.',
                     "After a calima episode, rinse with plenty of water before rubbing, so you don't "
                     'scratch the paint.',
                     'Avoid washing in the midday sun: water dries fast and leaves marks.',
                     'Use a windscreen sunshade to protect the dashboard from the strong sun.']),
                   ('p',
                    "If there's anything inside you'd rather we didn't touch, such as a child seat already "
                    'fitted or personal items in the glovebox, let us know when you drop the car off. And if '
                    "anything at handover doesn't feel right, tell us there and then. We want you to leave "
                    'happy with the repair and with the way we return your car.'),
                   ('h2', 'Looking for more?'),
                   ('p',
                    "If you'd like to restore your paint's shine, remove light surface scratches or protect "
                    'the finish, see our [polishing](servicio-pulido-y-abrillantado.html) service. If your '
                    'headlights have gone yellow, look at [headlight '
                    'restoration](servicio-restauracion-de-faros.html). For anything else, [get in '
                    'touch](contacto.html).')],
         'faq': [('Is there a charge for cleaning?',
                  "It's part of how we hand your car back after a repair. If you have questions about your "
                  "case, we'll confirm it in the estimate."),
                 ('Do you deep-clean the upholstery?',
                  "No. It's a courtesy clean, not a deep upholstery treatment."),
                 ('Can I ask you not to wash the car?',
                  "Of course. If you'd rather wash it yourself or have a reason, just tell us when you drop "
                  'it off.'),
                 ("Do you clean the car if it's only in for a small touch-up?",
                  'Our aim is always to return your car in good condition. If you have any preference, let '
                  'us know.')]}}]
