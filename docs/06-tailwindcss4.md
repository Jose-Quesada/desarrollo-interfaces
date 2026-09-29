---
icon: lucide/wind
---

# Tailwind CSS 4 en Desarrollo de Interfaces

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Comprender y aplicar la filosofía utility-first en el contexto del desarrollo de interfaces empresariales con Angular, diferenciando claramente los casos donde Tailwind aporta ventajas competitivas sobre el CSS tradicional y aquellos donde el CSS puro puede ser más apropiado, siempre desde la premisa fundamental de que Tailwind es CSS con otro nombre y requiere un dominio sólido de los fundamentos de CSS para ser utilizado correctamente.
2. Configurar e integrar Tailwind CSS 4 en un proyecto Angular desde cero, utilizando el enfoque moderno basado en Vite con el plugin `@tailwindcss/vite`, y personalizar el sistema de diseño mediante la directiva `@theme` en CSS, definiendo tokens de color (usando espacios de color modernos como oklch), familias tipográficas, escalas de espaciado, breakpoints y otras variables del sistema de diseño.
3. Organizar eficazmente el código CSS en un proyecto Angular con Tailwind, estableciendo la estrategia adecuada de estilos globales, estilos por componente y uso (limitado y justificado) de la directiva `@apply`, evitando los antipatrones más comunes que degradan la mantenibilidad del código.
4. Dominar el vocabulario completo de clases utility de Tailwind para construir interfaces de aplicación completas, cubriendo layout (flex, grid, container), espaciado, colores, tipografía, estados interactivos (hover, focus, active, disabled), modo oscuro, diseño responsive, formularios y accesibilidad.
5. Aplicar técnicas avanzadas de Tailwind como valores arbitrarios, variantes personalizadas, las directivas `peer` y `group` para estilización contextual, y el selector `has-*` para estilos basados en el estado de elementos descendientes, comprendiendo el funcionamiento del motor JIT que genera solo el CSS utilizado.
6. Utilizar la extensión Tailwind CSS IntelliSense para VS Code como herramienta de productividad, aprovechando el autocompletado de clases, la previsualización de colores, el linting de clases inválidas y la documentación inline de los valores de cada clase.
7. Planificar y ejecutar una estrategia de adopción progresiva de Tailwind en un proyecto Angular existente, minimizando la fricción con el código CSS heredado y gestionando la coexistencia hasta la migración completa.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 4** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 4.** Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE g) Se ha diseñado el aspecto de la interfaz de usuario (colores y fuentes entre otros) atendiendo a su legibilidad.

> Nota: Tailwind CSS 4 es el framework de estilos con el que se materializa este criterio. A lo largo de la unidad se configura el tema mediante `@theme`, se aplican utilidades de layout, tipografía, color, estados interactivos y diseño responsive, y se emplean técnicas avanzadas (valores arbitrarios, variantes `peer`/`group`, selector `has-*`) para resolver necesidades de diseño sin CSS personalizado.

!!! note "Conocimientos previos"

    Para afrontar esta unidad con garantías, el alumnado debe dominar los siguientes conceptos y habilidades:

    - **Conocimientos sólidos de CSS3**: modelo de caja, especificidad, herencia y cascada, posicionamiento (static, relative, absolute, fixed, sticky), display (block, inline, inline-block, flex, grid, none), flexbox y CSS grid en profundidad, responsive design con media queries, pseudoclases y pseudoelementos, transiciones y animaciones, variables CSS (custom properties), unidades de medida (px, rem, em, %, vw, vh, dvh, ch) y funciones CSS modernas (calc, min, max, clamp). Tailwind no sustituye la necesidad de saber CSS; al contrario, cada clase de Tailwind se corresponde con una o varias propiedades CSS y quien no entienda CSS no podrá usar Tailwind eficazmente.
    - **Experiencia previa en maquetación web con CSS tradicional** aplicado a proyectos de cierta envergadura, habiendo experimentado los problemas que Tailwind resuelve: colisiones de nombres de clases, especificidad descontrolada, CSS muerto que nunca se elimina, inconsistencias de diseño entre páginas.
    - **Conocimientos de Angular**: estructura de un proyecto Angular, componentes standalone y basados en módulos, sistema de plantillas, estilos encapsulados (ViewEncapsulation.Emulated y None), archivo angular.json y su configuración de estilos globales.
    - **Conocimientos de npm y del ecosistema de herramientas de construcción**: instalación de paquetes, scripts npm, conceptos de bundling y tree-shaking.
    - Conocimientos previos de **diseño responsive (Unidad 8)** y **principios de UX (Unidad 1)**, ya que Tailwind incluye utilidades específicas para accesibilidad y diseño responsive que se apoyan en esos fundamentos.

## Contenidos

1. Filosofía Utility-First en el contexto empresarial
2. Configuración de Tailwind 4 en Angular
3. Organización del CSS en un proyecto Angular con Tailwind
4. Clases clave para interfaces de aplicación
5. Técnicas avanzadas con Tailwind
6. Tailwind CSS IntelliSense para VS Code
7. Estrategia de migración a Tailwind en proyectos existentes

## Desarrollo teórico

### 1. Filosofía Utility-First en el Contexto Empresarial

La irrupción de **Tailwind CSS** en el ecosistema del desarrollo frontend ha generado un debate intenso que, a menudo, parte de un malentendido fundamental: la comparación entre "CSS tradicional" y "Tailwind" como si fueran lenguajes diferentes. La realidad es que Tailwind es CSS. Cada clase de Tailwind como `flex`, `p-4`, `text-lg` o `bg-blue-500` se compila directamente a una o varias propiedades CSS estándar. No hay magia, no hay runtime en el navegador, no hay una capa de abstracción que se interponga entre el desarrollador y el navegador. Tailwind es un **generador de CSS en tiempo de compilación** que produce exactamente el CSS que necesitas, ni más ni menos.

Para el alumnado de Formación Profesional que ya ha cursado un módulo de CSS y ha sufrido en carne propia los problemas de mantener hojas de estilo en proyectos que crecen, la filosofía **utility-first** de Tailwind cobra sentido al enmarcarla en el contexto de equipos profesionales y aplicaciones empresariales. En un equipo de desarrollo con cinco personas trabajando en el mismo proyecto Angular, el CSS tradicional tiende a degenerar hacia el caos por varias razones. Cada desarrollador nombra las clases según su propio criterio: `.btn-primary`, `.button-main`, `.primary-action`. La especificidad se descontrola cuando para sobrescribir un estilo se recurre a selectores cada vez más largos: `.main-content .card .header .title`. Aparece **CSS muerto**: clases que se escribieron para una funcionalidad que ya no existe pero que nadie se atreve a eliminar porque no se sabe si algo en alguna página remota las sigue usando. Surgen **guerras de naming** (BEM, SMACSS, OOCSS, CSS Modules, CSS-in-JS) que consumen tiempo de debate sin aportar valor al producto final.

