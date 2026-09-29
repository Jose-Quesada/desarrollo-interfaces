---
icon: lucide/monitor-smartphone
---

# Responsive Design en Aplicaciones Angular

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Comprender y aplicar el enfoque Mobile First en el contexto de aplicaciones de escritorio y web empresariales, diferenciando conceptualmente entre "adaptarse a móviles" y "diseñar desde la restricción", y reconociendo cómo este cambio de mentalidad mejora la calidad del diseño en todos los tamaños.
2. Dominar el sistema de breakpoints de Tailwind CSS (`sm`, `md`, `lg`, `xl`, `2xl`) aplicado a interfaces de aplicación de gestión, comprendiendo cómo las variantes responsive se integran con las clases utility para crear layouts adaptables sin media queries explícitas ni archivos CSS adicionales.
3. Aplicar estrategias responsive específicas para cada componente de una aplicación de gestión: sidebar colapsable con overlay en móvil, tablas con scroll horizontal y columnas adaptativas, dashboards con grid responsive de 1 a 4 columnas, formularios con campos apilados en móvil y en columnas en desktop, modales fullscreen en móvil y centrados en desktop, y patrones de navegación adaptados al dispositivo.
4. Utilizar `BreakpointObserver` de Angular CDK para implementar lógica condicional basada en el tamaño de la pantalla en TypeScript, convirtiendo observables a señales para integración fluida con el nuevo modelo de reactividad de Angular, y diferenciando los casos donde la lógica responsive debe estar en TypeScript de aquellos donde las clases de Tailwind son suficientes.
5. Diseñar y construir un dashboard completamente responsive como proyecto integrador, que funcione correctamente en tres rangos de dispositivos (móvil, tablet y desktop), con comportamientos diferenciados en cada rango para la navegación, el layout, la visualización de datos y la interacción.
6. Comprender las particularidades del diseño responsive en aplicaciones de escritorio con Electron, donde la ventana de la aplicación puede redimensionarse desde tamaños muy reducidos hasta resoluciones 4K, y aplicar estrategias de layout fluido y breakpoints adaptados a este contexto.
7. Evaluar la calidad responsive de aplicaciones profesionales reales (Notion, Linear, VS Code web) mediante análisis sistemático de sus estrategias de adaptación, extrayendo patrones aplicables a los proyectos propios del alumnado.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 4** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 4.** Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE e) Se han distribuido adecuadamente los controles en la interfaz de usuario.
- CE f) Se ha utilizado el tipo de control más apropiado en cada caso.
- CE g) Se ha diseñado el aspecto de la interfaz de usuario (colores y fuentes entre otros) atendiendo a su legibilidad.

> Nota: el diseño responsive (mobile-first, breakpoints, container queries y detección programática en Angular) es la técnica con la que se garantiza la distribución adecuada de los controles y la legibilidad en cualquier dispositivo.
> Aclaración normativa: no debe confundirse con el **RA 2** del módulo («Genera interfaces naturales de usuario»), que corresponde a interfaces basadas en voz, movimiento corporal o realidad aumentada y se trata en la Unidad 3.

!!! note "Conocimientos previos"

    Para abordar esta unidad con éxito, el alumnado debe dominar los siguientes conocimientos:

    - Fundamentos sólidos de CSS responsive: media queries, unidades relativas (rem, em, %, vw, vh, dvh), flexbox y CSS grid aplicados a layouts adaptables, y comprensión del modelo mobile-first frente al modelo desktop-first.
    - Dominio de Tailwind CSS 4 (Unidades 6 y 7): sistema de breakpoints, variantes responsive (`sm:`, `md:`, `lg:`, `xl:`, `2xl:`), clases de layout responsivas (`grid-cols-1 md:grid-cols-2`, `flex-col md:flex-row`), y la filosofía mobile-first del framework.
    - Conocimientos intermedios de Angular: creación de componentes standalone, señales (signals), inyección de dependencias, RxJS y observables, y el uso de `toSignal` del paquete `@angular/core/rxjs-interop` para convertir observables a señales.
    - Experiencia en la implementación de componentes de interfaz con Angular y Tailwind (Unidad 7), ya que esta unidad aplica responsive design sobre los componentes ya construidos.
    - Conocimientos de UX (Unidad 1) y accesibilidad (Unidad 2), necesarios para garantizar que la adaptación responsive no comprometa la usabilidad ni la accesibilidad en ningún tamaño de pantalla.

## Contenidos

1. Mobile First en aplicaciones de escritorio
2. Breakpoints con Tailwind aplicados a interfaces de aplicación
3. Estrategias responsive para aplicaciones (no webs)
4. Técnicas responsive con Tailwind
5. Detección de dispositivo en Angular (BreakpointObserver)
6. Responsive en Electron (aplicaciones de escritorio)
7. Proyecto de la unidad: Dashboard completamente responsive

## Desarrollo teórico

### 1. Mobile First en Aplicaciones de Escritorio

El concepto de **Mobile First** ha sido adoptado por la comunidad de diseño web desde que Luke Wroblewski lo popularizara en 2009, pero a menudo se malinterpreta en el contexto de las aplicaciones de gestión empresarial. Mobile First no significa "diseñar solo para móviles", ni "priorizar los dispositivos móviles sobre el escritorio", ni "sacrificar funcionalidad de escritorio para que funcione en móvil". Significa empezar el proceso de diseño por la vista más restrictiva (la pantalla pequeña del teléfono móvil) y añadir progresivamente complejidad a medida que el espacio disponible aumenta hacia tablet y desktop.

Este enfoque tiene una justificación sólida basada en la restricción como herramienta creativa. Cuando se diseña para una pantalla de 1920 píxeles de ancho, todo cabe. El resultado suele ser una interfaz sobrecargada donde cada pixel disponible se rellena con información, menús, barras laterales, widgets y atajos. Cuando luego se intenta adaptar esta misma interfaz a una pantalla de 375 píxeles (un teléfono móvil típico), las decisiones ya están tomadas y la adaptación se convierte en un proceso de recorte doloroso: ¿qué elementos eliminamos?, ¿qué información dejamos de mostrar?, ¿cómo reorganizamos lo que queda? Este recorte, forzado por la falta de espacio, suele revelar que muchos de los elementos de la versión desktop eran superfluos o estaban mal priorizados.

El enfoque Mobile First invierte este proceso. Empezar por el móvil obliga a tomar decisiones difíciles desde el principio: ¿cuál es la información esencial que la persona usuaria necesita ver?, ¿cuál es la acción principal que debe estar disponible en todo momento?, ¿cómo organizamos el contenido con el mínimo espacio posible? Estas decisiones, guiadas por la restricción, producen una interfaz más clara, más enfocada y con mejor jerarquía visual. Luego, al expandir el diseño hacia tablet y desktop, se añade información complementaria, se amplían los espacios y se habilitan funcionalidades avanzadas. Pero el núcleo de la experiencia, definido en la restricción, permanece sólido y coherente en todos los tamaños.

