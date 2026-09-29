---
icon: lucide/book-open
---

# Introducción al Desarrollo de Interfaces

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Definir el concepto de interfaz de usuario y clasificar los diferentes tipos existentes, identificando sus características, ventajas y contextos de aplicación.
2. Describir la evolución histórica de las interfaces gráficas desde la línea de comandos hasta las interfaces conversacionales basadas en inteligencia artificial, comprendiendo los hitos tecnológicos que han marcado cada etapa.
3. Diferenciar con precisión los conceptos de UX (User Experience) y UI (User Interface), explicando sus ámbitos de actuación, metodologías y perfiles profesionales asociados.
4. Identificar las características diferenciales de las interfaces web, las aplicaciones web progresivas (PWA), las aplicaciones híbridas y las aplicaciones nativas, así como el papel de Electron en el desarrollo de aplicaciones de escritorio con tecnologías web.
5. Reconocer las tendencias actuales en diseño de interfaces, valorando su impacto en la experiencia de usuario y su viabilidad técnica en proyectos reales.
6. Situar el framework Angular dentro del ecosistema de desarrollo de interfaces, comprendiendo su arquitectura, su modelo de componentes y su idoneidad para aplicaciones empresariales.
7. Explicar el proceso de Diseño Centrado en el Usuario (UCD), describiendo cada una de sus fases y las técnicas empleadas en cada una de ellas.
8. Describir el rol del desarrollador de interfaces en equipos de desarrollo modernos, identificando los perfiles con los que colabora y las responsabilidades que asume.

## Resultados de aprendizaje asociados

Este módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE) se organiza en torno a ocho resultados de aprendizaje oficiales:

- **RA 1.** Genera interfaces gráficos de usuario mediante editores visuales utilizando las funcionalidades del editor y adaptando el código generado.
- **RA 2.** Genera interfaces naturales de usuario utilizando herramientas visuales.
- **RA 3.** Crea componentes visuales valorando y empleando herramientas específicas.
- **RA 4.** Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad.
- **RA 5.** Crea informes evaluando y utilizando herramientas gráficas.
- **RA 6.** Documenta aplicaciones seleccionando y utilizando herramientas específicas.
- **RA 7.** Prepara aplicaciones para su distribución evaluando y utilizando herramientas específicas.
- **RA 8.** Evalúa el funcionamiento de aplicaciones diseñando y ejecutando pruebas.

**Cobertura por unidades del módulo:**

| RA | Unidad(es) principal(es) |
|----|--------------------------|
| RA 1 | U4 (Figma), U9 (ecosistema), U10 (Angular), U12 (formularios), U20 (Electron) |
| RA 2 | U3 (interfaces naturales de usuario) |
| RA 3 | U7, U10, U11, U13, U14, U15 (componentes visuales) |
| RA 4 | U1 (UX), U2 (accesibilidad), U4, U5, U6, U8, U17 (usabilidad y accesibilidad) |
| RA 5 | U16 (informes), U17 (dashboards) |
| RA 6 | U14 (documentación de componentes), U18 (documentación de aplicaciones) |
| RA 7 | U20 (Electron), U21 (empaquetado y distribución) |
| RA 8 | U19 (pruebas de software) |

> Nota: los contenidos sobre interfaces por voz, gestos, cuerpo e IA conversacional (VUI/NUI) que se presentan en esta introducción corresponden al **RA 2** y se desarrollan en profundidad en la Unidad 3.

!!! note "Conocimientos previos"

    Para abordar con éxito esta unidad, el alumnado debe poseer los siguientes conocimientos:

    - Fundamentos de programación estructurada y orientada a objetos, adquiridos en el módulo de Programación del primer curso.
    - Conocimientos básicos de **HTML5 y CSS3**, incluyendo la estructura del DOM, selectores CSS, modelo de caja y propiedades fundamentales de estilo.
    - Manejo elemental de entornos de desarrollo integrados (IDE), preferentemente **Visual Studio Code**.
    - Comprensión de la arquitectura cliente-servidor y del funcionamiento básico del protocolo **HTTP**.
    - Experiencia en el uso de navegadores web y sus herramientas de desarrollo integradas (**DevTools**).
    - Capacidad para trabajar con sistemas de control de versiones, específicamente **Git y GitHub**.

    Estos conocimientos previos se consideran prerrequisitos fundamentales. Se recomienda realizar una **evaluación diagnóstica** al inicio de la unidad para detectar posibles carencias y establecer medidas de refuerzo individualizadas.

## Contenidos

**Bloque 1: Fundamentos de las interfaces de usuario**
- **Definición de interfaz de usuario**: concepto, función y relevancia en sistemas software.
- **Tipologías de interfaces**: GUI (Graphical User Interface), CLI (Command Line Interface), VUI (Voice User Interface), NUI (Natural User Interface), TUI (Tangible User Interface).
- **Características técnicas de cada tipo de interfaz**: dispositivos de entrada/salida asociados, tecnologías subyacentes, casos de uso representativos.

**Bloque 2: Evolución histórica de las interfaces**
- **De la línea de comandos a las ventanas**: Xerox Alto, Apple Lisa, Windows 1.0.
- **La era web**: del HTML estático a las aplicaciones de una sola página (SPA).
- **La revolución móvil**: interfaces táctiles, gestos, diseño responsive.
- **Realidad aumentada, realidad virtual e interfaces espaciales**.
- **Interfaces conversacionales e inteligencia artificial generativa**.

**Bloque 3: UX vs UI**
- **Definición precisa de User Experience (UX)**: arquitectura de la información, investigación de usuarios, flujos de navegación, prototipado, usabilidad.
- **Definición precisa de User Interface (UI)**: tipografía, color, espaciado, iconografía, sistemas de diseño, microinteracciones.
- **Comparativa y sinergias entre ambos ámbitos**: por qué son disciplinas complementarias pero diferenciadas.

**Bloque 4: Interfaces web y multiplataforma**
- **Web apps tradicionales**: características, ventajas, limitaciones.
- **Progressive Web Apps (PWA)**: service workers, manifiesto, instalabilidad, funcionalidad offline.
- **Aplicaciones híbridas**: Apache Cordova, Ionic, Capacitor.
- **Aplicaciones nativas vs aplicaciones web**: rendimiento, acceso al hardware, distribución, costes.
- **Electron**: arquitectura, proceso principal y procesos renderizadores, casos de uso emblemáticos (VS Code, Discord, Figma, Slack, Postman, Notion).

**Bloque 5: Tendencias actuales en diseño de interfaces**
- **Neumorfismo**: fundamentos estéticos, implementación técnica, cuándo usarlo y cuándo evitarlo.
- **Glassmorphism**: efecto vidrio esmerilado, backdrop-filter, jerarquía visual.
- **Minimalismo y brutalismo**: reducción a lo esencial.
- **Dark Mode**: beneficios de accesibilidad y ahorro energético, implementación con variables CSS.
- **Microinteracciones**: definición, propósito, ejemplos (animaciones de feedback, transiciones de estado).
- **Motion Design**: principios de animación aplicados a interfaces (timing, easing, choreography).
- **Diseño inclusivo**: más allá de la accesibilidad, diseño para la diversidad humana.
- **IA en interfaces**: generación de layouts, personalización adaptativa, asistentes integrados.

**Bloque 6: El ecosistema Angular en el desarrollo de interfaces**
- **Angular como framework para aplicaciones empresariales**: filosofía, ecosistema, gobernanza.
- **Single Page Applications (SPA)**: concepto y arquitectura.
- **Modelo de componentes**: encapsulación, reutilización, composición.
- **Enrutamiento**: navegación entre vistas sin recarga de página.
- **Servicios e inyección de dependencias**: separación de lógica de negocio.
- **Angular Material y CDK**: componentes accesibles y utilidades de interacción.
- **Angular Signals**: reactividad moderna y granular.

**Bloque 7: Diseño Centrado en el Usuario (UCD)**
- **Proceso UCD según ISO 9241-210**: investigación, especificación, diseño, evaluación.
- **Técnicas de investigación**: entrevistas, encuestas, observación contextual, análisis competitivo.
- **Personas y escenarios de uso**: definición, construcción y aplicación.
- **Mapas de empatía y customer journey maps**.
- **Prototipado de baja y alta fidelidad**.
- **Test de usabilidad**: planificación, ejecución, análisis de resultados.
- **Iteración**: el ciclo construir-medir-aprender.

**Bloque 8: El rol profesional del desarrollador de interfaces**
- **Competencias técnicas requeridas**: HTML, CSS, JavaScript/TypeScript, frameworks, control de versiones, testing.
- **Competencias transversales**: comunicación, trabajo en equipo, resolución de problemas.
- **Colaboración multidisciplinar**: relación con diseñadores UX/UI, product managers, desarrolladores backend, DevOps.
- **El módulo de Desarrollo de Interfaces en el currículo DAM**: relación con Lenguajes de marcas y sistemas de gestión de información, Entornos de desarrollo, Programación, Acceso a datos y Programación multimedia y dispositivos móviles (PMDM).

## Desarrollo teórico

### 1. Qué es una interfaz de usuario

!!! info "Definición"

    Una **interfaz de usuario** (UI, por sus siglas en inglés) constituye el punto de encuentro entre un ser humano y un sistema informático. Es el conjunto de elementos, mecanismos y canales a través de los cuales una persona interactúa con una máquina para proporcionarle instrucciones, recibir información y completar tareas. La interfaz actúa como traductora entre el mundo conceptual humano y el mundo binario de la computadora.

