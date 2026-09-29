---
icon: lucide/layout-grid
---

# Unidad 5: Layouts Modernos para Interfaces Web

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Construir layouts complejos de aplicaciones web utilizando **Flexbox** y **CSS Grid** a través de las clases utilitarias de Tailwind CSS, seleccionando el sistema de layout más adecuado para cada contexto.
2. Traducir layouts de aplicaciones de escritorio clásicas (VBox, HBox, GridPane, StackPane) a sus equivalentes en Tailwind CSS, comprendiendo las equivalencias conceptuales entre ambos paradigmas.
3. Diseñar dashboards administrativos, paneles SaaS, catálogos de ecommerce y aplicaciones de mensajería combinando Grid para la estructura principal y Flexbox para los componentes internos.
4. Aplicar técnicas de posicionamiento (relative, absolute, fixed, sticky) para implementar elementos superpuestos como tooltips, dropdowns, modales y cabeceras fijas.
5. Implementar layouts responsivos utilizando los breakpoints de Tailwind CSS con estrategia mobile-first, asegurando que las interfaces se adapten fluidamente a dispositivos móviles, tablets y escritorio.
6. Utilizar técnicas avanzadas de layout como **container queries**, layouts fluidos con funciones CSS modernas (minmax, auto-fit, clamp) y sistemas de espaciado consistente.
7. Evaluar y depurar problemas de layout utilizando las herramientas de desarrollo del navegador (DevTools), identificando colapsos de márgenes, desbordamientos y problemas de especificidad.
8. Construir desde cero cuatro layouts profesionales completos (Dashboard, SaaS, Ecommerce, Chat) que servirán como base para aplicaciones reales.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 4** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 4.** Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad.

!!! info "Criterios de evaluación"

    Criterios de evaluación oficiales que se trabajan en esta unidad:

    - CE e) Se han distribuido adecuadamente los controles en la interfaz de usuario.
    - CE f) Se ha utilizado el tipo de control más apropiado en cada caso.
    - CE g) Se ha diseñado el aspecto de la interfaz de usuario (colores y fuentes entre otros) atendiendo a su legibilidad.

> Nota: la maquetación con Flexbox, CSS Grid y utilidades de Tailwind es el vehículo técnico con el que se materializan estos criterios de distribución, jerarquía visual y legibilidad.

!!! note "Conocimientos previos"

    Para abordar con éxito esta unidad, el alumnado debe dominar los siguientes contenidos:

    - **Fundamentos de HTML5**: estructura semántica de documentos, elementos de bloque vs elementos en línea, anidamiento correcto de elementos, uso de atributos de clase e id.
    - **CSS3 básico-intermedio**: modelo de caja (content, padding, border, margin), display (block, inline, inline-block, none), posicionamiento básico (static, relative), unidades de medida (px, rem, em, %, vw, vh).
    - **Familiaridad básica con Tailwind CSS** (se introduce en la Unidad 6): comprensión del enfoque utility-first, capacidad de aplicar clases de Tailwind en templates HTML, familiaridad con el sistema de colores, tipografías y espaciado.
    - **Angular nivel básico** (se trabaja en la Unidad 10): capacidad de crear componentes standalone con Angular CLI, comprensión de la estructura de un componente (template, clase TypeScript, estilos), manejo de inputs y control flow (@if, @for).
    - **Diseño en Figma** (Unidad 4): capacidad de interpretar un diseño en Figma y extraer medidas, colores, tipografías y estructuras de layout (Auto Layout → Flexbox).

    Se realizará una **evaluación diagnóstica** al inicio de la unidad consistente en un ejercicio práctico de maquetación de una tarjeta simple con Flexbox y Tailwind. El resultado permitirá al docente ajustar el ritmo y ofrecer recursos de refuerzo a quienes lo necesiten.

## Contenidos

**Bloque A - Flexbox con Tailwind (nivel profesional, orientado a interfaces de aplicación)**

- Repaso rápido de conceptos clave:
  - **Main axis** (eje principal) y **cross axis** (eje perpendicular). Determinados por `flex-direction`.
  - **Contenedor flex** (elemento padre con `display: flex`) y **elementos flex** (hijos directos).
  - **Propiedades del contenedor**: `flex-direction`, `flex-wrap`, `justify-content`, `align-items`, `align-content`, `gap` (row-gap y column-gap).
  - **Propiedades de los elementos flex**: `flex-grow`, `flex-shrink`, `flex-basis`, `flex` (shorthand), `align-self`, `order`.

- Traducción completa a clases Tailwind:
  - `flex`, `inline-flex` → activan el contexto flex.
  - `flex-row`, `flex-row-reverse`, `flex-col`, `flex-col-reverse` → dirección.
  - `flex-wrap`, `flex-nowrap`, `flex-wrap-reverse` → ajuste de línea.
  - `justify-start`, `justify-end`, `justify-center`, `justify-between`, `justify-around`, `justify-evenly` → alineación en main axis.
  - `items-start`, `items-end`, `items-center`, `items-baseline`, `items-stretch` → alineación en cross axis.
  - `content-start`, `content-end`, `content-center`, `content-between`, `content-around`, `content-evenly` → alineación de filas cuando hay wrap.
  - `gap-{size}`, `gap-x-{size}`, `gap-y-{size}` → espaciado entre elementos.
  - `flex-1` (`flex: 1 1 0%`), `flex-auto` (`flex: 1 1 auto`), `flex-initial` (`flex: 0 1 auto`), `flex-none` (`flex: none`).
  - `grow`, `grow-0`, `shrink`, `shrink-0` → control fino de crecimiento/decrecimiento.
  - `self-auto`, `self-start`, `self-end`, `self-center`, `self-stretch`, `self-baseline` → alineación individual.

- Equivalencias con layouts de escritorio clásicos:
  - **VBox (JavaFX/Swing):** Contenedor que apila hijos verticalmente → `flex flex-col` (y normalmente `gap-N`).
  - **HBox (JavaFX/Swing):** Contenedor que alinea hijos horizontalmente → `flex flex-row` (comportamiento por defecto de flex) + `gap-N`.
  - **StackPane (JavaFX):** Contenedor que superpone hijos uno sobre otro → `relative` en el padre, `absolute inset-0` en los hijos.
  - **BorderPane (JavaFX):** Contenedor con 5 regiones (top, bottom, left, right, center) → `flex flex-col` en el padre raíz, con regiones top/bottom como hijos en columna, y región central como `flex flex-row` con left/right/center.
  - **GridPane (JavaFX):** Contenedor con filas y columnas → `grid grid-cols-{N}` y potencialmente `grid-rows-{M}`.
  - **AnchorPane (JavaFX):** Contenedor donde los hijos se anclan a los bordes del contenedor → `relative` en el padre, `absolute` con posiciones `top-0`, `left-0`, etc., en los hijos.

- Construcción de layouts profesionales con Flexbox:
  - **Sidebar layout (barra lateral + contenido):** Contenedor `flex h-screen`. Sidebar: `w-64 flex-shrink-0`. Contenido: `flex-1 overflow-auto`.
  - **Toolbar horizontal:** `flex items-center gap-3 px-4 py-2 border-b`.
  - **List layout (elementos apilados):** `flex flex-col divide-y` (para listas con separadores) o `flex flex-col gap-4`.
  - **Card grid flexible:** Aunque Grid es más natural para grids de tarjetas, Flexbox con `flex-wrap` + `flex-1` + `basis` también funciona. Comparativa Flex vs Grid para este caso.
  - **Status bar inferior:** `flex items-center justify-between px-4 py-1 bg-gray-900 text-white text-xs`.

**Bloque B - CSS Grid con Tailwind (orientado a dashboards y aplicaciones)**

- Repaso de conceptos:
  - **Contenedor grid** y **grid items** (hijos directos).
  - **Definición de columnas**: `grid-template-columns` (tamaños fijos, fracciones `fr`, `repeat()`, `minmax()`).
  - **Definición de filas**: `grid-template-rows`.
  - **Posicionamiento de items**: `grid-column-start/end`, `grid-row-start/end`, `grid-area`.
  - **Alineación**: `justify-items`, `align-items`, `justify-content`, `align-content` (contenedor), `justify-self`, `align-self` (items).
  - **Gap**: `gap`, `column-gap`, `row-gap`.

- Traducción completa a clases Tailwind:
  - `grid`, `inline-grid` → activan el contexto grid.
  - `grid-cols-{n}` (1 a 12), `grid-cols-none`, `grid-cols-subgrid` → número de columnas explícitas.
  - `col-span-{n}` (1 a 12), `col-span-full`, `col-start-{n}`, `col-end-{n}` → posicionamiento en columnas.
  - `grid-rows-{n}` (1 a 6), `grid-rows-none`, `grid-rows-subgrid` → número de filas explícitas.
  - `row-span-{n}`, `row-start-{n}`, `row-end-{n}` → posicionamiento en filas.
  - `auto-cols-auto`, `auto-cols-min`, `auto-cols-max`, `auto-cols-fr` → tamaño de columnas implícitas (creadas automáticamente).
  - `auto-rows-auto`, `auto-rows-min`, `auto-rows-max`, `auto-rows-fr` → tamaño de filas implícitas.
  - `grid-flow-row`, `grid-flow-col`, `grid-flow-dense`, `grid-flow-row-dense`, `grid-flow-col-dense` → algoritmo de colocación automática.
  - `justify-items-start/end/center/stretch`, `items-start/end/center/stretch` (atajo) → alineación horizontal de items.
  - `justify-self-start/end/center/stretch`, `self-start/end/center/stretch` (atajo) → alineación horizontal individual.
  - `gap-{size}`, `gap-x-{size}`, `gap-y-{size}` → espaciado entre celdas.

- Construcción de layouts complejos con CSS Grid:

  1. **Dashboard con widgets (tipo Google Analytics / panel de control):**
     - Grid de 12 columnas con diferentes tamaños de widget.
     - Widgets principales (gráficos grandes): `col-span-8 row-span-2`.
     - Widgets secundarios (estadísticas, KPIs): `col-span-4`.
     - Widget de actividad: `col-span-4 row-span-2`.
     - Widget de tabla: `col-span-full`.
     - Responsive: en móvil, todo `col-span-full` (una sola columna).

  2. **Panel administrativo (tipo WordPress / Django Admin):**
     - Sidebar izquierdo fijo (250px) + área de contenido.
     - El área de contenido a su vez tiene un grid: toolbar superior a toda anchura, área principal con formularios/tablas, panel de detalles opcional a la derecha.
     - Uso de `grid-cols-[250px_1fr]` (sintaxis de Tailwind con valores arbitrarios) o `grid-cols-[auto_1fr]`.

  3. **Layout de ecommerce (catálogo de productos):**
     - Grid principal: sidebar de filtros (250px) + área de productos (resto).
     - Área de productos: grid de tarjetas de producto: `grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6`.
     - Cabecera con buscador, carrito, cuenta de usuario (flex).
     - Footer con múltiples columnas (grid).

  4. **Aplicación SaaS típica (tipo Notion / Linear / Slack):**
     - Estructura de 3 columnas: navegación de workspace (izquierda, más estrecha), sidebar de contenido (centro-izquierda), área principal (derecha, más ancha).
     - Layout: `grid grid-cols-[60px_240px_1fr]` o `flex` con una combinación.

  5. **Layout de 3 paneles (maestro-detalle, tipo Outlook / Gmail):**
     - Panel izquierdo: lista de carpetas/etiquetas (flex).
     - Panel central: lista de mensajes (scroll).
     - Panel derecho: detalle del mensaje seleccionado.
     - Layout: `flex h-screen`. Cada panel con anchos fijos o `flex-1`. Divisores redimensionables (con JavaScript).