Tailwind corta de raíz estos problemas mediante un mecanismo simple y radical: no nombras tus estilos, los aplicas directamente en el HTML. Esto puede resultar chocante al principio. Ver un botón definido como `<button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:ring-2 focus:ring-blue-500 focus:outline-none">Guardar</button>` produce una reacción instintiva de rechazo en quien está acostumbrado a una única clase semántica como `class="btn-primary"`. Pero esta reacción se disipa cuando se comprende el valor de la **transparencia y la inmediatez**: en el propio HTML puedes ver exactamente qué estilos tiene cada elemento, sin necesidad de abrir el DevTools, navegar por las reglas CSS aplicadas, identificar qué archivo define cada regla y calcular la especificidad para entender por qué un estilo no se aplica.

La **consistencia** es otra ventaja decisiva en proyectos empresariales. Tailwind viene con un **sistema de diseño embebido**: escalas de espaciado, colores, tamaños de tipografía, breakpoints, sombras y bordes predefinidos y coherentes entre sí. Cuando un equipo de desarrollo usa Tailwind, no necesita acordar manualmente qué tono de azul usar: `blue-500` es siempre el mismo tono. No necesita decidir si el padding es de 15px o 16px: `p-4` son siempre 16px (1rem). Esta consistencia forzada, que algunos críticos tachan de limitante, es en realidad una ventaja de productividad y calidad: el diseño resultante es coherente sin requerir disciplina manual.

La premisa fundamental que debe quedar clara desde el principio de esta unidad es que ==Tailwind no reemplaza saber CSS==; todo lo contrario, necesitas dominar CSS para usar Tailwind bien. Cuando escribes `flex items-center justify-between gap-4`, estás aplicando `display: flex`, `align-items: center`, `justify-content: space-between` y `gap: 1rem`. Si no sabes qué hacen estas propiedades CSS, no sabrás qué clases de Tailwind utilizar. Tailwind es simplemente "CSS con otro nombre", una traducción directa de propiedades y valores CSS a nombres de clases memorizables y componibles.

### 2. Configuración de Tailwind 4 en Angular

**Tailwind CSS 4** representa un salto cualitativo respecto a la versión 3. La versión 4, lanzada a principios de 2025, abandona el archivo `tailwind.config.js` basado en JavaScript y adopta un enfoque nativo de CSS para la configuración. El sistema de diseño se define directamente en el archivo CSS de **estilos globales** mediante la directiva `@theme`, que utiliza la sintaxis de custom properties CSS. Esta decisión simplifica la integración con cualquier herramienta de construcción, elimina la dependencia de Node.js para interpretar la configuración, y hace que la personalización de Tailwind sea tan sencilla como declarar variables CSS.

La instalación de Tailwind 4 en un proyecto Angular 17 o superior (que utiliza Vite o esbuild para las builds de desarrollo) es notablemente simple. El primer paso es instalar el paquete correspondiente desde npm. Angular 17+ usa esbuild, y el equipo de Tailwind proporciona un plugin específico para **Vite** que garantiza una integración óptima. En la terminal del proyecto Angular, se ejecuta: `npm install tailwindcss @tailwindcss/vite`. Si el proyecto Angular utiliza **PostCSS** (configuración más tradicional aún soportada por Angular 17+ con builders de Webpack o esbuild), la alternativa es instalar `npm install tailwindcss @tailwindcss/postcss` y crear un archivo `postcss.config.js` que referencie el plugin.

Una vez instalados los paquetes, el segundo paso es configurar el plugin de Vite. En proyectos Angular con builder `@angular/build:application` (el builder moderno basado en esbuild/Vite), se debe modificar el `angular.json` o, en Angular 17+, crear o editar el archivo `vite.config.ts` en la raíz del proyecto para registrar el plugin de Tailwind. La configuración típica incluye la importación del plugin y su adición al array de plugins: `import tailwindcss from '@tailwindcss/vite'` seguido de `plugins: [tailwindcss()]`. Este plugin se encarga de escanear las plantillas de los componentes Angular en busca de clases de Tailwind y generar únicamente el CSS correspondiente.

El tercer paso, y el más importante conceptualmente, es la configuración del archivo de estilos globales. En el archivo `src/styles.css` (o `src/styles.scss` si se usa Sass), se añade una única línea al inicio: `@import "tailwindcss";`. Esta directiva CSS, procesada por Tailwind en tiempo de compilación, inyecta todo el CSS utility generado. A diferencia de versiones anteriores donde se usaban las directivas `@tailwind base;`, `@tailwind components;` y `@tailwind utilities;`, la versión 4 las unifica en una simple importación CSS estándar que cualquier herramienta de construcción entiende.

A partir de aquí, la personalización del sistema de diseño se realiza directamente en el mismo archivo CSS global, debajo de la importación de Tailwind, mediante la directiva `@theme`. Esta directiva define los **tokens de diseño** que Tailwind utilizará para generar sus clases utility. La sintaxis es idéntica a la definición de custom properties CSS, pero dentro de un bloque `@theme` que Tailwind procesa especialmente. Un ejemplo completo de personalización para una aplicación de gestión empresarial se vería así:

```css
@import "tailwindcss";

@theme {
  --color-primary-50: oklch(0.97 0.01 255);
  --color-primary-100: oklch(0.93 0.03 255);
  --color-primary-200: oklch(0.85 0.07 255);
  --color-primary-300: oklch(0.75 0.11 255);
  --color-primary-400: oklch(0.68 0.15 255);
  --color-primary-500: oklch(0.62 0.19 255);
  --color-primary-600: oklch(0.55 0.19 255);
  --color-primary-700: oklch(0.47 0.17 255);
  --color-primary-800: oklch(0.38 0.14 255);
  --color-primary-900: oklch(0.28 0.10 255);
  
  --color-secondary-50: oklch(0.97 0.02 155);
  --color-secondary-100: oklch(0.93 0.05 155);
  --color-secondary-500: oklch(0.65 0.18 155);
  --color-secondary-900: oklch(0.30 0.09 155);
  
  --color-success-500: oklch(0.62 0.19 145);
  --color-warning-500: oklch(0.75 0.15 85);
  --color-danger-500: oklch(0.55 0.22 25);
  
  --font-family-sans: 'Inter', 'Segoe UI', system-ui, sans-serif;
  --font-family-mono: 'JetBrains Mono', 'Fira Code', monospace;
  
  --spacing-section: 5rem;
  --spacing-component: 2.5rem;
  
  --radius-button: 0.5rem;
  --radius-card: 0.75rem;
}
```

!!! info "Definición"

    La elección de **oklch** como espacio de color merece una breve explicación. Tradicionalmente, los colores en Tailwind se definían en hexadecimal o RGB. El espacio de color oklch, soportado por los navegadores modernos, es **perceptualmente uniforme**: cambios iguales en sus coordenadas producen cambios visuales iguales. Esto facilita muchísimo la creación de escalas de color: una vez definido el tono matiz (el cuarto parámetro en oklch, que va de 0 a 360 grados en el círculo cromático), variar la luminosidad (el primer parámetro, de 0 a 1) produce automáticamente tonos más claros y más oscuros del mismo color sin los artefactos que aparecen al manipular RGB. Para una aplicación empresarial andaluza, podríamos definir el azul corporativo de la Junta de Andalucía, el verde de sus consejerías, o los colores de marca de una empresa privada, y generar escalas completas y armoniosas con facilidad.

