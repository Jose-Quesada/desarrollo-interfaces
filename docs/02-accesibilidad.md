---
icon: lucide/accessibility
---

# Accesibilidad Web (WCAG)

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Comprender los fundamentos de la accesibilidad web como derecho fundamental y necesidad de negocio, identificando los diferentes tipos de discapacidad (visual, auditiva, motriz, cognitiva) y las barreras que las interfaces inaccesibles generan para cada colectivo.
2. Conocer y aplicar la normativa WCAG (Web Content Accessibility Guidelines) en sus versiones 2.1 y 2.2, distinguiendo los tres niveles de conformidad (A, AA, AAA) y las exigencias legales aplicables en España y la Unión Europea, incluyendo el Real Decreto 1112/2018 y la Directiva Europea 2016/2102.
3. Aplicar los cuatro principios POUR (Perceptible, Operable, Comprensible, Robusto) en el desarrollo de interfaces con Angular y Tailwind CSS, implementando cada criterio de conformidad con ejemplos concretos de código y verificando su cumplimiento.
4. Dominar el uso de ARIA (Accessible Rich Internet Applications) como complemento al HTML semántico, aplicando roles, propiedades, estados y regiones en vivo con la regla de oro: "No uses ARIA si HTML ya lo resuelve".
5. Implementar componentes accesibles en Angular utilizando las herramientas del ecosistema: Angular CDK para gestión del foco y anuncios dinámicos, Angular Material para componentes con accesibilidad integrada, y Angular ESLint para detección automática de problemas.
6. Utilizar herramientas de evaluación de accesibilidad (Lighthouse, WAVE, axe DevTools, lectores de pantalla) para auditar aplicaciones, interpretar informes de accesibilidad y corregir sistemáticamente todos los errores detectados.
7. Aplicar la checklist de accesibilidad para desarrollo como parte del proceso habitual de construcción de interfaces, integrando la verificación de accesibilidad en el ciclo de desarrollo diario y en los criterios de definición de terminado de cada historia de usuario.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 4** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 4.** Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE a) Se han identificado los principales estándares de usabilidad y accesibilidad.
- CE b) Se ha valorado la importancia del uso de estándares para la creación de interfaces.
- CE i) Se han realizado pruebas para evaluar la usabilidad y accesibilidad de la aplicación.

!!! note "Conocimientos previos"

    Para abordar esta unidad con éxito, el alumnado debe poseer los siguientes conocimientos y destrezas:

    - Dominio de **HTML5 semántico**: uso correcto de etiquetas como `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<h1>`-`<h6>`, `<ul>`, `<ol>`, `<table>`, `<form>`, `<label>`, `<input>`, `<button>`. La accesibilidad empieza por un HTML correcto y semántico; sin esta base, ARIA y otras técnicas avanzadas pierden su fundamento.
    - Conocimientos de **CSS3** y del framework **Tailwind CSS**, ya que muchos criterios de accesibilidad tienen implicaciones visuales que se implementan mediante estilos (contraste, foco visible, espaciado, unidades relativas para tipografía).
    - Programación en **TypeScript** y manejo del framework **Angular**, incluyendo el sistema de plantillas, el binding de propiedades y eventos, los formularios reactivos y la inyección de dependencias.
    - Conocimientos previos de **UX** y usabilidad (Unidad 1), ya que accesibilidad y usabilidad son disciplinas complementarias que se solapan significativamente.
    - Manejo básico de herramientas de desarrollo del navegador (**Chrome DevTools**) para inspeccionar el DOM, el árbol de accesibilidad y las propiedades **ARIA**.

## Contenidos

1. Fundamentos de accesibilidad web
2. WCAG: versiones, niveles de conformidad y principios POUR
3. Principio POUR: Perceptible
4. Principio POUR: Operable
5. Principio POUR: Comprensible
6. Principio POUR: Robusto
7. ARIA: Accessible Rich Internet Applications
8. Implementación de accesibilidad en Angular
9. Herramientas de evaluación de accesibilidad
10. Checklist de accesibilidad para desarrollo

## Desarrollo teórico

### 1. Fundamentos de Accesibilidad Web

!!! info "Definición"

    La **accesibilidad web** es la práctica de diseñar y desarrollar sitios web y aplicaciones que puedan ser utilizados por todas las personas, independientemente de sus capacidades físicas, sensoriales o cognitivas, y del contexto y dispositivo que utilicen para acceder a ellos. Esta definición, aparentemente técnica, encierra un principio fundamental de justicia social y de **diseño universal**: la tecnología debe estar al servicio de todas las personas, no solo de aquellas que encajan en el perfil de "usuario estándar" que imaginamos al desarrollar.

Para comprender la magnitud de la accesibilidad, es necesario conocer los diferentes tipos de discapacidad y cómo cada uno afecta a la interacción con las interfaces digitales. La discapacidad visual abarca desde la ceguera total hasta la baja visión, pasando por el daltonismo (que afecta aproximadamente al 8% de los hombres). Una persona ciega utiliza un **lector de pantalla** (screen reader) que lee el contenido en voz alta o lo transmite a una línea braille. Si nuestra aplicación usa imágenes sin **texto alternativo**, formularios sin etiquetas asociadas, o interfaces construidas enteramente con divs sin semántica, el lector de pantalla no podrá interpretar el contenido y la persona quedará excluida. Una persona con baja visión puede necesitar aumentar el tamaño del texto, utilizar modos de alto contraste, o aplicar hojas de estilo personalizadas. Si nuestra aplicación fija tamaños de fuente en píxeles absolutos y no permite el zoom, o utiliza combinaciones de colores con bajo contraste, estaremos creando barreras innecesarias. Una persona daltónica no distinguirá un gráfico cuyas líneas solo se diferencien por colores rojo y verde; necesitará patrones, texturas o etiquetas adicionales.

La discapacidad auditiva afecta a personas sordas o con pérdida de audición. En aplicaciones web, la barrera principal son los contenidos de audio o vídeo sin subtítulos ni transcripciones. Un vídeo tutorial de la aplicación sin subtítulos es inaccesible para una persona sorda. Una notificación exclusivamente sonora (un beep al recibir un mensaje) pasará desapercibida. La solución es proporcionar alternativas textuales y visuales para todo contenido auditivo.

La discapacidad motriz abarca desde la imposibilidad de usar las manos hasta temblores que dificultan el control preciso del ratón, pasando por la parálisis parcial. Estas personas pueden navegar exclusivamente con el teclado, con dispositivos apuntadores alternativos (joystick bucal, eye-tracker) o con software de reconocimiento de voz. Si nuestra aplicación tiene áreas interactivas demasiado pequeñas, requiere gestos complejos de ratón (drag and drop sin alternativa de teclado), o tiene **trampas de teclado** (el foco entra en un componente pero no puede salir), será inoperable para estas personas.

La discapacidad cognitiva incluye condiciones como dislexia, TDAH, trastornos del espectro autista, o discapacidad intelectual. Las barreras aquí son interfaces sobrecargadas, lenguaje complejo, animaciones que distraen, timeouts estrictos, navegación inconsistente, o instrucciones ambiguas. El **diseño claro, predecible y tolerante a errores** que beneficia a las personas con discapacidad cognitiva beneficia a todas las personas usuarias.

!!! info "Normativa"

    Más allá de las consideraciones éticas y de derechos fundamentales, la accesibilidad tiene una justificación legal contundente en el contexto europeo y español. La **Directiva Europea 2016/2102** exige que los sitios web y aplicaciones móviles del sector público sean accesibles, estableciendo la norma EN 301 549 que referencia directamente las WCAG 2.1 nivel AA. En España, el **Real Decreto 1112/2018** sobre accesibilidad de los sitios web y aplicaciones para dispositivos móviles del sector público traspone esta directiva. La Ley 11/2023, publicada en el BOE el 9 de mayo de 2023, amplía estas obligaciones a determinados servicios del sector privado, incluyendo servicios bancarios, comercio electrónico, transporte, y servicios audiovisuales. En Andalucía, el Decreto 1/2017 regula la accesibilidad en los sistemas de información de la administración autonómica. Por tanto, desarrollar interfaces accesibles no es opcional ni una buena práctica recomendada: es una obligación legal para un número creciente de aplicaciones y servicios.