Para el alumnado de DAM, acostumbrado a pensar en aplicaciones de gestión que "solo se usan en la oficina con un monitor grande", este cambio de mentalidad es particularmente importante. La realidad del mercado laboral actual es que muchas aplicaciones de gestión se utilizan desde múltiples dispositivos. El comercial que visita clientes consulta el catálogo desde su tablet. El encargado de almacén confirma recepción de mercancía desde su teléfono móvil. El administrativo trabaja con la aplicación completa desde su monitor de 24 pulgadas en la oficina. Todos utilizan la misma aplicación, y todos merecen una experiencia de calidad adaptada a su dispositivo.

Mobile First también favorece la accesibilidad. Una interfaz diseñada para funcionar en pantallas pequeñas suele tener mejor contraste, tipografía más grande, menos densidad de información, espacios interactivos más amplios (necesarios para dedos en pantalla táctil) y navegación más simplificada. Todas estas características benefician también a personas con discapacidad visual, motriz o cognitiva que acceden desde desktop. Diseñar para la restricción mejora la experiencia para todas las personas.

### 2. Breakpoints con Tailwind Aplicados a Interfaces de Aplicación

Tailwind CSS adopta el enfoque Mobile First en su sistema de **breakpoints**. Las clases sin prefijo se aplican a todos los tamaños de pantalla (desde el más pequeño). Las clases con prefijo (`sm:`, `md:`, `lg:`, `xl:`, `2xl:`) se aplican a partir del breakpoint indicado hacia arriba. Esto significa que el diseño base que escribimos es el diseño móvil, y las variantes responsive lo van enriqueciendo para pantallas más grandes.

Los breakpoints por defecto de Tailwind son: `sm` a 640 píxeles (típicamente tablet pequeña en orientación vertical, o teléfono grande en horizontal), `md` a 768 píxeles (tablet estándar en vertical, tablet pequeña en horizontal, o ventana de navegador reducida), `lg` a 1024 píxeles (tablet grande en horizontal, portátil pequeño, o ventana de navegador con sidebar visible), `xl` a 1280 píxeles (portátil estándar, monitor de escritorio pequeño), y `2xl` a 1536 píxeles (monitor de escritorio grande, pantalla externa de alta resolución). Estos breakpoints, aunque se definieron para el diseño web general, se aplican perfectamente a aplicaciones de gestión, con la particularidad de que los anchos típicos de las aplicaciones de escritorio suelen moverse en los rangos `lg` y `xl`.

Los breakpoints pueden personalizarse en `@theme` si el proyecto requiere puntos de ruptura diferentes. Por ejemplo, una aplicación de gestión con una sidebar de 280px podría necesitar un breakpoint adicional o ajustar los existentes para que la transición entre "sidebar oculta" y "sidebar visible" ocurra en el punto óptimo. La personalización se realiza añadiendo tokens de breakpoint al bloque `@theme`:

```css
@theme {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;
  --breakpoint-app: 960px;
}
```

La estrategia de aplicación de breakpoints en interfaces de aplicación difiere de la del diseño web de marketing. En una web promocional, los breakpoints se utilizan para reorganizar secciones completas, cambiar tipografías drásticamente y adaptar imágenes de fondo. En una aplicación de gestión, los breakpoints se utilizan para ajustar el layout de la zona de trabajo: cuándo mostrar u ocultar la sidebar, cómo reorganizar los widgets del dashboard, cómo adaptar las tablas de datos, y cómo disponer los campos de los formularios. La aplicación de gestión no cambia su identidad visual entre breakpoints; optimiza el uso del espacio disponible.

Un concepto fundamental que el alumnado debe interiorizar es que los breakpoints no representan dispositivos concretos, sino rangos de espacio disponible. No se diseña para "iPhone" o "iPad" o "monitor Dell de 24 pulgadas". Se diseña para "pantallas menores de 640px de ancho", "pantallas entre 640px y 768px", y así sucesivamente. Esta abstracción permite que el diseño funcione correctamente en cualquier dispositivo presente y futuro, incluidos aquellos que no existían cuando se escribió el código.

### 3. Estrategias Responsive para Aplicaciones

Cada componente de una aplicación de gestión requiere una estrategia responsive específica, basada en su función y en la información que presenta. A continuación se detallan las estrategias para los componentes más comunes.

La sidebar de navegación es probablemente el elemento que más transformación sufre entre breakpoints. En móvil, el espacio es insuficiente para mantener una sidebar visible permanentemente; la estrategia es ocultarla completamente y mostrarla como un drawer que se abre con overlay al pulsar un botón hamburguesa. El overlay oscurece el contenido principal y captura la interacción, cerrando la sidebar al hacer clic fuera de ella o al seleccionar una opción de navegación. En tablet, la sidebar puede mostrarse colapsada (solo iconos, ancho de 64px), liberando espacio para el contenido pero manteniendo la navegación accesible sin gestos adicionales. En desktop, la sidebar se expande completamente (ancho de 256px), mostrando iconos y texto, y convirtiéndose en el sistema de navegación principal.

La transición entre estos tres estados no es binaria (abierta/cerrada) sino gradual, y se implementa con las variantes responsive de Tailwind. La sidebar tiene clases base para móvil (`fixed inset-y-0 left-0 z-40 w-64 transform -translate-x-full transition-transform duration-300`) que la ocultan fuera de la pantalla. En tablet (`md:relative md:translate-x-0 md:w-16`) se muestra colapsada en el flujo del layout. En desktop (`lg:w-64`) se expande completamente. Un servicio de estado o una señal controla si la sidebar móvil está abierta (se añade la clase `translate-x-0` mediante binding condicional). El overlay se muestra solo en móvil con `md:hidden`.

Las tablas de datos presentan un desafío responsive particular porque la información tabular es inherentemente bidimensional y no se reorganiza fácilmente en una sola columna. La estrategia más común y efectiva para aplicaciones de gestión es el scroll horizontal en pantallas pequeñas. La tabla se envuelve en un contenedor con `overflow-x-auto` y `rounded-lg border`, y la tabla interior recibe un ancho mínimo (`min-w-[800px]` o superior) que fuerza el scroll cuando el **viewport** es más estrecho. En pantallas grandes, la tabla ocupa el ancho disponible sin scroll.