El cuarto paso es la integración con **Angular CLI**. El archivo `angular.json` debe referenciar correctamente el archivo de estilos globales. En la sección `projects > nombre-del-proyecto > architect > build > options > styles`, debe aparecer `"src/styles.css"` o la ruta correspondiente. En proyectos Angular 17+ con configuración standalone y Vite, esta configuración suele ser correcta por defecto y no requiere ajustes adicionales.

Un aspecto crucial que cambia en Tailwind 4 es que la detección de contenido (**content scanning**) ya no requiere configurar manualmente las rutas de los archivos donde Tailwind debe buscar clases. Tailwind 4 utiliza el plugin de Vite o PostCSS para detectar automáticamente todos los archivos que son procesados por la herramienta de construcción (HTML, TypeScript, plantillas Angular), eliminando la necesidad del array `content` del antiguo `tailwind.config.js`.

### 3. Organización del CSS en un Proyecto Angular con Tailwind

La organización del CSS en un proyecto Angular con Tailwind es notablemente más sencilla que con CSS tradicional, pero requiere disciplina para no caer en un antipatrón igualmente dañino: el abuso de `@apply`. La estrategia recomendada se articula en **tres niveles**.

El primer nivel son los **estilos globales** en `src/styles.css` (o `.scss`). Este archivo contiene exclusivamente la importación de Tailwind (`@import "tailwindcss"`) y la configuración de `@theme` con los tokens de diseño. Adicionalmente, puede contener estilos base globales que afectan a toda la aplicación y que no son specificables mediante clases Tailwind. Por ejemplo, un reset CSS adicional, la definición de animaciones globales con `@keyframes`, variables CSS que no forman parte del sistema de diseño de Tailwind, o estilos para elementos que Angular no controla directamente (como el body, el scrollbar del navegador, o la tipografía base). Lo ideal es que este archivo sea mínimo: en un proyecto bien estructurado con Tailwind, el archivo de estilos globales rara vez supera las 50 líneas.

El segundo nivel, y el más importante, son las clases de Tailwind directamente en las plantillas de los componentes Angular. Esta es la **práctica estándar y recomendada**. Cada componente Angular define su apariencia visual mediante las clases Tailwind en su plantilla HTML. Para el desarrollador, esto significa que abriendo un único archivo (la plantilla del componente) se ve todo lo necesario para entender la estructura y el aspecto del componente, sin tener que alternar entre el HTML y un archivo CSS separado. La legibilidad de un botón con 10 clases de Tailwind mejora con la práctica: en pocas semanas, el desarrollador lee `px-4 py-2 bg-primary-500 text-white rounded-lg hover:bg-primary-600` tan fluidamente como leía `class="btn-primary"`, pero con la ventaja de saber exactamente qué hace cada clase sin tener que buscar la definición de `.btn-primary`.

El tercer nivel, que debe usarse con moderación extrema, es la directiva `@apply` en la hoja de estilos del componente (el archivo `.css` o `.scss` asociado). `@apply` permite agrupar varias clases de Tailwind dentro de una regla CSS personalizada. El **caso de uso legítimo** es cuando un componente Angular reutilizable necesita aplicar exactamente los mismos estilos a muchos elementos, y la repetición de las mismas clases en múltiples lugares de la plantilla se vuelve difícil de mantener. Por ejemplo, si un componente de tabla tiene 20 `<td>` que requieren las mismas 8 clases, tiene sentido definir `.td-base { @apply px-4 py-3 text-sm text-gray-700 border-b border-gray-200; }` y aplicar `class="td-base"` a cada `<td>`. Pero este caso es raro en la práctica, porque Angular ya ofrece un mecanismo superior para la reutilización de estilos: crear un componente. Si tienes que repetir las mismas clases en muchos elementos, probablemente deberías extraer un componente hijo, no usar `@apply`.

!!! warning "Antipatrón"

    El antipatrón que debe evitarse es usar `@apply` para recrear clases semánticas como `.btn-primary` o `.card-header` en una hoja de estilos global. Esto destruye la **principal ventaja de Tailwind** (la transparencia y la inmediatez en el HTML) y recrea los problemas del CSS tradicional (tener que ir a otro archivo a buscar la definición de una clase). La regla práctica es: Tailwind en el HTML para todo, `@apply` como excepción muy justificada, y si necesitas `@apply` constantemente, probablemente necesitas crear un componente Angular, no luchar contra Tailwind.

### 4. Clases Clave para Interfaces de Aplicación

Tailwind CSS proporciona miles de clases predefinidas, pero en el desarrollo de **interfaces de aplicación** (no de páginas web de marketing), hay un subconjunto de clases que cubren el 90% de las necesidades diarias. Organizamos estas clases por categoría funcional.

Para layout, las clases esenciales giran en torno a **flexbox y CSS grid**. `flex`, `inline-flex`, `flex-col`, `flex-row`, `flex-wrap`, `flex-1`, `flex-auto`, `flex-none` controlan el comportamiento flexible. `items-start`, `items-center`, `items-end`, `items-stretch` alinean los hijos en el eje transversal. `justify-start`, `justify-center`, `justify-end`, `justify-between`, `justify-around`, `justify-evenly` distribuyen el espacio en el eje principal. `gap-*` establece el espaciado entre hijos de un contenedor flex o grid, reemplazando los antiguos `margin` que requerían limpiar el último elemento. Para grid, `grid`, `grid-cols-*` (de 1 a 12), `col-span-*`, `grid-rows-*` definen la estructura de cuadrícula. `container` centra el contenido y lo limita a los anchos de breakpoint. `mx-auto` centra horizontalmente un bloque con margen automático. `min-h-screen` asegura que una sección ocupe al menos el alto de la ventana, útil para layouts de dashboard que llenan la pantalla.

Para espaciado, las clases de padding (`p-*`, `px-*`, `py-*`, `pt-*`, `pr-*`, `pb-*`, `pl-*`) y margin (`m-*`, `mx-*`, `my-*`, `mt-*`, `mr-*`, `mb-*`, `ml-*`) utilizan una **escala predefinida** que va de 0 (0px) a 96 (24rem, 384px), con valores intermedios como 0.5 (2px), 1 (4px), 2 (8px), 3 (12px), 4 (16px), 5 (20px), 6 (24px), 8 (32px), 10 (40px), 12 (48px), 16 (64px), 20 (80px). La escala es exponencial, no lineal, lo que proporciona granularidad fina en valores pequeños y saltos útiles en valores grandes. `space-y-*` y `space-x-*` aplican margen entre hijos de forma más ergonómica que `gap` en ciertos contextos.

Para colores, Tailwind incluye una **paleta extensa y científicamente diseñada** con nombres como `slate`, `gray`, `zinc`, `neutral`, `stone`, `red`, `orange`, `amber`, `yellow`, `lime`, `green`, `emerald`, `teal`, `cyan`, `sky`, `blue`, `indigo`, `violet`, `purple`, `fuchsia`, `pink` y `rose`. Cada color tiene 11 tonos (50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950). Las clases se aplican a color de texto (`text-{color}-{tono}`), fondo (`bg-{color}-{tono}`), borde (`border-{color}-{tono}`), sombra de anillo (`ring-{color}-{tono}`) y decoración. Los colores personalizados definidos en `@theme` siguen exactamente el mismo patrón, de modo que `--color-primary-500` genera las clases `bg-primary-500`, `text-primary-500`, etc.