!!! info "Dato clave"

    Desde el punto de vista del negocio, la accesibilidad amplía el mercado potencial: según la Organización Mundial de la Salud, aproximadamente el **15% de la población mundial** vive con algún tipo de discapacidad. En España, según el INE, hay más de **4 millones de personas con discapacidad reconocida**. Excluir a este segmento de población no solo es éticamente cuestionable y legalmente arriesgado, sino también una mala decisión de negocio. Además, las mejoras de accesibilidad benefician a todas las personas usuarias: los subtítulos en vídeos son útiles en entornos ruidosos, el buen contraste es necesario en pantallas con reflejos, y la navegación por teclado es más rápida para personas usuarias avanzadas.

### 2. WCAG: Versiones, Niveles de Conformidad y Principios POUR

Las **Web Content Accessibility Guidelines (WCAG)** son el estándar internacional de accesibilidad web, desarrollado por el **W3C** a través de la Web Accessibility Initiative (WAI). Han evolucionado a lo largo del tiempo para adaptarse a las tecnologías emergentes: WCAG 2.0 se publicó en 2008 y estableció las bases; WCAG 2.1 se publicó en 2018 y añadió criterios para dispositivos móviles, baja visión y discapacidad cognitiva; WCAG 2.2 se publicó en 2023 y añadió criterios adicionales sobre foco, entrada de datos y consistencia. Actualmente se está desarrollando WCAG 3.0, que supondrá un cambio de paradigma en la forma de medir la accesibilidad, pasando de criterios binarios (cumple/no cumple) a puntuaciones graduales.

Las WCAG organizan sus requisitos en **tres niveles** de conformidad. 

 - El **nivel A** es el mínimo imprescindible: sin él, la aplicación es completamente inaccesible para algunos grupos de personas. Incluye criterios como proporcionar texto alternativo en imágenes, asegurar que toda la funcionalidad sea operable por teclado, y evitar el uso exclusivo del color para transmitir información. 
 - El **nivel AA** es el estándar legalmente exigido en la Unión Europea y el nivel que toda aplicación profesional debería cumplir como mínimo. Incluye criterios más exigentes como el contraste de color de al menos 4.5:1 para texto normal, la navegación consistente entre páginas, y la identificación de errores en formularios con sugerencias de corrección. 
 - El **nivel AAA** es el máximo nivel de accesibilidad y no es exigible para sitios completos porque algunos criterios son imposibles de satisfacer para ciertos tipos de contenido. Incluye criterios como el contraste mejorado de 7:1, el lenguaje de señas en contenidos audiovisuales, y la definición de palabras inusuales.

Los cuatro principios **POUR** constituyen la columna vertebral de las WCAG y organizan todos sus criterios de conformidad. Cualquier interfaz que aspire a ser accesible debe ser:

 - *Perceptible* (la información y los componentes de la interfaz deben presentarse de forma que las personas usuarias puedan percibirlos con los sentidos disponibles), 
 - *Operable* (los componentes de la interfaz y la navegación deben ser manejables con distintos métodos de entrada), 
 - *Comprensible* (la información y el manejo de la interfaz deben ser entendibles), y 
 - *Robusto* (el contenido debe ser suficientemente robusto para ser interpretado de forma fiable por una amplia gama de agentes de usuario, incluyendo tecnologías asistivas).

Estos cuatro principios ==son interdependientes y no negociables==. Si una interfaz falla en cualquiera de ellos, es inaccesible para un segmento de la población, independientemente de lo bien que cumpla los otros tres.

### 3. Principio POUR: Perceptible

El principio **Perceptible** establece que toda la información y los componentes de la interfaz deben presentarse de forma que todas las personas usuarias puedan percibirlos. Esto significa que el contenido no puede ser invisible para ninguno de los sentidos disponibles para la interacción. A continuación, se detallan las pautas y criterios de este principio con ejemplos concretos de implementación en Angular y Tailwind CSS.

La pauta 1.1 exige proporcionar **alternativas textuales** para todo contenido no textual, de forma que pueda ser convertido a otros formatos que las personas necesiten, como texto ampliado, braille, voz, símbolos o lenguaje simplificado. En la implementación Angular, esto significa que cada imagen debe tener un atributo `alt` descriptivo. No todas las imágenes requieren el mismo tipo de texto alternativo. Si la imagen transmite información relevante, el `alt` debe describir esa información de forma concisa. Si la imagen es puramente decorativa, debe usar `alt=""` (cadena vacía, no omitir el atributo) para que el lector de pantalla la ignore. Si la imagen contiene texto informativo, el texto debe estar en el `alt` o, mejor aún, no usar imágenes para texto. En Angular, el binding se escribe `[alt]="imagen.altText"` o directamente `<img alt="Gráfico de ventas mensuales: enero 15000, febrero 18200, marzo 21000" />`. Los iconos SVG que transmiten información requieren `role="img"` y un `aria-label` o un elemento `<title>` dentro del SVG.

La pauta 1.2 proporciona alternativas para **medios tempodependientes** (audio y vídeo). Los vídeos deben tener subtítulos (al menos pregrabados para nivel A, y en directo para nivel AA). Las grabaciones de audio deben tener transcripciones textuales completas. Las aplicaciones de gestión rara vez incluyen vídeo, pero si incluyen tutoriales en vídeo, webinars grabados o podcasts informativos, estos deben ser accesibles.

La pauta 1.3 exige crear contenido que pueda presentarse de diferentes formas sin perder información o estructura. Esto se logra mediante **HTML semántico** y una estructura de contenido lógica. Los encabezados deben utilizarse en orden jerárquico sin saltarse niveles: un `<h1>` para el título de la página, `<h2>` para secciones principales, `<h3>` para subsecciones, y así sucesivamente. En Angular, cada componente de página debe comenzar con un `<h1>` (o heredarlo del layout), y los componentes reutilizables deben comenzar con el nivel de encabezado adecuado, que puede parametrizarse mediante una propiedad de entrada. Las listas deben usar `<ul>`, `<ol>` y `<dl>` según corresponda, no párrafos con guiones al inicio. Las tablas de datos deben usar `<table>` con `<thead>`, `<tbody>`, `<th>` con alcance (`scope="col"` o `scope="row"`) y un `<caption>` que describa el contenido de la tabla. En Angular, una tabla accesible se implementa con un componente que recibe columnas y filas y genera la estructura semántica correcta.

La pauta 1.4 busca que el contenido sea fácil de ver y oír, separando el primer plano del fondo. Aquí se incluyen los requisitos de **contraste de color**. El nivel AA exige una relación de contraste de al menos 4.5:1 para texto normal y de al menos 3:1 para texto grande (más de 18px o 14px en negrita). En Tailwind CSS, las combinaciones de colores predefinidas (como `text-gray-900` sobre `bg-white`) suelen cumplir estos requisitos, pero las combinaciones personalizadas (definidas en `@theme`) deben verificarse explícitamente con herramientas como el comprobador de contraste de **WebAIM**. Un error frecuente es usar `text-gray-400` sobre `bg-gray-100`, que tiene un contraste insuficiente para texto normal.

El color no debe ser el único medio de transmitir información (criterio 1.4.1). Un mensaje de error no puede limitarse a poner el borde del campo en rojo; debe incluir también un icono de error, un texto descriptivo y un atributo `aria-invalid="true"`. Un gráfico de líneas no puede distinguir sus series solo por color; debe usar diferentes patrones de línea (discontinua, punteada) o marcadores (círculos, cuadrados, triángulos). Una tabla con estados (pendiente, en curso, completado) no puede limitarse a cambiar el color de fondo de la fila; debe incluir una columna con el texto del estado.

El texto debe poder redimensionarse hasta un 200% sin pérdida de contenido ni funcionalidad (criterio 1.4.4). Esto implica usar unidades relativas (rem, em, porcentajes) en lugar de unidades absolutas (px) para tamaños de fuente, y asegurar que los contenedores se adaptan al texto ampliado sin desbordamientos ni solapamientos. Tailwind por defecto usa rem, lo que facilita este criterio.