La importancia de la interfaz de usuario no puede subestimarse: para el usuario final, la interfaz **es** el producto. No importa cuán sofisticado sea el algoritmo de recomendación de una plataforma de streaming si el usuario no encuentra el botón de reproducción. No importa la potencia de un motor de base de datos si la pantalla de inicio de sesión resulta confusa. La interfaz condiciona completamente la percepción de calidad, la satisfacción y, en última instancia, la adopción o el abandono de un producto digital.

Existen diversos tipos de interfaces de usuario, cada una con sus características, tecnologías asociadas y contextos de aplicación:

- **GUI (Graphical User Interface):** Es la interfaz gráfica tradicional basada en ventanas, iconos, menús y puntero (WIMP). Los usuarios interactúan mediante dispositivos como el ratón, el teclado o pantallas táctiles, manipulando representaciones visuales de objetos y acciones. Es el tipo predominante en ordenadores personales, aplicaciones web y aplicaciones móviles.

![Graphical User Interface](./img/00/GUI.webp)

- **CLI (Command Line Interface):** Interfaz basada en texto donde el usuario introduce comandos mediante el teclado y recibe respuestas textuales del sistema. Aunque aparentemente arcaica, sigue siendo fundamental en entornos de desarrollo, administración de sistemas y operaciones DevOps por su eficiencia, automatización y precisión.

![Command Line Interface](./img/00/CLI.png)

- **VUI (Voice User Interface):** Interfaz basada en voz que permite la interacción mediante comandos hablados y respuestas sonoras. Tecnologías como el procesamiento de lenguaje natural (NLP) y el reconocimiento automático del habla (ASR) la hacen posible. Asistentes como Alexa, Siri o Google Assistant son ejemplos paradigmáticos.

![Voice User Interface](./img/00/VUI.png)

- **NUI (Natural User Interface):** Interfaces que buscan una interacción "natural" e intuitiva mediante gestos, movimientos corporales o incluso pensamientos. Las pantallas táctiles multitáctiles, los controladores de movimiento (Kinect) y los dispositivos de seguimiento ocular son ejemplos de NUI.

![Natural User Interface](./img/00/NUI.avif)

- **TUI (Tangible User Interface):** Interfaces que permiten la interacción con información digital a través de objetos físicos manipulables. Por ejemplo, un mando MIDI con diales físicos que modifica parámetros de un sintetizador digital, o Reactable, el instrumento musical electrónico que combina objetos físicos con una superficie interactiva.

![Tangible User Interface](./img/00/TUI.jpg)

- **Conversacional:** Lo que define a una interfaz conversacional es la capacidad de mantener un diálogo fluido, con memoria y contexto. No importa si el usuario usa la voz, un teclado o botones; lo importante es la inteligencia de la charla. Se basan en IA avanzada y lenguaje natural puro. Estas interfaces entienden instrucciones ambiguas, recuerdan lo que se ha dicho hace un rato y adaptan sus respuestas dinámicamente sin depender de comandos exactos.

En el contexto de este módulo, nos centraremos fundamentalmente en las interfaces gráficas de usuario (GUI), y más concretamente en las interfaces gráficas desarrolladas con **tecnologías web**, que constituyen la plataforma más extendida para aplicaciones de escritorio, web y, cada vez más, aplicaciones móviles.

### 2. Evolución de las interfaces gráficas

La historia de las interfaces gráficas es la historia de la democratización de la informática. Cada evolución ha reducido la barrera de entrada, ha ampliado la base de usuarios y ha transformado radicalmente la relación entre humanos y máquinas.

**Fase 1: La línea de comandos (años 60-70)**

Antes de la GUI, la interacción con ordenadores se realizaba exclusivamente mediante tarjetas perforadas y, posteriormente, terminales de texto. El usuario debía conocer la sintaxis exacta de comandos crípticos. Solo ingenieros y científicos podían utilizar estas máquinas. Esta fase, sin embargo, sentó las bases de la interacción humano-máquina y sigue vigente en herramientas como PowerShell, Bash o Zsh.

**Fase 2: La era de las ventanas (años 80-90)**

En 1973, Xerox PARC desarrolló el Xerox Alto, el primer ordenador con interfaz gráfica de ventanas, escritorio metafórico y ratón. Aunque nunca se comercializó masivamente, inspiró a Steve Jobs para crear el Apple Lisa (1983) y, sobre todo, el Macintosh (1984). Microsoft lanzó Windows 1.0 en 1985, iniciando una competencia que definiría la informática personal durante décadas.

El paradigma **WIMP** (Windows, Icons, Menus, Pointer) se consolidó como estándar y sigue siendo la base de las interfaces gráficas contemporáneas. La **metáfora del escritorio** (carpetas, archivos, papelera) permitió que personas sin formación técnica pudieran utilizar ordenadores.

**Fase 3: La web (1995-2010)**

Con la popularización de Internet, el navegador web se convirtió en la nueva plataforma de aplicaciones. HTML, CSS y JavaScript reemplazaron progresivamente a las aplicaciones de escritorio tradicionales. La web 2.0 introdujo la **interactividad asíncrona (AJAX)**, permitiendo aplicaciones tan fluidas como las nativas. Servicios como Gmail (2004) demostraron que la web podía competir con el escritorio.

**Fase 4: La revolución móvil (2007-presente)**

El lanzamiento del iPhone en 2007 con su pantalla táctil capacitiva y su interfaz basada en gestos naturales supuso un punto de inflexión comparable al Macintosh de 1984. El **diseño responsive**, popularizado por Ethan Marcotte en 2010, permitió que una misma interfaz se adaptara fluidamente a diferentes tamaños de pantalla. Las aplicaciones móviles nativas añadieron capacidades inexistentes en la web: GPS, acelerómetro, cámara, notificaciones push y acceso sin conexión.

**Fase 5: Realidad extendida y espacios (2015-presente)**

La **realidad aumentada (RA)**, que superpone información digital sobre el mundo real, y la **realidad virtual (RV)**, que sumerge al usuario en entornos completamente virtuales, han abierto nuevas dimensiones para las interfaces. Aplicaciones como Pokémon GO demostraron el potencial masivo de la RA, mientras que dispositivos como Oculus Quest han llevado la RV al consumo doméstico. Las interfaces espaciales presentan desafíos únicos de diseño: interacción en 360 grados, profundidad, prevención de fatiga y cinetosis.

**Fase 6: IA conversacional y generativa (2022-presente)**

La aparición de **modelos de lenguaje de gran escala (LLMs)** como GPT ha inaugurado la era de las interfaces conversacionales avanzadas. Los usuarios pueden expresar sus intenciones en lenguaje natural y obtener respuestas, código o acciones del sistema. La interfaz se diluye: ya no se trata de manipular controles sino de mantener un diálogo. Herramientas como ChatGPT, Copilot o Gemini están redefiniendo lo que significa "usar" una aplicación.

**Lecciones de la evolución**

La tendencia histórica es clara: ==cada nueva generación de interfaces reduce la distancia entre la intención del usuario y la acción del sistema==. De memorizar comandos a señalar con un clic, de hacer clic a deslizar con el dedo, de deslizar a hablar, de hablar a pensar. El desarrollo de interfaces consiste, en esencia, en acortar esa distancia.

Otra tendencia es la abstracción creciente: los detalles técnicos que antes debía conocer el usuario (comandos, rutas de archivos, configuraciones) quedan ocultos bajo capas de diseño y automatización. El rol del desarrollador de interfaces es, precisamente, construir esas capas de abstracción que hacen la tecnología accesible y placentera.

### 3. UX vs UI: dos caras de una misma moneda

La confusión entre **UX (User Experience)** y **UI (User Interface)** es una de las más persistentes en el sector tecnológico. Aunque están íntimamente relacionadas, son disciplinas distintas que responden a preguntas diferentes y requieren habilidades y metodologías diferentes.

**User Experience (UX)** responde a las preguntas: ¿Es útil este producto? ¿Resuelve un problema real? ¿Es fácil de usar? ¿Resulta satisfactorio? La UX abarca el recorrido completo del usuario desde que descubre la existencia del producto hasta que completa su objetivo y más allá. Incluye disciplinas como:

- **Investigación de usuarios:** Entrevistas, encuestas, observación contextual, análisis de datos de uso. Se busca entender quién es el usuario, qué necesita, en qué contexto utilizará el producto y qué problemas encuentra con las soluciones actuales.

- **Arquitectura de la información:** Organización, estructuración y etiquetado del contenido para que los usuarios puedan encontrar información y completar tareas de manera eficiente. El card sorting es una técnica clásica: pedir a usuarios que agrupen conceptos y nombren cada grupo.

- **Diseño de interacción:** Definición de cómo responde el sistema a las acciones del usuario. Los flujos de navegación, los diagramas de secuencia y la especificación de comportamientos son artefactos típicos.

- **Prototipado:** Creación de versiones simuladas del producto, desde bocetos en papel (baja fidelidad) hasta prototipos interactivos en herramientas como Figma (alta fidelidad), para validar hipótesis sin necesidad de desarrollar completamente.

- **Evaluación de usabilidad:** Test con usuarios reales realizando tareas concretas, medición del tiempo de realización, tasa de errores y satisfacción subjetiva. La evaluación heurística (inspección por expertos) complementa los tests con usuarios.

![UX - UI](./img/00/UX-UI.jpg)

**User Interface (UI)** responde a las preguntas: ¿Cómo se ve? ¿Es visualmente atractivo? ¿Comunica correctamente la jerarquía de la información? ¿Es consistente? ¿Guía al usuario adecuadamente? La UI se ocupa de la capa visual de la interfaz. Incluye disciplinas como:

- **Diseño visual:** Selección y aplicación de colores, tipografías, iconografía, ilustraciones, fotografías y texturas. Se rige por principios de teoría del color, jerarquía visual, contraste, equilibrio, ritmo y unidad.

- **Sistemas de diseño:** Creación de bibliotecas de componentes reutilizables y las reglas que los gobiernan, garantizando consistencia visual y funcional a lo largo de toda la aplicación.

- **Espaciado y layout:** Definición de retículas, márgenes, rellenos y sistemas de espaciado que aseguran respiración visual, agrupación lógica de elementos y fluidez de lectura.

- **Tipografía:** Selección de familias tipográficas, definición de escalas, establecimiento de jerarquías (títulos, subtítulos, cuerpo, notas). La tipografía es el vehículo principal de contenido textual y condiciona la legibilidad.

- **Microinteracciones:** Pequeños momentos de interacción que comunican estado, proporcionan feedback y aportan personalidad a la interfaz (un botón que cambia de color al pasar el cursor, un icono que gira al cargar contenido, una animación de confirmación al completar una acción).

**Diferencias clave y sinergias**

La metáfora más efectiva para distinguir UX y UI es la de un automóvil: la UX sería la experiencia completa de conducir (facilidad para girar el volante, visibilidad, comodidad del asiento, respuesta del motor), mientras que la UI sería el diseño del salpicadero (color de los diales, tipo de letra de los indicadores, disposición de los botones). Un coche puede tener un salpicadero precioso (UI excelente) pero ser incómodo de conducir (UX pésima). Y viceversa.

En la práctica profesional, no debe existir rivalidad sino colaboración. La UX define *qué* debe hacer la interfaz y en *qué orden*, mientras que la UI define *cómo* se presenta visualmente y *cómo* se siente cada interacción. Un diseñador UX que no tiene sensibilidad visual produce wireframes funcionales pero difíciles de interpretar. Un diseñador UI que no comprende usabilidad produce interfaces bellas pero frustrantes.

!!! tip "Consejo práctico"

    Para el alumnado de Desarrollo de Interfaces, es crucial comprender ambas disciplinas. Vuestro perfil profesional tiende al desarrollo frontend (más técnico), pero debéis ser capaces de leer y comprender las decisiones de diseño que os llegan desde UX/UI, y de colaborar activamente con estos perfiles durante el desarrollo.

### 4. Interfaces web y multiplataforma

El desarrollo de interfaces se enfrenta hoy a un problema fundamental: la **fragmentación de plataformas**. Una aplicación debe funcionar en navegadores de escritorio, navegadores móviles, potencialmente como aplicación nativa en iOS y Android, y quizás como aplicación de escritorio en Windows, macOS y Linux. Desarrollar y mantener versiones nativas separadas para cada plataforma es económicamente inviable para la mayoría de organizaciones.

**Aplicaciones web tradicionales**

Son aplicaciones que se ejecutan completamente dentro de un navegador web. No requieren instalación: el usuario accede mediante una URL. Las actualizaciones son transparentes (el servidor sirve la nueva versión). Sin embargo, tienen limitaciones: acceso restringido al hardware del dispositivo (no pueden acceder a todos los sensores, al sistema de archivos completo, etc.), dependencia de conexión a internet y rendimiento inferior a las aplicaciones nativas para tareas intensivas. Además, no tienen presencia en las tiendas de aplicaciones ni pueden aprovechar ciertos canales de distribución y monetización.

**Progressive Web Apps (PWA)**

Las PWA representan una evolución de las aplicaciones web que busca eliminar sus principales limitaciones. Mediante tres tecnologías clave ofrecen una experiencia casi nativa:

1. **Service Workers:** Scripts que se ejecutan en segundo plano, independientemente de la página web, y permiten funcionalidades como cacheo avanzado, funcionamiento offline, sincronización en segundo plano y notificaciones push.

2. **Web App Manifest:** Un archivo JSON que define cómo se mostrará la aplicación cuando se instale en el dispositivo del usuario (nombre, iconos, colores, orientación, modo de pantalla completa).

3. **HTTPS obligatorio:** Por seguridad, los service workers requieren conexión segura.

Las PWA pueden instalarse en la pantalla de inicio del dispositivo, funcionar sin conexión, recibir notificaciones push y acceder a varias APIs de hardware. Grandes empresas como Twitter (Twitter Lite), Starbucks, Uber o Pinterest han adoptado PWA con resultados notables en engagement y conversión.

**Aplicaciones híbridas**

Las aplicaciones híbridas se desarrollan con tecnologías web (HTML, CSS, JavaScript) pero se ejecutan dentro de un contenedor nativo que proporciona acceso a las APIs del dispositivo. Frameworks como Apache Cordova, Ionic y Capacitor son los más utilizados. La principal ventaja es compartir código entre plataformas; la principal desventaja es un rendimiento inferior a las aplicaciones nativas puras, especialmente en animaciones complejas o listas muy largas.

**Electron: aplicaciones de escritorio con tecnologías web**

Electron es un framework de código abierto desarrollado por GitHub que permite construir aplicaciones de escritorio multiplataforma utilizando tecnologías web (HTML, CSS, JavaScript) combinadas con Node.js. Su arquitectura se compone de dos tipos de procesos:

1. **Proceso principal (Main Process):** Un proceso Node.js que gestiona el ciclo de vida de la aplicación, crea ventanas del sistema operativo y tiene acceso completo a las APIs nativas (sistema de archivos, menús nativos, accesos directos de teclado, notificaciones del sistema, etc.).

2. **Procesos renderizadores (Renderer Processes):** Cada ventana de la aplicación ejecuta su propio proceso Chromium. Aquí se carga la interfaz web propiamente dicha: HTML, CSS y JavaScript. Por seguridad, los procesos renderizadores tienen acceso limitado a las APIs de Node.js (a menos que se configure explícitamente mediante preload scripts).

Electron utiliza Chromium (el motor de renderizado de Google Chrome) y Node.js, por lo que empaqueta una versión completa de ambos. Esto tiene dos implicaciones: las aplicaciones Electron ocupan un tamaño considerable (mínimo ~100 MB) y consumen más memoria RAM que una aplicación nativa equivalente, pero a cambio obtienen compatibilidad multiplataforma casi perfecta (Windows, macOS, Linux) y acceso completo a todo el ecosistema de librerías de Node.js y npm.

Aplicaciones emblemáticas construidas con Electron incluyen:

- **Visual Studio Code:** El editor de código más popular del mundo, desarrollado por Microsoft. Es un ejemplo de cómo Electron puede ofrecer una experiencia de escritorio de primer nivel si se optimiza adecuadamente.

- **Discord:** La plataforma de comunicación para comunidades, con millones de usuarios concurrentes.

- **Slack:** La herramienta de comunicación empresarial.

- **Figma:** La herramienta de diseño colaborativo que utilizaremos en este módulo.

- **Postman:** La plataforma de desarrollo de APIs.

- **Notion:** La herramienta de productividad y gestión de conocimiento.

Para el módulo de Desarrollo de Interfaces, Electron es relevante porque nos permite llevar nuestras interfaces construidas con Angular y Tailwind CSS al escritorio sin necesidad de aprender tecnologías completamente diferentes como C# con WPF o Swift con AppKit. La inversión en aprender a construir buenas interfaces web se multiplica al poder desplegarlas en web, móvil (mediante PWA o híbridas) y escritorio (mediante Electron).

### 5. Tendencias actuales en diseño de interfaces

El diseño de interfaces no es estático: evoluciona influenciado por las capacidades técnicas de los navegadores, los cambios culturales, las demandas de los usuarios y las modas estéticas. Conocer las tendencias actuales no significa aplicarlas todas indiscriminadamente, sino disponer de un repertorio amplio de recursos para elegir los más adecuados a cada proyecto.

**Neumorfismo (Neumorphism)**

Es una evolución del **skeuomorfismo** (imitación de texturas reales) que combina elementos del diseño plano con sombras suaves para crear la ilusión de que los elementos emergen o se hunden en el fondo. Se consigue mediante dos sombras: una clara en la parte superior izquierda y una oscura en la parte inferior derecha, sobre un fondo del mismo color. El efecto es plástico, táctil y suave. Sin embargo, presenta serios problemas de accesibilidad debido al bajo contraste, por lo que debe usarse con moderación y siempre complementado con indicadores visuales adicionales. Es adecuado para interfaces simples (calculadoras, reproductores de música), nunca para formularios complejos o dashboards con mucha información.

![Neumorfismo](./img/00/Neumorfismo.png)

**Glassmorfismo**

Efecto de vidrio esmerilado que difumina y tiñe el fondo detrás de un elemento, creando profundidad y jerarquía visual. Implementado en CSS mediante `backdrop-filter: blur()` y fondos semitransparentes, se popularizó con Windows Vista, desapareció con el diseño plano y ha resurgido con Windows 11 y macOS. Funciona bien para tarjetas, modales, barras de navegación y paneles superpuestos. En Tailwind CSS 4, se implementa mediante clases como `backdrop-blur-lg`, `bg-white/70` y `border border-white/20`.

![Glassmorfismo](./img/00/Glassmorfismo.jpeg)

**Minimalismo**

El minimalismo busca reducir la interfaz a sus elementos esenciales: amplio espacio en blanco, pocos colores, tipografía clara y eliminación de todo adorno superfluo. Es la tendencia dominante en productos de productividad (Notion, Linear, Things, Craft). 

![Minimalismo](./img/00/Minimalismo.avif)