**Bloque C - Posicionamiento**

- Repaso de los valores de `position`:
  - `static` (por defecto): el elemento se posiciona según el flujo normal del documento. Ignora top/right/bottom/left y z-index.
  - `relative`: el elemento se posiciona respecto a su posición original en el flujo. Crea un nuevo contexto de posicionamiento para hijos absolute. El espacio original se conserva.
  - `absolute`: el elemento se posiciona respecto al ancestro posicionado más cercano (con position diferente a static). Sale del flujo (el espacio original NO se conserva).
  - `fixed`: el elemento se posiciona respecto al viewport. Sale del flujo. Permanece fijo al hacer scroll.
  - `sticky`: híbrido entre relative y fixed. Se comporta como relative hasta que cruza un umbral de scroll; entonces se vuelve fixed. Útil para cabeceras que se pegan al hacer scroll.

- Traducción a clases Tailwind:
  - `static`, `relative`, `absolute`, `fixed`, `sticky`.
  - **Coordenadas**: `top-0`, `top-{n}`, `-top-{n}`, `top-full`, `top-1/2` (50%)... y equivalentes para right, bottom, left.
  - `inset-0`, `inset-x-0`, `inset-y-0` → atajo para todas las coordenadas (útil para superposiciones a pantalla completa).
  - **z-index**: `z-0`, `z-10`, `z-20`, `z-30`, `z-40`, `z-50`, `z-auto`.

- Casos de uso prácticos:
  - **Tooltip:** Contenedor `relative` (padre), tooltip `absolute` posicionado arriba/derecha/abajo/izquierda del padre, con `z-10`.
  - **Dropdown / Menú desplegable:** Botón `relative`, menú `absolute top-full left-0 mt-1 z-20`.
  - **Modal / Overlay:** Fondo oscuro semitransparente `fixed inset-0 bg-black/50 z-40`, contenido del modal `fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50`.
  - **Header fija:** `fixed top-0 left-0 right-0 z-30 bg-white border-b`. Añadir `pt-{altura-header}` al contenido para que no quede tapado.
  - **Sidebar fija:** `fixed top-0 left-0 h-full w-64 z-20`. Añadir `pl-64` al contenido.
  - **Boton "volver arriba":** `fixed bottom-8 right-8 z-10`.
  - **Sticky header en tablas:** Cabecera de tabla `sticky top-0 bg-white z-10`.

**Bloque D - Técnicas avanzadas de layout**

- **Combinación de Grid + Flexbox:**
  ==Regla práctica: Grid para la estructura macro (layout de página), Flexbox para los componentes y subcomponentes== (layout interno de tarjetas, barras de herramientas, formularios, etc.). Grid es bidimensional (filas y columnas simultáneamente); Flexbox es ideal para layouts unidimensionales (una fila O una columna).

  Ejemplo de patrón: Página con grid de 3 columnas (sidebar, contenido, panel lateral). Dentro del panel de contenido, las tarjetas de estadísticas se disponen con Flexbox wrap. Dentro de cada tarjeta, el layout interno (icono + label + valor) usa Flexbox vertical.

- **Container queries con Tailwind 4:**
  Las container queries permiten aplicar estilos basados en el tamaño del contenedor padre, no en el viewport (que es lo que hacen las media queries). Esto es revolucionario para componentes reutilizables que deben adaptarse a diferentes contextos.

  En Tailwind 4, se usan con:
  ```html
  <div class="@container">
    <div class="grid @sm:grid-cols-2 @lg:grid-cols-3 @xl:grid-cols-4">
      <!-- Las columnas cambian según el ancho de @container, no del viewport -->
    </div>
  </div>
  ```

  Caso de uso: un componente de grid de tarjetas que debe mostrar 2 columnas cuando se coloca en un sidebar estrecho (300px), pero 4 columnas cuando se coloca en el área de contenido principal (800px). Con media queries, este componente no podría adaptarse porque depende del viewport; con container queries, sí.

- **Layouts fluidos con funciones CSS modernas:**
  Usando `min()`, `max()`, `clamp()`, `minmax()` y `repeat()` + `auto-fit` / `auto-fill`:

  ```html
  <!-- Grid responsivo sin media queries (auto-fit + minmax) -->
  <div class="grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-6">
    <!-- Las tarjetas se ajustan automáticamente: mínimo 280px, máximo 1fr -->
  </div>
  ```

  ```css
  /* Anchos fluidos con clamp() */
  .container {
    width: clamp(320px, 80vw, 1200px);
    /* Mínimo 320px, ideal 80% del viewport, máximo 1200px */
  }
  ```

  Tailwind 4 permite valores arbitrarios para aplicar estas funciones: `w-[clamp(320px,80vw,1200px)]` o definir tokens personalizados en `@theme`.

- **Técnicas de centrado:**
  - Centrado horizontal de un elemento bloque: `mx-auto` (funciona para cualquier elemento con width definido).
  - Centrado con Flexbox (más versátil): `flex items-center justify-center` en el contenedor padre. Los hijos (únicos o múltiples) se centran vertical y horizontalmente.
  - Centrado con Grid: `grid place-items-center` en el contenedor. El hijo (único o múltiples) se centra en ambas direcciones. Es la sintaxis más concisa para centrar un único elemento.
  - Centrado absoluto (para overlays y modales): `absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2`.

- **Espaciado consistente (sistema de gap y padding):**
  Un sistema de espaciado consistente es la diferencia entre una interfaz que se siente "bien" y una que se siente "rara". Tailwind proporciona una escala de espaciado predefinida (basada en 0.25rem = 4px) que debe usarse de forma consistente:
  - 1 (0.25rem = 4px): micro-espaciado (entre iconos y texto, dentro de chips).
  - 2 (0.5rem = 8px): espaciado pequeño (entre elementos de un formulario, dentro de un grupo).
  - 3 (0.75rem = 12px): espaciado medio-pequeño (padding interior de componentes, gap de listas).
  - 4 (1rem = 16px): espaciado medio (padding de tarjetas, gap entre párrafos).
  - 6 (1.5rem = 24px): espaciado medio-grande (entre secciones de una página).
  - 8 (2rem = 32px): espaciado grande (padding de página, entre componentes mayores).
  - 12 (3rem = 48px): espaciado muy grande (entre secciones principales).
  - 16 (4rem = 64px): macro-espaciado (márgenes de secciones hero).

  ==La clave es la consistencia==: no mezclar `p-3` (12px) con `p-[14px]` (arbitrario). Todo debe pertenecer a la escala.

## Desarrollo teórico

### Sección A: Flexbox con Tailwind

**Flexbox** (Flexible Box Layout Module) fue introducido en CSS3 en 2009 y alcanzó soporte universal alrededor de 2015. Diseñado específicamente para layouts unidimensionales (una fila O una columna, no ambas simultáneamente), Flexbox resuelve problemas que durante décadas atormentaron a los desarrolladores web: centrar elementos verticalmente (imposible sin hacks hasta Flexbox), distribuir espacio equitativamente entre elementos, alinear elementos de diferentes alturas al mismo borde, y crear layouts que se adapten al contenido sin necesidad de cálculos de ancho manuales.

Aunque lleva más de una década entre nosotros, muchos desarrolladores no aprovechan todo el potencial de Flexbox porque aprendieron lo básico y se quedaron ahí. Esta sección busca un dominio profesional, orientado específicamente a la construcción de interfaces de aplicación con Tailwind.

#### Conceptos fundamentales

Cuando aplicas `display: flex` (o la clase `flex` de Tailwind) a un contenedor, ocurren varias cosas:

1. El contenedor se convierte en un **flex container**.
2. Todos sus hijos directos se convierten automáticamente en **flex items** (no es necesario aplicar clases a los hijos para que participen en el layout flex, aunque puedes hacerlo para controlar su comportamiento).
3. Se establecen dos ejes:
   - **Main axis (eje principal):** definido por `flex-direction`. Por defecto, horizontal (row) de izquierda a derecha. Si cambias a `flex-col`, el eje principal es vertical de arriba a abajo.
   - **Cross axis (eje perpendicular):** perpendicular al eje principal. Si main axis es horizontal, cross axis es vertical.

Esta distinción entre ejes es **crítica**. Las propiedades `justify-*` siempre actúan sobre el main axis, y las propiedades `items-*` siempre actúan sobre el cross axis. Invertir la dirección invierte qué hace cada propiedad.

```
flex flex-row (por defecto):
  Main axis → (horizontal)
  ┌─────────────────────────────┐
  │ ← justify-content →         │  Controla distribución horizontal
  │ ↕ items (align-items) ↕     │  Controla alineación vertical
  
flex flex-col:
  Main axis ↓ (vertical)
  ┌─────────────────────────────┐
  │ ↕ justify-content ↕         │  Controla distribución vertical
  │ ← items (align-items) →     │  Controla alineación horizontal
```

Este es probablemente el concepto más confuso para quienes aprenden Flexbox, y el que más errores de layout explica.

#### Propiedades del contenedor flex con Tailwind

**Dirección y ajuste de línea:**

```html
<!-- Fila (comportamiento por defecto de flex) -->
<div class="flex flex-row gap-4">
  <div>A</div> <div>B</div> <div>C</div>
</div>

<!-- Columna -->
<div class="flex flex-col gap-4">
  <div>A</div> <div>B</div> <div>C</div>
</div>

<!-- Fila con wrap (como float o inline-block pero con esteroides) -->
<div class="flex flex-row flex-wrap gap-4">
  <div class="w-64">...</div> <div class="w-64">...</div> ...
</div>
```

**Alineación en el eje principal (justify-content):**

```html
<!-- Distribución de espacio sobrante -->
<div class="flex justify-start">...</div>   <!-- Al inicio (por defecto) -->
<div class="flex justify-center">...</div>   <!-- Centrados -->
<div class="flex justify-end">...</div>      <!-- Al final -->
<div class="flex justify-between">...</div>  <!-- Espacio entre items, sin espacio en extremos -->
<div class="flex justify-around">...</div>   <!-- Espacio alrededor de cada item (mitad en extremos) -->
<div class="flex justify-evenly">...</div>   <!-- Espacio igual entre items y extremos -->
```

**Alineación en el eje perpendicular (align-items):**

```html
<div class="flex items-start">...</div>     <!-- Al inicio del cross axis -->
<div class="flex items-center">...</div>     <!-- Centrados (¡el santo grial! centrado vertical) -->
<div class="flex items-end">...</div>        <!-- Al final -->
<div class="flex items-baseline">...</div>   <!-- Línea base del texto alineada (para tipografía) -->
<div class="flex items-stretch">...</div>    <!-- Estirar al tamaño del cross axis (por defecto) -->
```

**Gap:**

La propiedad `gap` es una de las mejores adiciones a CSS. Antes de `gap`, para espaciar elementos flex solo se podía usar márgenes (con el engorro de eliminar el margen del primer/último elemento). Con `gap`, el espaciado entre elementos se define en el contenedor, no en los hijos:

```html
<div class="flex gap-4">...</div>         <!-- 16px entre todos los items -->
<div class="flex gap-x-4 gap-y-2">...</div> <!-- Diferente gap horizontal y vertical (con wrap) -->
```

#### Propiedades de los elementos flex

Cada hijo directo de un contenedor flex puede controlar su propio comportamiento:

**Flex grow, shrink, basis:**