Esta estrategia de scroll horizontal puede complementarse con la ocultación progresiva de columnas. Las columnas menos esenciales (como fechas de creación, IDs internos, o metadatos administrativos) se ocultan en breakpoints pequeños usando `hidden md:table-cell`. En móvil, se muestran solo las 2-3 columnas más importantes (nombre, acción principal). En tablet, se añaden 2-3 columnas más. En desktop, se muestran todas las columnas. Esta ocultación progresiva, combinada con el scroll horizontal, garantiza que la tabla sea utilizable en todos los tamaños sin perder su naturaleza tabular.

Los dashboards son grids de widgets cuyo número de columnas debe adaptarse al espacio disponible. La regla general es: 1 columna en móvil (<640px), 2 columnas en tablet (640px-1024px), 3 columnas en desktop pequeño (1024px-1280px), y 4 columnas en desktop grande (>1280px). Con Tailwind, esto se expresa en una sola línea: `grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6`. Los widgets individuales no cambian de diseño (una card de estadística se ve igual en móvil que en desktop), pero su disposición en el grid se adapta fluidamente.

Los formularios en aplicaciones de gestión tienden a ser largos (muchos campos) y se benefician de múltiples columnas en pantallas grandes para reducir el scroll vertical y agrupar campos relacionados visualmente. En móvil, los campos se apilan en una sola columna (`flex flex-col gap-4`). En desktop, se distribuyen en dos columnas (`md:grid md:grid-cols-2 md:gap-6`), con algunos campos que ocupan el ancho completo (`md:col-span-2`) cuando contienen información extensa como direcciones o descripciones. La clave es que la estructura de columnas sea semántica: campos relacionados deben aparecer en la misma fila o en filas adyacentes, no distribuidos arbitrariamente.

Los modales en pantallas pequeñas deben ocupar la pantalla completa para ser utilizables, ya que un modal pequeño en una pantalla ya pequeña resulta incómodo. En móvil, un modal es fullscreen: `fixed inset-0 z-50` sin márgenes, con `rounded-none` (sin bordes redondeados) y ocupando el 100% del viewport. En desktop, el modal se centra y se limita en tamaño: `fixed inset-0 z-50 flex items-center justify-center p-4`, con la tarjeta interior teniendo `max-w-lg w-full rounded-2xl`. Esta transición se implementa con las variantes responsive de Tailwind.

La navegación sufre el cambio más radical entre dispositivos. En móvil, el patrón óptimo es la barra de navegación inferior fija (bottom tab bar), con 3-5 iconos que representan las secciones principales de la aplicación. Este patrón, popularizado por las aplicaciones nativas móviles, sitúa las opciones de navegación al alcance del pulgar, en la zona más accesible de la pantalla. En tablet y desktop, la navegación migra a una sidebar lateral, liberando la barra inferior y aprovechando mejor el espacio horizontal. La implementación con Tailwind usa `fixed bottom-0 inset-x-0 md:hidden` para la barra inferior móvil, y `hidden md:flex` para la sidebar de escritorio.

### 4. Técnicas Responsive con Tailwind

Más allá de las estrategias por componente, Tailwind proporciona un arsenal de técnicas responsive que todo desarrollador de interfaces debe dominar. La más fundamental es el grid responsive, que permite cambiar el número de columnas, el tamaño de las columnas y el gap entre breakpoints. Un ejemplo canónico: `grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 md:gap-6`. Las columnas, el gap y cualquier otra propiedad del grid pueden variar independientemente por breakpoint.

Flexbox responsive es igualmente potente. La dirección del flex puede cambiar de columna a fila: `flex flex-col md:flex-row`. Esto es ideal para layouts de detalle donde en móvil la imagen o el resumen va arriba y las acciones abajo, pero en desktop van en columnas paralelas. El wrap también puede controlarse: `flex-wrap` en móvil para que los items pasen a la siguiente línea si no caben, `md:flex-nowrap` en desktop para mantenerlos en una sola línea.

Ocultar y mostrar elementos según el breakpoint es una de las técnicas más utilizadas. Las combinaciones típicas son `hidden md:block` (oculto en móvil, visible desde tablet) y `block md:hidden` (visible en móvil, oculto desde tablet). Estas clases son la base de patrones como "elemento diferente en móvil y desktop" o "contenido simplificado en móvil, completo en desktop".

El tamaño de los textos debe adaptarse al dispositivo de lectura. En pantallas pequeñas, vistas de cerca (30-40 cm), los textos pueden ser más pequeños. En pantallas grandes, vistas de lejos (50-70 cm), o en monitores de alta resolución, los textos deben ser proporcionalmente mayores. Tailwind permite variar el tamaño de texto por breakpoint: `text-sm md:text-base lg:text-lg`. Lo mismo aplica al espaciado: `p-4 md:p-6 lg:p-8`. Las interfaces de aplicación se benefician de un espaciado generoso en desktop (donde sobra espacio) y un espaciado contenido pero suficiente en móvil (donde el espacio escasea).

Las imágenes y los medios requieren atención responsive. Las imágenes dentro de cards o listados deben usar `w-full h-48 object-cover` para mantener la proporción. En grid de imágenes con Tailwind, `grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-1` crea una galería adaptable. La propiedad `aspect-ratio` (clases `aspect-video`, `aspect-square`, o valores arbitrarios `aspect-[16/9]`) asegura que los contenedores de medios mantengan su proporción en cualquier ancho. `max-w-full` y `h-auto` evitan que las imágenes desborden su contenedor.

### 5. Detección de Dispositivo en Angular (BreakpointObserver)

Las clases responsive de Tailwind cubren la mayoría de necesidades de adaptación visual. Sin embargo, hay situaciones donde la adaptación requiere lógica en TypeScript: cargar datos diferentes según el dispositivo, inicializar o destruir funcionalidades completas (como un editor de arrastrar y soltar que no tiene sentido en móvil), o modificar el comportamiento de navegación. Para estos casos, Angular CDK proporciona `BreakpointObserver`.

`BreakpointObserver` es un servicio inyectable que permite suscribirse a cambios en breakpoints definidos por **media queries** CSS. No depende de Tailwind; trabaja directamente con el `matchMedia` del navegador. Para utilizarlo, se importa `LayoutModule` de `@angular/cdk/layout` en el componente o en la configuración de la aplicación. El servicio expone el método `observe(breakpoints: string | string[])` que devuelve un `Observable<BreakpointState>` con un mapa de los breakpoints observados y si cada uno coincide actualmente.