**Brutalismo**
El brutalismo, por contraste, abraza una estética intencionadamente cruda: tipografía grande y sin adornos, colores planos y vibrantes, bordes duros y falta de sutileza. Ambas corrientes representan reacciones frente al exceso visual.

![Brutalismo](./img/00/Brutalismo.jpg)

**Dark Mode**

El modo oscuro invierte la paleta tradicional (texto oscuro sobre fondo claro) presentando texto claro sobre fondo oscuro. Sus ventajas incluyen: reducción de la fatiga visual en entornos de poca luz, ahorro de batería en pantallas OLED (los píxeles negros están apagados) y preferencia estética de muchos usuarios. La implementación técnica moderna se basa en variables CSS y la media query `prefers-color-scheme`, combinadas con un toggle manual. Un sistema de diseño profesional debe contemplar ambos modos desde el inicio, no como un añadido posterior.

![Drak Mode](./img/00/DarkMode.jpg)

**Microinteracciones**

Son momentos de interacción pequeños pero significativos que realizan tres funciones: comunicar estado (un switch que se desliza), proporcionar feedback (un botón que cambia de color al ser presionado) y ayudar a visualizar acciones (un elemento que se desvanece al ser eliminado). No son meramente decorativas: las microinteracciones mejoran la usabilidad reduciendo la incertidumbre del usuario y haciendo la interfaz más predecible y satisfactoria. El libro "Microinteractions" de Dan Saffer es la referencia canónica en este ámbito.

![Microinteracciones](./img/00/Microinteracciones.png)

**Motion Design**

El movimiento en las interfaces debe tener propósito: guiar la atención, comunicar relaciones espaciales, proporcionar feedback y añadir personalidad. Los **principios de Disney** adaptados a interfaces (squash and stretch, anticipation, staging, follow-through) ayudan a crear animaciones naturales y fluidas. A nivel técnico, CSS ofrece `transition` para cambios entre estados, `animation` con `@keyframes` para secuencias más complejas, y las modernas `view-timeline` y `scroll-driven-animations` para animaciones vinculadas al scroll. En Angular, las animaciones se definen en los metadatos del componente mediante las funciones del paquete `@angular/animations`.

![Motion Design](./img/00/MotionDesign.gif)

**Diseño inclusivo**

Va más allá de la accesibilidad técnica (**WCAG**). El diseño inclusivo busca crear productos que funcionen para la mayor diversidad posible de personas, independientemente de su edad, género, cultura, capacidad, idioma o contexto. Implica considerar situaciones como: uso con una sola mano, visión reducida por luz solar, daltonismo, dislexia, conexiones lentas, dispositivos antiguos, bajo alfabetismo digital, diferencias culturales en el significado de colores e iconos, etc. Microsoft ha sido pionera en esta filosofía con su Inclusive Design Toolkit.

![Diseño Inclusivo](./img/00/DiseñoInclusivo.png)

**IA en interfaces**

La inteligencia artificial está transformando el desarrollo de interfaces en múltiples frentes. Herramientas como v0.dev o Galileo AI generan interfaces completas a partir de descripciones textuales. GitHub Copilot y similares asisten en la escritura de código de interfaz. Del lado del usuario, las interfaces se vuelven adaptativas: pueden reorganizarse, priorizar contenido y sugerir acciones basándose en el comportamiento observado. Esto plantea preguntas sobre el rol futuro del desarrollador de interfaces (¿seguiremos escribiendo HTML y CSS manualmente dentro de cinco años?) que debéis considerar críticamente.

### 6. Ecosistema Angular

Angular es un framework de desarrollo de aplicaciones web de código abierto mantenido por Google y una amplia comunidad. A diferencia de bibliotecas como React (que se centra exclusivamente en la capa de vista), Angular es un **framework completo** (*batteries included*) que proporciona soluciones integradas para casi todas las necesidades del desarrollo frontend moderno: renderizado de vistas, enrutamiento, gestión de estado, comunicación HTTP, validación de formularios, internacionalización (i18n), animaciones y testing.

**Filosofía y posicionamiento**

Angular está diseñado para aplicaciones a gran escala (*enterprise-grade*). Su arquitectura modular, su sistema de tipos con TypeScript, su inyección de dependencias y sus herramientas integradas (Angular CLI) lo hacen especialmente adecuado para equipos grandes, proyectos de larga duración y aplicaciones con lógica de negocio compleja. Donde React ofrece flexibilidad a costa de más decisiones, Angular ofrece opinión y estructura a costa de menos libertad.

**Modelo de componentes**

Un componente en Angular es una clase TypeScript decorada con `@Component` que encapsula:
- Un template HTML que define la vista.
- Estilos CSS (con encapsulación por defecto mediante Shadow DOM emulado).
- Lógica de presentación (propiedades, métodos, manejadores de eventos).
- Metadatos (selector CSS, animaciones, proveedores de servicios).

Los componentes se organizan en módulos (NgModules) o, desde Angular 14, pueden ser **Standalone Components** (componentes autónomos que no requieren un módulo padre). Esta última opción, que utilizaremos en este módulo, simplifica la estructura del proyecto y lo acerca a la experiencia de React o Vue.


```typescript
@Component({
  selector: 'app-card',
  standalone: true,
  template: `
    <div class="rounded-lg bg-white p-6 shadow-md">
      <h3 class="text-lg font-bold">{{ title }}</h3>
      <p class="text-gray-600">{{ description }}</p>
    </div>
  `,
  styles: [],
})
export class CardComponent {
  @Input({ required: true }) title!: string;
  @Input() description = '';
}
```

**Enrutamiento**

Angular proporciona un sistema de enrutamiento integrado que permite la navegación entre vistas sin recarga completa de página, con soporte para carga perezosa (lazy loading) de módulos, **guards** que protegen rutas según condiciones (autenticación, roles), **resolvers** que precargan datos antes de activar una ruta, y paso de parámetros por URL, query string o estado de navegación.

**Servicios e inyección de dependencias**

La lógica de negocio, la comunicación con APIs, la gestión de estado compartido y la funcionalidad transversal se extraen de los componentes y se encapsulan en servicios. Estos servicios son clases TypeScript decoradas con `@Injectable` que Angular inyecta automáticamente en los componentes que las solicitan. Este patrón promueve la separación de responsabilidades, la reusabilidad y la testabilidad (los servicios pueden mockearse fácilmente en tests unitarios).

**Angular Signals**

Introducidos en Angular 16 y estabilizados en versiones posteriores, los **Signals** representan un nuevo modelo de reactividad en Angular. Un Signal es un envoltorio alrededor de un valor que notifica a los consumidores cuando cambia. A diferencia de RxJS (que sigue siendo compatible y recomendado para flujos asíncronos complejos), los Signals ofrecen una reactividad más simple y granular, con detección de cambios más eficiente. Se crean con `signal(valorInicial)`, se leen como función (`miSignal()`) y se actualizan con `set`, `update` o `mutate`. Los Signals son la dirección futura de Angular y deben dominarse.

**Angular Material y CDK**

**Angular Material** es la implementación oficial de Material Design de Google para Angular. Proporciona componentes de interfaz de alta calidad, accesibles y probados en batalla: botones, tarjetas, diálogos, tablas, menús, formularios y más. El **Component Dev Kit (CDK)**, por su parte, proporciona primitivas de comportamiento (arrastrar y soltar, overlay, scrolling virtual, clipboard, etc.) sin imponer un estilo visual, permitiendo crear componentes personalizados con interacciones complejas. Usaremos Angular Material en la segunda mitad del módulo, una vez dominemos la construcción de componentes desde cero con Tailwind CSS.

### 7. Diseño Centrado en el Usuario (UCD)

El **Diseño Centrado en el Usuario (User-Centered Design, UCD)** es una filosofía y un proceso de diseño que sitúa al usuario en el centro de todas las decisiones. No se trata de preguntarle al usuario qué quiere (Henry Ford dijo: "si hubiera preguntado a la gente qué querían, habrían dicho caballos más rápidos"), sino de comprender profundamente sus necesidades, comportamientos, contextos y limitaciones para diseñar soluciones que realmente funcionen para ellos. La **ISO 9241-210** define el estándar internacional para el UCD.

**Fases del proceso UCD**

1. **Investigación:** Antes de diseñar nada, se investiga quiénes son los usuarios, qué tareas necesitan realizar y en qué contexto. Técnicas: entrevistas en profundidad, observación contextual (acompañar al usuario en su entorno real), encuestas a gran escala, análisis de datos de uso, análisis de la competencia.

2. **Especificación de requisitos:** A partir de la investigación, se definen requisitos de usuario (historias de usuario, casos de uso) y requisitos del sistema. Quedan documentados lo que el producto debe hacer y por qué.

3. **Diseño:** Se generan soluciones de diseño que satisfacen los requisitos. Comienza con bocetos (baja fidelidad), evoluciona a wireframes y finalmente a prototipos interactivos de alta fidelidad.

4. **Evaluación:** Se somete el diseño a prueba con usuarios reales realizando tareas concretas. Se mide efectividad (¿pueden completar la tarea?), eficiencia (¿cuánto tardan?) y satisfacción (¿cómo se sienten?). Los problemas encontrados se registran y priorizan por gravedad.

5. **Iteración:** Los resultados de la evaluación informan modificaciones en el diseño. Este ciclo construir-medir-aprender se repite hasta alcanzar los objetivos de usabilidad definidos.

**Herramientas del UCD**