- `flex-1` = `flex: 1 1 0%` → el elemento crece para ocupar espacio disponible, puede encogerse si es necesario, y su tamaño base es 0 (ignora el tamaño del contenido para el reparto). Es la forma más común de hacer que un elemento ocupe el resto del espacio.

- `flex-auto` = `flex: 1 1 auto` → crece y encoge, pero el tamaño base es `auto` (el tamaño del contenido). La diferencia con `flex-1` es sutil pero importante cuando hay múltiples elementos con contenido de diferente tamaño.

- `flex-initial` = `flex: 0 1 auto` → no crece, puede encogerse. Comportamiento por defecto de los flex items.

- `flex-none` = `flex: none` → no crece, no se encoge. El elemento mantiene su tamaño cueste lo que cueste.

- `grow` y `grow-0` → controlan solo grow.
- `shrink` y `shrink-0` → controlan solo shrink.

**Auto-márgenes:**

Una técnica Flexbox menos conocida pero extremadamente útil: los márgenes `auto` en el eje principal consumen todo el espacio disponible. Esto permite empujar elementos a los extremos sin necesidad de `justify-between`:

```html
<div class="flex gap-4">
  <span>Logo</span>
  <span>Home</span>
  <span>Products</span>
  <span class="ml-auto">Login</span>  <!-- ml-auto empuja Login a la derecha -->
</div>
```

Este patrón es preferible a `justify-between` cuando no quieres separar todos los elementos, solo empujar uno a la derecha.

#### Layouts profesionales con Flexbox

**Sidebar + Contenido (el layout más común en aplicaciones)**

```html
<div class="flex h-screen bg-gray-50">
  <!-- Sidebar -->
  <aside class="w-64 flex-shrink-0 bg-gray-900 text-white flex flex-col">
    <div class="p-4 text-xl font-bold border-b border-gray-700">Mi App</div>
    <nav class="flex-1 overflow-y-auto p-4">
      <ul class="flex flex-col gap-1">
        <li><a href="#" class="block px-3 py-2 rounded-lg hover:bg-gray-800">Dashboard</a></li>
        <li><a href="#" class="block px-3 py-2 rounded-lg hover:bg-gray-800">Proyectos</a></li>
        <li><a href="#" class="block px-3 py-2 rounded-lg hover:bg-gray-800">Equipo</a></li>
        <li><a href="#" class="block px-3 py-2 rounded-lg hover:bg-gray-800">Configuración</a></li>
      </ul>
    </nav>
    <div class="p-4 border-t border-gray-700">
      <div class="flex items-center gap-3">
        <img src="avatar.jpg" class="w-8 h-8 rounded-full" alt="User" />
        <span class="text-sm">María García</span>
      </div>
    </div>
  </aside>

  <!-- Contenido principal -->
  <main class="flex-1 flex flex-col min-w-0">
    <header class="flex items-center justify-between px-6 py-4 bg-white border-b">
      <h1 class="text-xl font-semibold">Dashboard</h1>
      <div class="flex items-center gap-3">
        <button class="px-3 py-1.5 text-sm bg-blue-600 text-white rounded-lg">New</button>
      </div>
    </header>
    <div class="flex-1 overflow-y-auto p-6">
      <!-- Contenido de la página aquí -->
    </div>
  </main>
</div>
```

**Elementos clave de este layout:**
- `h-screen` en el contenedor raíz para que ocupe toda la altura del viewport.
- `flex-shrink-0` en el sidebar para que nunca se encoja cuando el contenido es muy ancho.
- `flex-1` en el contenido para que ocupe el resto del espacio.
- `min-w-0` en el contenido principal: **esto es crítico y a menudo olvidado**. Por defecto, los flex items tienen `min-width: auto`, lo que impide que se encojan por debajo del tamaño de su contenido. Añadir `min-w-0` permite que el contenido se reduzca correctamente (necesario para que el overflow funcione).
- `overflow-y-auto` en las zonas con scroll (sidebar con muchos items, área de contenido principal).
- `flex-col` en sidebar y main para estructurar sus contenidos verticalmente.

**Layout de lista con items complejos**

```html
<div class="flex flex-col divide-y divide-gray-200">
  <!-- Item de lista -->
  <div class="flex items-center gap-4 px-4 py-3 hover:bg-gray-50">
    <input type="checkbox" class="flex-shrink-0 w-4 h-4" />
    <div class="flex-shrink-0 w-2 h-2 rounded-full bg-red-500"></div>
    <div class="flex-1 min-w-0">
      <p class="font-medium truncate">Título de la tarea que es muy largo y debería truncarse</p>
      <p class="text-sm text-gray-500">Proyecto Alpha · Vence mañana</p>
    </div>
    <span class="flex-shrink-0 px-2 py-0.5 text-xs font-medium rounded-full bg-yellow-100 text-yellow-800">Urgente</span>
    <img src="avatar.jpg" class="flex-shrink-0 w-6 h-6 rounded-full" alt="Assignee" />
  </div>
  <!-- Más items... -->
</div>
```

**Patrones importantes aquí:**
- `divide-y divide-gray-200` en el contenedor añade bordes entre items (más limpio que `border-b` en cada item).
- Todos los elementos que no queremos que se encojan tienen `flex-shrink-0`.
- El elemento de texto tiene `flex-1 min-w-0` y `truncate` para que ocupe el espacio disponible y trunque con "..." si es demasiado largo.
- La combinación `flex items-center gap-4` crea una fila con todos los items alineados verticalmente.

### Sección B: CSS Grid con Tailwind

Si Flexbox es la herramienta para layouts unidimensionales, **CSS Grid** es la herramienta para layouts bidimensionales: cuando necesitas controlar simultáneamente filas y columnas. Grid fue introducido en CSS en 2017 y representa un salto generacional en la capacidad de maquetación web.

#### Conceptos fundamentales

Al aplicar `display: grid` (o la clase `grid` de Tailwind) a un contenedor:

1. El contenedor se convierte en un **grid container**.
2. Sus hijos directos se convierten en **grid items**.
3. Puedes definir explícitamente las columnas y filas del grid, o dejar que se generen implícitamente.
4. Los items pueden posicionarse en celdas específicas del grid usando `grid-column` y `grid-row`, o pueden fluir automáticamente.

#### Definiendo columnas y filas

```html
<!-- Grid de 3 columnas iguales -->
<div class="grid grid-cols-3 gap-4">
  <div>A</div> <div>B</div> <div>C</div>
  <div>D</div> <div>E</div> <div>F</div>
</div>

<!-- Grid de 12 columnas (sistema clásico) -->
<div class="grid grid-cols-12 gap-4">
  <div class="col-span-8">Sidebar (8/12)</div>
  <div class="col-span-4">Sidebar (4/12)</div>
</div>

<!-- Grid con columnas de diferente tamaño -->
<div class="grid grid-cols-[250px_1fr_200px] gap-4">
  <div>Sidebar (250px fijo)</div>
  <div>Contenido (1fr = resto del espacio)</div>
  <div>Panel lateral (200px fijo)</div>
</div>

<!-- Grid responsivo con auto-fit (¡sin media queries!) -->
<div class="grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-6">
  <!-- Se generan automáticamente tantas columnas como quepan de al menos 280px -->
  <!-- Cada columna se estira para ocupar el espacio disponible (1fr) -->
</div>
```

!!! info "Dato clave"

    La sintaxis `grid-cols-[250px_1fr_200px]` es una de las características más potentes de Tailwind: permite definir tracks con unidades mixtas directamente en el HTML. La unidad `fr` (fracción) es la **unidad mágica de Grid**: distribuye el espacio disponible proporcionalmente después de restar los tracks de tamaño fijo.

#### Posicionamiento de items

```html
<div class="grid grid-cols-4 gap-4">
  <div class="col-span-2">Ocupa 2 columnas</div>
  <div>Columna 3</div>
  <div>Columna 4</div>
  
  <div class="col-start-2 col-span-3">Empieza en columna 2, ocupa 3 columnas</div>
  
  <div class="col-span-full">Ocupa TODAS las columnas (full width)</div>
  
  <div class="row-span-2">Ocupa 2 filas</div>
</div>
```

Tailwind soporta `col-span-{1-12}`, `col-start-{1-13}`, `col-end-{1-13}`, y los equivalentes para filas `row-span-{1-6}`, `row-start-{1-7}`, `row-end-{1-7}`. También valores especiales como `col-span-full`, `col-start-auto`, `row-span-full`.

#### Layouts complejos con Grid

**Dashboard de análisis (tipo Google Analytics)**

```html
<div class="min-h-screen bg-gray-100">
  <!-- Header -->
  <header class="bg-white border-b px-6 py-4 flex items-center justify-between">
    <h1 class="text-2xl font-bold">Analytics Dashboard</h1>
    <div class="flex items-center gap-3">...</div>
  </header>
  
  <!-- Dashboard Grid -->
  <div class="p-6 grid grid-cols-12 gap-6">
    <!-- KPI Cards - Fila de 4 tarjetas -->
    <div class="col-span-full sm:col-span-6 lg:col-span-3 bg-white rounded-xl p-6 shadow-sm">
      <p class="text-sm text-gray-500">Total Users</p>
      <p class="text-3xl font-bold mt-1">24,521</p>
      <p class="text-sm text-green-600 mt-2">↑ 12.5%</p>
    </div>
    <div class="col-span-full sm:col-span-6 lg:col-span-3 bg-white rounded-xl p-6 shadow-sm">...</div>
    <div class="col-span-full sm:col-span-6 lg:col-span-3 bg-white rounded-xl p-6 shadow-sm">...</div>
    <div class="col-span-full sm:col-span-6 lg:col-span-3 bg-white rounded-xl p-6 shadow-sm">...</div>

    <!-- Main Chart - Ocupa 2/3 del ancho -->
    <div class="col-span-full lg:col-span-8 bg-white rounded-xl p-6 shadow-sm">
      <h2 class="text-lg font-semibold mb-4">Revenue Over Time</h2>
      <div class="h-80 bg-gray-50 rounded-lg flex items-center justify-center text-gray-400">
        [Chart placeholder]
      </div>
    </div>

    <!-- Recent Activity - 1/3 del ancho -->
    <div class="col-span-full lg:col-span-4 bg-white rounded-xl p-6 shadow-sm">
      <h2 class="text-lg font-semibold mb-4">Recent Activity</h2>
      <div class="flex flex-col gap-4">
        <div class="flex items-start gap-3 text-sm">
          <div class="w-2 h-2 rounded-full bg-blue-500 mt-1.5 flex-shrink-0"></div>
          <div>
            <p class="font-medium">New user registered</p>
            <p class="text-gray-500">2 minutes ago</p>
          </div>
        </div>
        <!-- Más items de actividad... -->
      </div>
    </div>

    <!-- Table - Full width -->
    <div class="col-span-full bg-white rounded-xl p-6 shadow-sm">
      <h2 class="text-lg font-semibold mb-4">Recent Orders</h2>
      <div class="overflow-x-auto">
        <table class="w-full text-sm">
          <thead>
            <tr class="border-b text-left">
              <th class="pb-3 font-medium">Order ID</th>
              <th class="pb-3 font-medium">Customer</th>
              <th class="pb-3 font-medium">Status</th>
              <th class="pb-3 font-medium text-right">Amount</th>
            </tr>
          </thead>
          <tbody class="divide-y">
            <tr>
              <td class="py-3">#ORD-001</td>
              <td class="py-3">Carlos López</td>
              <td class="py-3"><span class="px-2 py-0.5 text-xs rounded-full bg-green-100 text-green-800">Completed</span></td>
              <td class="py-3 text-right font-medium">€1,234.00</td>
            </tr>
            <!-- Más filas... -->
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
```