Un caso de uso típico en aplicaciones de gestión es abrir o cerrar automáticamente la sidebar al cruzar un breakpoint. En móvil, la sidebar comienza cerrada. Cuando la ventana se redimensiona y cruza el breakpoint `lg` (1024px), la sidebar debería abrirse automáticamente porque hay espacio suficiente. Cuando la ventana se reduce por debajo de `lg`, la sidebar debería cerrarse y pasar a modo overlay. Esta lógica se implementa con `BreakpointObserver`:

```typescript
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { toSignal } from '@angular/core/rxjs-interop';

@Component({ ... })
export class SidebarService {
  private breakpointObserver = inject(BreakpointObserver);
  
  readonly isDesktop = toSignal(
    this.breakpointObserver.observe([Breakpoints.Large, Breakpoints.XLarge])
      .pipe(map(state => state.matches)),
    { initialValue: false }
  );
  
  readonly isMobile = toSignal(
    this.breakpointObserver.observe(['(max-width: 639px)'])
      .pipe(map(state => state.matches)),
    { initialValue: true }
  );
}
```

En Angular 17 y superior, `toSignal` del paquete `@angular/core/rxjs-interop` convierte el observable de `BreakpointObserver` en una señal, integrándose limpiamente con el nuevo modelo de reactividad. La señal `isDesktop` se actualiza automáticamente cuando la ventana cruza el breakpoint, y los componentes que la consumen se re-renderizan de forma eficiente y predecible.

Es importante usar `BreakpointObserver` con moderación. La regla práctica es: si la adaptación es puramente visual (cambiar clases, mostrar/ocultar elementos), usa las variantes responsive de Tailwind. Si la adaptación requiere cambiar lógica de negocio (inicializar o destruir servicios, cambiar el comportamiento de navegación, decidir qué datos cargar), usa `BreakpointObserver`. Esta separación mantiene la lógica de presentación en la capa de estilos (Tailwind) y la lógica de negocio en la capa de TypeScript (Angular), respetando el principio de separación de responsabilidades.

### 6. Responsive en Electron (Aplicaciones de Escritorio)

Electron es un framework que permite construir aplicaciones de escritorio multiplataforma utilizando tecnologías web (HTML, CSS, JavaScript/TypeScript). La aplicación Angular se ejecuta dentro de un proceso renderizador de Chromium, en una ventana nativa del sistema operativo. Esta arquitectura introduce consideraciones de responsive design que no existen en la web.

La ventana de una aplicación Electron puede ser redimensionada por la persona usuaria arrastrando sus bordes, igual que cualquier otra ventana del sistema operativo. La aplicación debe responder a estos cambios de tamaño, reconfigurando su layout para funcionar correctamente desde el tamaño mínimo hasta el tamaño máximo. A diferencia de una aplicación web, donde los anchos disponibles tienen un rango conocido (típicamente 375px a 2560px), una ventana de Electron puede tener cualquier tamaño, incluyendo tamaños extremadamente pequeños (300x200 píxeles) o enormes (múltiples monitores 4K).

Para gestionar esto, la aplicación Electron define tamaños mínimos de ventana en el proceso principal mediante las opciones `minWidth` y `minHeight` del constructor `BrowserWindow`. Por ejemplo, `minWidth: 800, minHeight: 600` establece que la ventana no puede reducirse por debajo de ese tamaño. El tamaño mínimo debe elegirse cuidadosamente: demasiado grande frustra a personas que quieren usar la aplicación en pantalla dividida; demasiado pequeño resulta en interfaces rotas o ilegibles. Una buena práctica es establecer el tamaño mínimo en el punto donde la interfaz deja de ser funcional, típicamente alrededor de 800x600 para aplicaciones de gestión.

Dentro de la ventana de Electron, la aplicación Angular se comporta como una SPA web normal y utiliza exactamente el mismo código responsive (Tailwind, BreakpointObserver) que la versión web. No hay código específico de Electron para responsive design, más allá de definir el tamaño mínimo de ventana. Esto significa que una aplicación Angular bien diseñada con responsive design funciona tanto en el navegador como en Electron sin modificaciones, lo cual es una ventaja significativa cuando se desarrollan aplicaciones que deben desplegarse en ambos entornos.

Un aspecto específico de Electron es que, al ser una aplicación de escritorio, la persona usuaria espera que funcione bien en modo "maximizado" (ventana que ocupa toda la pantalla) y en modo "ventana normal" (tamaño libre). Los diseños deben contemplar anchos que van desde 800px (ventana pequeña) hasta 2560px o más (pantalla 4K maximizada). Un dashboard con solo 4 widgets en `grid-cols-4` se ve bien a 1280px pero desperdicia espacio a 2560px. Una posible estrategia para pantallas muy grandes es limitar el ancho máximo del contenido con `max-w-screen-2xl mx-auto`, centrando el contenido y dejando márgenes generosos, o aumentar el número de columnas con breakpoints adicionales para 2XL y superiores.

### 7. Proyecto de la Unidad: Dashboard Completamente Responsive

El proyecto integrador de esta unidad consiste en construir un dashboard de aplicación de gestión que funcione correctamente en tres rangos de dispositivos: móvil, tablet y desktop. Este proyecto pone en práctica todas las estrategias y técnicas estudiadas.

En la vista móvil (menos de 768px), la sidebar de navegación está completamente oculta y solo se muestra al pulsar un botón hamburguesa en la esquina superior izquierda de la barra de navegación superior. Al abrirse, un overlay semitransparente cubre el contenido y la sidebar se desliza desde la izquierda como un drawer. La barra de navegación superior contiene el logo o nombre de la aplicación, el botón hamburguesa, y el avatar de la persona usuaria con un menú desplegable. Los widgets de estadísticas se muestran en una sola columna, ocupando todo el ancho disponible. La tabla de datos utiliza scroll horizontal y muestra solo las 3 columnas más importantes (las demás están ocultas con `hidden`). La barra de navegación inferior, fija, contiene 4 iconos con texto pequeño que dan acceso a las secciones principales: Dashboard, Clientes, Productos, Configuración.

En la vista tablet (768px a 1024px), la sidebar se muestra colapsada permanentemente a la izquierda, con ancho de 64px y solo iconos. Al pasar el cursor sobre un icono, se despliega un tooltip con el nombre de la sección. El botón hamburguesa superior desaparece (reemplazado por la sidebar siempre visible). La barra de navegación inferior de móvil desaparece (`md:hidden`). Los widgets se distribuyen en 2 columnas. La tabla muestra 5 columnas (se añaden dos más respecto a móvil). El contenido principal tiene un margen izquierdo igual al ancho de la sidebar colapsada (`ml-16`).