- **Personas:** Arquetipos ficticios pero basados en datos reales de investigación que representan grupos de usuarios. Una persona incluye nombre, foto, datos demográficos, objetivos, frustraciones, comportamientos y una cita representativa. Las personas humanizan los datos y ayudan al equipo a empatizar con los usuarios reales.

- **Escenarios:** Narraciones breves que describen cómo una persona utilizaría el producto en una situación concreta para lograr un objetivo específico. Por ejemplo: "María, profesora de secundaria de 42 años, necesita preparar el informe trimestral de calificaciones de sus 120 alumnos. Tras una larga jornada, enciende su portátil en casa a las 21:00..."

- **Mapas de empatía:** Diagramas que capturan lo que el usuario piensa, siente, ve, dice, hace y escucha en relación con el producto o el problema. Ayudan a desarrollar una comprensión más profunda y matizada que los meros datos demográficos.

- **Customer Journey Maps:** Visualizaciones del recorrido completo del usuario desde que descubre el producto hasta que alcanza su objetivo (y más allá), incluyendo todos los puntos de contacto, emociones, puntos de dolor y oportunidades de mejora en cada etapa.

!!! info "Dato clave"

    El UCD no es un añadido opcional ni un lujo. Los estudios demuestran consistentemente que la corrección de un problema de usabilidad detectado durante el desarrollo cuesta **10 veces** más que si se detecta durante el diseño, y **100 veces** más que si se detecta después del lanzamiento. ==Invertir en UCD es una de las decisiones más rentables en desarrollo de software.==

### 8. El rol del desarrollador de interfaces en equipos modernos

El **desarrollador de interfaces** (o **frontend developer**) ocupa una posición estratégica en los equipos de desarrollo de productos digitales. Es el profesional responsable de implementar la capa de presentación, aquella con la que los usuarios interactúan directamente. Su trabajo conecta el diseño (UX/UI) con la ingeniería (backend, infraestructura), y debe dominar tanto los aspectos técnicos como tener sensibilidad para el diseño y la experiencia de usuario.

**Competencias técnicas esenciales**

- **HTML5 semántico** y accesible (ARIA, landmarks, roles).
- **CSS3 avanzado**: Flexbox, Grid, animaciones, variables, responsive design con media queries y container queries.
- **JavaScript y TypeScript** (tipos, interfaces, genéricos, programación funcional y reactiva).
- Al menos un framework/librería principal (Angular en nuestro caso, pero también React, Vue, Svelte).
- **Control de versiones** con Git y plataformas como GitHub o GitLab.
- **Testing**: unitario (Karma/Jasmine en Angular), de componentes (Testing Library), de integración, end-to-end (Cypress, Playwright).
- **Herramientas de build**: Webpack, Vite, esbuild.
- **Principios de rendimiento**: lazy loading, code splitting, optimización de imágenes, métricas Core Web Vitals.

**Competencias transversales**

- **Comunicación efectiva**: explicar decisiones técnicas a diseñadores, traducir requisitos de diseño en especificaciones técnicas, argumentar sobre viabilidad.
- **Colaboración multidisciplinar**: trabajar en equipo con diseñadores, product managers, desarrolladores backend, especialistas en QA y DevOps.
- **Resolución de problemas y pensamiento crítico**: capacidad para analizar problemas, descomponerlos y diseñar soluciones.
- **Aprendizaje continuo**: la tecnología frontend evoluciona más rápido que cualquier otra área del desarrollo. La capacidad de aprender de forma autónoma no es negociable.

**Colaboración con otros perfiles**

- **Diseñador UX:** Recibe wireframes, flujos de usuario, prototipos y especificaciones de interacción.
- **Diseñador UI:** Recibe los diseños finales en Figma (o herramienta equivalente), con especificaciones de color, tipografía, espaciado y assets.
- **Product Manager:** Recibe los requisitos funcionales, las historias de usuario y las prioridades del backlog.
- **Desarrollador backend:** Acuerda los contratos de API (endpoints, formatos de datos, códigos de estado), negocia qué lógica reside en el frontend y cuál en el backend.
- **QA / Tester:** Recibe reportes de bugs, participa en la definición de criterios de aceptación, colabora en tests automatizados.
- **DevOps:** Configuración de pipelines CI/CD, despliegue, monitorización de errores en producción.

**El módulo en el contexto del ciclo DAM**

El módulo de Desarrollo de Interfaces se imparte en el segundo curso del Ciclo Formativo de Grado Superior en Desarrollo de Aplicaciones Multiplataforma. Tiene una carga distribuidas en 6 horas semanales. Se relaciona estrechamente con otros módulos:

- **Lenguajes de marcas y sistemas de gestión de información:** Proporciona los fundamentos de HTML, CSS y maquetación web sobre los que este módulo construye interfaces. Mientras ese módulo se centra en el marcado y el estilo, Desarrollo de Interfaces se centra en la implementación con Angular y en la integración con herramientas profesionales como Figma, Tailwind y Storybook.
- **Programación:** Proporciona las bases de TypeScript y patrones de diseño.
- **Programación Multimedia y Dispositivos Móviles (PMDM):** Comparte el interés por las interfaces de usuario, pero desde la perspectiva de aplicaciones móviles nativas o híbridas.
- **Acceso a Datos:** Proporciona las APIs REST y GraphQL que consumiremos desde nuestras interfaces Angular.
- **Sistemas de Gestión Empresarial (SGE):** Las interfaces que desarrollemos deben integrarse en sistemas empresariales completos.

!!! example "Casos reales"

    ### Caso 1: La transformación digital de Genially

    **Genially**, empresa cordobesa fundada en 2015, desarrolla una plataforma web para crear contenidos interactivos y presentaciones. Con más de 30 millones de usuarios en 190 países, es uno de los casos de éxito más notables del ecosistema tecnológico andaluz. Su stack tecnológico ha evolucionado desde una aplicación PHP + jQuery hasta una arquitectura moderna basada en React + TypeScript, con un sistema de diseño propio documentado en **Storybook** y diseños gestionados en Figma.

    Para un desarrollador de interfaces, Genially ejemplifica los desafíos de escalar una interfaz web: miles de plantillas con editores drag-and-drop, renderizado en tiempo real de animaciones complejas, exportación a múltiples formatos (HTML, PDF, SCORM), colaboración en tiempo real entre múltiples usuarios (similar a Figma o Google Docs). Su equipo de frontend aplica rigurosos principios de accesibilidad **WCAG 2.1 AA** y performance (LCP < 2.5s, TBT < 300ms en dispositivos de gama media).

    ### Caso 2: La interfaz de administración de una cooperativa agrícola

    Imaginemos una cooperativa de aceite de oliva en Jaén que necesita digitalizar su gestión. Requieren una interfaz para control de producción (entrada de aceituna, rendimiento, trazabilidad), gestión de almacén, facturación y relaciones con agricultores. Los usuarios tienen entre 40 y 65 años, con baja alfabetización digital, y trabajarán con tablets en entornos con polvo, poca luz y conexión intermitente (zonas rurales de sierra).

    Este caso ilustra la aplicación de los principios vistos en la unidad:

    - **UCD:** Realizamos entrevistas con los agricultores en sus almazaras, observamos su jornada laboral para entender sus flujos reales.

    - **Diseño inclusivo:** Tipografía legible a 1.5-2 metros, targets táctiles de mínimo 48x48px, alto contraste, modo offline (PWA con service workers), interfaces simplificadas con solo las opciones esenciales, lenguaje en español llano sin tecnicismos.

    - **Elección tecnológica:** Aplicación web (accesible desde cualquier dispositivo sin instalación) pero con funcionalidad PWA para offline. Angular proporciona la estructura robusta que una aplicación de gestión necesita. Tailwind garantiza consistencia visual. Electron permite distribuir una versión de escritorio para los ordenadores de oficina.

## Ejemplos guiados

### Ejemplo guiado 1: Análisis UX/UI de Spotify

**Objetivo:** Identificar patrones de diseño UX/UI en una aplicación real de gran escala.

**Desarrollo en el aula:**

1. Abrimos Spotify (versión de escritorio) y navegamos por sus secciones principales: Inicio, Buscar, Tu Biblioteca.

![Spotify](./img/00/spotify.png)

2. **Análisis UX:**
   - **Navegación principal:** Menú lateral siempre visible con las secciones principales. Patrón de navegación persistente que reduce la carga cognitiva: el usuario siempre sabe dónde está y cómo ir a otra sección.
   - **Arquitectura de la información:** Jerarquía clara de tres niveles: secciones principales (Inicio, Buscar, Biblioteca) > subsecciones (Playlists, Podcasts, Artistas) > contenido detallado (una playlist concreta, un álbum).
   - **Búsqueda:** Búsqueda predictiva con sugerencias mientras se escribe. Muestra resultados por categorías (artistas, canciones, álbumes, playlists, podcasts) reduciendo el tiempo para encontrar contenido.
   - **Reproductor persistente:** Barra inferior siempre visible que muestra la canción actual, controles y progreso. El usuario puede interactuar con la reproducción en cualquier momento sin perder el contexto de navegación.

3. **Análisis UI:**
   - **Paleta de colores:** Modo oscuro con negro profundo (`#121212`) como base, verde característico (`#1DB954`) como color de acento y escalas de grises para jerarquía de texto.
   - **Tipografía:** Circular (tipografía propietaria de Spotify), con variantes Bold para títulos, Book para cuerpo y diferentes tamaños claramente jerarquizados.
   - **Cards:** Tarjetas cuadradas con imagen, título y descripción. Implementadas con hover effects (escala, sombra, botón de reproducción) que proporcionan feedback y affordance claro.
   - **Consistencia:** Todas las pantallas comparten el mismo lenguaje visual (idénticos espaciados, mismas tipografías, mismos efectos hover).