En este layout, **Grid** maneja la estructura bidimensional (KPI cards en fila, main chart + activity, tabla full-width) mientras que **Flexbox** maneja los layouts internos (contenido de cada tarjeta, lista de actividad, filas de la tabla).

**Layout de ecommerce (catálogo de productos)**

```html
<div class="min-h-screen flex flex-col">
  <!-- Header -->
  <header class="sticky top-0 z-30 bg-white border-b">
    <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
      <div class="flex items-center gap-8">
        <h1 class="text-xl font-bold">ShopName</h1>
        <nav class="hidden md:flex items-center gap-6">
          <a href="#">Men</a> <a href="#">Women</a> <a href="#">Kids</a> <a href="#">Sale</a>
        </nav>
      </div>
      <div class="flex items-center gap-4">
        <button class="relative">
          <svg><!-- Search icon --></svg>
        </button>
        <button class="relative">
          <svg><!-- Cart icon --></svg>
          <span class="absolute -top-1 -right-1 w-4 h-4 bg-red-500 text-white text-xs rounded-full flex items-center justify-center">3</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Main content: sidebar + products -->
  <div class="flex-1 flex">
    <!-- Filters Sidebar -->
    <aside class="hidden lg:block w-64 flex-shrink-0 border-r bg-white p-4">
      <h2 class="font-semibold mb-4">Filters</h2>
      
      <div class="mb-6">
        <h3 class="text-sm font-medium mb-2">Category</h3>
        <div class="flex flex-col gap-2">
          <label class="flex items-center gap-2 text-sm">
            <input type="checkbox" class="w-4 h-4" /> T-Shirts
          </label>
          <label class="flex items-center gap-2 text-sm">
            <input type="checkbox" class="w-4 h-4" /> Hoodies
          </label>
          <label class="flex items-center gap-2 text-sm">
            <input type="checkbox" class="w-4 h-4" /> Jackets
          </label>
        </div>
      </div>

      <div class="mb-6">
        <h3 class="text-sm font-medium mb-2">Price Range</h3>
        <div class="flex items-center gap-2">
          <input type="number" placeholder="Min" class="w-full px-2 py-1 border rounded text-sm" />
          <span>-</span>
          <input type="number" placeholder="Max" class="w-full px-2 py-1 border rounded text-sm" />
        </div>
      </div>

      <div class="mb-6">
        <h3 class="text-sm font-medium mb-2">Size</h3>
        <div class="grid grid-cols-4 gap-2">
          <button class="px-2 py-1 text-sm border rounded hover:bg-gray-50">XS</button>
          <button class="px-2 py-1 text-sm border rounded hover:bg-gray-50">S</button>
          <button class="px-2 py-1 text-sm border rounded bg-blue-600 text-white">M</button>
          <button class="px-2 py-1 text-sm border rounded hover:bg-gray-50">L</button>
          <button class="px-2 py-1 text-sm border rounded hover:bg-gray-50">XL</button>
        </div>
      </div>
    </aside>

    <!-- Products Grid -->
    <main class="flex-1 p-4 md:p-6">
      <!-- Toolbar -->
      <div class="flex items-center justify-between mb-6">
        <p class="text-sm text-gray-500">Showing 24 of 156 products</p>
        <select class="px-3 py-1.5 text-sm border rounded-lg">
          <option>Sort by: Featured</option>
          <option>Price: Low to High</option>
          <option>Price: High to Low</option>
          <option>Newest</option>
        </select>
      </div>

      <!-- Products Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 md:gap-6">
        <!-- Product Card (repetido para cada producto) -->
        <div class="group bg-white rounded-xl overflow-hidden border hover:shadow-lg transition-shadow">
          <div class="aspect-square bg-gray-100 relative overflow-hidden">
            <img src="product.jpg" alt="Product Name" class="w-full h-full object-cover group-hover:scale-105 transition-transform" />
            <button class="absolute bottom-3 right-3 w-10 h-10 bg-white rounded-full shadow-md flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
              <svg><!-- Heart icon --></svg>
            </button>
          </div>
          <div class="p-4">
            <p class="text-sm text-gray-500 mb-1">Brand Name</p>
            <h3 class="font-medium mb-1 truncate">Premium Cotton T-Shirt</h3>
            <div class="flex items-center gap-2">
              <span class="font-bold">€29.99</span>
              <span class="text-sm text-gray-400 line-through">€49.99</span>
            </div>
          </div>
        </div>
        <!-- Fin Product Card -->
      </div>

      <!-- Pagination -->
      <div class="flex items-center justify-center gap-2 mt-8">
        <button class="px-3 py-2 text-sm border rounded-lg hover:bg-gray-50">Previous</button>
        <button class="px-3 py-2 text-sm bg-blue-600 text-white rounded-lg">1</button>
        <button class="px-3 py-2 text-sm border rounded-lg hover:bg-gray-50">2</button>
        <button class="px-3 py-2 text-sm border rounded-lg hover:bg-gray-50">3</button>
        <span class="px-1">...</span>
        <button class="px-3 py-2 text-sm border rounded-lg hover:bg-gray-50">12</button>
        <button class="px-3 py-2 text-sm border rounded-lg hover:bg-gray-50">Next</button>
      </div>
    </main>
  </div>
</div>
```

Este layout es un compendio de técnicas: **Grid** para el catálogo de productos (responsivo con media queries de Tailwind), **Flexbox** para la estructura general (header + contenido), Flexbox para el sidebar de filtros, y Grid para las tallas. La decisión de usar Grid para los productos (en lugar de Flexbox con wrap) se debe a que Grid proporciona un control más predecible: todas las tarjetas mantendrán exactamente el mismo ancho, alineadas en filas y columnas perfectas.

### Sección C: Posicionamiento

Aunque Flexbox y Grid cubren el 95% de las necesidades de layout, hay situaciones que requieren **posicionamiento explícito**: elementos que deben salirse del flujo normal para superponerse a otros, fijarse al viewport, o posicionarse respecto a un ancestro.

#### Relative + Absolute: el dúo dinámico de los overlays

El patrón más común es `relative` en el padre + `absolute` en el hijo. El hijo absolute se posiciona respecto al ancestro posicionado más cercano (con `position` diferente a `static`):

```html
<!-- Tooltip -->
<div class="relative inline-block">
  <button class="px-3 py-1 bg-gray-200 rounded">Hover me</button>
  <div class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-3 py-2 bg-gray-900 text-white text-sm rounded-lg opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">
    Tooltip text
    <div class="absolute top-full left-1/2 -translate-x-1/2 w-2 h-2 bg-gray-900 rotate-45 -mt-1"></div>
  </div>
</div>

<!-- Dropdown -->
<div class="relative" x-data="{ open: false }">
  <button @click="open = !open" class="px-4 py-2 bg-white border rounded-lg flex items-center gap-2">
    Options
    <svg><!-- Chevron icon --></svg>
  </button>
  <div x-show="open" @click.outside="open = false" class="absolute top-full right-0 mt-1 w-48 bg-white rounded-lg shadow-lg border py-1 z-20">
    <a href="#" class="block px-4 py-2 text-sm hover:bg-gray-50">Edit</a>
    <a href="#" class="block px-4 py-2 text-sm hover:bg-gray-50">Duplicate</a>
    <a href="#" class="block px-4 py-2 text-sm hover:bg-gray-50">Archive</a>
    <hr class="my-1" />
    <a href="#" class="block px-4 py-2 text-sm text-red-600 hover:bg-red-50">Delete</a>
  </div>
</div>
```

#### Fixed: elementos pegados al viewport

Los elementos `fixed` son ideales para navegación persistente, modales y overlays de pantalla completa:

```html
<!-- Modal -->
<div class="fixed inset-0 z-50">
  <!-- Overlay oscuro -->
  <div class="absolute inset-0 bg-black/50 backdrop-blur-sm"></div>
  
  <!-- Contenido del modal centrado -->
  <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-lg bg-white rounded-2xl shadow-2xl p-6">
    <h2 class="text-xl font-bold mb-4">Modal Title</h2>
    <p class="text-gray-600 mb-6">Modal content goes here...</p>
    <div class="flex justify-end gap-3">
      <button class="px-4 py-2 border rounded-lg">Cancel</button>
      <button class="px-4 py-2 bg-blue-600 text-white rounded-lg">Confirm</button>
    </div>
  </div>
</div>
```

!!! tip "Memoriza esta combinación"

    La técnica `top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2` centra el modal perfectamente en el viewport. Es una combinación que todo desarrollador frontend debería conocer de memoria.

#### Sticky: lo mejor de relative y fixed

`position: sticky` es ideal para cabeceras de sección que se quedan pegadas al hacer scroll, o para cabeceras de tabla:

```html
<!-- Sticky header -->
<header class="sticky top-0 z-30 bg-white/80 backdrop-blur-md border-b">
  <!-- Contenido del header -->
</header>

<!-- Sticky headers de sección en una lista larga -->
<div class="flex flex-col">
  <div class="sticky top-16 bg-gray-50 px-4 py-2 text-sm font-semibold text-gray-500 z-10">
    Hoy
  </div>
  <div class="px-4 py-3 border-b">Tarea 1</div>
  <div class="px-4 py-3 border-b">Tarea 2</div>
  
  <div class="sticky top-16 bg-gray-50 px-4 py-2 text-sm font-semibold text-gray-500 z-10">
    Ayer
  </div>
  <div class="px-4 py-3 border-b">Tarea 3</div>
</div>
```

!!! warning "Trampa con sticky"

    Nota importante sobre sticky: necesita que el contenedor padre tenga altura suficiente. Si el padre no tiene scroll, sticky no tiene efecto. Además, no funciona si algún ancestro tiene `overflow: hidden`.

### Sección D: Técnicas avanzadas

#### Combinación Grid + Flexbox: la regla de oro

La práctica profesional ha consolidado una regla empírica que resuelve la duda de "¿uso Grid o Flexbox?":

> **Grid para la estructura de página (macro-layout), Flexbox para los componentes (micro-layout).**

Esta regla se basa en las fortalezas naturales de cada sistema:
- **Grid** es bidimensional: ideal para layouts que necesitan alinear elementos en filas Y columnas simultáneamente.
- **Flexbox** es unidimensional: ideal para distribuir elementos en una fila O una columna, con control fino sobre alineación y distribución de espacio.

Ejemplo de aplicación de esta regla:

```html
<!-- Grid para la estructura macro -->
<div class="grid grid-cols-[250px_1fr] h-screen">
  <!-- Sidebar: Flexbox para su contenido -->
  <aside class="flex flex-col bg-gray-900">
    <div class="p-4">...</div>
    <nav class="flex-1 overflow-y-auto">
      <div class="flex flex-col gap-4 p-4">
        <!-- Enlaces del menú -->
      </div>
    </nav>
  </aside>

  <!-- Main: Flexbox para su estructura -->
  <main class="flex flex-col min-w-0">
    <!-- Header: Flexbox -->
    <header class="flex items-center justify-between px-6 py-4">
      <div class="flex items-center gap-4">...</div>
      <div class="flex items-center gap-3">...</div>
    </header>

    <!-- Contenido: Grid para widgets del dashboard -->
    <div class="flex-1 overflow-y-auto p-6">
      <div class="grid grid-cols-12 gap-6">
        <!-- Widgets del dashboard usando Grid -->
      </div>
    </div>
  </main>
</div>
```

