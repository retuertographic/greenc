"""Textos legales (ES/EN): aviso legal, política de privacidad y cookies."""

_TITULAR_ES = [
    "Titular: T Mas T Summerfeeling, S.L. (nombre comercial: Green Car Service Tenerife).",
    "CIF: B38553269.",
    "Domicilio: Av. Siete Islas Canarias, 34, Pol. Ind. Llano del Camello, 38639 Las Chafiras, San Miguel de Abona (Santa Cruz de Tenerife).",
    "Correo electrónico: info@greencarservicetenerife.com.",
    "Teléfono: 922 73 64 47.",
]
_TITULAR_EN = [
    "Owner: T Mas T Summerfeeling, S.L. (trading as Green Car Service Tenerife).",
    "Tax ID (CIF): B38553269.",
    "Registered address: Av. Siete Islas Canarias, 34, Pol. Ind. Llano del Camello, 38639 Las Chafiras, San Miguel de Abona (Santa Cruz de Tenerife), Spain.",
    "Email: info@greencarservicetenerife.com.",
    "Telephone: +34 922 73 64 47.",
]

LEGAL = {
    # ------------------------------------------------------------------
    "aviso-legal": {
        "es": {
            "titulo": "Aviso legal",
            "entradilla": "Condiciones de uso de este sitio web e información sobre su titular, conforme a la Ley 34/2002, de Servicios de la Sociedad de la Información y de Comercio Electrónico (LSSI-CE).",
            "secciones": [
                ("Datos identificativos", [
                    ("p", "En cumplimiento del artículo 10 de la LSSI-CE, se informa de los datos del titular de este sitio web:"),
                    ("ul", _TITULAR_ES),
                ]),
                ("Objeto", [
                    ("p", "Este sitio web tiene por objeto informar sobre los servicios de chapa, pintura, mecánica y reparación de vehículos que presta Green Car Service Tenerife, así como sobre la venta de vehículos de ocasión, y facilitar el contacto con el taller."),
                    ("p", "El acceso al sitio es gratuito y no requiere registro. El uso del sitio implica la aceptación de este aviso legal. Si no estás de acuerdo con su contenido, te rogamos que no utilices el sitio."),
                ]),
                ("Condiciones de uso", [
                    ("p", "Te comprometes a hacer un uso adecuado del sitio y de sus contenidos, de acuerdo con la ley, la buena fe y el orden público. En particular, te comprometes a no:"),
                    ("ul", [
                        "Utilizar el sitio con fines ilícitos o que puedan perjudicar los derechos de terceros.",
                        "Introducir virus o cualquier otro sistema que pueda dañar el sitio o los equipos de otros usuarios.",
                        "Reproducir, distribuir o modificar los contenidos sin autorización del titular.",
                    ]),
                ]),
                ("Carácter informativo de los contenidos", [
                    ("p", "Las guías, artículos, preguntas frecuentes y el diccionario de chapa y pintura tienen carácter meramente informativo y general. No constituyen asesoramiento jurídico, técnico ni asegurador sobre un caso concreto."),
                    ("p", "Los precios, plazos y condiciones de cada trabajo se confirman en el presupuesto correspondiente. Las coberturas de seguro dependen siempre de la póliza de cada cliente."),
                ]),
                ("Propiedad intelectual e industrial", [
                    ("p", "Los textos, imágenes, logotipos, diseño gráfico y demás elementos del sitio son titularidad de T Mas T Summerfeeling, S.L. o de terceros que han autorizado su uso, y están protegidos por la normativa de propiedad intelectual e industrial."),
                    ("p", "Queda prohibida su reproducción, distribución, comunicación pública o transformación, total o parcial, sin autorización expresa del titular, salvo para uso personal y privado."),
                ]),
                ("Enlaces", [
                    ("p", "El sitio puede incluir enlaces a páginas de terceros, como redes sociales o mapas. El titular no controla esos sitios ni se responsabiliza de sus contenidos, de su disponibilidad ni de sus políticas de privacidad."),
                    ("p", "Si deseas enlazar a este sitio desde otra página, el enlace no podrá dar a entender una relación con el titular que no exista ni incluir contenidos ilícitos."),
                ]),
                ("Responsabilidad", [
                    ("p", "El titular procura que la información del sitio sea exacta y esté actualizada, pero no garantiza la ausencia de errores ni la disponibilidad continua del sitio. En la medida permitida por la ley, no se hace responsable de los daños derivados del uso de la información publicada ni de interrupciones técnicas ajenas a su control."),
                ]),
                ("Protección de datos y cookies", [
                    ("p", "El tratamiento de datos personales se rige por la [política de privacidad](politica-de-privacidad.html). El uso de cookies y tecnologías similares se explica en la [política de cookies](cookies.html)."),
                ]),
                ("Legislación aplicable y jurisdicción", [
                    ("p", "Este aviso legal se rige por la legislación española. Para cualquier controversia, las partes se someterán a los juzgados y tribunales que correspondan conforme a la ley. Si actúas como consumidor, serán competentes los del lugar de tu domicilio."),
                    ("p", "El titular podrá modificar este aviso legal cuando sea necesario. La versión vigente es la publicada en esta página."),
                ]),
            ],
        },
        "en": {
            "titulo": "Legal notice",
            "entradilla": "Terms of use of this website and information about its owner, in accordance with Spanish Law 34/2002 on Information Society Services and Electronic Commerce (LSSI-CE).",
            "secciones": [
                ("Owner details", [
                    ("p", "In accordance with Article 10 of the LSSI-CE, the details of the owner of this website are as follows:"),
                    ("ul", _TITULAR_EN),
                ]),
                ("Purpose", [
                    ("p", "The purpose of this website is to provide information about the bodywork, paint, mechanical and vehicle repair services offered by Green Car Service Tenerife, as well as the sale of used vehicles, and to make it easy to contact the workshop."),
                    ("p", "Access to the site is free of charge and does not require registration. Using the site implies acceptance of this legal notice. If you do not agree with it, please do not use the site."),
                ]),
                ("Terms of use", [
                    ("p", "You agree to use the site and its content appropriately, in accordance with the law, good faith and public order. In particular, you agree not to:"),
                    ("ul", [
                        "Use the site for unlawful purposes or in ways that may harm the rights of third parties.",
                        "Introduce viruses or any other system that could damage the site or other users' devices.",
                        "Reproduce, distribute or modify the content without the owner's permission.",
                    ]),
                ]),
                ("Information purposes only", [
                    ("p", "The guides, articles, frequently asked questions and car glossary are for general information only. They do not constitute legal, technical or insurance advice on any specific case."),
                    ("p", "Prices, timescales and conditions for each job are confirmed in the corresponding estimate. Insurance cover always depends on each customer's policy."),
                ]),
                ("Intellectual and industrial property", [
                    ("p", "The texts, images, logos, graphic design and other elements of the site belong to T Mas T Summerfeeling, S.L. or to third parties who have authorised their use, and are protected by intellectual and industrial property law."),
                    ("p", "Reproduction, distribution, public communication or transformation of all or part of them without the owner's express permission is prohibited, except for personal and private use."),
                ]),
                ("Links", [
                    ("p", "The site may include links to third-party pages, such as social networks or maps. The owner does not control those sites and accepts no responsibility for their content, availability or privacy policies."),
                    ("p", "If you wish to link to this site from another page, the link must not suggest a relationship with the owner that does not exist or include unlawful content."),
                ]),
                ("Liability", [
                    ("p", "The owner endeavours to keep the information on the site accurate and up to date, but does not guarantee that it is free of errors or that the site will be continuously available. To the extent permitted by law, the owner is not liable for damage arising from the use of the published information or from technical interruptions beyond its control."),
                ]),
                ("Data protection and cookies", [
                    ("p", "The processing of personal data is governed by the [privacy policy](politica-de-privacidad.html). The use of cookies and similar technologies is explained in the [cookie policy](cookies.html)."),
                ]),
                ("Governing law and jurisdiction", [
                    ("p", "This legal notice is governed by Spanish law. Any dispute will be submitted to the courts that have jurisdiction under the law. If you are acting as a consumer, the courts of your place of residence will have jurisdiction."),
                    ("p", "The owner may amend this legal notice when necessary. The version in force is the one published on this page. In the event of any discrepancy between language versions, the Spanish version shall prevail."),
                ]),
            ],
        },
    },
    # ------------------------------------------------------------------
    "politica-de-privacidad": {
        "es": {
            "titulo": "Política de privacidad",
            "entradilla": "Cómo tratamos los datos personales que nos facilitas, de acuerdo con el Reglamento (UE) 2016/679 (RGPD) y la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales (LOPDGDD).",
            "secciones": [
                ("Responsable del tratamiento", [
                    ("ul", _TITULAR_ES),
                    ("p", "Para cualquier cuestión relacionada con tus datos personales puedes escribirnos a info@greencarservicetenerife.com."),
                ]),
                ("Qué datos tratamos", [
                    ("p", "Este sitio web es estático: no dispone de formularios que envíen datos a un servidor propio ni de áreas de usuario. Tratamos únicamente los datos que tú decides facilitarnos cuando te pones en contacto con nosotros, por ejemplo:"),
                    ("ul", [
                        "Datos de identificación y contacto: nombre, teléfono y correo electrónico.",
                        "Datos del vehículo: marca, modelo, matrícula y descripción de la avería o del daño.",
                        "Datos relacionados con un siniestro, cuando nos pides que lo gestionemos con tu aseguradora.",
                        "Cualquier otra información que incluyas en tus mensajes.",
                    ]),
                    ("p", "Los formularios de cita, presupuesto y contacto de esta web abren tu propio programa de correo electrónico con el mensaje preparado. Los datos solo nos llegan si tú decides enviar ese correo."),
                ]),
                ("Finalidades", [
                    ("ul", [
                        "Atender tus consultas y solicitudes de información.",
                        "Gestionar citas, presupuestos y la prestación de los servicios de reparación.",
                        "Gestionar, a petición tuya, la tramitación de siniestros con tu compañía de seguros.",
                        "Gestionar la venta de vehículos de ocasión.",
                        "Cumplir las obligaciones legales, contables y fiscales que correspondan.",
                    ]),
                    ("p", "No elaboramos perfiles ni tomamos decisiones automatizadas con tus datos, y no los utilizamos para enviarte publicidad sin tu consentimiento."),
                ]),
                ("Base jurídica", [
                    ("ul", [
                        "Tu consentimiento, al ponerte en contacto con nosotros (art. 6.1.a RGPD).",
                        "La aplicación de medidas precontractuales o la ejecución del contrato de servicio (art. 6.1.b RGPD).",
                        "El cumplimiento de obligaciones legales, por ejemplo en materia fiscal o de talleres de reparación (art. 6.1.c RGPD).",
                    ]),
                ]),
                ("Plazo de conservación", [
                    ("p", "Conservamos los datos durante el tiempo necesario para atender tu solicitud o prestar el servicio y, después, durante los plazos que exija la ley para atender posibles responsabilidades. Las consultas que no den lugar a una relación comercial se eliminan cuando dejan de ser necesarias."),
                ]),
                ("Destinatarios", [
                    ("p", "No cedemos tus datos a terceros salvo obligación legal o cuando sea necesario para prestar el servicio que nos pides, por ejemplo:"),
                    ("ul", [
                        "A tu compañía de seguros y a los peritos que designe, cuando gestionamos un siniestro por encargo tuyo.",
                        "A las administraciones públicas, cuando lo exija la normativa.",
                        "A proveedores que nos prestan servicios (correo electrónico, gestión administrativa), con los que tenemos los contratos de encargo de tratamiento exigidos.",
                    ]),
                    ("p", "Si te comunicas con nosotros por WhatsApp, el servicio lo presta un tercero que puede tratar datos fuera del Espacio Económico Europeo con las garantías previstas en el RGPD. Si lo prefieres, puedes usar el teléfono o el correo electrónico."),
                ]),
                ("Tus derechos", [
                    ("p", "Puedes ejercer en cualquier momento los siguientes derechos escribiendo a info@greencarservicetenerife.com o por correo postal a nuestro domicilio, indicando el derecho que ejerces y acreditando tu identidad:"),
                    ("ul", [
                        "Acceso a tus datos.",
                        "Rectificación de los datos inexactos.",
                        "Supresión de tus datos.",
                        "Limitación y oposición al tratamiento.",
                        "Portabilidad de los datos.",
                        "Retirada del consentimiento, sin que afecte a la licitud del tratamiento anterior.",
                    ]),
                    ("p", "Si consideras que no hemos atendido correctamente tus derechos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (AEPD), www.aepd.es."),
                ]),
                ("Seguridad y menores", [
                    ("p", "Aplicamos medidas técnicas y organizativas razonables para proteger tus datos frente a pérdidas, accesos no autorizados o alteraciones. Te pedimos que no nos envíes más datos de los necesarios para tu consulta."),
                    ("p", "Este sitio no está dirigido a menores de 14 años, y no tratamos conscientemente datos de menores sin el consentimiento de sus padres o tutores."),
                ]),
                ("Cambios en esta política", [
                    ("p", "Podemos actualizar esta política para adaptarla a cambios legales o de funcionamiento. La versión vigente es la publicada en esta página. Consulta también el [aviso legal](aviso-legal.html) y la [política de cookies](cookies.html)."),
                ]),
            ],
        },
        "en": {
            "titulo": "Privacy policy",
            "entradilla": "How we process the personal data you provide, in accordance with Regulation (EU) 2016/679 (GDPR) and Spanish Organic Law 3/2018 on the Protection of Personal Data and Guarantee of Digital Rights (LOPDGDD).",
            "secciones": [
                ("Data controller", [
                    ("ul", _TITULAR_EN),
                    ("p", "For any question about your personal data, please write to info@greencarservicetenerife.com."),
                ]),
                ("What data we process", [
                    ("p", "This is a static website: it has no forms that send data to our own server and no user accounts. We only process the data you choose to give us when you contact us, for example:"),
                    ("ul", [
                        "Identification and contact details: name, telephone number and email address.",
                        "Vehicle details: make, model, registration and a description of the fault or damage.",
                        "Details of an insurance claim, when you ask us to handle it with your insurer.",
                        "Any other information you include in your messages.",
                    ]),
                    ("p", "The appointment, estimate and contact forms on this website open your own email program with the message ready to send. We only receive the data if you choose to send that email."),
                ]),
                ("Purposes", [
                    ("ul", [
                        "Answering your enquiries and requests for information.",
                        "Managing appointments, estimates and the provision of repair services.",
                        "Handling insurance claims with your insurer, at your request.",
                        "Managing the sale of used vehicles.",
                        "Meeting our legal, accounting and tax obligations.",
                    ]),
                    ("p", "We do not create profiles or make automated decisions with your data, and we do not use it to send you advertising without your consent."),
                ]),
                ("Legal basis", [
                    ("ul", [
                        "Your consent, when you contact us (Art. 6(1)(a) GDPR).",
                        "Taking steps prior to entering into a contract, or performing the service contract (Art. 6(1)(b) GDPR).",
                        "Compliance with legal obligations, for example tax rules or regulations on repair workshops (Art. 6(1)(c) GDPR).",
                    ]),
                ]),
                ("How long we keep data", [
                    ("p", "We keep data for as long as needed to deal with your request or provide the service and, afterwards, for the periods required by law to handle any possible liabilities. Enquiries that do not lead to a business relationship are deleted once they are no longer needed."),
                ]),
                ("Recipients", [
                    ("p", "We do not share your data with third parties except where required by law or where necessary to provide the service you ask for, for example:"),
                    ("ul", [
                        "Your insurance company and the loss adjusters it appoints, when we handle a claim on your behalf.",
                        "Public authorities, where required by law.",
                        "Service providers working for us (email, administration), with whom we have the required data processing agreements.",
                    ]),
                    ("p", "If you contact us via WhatsApp, the service is provided by a third party that may process data outside the European Economic Area with the safeguards set out in the GDPR. If you prefer, you can use the telephone or email instead."),
                ]),
                ("Your rights", [
                    ("p", "You may exercise the following rights at any time by writing to info@greencarservicetenerife.com or by post to our address, stating which right you are exercising and proving your identity:"),
                    ("ul", [
                        "Access to your data.",
                        "Rectification of inaccurate data.",
                        "Erasure of your data.",
                        "Restriction of and objection to processing.",
                        "Data portability.",
                        "Withdrawal of consent, without affecting the lawfulness of earlier processing.",
                    ]),
                    ("p", "If you feel we have not dealt properly with your rights, you can lodge a complaint with the Spanish Data Protection Agency (AEPD), www.aepd.es."),
                ]),
                ("Security and minors", [
                    ("p", "We apply reasonable technical and organisational measures to protect your data against loss, unauthorised access or alteration. Please do not send us more data than your enquiry needs."),
                    ("p", "This site is not aimed at children under 14, and we do not knowingly process children's data without the consent of their parents or guardians."),
                ]),
                ("Changes to this policy", [
                    ("p", "We may update this policy to reflect legal or operational changes. The version in force is the one published on this page. See also the [legal notice](aviso-legal.html) and the [cookie policy](cookies.html)."),
                ]),
            ],
        },
    },
    # ------------------------------------------------------------------
    "cookies": {
        "es": {
            "titulo": "Política de cookies",
            "entradilla": "Qué son las cookies, cuáles puede utilizar este sitio y cómo puedes gestionarlas, conforme al artículo 22.2 de la LSSI-CE y a la guía sobre el uso de cookies de la AEPD.",
            "secciones": [
                ("Qué son las cookies", [
                    ("p", "Las cookies son pequeños archivos que un sitio web guarda en tu navegador. Existen tecnologías similares, como el almacenamiento local del navegador, que cumplen funciones parecidas. En esta política nos referimos a todas ellas como «cookies»."),
                ]),
                ("Qué cookies usa este sitio", [
                    ("p", "Este sitio web es estático y **no utiliza cookies propias de analítica ni de publicidad**, ni rastrea tu navegación con fines comerciales."),
                    ("p", "Como mucho, puede guardar en tu navegador alguna preferencia estrictamente técnica, por ejemplo el idioma o el aspecto de la página que has elegido. Esa información se queda en tu dispositivo, no se envía a ningún servidor y no sirve para identificarte. Al ser necesaria para el funcionamiento que tú solicitas, está exenta de consentimiento."),
                ]),
                ("Recursos y servicios de terceros", [
                    ("p", "Algunas páginas cargan recursos de terceros que pueden recibir datos técnicos de tu conexión (como la dirección IP) o instalar sus propias cookies:"),
                    ("tabla", [
                        "Servicio | Proveedor | Dónde se usa | Finalidad",
                        "Google Fonts | Google | Todo el sitio | Mostrar las tipografías de la web",
                        "Google Maps (mapa incrustado) | Google | Página de contacto | Mostrar la ubicación del taller",
                    ]),
                    ("p", "Estos terceros actúan bajo sus propias políticas de privacidad y cookies, que te recomendamos consultar. El titular del sitio no tiene acceso a la información que recogen."),
                ]),
                ("Enlaces externos", [
                    ("p", "Los enlaces a redes sociales o a WhatsApp te llevan a servicios de terceros. Al hacer clic, se aplican sus propias condiciones y políticas de cookies."),
                ]),
                ("Cómo gestionar o eliminar las cookies", [
                    ("p", "Puedes permitir, bloquear o eliminar las cookies y los datos guardados en cualquier momento desde la configuración de tu navegador. Los principales navegadores lo permiten desde sus menús de privacidad o seguridad:"),
                    ("ul", [
                        "Google Chrome: Configuración > Privacidad y seguridad.",
                        "Mozilla Firefox: Ajustes > Privacidad y seguridad.",
                        "Safari: Ajustes > Privacidad.",
                        "Microsoft Edge: Configuración > Cookies y permisos del sitio.",
                    ]),
                    ("p", "Si bloqueas los recursos de terceros, es posible que algunas partes de la web, como el mapa, no se muestren correctamente."),
                ]),
                ("Más información y cambios", [
                    ("p", "Si en el futuro incorporamos cookies que requieran tu consentimiento, te lo pediremos antes de instalarlas y actualizaremos esta política. Para más información sobre el tratamiento de tus datos, consulta la [política de privacidad](politica-de-privacidad.html) y el [aviso legal](aviso-legal.html)."),
                ]),
            ],
        },
        "en": {
            "titulo": "Cookie policy",
            "entradilla": "What cookies are, which ones this site may use and how you can manage them, in accordance with Article 22.2 of the LSSI-CE and the AEPD's guidance on the use of cookies.",
            "secciones": [
                ("What cookies are", [
                    ("p", "Cookies are small files that a website stores in your browser. There are similar technologies, such as the browser's local storage, that serve comparable purposes. In this policy we refer to all of them as 'cookies'."),
                ]),
                ("Which cookies this site uses", [
                    ("p", "This is a static website and it **does not use its own analytics or advertising cookies**, nor does it track your browsing for commercial purposes."),
                    ("p", "At most, it may store a strictly technical preference in your browser, such as the language or display option you have chosen. That information stays on your device, is not sent to any server and cannot be used to identify you. As it is needed for a feature you request, it is exempt from consent."),
                ]),
                ("Third-party resources and services", [
                    ("p", "Some pages load resources from third parties that may receive technical data about your connection (such as your IP address) or set their own cookies:"),
                    ("tabla", [
                        "Service | Provider | Where it is used | Purpose",
                        "Google Fonts | Google | Whole site | Displaying the website's typefaces",
                        "Google Maps (embedded map) | Google | Contact page | Showing the workshop's location",
                    ]),
                    ("p", "These third parties operate under their own privacy and cookie policies, which we recommend you read. The site owner has no access to the information they collect."),
                ]),
                ("External links", [
                    ("p", "Links to social networks or WhatsApp take you to third-party services. When you click them, their own terms and cookie policies apply."),
                ]),
                ("How to manage or delete cookies", [
                    ("p", "You can allow, block or delete cookies and stored data at any time in your browser settings. The main browsers let you do this from their privacy or security menus:"),
                    ("ul", [
                        "Google Chrome: Settings > Privacy and security.",
                        "Mozilla Firefox: Settings > Privacy & Security.",
                        "Safari: Settings > Privacy.",
                        "Microsoft Edge: Settings > Cookies and site permissions.",
                    ]),
                    ("p", "If you block third-party resources, some parts of the site, such as the map, may not display correctly."),
                ]),
                ("Further information and changes", [
                    ("p", "If we add cookies that require your consent in future, we will ask for it before setting them and update this policy. For more information about how your data is processed, see the [privacy policy](politica-de-privacidad.html) and the [legal notice](aviso-legal.html)."),
                ]),
            ],
        },
    },
}