Las imágenes de texto deben evitarse (criterio 1.4.5) salvo cuando la presentación del texto sea esencial (por ejemplo, un logotipo). En aplicaciones de gestión, no hay justificación para usar imágenes de texto; el texto debe ser texto real, estilizado con CSS.

### 4. Principio POUR: Operable

El principio **Operable** exige que los componentes de la interfaz y la navegación puedan ser utilizados por todas las personas, independientemente del dispositivo de entrada que utilicen.

La pauta 2.1, **accesibilidad por teclado**, es una de las más críticas y una de las más frecuentemente violadas en aplicaciones web modernas construidas con frameworks JavaScript. Toda la funcionalidad de la aplicación debe ser operable a través de una interfaz de teclado sin requerir tiempos específicos para pulsaciones individuales (criterio 2.1.1). Esto significa que cada botón, enlace, campo de formulario, pestaña, modal, menú desplegable y cualquier otro elemento interactivo debe ser alcanzable y operable exclusivamente con el teclado. Los elementos interactivos nativos de HTML (`<button>`, `<a href>`, `<input>`, `<select>`, `<textarea>`) son accesibles por teclado por defecto, lo que refuerza la regla de oro: usa HTML semántico siempre que sea posible. Los problemas surgen cuando se crean elementos interactivos personalizados con `<div>` o `<span>` porque "el botón nativo no se puede estilizar". Un `<div>` con un `(click)` en Angular no es accesible por teclado a menos que se le añada `tabindex="0"`, un manejador de teclado para Enter y Space, y los roles y estados ARIA correspondientes. Es mucho más sencillo usar un `<button>` y estilizarlo con Tailwind para que tenga el aspecto deseado.

El foco del teclado debe ser visible en todo momento (criterio 2.4.7, nivel AA). Los navegadores muestran por defecto un contorno (outline) alrededor del elemento que tiene el foco. Muchos desarrolladores y diseñadores eliminan este contorno con `outline: none` porque "queda feo", pero esto hace la aplicación inaccesible para personas que navegan con teclado. La solución correcta no es eliminar el foco visible, sino estilizarlo de forma que sea estéticamente agradable y funcional. Tailwind CSS proporciona utilidades para esto: en lugar de `outline-none`, se usa `focus:ring-2 focus:ring-primary-500 focus:ring-offset-2` para crear un anillo de foco visible y elegante. La pseudoclase `:focus-visible` (Tailwind: `focus-visible:`) permite mostrar el foco solo cuando la persona usuaria está navegando con teclado, no cuando hace clic con el ratón, combinando lo mejor de ambos mundos.

No debe haber **trampas de teclado** (criterio 2.1.2): si el foco puede entrar en un componente de la página usando el teclado, debe poder salir del componente usando solo el teclado. Los modales son el caso más típico de trampa de teclado potencial. Un modal accesible debe capturar el foco dentro de sí mismo mientras está abierto (para que la persona usuaria no tabule accidentalmente al contenido detrás del modal), pero debe permitir salir del modal cerrándolo con la tecla Escape y devolviendo el foco al elemento que lo abrió. Angular CDK proporciona la directiva `cdkTrapFocus` precisamente para este propósito.

La pauta 2.2 exige proporcionar tiempo suficiente para leer y usar el contenido. Las aplicaciones no deben imponer límites de tiempo estrictos sin opción de ajustarlos o desactivarlos. Si una aplicación de gestión cierra la sesión por inactividad, debe avisar con antelación y ofrecer la opción de extenderla con una acción simple (como pulsar cualquier tecla o hacer clic en un botón). Los carruseles automáticos deben tener controles de pausa.

La pauta 2.3 advierte contra el contenido que pueda provocar convulsiones o reacciones físicas. No se debe incluir contenido que destelle más de tres veces por segundo. En aplicaciones de gestión esto rara vez es un problema, pero las animaciones CSS y las transiciones deben ser sutiles y respetar la consulta de medios `prefers-reduced-motion: reduce`.

La pauta 2.4, navegación, es extensa y fundamental. Las aplicaciones deben proporcionar formas de ayudar a las personas usuarias a navegar, encontrar contenido y determinar dónde se encuentran. Los criterios incluyen: proporcionar un enlace para saltar bloques de contenido repetido (**skip link**) como menús de navegación, que en Angular se implementa como un enlace oculto que solo se muestra al recibir el foco (`sr-only focus:not-sr-only` en Tailwind) y que apunta al contenido principal (`<main id="main-content">`). Las páginas deben tener títulos descriptivos (criterio 2.4.2), que en Angular se gestionan mediante el servicio `Title` del paquete `@angular/platform-browser`, actualizando el título en cada navegación. El orden de foco debe ser lógico y predecible (criterio 2.4.3), siguiendo el flujo visual de la página. Los enlaces y botones deben tener **textos descriptivos** que permitan entender su propósito sin necesidad de contexto adicional (criterio 2.4.4): "Ver detalle del cliente" en lugar de "Ver más" o "Click aquí". La navegación debe ser consistente entre páginas (criterio 3.2.3): los mismos elementos de navegación en el mismo orden en todas las páginas.

### 5. Principio POUR: Comprensible

El principio **Comprensible** aborda la claridad del lenguaje, la previsibilidad del comportamiento y la ayuda para evitar y corregir errores.

La pauta 3.1 exige que el contenido sea legible y comprensible. El idioma de la página debe estar declarado en el elemento `<html>` mediante el atributo `lang="es"` (criterio 3.1.1), y los cambios de idioma dentro de la página deben marcarse con `lang` en el elemento correspondiente. Esto es esencial para que los **lectores de pantalla** utilicen la pronunciación y entonación correctas. En Angular, el idioma se establece en el `index.html` y los cambios de idioma se marcan con `[attr.lang]="'en'"` en plantillas. El contenido debe ser legible para el público objetivo (criterio 3.1.5): en aplicaciones de gestión para administración pública andaluza, el lenguaje debe ser claro, evitar tecnicismos innecesarios y ofrecer definiciones de términos especializados cuando aparezcan.

La pauta 3.2 exige que las páginas web aparezcan y funcionen de manera predecible. Los elementos de la interfaz deben comportarse como las personas usuarias esperan: un botón debe activarse con clic o Enter/Space, no con doble clic o gestos complejos. El **cambio de contexto** (abrir una nueva ventana, mover el foco, enviar un formulario) solo debe ocurrir cuando la persona usuaria lo solicite explícitamente, no automáticamente al seleccionar una opción de un `<select>` (criterio 3.2.2). La navegación y los elementos identificativos deben mantenerse consistentes a lo largo de toda la aplicación (criterios 3.2.3 y 3.2.4): el logo y el nombre de la aplicación deben aparecer en la misma ubicación en todas las páginas, y los mecanismos de navegación deben presentarse en el mismo orden relativo.

La pauta 3.3, ayuda a la entrada de datos, es especialmente relevante para aplicaciones de gestión con formularios complejos. Las etiquetas o instrucciones deben proporcionarse cuando el contenido requiere entrada de la persona usuaria (criterio 3.3.2). Cada campo de formulario debe tener un `<label>` asociado mediante el atributo `for` (en Angular: `[for]="id"`) que coincida con el `id` del campo. En Angular, los **formularios reactivos** facilitan este patrón, pero hay que implementarlo explícitamente en la plantilla. Las etiquetas flotantes (material design) requieren atención especial para mantener la asociación label-input.

Los **errores de entrada** deben ser detectados y descritos textualmente a la persona usuaria (criterio 3.3.1), y cuando se detectan, deben proporcionarse sugerencias para su corrección (criterio 3.3.3, nivel AA). En Angular, esto implica mostrar mensajes de error junto al campo, con texto que explique el problema y cómo solucionarlo, y asociar el mensaje de error al campo mediante `aria-describedby`. Para formularios que implican transacciones legales o financieras (como un formulario de compra en una aplicación de gestión comercial), la persona usuaria debe poder revisar, confirmar y corregir la información antes de finalizar el envío (criterio 3.3.4, nivel AA).

### 6. Principio POUR: Robusto

El principio **Robusto** exige que el contenido sea suficientemente sólido para ser interpretado de forma fiable por una amplia variedad de agentes de usuario, incluyendo las tecnologías asistivas actuales y futuras.