#### Container queries: el futuro es ahora

Las **container queries** resuelven una limitación fundamental de las **media queries**: con media queries, los estilos dependen del viewport (tamaño de la ventana del navegador), pero los componentes reutilizables viven dentro de contenedores cuyos tamaños varían independientemente del viewport.

Un componente de card grid que debe mostrar 4 columnas en una página de escritorio (1200px) pero 2 columnas en el sidebar de un dashboard (300px): con media queries, ambos contextos comparten los mismos breakpoints (definidos por el viewport, no por el contenedor). Con container queries, el componente consulta el ancho de su contenedor inmediato.

Tailwind 4 introduce soporte para container queries:

```html
<!-- Contenedor con container query habilitado -->
<div class="@container">
  <!-- Este grid se adapta al ancho del contenedor, no al viewport -->
  <div class="grid grid-cols-1 @sm:grid-cols-2 @lg:grid-cols-3 @2xl:grid-cols-4 gap-4">
    <div class="bg-white rounded-xl p-4 shadow">Card 1</div>
    <div class="bg-white rounded-xl p-4 shadow">Card 2</div>
    <div class="bg-white rounded-xl p-4 shadow">Card 3</div>
    <div class="bg-white rounded-xl p-4 shadow">Card 4</div>
  </div>
</div>
```

Los prefijos `@sm:`, `@md:`, `@lg:`, `@xl:`, `@2xl:` funcionan como las media queries de Tailwind pero referidas al tamaño del contenedor, no del viewport.

#### Layouts fluidos sin media queries

Una de las técnicas más elegantes de CSS moderno es ==crear layouts que se adaptan fluidamente sin necesidad de breakpoints explícitos==, utilizando las funciones `min()`, `max()`, `clamp()` y, en Grid, `minmax()` y `auto-fit`/`auto-fill`:

```html
<!-- Grid de tarjetas que se adapta automáticamente SIN media queries -->
<div class="grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-6">
  <!-- Cada tarjeta será como mínimo 280px de ancho -->
  <!-- Si hay espacio, se estirarán para ocupar 1 fracción cada una -->
  <!-- Si no caben, saltarán a la siguiente fila automáticamente -->
</div>
```

Esto es puro CSS moderno aplicado mediante Tailwind. La función `repeat(auto-fit, minmax(280px, 1fr))` le dice al navegador: "crea tantas columnas como quepan, cada una de al menos 280px de ancho y como máximo 1fr (se estiran si sobra espacio)".

Para anchos fluidos de contenido (por ejemplo, limitar el ancho de lectura):

```html
<article class="w-[min(100%,65ch)] mx-auto">
  <!-- El ancho es el mínimo entre 100% del contenedor y 65 caracteres -->
  <!-- En pantallas pequeñas, será 100%; en pantallas grandes, se limitará a 65ch -->
</article>
```

#### Overflows y scroll

El control del **overflow** es uno de los aspectos más olvidados y más importantes del desarrollo de interfaces. Una interfaz puede ser visualmente perfecta pero frustrante si aparecen scrolls inesperados o si los elementos se desbordan.

**Scroll vertical en áreas de contenido:**

```html
<div class="flex flex-col h-screen">
  <header class="flex-shrink-0 h-16 bg-white border-b">Header fijo</header>
  <main class="flex-1 overflow-y-auto">
    <!-- Contenido largo con scroll -->
  </main>
  <footer class="flex-shrink-0 h-12 bg-gray-900">Footer fijo</footer>
</div>
```

!!! tip "Consejo práctico"

    La clave: `flex-1 overflow-y-auto` en el área de contenido. `flex-1` hace que ocupe todo el espacio disponible, y `overflow-y-auto` añade scroll vertical cuando el contenido excede.

**Scroll horizontal en tablas anchas:**

```html
<div class="overflow-x-auto">
  <table class="min-w-[800px]">
    <!-- Tabla más ancha que el viewport, scroll horizontal automático -->
  </table>
</div>
```

**Prevenir desbordamiento de texto largo:**

```html
<p class="truncate">Texto muy largo que se truncará con puntos suspensivos...</p>
<p class="break-words">URL_muy_larga_sin_espacios_que_se_partira_automaticamente_para_evitar_desbordamiento</p>
```

Las utilidades `truncate` (equivale a `overflow: hidden; text-overflow: ellipsis; white-space: nowrap`) y `break-words` (equivale a `overflow-wrap: break-word`) son esenciales para manejar contenido generado por usuarios o URLs.

## Ejemplos guiados

### Ejemplo guiado 1: Construir un Dashboard Administrativo completo

**Objetivo:** Construir paso a paso un dashboard profesional con sidebar fijo, cabecera, área de KPI cards, gráfico principal, panel de actividad y tabla de datos.

**Duración:** 50 minutos.

**Desarrollo paso a paso:**

El docente guía al alumnado mientras implementan el dashboard descrito en la Sección B. Se enfatiza:

1. **Estructura semántica:** Usar `<aside>` para el sidebar, `<main>` para el contenido, `<header>` para la cabecera. Esto mejora la accesibilidad (landmarks ARIA implícitos).

2. **Decisiones de layout:** ¿Por qué Grid en 12 columnas para el dashboard? ¿Qué pasaría si usáramos Flexbox wrap? (las tarjetas no estarían alineadas en filas perfectas si tienen diferentes alturas).

3. **Responsive:** Probar en diferentes anchos redimensionando el navegador. Verificar que en móvil (`< sm`) todo es `col-span-full` y se apila verticalmente. Usar las breakpoints de Tailwind: `sm:` (640px), `md:` (768px), `lg:` (1024px), `xl:` (1280px), `2xl:` (1536px).

4. **Valores arbitrarios:** Para la columna del sidebar usar Tailwind puro (`col-span-3` = 25% del ancho), pero también mostrar valores arbitrarios para anchos fijos: `grid-cols-[250px_1fr]`.

5. **Inspección con DevTools:** Usar el panel de Layout de Chrome DevTools para visualizar el Grid overlay y entender cómo se posicionan los elementos.

### Ejemplo guiado 2: Construir un Panel SaaS (tipo Notion/Linear)

**Objetivo:** Construir un layout de 3 columnas típico de aplicaciones SaaS modernas.

**Diseño:**

```
+--------+------------+----------------------------------+
| Works- | Sidebar    |  Contenido principal              |
| pace   | (proyectos,|                                    |
| nav    |  docs...)  |  [Header]                         |
| (48px) | (240px)    |  [Editor / Tabla / Canvas]        |
|        |            |                                    |
+--------+------------+----------------------------------+
```

**Implementación con Tailwind:**

```html
<div class="flex h-screen bg-white">
  <!-- Columna 1: Navegación del workspace -->
  <nav class="w-12 flex-shrink-0 bg-gray-900 flex flex-col items-center py-3 gap-4">
    <div class="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center text-white font-bold text-sm">W</div>
    <div class="w-8 h-8 bg-gray-700 rounded-lg"></div>
    <div class="w-8 h-8 bg-gray-700 rounded-lg"></div>
    <div class="mt-auto w-8 h-8 bg-gray-700 rounded-full"></div>
  </nav>

  <!-- Columna 2: Sidebar de contenido -->
  <aside class="w-60 flex-shrink-0 border-r flex flex-col">
    <div class="p-4 border-b flex items-center justify-between">
      <span class="font-semibold text-sm">Proyecto Alpha</span>
      <button class="w-5 h-5">⌄</button>
    </div>
    <nav class="flex-1 overflow-y-auto p-3">
      <div class="flex flex-col gap-1">
        <a href="#" class="flex items-center gap-2 px-2 py-1.5 text-sm rounded hover:bg-gray-100">
          <span>📋</span> Tasks
        </a>
        <a href="#" class="flex items-center gap-2 px-2 py-1.5 text-sm rounded bg-gray-100">
          <span>📄</span> Documents
        </a>
        <a href="#" class="flex items-center gap-2 px-2 py-1.5 text-sm rounded hover:bg-gray-100">
          <span>📊</span> Reports
        </a>
        <a href="#" class="flex items-center gap-2 px-2 py-1.5 text-sm rounded hover:bg-gray-100">
          <span>⚙️</span> Settings
        </a>
      </div>
      
      <div class="mt-6">
        <p class="px-2 text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2">Favorites</p>
        <div class="flex flex-col gap-1">
          <a href="#" class="px-2 py-1.5 text-sm rounded hover:bg-gray-100">Onboarding Guide</a>
          <a href="#" class="px-2 py-1.5 text-sm rounded hover:bg-gray-100">API Reference</a>
        </div>
      </div>
    </nav>
    <div class="p-3 border-t">
      <button class="w-full text-left px-2 py-1.5 text-sm text-gray-500 hover:text-gray-700">+ New Page</button>
    </div>
  </aside>

  <!-- Columna 3: Área de contenido -->
  <main class="flex-1 flex flex-col min-w-0">
    <header class="flex items-center justify-between px-6 py-3 border-b">
      <div class="flex items-center gap-3">
        <h1 class="text-lg font-semibold">Q2 Planning</h1>
        <span class="px-2 py-0.5 text-xs bg-blue-100 text-blue-700 rounded">Draft</span>
      </div>
      <div class="flex items-center gap-2">
        <button class="px-3 py-1.5 text-sm border rounded-lg hover:bg-gray-50">Share</button>
        <button class="px-3 py-1.5 text-sm bg-blue-600 text-white rounded-lg">Publish</button>
      </div>
    </header>
    <div class="flex-1 overflow-y-auto p-6">
      <!-- Área de contenido (editor, tabla, canvas, etc.) -->
      <div class="max-w-3xl mx-auto">
        <p class="text-2xl font-bold mb-4">Quarter 2 Objectives</p>
        <p class="text-gray-700 leading-relaxed mb-4">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
        <!-- Más contenido... -->
      </div>
    </div>
  </main>
</div>
```

Aspectos a destacar en este layout:
- `flex h-screen` en el contenedor raíz para ocupar toda la altura.
- `flex-shrink-0` en las columnas fijas para que nunca se reduzcan.
- `flex-1 min-w-0` en el área de contenido para que ocupe el resto y permita overflow.
- `overflow-y-auto` en áreas con scroll potencial.
- Las columnas fijas usan anchos en Tailwind: `w-12` (48px iconos) y `w-60` (240px sidebar).
- El contenido tiene `max-w-3xl mx-auto` para limitar el ancho de lectura y centrarlo.

### Ejemplo guiado 3: Construir un Layout de Ecommerce

**Objetivo:** Implementar el layout de ecommerce descrito en la Sección B, enfocándose en la técnica de Grid con sidebar de filtros + catálogo de productos responsivo.

**Decisiones de layout:**

1. El contenedor principal usa `flex` para sidebar + contenido.
2. El catálogo usa `grid` para las tarjetas porque queremos columnas perfectamente alineadas.
3. Responsive: en móvil, el sidebar desaparece (`hidden lg:block`) y los productos se muestran en 1 columna.

### Ejemplo guiado 4: Construir un Chat (tipo Slack/Discord)

**Objetivo:** Construir un layout de 3 paneles (servidores, canales, chat).

**Diseño:**

```
+------+-----------+----------------------------------+
| Serv-| Canales   |  Chat                             |
| ido- |           |                                    |
| res   | # general |  [Zona de mensajes]               |
|      | # random  |                                    |
| (60) | # dev     |  [Input de texto]                |
+------+-----------+----------------------------------+
```