Para tipografía, las clases más utilizadas son `text-xs` (12px, 0.75rem), `text-sm` (14px, 0.875rem), `text-base` (16px, 1rem), `text-lg` (18px, 1.125rem), `text-xl` (20px, 1.25rem), `text-2xl` (24px, 1.5rem), `text-3xl` (30px, 1.875rem) y `text-4xl` (36px, 2.25rem). `font-thin`, `font-light`, `font-normal`, `font-medium`, `font-semibold`, `font-bold` controlan el peso. `leading-*` controla el interlineado. `tracking-*` controla el espaciado entre caracteres. `text-center`, `text-left`, `text-right` alinean el texto. `truncate` aplica `overflow: hidden; text-overflow: ellipsis; white-space: nowrap` para truncar texto largo, esencial en celdas de tablas y tarjetas. `line-clamp-*` limita el texto a un número de líneas con puntos suspensivos.

Para estados interactivos, Tailwind proporciona **variantes** que se anteponen a cualquier clase: `hover:`, `focus:`, `active:`, `disabled:`, `focus-visible:`, `focus-within:`, `group-hover:`, `peer-checked:` y docenas más. Un botón típico combina varios estados: `bg-primary-500 hover:bg-primary-600 active:bg-primary-700 focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:outline-none disabled:opacity-50 disabled:cursor-not-allowed`.

La variante `dark:` permite estilizar la aplicación en modo oscuro. Tailwind soporta **dos estrategias**: `media` (respeta la configuración del sistema operativo mediante `prefers-color-scheme`) y `class` (añade o quita la clase `dark` manualmente, por ejemplo, mediante un toggle en la interfaz). Para aplicaciones de gestión, la estrategia `class` suele ser preferible porque permite a la persona usuaria elegir explícitamente el tema, independientemente de su configuración del sistema.

Para diseño **responsive**, las variantes `sm:` (640px), `md:` (768px), `lg:` (1024px), `xl:` (1280px) y `2xl:` (1536px) permiten modificar cualquier clase en función del ancho de la ventana. Tailwind adopta el enfoque **mobile-first**: las clases sin prefijo se aplican a todos los tamaños, y las clases con prefijo se aplican a partir del **breakpoint** indicado hacia arriba. Por tanto, `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` significa: 1 columna en móvil, 2 columnas a partir de 768px, 3 columnas a partir de 1024px.

Para formularios, las clases específicas permiten crear inputs con apariencia personalizada sin perder accesibilidad: `focus:ring-2`, `focus:border-primary-500`, `disabled:opacity-50`, `disabled:bg-gray-100`, `read-only:bg-gray-50`. Las clases `accent-primary-500` estilizan el color de acento de checkboxes y radios nativos.

!!! tip "Accesibilidad"

    Para accesibilidad, `sr-only` oculta visualmente un elemento manteniéndolo accesible para lectores de pantalla, ideal para labels de "saltar al contenido" o para proporcionar contexto adicional a elementos visualmente autodescriptivos. `focus-visible:ring-2` proporciona un foco visible solo cuando la navegación es por teclado, preservando la estética para personas usuarias de ratón. Los atributos **ARIA** pueden combinarse con clases y variantes de Tailwind para crear componentes accesibles sin CSS personalizado.

### 5. Técnicas Avanzadas con Tailwind

Los **valores arbitrarios** son una de las características más potentes de Tailwind para resolver necesidades de diseño que no encajan en la escala predefinida. Mediante la sintaxis de corchetes, se puede especificar cualquier valor CSS válido: `w-[300px]`, `text-[#bada55]`, `grid-cols-[200px_1fr_200px]`, `bg-[url('/images/hero.webp')]`, `transition-[opacity,transform]`, `duration-[400ms]`, `delay-[200ms]`. Los valores arbitrarios deben usarse con moderación: si un valor arbitrario se repite en múltiples lugares, debería promocionarse a un token de diseño en `@theme`. Pero en el desarrollo diario, los valores arbitrarios evitan tener que escribir CSS personalizado para casos puntuales, lo que mantiene el proyecto libre de hojas de estilo adicionales.

Las variantes `peer` y `group` permiten estilizar un elemento basándose en el estado de otro elemento. `peer` mira a un **elemento hermano anterior** (en el DOM): `peer` se aplica al elemento cuyo estado se observa, y `peer-*` se aplica a los elementos hermanos que reaccionan a ese estado. Un caso típico es un mensaje de error que se muestra cuando un input es inválido: `<input class="peer" required /> <p class="hidden peer-invalid:block text-red-500">Este campo es obligatorio</p>`. La clase `peer-invalid:block` convierte el párrafo de `display: none` a `display: block` cuando el input hermano (marcado con `peer`) está en estado `:invalid`. `group` funciona de forma similar pero basándose en el estado de un elemento padre: `<div class="group"><h2 class="group-hover:text-blue-500">Título</h2></div>` aplica el color azul al título cuando el cursor pasa sobre el div padre.

El selector `has-*` (soportado por Tailwind 4 con la variante `has-*`) permite estilizar un elemento padre basándose en el estado de uno de sus descendientes. Es decir, opera en **dirección contraria a la cascada normal**. Un uso práctico es estilizar un contenedor de formulario cuando alguno de sus campos es inválido: `<fieldset class="has-[:invalid]:border-red-500 has-[:invalid]:bg-red-50">`. Cuando cualquier input dentro del fieldset tiene `:invalid`, el fieldset entero cambia su borde a rojo y su fondo a rojo claro. Otro uso común es estilizar un elemento de lista que contiene un checkbox marcado: `<li class="has-[:checked]:bg-green-50 has-[:checked]:line-through">`.

El motor **JIT** (Just-In-Time) de Tailwind es el responsable de que estas miles de clases utility no generen un archivo CSS de varios megabytes. En tiempo de compilación, Tailwind escanea todos los archivos de la aplicación (plantillas Angular, archivos TypeScript, estilos CSS) en busca de cadenas que coincidan con el patrón de sus clases utility. Solo las clases encontradas se incluyen en el CSS generado. Esto significa que aunque Tailwind ofrezca miles de clases, ==el CSS resultante contiene exclusivamente las que realmente utilizas==. En un proyecto Angular típico con Tailwind 4 y JIT, el CSS generado rara vez supera los 15-20 KB comprimidos, a pesar de que el conjunto completo de clases de Tailwind ocuparía varios megabytes.

### 6. Tailwind CSS IntelliSense para VS Code

La extensión oficial **Tailwind CSS IntelliSense** para Visual Studio Code, desarrollada por el equipo de Tailwind, transforma la experiencia de desarrollo con este framework. Sus funcionalidades principales incluyen:

**Autocompletado de clases** mientras se escribe en el HTML o en las plantillas Angular. Al empezar a escribir `bg-`, la extensión sugiere todas las clases que comienzan por ese prefijo, mostrando el nombre de la clase, su valor CSS equivalente y una previsualización del color (si es una clase de color). Esto elimina la necesidad de consultar la documentación constantemente y acelera drásticamente el flujo de trabajo.