En la vista desktop (más de 1024px), la sidebar se expande completamente a 256px de ancho, mostrando icono y texto para cada sección. Algunas secciones con subsecciones muestran un indicador de expansión (chevron) y al hacer clic despliegan los items hijos con una animación de altura. Los widgets se distribuyen en 3 columnas (lg) o 4 (xl). La tabla muestra todas las columnas disponibles. El contenido principal tiene margen izquierdo `ml-64`. El espacio adicional en pantallas muy anchas se gestiona centrando el contenido o añadiendo más widgets por fila.

El proyecto integra `BreakpointObserver` para la lógica de la sidebar: en móvil, la sidebar se abre y se cierra manualmente; al cruzar a tablet, se abre automáticamente en modo colapsado; al cruzar a desktop, se expande automáticamente. La transición entre estados se anima con `transition-all duration-300` en las clases de Tailwind de la sidebar.

La implementación se organiza en componentes Angular: `DashboardLayout` (layout raíz con sidebar, navbar superior, navbar inferior móvil y zona de contenido), `Sidebar` (con lógica de colapso/expansión y navegación), `Navbar` (barra superior), `MobileNav` (barra inferior móvil), `StatsWidget` (widget de estadística individual), y `DataTable` (tabla de datos responsive). Cada componente utiliza exclusivamente Tailwind para el responsive, y los que requieren lógica condicional por breakpoint inyectan `BreakpointObserver` mediante señales.

## Ejemplos guiados

### Ejemplo Guiado 1: Dashboard para Vista Móvil (< 768px)

En este ejemplo, se construye la vista móvil del dashboard. Se comienza con el layout base: un `<div>` raíz con `min-h-screen bg-gray-50`. La barra de navegación superior es `fixed top-0 inset-x-0 z-30 h-14 bg-white border-b border-gray-200 flex items-center justify-between px-4`. A la izquierda, el botón hamburguesa (tres líneas SVG) con `p-2 rounded-lg hover:bg-gray-100`. En el centro, el nombre de la aplicación con `text-lg font-semibold text-gray-900`. A la derecha, el avatar circular (`w-8 h-8 rounded-full bg-primary-500 text-white flex items-center justify-center text-sm font-medium`) con un menú desplegable que se abre al hacer clic.

El contenido principal comienza después de la barra superior, con `pt-14 pb-16` (padding-top para la barra superior fija, padding-bottom para la barra inferior fija). Los widgets se muestran en una columna: `grid grid-cols-1 gap-4 px-4`. Cada widget es una card con `bg-white rounded-xl shadow-sm border border-gray-200 p-4`.

La tabla de datos se envuelve en `overflow-x-auto rounded-xl border border-gray-200 mx-4` con sombra. La tabla interior tiene `min-w-[600px]`. Las columnas "Fecha de creación" y "Última modificación" se ocultan con `hidden` (visible en tablet/desktop). Solo se muestran "Nombre", "Estado" y "Acciones".

La barra de navegación inferior es `fixed bottom-0 inset-x-0 z-30 bg-white border-t border-gray-200 h-14 flex items-center justify-around`. Cada item es un enlace con `flex flex-col items-center justify-center gap-0.5 py-1 px-3 text-xs text-gray-400`. El item activo se destaca con `text-primary-600`.

### Ejemplo Guiado 2: Dashboard para Vista Tablet (768px - 1024px)

En este ejemplo, se añaden las variantes responsive `md:` sobre el código del ejemplo 1 para transformar la vista a tablet. La barra de navegación inferior se oculta: `md:hidden`. La sidebar colapsada se añade junto al contenido: `hidden md:flex md:flex-col md:fixed md:inset-y-0 md:left-0 md:z-40 md:w-16 md:bg-gray-900 md:text-white`. El botón hamburguesa se oculta en tablet: `md:hidden`. El contenido principal añade margen izquierdo para la sidebar: `md:ml-16`.

Los widgets pasan a 2 columnas: `grid grid-cols-1 sm:grid-cols-2 gap-4 md:gap-6`. La tabla oculta sus columnas con `hidden md:table-cell`, mostrando dos columnas adicionales respecto a móvil. El padding del contenido se amplía: `px-4 md:px-6`.

### Ejemplo Guiado 3: Dashboard para Vista Desktop (> 1024px)

En este ejemplo final, se añaden las variantes `lg:` y `xl:` para completar la experiencia desktop. La sidebar se expande: `lg:w-64`. Los textos de los items de navegación, ocultos en tablet, se muestran en desktop: `hidden lg:block`. El contenido principal ajusta su margen: `lg:ml-64`. Los widgets pasan a 3 columnas y luego a 4: `lg:grid-cols-3 xl:grid-cols-4`. La tabla muestra todas las columnas (las que tenían `hidden md:table-cell` ahora se complementan con `lg:table-cell` para las columnas que solo se muestran en desktop). El tamaño de tipografía base aumenta ligeramente: `text-sm md:text-base`.

La transición completa entre los tres estados está ahora implementada: el mismo código base (móvil) se ha ido enriqueciendo con variantes responsive que añaden funcionalidad y complejidad visual a medida que el espacio disponible crece. El resultado es una aplicación que funciona con fluidez en cualquier tamaño de pantalla, desde un teléfono móvil hasta un monitor 4K, sin código duplicado ni archivos CSS específicos por dispositivo.

## Actividades guiadas

### Actividad Guiada 1: Conversión de un Dashboard Desktop-First a Mobile-First

El docente proporciona un dashboard implementado con enfoque desktop-first: diseñado para 1440px, con grid de 4 columnas, sidebar expandida, tabla con 10 columnas, y overlays para los breakpoints menores que intentan forzar el diseño grande en pantallas pequeñas. El alumnado deberá analizar los problemas de usabilidad que genera este enfoque (tablas ilegibles, widgets minúsculos, sidebar que tapa todo el contenido) y reescribir completamente el layout usando el enfoque mobile-first con Tailwind. El rediseño debe comenzar desde el móvil (1 columna, sin sidebar, tabla con scroll), pasar por tablet (2 columnas, sidebar colapsada, tabla con 5 columnas), y llegar a desktop (4 columnas, sidebar expandida, tabla completa). El resultado debe ser visualmente equivalente en desktop al diseño original, pero funcionalmente superior en móvil y tablet.

### Actividad Guiada 2: BreakpointObserver con Señales para Sidebar Inteligente