4. **Identificación de patrones técnicos:**
   - Scroll infinito con lazy loading en listas largas (optimización de rendimiento).
   - Skeleton screens durante la carga (mejor experiencia que un spinner genérico).
   - Transiciones suaves entre páginas (animaciones de navegación).
   - Borrosidad en fondos de cabeceras (glassmorphism).

5. **Discusión:** ¿Qué tecnologías utilizarían para implementar esta interfaz? Angular para la estructura SPA y los componentes, Tailwind CSS para los estilos, RxJS para los datos en tiempo real (streaming de reproducción).

### Ejemplo guiado 2: Descomposición de una pantalla con Atomic Design

<!-- **Objetivo:** Aprender a descomponer visualmente una interfaz en componentes siguiendo la metodología Atomic Design (Brad Frost).

**Metodología:** Tomamos una captura de pantalla de la interfaz de Linear (herramienta de gestión de proyectos) y la descomponemos en átomos, moléculas y organismos.

**Paso 1 - Definición de niveles de Atomic Design:**

- **Átomos:** Elementos más pequeños irreductibles (botones, inputs, labels, iconos, avatars, badges, checkboxes individuales).

- **Moléculas:** Combinaciones simples de átomos que funcionan juntos (un campo de búsqueda = input + icono + botón; un elemento de menú = icono + label + badge; un filter chip = label + icono de cierre).

- **Organismos:** Grupos de moléculas y átomos que forman secciones distintas de la interfaz (un sidebar completo, una cabecera, una tabla con filtros, un panel de comentarios).

- **Templates:** Composición de organismos que forma la estructura de una página (aún con contenido placeholder).

- **Pages:** Templates con contenido real.

**Paso 2 - Descomposición práctica:**

En la pantalla de Linear identificamos:

- **Átomos:** Button, IconButton, Avatar, Badge (indicador de prioridad: alta/urgente/media/baja), Label, Input, Select, Checkbox, Divider.

- **Moléculas:**
    - `IssueRow`: combina checkbox + badge de prioridad + ID de issue + título + labels (múltiples) + assignee avatar + fecha relativa.
    - `FilterBar`: combina múltiples FilterChips + botón Add Filter + SearchInput.
    - `StatusColumn`: combina título de columna + contador de issues + botón Add + lista de IssueRow.

- **Organismos:**
    - `BoardView`: combina StatusColumn × N, con scroll horizontal y botón Add Column.
    - `Sidebar`: combina Logo + NavigationMenu + workspace switcher + UserMenu.
    - `TopBar`: combina breadcrumb + actions (Share, Filter toggle, View options).
    - `IssueDetail`: panel lateral que combina título editable, descripción (editor), propiedades (status, priority, assignee, labels, due date), actividad (timeline de comentarios y cambios).

- **Template:** `ProjectBoard` = TopBar + Sidebar + BoardView.

**Paso 3 - Traslación a Angular y Tailwind:**

Para cada nivel, identificamos qué será un componente Angular:

- Átomos como `app-button`, `app-badge`, `app-avatar` → Componentes standalone en `shared/ui/`.
- Moléculas como `app-issue-row`, `app-filter-bar` → Componentes standalone en `shared/components/` o directamente en los feature modules.
- Organismos como `app-sidebar`, `app-board-view` → Componentes de feature (posiblemente lazy-loaded).

Cada componente utilizará Tailwind CSS para los estilos, manteniendo consistencia con variables de diseño (design tokens) extraídas del sistema de diseño.

**Discusión:** Este ejercicio conecta directamente con la Unidad 4 (Figma, donde diseñamos componentes) y la Unidad 15 (del diseño a la implementación, donde convertimos estos componentes de Figma a Angular). -->


## Actividades guiadas

### Actividad guiada 1: Análisis de tipos de interfaces

**Desarrollo:** Analiza las 6 imágenes/situaciones diferentes de interfaces:

<!-- 1. Una terminal de Linux con comandos `grep`, `awk` y `|` (CLI).

2. La pantalla de inicio de Windows 11 (GUI).

3. Un usuario dando órdenes a Alexa: "Alexa, añade leche a la lista de la compra" (VUI).

4. Una persona usando gestos en un Microsoft HoloLens para manipular un holograma 3D (NUI).

5. Un DJ manipulando un controlador MIDI físico (TUI).

6. ChatGPT respondiendo preguntas en lenguaje natural (interfaz conversacional). -->

### Interfaz 1
![Imagen 1](./img/00/terminal.jpg)

### Interfaz 2
![Imagen 2](./img/00/windows11.jpg)

### Interfaz 3
![Imagen 3](./img/00/alexa.webp)

### Interfaz 4
![Imagen 4](./img/00/hololens.jpeg)

### Interfaz 5
![Imagen 5](./img/00/DjMidi.jpeg)

### Interfaz 6
![Imagen 6](./img/00/chatgpt.webp)








El alumnado, organizado en parejas, debe para cada imagen: identificar el tipo de interfaz, enumerar las tecnologías involucradas (dispositivos de entrada/salida, software), describir un contexto donde ese tipo de interfaz es preferible a las demás y argumentar por qué.

Puesta en común y debate sobre la convivencia de múltiples tipos de interfaces.

### Actividad guiada 2: Línea del tiempo de la evolución de interfaces
<!-- 

**Desarrollo:** El docente proporciona 10 tarjetas desordenadas con hitos de la evolución de interfaces (Xerox Alto 1973, Macintosh 1984, Windows 95, Gmail AJAX 2004, iPhone 2007, Diseño Responsive 2010, Google Material Design 2014, Oculus Rift CV1 2016, Figma 2016, ChatGPT 2022). En grupos de 3-4 personas, deben ordenarlas cronológicamente y para cada hito explicar por qué fue relevante: ¿qué novedad introdujo? ¿Qué problema resolvió?

Corrección colaborativa: cada grupo expone su cronología. El docente corrige errores y profundiza en los hitos clave. -->

### Actividad guiada 3: Persona y escenario

<!-- 
**Desarrollo:** Cada grupo de 3-4 alumnos recibe datos de investigación sobre usuarios de una aplicación de gestión de tareas (datos demográficos, respuestas a encuestas, citas literales de entrevistas). A partir de esos datos, deben construir una persona siguiendo la plantilla proporcionada:

```
Nombre ficticio: _____
Edad: _____ Ocupación: _____
Contexto de uso: _____
Objetivos principales: (1) _____ (2) _____ (3) _____
Frustraciones principales: (1) _____ (2) _____ (3) _____
Comportamientos observados: _____
Cita representativa: "_____"
```

A continuación, deben escribir un escenario de 150 palabras describiendo cómo esa persona utilizaría la app en una situación concreta: ¿Dónde está? ¿Qué hora es? ¿Qué dispositivo usa? ¿Qué quiere conseguir? ¿Qué emociones experimenta durante el proceso?

Cada grupo presenta su persona y escenario. El resto valora si los datos de investigación justifican realmente ese perfil o si se han proyectado sesgos. -->

## Actividades propuestas

### Actividad 1

**Objetivo:** Identificar y clasificar interfaces de usuario en el entorno cotidiano.
<!-- 

**Enunciado:** Durante una semana, documenta cada interfaz con la que interactúes (despertador, microondas, cajero automático, app del banco, redes sociales, GPS del coche, etc.). Crea una tabla con las siguientes columnas: Dispositivo, Tipo de interfaz (GUI/CLI/VUI/NUI/TUI/Otro), Dispositivo de entrada, Dispositivo de salida, Tecnología subyacente (si la conoces), Valoración personal (1-5). Debes documentar al menos 15 interfaces diferentes.

**Requisitos:** Incluir al menos un ejemplo de cada tipo de interfaz (GUI, CLI, VUI, NUI, TUI). Justificar la clasificación elegida.

**Pistas:** Fíjate en interfaces no obvias: el lector de huellas dactilares del móvil (¿qué tipo es?), el asistente de aparcamiento del coche, el panel táctil de una impresora, la pulsera de actividad.

**Criterios de evaluación:** (1) Correcta identificación de los tipos de interfaz. (2) Diversidad y originalidad de los ejemplos. (3) Calidad de las justificaciones. -->

### Actividad 2


**Objetivo:** Analizar la UX y UI de dos aplicaciones competidoras.

<!-- **Enunciado:** Elige dos aplicaciones que compitan directamente (por ejemplo, Spotify vs Apple Music, Notion vs Obsidian, Todoist vs TickTick, Netflix vs HBO Max). Realiza un análisis comparativo estructurado que incluya: comparación de la navegación principal, arquitectura de la información, paleta de colores y tipografía, jerarquía visual de la pantalla principal, tiempos para completar 3 tareas comunes (cronometrados), 3 puntos fuertes y 3 puntos débiles de UX de cada una, 3 puntos fuertes y 3 puntos débiles de UI de cada una. Concluye con tu recomendación personal justificada.

**Requisitos:** Incluir capturas de pantalla anotadas con flechas y comentarios señalando los elementos analizados. Documentar las 3 tareas cronometradas con capturas de cada paso.

**Pistas:** Las DevTools del navegador (F12) son tus aliadas para inspeccionar tipografías, colores exactos, espaciados y estructura del DOM. Usa la herramienta de captura de pantalla completa para documentar.

**Criterios de evaluación:** (1) Profundidad del análisis UX (no solo descripción superficial). (2) Precisión del análisis UI (identificación de colores, tipografías, espaciado). (3) Objetividad en la comparación (argumentos, no gustos personales). -->