**Previsualización de colores inline** en el código. Junto a cada clase de color, la extensión muestra un pequeño cuadrado del color correspondiente, facilitando la verificación visual inmediata de que el color elegido es el correcto.

**Linting de clases inválidas**. Si escribes `bg-primari-500` (con una errata), la extensión lo subraya en amarillo o rojo y sugiere la clase correcta. También advierte sobre clases que no existen, clases con valores incorrectos, y clases que entran en conflicto entre sí (por ejemplo, `p-2 p-4` en el mismo elemento, donde la segunda anula a la primera).

**Documentación inline**. Al pasar el cursor sobre una clase de Tailwind, se muestra un tooltip con la propiedad o propiedades CSS que genera esa clase, el valor calculado, y si es parte de una escala, su posición en la escala.

**Soporte para personalización** con `@theme`. La extensión lee la configuración de `@theme` en los archivos CSS del proyecto y proporciona autocompletado para los colores, espaciados, familias tipográficas y demás tokens personalizados definidos por el equipo. Si defines `--color-brand-500: oklch(0.62 0.19 255)`, la extensión sugerirá `bg-brand-500` y mostrará la previsualización del color correspondiente.

### 7. Estrategia de Migración a Tailwind en Proyectos Existentes

Introducir Tailwind en un proyecto Angular que ya tiene cientos o miles de líneas de CSS tradicional es un desafío que debe abordarse con estrategia, no con un "big bang" que rompa todo y requiera reescribir la aplicación entera. La migración se plantea en **varias fases**, cada una de las cuales puede implementarse incrementalmente sin detener el desarrollo de nuevas funcionalidades.

La **fase 0**, de preparación, consiste en instalar Tailwind en el proyecto sin que afecte al CSS existente. Se instalan los paquetes npm, se configura el plugin de Vite o PostCSS, y se añade `@import "tailwindcss"` en el archivo de estilos globales, pero al final, de forma que su baja especificidad (las clases utility tienen todas especificidad 0-1-0, equivalente a una sola clase) no sobrescriba al CSS existente. En este punto, las classes de Tailwind están disponibles para usar en nuevos componentes, pero no interfieren con el CSS heredado.

La **fase 1** consiste en usar Tailwind exclusivamente para nuevos componentes. Cada componente nuevo que se crea en el proyecto se estiliza con Tailwind. Esto genera familiaridad con el framework en el equipo y empieza a acumular ejemplos de código con Tailwind dentro del proyecto. Los componentes existentes se siguen manteniendo con CSS tradicional.

La **fase 2** aborda la migración de componentes existentes de forma oportunista: cuando un componente necesita una modificación significativa por razones de negocio (una nueva funcionalidad, un rediseño de una sección), se aprovecha para migrarlo a Tailwind. Esto convierte la migración en un subproducto del trabajo planificado, no en una tarea independiente que compite por prioridad.

La **fase 3** aborda la eliminación del CSS heredado. A medida que los componentes se van migrando, sus hojas de estilo asociadas se van vaciando. Cuando una hoja de estilo queda completamente vacía o solo contiene reglas que ya no aplican a ningún componente activo, se elimina. Las herramientas de análisis de CSS no utilizado (como PurgeCSS, aunque Tailwind ya lo incluye, o la cobertura de CSS en Chrome DevTools) ayudan a identificar qué partes del CSS heredado siguen siendo necesarias.

La **fase 4** es la consolidación final: limpiar los estilos globales heredados, eliminar dependencias de frameworks CSS anteriores si los había (Bootstrap, Materialize, etc.), y establecer Tailwind como el estándar del proyecto documentado en el README y en la guía de contribución.

Durante todo el proceso, es importante establecer **reglas de coexistencia**: no mezclar Tailwind y CSS tradicional en el mismo componente si no es estrictamente necesario, documentar los componentes ya migrados, y mantener tests visuales (con herramientas como Storybook o Chromatic) que detecten regresiones visuales durante la migración.

## Ejemplos guiados

### Ejemplo Guiado 1: Configurar Tailwind 4 en un Proyecto Angular desde Cero

En este ejemplo, se crea un proyecto Angular nuevo y se configura Tailwind 4 paso a paso. Se comienza generando el proyecto con Angular CLI: `ng new gestion-tareas --style=css --standalone --ssr=false`. Se navega al directorio del proyecto y se instalan los paquetes: `npm install tailwindcss @tailwindcss/vite`. En Angular 17+, se crea o edita el archivo `vite.config.ts` en la raíz del proyecto para añadir el plugin de Tailwind. En el archivo `src/styles.css`, se añade exclusivamente `@import "tailwindcss";`.

A continuación, se personaliza el sistema de diseño mediante `@theme`. Se definen los colores corporativos de una empresa ficticia llamada "GestionaAndalucía", con un azul corporativo basado en oklch. Se crea una escala completa de 9 tonos del color primario (azul) y una escala reducida del secundario (naranja). Se define la familia tipográfica Inter para el texto general. Se añade un espaciado personalizado `--spacing-section: 5rem` para secciones de página.

Se verifica la configuración creando un componente simple en `app.component.html` con varias clases de Tailwind, incluyendo los colores personalizados (`bg-primary-500`, `text-primary-100`). Al ejecutar `ng serve` y abrir el navegador, se comprueba que los estilos se aplican correctamente. Se inspecciona el elemento para verificar que las clases de Tailwind se han compilado a CSS real. Se abre DevTools y se comprueba el tamaño del CSS cargado, que debería ser mínimo (solo las clases utilizadas en la plantilla, gracias al motor JIT).

Finalmente, se configura la extensión Tailwind CSS IntelliSense en VS Code para verificar que el autocompletado funciona con los colores personalizados de `@theme`.

### Ejemplo Guiado 2: Construir un Dashboard Widget con Tailwind

Se construye un componente de widget de dashboard para mostrar una estadística con tendencia. El widget, típico en aplicaciones de gestión, muestra un título, un valor numérico grande, un indicador de tendencia (subida o bajada con porcentaje y flecha), y un área reservada para un gráfico placeholder.

El HTML del componente se estructura con un `<article>` como contenedor raíz. Mediante Tailwind, se aplica un fondo blanco con borde redondeado y sombra sutil: `bg-white rounded-xl shadow-sm border border-gray-200 p-6`. El interior se organiza con flexbox: `flex flex-col gap-4`.

La cabecera muestra el título del widget en gris medio con tamaño pequeño y peso semibold: `text-sm font-medium text-gray-500 tracking-wide uppercase`. El valor principal utiliza el tamaño de texto más grande disponible y peso bold: `text-4xl font-bold text-gray-900`.

El indicador de tendencia se implementa con un `<span>` condicional que muestra una flecha hacia arriba o hacia abajo y el porcentaje. Los estilos se condicionan en la plantilla Angular: si la tendencia es positiva, se aplica `text-emerald-600 bg-emerald-50`; si es negativa, `text-red-600 bg-red-50`. Ambas variantes comparten estilos base: `inline-flex items-center gap-1 px-2 py-1 text-sm font-medium rounded-full`.