**Implementación:**

```html
<div class="flex h-screen bg-gray-200">
  <!-- Panel 1: Lista de servidores (iconos) -->
  <nav class="w-[60px] flex-shrink-0 bg-gray-900 flex flex-col items-center py-3 gap-2 overflow-y-auto">
    <div class="w-10 h-10 bg-blue-500 rounded-2xl flex items-center justify-center text-white font-bold">D</div>
    <div class="w-10 h-10 bg-gray-700 rounded-2xl flex items-center justify-center text-gray-300 hover:rounded-xl hover:bg-green-500 transition-all">S1</div>
    <div class="w-10 h-10 bg-gray-700 rounded-2xl flex items-center justify-center text-gray-300 hover:rounded-xl hover:bg-green-500 transition-all">S2</div>
    <div class="w-10 h-10 bg-gray-700 rounded-2xl flex items-center justify-center text-gray-300 hover:rounded-xl hover:bg-green-500 transition-all">+</div>
  </nav>

  <!-- Panel 2: Lista de canales -->
  <aside class="w-60 flex-shrink-0 bg-gray-800 flex flex-col">
    <div class="px-4 py-3 border-b border-gray-700 flex items-center justify-between">
      <span class="font-semibold text-white text-sm">Servidor 1</span>
      <button class="text-gray-400 hover:text-white">⌄</button>
    </div>
    <div class="flex-1 overflow-y-auto py-2">
      <div class="px-2 mb-4">
        <div class="flex items-center justify-between px-2 mb-1">
          <span class="text-xs font-semibold text-gray-400 uppercase">Canales de texto</span>
          <button class="text-gray-400 hover:text-white text-lg">+</button>
        </div>
        <a href="#" class="flex items-center gap-1.5 px-2 py-1 rounded text-gray-300 hover:bg-gray-700 hover:text-white">
          <span class="text-lg">#</span> <span class="text-sm">general</span>
        </a>
        <a href="#" class="flex items-center gap-1.5 px-2 py-1 rounded bg-gray-700 text-white">
          <span class="text-lg">#</span> <span class="text-sm">desarrollo</span>
        </a>
        <a href="#" class="flex items-center gap-1.5 px-2 py-1 rounded text-gray-300 hover:bg-gray-700 hover:text-white">
          <span class="text-lg">#</span> <span class="text-sm">random</span>
        </a>
      </div>
    </div>
    <div class="px-3 py-2 bg-gray-900 flex items-center gap-2">
      <div class="w-8 h-8 bg-gray-600 rounded-full flex-shrink-0"></div>
      <div class="min-w-0">
        <p class="text-sm text-white truncate">usuario123</p>
        <p class="text-xs text-gray-400">#online</p>
      </div>
      <div class="flex items-center gap-1 ml-auto">
        <button class="text-gray-400 hover:text-white">🔇</button>
        <button class="text-gray-400 hover:text-white">⚙️</button>
      </div>
    </div>
  </aside>

  <!-- Panel 3: Chat -->
  <main class="flex-1 flex flex-col min-w-0 bg-gray-100">
    <!-- Header del chat -->
    <header class="flex-shrink-0 px-4 py-3 bg-white border-b flex items-center gap-2">
      <span class="text-xl font-bold text-gray-500">#</span>
      <div>
        <h2 class="font-semibold">desarrollo</h2>
        <p class="text-xs text-gray-500">Discusión sobre el sprint actual</p>
      </div>
      <div class="ml-auto flex items-center gap-3">
        <button class="text-gray-400 hover:text-gray-600">🔍</button>
        <button class="text-gray-400 hover:text-gray-600">📌</button>
        <button class="text-gray-400 hover:text-gray-600">🔔</button>
      </div>
    </header>

    <!-- Zona de mensajes -->
    <div class="flex-1 overflow-y-auto px-4 py-4">
      <!-- Mensaje de ejemplo -->
      <div class="flex items-start gap-3 mb-4 hover:bg-gray-50 -mx-2 px-2 py-1 rounded-lg">
        <img src="avatar.jpg" class="w-8 h-8 rounded-full mt-0.5 flex-shrink-0" alt="User" />
        <div>
          <div class="flex items-baseline gap-2">
            <span class="font-semibold text-sm">María López</span>
            <span class="text-xs text-gray-400">Hoy a las 10:45</span>
          </div>
          <p class="text-sm text-gray-800">¡Buenos días equipo! He subido los cambios del PR #42.</p>
        </div>
      </div>
      <!-- Más mensajes... -->
    </div>

    <!-- Input de mensaje -->
    <div class="flex-shrink-0 px-4 py-3 bg-white border-t">
      <div class="flex items-end gap-2 bg-gray-100 rounded-lg px-4 py-2">
        <button class="text-gray-400 hover:text-gray-600 text-lg flex-shrink-0">+</button>
        <textarea 
          rows="1" 
          placeholder="Escribe un mensaje..." 
          class="flex-1 bg-transparent resize-none text-sm py-1 outline-none max-h-32"
        ></textarea>
        <button class="text-gray-400 hover:text-gray-600 flex-shrink-0">😊</button>
        <button class="text-gray-400 hover:text-gray-600 flex-shrink-0">📎</button>
      </div>
    </div>
  </main>
</div>
```

Este layout de chat es un excelente ejemplo de composición de **Flexbox**: tres paneles en `flex` horizontal, cada panel estructurado con `flex-col`, áreas de scroll con `overflow-y-auto`, y cajas de input con `flex-shrink-0`.

## Actividades guiadas

### Actividad guiada 1: Depuración de layouts

**Duración:** 25 minutos

**Desarrollo:** El docente proporciona 3 layouts con errores intencionados (uno de Flexbox, uno de Grid, uno de posicionamiento). El alumnado debe:
1. Abrir las DevTools y usar el panel Elements + Styles para inspeccionar.
2. Activar los overlays de Flexbox y Grid (en el panel Layout de DevTools) para visualizar la distribución.
3. Identificar el error.
4. Corregirlo cambiando las clases de Tailwind adecuadas.

Errores comunes a incluir:
- Sidebar con `flex-1` en lugar de `flex-shrink-0` (se encoge con contenido largo).
- `min-width: auto` implícito causando desbordamiento (falta `min-w-0`).
- Contenedor flex sin `flex-col` cuando se pretendía layout vertical.
- `absolute` sin ancestro `relative`.
- Olvidar `inset-0` en un overlay.
- `sticky` sin altura en el contenedor padre.

### Actividad guiada 2: Layout responsive con media queries

**Duración:** 30 minutos

**Desarrollo:** Partiendo del dashboard del Ejemplo Guiado 1, el alumnado aplica las siguientes adaptaciones responsive:

1. En móvil (< 640px): sidebar se oculta (`hidden sm:block` o se convierte en un drawer/off-canvas), las KPI cards pasan a 1 columna, el main chart y el panel de actividad se apilan verticalmente.
2. En tablet (640px - 1024px): sidebar se mantiene visible pero más estrecho (`w-48 sm:w-56 lg:w-64`), KPI cards en 2 columnas (`col-span-full sm:col-span-3`), main chart y activity se apilan.
3. En escritorio (> 1024px): layout completo con sidebar ancho, 4 KPI cards en fila, main chart + activity en layout de 2/3 + 1/3.

El docente enfatiza la filosofía **mobile-first** de Tailwind: las clases base definen el layout móvil, y las clases con prefijo (`sm:`, `lg:`) añaden modificaciones para pantallas más grandes.

### Actividad guiada 3: Conversión de diseño Figma a layout

**Duración:** 30 minutos

**Desarrollo:** El docente proporciona 3 diseños de Figma (capturas de pantalla o archivo Figma con Dev Mode accesible). El alumnado debe:
1. Analizar la estructura del diseño: ¿dónde usa Grid? ¿dónde Flexbox? ¿hay posicionamiento absolute/fixed?
2. Traducir mentalmente las estructuras de Auto Layout de Figma a Flexbox/Grid de Tailwind (recordando la equivalencia de la Unidad 4: Auto Layout horizontal = flex-row, Auto Layout vertical = flex-col).
3. Escribir el código HTML + Tailwind correspondiente (no completo, solo la estructura de layout, con placeholders para el contenido).
4. Comparar la implementación con el diseño: ¿Las dimensiones coinciden? ¿Los espaciados son correctos? ¿La jerarquía es la misma?

## Actividades propuestas

### Actividad 1

**Nivel:** Básico
**Objetivo:** Practicar los fundamentos de Flexbox con Tailwind mediante la construcción de layouts unidimensionales.
**Enunciado:** Crea una página HTML (puede ser un componente standalone de Angular) que incluya los siguientes layouts construidos exclusivamente con Flexbox y Tailwind:

1. **Barra de navegación horizontal:** Logo a la izquierda, 4 enlaces en el centro, icono de carrito y avatar a la derecha. Usa `justify-between` o auto-márgenes.

2. **Lista de tareas vertical:** 5 ítems, cada uno con checkbox + texto (que debe truncarse si es muy largo) + badge de prioridad. Usa `flex flex-col` con `divide-y` y cada ítem con `flex items-center gap-3`.

3. **Centrado perfecto de un formulario de login:** Un contenedor que ocupe toda la pantalla (`h-screen`) y tenga un formulario de login centrado horizontal y verticalmente. El formulario debe tener un ancho máximo de 400px.

4. **Footer con 4 columnas:** En escritorio, 4 columnas iguales. En tablet, 2 columnas. En móvil, 1 columna. Cada columna contiene un título y una lista de enlaces.

**Requisitos:** Debe funcionar responsive (probar en móvil, tablet, escritorio). No usar CSS Grid (practica Flexbox). Todos los elementos deben tener nombres de clase de Tailwind, sin CSS personalizado.
**Pistas:** Para centrar el formulario de login, usa la combinación `flex items-center justify-center` en el contenedor padre que ocupa toda la pantalla.
**Criterios de evaluación:** (1) Correcto uso de Flexbox (no usar Grid). (2) Responsive real (verificar en DevTools con diferentes viewports). (3) Truncado de texto largo en la lista de tareas (verificar con texto muy largo). (4) Consistencia en el espaciado (uso de escala de Tailwind).

### Actividad 2

**Nivel:** Medio
**Objetivo:** Construir dashboards y layouts complejos con CSS Grid.
**Enunciado:** Crea un componente Angular standalone llamado `DashboardComponent` que implemente un dashboard de análisis con la siguiente estructura:

El dashboard usa un grid de 12 columnas con los siguientes elementos:
- **Fila 1 - KPI Cards (4 tarjetas):** Cada tarjeta ocupa 3 columnas en escritorio, 6 en tablet, 12 en móvil. Muestran: icono, título (e.g., "Total Revenue"), valor ($45,231.89), variación porcentual (+20.1% en verde o -5.2% en rojo).
- **Fila 2 - Gráfico principal:** Ocupa 8 columnas en escritorio, 12 en tablet/móvil. Placeholder para un gráfico (un rectángulo con altura fija 400px).
- **Fila 2 - Panel lateral (en las 4 columnas restantes):** Lista de "Recent Transactions" con 5 items. Cada item: avatar, nombre, descripción, cantidad, timestamp relativo ("hace 2 horas").
- **Fila 3 - Tabla de datos:** Ocupa las 12 columnas completas. Tabla con columnas: Invoice, Status (badge coloreado), Method, Amount. Al menos 6 filas de datos.