El alumnado implementará un servicio `LayoutService` que utilice `BreakpointObserver` para detectar el tamaño actual de la pantalla y exponerlo como señales. El servicio definirá señales para `isMobile`, `isTablet` y `isDesktop`, cada una derivada de la observación de los breakpoints correspondientes. Un componente `SidebarComponent` consumirá estas señales para gestionar automáticamente su estado: en móvil, comienza cerrada y se abre/cierra manualmente; al cruzar a tablet, se abre automáticamente en modo colapsado; al cruzar a desktop, se expande automáticamente; si la ventana se redimensiona de desktop a móvil, la sidebar se cierra automáticamente. El alumnado escribirá tests unitarios para el servicio (mockeando `BreakpointObserver` con observables controlados) y tests de integración para el componente (simulando cambios de tamaño de ventana con `window.resizeTo`).

### Actividad Guiada 3: Tabla de Datos con Ocultación Progresiva de Columnas

El alumnado implementará un componente `ResponsiveDataTable` que acepta una definición de columnas con un nuevo campo `breakpoint` que indica a partir de qué breakpoint debe mostrarse cada columna. Por ejemplo, la columna "ID" tiene `breakpoint: 'hidden'` (nunca visible), "Nombre" tiene `breakpoint: 'always'` (siempre visible), "Fecha" tiene `breakpoint: 'md'` (visible desde tablet), y "Descripción" tiene `breakpoint: 'lg'` (solo visible en desktop). El componente traduce estos breakpoints lógicos a clases de Tailwind (`hidden md:table-cell`, `hidden lg:table-cell`) y las aplica dinámicamente a cada celda. La tabla debe seguir siendo accesible (los datos ocultos visualmente deben estar disponibles para lectores de pantalla, a menos que se marquen explícitamente como no esenciales). El alumnado probará la tabla con un dataset de 50 registros y 8 columnas, verificando su comportamiento en todos los breakpoints.

## Actividades propuestas

### Actividad Propuesta 1: Análisis Responsive de Aplicaciones Profesionales

Selecciona tres aplicaciones profesionales (recomendadas: Notion, Linear, VS Code web, o cualquier aplicación de gestión que utilices) y realiza un análisis detallado de su comportamiento responsive. Para cada aplicación: documenta los breakpoints que utiliza (mide los anchos exactos donde cambia el layout), identifica las estrategias responsive de cada componente (sidebar, tablas, formularios, modales, navegación), captura pantallas en al menos 4 tamaños diferentes (375px, 768px, 1024px, 1440px), y analiza cómo manejan la información en cada tamaño (¿qué se oculta?, ¿qué se reorganiza?, ¿qué se simplifica?). Elabora un informe comparativo con capturas anotadas y extrae los 5 patrones responsive más efectivos que hayas encontrado, explicando cómo los implementarías en un proyecto Angular con Tailwind.

### Actividad Propuesta 2: Sidebar Multinivel Responsive

Implementa una sidebar de navegación con soporte para tres niveles de profundidad, completamente responsive. El primer nivel muestra secciones principales siempre visibles. El segundo nivel (subsecciones) se despliega al hacer clic en una sección principal en desktop, o al navegar a una vista dedicada en móvil. El tercer nivel (sub-subsecciones) se muestra como tabs dentro del contenido en desktop, o como un menú desplegable adicional en móvil. La sidebar debe ser completamente colapsable a iconos, con transiciones animadas. En móvil, debe funcionar como drawer con overlay. Implementa navegación por teclado completa con `FocusKeyManager`. Usa `BreakpointObserver` para cambiar el comportamiento de navegación entre móvil (push navigation) y desktop (expand in place).

### Actividad Propuesta 3: Formulario Multi-columna Responsive

Diseña e implementa un formulario complejo de alta de producto (20 campos) que se adapte fluidamente a diferentes tamaños de pantalla. En móvil (<640px), todos los campos en una sola columna, organizados en secciones con acordeones colapsables para no abrumar con scroll. En tablet (640px-1024px), campos en 2 columnas con secciones visibles simultáneamente pero colapsables. En desktop (>1024px), campos en 3 columnas para secciones densas, con todas las secciones visibles. Los campos que contienen información extensa (descripción del producto, notas internas) deben ocupar el ancho completo en todos los breakpoints. Utiliza CSS grid con `col-span-full` para estos campos. El formulario debe ser 100% funcional con validación reactiva en todos los breakpoints.

### Actividad Propuesta 4: Dashboard de Analytics Responsive

Construye un dashboard de analytics con los siguientes widgets, cada uno con su propio comportamiento responsive: tarjeta de métrica principal (valor grande, tendencia, sparkline), gráfico de barras apiladas por categoría (vertical en móvil, horizontal en desktop), tabla de últimos eventos (scroll horizontal en móvil, columnas completas en desktop), mapa de calor de actividad (grid de 7x24 en desktop, 7x12 con scroll en móvil), y lista de top 10 elementos con mini gráfico de barras. El dashboard debe reorganizar los widgets según el espacio disponible, priorizando la métrica principal y la tabla en móvil, y mostrando todos los widgets en desktop con un layout de revista (algunos widgets ocupan 2 columnas, otros 1). Usa `grid` con `col-span-*` responsive y `order-*` para controlar la prioridad visual en cada breakpoint.

### Actividad Propuesta 5: Aplicación Angular para Electron con Diseño Responsive

Crea una aplicación Angular que funcione tanto en navegador web como en Electron, con diseño responsive que cubra tres contextos de uso: navegador web (responsive estándar), ventana de Electron pequeña (800x600), y ventana de Electron maximizada (cualquier resolución). Configura `minWidth: 800` y `minHeight: 600` en el proceso principal de Electron. Implementa un layout que use Tailwind responsive y `BreakpointObserver` para: en ventana pequeña (800-1024px), sidebar colapsada y widgets en 2 columnas; en ventana mediana (1024-1440px), sidebar expandida y widgets en 3 columnas; en ventana grande (>1440px), sidebar expandida, widgets en 4 columnas, y contenido centrado con `max-w-screen-2xl mx-auto`. Prueba que la aplicación funcione correctamente tanto en `ng serve` (navegador) como en `npm run electron:start` (ventana nativa). Documenta las diferencias de comportamiento entre ambos entornos.