El área del gráfico placeholder se implementa con un `<div>` que simula un gráfico de barras simples usando barras de diferentes alturas construidas con `h-*` arbitrarias (`h-[40px]`, `h-[65px]`, `h-[35px]`, `h-[80px]`, `h-[55px]`). Las barras se distribuyen con `flex items-end gap-1 h-24`. Cada barra es un `<div>` con `w-4 bg-primary-200 rounded-t` y la barra actual se destaca con `bg-primary-500`.

El resultado es un widget profesional y consistente, implementado en aproximadamente 15 minutos sin escribir una sola línea de CSS personalizado. Este ejemplo ilustra la productividad de Tailwind cuando se domina el vocabulario de clases.

### Ejemplo Guiado 3: Sistema de Temas Claro/Oscuro con Tailwind

Se implementa un sistema de alternancia entre tema claro y oscuro en una aplicación Angular, utilizando la estrategia `class` de Tailwind. El primer paso es añadir `darkMode: 'class'` a la configuración de Tailwind (en Tailwind 4, esto se configura dentro de `@theme` o mediante CSS). En las plantillas de los componentes, se añade la variante `dark:` a las clases que deben cambiar en modo oscuro. Por ejemplo, el fondo de la aplicación pasa de `bg-gray-50` a `dark:bg-gray-900`, y el texto de `text-gray-900` a `dark:text-gray-100`.

En Angular, se crea un servicio `ThemeService` que gestiona el estado del tema mediante una señal. El servicio lee la preferencia guardada en `localStorage` al iniciar, y si no hay preferencia guardada, respeta la preferencia del sistema operativo (consultando `window.matchMedia('(prefers-color-scheme: dark)')`). El servicio expone un método `toggle()` y una señal computada que devuelve `'dark'` o `'light'`.

Un componente `ThemeToggle` inyecta el servicio y renderiza un botón con un icono de sol (tema claro) o luna (tema oscuro) según el estado actual. Al hacer clic, llama a `themeService.toggle()`.

El servicio también se encarga de manipular la clase `dark` en el elemento `<html>`. Cuando el tema es oscuro, añade `document.documentElement.classList.add('dark')`; cuando es claro, la elimina. Esta manipulación del DOM es segura porque solo afecta al elemento raíz y es independiente del ciclo de detección de cambios de Angular.

El resultado es una aplicación que respeta la preferencia del sistema, persiste la elección del usuario, y aplica el tema oscuro de forma consistente en todos los componentes sin CSS personalizado, utilizando exclusivamente las variantes `dark:` de Tailwind.

## Actividades guiadas

### Actividad Guiada 1: Configuración de Tailwind 4 en un Proyecto Angular Existente

El alumnado partirá de un proyecto Angular proporcionado por el docente que contiene una aplicación de gestión de biblioteca con varios componentes estilizados con CSS tradicional. El proyecto no tiene Tailwind instalado. La actividad consiste en instalar y configurar Tailwind 4 siguiendo el procedimiento de migración incremental: instalar los paquetes npm sin romper el CSS existente, personalizar `@theme` con los colores corporativos de la biblioteca (verde institucional, beige de fondo), y verificar que tanto el CSS tradicional como las nuevas clases de Tailwind funcionan simultáneamente. El alumnado creará un nuevo componente de "panel de estadísticas" estilizado íntegramente con Tailwind que conviva con los componentes existentes en CSS tradicional.

### Actividad Guiada 2: Construcción de un Dashboard Completo con Tailwind