### Actividad 3


**Objetivo:** Realizar un análisis de accesibilidad básico.
<!-- 
**Enunciado:** Selecciona una página web de un servicio público andaluz (Junta de Andalucía, Salud Responde, cita previa de salud, etc.). Realiza una auditoría de accesibilidad básica utilizando: (1) La extensión WAVE o axe DevTools, (2) Navegación completa solo con teclado (Tab, Shift+Tab, Enter, Escape), (3) Simulación de daltonismo usando las DevTools de Chrome (Rendering > Emulate vision deficiencies), (4) Aumento de zoom al 200% para comprobar que no se rompe el layout. Documenta todos los problemas encontrados con capturas y sugiere soluciones concretas para cada uno.

**Requisitos:** Documentar al menos 5 problemas de accesibilidad. Para cada uno: descripción, criterio WCAG vulnerado (investiga la numeración correcta), gravedad (crítica/seria/moderada/leve), captura y solución propuesta en lenguaje técnico (código HTML/CSS específico).

**Pistas:** Foco visible al navegar con teclado, contraste de color suficiente (ratio mínimo 4.5:1 para texto normal, 3:1 para texto grande), etiquetas en formularios, textos alternativos en imágenes, landmarks ARIA.

**Criterios de evaluación:** (1) Uso correcto de las herramientas de auditoría. (2) Precisión en la identificación de criterios WCAG. (3) Viabilidad técnica de las soluciones propuestas. -->

### Actividad 4


**Objetivo:** Investigar el ecosistema Angular y preparar una presentación técnica breve.
<!-- 
**Enunciado:** Investiga y prepara una presentación de 7-8 diapositivas sobre una de las siguientes características de Angular: (a) Signals y su impacto en la detección de cambios, (b) Standalone Components y la evolución desde NgModules, (c) Angular Material 3 y Material Design 3, (d) RxJS y la programación reactiva en Angular, (e) Angular Universal y el Server-Side Rendering. La presentación debe explicar el concepto, mostrar código de ejemplo (con comentarios explicativos), comparar con la alternativa anterior (si aplica), y exponer ventajas y casos de uso recomendados.

**Requisitos:** Incluir fragmentos de código funcionales en la presentación. Citar fuentes oficiales (angular.dev). La presentación debe ser comprensible para compañeros sin conocimiento previo de Angular.

**Pistas:** La documentación oficial de Angular (angular.dev) es la mejor fuente. Usa el playground de StackBlitz para crear ejemplos interactivos que puedas mostrar.

**Criterios de evaluación:** (1) Corrección técnica de los conceptos explicados. (2) Claridad didáctica (¿lo entenderían tus compañeros?). (3) Calidad de los ejemplos de código. -->

### Actividad 5



**Objetivo:** Aplicar el proceso UCD a un problema real del instituto.
<!-- 
**Enunciado:** Aplica el proceso de Diseño Centrado en el Usuario para proponer una mejora a un sistema o proceso del instituto que involucre una interfaz digital (por ejemplo: la plataforma Moodle del centro, el sistema de reserva de aulas, el proceso de matrícula online, la app del instituto si existe, etc.). Realiza las siguientes fases documentadas: (1) Entrevista a 3 usuarios reales (compañeros, profesores, personal administrativo) con un guion de al menos 10 preguntas, (2) Crea 2 personas basadas en los datos recogidos, (3) Dibuja un mapa de empatía para una de ellas, (4) Identifica 3 problemas principales y propón soluciones de diseño (wireframes a mano o en Figma). Entrega un informe de 4-6 páginas documentando todo el proceso.

**Requisitos:** Adjuntar evidencias de las entrevistas (fotos de las notas, grabaciones de audio con consentimiento, o transcripciones). Los wireframes deben ser comprensibles.

**Pistas:** Prepara un consentimiento informado simple para los entrevistados explicando que es para un trabajo de clase. Empieza con preguntas abiertas ("cuéntame tu experiencia con...") y luego profundiza en los puntos concretos.

**Criterios de evaluación:** (1) Rigor en la aplicación de las técnicas UCD. (2) Calidad de las personas (basadas en datos, no en suposiciones). (3) Pertinencia y creatividad de las soluciones propuestas. -->

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Análisis de interfaces de videojuegos

    <!-- Los videojuegos representan un laboratorio de interfaces de usuario extremadamente rico y diverso. Elige un videojuego que conozcas bien y analiza su interfaz siguiendo este esquema: (1) Tipos de interfaz que combina (GUI para el HUD, NUI para los controles, posiblemente VUI en juegos con comandos de voz). (2) Elementos del HUD: analiza cada elemento (barra de vida, minimapa, inventario, indicadores de misión) explicando qué información comunica y por qué es necesaria para la experiencia de juego. (3) Diegética vs no diegética: clasifica los elementos de interfaz según estén dentro del mundo del juego (diegéticos, como la interfaz del traje en Dead Space) o fuera de él (no diegéticos, como la barra de vida en pantalla). (4) Microinteracciones y feedback: analiza cómo el juego comunica acciones al jugador (animaciones de daño, sonidos de recogida de objetos, vibración del mando). (5) Accesibilidad: investiga las opciones de accesibilidad del juego y relaciónalas con los principios WCAG adaptados a videojuegos. Entrega un informe en formato presentación (PDF) de 10-15 diapositivas con abundantes capturas. -->

    ### Actividad de ampliación 2: Mini-investigación sobre TUI en el Internet of Things

    <!-- El Internet of Things (IoT) y las interfaces tangibles (TUI) están transformando la forma de interactuar con objetos cotidianos. Realiza una investigación documental sobre aplicaciones reales de TUI en IoT. Identifica y describe en detalle 3 productos o prototipos que utilicen TUI en contextos de IoT (por ejemplo: termostatos inteligentes con diales físicos que modifican parámetros digitales, lámparas inteligentes que cambian de color al girarlas físicamente, altavoces inteligentes con paneles táctiles, etc.). Para cada uno: describe la interacción, explica qué tecnologías la hacen posible (sensores, actuadores, protocolos de comunicación), e identifica ventajas de la TUI frente a una GUI tradicional para ese contexto. Concluye reflexionando sobre el futuro de las TUI en el hogar inteligente. Formato: artículo de blog de 1200-1500 palabras con imágenes y referencias. -->

    ### Actividad de ampliación 3: Debate sobre el impacto de la IA en el desarrollo de interfaces

    <!-- La inteligencia artificial generativa (ChatGPT, GitHub Copilot, v0.dev, Midjourney) está transformando el desarrollo de software y el diseño de interfaces. Algunos expertos predicen que los desarrolladores frontend y diseñadores UI serán reemplazados por IA en los próximos 5-10 años. Otros argumentan que la IA será una herramienta que aumentará la productividad pero no reemplazará a los profesionales humanos. Investiga argumentos de ambos lados (al menos 5 fuentes contrastadas, incluyendo artículos académicos, informes de la industria y opiniones de expertos reconocidos) y escribe un ensayo argumentativo de 1500-2000 palabras donde expongas el estado de la cuestión, los argumentos a favor y en contra, y finalmente tu posición personal razonada sobre cómo crees que evolucionará la profesión de desarrollador de interfaces en los próximos 10 años. Incluye una sección específica sobre las competencias que consideras que serán más valiosas en ese futuro escenario y cómo te estás preparando (o deberías prepararte) para ello. -->

!!! tip "Buenas prácticas"

    1. **Diseña para el usuario, no para ti mismo.** El desarrollador de interfaces no es el usuario. Tus preferencias estéticas, tu familiaridad con la tecnología y tu contexto de uso son radicalmente diferentes a los de la mayoría de usuarios. Valida siempre con usuarios reales.

    2. **Comienza siempre con un análisis, nunca con el código.** Antes de abrir VS Code, debes tener claro: ¿quién usará esto? ¿qué tarea necesita completar? ¿en qué contexto? ¿qué dispositivos usará? Documenta estas respuestas, aunque sean breves, antes de implementar.

    3. **Mantén la consistencia como principio fundamental.** Cada decisión de diseño (color, tipografía, espaciado, nomenclatura, interacción) debe ser consistente a lo largo de toda la aplicación. Las inconsistencias generan confusión, aumentan la carga cognitiva y transmiten falta de profesionalidad.

    4. **No confundas tendencia con buena práctica.** Que algo esté de moda (neumorfismo, animaciones excesivas, scroll hijacking) no significa que sea beneficioso para el usuario. Evalúa cada tendencia críticamente: ¿mejora la usabilidad? ¿Reduce la carga cognitiva? ¿Funciona para todos los usuarios?

    5. **Involucra a los usuarios durante todo el proceso.** El UCD no consiste en preguntar al inicio y olvidarse. Cada iteración de diseño debe validarse con usuarios. Cuanto antes detectes un problema, más barato será solucionarlo.

    6. **Piensa en accesibilidad desde el minuto cero.** La accesibilidad no es un checklist que se revisa al final del proyecto. Integrarla desde el diseño evita costosos rediseños y amplía tu base de usuarios (el 15% de la población mundial tiene alguna discapacidad). Además, muchas mejoras de accesibilidad benefician a todos los usuarios (subtítulos en entornos ruidosos, alto contraste bajo luz solar, navegación por teclado cuando falla el ratón).

    7. **Documenta tus decisiones de diseño.** Las decisiones de UX/UI no deben ser arbitrarias. Mantén un registro (puede ser un simple documento o un archivo Figma) donde expliques por qué elegiste ciertos colores, por qué estructuraste la navegación de esa manera, por qué priorizaste ciertas funcionalidades. Esto facilita la incorporación de nuevos miembros al equipo y la toma de decisiones futuras.

    8. **Aprende a leer código ajeno y a trabajar con código heredado.** En tu carrera profesional, pasarás mucho más tiempo leyendo, modificando y manteniendo código existente que escribiendo código desde cero. Acostúmbrate a analizar interfaces existentes y a entender por qué se implementaron de cierta manera, incluso si hoy harías algo diferente.