??? "Actividades de ampliación"

    ### Actividad de Ampliación 1: Sistema de Layouts Dinámicos con Tailwind y Angular

    Investiga e implementa un sistema de layouts dinámicos donde la persona usuaria pueda, en tiempo de ejecución, elegir entre varios layouts predefinidos (sidebar izquierda, sidebar derecha, solo contenido, dos paneles, tres paneles) y cambiar entre ellos sin recargar la aplicación. El sistema debe basarse en CSS grid con `grid-template-areas` definidas en Tailwind mediante `@theme` y clases utility personalizadas. Cada layout debe tener su variante responsive. Implementa un selector de layout en la interfaz (dropdown en la barra de navegación) que persista la elección en `localStorage`. Escribe tests que verifiquen que cada layout se renderiza correctamente en todos los breakpoints.

    ### Actividad de Ampliación 2: Imágenes y Medios Responsive Avanzados

    Investiga y aplica técnicas avanzadas de imágenes responsive en Angular: uso de `srcset` y `sizes` para servir diferentes resoluciones de imagen según el dispositivo y la densidad de píxeles, uso del elemento `<picture>` con `source` y `media` para servir imágenes recortadas o con diferente relación de aspecto según el breakpoint (una imagen horizontal en desktop, una imagen cuadrada en móvil), lazy loading nativo con `loading="lazy"`, y placeholders con efecto blur-up usando Tailwind (`bg-gray-200 animate-pulse` mientras carga, transición a la imagen real). Implementa un componente `ResponsiveImage` que encapsule toda esta lógica y lo aplica en una galería de productos. Mide la diferencia de rendimiento (bytes transferidos, Largest Contentful Paint) entre imágenes responsive y imágenes fijas en diferentes dispositivos.

    ### Actividad de Ampliación 3: Pruebas Visuales de Regresión Responsive con Playwright

    Configura un sistema de pruebas visuales de regresión responsive utilizando Playwright. Escribe tests que capturen screenshots de cada página de la aplicación en múltiples viewports (375px, 640px, 768px, 1024px, 1280px, 1536px) y los compare con screenshots de referencia. Configura el pipeline de CI/CD para ejecutar estas pruebas en cada pull request y fallar si se detectan cambios visuales no intencionados en cualquier breakpoint. Investiga cómo manejar diferencias sutiles entre ejecuciones (anti-aliasing, fuentes, renderizado del sistema operativo) para evitar falsos positivos. Documenta el proceso de configuración y escribe una guía para el equipo sobre cómo añadir nuevas capturas de referencia cuando se modifica intencionadamente el diseño responsive.

!!! tip "Buenas prácticas"

    1. Comienza siempre por el diseño móvil. Escribe primero el HTML con las clases base (sin prefijos) que definen la experiencia en pantallas pequeñas. Luego añade progresivamente las variantes `sm:`, `md:`, `lg:`, `xl:` para enriquecer la experiencia en pantallas más grandes. Este orden te obliga a priorizar el contenido y la funcionalidad esencial.

    2. Utiliza `min-width` en las media queries implícitas de Tailwind, no `max-width`. Las variantes de Tailwind (`sm:`, `md:`, etc.) aplican estilos desde el breakpoint hacia arriba. Esto es mobile-first: defines los estilos base (móvil) y los sobrescribes hacia arriba. Evita patrones desktop-first como definir estilos para desktop y luego sobrescribirlos para móvil con `max-md:`.

    3. Prueba la aplicación en dispositivos reales, no solo redimensionando el navegador. El viewport del navegador redimensionado en el escritorio no simula fielmente un dispositivo móvil: las fuentes se renderizan diferente, el teclado virtual no aparece, los eventos táctiles no existen, y la densidad de píxeles es distinta. Conecta un teléfono real mediante USB y utiliza las DevTools para depurar, o al menos usa el modo de dispositivo en DevTools con throttling de red y CPU.

    4. No ocultes contenido crítico en móvil para simplificar el diseño. La simplificación responsive debe basarse en priorización: la información esencial debe estar siempre disponible; la información complementaria puede requerir una interacción adicional en móvil (un acordeón, una pestaña, un "ver más"). Ocultar información crítica porque "en móvil no cabe" es un fallo de diseño, no una limitación técnica.

    5. Usa `BreakpointObserver` solo para lógica que no puede expresarse con clases responsive de Tailwind. Si necesitas mostrar/ocultar un elemento, cambiar el layout, o modificar el tamaño de fuente, Tailwind es la herramienta correcta. Si necesitas decidir qué datos cargar del backend, qué funcionalidad inicializar, o cómo gestionar la navegación, `BreakpointObserver` en TypeScript es la herramienta correcta.

    6. Define un sistema de espaciado responsive consistente. El espaciado en móvil debe ser suficiente para la legibilidad y la interacción táctil (mínimo 16px de padding horizontal), pero contenido para aprovechar el espacio. En desktop, el espaciado puede ser más generoso (24-32px) para crear jerarquía visual con el espacio en blanco. Usa la escala de Tailwind para mantener la consistencia: `p-4 md:p-6 lg:p-8`.

    7. Diseña los puntos de interacción táctil con el tamaño adecuado. En móvil, los botones y enlaces deben tener al menos 44x44px (recomendación de Apple) o 48x48px (recomendación de Google) para ser fácilmente tocables con el dedo. Las clases `p-3` (12px de padding) en un botón con texto de 16px superan este mínimo. En desktop, los mismos botones pueden reducir su tamaño para aprovechar mejor el espacio.

    8. Asegura que las imágenes y los medios sean responsive no solo en tamaño, sino también en resolución y formato. Usa `srcset` para servir imágenes de mayor resolución en pantallas de alta densidad (Retina) y de menor resolución en pantallas estándar. Considera usar formatos modernos (WebP, AVIF) con fallback a JPEG/PNG mediante `<picture>`.

    9. Prueba el rendimiento en condiciones de red móvil. Una aplicación que funciona bien en WiFi de oficina puede ser inutilizable en 4G con mala cobertura. Usa el throttling de red de las DevTools para simular condiciones de red lentas y verifica que la aplicación sigue siendo usable: carga progresiva, esqueletos mientras los datos llegan, y funcionalidad offline cuando sea posible.

    10. Documenta las decisiones responsive en una guía de estilos o en el README del proyecto. Explica qué breakpoints se utilizan, por qué se eligieron esos valores, y qué estrategia responsive sigue cada tipo de componente. Esta documentación ayuda a mantener la consistencia cuando nuevas personas se incorporan al equipo.