La pauta 4.1, **compatibilidad**, requiere maximizar la compatibilidad con los agentes de usuario actuales y futuros. El HTML debe ser válido según las especificaciones del W3C: etiquetas correctamente anidadas y cerradas, atributos sin duplicar, IDs únicos por página. La validación del HTML generado por una aplicación Angular puede realizarse extrayendo el HTML renderizado desde las DevTools y pasándolo por el validador del W3C. Errores comunes en Angular incluyen IDs duplicados cuando un componente reutilizable genera el mismo ID en múltiples instancias, y etiquetas no estándar de componentes que no se renderizan adecuadamente.

Los componentes de interfaz de usuario deben tener sus nombres, roles, estados, propiedades y valores determinados programáticamente y expuestos a las **tecnologías asistivas** (criterio 4.1.2). Esto significa que cada elemento interactivo debe comunicar al lector de pantalla qué es (rol), cómo se llama (nombre accesible), en qué estado se encuentra (expandido, seleccionado, deshabilitado) y cuál es su valor actual. Los elementos HTML nativos proporcionan esta información automáticamente: un `<button>` tiene rol de botón, su nombre accesible es su contenido textual, y tiene estados como disabled. Los componentes personalizados requieren ARIA para proporcionar esta semántica. En Angular, los atributos ARIA deben estar vinculados a las propiedades del componente mediante `[attr.aria-expanded]="isOpen()"` para que se actualicen reactivamente con el estado del componente.

### 7. ARIA: Accessible Rich Internet Applications

**ARIA** (Accessible Rich Internet Applications) es una especificación del W3C que define un conjunto de atributos HTML adicionales que permiten mejorar la accesibilidad de aplicaciones web dinámicas y componentes de interfaz personalizados. ARIA no añade nuevas funcionalidades al navegador; añade semántica que los lectores de pantalla y otras tecnologías asistivas interpretan para comunicar a la persona usuaria la naturaleza y el estado de los elementos de la interfaz.

La regla de oro de ARIA, que todo desarrollador debe grabar a fuego, es: "==No uses ARIA si HTML ya lo resuelve==". Antes de añadir `role="button"` a un `<div>`, pregúntate si puedes usar un `<button>`. Antes de construir un menú con `role="menu"`, `role="menuitem"` y gestión de foco manual, pregúntate si puedes usar un `<nav>` con una lista de enlaces. **HTML5** ha incorporado elementos semánticos que cubren la mayoría de necesidades de las aplicaciones: `<main>`, `<nav>`, `<header>`, `<footer>`, `<article>`, `<section>`, `<aside>`, `<figure>`, `<figcaption>`, `<details>`, `<summary>`, `<dialog>`. Cada vez que usas uno de estos elementos en lugar de un `<div>` genérico, estás proporcionando accesibilidad sin esfuerzo adicional.

Los **roles ARIA** definen qué es un elemento. Los más utilizados en aplicaciones de gestión son: `button` (para elementos que actúan como botones pero no pueden usar el elemento nativo), `link` (para elementos que actúan como enlaces), `dialog` (para ventanas modales), `alert` (para mensajes que requieren atención inmediata), `tab`, `tabpanel` y `tablist` (para interfaces de pestañas), `navigation` (para bloques de navegación, aunque es preferible usar `<nav>`), `main` (para el contenido principal, aunque es preferible usar `<main>`), `complementary` (para contenido complementario, preferible `<aside>`), y `alertdialog` (para diálogos de confirmación que requieren respuesta).

Las **propiedades ARIA** proporcionan información adicional sobre los elementos. `aria-label` asigna un nombre accesible al elemento, visible solo para tecnologías asistivas. Es útil para botones que solo contienen iconos: `<button aria-label="Cerrar diálogo"><svg>...</svg></button>`. `aria-labelledby` referencia el ID de otro elemento que actúa como etiqueta visible, útil cuando la etiqueta ya existe en el DOM. `aria-describedby` referencia elementos que proporcionan una descripción más extensa, como un párrafo con instrucciones o un mensaje de error. `aria-expanded` indica si un elemento que controla la visibilidad de otro está expandido (`true`) o colapsado (`false`), esencial para menús desplegables y acordeones. `aria-current` indica el elemento activo en un conjunto, como la página actual en un menú de navegación. `aria-hidden` oculta un elemento de las tecnologías asistivas sin eliminarlo visualmente, útil para iconos decorativos o contenido duplicado. `aria-live` convierte una región del DOM en una región en vivo cuyos cambios son anunciados automáticamente por los lectores de pantalla, con valores `polite` (espera a que el lector termine de hablar) o `assertive` (interrumpe inmediatamente).

Los **estados ARIA** representan condiciones que pueden cambiar. `aria-disabled` indica que un elemento está deshabilitado (preferible usar el atributo HTML `disabled` en elementos nativos). `aria-selected` indica si un elemento seleccionable está seleccionado. `aria-checked` indica el estado de un checkbox o radio button personalizado. `aria-pressed` indica el estado de un botón toggle. `aria-invalid` marca un campo de formulario como inválido, complementando la validación nativa de HTML.

Las **regiones en vivo** (live regions) son uno de los usos más potentes de ARIA en aplicaciones dinámicas. Cuando el contenido de una aplicación cambia como resultado de una acción asíncrona (carga de datos, envío de formulario, recepción de un mensaje), la persona usuaria de lector de pantalla puede no percibir el cambio porque está enfocada en otra parte de la página. Una región `aria-live="polite"` anuncia estos cambios de forma no intrusiva (el lector espera a terminar su frase actual). Una región `aria-live="assertive"` anuncia cambios importantes de forma inmediata. En Angular, el servicio `LiveAnnouncer` de Angular CDK abstrae el uso de live regions: `this.liveAnnouncer.announce('Se han cargado 153 registros', 'polite')`.

!!! warning "Mal uso de ARIA"

    Es fundamental entender lo que ARIA no hace. ARIA no añade interactividad; si creas un `<div role="button">`, debes implementar manualmente el manejo de teclado (Enter, Space), el foco visible, y la prevención de comportamiento por defecto. ARIA no modifica el comportamiento del navegador; solo comunica semántica a las tecnologías asistivas. **Un mal uso de ARIA puede empeorar la accesibilidad**: un `aria-label` redundante que repita información ya disponible, un `aria-hidden="true"` en un elemento interactivo que debería ser accesible, o un rol incorrecto que confunda al lector de pantalla.