Además, el dashboard debe tener:
- Sidebar izquierdo (colapsable con un botón de hamburguesa) que contiene el logo y navegación.
- Header superior con título de la página, campo de búsqueda y avatar de usuario.
- El sidebar y el header deben ser componentes separados, reutilizables.

**Requisitos:** Todo el layout debe usar CSS Grid para la estructura del dashboard. Flexbox solo para layouts internos de componentes individuales. Responsive: sidebar se oculta en móvil, KPI cards se apilan, gráfico y panel lateral se apilan. Usar Angular standalone components y Tailwind CSS.
**Pistas:** Define primero la estructura del grid en el template. Luego implementa cada componente hijo. Para el sidebar colapsable, usa una signal `isSidebarOpen` que se comunique del componente padre al sidebar mediante un input.
**Criterios de evaluación:** (1) Correcta estructura Grid del dashboard (inspeccionar con DevTools Grid overlay). (2) Responsive funcional. (3) Componentización correcta (sidebar, header y dashboard en componentes separados). (4) Tipado TypeScript de los datos (interfaces para KPI, Transaction, Invoice).

### Actividad 3

**Nivel:** Medio
**Objetivo:** Implementar posicionamiento avanzado con overlays, modales y tooltips.
**Enunciado:** Crea un componente `AdvancedPositioningComponent` que demuestre el uso de posicionamiento CSS con Tailwind:

1. **Tooltip:** Un botón que al hacer hover (usando `group-hover:`) muestre un tooltip posicionado encima del botón. El tooltip debe tener una flecha triangular (usando CSS borders o `rotate-45`).

2. **Dropdown:** Un botón que al hacer clic despliegue un menú. El menú debe cerrarse al hacer clic fuera (puedes usar Angular event handling o simplemente documentar que en producción usarías algo como Angular CDK Overlay).

3. **Modal:** Un botón que al hacer clic abra un modal centrado en pantalla. El modal debe tener: overlay oscuro semitransparente con blur (`backdrop-blur-sm`), contenido del modal centrado, botón de cierre (X) en la esquina superior derecha, y debe cerrarse al hacer clic en el overlay o presionar Escape.

4. **Sticky header de sección:** Una lista larga (50 ítems) con encabezados de sección sticky que se pegan al llegar a la parte superior de la pantalla.

5. **Notificación toast:** Un botón que al hacer clic muestre una notificación en la esquina inferior derecha (`fixed bottom-4 right-4`) que desaparece automáticamente después de 3 segundos. Implementa la animación de entrada (slide + fade).

**Requisitos:** El modal y las notificaciones deben manejarse correctamente sin perder scroll del body cuando el modal está abierto. El modal debe ser accesible: foco atrapado dentro del modal (puedes implementarlo manualmente o usar Angular CDK).
**Pistas:** Para la flecha del tooltip, usa un pseudo-elemento `::after` o un div adicional con `rotate-45`. Para el toast, usa `setTimeout` o `setInterval` combinado con signals de Angular para controlar la visibilidad.
**Criterios de evaluación:** (1) Correcto posicionamiento de todos los elementos (inspeccionar con DevTools). (2) Funcionalidad de apertura/cierre de modal y dropdown. (3) Accesibilidad básica del modal (Escape para cerrar, foco). (4) Calidad de las animaciones de entrada/salida.

### Actividad 4

**Nivel:** Avanzado
**Objetivo:** Construir una aplicación de chat completa (tipo Slack/Discord/WhatsApp Web).
**Enunciado:** Implementa una aplicación de chat completa en Angular standalone + Tailwind con la siguiente arquitectura:

1. **Layout principal:** Sidebar de servidores (iconos), sidebar de canales, área de chat (mensajes + input). Exactamente como el Ejemplo Guiado 4 pero con funcionalidad real.

2. **Gestión de estado:** Usa Angular signals para gestionar: servidor activo, canal activo, lista de mensajes del canal (array de objetos Mensaje con id, autor, avatar, texto, timestamp). Los mensajes se "envían" localmente (no se necesita backend, solo añadir al array).

3. **Componentes hijos (mínimo 5):**
   - `ServerListComponent`: Lista de iconos de servidores.
   - `ChannelListComponent`: Lista de canales del servidor activo.
   - `MessageListComponent`: Lista de mensajes con scroll automático al final al recibir/enviar uno nuevo.
   - `MessageInputComponent`: Campo de texto con emoji picker placeholder, soporte para Enter para enviar, auto-resize del textarea.
   - `ChatHeaderComponent`: Nombre del canal + botones de acción.

4. **Layout responsive:** En móvil (< 768px), solo se muestra una columna cada vez (servidores → canales → chat). Implementa navegación hacia atrás (botón "←" para volver de chat a canales, de canales a servidores).

5. **Funcionalidades adicionales:**
   - Agrupación de mensajes del mismo autor (no repetir avatar).
   - Indicador de "está escribiendo..." cuando el textarea tiene contenido.
   - Timestamp en los mensajes con formato relativo ("hace 2 minutos", "ayer a las 15:30").
   - Búsqueda de mensajes (filtrar en cliente).

**Requisitos:** Todo con Angular Signals. Sin servicios HTTP (todo datos locales). Tipos TypeScript para todos los modelos de datos. Tests unitarios para al menos 2 componentes (MessageList, MessageInput).
**Pistas:** Para el scroll automático al final en MessageList, usa `ViewChild` + `ElementRef` y llama a `scrollIntoView()` después de añadir un mensaje. Para formatear timestamps relativos, puedes usar `Intl.RelativeTimeFormat` o una pequeña función utilitaria.
**Criterios de evaluación:** (1) Arquitectura de componentes correcta. (2) Gestión de estado con Signals (reactividad, no manipulación directa del DOM). (3) Responsive en móvil con navegación entre paneles. (4) Calidad del código TypeScript (interfaces, tipos, sin `any`). (5) Tests unitarios funcionales.

### Actividad 5

**Nivel:** Avanzado
**Objetivo:** Implementar layout builder (constructor de layouts) con drag-and-drop usando Angular CDK.
**Enunciado:** Crea un "Layout Builder", una interfaz que permite al usuario construir su propio dashboard arrastrando y soltando widgets en una cuadrícula. Inspírate en herramientas como Grafana, Notion o WordPress Gutenberg.

1. **Grid subyacente:** El área de construcción es un grid de 12 columnas con un número variable de filas (gap de 16px). El grid tiene un tamaño mínimo de 800px de ancho y se renderiza con líneas visuales sutiles (modo "cuadrícula").

2. **Widgets disponibles (sidebar de widgets):** Panel lateral que lista los tipos de widgets disponibles: "KPI Card", "Chart" (3 tamaños: small/medium/large), "Table", "Text", "Activity Feed". Cada tipo es un componente Angular separado con su propia lógica.

3. **Funcionalidad drag-and-drop:** Usa Angular CDK Drag and Drop (`@angular/cdk/drag-drop`). Los widgets pueden arrastrarse desde el panel lateral al grid, y reposicionarse dentro del grid arrastrándolos. Deben ocupar múltiples celdas según su tamaño (small = 3 cols × 1 row, medium = 6 cols × 2 rows, large = 12 cols × 3 rows).

4. **Redimensionamiento:** Widgets redimensionables desde las esquinas (usando resize handles). Al redimensionar, el widget debe "snappear" a múltiplos de la celda del grid.

5. **Persistencia:** El layout se guarda en localStorage y se restaura al recargar la página. Usa un modelo de datos que represente el layout (array de widgets con sus posiciones y tamaños).

6. **Modo previsualización / modo edición:** Toggle para cambiar entre modo edición (se ven las líneas del grid, los widgets tienen handles de drag y resize) y modo previsualización (el grid se oculta, los widgets se ven como en un dashboard real).

**Requisitos:** Usar Angular CDK para drag-and-drop. Usar CSS Grid para el layout (no posicionamiento absolute). Usar Angular Signals para el estado. Los widgets deben ser componentes standalone separados con contenido placeholder realista (no solo colores de fondo).
**Pistas:** Angular CDK tiene un módulo `DragDropModule` (standalone desde Angular 15+) que proporciona las directivas `cdkDrag`, `cdkDropList`, `cdkDragHandle`. Para el resize, puedes usar `cdkDrag` en los handles de las esquinas y actualizar las dimensiones en la signal. Para el snap a grid, calcula la celda más cercana al soltar.
**Criterios de evaluación:** (1) Correcto funcionamiento del drag-and-drop. (2) Estructura de datos del layout (modelos tipados). (3) Persistencia en localStorage. (4) Componentización (cada tipo de widget es un componente independiente). (5) Experiencia de usuario pulida (animaciones de transición, feedback visual al arrastrar).

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Implementación de un sistema de layout con Container Queries

    Investiga a fondo las container queries y su soporte en Tailwind CSS 4. Crea una aplicación de demostración que muestre las diferencias entre media queries y container queries. La demo debe incluir:

    1. **Un componente "CardGrid"** que se renderiza en dos contextos diferentes en la misma página: dentro de un contenedor estrecho (300px, simulando un sidebar) y dentro de un contenedor ancho (900px, simulando un área de contenido principal).

    2. **Primera versión (media queries):** El CardGrid usa `sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4`. Muestra que en el sidebar estrecho, las media queries no pueden detectar el espacio reducido y las cartas se desbordan o se ven incorrectas.

    3. **Segunda versión (container queries):** El CardGrid usa `@container` y `@sm:grid-cols-1 @md:grid-cols-2 @lg:grid-cols-3`. Muestra cómo el mismo componente se adapta correctamente al ancho de su contenedor en ambos contextos.

    4. **Visualización side-by-side** con etiquetas que indiquen qué técnica se está usando y por qué una funciona y la otra no.

    Entrega: repositorio GitHub con la demo funcional y un README que explique el concepto de container queries y cuándo usarlas.

    ### Actividad de ampliación 2: Testing visual de layouts con Storybook y Chromatic

    Configura un proyecto Angular con Storybook y Chromatic (o Percy como alternativa gratuita) para realizar testing visual automatizado de layouts. Debes:

    1. Crear stories para los 4 layouts principales del módulo (Dashboard, SaaS, Ecommerce, Chat). Cada story debe mostrar el layout completo.

    2. Configurar Chromatic para que capture screenshots de cada story en diferentes viewports (móvil: 375px, tablet: 768px, escritorio: 1440px).

    3. Crear 3 variaciones de cada layout (ej: sidebar colapsado, modal abierto, tema oscuro) y asegurar que cada variación tiene su propia story.

    4. Configurar el pipeline CI/CD (GitHub Actions) para que ejecute Chromatic en cada PR y bloquee el merge si hay cambios visuales no aprobados.

    5. Documentar el flujo completo: cómo desarrollar un layout, cómo escribir sus stories, cómo ejecutar Chromatic localmente para previsualizar, cómo funciona el proceso de revisión en PR.

    Entrega: repositorio configurado + informe documentando el proceso y las lecciones aprendidas sobre testing visual.

    ### Actividad de ampliación 3: Layout engine personalizado para aplicaciones de datos

    Diseña e implementa un "layout engine" para paneles de datos que se adapte automáticamente al tipo de datos que recibe. El motor debe:

    1. Recibir un array de "paneles" donde cada panel tiene: tipo de visualización (kpi, chart, table, list, text), datos (genéricos, tipados), y prioridad (high, medium, low).

    2. Analizar los paneles y decidir automáticamente el layout más adecuado:
       - Si hay 1-2 KPIs: se muestran grandes y centrados.
       - Si hay 3-4 KPIs: grid de 2×2.
       - Si hay un chart y KPIs: el chart ocupa 2/3, los KPIs 1/3.
       - Los paneles de baja prioridad se muestran más pequeños o colapsados al final de la página.

    3. El layout debe ser responsive: adaptarse a diferentes tamaños de pantalla sin perder la jerarquía de prioridad.

    4. Utilizar CSS Grid con `grid-template-areas` (traducido a clases Tailwind mediante valores arbitrarios) para definir áreas nombradas y asignar paneles a dichas áreas según el análisis.

    5. Implementar animaciones de transición cuando los paneles se reordenan (usando FLIP animation technique o la API View Transitions si está disponible).

    Entrega: componente Angular standalone + documentación del algoritmo de decisión de layout.