!!! warning "Errores frecuentes"

    1. **Creer que UX y UI son lo mismo.** Es el error conceptual más común entre principiantes. UX es investigación, arquitectura y flujos; UI es color, tipografía y pixel-perfect. Ambas son necesarias, pero no son lo mismo. Si estás haciendo un diseño bonito en Figma, estás haciendo UI, no UX.

    2. **Ignorar al usuario y diseñar para uno mismo.** "A mí me parece intuitivo" es una frase peligrosa. Tú conoces el sistema porque lo has diseñado; el usuario llega sin ese conocimiento previo. Lo que es obvio para ti puede ser completamente opaco para un usuario real.

    3. **Empezar a programar sin tener un diseño (ni siquiera un boceto).** Síndrome del "ya iré viendo sobre la marcha". Resultado: interfaces inconsistentes, decisiones de diseño tomadas sobre la marcha sin criterio, pérdida de tiempo refactorizando, insatisfacción del usuario.

    4. **Subestimar las interfaces de línea de comandos como "cosa del pasado".** Las CLI son más rápidas, más automatizables y más eficientes en muchos contextos profesionales. Un desarrollador competente debe sentirse cómodo en la terminal.

    5. **Aplicar tendencias de diseño sin criterio.** El neumorfismo es bonito pero inaccesible. El glassmorphism es elegante pero puede afectar al rendimiento (backdrop-filter es costoso). No uses una tendencia porque sí; úsala cuando resuelva un problema concreto de tu interfaz.

    6. **No diferenciar entre aplicaciones nativas, web apps y PWA.** Elegir la tecnología incorrecta para el contexto de uso puede condenar un proyecto: una aplicación que necesita funcionar en zonas sin cobertura no puede ser una web app tradicional; una aplicación que necesita acceso a Bluetooth no puede ser una PWA básica.

    7. **Confundir "minimalismo" con "eliminar funcionalidades útiles".** El minimalismo bien entendido elimina elementos visuales superfluos, no funcionalidades necesarias. Ocultar funciones en menús de hamburguesa o gestos secretos para mantener una interfaz "limpia" suele perjudicar la usabilidad (lo que Jakob Nielsen llamó "minimalismo extremo").

    8. **Olvidar que las interfaces las usan personas reales con contextos reales.** Es fácil diseñar en un monitor 4K de 27 pulgadas, con fibra óptica simétrica y en una habitación silenciosa. Pero tu usuario puede estar consultando tu aplicación en un móvil de gama media, con luz solar directa sobre la pantalla, conectado por 4G con una cobertura justa y con una mano mientras sujeta una bolsa de la compra con la otra. Diseña para ese usuario, no para tu setup de desarrollo.

!!! abstract "Resumen"

    Esta unidad ha establecido los cimientos conceptuales sobre los que construiremos todo el módulo. Hemos definido qué es una interfaz de usuario y clasificado sus tipos (GUI, CLI, VUI, NUI, TUI), recorrido la fascinante evolución de las interfaces desde la línea de comandos hasta la IA conversacional, y delimitado claramente las disciplinas de UX y UI, que a menudo se confunden pero responden a preguntas fundamentalmente diferentes.

    Hemos explorado el panorama de las interfaces web y multiplataforma, con especial atención a las **PWA** como puente entre web y nativo, y a **Electron** como tecnología clave para llevar nuestras habilidades web al escritorio. Las tendencias actuales —neumorfismo, glassmorphism, modo oscuro, microinteracciones, diseño inclusivo— nos proporcionan un vocabulario visual amplio, pero deben aplicarse con criterio, situando siempre las necesidades del usuario por encima de la moda.

    Hemos situado a Angular en el ecosistema de desarrollo de interfaces: un **framework completo**, enterprise-grade, que nos acompañará durante todo el módulo como herramienta principal de implementación. Su modelo de componentes, su sistema de enrutamiento, sus servicios inyectables y sus Signals conformarán nuestro arsenal técnico.

    El Diseño Centrado en el Usuario nos ha proporcionado un marco metodológico riguroso para no perder nunca de vista al destinatario final de nuestro trabajo: investigar, diseñar, prototipar, testear e iterar. Personas, escenarios, mapas de empatía y tests de usabilidad son herramientas concretas para aplicar este enfoque.

    Finalmente, hemos reflexionado sobre nuestro futuro rol profesional como desarrolladores de interfaces, identificando las competencias técnicas y transversales necesarias y cómo este módulo se integra con el resto del currículo DAM.

    En las siguientes unidades pasaremos de la teoría a la práctica: configuraremos nuestro entorno de desarrollo, dominaremos Figma para el diseño de interfaces, construiremos layouts profesionales con Tailwind CSS y CSS Grid, y recorreremos el camino completo desde un diseño en Figma hasta una aplicación funcional en Angular.

## Recursos complementarios

### Libros y referencias académicas

- Norman, D. (2013). *The Design of Everyday Things*. Basic Books. La obra fundacional sobre diseño centrado en el usuario y affordances. Lectura obligatoria para cualquier profesional de interfaces.

- Krug, S. (2014). *Don't Make Me Think, Revisited: A Common Sense Approach to Web Usability*. New Riders. La introducción más accesible a la usabilidad web. Corto, práctico y lleno de ejemplos.

- Saffer, D. (2013). *Microinteractions: Designing with Details*. O'Reilly Media. La referencia sobre microinteracciones: qué son, por qué importan y cómo diseñarlas.

- Frost, B. (2016). *Atomic Design*. Disponible gratuitamente en atomicdesign.bradfrost.com. La metodología que utilizaremos para estructurar nuestros componentes.

- Gothelf, J. y Seiden, J. (2021). *Lean UX: Designing Great Products with Agile Teams*. O'Reilly Media. Cómo integrar UX en equipos ágiles.

### Recursos web

- **Angular Official Documentation:** [https://angular.dev](https://angular.dev). La documentación oficial, renovada y accesible con tutoriales interactivos.

- **Tailwind CSS Documentation:** [https://tailwindcss.com](https://tailwindcss.com). Documentación exhaustiva con ejemplos y guías de configuración.

- **MDN Web Docs (Mozilla):** [https://developer.mozilla.org](https://developer.mozilla.org). La referencia definitiva para HTML, CSS y JavaScript. Inmejorable para consultar propiedades CSS, APIs web y accesibilidad.

- **Web Content Accessibility Guidelines (WCAG) 2.2:** [https://www.w3.org/WAI/WCAG22/Understanding/](https://www.w3.org/WAI/WCAG22/Understanding/). El estándar internacional de accesibilidad web.

- **Nielsen Norman Group:** [https://www.nngroup.com](https://www.nngroup.com). Artículos de investigación en usabilidad, UX y diseño de interacción. Fuente de autoridad en el sector.

- **CSS-Tricks:** [https://css-tricks.com](https://css-tricks.com). Guías y tutoriales avanzados de CSS, especialmente los completísimos artículos sobre Flexbox y CSS Grid.

- **Figma Learn:** [https://help.figma.com/hc/en-us/categories/360002051613-Get-started](https://help.figma.com/hc/en-us/categories/360002051613-Get-started). Recursos oficiales de aprendizaje de Figma.

- **Storybook Tutorial:** [https://storybook.js.org/tutorials/](https://storybook.js.org/tutorials/). Tutoriales oficiales para aprender a documentar componentes.

### Canales de YouTube y podcasts

- **Fireship:** Canal sobre desarrollo web moderno con vídeos concisos y muy informativos sobre Angular, Tailwind, TypeScript y tendencias.

- **DesignCourse:** Tutoriales de diseño UI/UX con Figma, CSS y Tailwind.

- **Kevin Powell:** Canal especializado en CSS, Flexbox, Grid y técnicas avanzadas de maquetación.

- **La Tecnologería:** Podcast en español sobre diseño y desarrollo de productos digitales, con entrevistas a profesionales del sector en España.

### Herramientas

- **Figma:** Herramienta de diseño colaborativo (gratuita para educación).
- **Visual Studio Code:** Editor de código con extensiones para Angular, Tailwind, ESLint, Prettier.
- **Angular CLI:** Interfaz de línea de comandos oficial de Angular.
- **WAVE Evaluation Tool:** Extensión de navegador para auditoría de accesibilidad.
- **axe DevTools:** Extensión para análisis de accesibilidad en tiempo de desarrollo.
- **Lighthouse:** Herramienta integrada en Chrome DevTools para auditorías de rendimiento, accesibilidad, SEO y buenas prácticas.

### Organizaciones y comunidades

- **Andalucía Compromiso Digital:** Iniciativa de la Junta de Andalucía para la capacitación digital con recursos formativos gratuitos.
- **Google Developer Groups (GDG) Andalucía:** Comunidades locales en Granada, Sevilla, Málaga y Córdoba con meetups regulares sobre tecnologías de desarrollo.
- **Yes We Tech:** Asociación de mujeres en tecnología con comunidad activa en Andalucía, mentorías y eventos.
- **Open Source Weekends:** Comunidad española de open source con hackathons y contribuciones a proyectos reales.