!!! warning "Errores frecuentes"

    1. Diseñar desktop-first y luego intentar "adaptar" a móvil con overlays y escalado. Este enfoque produce aplicaciones técnicamente funcionales en móvil pero terriblemente incómodas de usar. El móvil no es un desktop pequeño; es un contexto de uso diferente con sus propias reglas de interacción.

    2. Usar breakpoints fijos pensando en dispositivos concretos en lugar de en rangos de espacio. Asumir que `md` es "tablet en vertical" y `lg` es "tablet en horizontal" lleva a diseños frágiles que se rompen cuando un nuevo dispositivo con dimensiones diferentes sale al mercado. Diseña para el espacio disponible, no para el dispositivo.

    3. Ocultar la navegación principal en móvil sin proporcionar una alternativa clara. El botón hamburguesa esconde la navegación, pero debe ser visible y reconocible. Si la persona usuaria no encuentra cómo navegar, abandonará la aplicación. Complementa el menú hamburguesa con una barra de navegación inferior para las secciones más importantes.

    4. No gestionar el scroll horizontal accidental. Una tabla con `overflow-x-auto` es necesaria, pero si toda la página tiene scroll horizontal (porque algún elemento desborda), la experiencia es muy negativa. Verifica que en cada breakpoint el scroll horizontal global es cero (`html, body { overflow-x: hidden }` si es necesario) y que solo los componentes que lo necesitan (tablas) tienen scroll horizontal local.

    5. Ignorar el modo landscape en móvil. Probar solo en portrait (vertical) es insuficiente. Muchas personas usuarias utilizan sus teléfonos en landscape (horizontal), especialmente para ver tablas, documentos o vídeos. La interfaz debe funcionar en ambas orientaciones.

    6. Usar `display: none` para ocultar elementos en móvil sin considerar las implicaciones de accesibilidad y SEO. El contenido oculto con `hidden` (display: none) no está disponible para lectores de pantalla. Si el contenido es importante para la comprensión de la página, utiliza `sr-only` en su lugar o muéstralo de forma accesible.

    7. No probar con el teclado virtual abierto en móvil. En formularios, el teclado virtual ocupa aproximadamente el 40% de la pantalla. Verifica que los campos de formulario, especialmente los que están cerca del fondo, sean visibles y accesibles con el teclado abierto. Usa `visualViewport` API si es necesario para ajustar el scroll.

    8. Asumir que todos los dispositivos tienen la misma densidad de píxeles. Un diseño que se ve bien a 1x puede verse borroso o con artefactos a 2x o 3x. Usa SVG para iconos y gráficos vectoriales, y `srcset` para imágenes rasterizadas.

    9. Implementar responsive solo con media queries CSS sin considerar el rendimiento. En móvil, cargar la tabla con 1000 registros, renderizarlos todos y luego ocultar la mayoría de las columnas con CSS es ineficiente. Considera estrategias de virtualización (CDK Virtual Scroll) y carga de datos condicionada por breakpoint para optimizar el rendimiento en dispositivos con recursos limitados.

    10. No actualizar la lógica de negocio al cambiar de breakpoint. Si un componente se comporta diferente en móvil (por ejemplo, navegación push en lugar de tabs), olvidar actualizar los manejadores de eventos, la gestión del historial y la restauración del estado. La adaptación responsive no es solo visual; la lógica de interacción también debe adaptarse.

!!! abstract "Resumen"

    Esta unidad ha establecido los fundamentos teóricos y prácticos del diseño responsive aplicado a aplicaciones de gestión construidas con Angular y Tailwind CSS. Hemos comenzado desmontando el mito de que Mobile First es irrelevante para aplicaciones de escritorio, argumentando que el enfoque de "diseñar desde la restricción" mejora la calidad del diseño en todos los tamaños y prepara la aplicación para un mercado laboral donde las aplicaciones de gestión se utilizan crecientemente desde múltiples dispositivos.

    El sistema de breakpoints de Tailwind (`sm`, `md`, `lg`, `xl`, `2xl`) se ha aplicado de forma sistemática a los siete tipos de componentes más comunes en aplicaciones de gestión: sidebars, tablas, dashboards, formularios, modales y barras de navegación. Cada componente ha recibido una estrategia responsive específica, basada en su función y en la información que presenta, que puede implementarse con las variantes responsive de Tailwind sin media queries explícitas.

    Hemos explorado el arsenal de técnicas responsive de Tailwind: grid y flexbox responsive, ocultación y visualización condicional, tipografía y espaciado adaptativos, e imágenes responsive. Estas técnicas, combinadas, permiten construir interfaces que se adaptan fluidamente a cualquier ancho de ventana.

    `BreakpointObserver` de Angular CDK y su integración con señales mediante `toSignal` proporcionan el puente necesario para aquellos casos donde la adaptación responsive requiere lógica en TypeScript: cambiar el comportamiento de la navegación, inicializar o destruir funcionalidades, o decidir qué datos cargar. La regla práctica de "Tailwind para lo visual, BreakpointObserver para la lógica de negocio" guía esta separación de responsabilidades.

    El proyecto integrador del dashboard completamente responsive ha demostrado cómo todas estas técnicas se unen en una aplicación real que funciona en tres rangos de dispositivos, con comportamientos diferenciados pero coherentes en cada rango.

    Finalmente, hemos abordado las particularidades del diseño responsive en aplicaciones de escritorio con Electron, preparando al alumnado para el escenario cada vez más común de desarrollar aplicaciones que funcionan tanto en navegador como en escritorio nativo.

## Recursos complementarios

### Documentación oficial
- Tailwind CSS - Responsive Design: https://tailwindcss.com/docs/responsive-design
- Tailwind CSS - Breakpoints: https://tailwindcss.com/docs/screens
- Angular CDK - Layout (BreakpointObserver): https://material.angular.io/cdk/layout/overview
- Angular - Signals: https://angular.dev/guide/signals
- Angular - RxJS Interop (toSignal): https://angular.dev/guide/signals/rxjs-interop
- Electron - BrowserWindow (minWidth, minHeight): https://www.electronjs.org/docs/latest/api/browser-window

### Artículos y guías
- "Mobile First" de Luke Wroblewski (A Book Apart, 2011): obra fundacional del concepto Mobile First.
- "Responsive Web Design" de Ethan Marcotte (A Book Apart, 2011): obra fundacional del diseño web responsive.
- "Responsive Design Patterns & Principles" de Ethan Marcotte (A Book Apart, 2015): patrones y principios de diseño responsive.
- MDN - Responsive Design: https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design
- web.dev - Responsive Web Design Basics: https://web.dev/responsive-web-design-basics/

### Herramientas
- Chrome DevTools Device Mode: simulador de dispositivos móviles con throttling de red y CPU.
- Responsively App: herramienta de desarrollo que muestra la aplicación en múltiples viewports simultáneamente (https://responsively.app).
- Polypane: navegador para desarrollo responsive con vistas múltiples sincronizadas.
- BrowserStack: testing en dispositivos reales en la nube (https://browserstack.com).
- Playwright: testing automatizado en múltiples navegadores y viewports (https://playwright.dev).

### Ejemplos de referencia
- Tailwind CSS - Official Components (responsive): https://tailwindcss.com/docs/container
- Tailwind UI - Application Layouts: https://tailwindui.com/components/application-ui
- shadcn/ui - Components responsive: https://ui.shadcn.com
- Notion, Linear, VS Code web: aplicaciones de referencia para análisis responsive.