El alumnado construirá un dashboard de tres filas completamente con Tailwind. La primera fila contiene cuatro widgets de estadísticas (total de libros, préstamos activos, personas usuarias registradas, libros más prestados). La segunda fila contiene una tabla de últimos préstamos con columnas zebra y acciones. La tercera fila contiene dos gráficos placeholder (barras y líneas). El layout utiliza CSS grid con Tailwind: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6` para los widgets. Cada widget se estiliza con las clases vistas en el ejemplo guiado. La tabla utiliza `overflow-x-auto` para scroll horizontal en móvil y las clases `even:bg-gray-50` para el zebra. Los gráficos placeholder utilizan barras y puntos construidos con divs y clases de Tailwind.

### Actividad Guiada 3: Migración de un Componente de CSS Tradicional a Tailwind

El alumnado recibirá un componente Angular (un formulario de alta de libro) estilizado con CSS tradicional en un archivo `.css` separado que contiene aproximadamente 100 líneas de CSS. La actividad consiste en migrar este componente a Tailwind, eliminando todo el CSS tradicional y reemplazándolo con clases utility en la plantilla HTML. El componente debe conservar exactamente la misma apariencia visual tras la migración. El alumnado deberá identificar correspondencias entre las reglas CSS tradicionales y las clases de Tailwind, utilizar valores arbitrarios para propiedades que no tengan una clase Tailwind directa, y verificar visualmente que el resultado es idéntico. Al finalizar, el archivo CSS del componente deberá estar vacío y la apariencia del componente inalterada.

## Actividades propuestas

### Actividad Propuesta 1: Sistema de Diseño Personalizado con @theme

Define un sistema de diseño completo para una aplicación de gestión de clínica dental andaluza. La aplicación se llama "DentAndalucía" y tiene los siguientes requisitos de marca: color primario azul corporativo (tono 220 en oklch), color secundario verde menta (tono 160 en oklch), tipografía principal Nunito, tipografía para datos tabulares JetBrains Mono, espaciado base 0.25rem (4px), y border-radius de 0.375rem para botones y 0.625rem para tarjetas. Crea el bloque `@theme` completo con escalas de color completas (9 tonos para primario, 5 para secundario, más success, warning y danger). Configura este `@theme` en un proyecto Angular y crea una página de demostración que muestre todos los colores, tipografías y espaciados definidos. La página debe servir como referencia de diseño para el equipo.

### Actividad Propuesta 2: Análisis Comparativo del CSS Generado

Instala Tailwind 4 en dos proyectos Angular idénticos (puedes usar el mismo proyecto con dos ramas de git). En uno, utiliza Tailwind de forma óptima (solo las clases necesarias, sin `@apply`). En el otro, introduce deliberadamente malas prácticas: abuso de `@apply` para recrear clases semánticas, duplicación de estilos, y clases de Tailwind que se anulan mutuamente. Utiliza las DevTools del navegador para comparar el tamaño del CSS generado por cada proyecto. Analiza el árbol de CSS en la pestaña "Coverage" de DevTools para identificar CSS no utilizado. Documenta tus hallazgos en un informe con capturas de pantalla y extrae conclusiones sobre las buenas prácticas que más impactan en el rendimiento.

### Actividad Propuesta 3: Componentes de Formulario con Estados Complejos

Crea un sistema de 6 componentes de formulario reutilizables estilizados con Tailwind: InputText (con label, placeholder, estados normal, focus, error, disabled), InputSelect (con dropdown personalizado), Checkbox (con diseño personalizado que oculte el input nativo), ToggleSwitch (interruptor de encendido/apagado), InputSearch (con icono de lupa y botón de limpiar), y TextArea (con contador de caracteres). Cada componente debe aceptar propiedades Angular para su configuración (label, placeholder, valor, estado de error, mensaje de error, disabled) y reflejar correctamente todos los estados en su apariencia. Los estilos deben ser 100% Tailwind, sin CSS personalizado. Publica los componentes en una pequeña librería documentada con Storybook (Unidad 14).

### Actividad Propuesta 4: Tema Oscuro Completo

Implementa un sistema de tema oscuro en una aplicación Angular existente (la de la biblioteca de unidades anteriores). El sistema debe incluir: servicio ThemeService con persistencia en localStorage, componente ThemeToggle con iconos animados, y aplicación de la variante `dark:` a TODOS los componentes de la aplicación (al menos 10 componentes distintos). Debes verificar visualmente cada pantalla en ambos temas para asegurar que el contraste cumple los requisitos WCAG AA (4.5:1 para texto normal, 3:1 para texto grande) en ambos modos. Documenta las combinaciones de colores problemáticas que has tenido que ajustar.

### Actividad Propuesta 5: Guía de Estilo Interactiva

Crea una página de guía de estilo interactiva (style guide) dentro de la aplicación Angular que sirva como documentación viva del sistema de diseño. La página debe incluir secciones para: colores (mostrando todos los tonos de cada color con su nombre de clase Tailwind), tipografías (todos los tamaños, pesos y estilos disponibles), botones (todas las variantes: primary, secondary, outline, ghost, danger, en todos los tamaños y estados), formularios (todos los tipos de input con sus estados), tarjetas, badges, alerts, y espaciado (una demostración visual de la escala de espaciado). Cada elemento de la guía debe mostrar su nombre de clase y el CSS generado. La guía debe servirse en una ruta `/style-guide` y ser responsive.

??? "Actividades de ampliación"

    ### Actividad de Ampliación 1: Plugin de Tailwind Personalizado

    Investiga la API de plugins de Tailwind 4 y desarrolla un plugin personalizado que añada utilidades específicas para el dominio de una aplicación de gestión de inventario. El plugin debe proporcionar: utilidades para estilos de "nivel de stock" (in-stock, low-stock, out-of-stock) que combinen colores, iconos y bordes, componentes de "badge de estado" para estados de pedido (pending, processing, shipped, delivered, cancelled) con colores y estilos apropiados, y un sistema de grid para layouts de formularios de dos columnas con etiquetas alineadas a la derecha. Documenta el plugin, instálalo en un proyecto Angular y demuestra sus utilidades en una página de ejemplo.

    ### Actividad de Ampliación 2: Migración Completa de un Proyecto Grande

    Toma un proyecto Angular con al menos 15 componentes y 500 líneas de CSS tradicional (puedes usar un proyecto de cursos anteriores o uno de código abierto) y realiza una migración completa a Tailwind siguiendo la estrategia de 4 fases descrita en la unidad. Documenta cada fase con métricas: líneas de CSS eliminadas, número de componentes migrados, tiempo empleado, problemas encontrados y soluciones aplicadas. Al finalizar el proceso, la carpeta de estilos del proyecto debe estar vacía (salvo los estilos globales con `@import "tailwindcss"` y `@theme`) y todas las clases personalizadas deben haber sido reemplazadas por clases de Tailwind. La aplicación debe pasar los tests existentes y ser visualmente idéntica a la versión original.

    ### Actividad de Ampliación 3: Evaluación de Rendimiento entre Tailwind 3 y Tailwind 4

    Configura dos proyectos Angular idénticos, uno con Tailwind 3 (usando PostCSS y `tailwind.config.js`) y otro con Tailwind 4 (usando el plugin de Vite y `@theme`). En ambos proyectos, construye exactamente la misma aplicación de dashboard con las mismas clases de Tailwind. Mide y compara: tiempo de build de desarrollo, tiempo de build de producción, tamaño del bundle CSS generado, tiempo de Hot Module Replacement (HMR) al modificar una clase, y soporte de IntelliSense en VS Code. Documenta las diferencias, explica sus causas técnicas a partir de los cambios en el motor de Tailwind, y emite una recomendación argumentada sobre si merece la pena migrar de Tailwind 3 a 4.

!!! tip "Buenas prácticas"

    1. **Domina CSS antes de usar Tailwind.** Las clases de Tailwind son una traducción directa de propiedades CSS. No saber qué hace `justify-between` te impedirá usar correctamente esta clase, por mucho que la tengas a golpe de autocompletado. Estudia CSS en profundidad: Tailwind es una herramienta para aplicar CSS más rápido, no un sustituto de saber CSS.

    2. **Utiliza los colores y espaciados del `@theme` siempre que sea posible.** Antes de recurrir a un valor arbitrario como `p-[13px]` o `text-[#1a2b3c]`, pregúntate si puedes usar un valor de la escala predefinida o añadir un nuevo token. La consistencia visual se construye usando siempre la misma paleta.

    3. **No abuses de `@apply`.** Si te descubres usando `@apply` constantemente para crear clases como `.btn-primary` o `.card`, estás luchando contra Tailwind en lugar de aprovecharlo. En Angular, extrae un componente reutilizable; en otros frameworks, usa un sistema de componentes equivalente. `@apply` debe ser la excepción, no la regla.

    4. **Agrupa las clases de Tailwind de forma lógica en el HTML.** Adopta una convención de orden en el equipo para que todas las plantillas sean legibles. Una recomendación común es: layout (display, position, flex/grid), espaciado (margin, padding), tamaño (width, height), tipografía, colores (fondo, texto, borde), bordes y sombras, estados (hover, focus), responsive, y miscelánea. La extensión Headwind para VS Code puede ordenar las clases automáticamente.

    5. **Usa la variante `focus-visible` en lugar de `focus` para estilos de foco en elementos interactivos.** Esto garantiza que los estilos de foco se muestren cuando la persona usuaria navega con teclado, pero no al hacer clic con el ratón, mejorando la accesibilidad sin sacrificar la estética.

    6. **Aprovecha `peer` y `group` para reducir la lógica de estado en TypeScript.** En lugar de manejar estados de hover/focus/error en el componente Angular con señales y bindings condicionales, pregunta si puedes delegar esa lógica a CSS mediante las variantes de Tailwind. Esto simplifica el código TypeScript y mejora el rendimiento.

    7. **Utiliza las herramientas de desarrollo del navegador para depurar Tailwind.** El panel de estilos de Chrome DevTools muestra las clases de Tailwind aplicadas a cada elemento junto con sus propiedades CSS equivalentes. Puedes marcar/desmarcar clases para experimentar y luego copiar el resultado a la plantilla.

    8. **Mantén el archivo de estilos globales mínimo.** Un proyecto Angular con Tailwind bien configurado debería tener `styles.css` con menos de 100 líneas: el `@import`, el bloque `@theme`, y quizás algunos estilos base o animaciones globales. Si tu `styles.css` crece, pregunta si ese CSS debería estar en un componente.

    9. **Extrae componentes cuando un conjunto de clases se repita.** Si tecleas las mismas 8 clases de Tailwind en 5 botones diferentes de la aplicación, no recurras a `@apply`: crea un componente `<app-button>` que encapsule esos estilos y exponga propiedades para las variantes. Esto es más idiomático en Angular y más mantenible.

    10. **Verifica el contraste de colores después de personalizar `@theme`.** Los colores generados con oklch no garantizan automáticamente el contraste WCAG AA. Utiliza un comprobador de contraste para verificar que las combinaciones de `text-primary-*` sobre `bg-primary-*` cumplen los requisitos, especialmente en los tonos claros.

!!! warning "Errores frecuentes"

    1. **Usar Tailwind sin entender CSS.** El error más grave es aprender Tailwind como atajo para no aprender CSS. Cuando algo no funciona, el desarrollador prueba clases al azar hasta que "se ve bien", sin entender por qué. Esto genera código frágil e imposible de depurar. Tailwind acelera a quien sabe CSS; retrasa a quien no lo sabe.

    2. **Abusar de valores arbitrarios.** Si cada propiedad de tu interfaz usa `w-[314px]`, `h-[127px]`, `text-[15px]` y `p-[23px]`, no estás usando Tailwind: estás escribiendo CSS inline con una sintaxis diferente. Los valores arbitrarios deben ser excepcionales, no la norma.

    3. **Crear clases semánticas con @apply de forma masiva.** El error opuesto al anterior: usar `@apply` para redefinir `.btn`, `.card`, `.header`, `.sidebar` en un archivo CSS global, recreando el CSS tradicional dentro de Tailwind. Esto anula las ventajas del utility-first y crea dependencias ocultas entre el HTML y el CSS.

    4. **No aprovechar la configuración de `@theme`.** Usar siempre `text-[#1a56db]` en lugar de definir `--color-primary-500: #1a56db` una vez y usar `text-primary-500` consistentemente. La configuración centralizada existe precisamente para evitar valores mágicos dispersos por el código.

    5. **Ignorar la variante `dark:` al construir la interfaz.** Desarrollar toda la aplicación en modo claro y luego intentar añadir el modo oscuro "después" requiere revisitar cada componente y añadir `dark:` a cada clase. El tema oscuro debe contemplarse desde el primer componente.

    6. **Mezclar CSS tradicional y Tailwind en el mismo componente sin criterio.** Ver un componente con `class="sidebar"` y en la hoja de estilos `.sidebar { @apply flex flex-col h-full bg-gray-900 text-white; }`. Si ya estás usando Tailwind, usa las clases directamente en el HTML. Si necesitas una clase semántica, probablemente necesitas un componente Angular.

    7. **Anidar variantes incorrectamente.** Intentar escribir `hover:dark:bg-gray-800` cuando el orden correcto es `dark:hover:bg-gray-800`. Las variantes se aplican en el orden en que se escriben, de izquierda a derecha, y el orden afecta a la especificidad y al comportamiento.

    8. **Olvidar que Tailwind usa mobile-first.** Escribir `lg:grid-cols-3 grid-cols-1` es un error: las clases sin prefijo se aplican SIEMPRE, por lo que `grid-cols-1` anularía a `lg:grid-cols-3` incluso en pantallas grandes. El orden correcto es `grid-cols-1 lg:grid-cols-3`: 1 columna por defecto, 3 a partir de lg.

    9. **Usar `@apply` con variantes responsive.** No es válido escribir `.sidebar { @apply w-64 md:w-0; }`. `@apply` no soporta variantes responsive; las variantes deben aplicarse en el HTML directamente o replicarse en media queries CSS tradicionales.

    10. **No verificar el CSS generado en producción.** Durante el desarrollo, Tailwind puede generar más CSS del necesario. En producción, el motor JIT genera solo el CSS utilizado. Verifica siempre el build de producción (`ng build --configuration production`) para ver el tamaño real del CSS que recibirán las personas usuarias.

!!! abstract "Resumen"

    Esta unidad ha proporcionado una formación completa en Tailwind CSS 4 como herramienta profesional para el desarrollo de interfaces en Angular. Hemos comenzado desmontando el debate entre "CSS tradicional" y "Tailwind", aclarando que Tailwind es CSS con otro nombre y que su filosofía utility-first aborda problemas reales de los equipos de desarrollo: consistencia forzada, eliminación de guerras de naming, CSS muerto cero y un sistema de diseño embebido que genera coherencia visual sin esfuerzo.

    La configuración de Tailwind 4 en Angular aprovecha el ecosistema moderno de Vite con el plugin `@tailwindcss/vite`, simplificando la integración a tres pasos: instalar paquetes, añadir el plugin, e importar Tailwind en los estilos globales. La personalización con `@theme` y colores oklch proporciona un control preciso sobre el sistema de diseño sin archivos de configuración JavaScript.

    La organización del CSS en un proyecto Angular con Tailwind sigue una estrategia clara de tres niveles: estilos globales mínimos, Tailwind en plantillas como práctica estándar, y `@apply` como excepción muy justificada. Esta estrategia mantiene el código mantenible y evita los antipatrones de ambas filosofías.

    Hemos recorrido el vocabulario esencial de clases utility organizadas por funcionalidad (layout, espaciado, colores, tipografía, estados, dark mode, responsive, formularios, accesibilidad), y hemos explorado técnicas avanzadas como valores arbitrarios, variantes `peer` y `group`, y el selector `has-*`, todas ellas potenciadas por el motor JIT que genera exclusivamente el CSS utilizado.

    Finalmente, hemos abordado la integración de Tailwind en el flujo de trabajo con VS Code IntelliSense y la estrategia de migración progresiva en proyectos existentes, preparando al alumnado para aplicar estos conocimientos tanto en proyectos nuevos como en brownfield.

## Recursos complementarios

### Documentación oficial
- **Tailwind CSS 4** - Documentación oficial: https://tailwindcss.com/docs/v4-beta
- **Tailwind CSS con Vite**: https://tailwindcss.com/docs/installation/vite
- **Tailwind CSS con PostCSS**: https://tailwindcss.com/docs/installation/postcss
- Tailwind CSS `@theme` directive: https://tailwindcss.com/docs/theme
- **Tailwind CSS IntelliSense para VS Code**: https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss

### Tutoriales y cursos
- **Tailwind CSS from Zero to Production** (canal oficial de Tailwind en YouTube)
- **Tailwind CSS Fundamentals** (Tailwind Labs)
- **"Every Layout"** de Heydon Pickering y Andy Bell (patrones de layout aplicables con Tailwind)
- **"Refactoring UI"** de Adam Wathan y Steve Schoger (libro de los creadores de Tailwind sobre diseño para desarrolladores)

### Herramientas complementarias
- **Headwind**: extensión de VS Code para ordenar clases de Tailwind automáticamente
- **Tailwind Fold**: extensión de VS Code para plegar clases de Tailwind largas
- **Prettier plugin para Tailwind**: https://github.com/tailwindlabs/prettier-plugin-tailwindcss
- **Color.review**: herramienta web para verificar contraste de colores con espacio oklch
- **OKLCH Color Picker**: https://oklch.com

### Comunidad y referencias
- **Tailwind CSS GitHub Discussions**: https://github.com/tailwindlabs/tailwindcss/discussions
- **Tailwind CSS Showcase**: https://tailwindcss.com/showcase
- **Tailwind UI** (componentes de pago de referencia, no necesarios pero inspiradores): https://tailwindui.com
- **Awesome Tailwind CSS**: https://github.com/aniftyco/awesome-tailwindcss (lista curada de recursos)