[¿Qué es ARIA?](https://www.youtube.com/watch?v=ro3GQ9E7HVA)

[Angular ARIA](https://www.youtube.com/watch?v=pVTiAZgEslw&t=1510s)

### 8. Implementación de Accesibilidad en Angular

El ecosistema Angular ofrece varias herramientas específicas para implementar accesibilidad de forma robusta. **Angular CDK** (Component Dev Kit) es una biblioteca oficial del equipo de Angular que proporciona primitivas de comportamiento sin estilos predefinidos, incluyendo varias utilidades de accesibilidad.

La directiva `cdkTrapFocus` captura el foco del teclado dentro de un elemento, imprescindible para modales accesibles. Su uso es directo: `<div cdkTrapFocus [cdkTrapFocusAutoCapture]="true">` en el contenedor del modal. Cuando el modal se cierra, el foco se libera automáticamente. Combinada con un listener de teclado para la tecla Escape (`@HostListener('document:keydown.escape')`), se obtiene un modal completamente accesible por teclado.

`FocusKeyManager` es un servicio que gestiona el foco del teclado en listas de elementos, ideal para listas desplegables, menús, tabs y cualquier colección de elementos navegables. Permite navegar con las flechas del teclado, con soporte para wrap-around (al llegar al último elemento, pasar al primero), activación con Enter, y **tipado anticipatorio** (escribir letras para saltar a un elemento). En Angular basado en señales, `FocusKeyManager` se integra mediante `@ViewChildren` para obtener los elementos del DOM y `keydown` listeners en el elemento contenedor.

`LiveAnnouncer`, como se mencionó anteriormente, anuncia mensajes a las personas usuarias de lectores de pantalla mediante regiones en vivo gestionadas internamente. Es útil para confirmar acciones asíncronas, anunciar el número de resultados de una búsqueda, notificar errores, y cualquier cambio dinámico que deba ser comunicado.

**Angular Material** proporciona componentes que incluyen accesibilidad integrada. Sus componentes (mat-input, mat-select, mat-checkbox, mat-dialog, mat-tabs, mat-menu) implementan roles, propiedades y gestión de foco según las especificaciones de **WAI-ARIA**. Sin embargo, Angular Material impone su propio sistema de diseño, lo que lo hace incompatible con Tailwind CSS en muchos casos. Para proyectos que usan Tailwind, se recomienda utilizar Angular CDK (que no impone estilos) e implementar componentes personalizados con la semántica y el comportamiento correctos.

El plugin de **Angular ESLint** incluye **reglas de accesibilidad** (`@angular-eslint/template/accessibility-*`) que detectan problemas comunes en las plantillas Angular. Reglas como `accessibility-alt-text` verifican que las imágenes tengan atributo `alt`, `accessibility-label-has-associated-control` verifica que los labels estén asociados a controles, `accessibility-valid-aria` verifica que los atributos ARIA sean válidos, y `accessibility-role-supports-aria-attr` verifica que los atributos ARIA sean compatibles con el rol del elemento. Configurar estas reglas como errores (no solo advertencias) en el ESLint del proyecto fuerza a todo el equipo a mantener la accesibilidad en cada commit.

El bindeo de atributos ARIA en Angular se realiza mediante la sintaxis `[attr.aria-*]`. Por ejemplo: `[attr.aria-expanded]="isOpen()"`, `[attr.aria-selected]="isActive(item)"`, `[attr.aria-label]="label()"`, `[attr.aria-describedby]="errorId"`. En componentes con señales (Angular 17+), estas vinculaciones se actualizan reactivamente.

### 9. Herramientas de Evaluación de Accesibilidad

La evaluación de la accesibilidad debe combinar **herramientas automáticas** (que detectan problemas programáticos) con **pruebas manuales** (que detectan problemas de usabilidad y contexto). Ninguna herramienta automática puede verificar todos los criterios de las WCAG; se estima que cubren entre un 30% y un 50% de los criterios. El resto requiere juicio humano y pruebas con tecnologías asistivas reales.

**Lighthouse** es la herramienta de auditoría integrada en Chrome DevTools. Accesible desde la pestaña "Lighthouse" tras inspeccionar una página (F12 > Lighthouse), realiza una auditoría automática de accesibilidad, rendimiento, buenas prácticas y SEO. Su puntuación de accesibilidad (0-100) se basa en una selección de criterios de WCAG verificables automáticamente. Una puntuación de 100 en Lighthouse no garantiza que la página sea completamente accesible, pero una puntuación baja sí indica problemas que deben corregirse. Lighthouse es ideal como primera verificación en el flujo de desarrollo diario.

**WAVE** (Web Accessibility Evaluation Tool) es una extensión de navegador (Chrome, Firefox, Edge) que realiza un análisis visual de la página. Superpone iconos e indicadores sobre el contenido para señalar problemas de accesibilidad, características accesibles, elementos estructurales y posibles problemas. Su panel lateral muestra un resumen de errores, alertas, características y elementos estructurales, con explicaciones detalladas de cada hallazgo y enlaces a la documentación de WCAG correspondiente. WAVE es especialmente útil para detectar problemas de contraste, falta de etiquetas, estructura de encabezados incorrecta y atributos ARIA mal utilizados.

**axe DevTools** (de Deque Systems) es una extensión de navegador que proporciona un análisis detallado de accesibilidad directamente en las DevTools. A diferencia de Lighthouse, que analiza la página completa de una vez, axe DevTools se integra en el panel de elementos y analiza el árbol de accesibilidad del DOM renderizado. Identifica violaciones de WCAG, las clasifica por gravedad (críticas, graves, moderadas, menores) y proporciona información detallada sobre cada problema: elemento afectado, criterio WCAG violado, descripción del problema, impacto en las personas usuarias y código de ejemplo para solucionarlo. Su versión Pro incluye tests de componentes inteligentes y guías de corrección paso a paso.

**axe-core** es la librería subyacente que utilizan Lighthouse, axe DevTools y muchas otras herramientas. Puede integrarse en tests automatizados con frameworks como Jasmine (el framework de testing por defecto de Angular) o Jest. En Angular, se instala como dependencia de desarrollo (`npm install -D axe-core`) y se escribe un test de integración que monta el componente, inyecta axe-core y ejecuta el análisis, fallando si se detectan violaciones. Este enfoque permite integrar la verificación de accesibilidad en el pipeline de CI/CD, evitando regresiones.

Los **lectores de pantalla** son la prueba de fuego de la accesibilidad. **NVDA** (NonVisual Desktop Access) es el lector de pantalla gratuito más utilizado en Windows. VoiceOver está integrado en macOS e iOS. JAWS es el lector de pantalla comercial más extendido en entornos profesionales. Probar la aplicación con al menos un lector de pantalla real es irremplazable: ninguna herramienta automática puede simular la experiencia de una persona ciega navegando por la aplicación. Se recomienda a cada desarrollador pasar al menos diez minutos al mes navegando por la aplicación que desarrolla usando exclusivamente un lector de pantalla, sin mirar la pantalla.

!!! tip "Comprobadores de contraste"

    Los comprobadores de contraste son herramientas indispensables. El **Contrast Checker de WebAIM** (https://webaim.org/resources/contrastchecker/) permite introducir colores en hexadecimal y verifica la relación de contraste para texto normal, texto grande y componentes UI. La extensión **Stark** para Figma permite verificar el contraste directamente en los diseños antes de implementarlos. El plugin de contraste de Tailwind CSS puede integrar esta verificación en el flujo de desarrollo.

### 10. Checklist de Accesibilidad para Desarrollo

A continuación se presenta una **checklist sistemática** que todo desarrollador de interfaces debe aplicar antes de considerar terminada una funcionalidad. Esta checklist no sustituye a una auditoría profesional completa, pero garantiza un nivel básico de accesibilidad que cubre la mayoría de los problemas evitables:

1. Validar el HTML renderizado con el validador del W3C. Errores de sintaxis HTML pueden confundir a los lectores de pantalla y provocar comportamientos impredecibles. En Angular, usa las DevTools para copiar el HTML externo de la página y pégalo en https://validator.w3.org/nu/.

2. Revisar la **estructura de encabezados** (h1-h6). Debe haber exactamente un `<h1>` por página (el título principal). Los niveles no deben saltarse (no pasar de h2 a h4 sin un h3 intermedio). Verifica que todos los textos que visualmente actúan como títulos estén marcados con el elemento de encabezado correspondiente.

3. Comprobar que toda la funcionalidad sea operativa con teclado. Desconecta el ratón y navega por la aplicación usando solo Tab, Shift+Tab, Enter, Escape, y teclas de flecha. Pregúntate: ¿Puedo llegar a todos los elementos interactivos? ¿Puedo activarlos? ¿Puedo salir de los modales y menús? ¿El orden de foco es lógico?

4. Verificar el foco visible en todos los elementos interactivos. Con el teclado, tabula por toda la página y asegúrate de que en cada paso se ve claramente qué elemento tiene el foco. No uses `outline: none` sin reemplazarlo por un indicador de foco alternativo como `focus-visible:ring-2`.

5. Revisar todos los textos alternativos: cada imagen informativa tiene un `alt` descriptivo; cada imagen decorativa tiene `alt=""`; cada icono SVG informativo tiene `role="img"` y `aria-label`; cada gráfico o infografía tiene una alternativa textual.

6. Comprobar el **contraste de colores** de todas las combinaciones texto-fondo utilizadas en la aplicación. Usa el comprobador de WebAIM o la extensión axe DevTools. Presta especial atención a texto gris sobre fondo gris, texto sobre imágenes, y placeholders en inputs.

7. Verificar formularios: cada campo tiene un `<label>` asociado mediante `for`/`id` o está envuelto por el `<label>`; los campos obligatorios están indicados visualmente y programáticamente; los errores de validación se muestran junto al campo y están asociados mediante `aria-describedby`; las instrucciones generales del formulario están al principio.

8. Añadir un **skip link** al inicio de la página que permita saltar al contenido principal. En Angular, se puede añadir en el `index.html` como `<a href="#main-content" class="sr-only focus:not-sr-only ...">Saltar al contenido principal</a>`.

9. Auditar con Lighthouse desde Chrome DevTools y corregir todas las incidencias detectadas. Apuntar a una puntuación de 100 en accesibilidad, aunque esto no garantiza accesibilidad completa.

10. Probar al menos la funcionalidad principal con un lector de pantalla real (NVDA en Windows o VoiceOver en Mac). Sin mirar la pantalla, intenta completar una tarea principal de la aplicación. Anota cada punto de confusión y cada elemento que no se anuncia correctamente.

## Ejemplos guiados

### Ejemplo Guiado 1: Hacer Accesible un Modal

Partimos de un componente modal implementado en Angular de forma visualmente correcta pero completamente inaccesible. El modal es un `<div>` con overlay oscuro que aparece al hacer clic en un botón y se cierra al hacer clic en la X o fuera del modal. El código original carece de **gestión de foco**, **roles ARIA**, cierre con Escape, y retorno del foco al cerrar.

El proceso de hacerlo accesible comienza añadiendo el rol `dialog` al contenedor del modal y `aria-modal="true"` para indicar a los lectores de pantalla que es una ventana modal. Se añade `aria-labelledby` referenciando el ID del título del modal, y `aria-describedby` referenciando el ID del contenido si incluye texto descriptivo adicional.

Para la gestión del foco, se importa la directiva `cdkTrapFocus` de Angular CDK (`import { A11yModule } from '@angular/cdk/a11y'` en el módulo o componente standalone) y se aplica al contenedor del modal: `<div cdkTrapFocus [cdkTrapFocusAutoCapture]="true">`. Esto asegura que al abrirse el modal, el foco se mueva automáticamente al primer elemento interactivo dentro del modal, y que al tabular no se escape al contenido de fondo.

Para el cierre con teclado, se implementa un `@HostListener` en el componente del modal que escucha la tecla Escape y emite el evento de cierre. También se añade un manejador para que el foco retorne al botón que abrió el modal cuando este se cierra, almacenando una referencia al elemento activo antes de abrir el modal mediante `this.previouslyFocused = document.activeElement as HTMLElement` y llamando a `this.previouslyFocused.focus()` al cerrar.

El botón de cierre (la X) pasa de ser un `<span>` con un `(click)` a un `<button>` con `aria-label="Cerrar diálogo"`. Esto lo hace automáticamente accesible por teclado y comprensible para lectores de pantalla. Las acciones dentro del modal (botones de confirmar y cancelar) también son elementos `<button>` nativos.

Finalmente, se implementa un test unitario con Jasmine que verifica que el modal atrapa el foco correctamente y que la tecla Escape lo cierra. Se instala `axe-core` y se añade un test de integración que ejecuta el análisis de accesibilidad sobre el modal renderizado, verificando que no hay violaciones.

### Ejemplo Guiado 2: Auditoría de Accesibilidad con Lighthouse y WAVE

Se selecciona una página de la aplicación de gestión de biblioteca desarrollada por el alumnado y se somete a una auditoría completa. El proceso comienza ejecutando Lighthouse en Chrome DevTools sobre la página en cuestión. El informe revela una puntuación de 73 sobre 100 en accesibilidad, con problemas detectados en contraste de texto (2 elementos), nombres de enlaces no descriptivos (3 elementos), y falta de atributo `lang` en el elemento `<html>`.

Tras corregir estos problemas en el código Angular (añadiendo `lang="es"` al `index.html`, ajustando los colores de texto para cumplir el contraste 4.5:1 usando `text-gray-800` en lugar de `text-gray-500` sobre `bg-gray-50`, y reescribiendo los enlaces de "Ver más" a "Ver detalle del préstamo"), se ejecuta de nuevo Lighthouse, obteniendo una puntuación de 96.

A continuación, se ejecuta WAVE sobre la misma página. WAVE detecta problemas que Lighthouse no había encontrado: una imagen sin `alt` (un logotipo en el footer), una tabla sin encabezados de fila (solo tenía encabezados de columna), y un `<select>` sin `<label>` asociado (el filtro de estado). Estos problemas se corrigen en el código y se vuelve a ejecutar WAVE hasta que no muestra errores, solo alertas (que se documentan y priorizan para futuras iteraciones).

La auditoría se completa con una prueba manual de teclado: se navega por toda la página sin ratón, descubriendo que el menú desplegable de usuario en la barra de navegación no se abre con teclado (solo reacciona a hover). Se corrige añadiendo eventos `focus` y `keydown` y el atributo `aria-expanded`. El informe final de la auditoría documenta cada problema encontrado, el criterio WCAG violado, la solución implementada, y el resultado tras la corrección.

### Ejemplo Guiado 3: Tabla de Datos Navegable por Teclado

Se parte de una tabla de datos implementada en Angular con un `<table>` estándar que muestra un listado de alumnos con columnas para nombre, apellidos, curso y acciones (editar, eliminar). La tabla es semánticamente correcta pero no permite navegación por teclado dentro de las filas ni interacción eficiente con teclado en las acciones.

El objetivo es convertirla en una tabla completamente operable por teclado utilizando `FocusKeyManager` de Angular CDK. Se añade `tabindex="0"` al `<tbody>` para que sea focusable, y `(keydown)` al mismo elemento para capturar las teclas de flecha y otras teclas de navegación.

Mediante `@ViewChildren`, se obtiene una `QueryList` de todas las filas de la tabla. Se inicializa un `FocusKeyManager` con esta lista y se configura con `withWrap(true)` para que la navegación sea circular. En el manejador de `keydown`, se mapean las teclas: ArrowDown activa `focusKeyManager.setNextItemActive()`, ArrowUp activa `setPreviousItemActive()`, Enter activa la acción principal de la fila (editar), Tab mueve el foco a la primera acción de la fila. Las acciones de cada fila (editar, eliminar) se convierten en una lista secundaria gestionada por otro `FocusKeyManager` anidado, permitiendo navegar entre acciones con flechas izquierda/derecha y salir de la fila con Escape.

Se añaden los atributos ARIA necesarios: `role="grid"` en la tabla, `role="row"` en cada fila, `role="gridcell"` con `aria-selected` en cada celda, y `aria-label` descriptivo en cada celda de acciones (por ejemplo, `aria-label="Editar alumno María García"` en lugar de solo "Editar").

El resultado es una tabla que una persona usuaria de teclado o lector de pantalla puede navegar tan eficientemente como una persona usuaria de ratón, pudiendo recorrer filas, saltar entre acciones y ejecutarlas sin retirar las manos del teclado.

## Actividades guiadas

### Actividad Guiada 1: Hacer Accesible un Formulario de Alta de Cliente

El alumnado recibe un formulario de alta de cliente desarrollado en Angular con Tailwind CSS que actualmente es inaccesible. El formulario contiene campos para nombre, CIF, dirección, teléfono, email y tipo de cliente. Los problemas incluyen: ausencia de etiquetas `<label>` asociadas a los inputs (solo placeholders), campos sin indicación de obligatoriedad, mensajes de error genéricos sin asociación al campo, y botón de envío deshabilitado sin indicación. El alumnado deberá: añadir etiquetas visibles y asociadas a cada campo, marcar campos obligatorios con asterisco y atributo `required`, implementar mensajes de error con `aria-describedby`, añadir `aria-invalid` dinámico, implementar un resumen de errores al inicio del formulario con enlaces a los campos problemáticos, y asegurar que el botón de envío indique por qué está deshabilitado. Finalmente, auditarán el formulario corregido con **axe DevTools** y **Lighthouse** hasta alcanzar una puntuación de 100 en accesibilidad.

### Actividad Guiada 2: Navegación por Teclado en una Aplicación Completa

El alumnado realizará una auditoría completa de navegación por teclado en la aplicación de gestión de biblioteca que vienen desarrollando. Deberán desconectar físicamente el ratón de su equipo y navegar por toda la aplicación usando exclusivamente el teclado, documentando cada barrera encontrada: elementos no alcanzables con Tab, elementos que no se activan con Enter o Space, modales que no se cierran con Escape, trampas de teclado en componentes, orden de foco ilógico al abrir modales, foco que se pierde tras acciones dinámicas. Para cada barrera, propondrán e implementarán una solución. Tras implementar todas las soluciones, repetirán la navegación completa por teclado para verificar que ya no existen barreras.

### Actividad Guiada 3: Pruebas con Lector de Pantalla NVDA

Si el aula dispone de equipos con Windows, el alumnado instalará NVDA (lector de pantalla gratuito) y aprenderá los comandos básicos: tecla NVDA (Insert o Bloq Mayús) para iniciar/detener lectura, H para saltar entre encabezados, K para saltar entre enlaces, F para saltar entre formularios, T para saltar entre tablas. Aplicarán estos comandos a la aplicación que están desarrollando y documentarán su experiencia: ¿se anuncia correctamente el rol de cada elemento?, ¿los textos alternativos tienen sentido?, ¿la estructura de encabezados facilita la navegación?, ¿los formularios indican sus etiquetas y errores? Si el aula usa macOS, se utilizará VoiceOver (Cmd+F5) con sus comandos equivalentes (VO+Comando+H para encabezados, VO+Comando+L para enlaces, etc.). El entregable será un informe de experiencia de usuario con lector de pantalla que incluya los 5 problemas más graves encontrados y las soluciones implementadas.

## Actividades propuestas

### Actividad Propuesta 1: Auditoría WCAG Nivel AA

Selecciona tres aplicaciones web que utilices habitualmente (por ejemplo, la plataforma educativa del instituto, tu banco online y una red social) y realiza una **auditoría de accesibilidad** de cada una utilizando al menos tres herramientas diferentes (Lighthouse, [WAVE](https://wave.webaim.org/) y [axe DevTools](https://chromewebstore.google.com/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd?pli=1). Para cada aplicación, documenta los errores encontrados, clasifícalos por principio POUR y nivel WCAG, y elabora un cuadro comparativo de las tres aplicaciones. Incluye capturas de pantalla de los informes y reflexiona sobre qué aplicación es más accesible y por qué.

### Actividad Propuesta 2: Implementación de Componentes Accesibles

Desarrolla desde cero una pequeña **librería de 5 componentes Angular accesibles** con Tailwind CSS: botón (con variantes primary, secondary, ghost, y estados disabled, loading), modal (con gestión de foco, Escape, y retorno de foco), pestañas (tabs con navegación por flechas), menú desplegable (con teclado, aria-expanded, y role menu) y tabla de datos (con navegación por teclado en las filas). Cada componente debe incluir tests automatizados con axe-core que verifiquen su accesibilidad. Documenta cada componente con su lista de características de accesibilidad implementadas.

### Actividad Propuesta 3: Simulación de Discapacidad

Durante un día completo de trabajo práctico, utiliza una simulación de discapacidad para realizar las tareas de desarrollo. Opciones: venda en los ojos + lector de pantalla (discapacidad visual), tapones en los oídos + subtítulos automáticos (discapacidad auditiva), guantes gruesos + navegación solo por teclado (discapacidad motriz), o desactivación de imágenes y CSS en el navegador (discapacidad cognitiva/sensorial). Documenta tu experiencia en un diario de accesibilidad: qué tareas fueron más difíciles, qué barreras encontraste en las herramientas de desarrollo, cómo afectó a tu productividad, y qué cambios implementarías en las aplicaciones que utilizas.

### Actividad Propuesta 4: Comparativa Angular Material vs Tailwind en Accesibilidad

Desarrolla el mismo componente (un formulario de búsqueda con filtros, tabla de resultados y paginación) en dos versiones: una usando Angular Material (que incluye accesibilidad integrada) y otra usando Tailwind CSS con Angular CDK (que requiere implementar la accesibilidad manualmente). Audita ambas versiones con las mismas herramientas (Lighthouse, WAVE, axe DevTools) y compáralas en términos de accesibilidad obtenida, esfuerzo de implementación, y flexibilidad de diseño. Presenta conclusiones sobre cuándo conviene usar cada enfoque.

### Actividad Propuesta 5: Plan de Accesibilidad para un Proyecto Real

Elabora un plan de accesibilidad completo para un proyecto de aplicación de gestión que estés desarrollando o que tengas previsto desarrollar. El plan debe incluir: análisis de requisitos legales aplicables (normativa europea, española y autonómica), nivel de conformidad objetivo (justificando por qué A, AA o AAA), inventario de páginas y componentes a auditar, calendario de auditorías (inicial, intermedias, final), herramientas y metodología de evaluación, criterios de aceptación para cada nivel WCAG, proceso de corrección y verificación, plan de formación del equipo en accesibilidad, y declaración de accesibilidad para publicar en la aplicación. Este plan debe ser lo suficientemente concreto como para ser ejecutado en un proyecto real.

??? "Actividades de ampliación"

    ### Actividad de Ampliación 1: Accesibilidad en Aplicaciones de Escritorio con Electron

    Investiga y documenta las particularidades de la accesibilidad en aplicaciones de escritorio desarrolladas con **Electron** (que encapsulan una aplicación Angular). Explora cómo Electron expone la accesibilidad al sistema operativo (API de accesibilidad de Windows, macOS y Linux), cómo configurar `webPreferences` para optimizar la accesibilidad, qué herramientas permiten auditar aplicaciones Electron de escritorio (Accessibility Insights for Windows, Accessibility Inspector de macOS), y cómo probar con tecnologías asistivas del sistema operativo. Desarrolla una pequeña aplicación Electron con Angular que incluya características de accesibilidad y documenta el proceso.

    ### Actividad de Ampliación 2: Tests Automatizados de Accesibilidad en CI/CD

    Configura un pipeline de integración continua que ejecute tests automatizados de accesibilidad con **axe-core** en cada pull request, bloqueando la fusión si se introducen nuevas violaciones. Investiga cómo integrar **pa11y** (otra herramienta de testing de accesibilidad) o cypress-axe (plugin de accesibilidad para Cypress) en el proceso de CI/CD. Documenta la configuración, escribe ejemplos de tests de accesibilidad para varios componentes, y demuestra cómo el pipeline detecta una regresión de accesibilidad introducida deliberadamente.

    ### Actividad de Ampliación 3: Estudio Comparativo de WCAG 2.2 y Preparación para WCAG 3.0

    Investiga las novedades introducidas en **WCAG 2.2** (publicada en octubre de 2023) respecto a WCAG 2.1. Identifica los nuevos criterios de conformidad, explica su propósito y proporciona ejemplos de implementación en Angular para cada uno. A continuación, investiga el borrador de trabajo de **WCAG 3.0** y sus diferencias fundamentales con la versión 2.x: el cambio de criterios binarios a puntuaciones graduales (Bronze, Silver, Gold), la introducción de pruebas de usabilidad como parte de la conformidad, y las nuevas categorías de discapacidad cubiertas. Elabora un informe técnico que oriente a un equipo de desarrollo sobre cómo prepararse para la futura transición a WCAG 3.0.

!!! tip "Buenas prácticas"

    1. Empieza con **HTML semántico**. Antes de pensar en ARIA, pregúntate si puedes usar el elemento HTML correcto para lo que estás construyendo. `<button>` para acciones, `<a>` para navegación, `<nav>` para menús, `<main>` para contenido principal, `<form>` con `<label>` para formularios.

    2. No elimines el outline del foco sin reemplazarlo. Si el estilo por defecto del navegador no encaja con el diseño, utiliza `:focus-visible` con un anillo visible (`ring-2 ring-offset-2`) en lugar de `outline: none`. Usa `focus:outline-none focus-visible:ring-2` en Tailwind.

    3. Verifica el **contraste** de cada combinación de colores que crees. No confíes en que "parece legible". Utiliza un comprobador de contraste como WebAIM o la extensión axe DevTools. Asegura 4.5:1 para texto normal y 3:1 para texto grande.

    4. Navega por tu aplicación sin ratón cada día. Convierte esto en un hábito de desarrollo: antes de dar por terminada una funcionalidad, recórrela completamente con el teclado. Esta práctica de 30 segundos detecta la mayoría de los problemas de accesibilidad.

    5. Proporciona **textos alternativos** significativos. No escribas `alt="imagen"` ni `alt="foto"`. Describe la información que transmite la imagen. Si la imagen es decorativa, usa `alt=""`. Si contiene texto, el texto debe estar en el `alt` o (mejor) no uses imágenes para texto.

    6. Usa `aria-live` para cambios dinámicos importantes. Cualquier cambio en la interfaz que no sea directamente causado por la acción de la persona usuaria (carga asíncrona de datos, notificaciones push, temporizadores) debe anunciarse mediante una live region.

    7. Asocia los mensajes de error a sus campos mediante `aria-describedby`. No basta con mostrar el error visualmente cerca del campo; debe estar programáticamente vinculado para que el lector de pantalla lo anuncie cuando el campo recibe el foco.

    8. Prueba con un **lector de pantalla** real al menos una vez al mes. Dedica 15 minutos a navegar por tu aplicación con NVDA (Windows) o VoiceOver (Mac) sin mirar la pantalla. Anota los problemas y corrígelos antes de que lleguen a producción.

    9. Configura las reglas de accesibilidad de ESLint como errores, no como advertencias. Si el equipo es grande, comienza con las reglas más básicas (alt-text, label-has-associated-control, valid-aria) y ve añadiendo más progresivamente.

    10. Documenta la accesibilidad de tu aplicación con una declaración de accesibilidad pública, indicando el nivel de conformidad alcanzado, los criterios que no se cumplen (si los hay), los mecanismos de contacto para reportar problemas, y la fecha de la última revisión.

!!! warning "Errores frecuentes"

    1. Usar **ARIA** cuando HTML ya proporciona la semántica necesaria. Añadir `role="button"` a un `<button>` o `role="navigation"` a un `<nav>` es redundante y potencialmente confuso. Menos ARIA bien aplicada es mejor que mucha ARIA redundante.

    2. Eliminar el outline del foco sin proporcionar alternativa. `*:focus { outline: none; }` es una de las declaraciones CSS más dañinas para la accesibilidad. Si realmente necesitas eliminarlo, debes implementar un indicador de foco alternativo visible y estilizado.

    3. Usar placeholders como sustituto de etiquetas. El placeholder desaparece cuando el campo tiene contenido, dejando a la persona usuaria sin referencia. Las etiquetas deben estar siempre visibles y correctamente asociadas al campo con `for`/`id`.

    4. No marcar los **campos obligatorios** de formulario. Tanto visualmente (asterisco + leyenda explicativa) como programáticamente (`required` y `aria-required`). No asumas que la persona usuaria adivinará qué campos son obligatorios.

    5. Usar solo **color** para transmitir información de estado. Un borde rojo en un campo erróneo debe acompañarse de un icono, un texto descriptivo y el atributo `aria-invalid`. Una fila coloreada en una tabla debe incluir una columna de estado textual.

    6. Crear componentes interactivos con `<div>` y `<span>` en lugar de elementos nativos. "Es que el botón nativo no me deja estilizarlo como quiero" no es excusa: un `<button>` con Tailwind puede tener cualquier apariencia y es accesible sin esfuerzo adicional.

    7. No gestionar el foco en aplicaciones de una sola página (**SPA**). Cuando la ruta cambia en Angular, el foco se queda donde estaba (a menudo en la URL del navegador). Tras la navegación, el foco debe moverse al inicio del contenido principal o al `<h1>` de la nueva página.

    8. Ignorar el **zoom de página**. Probar siempre al 100% de zoom es insuficiente. La aplicación debe funcionar correctamente con zoom al 200%: sin solapamientos, sin contenido cortado, sin necesidad de scroll horizontal.

    9. No proporcionar subtítulos o transcripciones en contenido multimedia. Si la aplicación incluye vídeos, webinars o contenido de audio, deben tener subtítulos y transcripciones. No asumas que todas las personas usuarias pueden oír.

    10. Asumir que una puntuación Lighthouse de 100 significa que la aplicación es completamente accesible. Lighthouse solo verifica criterios programáticos. La verdadera accesibilidad se valida con pruebas manuales y con personas usuarias reales que utilizan tecnologías asistivas.

!!! abstract "Resumen"

    Esta unidad ha establecido los fundamentos de la accesibilidad web como una responsabilidad ineludible del desarrollador de interfaces. Se ha partido de la definición y la importancia de la accesibilidad, abarcando los distintos tipos de discapacidad (visual, auditiva, motriz, cognitiva) y las barreras que las interfaces inaccesibles crean para cada colectivo. Se ha contextualizado el marco legal, con la normativa europea y española que exige el cumplimiento del nivel AA de las WCAG para un número creciente de aplicaciones.

    Las WCAG, organizadas en los cuatro principios **POUR** (Perceptible, Operable, Comprensible y Robusto), proporcionan el estándar técnico de referencia. Cada principio se ha desarrollado en detalle, con ejemplos concretos de implementación en Angular y Tailwind CSS, cubriendo desde el texto alternativo y la estructura semántica hasta la navegación por teclado, el contraste de color, la gestión del foco y la ayuda en formularios.

    **ARIA** se ha presentado como el complemento a HTML semántico, con su regla de oro fundamental: "No uses ARIA si HTML ya lo resuelve". Se han detallado los roles, propiedades, estados y regiones en vivo más relevantes para aplicaciones de gestión, junto con las herramientas del ecosistema Angular (Angular CDK, Angular ESLint) que facilitan su implementación.

    Las herramientas de evaluación (Lighthouse, WAVE, axe DevTools, lectores de pantalla) constituyen el arsenal del desarrollador para verificar la accesibilidad, combinando auditorías automáticas con pruebas manuales para cubrir el espectro completo de criterios WCAG. La **checklist de accesibilidad** para desarrollo proporciona un procedimiento sistemático para integrar estas verificaciones en el ciclo de desarrollo diario.

    El mensaje central de esta unidad es doble: la accesibilidad no es una característica adicional ni un cumplimiento burocrático, sino una dimensión fundamental de la calidad del software; y ==la accesibilidad no se logra al final del proyecto, mediante una auditoría correctiva, sino desde el inicio==, mediante prácticas de desarrollo que integran la accesibilidad en cada decisión de diseño y en cada línea de código.

## Recursos complementarios

### Normativa y estándares
- WCAG 2.2 (W3C): https://www.w3.org/TR/WCAG22/
- WCAG 2.1 Quick Reference: https://www.w3.org/WAI/WCAG21/quickref/
- Understanding WCAG 2.2: https://www.w3.org/WAI/WCAG22/Understanding/
- Directiva Europea 2016/2102: https://eur-lex.europa.eu/eli/dir/2016/2102/oj
- Real Decreto 1112/2018: https://www.boe.es/eli/es/rd/2018/09/07/1112
- EN 301 549: Norma europea armonizada de accesibilidad TIC

### Guías y tutoriales
- Web Accessibility Initiative (WAI) del W3C: https://www.w3.org/WAI/
- ARIA Authoring Practices Guide (W3C): https://www.w3.org/WAI/ARIA/apg/
- MDN Web Docs - Accesibilidad: https://developer.mozilla.org/es/docs/Learn/Accessibility
- A11y Project: https://www.a11yproject.com
- Angular CDK A11y documentation: https://material.angular.io/cdk/a11y/overview
- WebAIM: Contrast Checker y artículos: https://webaim.org

### Herramientas de evaluación
- Lighthouse (integrado en Chrome DevTools)
- WAVE: https://wave.webaim.org
- axe DevTools: https://www.deque.com/axe/devtools/
- axe-core (npm): https://www.npmjs.com/package/axe-core
- Accessibility Insights: https://accessibilityinsights.io
- NVDA (lector de pantalla gratuito para Windows): https://www.nvaccess.org
- VoiceOver (integrado en macOS): https://www.apple.com/accessibility/voiceover/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- W3C HTML Validator: https://validator.w3.org/nu/

### Comunidades y formación
- Fundación ONCE - Accesibilidad: https://www.fundaciononce.es
- W3C WAI Curricula: https://www.w3.org/WAI/curricula/
- Deque University (cursos de accesibilidad): https://dequeuniversity.com
- A11ycasts (Google Chrome Developers): https://www.youtube.com/playlist?list=PLNYkxOF6rcICWx0C9LVWWVqvHlYJyqw7g