!!! tip "Buenas prácticas"

    1. **Empieza siempre con el layout más pequeño (móvil) y ve ampliando con breakpoints.** El enfoque mobile-first de Tailwind (clases base para móvil, prefijos `sm:`, `md:`, etc. para pantallas más grandes) es más mantenible y produce menos código que el enfoque desktop-first. Además, te obliga a priorizar el contenido esencial.

    2. **Grid para estructura macro, Flexbox para componentes micro.** Esta regla cubre el 95% de las decisiones de layout. Si tienes dudas, pregúntate: ¿necesito controlar filas Y columnas simultáneamente? Grid. ¿Necesito distribuir elementos en UNA dirección? Flexbox.

    3. **Nunca olvides `min-w-0` en elementos flex que contienen texto largo o elementos con overflow.** Sin `min-w-0`, el comportamiento por defecto de los flex items (`min-width: auto`) impide que se encojan por debajo del ancho de su contenido, causando desbordamientos misteriosos que son difíciles de depurar si no conoces esta peculiaridad.

    4. **Usa `gap` en lugar de márgenes para espaciar elementos en flex y grid.** `gap` es más semántico (el espaciado pertenece al layout del contenedor, no a los hijos), más mantenible (un solo valor que cambiar) y evita problemas de márgenes sobrantes en el primer/último elemento.

    5. **Establece una escala de espaciado y respétala religiosamente.** Usa siempre la escala de Tailwind (múltiplos de 4px). La consistencia en el espaciado es lo que separa una interfaz que se siente "bien" de una que se siente "rara". Nunca uses valores arbitrarios para padding, margin o gap a menos que sea absolutamente necesario.

    6. **Prueba tus layouts en múltiples viewports y navegadores.** Chrome en un MacBook Pro con pantalla retina no es representativo de tus usuarios reales. Prueba en: móvil (375px), tablet (768px), laptop pequeño (1024px), escritorio grande (1440px+). Verifica que no aparecen scrolls horizontales no deseados.

    7. **Usa las DevTools de layout (Flexbox overlay, Grid overlay) para depurar.** Chrome y Firefox ofrecen visualizaciones excelentes de Flexbox y Grid. Actívalas en el panel Layout de las DevTools. Verás líneas de colores que muestran ejes, gaps, áreas del grid y alineación. Son mucho más informativas que intentar deducirlo visualmente.

    8. **Semántica HTML y accesibilidad en la estructura de layout.** Usa elementos semánticos (`<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`) para las secciones principales del layout. Esto proporciona landmarks ARIA implícitos que los lectores de pantalla utilizan para navegar. No uses solo `<div>` para todo.

!!! warning "Errores frecuentes"

    1. **Olvidar `flex-col` en contenedores que deben apilar elementos verticalmente.** Por defecto, `flex` es `flex-row`. Si quieres una columna vertical y solo pones `flex`, los elementos se alinearán horizontalmente. Siempre usa `flex flex-col` explícitamente para layouts verticales.

    2. **Usar `justify-between` cuando quieres `space-between` con más espacio.** `justify-between` distribuye el espacio entre elementos sin espacio en los extremos. Si quieres que los elementos tengan espacio alrededor, usa `justify-around` o `justify-evenly`. Son comportamientos diferentes que a menudo se confunden.

    3. **Anidar `absolute` sin `relative` en el ancestro.** Un elemento con `position: absolute` se posiciona respecto al ancestro posicionado más cercano. Si ningún ancestro tiene `relative`, `absolute`, `fixed` o `sticky`, el elemento se posicionará respecto al `<body>`, lo que casi nunca es lo deseado. Siempre pon `relative` en el contenedor padre.

    4. **Aplicar propiedades de flex item a un elemento que no es hijo directo de un flex container.** Solo los hijos directos de un elemento con `display: flex` se convierten en flex items. Si tienes una jerarquía anidada y aplicas `flex-1` a un nieto, no funcionará a menos que haya un flex container intermedio.

    5. **`col-span-` que no suma 12 (o el número de columnas del grid).** Si tienes `grid-cols-4` y un elemento con `col-span-3` y otro sin especificar (ocupa 1 por defecto), la suma es 4. Correcto. Si tienes `grid-cols-3` y pones `col-span-3` + `col-span-2`, la suma es 5 y se desborda a la siguiente fila, lo que probablemente no es lo deseado.

    6. **No manejar el overflow en áreas de contenido.** Creas un layout con un sidebar y una zona de contenido. El contenido se sale del viewport y aparece un scroll en el body. La solución es: contenedor `h-screen` (altura fija = viewport), sidebar `h-full`, zona de contenido `overflow-y-auto`. Sin `h-screen`, elayout crece con el contenido y nunca aparecerá el scroll donde quieres.

    7. **Usar `sticky` en un contexto donde no funciona.** `position: sticky` requiere: (a) que el elemento tenga un valor de `top`, `bottom`, `left` o `right` definido (ej: `top-0`), (b) que ningún ancestro entre el elemento sticky y el viewport tenga `overflow: hidden` (esto rompe sticky), y (c) que el contenedor padre tenga altura suficiente para que haya scroll. Si sticky "no funciona", comprueba estas tres condiciones.

    8. **Abusar de valores arbitrarios.** Tailwind permite valores arbitrarios como `w-[327px]` o `p-[7px]`. Son útiles en casos puntuales (valores que realmente no están en la escala), pero abusar de ellos destruye la consistencia del sistema de diseño. Si te encuentras usando el mismo valor arbitrario 3 veces, defínelo como un token en `@theme`.

!!! abstract "Resumen"

    Esta unidad ha sido un recorrido exhaustivo por las técnicas modernas de layout para interfaces web, siempre con el foco en la práctica profesional con Tailwind CSS y la implementación en Angular. Hemos partido de **Flexbox**, el sistema de layout unidimensional, y lo hemos desglosado hasta sus aspectos más avanzados: el modelo de ejes (main y cross), la diferencia crucial entre `flex-1` y `flex-auto`, la técnica de auto-márgenes, y el siempre olvidado `min-w-0`. Hemos traducido patrones clásicos de escritorio (VBox, HBox, StackPane) a sus equivalentes en Flexbox y Tailwind, y hemos construido layouts profesionales como sidebars, barras de herramientas y listas de elementos.

    **CSS Grid** nos ha proporcionado la herramienta bidimensional que complementa a Flexbox. Hemos aprendido a definir columnas y filas, posicionar elementos con span y start/end, y crear layouts que antes requerían frameworks CSS completos: dashboards con 12 columnas, layouts de ecommerce con sidebars de filtros, y patrones de 3 columnas para aplicaciones SaaS. La regla de oro ("Grid para estructura macro, Flexbox para componentes micro") se ha consolidado como criterio de decisión práctica.

    El posicionamiento (relative, absolute, fixed, sticky) ha cubierto los casos que Flexbox y Grid no pueden manejar: tooltips, dropdowns, modales, cabeceras fijas y elementos sticky. Cada patrón tiene su receta concreta: `relative` en el padre + `absolute` en el hijo para overlays, `fixed inset-0` para modales a pantalla completa, `sticky top-0` para cabeceras pegajosas.

    Las técnicas avanzadas —**container queries**, layouts fluidos con `auto-fit` y `minmax`, funciones `clamp()`, y la combinación juiciosa de Grid con Flexbox— nos han equipado para resolver prácticamente cualquier desafío de layout que podamos encontrar en el desarrollo profesional.

    Los cuatro layouts completos (Dashboard, SaaS, Ecommerce, Chat) han servido como demostración práctica de que estas técnicas no son teoría abstracta, sino herramientas para construir interfaces reales, complejas y adaptables.

    En la Unidad 15 (del diseño a la implementación) cerraremos el ciclo completo: tomaremos diseños de Figma, extraeremos sus design tokens, configuraremos nuestro tema de Tailwind, implementaremos los componentes en Angular, los documentaremos en Storybook, y construiremos pantallas completas. Todo lo aprendido en Flexbox, Grid y posicionamiento será la base sobre la que se asentarán esas implementaciones.

## Recursos complementarios

### Documentación oficial

- **Tailwind CSS - Flexbox:** https://tailwindcss.com/docs/flex
- **Tailwind CSS - Grid:** https://tailwindcss.com/docs/grid-template-columns
- **Tailwind CSS - Position:** https://tailwindcss.com/docs/position
- **Tailwind CSS - Container Queries:** https://tailwindcss.com/docs/container-queries (verificar en docs de v4)
- **MDN - Flexbox:** https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout
- **MDN - CSS Grid:** https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout
- **MDN - Position:** https://developer.mozilla.org/en-US/docs/Web/CSS/position
- **Angular CDK - Drag & Drop:** https://material.angular.io/cdk/drag-drop/overview

### Guías de referencia

- **CSS-Tricks: A Complete Guide to Flexbox:** https://css-tricks.com/snippets/css/a-guide-to-flexbox/ — La guía más completa y visual de Flexbox. Imprescindible.
- **CSS-Tricks: A Complete Guide to CSS Grid:** https://css-tricks.com/snippets/css/complete-guide-grid/ — El equivalente para Grid.
- **Flexbox Froggy:** https://flexboxfroggy.com — Juego interactivo para aprender Flexbox mediante la colocación de ranas.
- **Grid Garden:** https://cssgridgarden.com — Juego interactivo para aprender CSS Grid regando un jardín.
- **Learn CSS Grid (Josh Comeau):** https://www.joshwcomeau.com/css/interactive-guide-to-grid/ — Guía interactiva y visualmente impresionante de CSS Grid.
- **Learn Flexbox (Josh Comeau):** https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/ — Similar para Flexbox.

### Herramientas

- **Chrome DevTools - Panel Layout:** Permite visualizar overlays de Grid y Flexbox. Accesible en DevTools → More tools → Layout.
- **Firefox DevTools - Grid Inspector:** Firefox tiene el inspector de Grid más avanzado. Muestra números de línea, nombres de área y gaps.
- **Tailwind CSS IntelliSense (VS Code):** Autocompletado de clases, previsualización de colores, linting de clases conflictivas.
- **CSS Grid Generator:** https://cssgrid-generator.netlify.app — Generador visual de layouts Grid.
- **Flexbox Playground:** https://codepen.io/enxaneta/full/adLPwv — Visualización interactiva de todas las propiedades de Flexbox.

### Libros

- Andrew, R. (2023). *CSS Master*. SitePoint. Cobertura exhaustiva de CSS moderno incluyendo Grid, Flexbox, Custom Properties, Container Queries.
- Meyer, E. y Weyl, E. (2023). *CSS: The Definitive Guide*. O'Reilly. La biblia de CSS, para consulta de referencia.
- Wathan, A. y col. (2023). *Refactoring UI*. Independiente. No específico de layout, pero contiene excelentes principios sobre espaciado, jerarquía y sistemas de diseño aplicables al layout.
