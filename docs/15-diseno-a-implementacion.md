---
icon: lucide/arrow-right-left
---

# Unidad 15: Del Diseño a la Implementación

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Analizar diseños de interfaces en Figma utilizando el modo desarrollador (Dev Mode) para extraer sistemáticamente medidas, colores, tipografías, espaciados y assets, documentándolos de forma que puedan ser implementados fielmente.
2. Extraer un sistema de design tokens completo a partir de un diseño en Figma, organizándolos en categorías (colores, tipografía, espaciado, bordes, sombras) y documentándolos en tablas de referencia para desarrollo.
3. Configurar un tema completo de Tailwind CSS 4 utilizando la directiva `@theme`, traduciendo los design tokens extraídos de Figma a variables CSS personalizadas con nombres semánticos y soporte para modo oscuro.
4. Identificar y clasificar los componentes de un diseño aplicando la metodología Atomic Design, decidiendo qué elementos serán átomos, moléculas y organismos, y plasmando esta decisión en una arquitectura de carpetas Angular coherente.
5. Implementar al menos 8 componentes de interfaz en Angular standalone + Tailwind, traduciendo fielmente los diseños de Figma a código funcional con tipado TypeScript y soporte para todos los estados (default, hover, focus, disabled, error, loading, empty).
6. Documentar todos los componentes implementados en Storybook, creando stories para cada variante y estado, asegurando que el catálogo de componentes implementados coincide con el sistema de diseño de Figma.
7. Exportar y optimizar assets gráficos (iconos SVG, imágenes, fuentes) desde Figma para su uso en la aplicación, aplicando técnicas de optimización para web (compresión de imágenes, SVG inline vs sprite, fuentes con font-display swap).
8. Integrar todos los componentes en pantallas completas funcionales de una aplicación Angular, demostrando que el flujo completo Figma → Design Tokens → Tailwind @theme → Componentes Angular → Storybook → Aplicación funciona de manera fluida y profesional.

## Resultado de aprendizaje asociado

Esta unidad integradora contribuye, como RA principal, al **RA 3** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 3.** Crea componentes visuales valorando y empleando herramientas específicas.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE a) Se han identificado las herramientas para diseño y prueba de componentes.
- CE b) Se han creado componentes visuales.
- CE c) Se han definido sus métodos y propiedades con asignación de valores por defecto.
- CE d) Se han determinado los eventos a los que debe responder el componente y se les han asociado las acciones correspondientes.
- CE f) Se han documentado los componentes creados.
- CE h) Se han programado aplicaciones cuyo interfaz gráfico utiliza los componentes creados.

Como RA secundario, se vincula al **RA 4** («Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad»):

- CE g) Se ha diseñado el aspecto de la interfaz de usuario (colores y fuentes entre otros) atendiendo a su legibilidad.

!!! note "Conocimientos previos"

    Esta unidad integra y aplica todos los conocimientos adquiridos en las unidades anteriores. El alumnado debe dominar:

    - **Unidad 1:** Conceptos de UX/UI, Diseño Centrado en el Usuario, tipos de interfaces, evolución de las GUI.
    - **Unidad 9:** Entorno de desarrollo completo configurado (Node.js, Angular CLI, Tailwind CSS 4, ESLint, Prettier, Storybook, Git). TypeScript (tipos, interfaces, genéricos, decoradores). Angular (standalone components, signals, control flow @if/@for, inputs/outputs, servicios, routing). Tailwind (clases utilitarias, configuración @theme, responsive prefixes, dark mode).
    - **Unidad 4:** Figma a nivel de diseño (Auto Layout, componentes, variantes, variables, Dev Mode, exportación de assets, handoff).
    - **Unidad 5:** Layouts modernos con Flexbox, CSS Grid y posicionamiento a través de Tailwind. Construcción de dashboards, layouts SaaS, ecommerce y aplicaciones de chat.

    Antes de iniciar esta unidad, se verificará que todo el alumnado tiene su entorno funcional y su proyecto Angular + Tailwind + Storybook operativo (el configurado a lo largo de las Unidades 9 y 10). Quienes no lo tengan recibirán un proyecto base para no quedar rezagados.

## Contenidos

**FASE 1: Inspección de diseños en Figma**
- **Lectura sistemática de un diseño**: metodología de capas (de fuera hacia dentro), jerarquía visual (tamaño, color, posición), espaciado, agrupación lógica.
- **Uso del Dev Mode** para extraer información precisa: medidas, distancias, colores (hex/rgba), tipografías (familia, peso, tamaño, line-height, letter-spacing), bordes y sombras.
- Identificación de patrones de Auto Layout en el diseño y traducción a estructuras Flexbox/Grid.
- **Anotaciones y especificaciones en Figma**: cómo leerlas y cómo crearlas.
- **Checklist de inspección**: lista de verificación para no olvidar nada al analizar un diseño antes de implementar.
- **Comparación de versiones del diseño**: identificación de cambios entre iteraciones del diseño y planificación de las modificaciones en código.

**FASE 2: Extracción del sistema de diseño (Design Tokens)**
- Identificación de la paleta de colores completa en el diseño:
  - Colores de marca (primario, secundario, acento).
  - Colores neutros (escala de grises para fondos, textos, bordes).
  - Colores semánticos (success, warning, error, info).
  - Variantes claras/oscuras para modo oscuro.
- Identificación de la escala tipográfica:
  - Familias tipográficas (heading, body, mono).
  - Escala de tamaños (xs, sm, base, lg, xl, 2xl, 3xl, 4xl).
  - Pesos utilizados (light, regular, medium, semibold, bold).
  - Interlineados (line-height) y espaciado entre letras (letter-spacing).
- Identificación de la escala de espaciado:
  - Múltiplo base (generalmente 4px u 8px).
  - Valores de la escala: 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 80, 96...
- Identificación de border-radius (escala de redondeos: none, sm, md, lg, xl, 2xl, full).
- Identificación de sombras (box-shadow) y otros efectos (blur, backdrop-filter).
- **Documentación en una tabla de Design Tokens**: formato estructurado con nombre del token, valor, descripción, ejemplo de uso.

**FASE 3: Configuración de Tailwind @theme**
- Traducción de los Design Tokens extraídos a la directiva `@theme` de Tailwind 4.
- Mapeo de categorías:
  - Colores de Figma → `--color-{nombre}: {valor}` en @theme.
  - Tipografías de Figma → `--font-{nombre}: {familia}`, `--text-{tamaño}: {valor}`, `--font-weight-{nombre}: {peso}`, `--leading-{nombre}: {interlineado}`.
  - Espaciados de Figma → `--spacing-{nombre}: {valor}`.
  - Border-radius de Figma → `--radius-{nombre}: {valor}`.
- **Configuración de modo oscuro**: variables con valores diferentes según el selector `.dark` (estrategia `class` de Tailwind).
- **Configuración de fuentes**: importación desde Google Fonts o archivos locales con `@font-face`.
- Configuración de estilos base (`@layer base`): estilos para `body`, headings (`h1`-`h6`), enlaces, scrollbar, selección de texto, antialiasing.
- **Verificación**: crear un componente de prueba que use los nuevos tokens para confirmar que la configuración funciona.

**FASE 4: Organización de componentes Angular**
- **Aplicación de Atomic Design** al análisis del diseño:
  - Átomos: elementos indivisibles (Button, Input, Icon, Badge, Avatar, Label, Checkbox, Radio, Toggle, Divider, Spinner).
  - Moléculas: combinaciones simples de átomos (InputField = Label + Input + Error message; SearchBar = Input + Icon + Button; ListItem = Avatar + Text + Badge).
  - Organismos: secciones complejas de la interfaz (Navbar, Sidebar, Card, Modal, Table, Form, DataGrid, Chart, Dashboard, UserMenu).
  - Templates: composiciones de organismos que definen la estructura de una página (DashboardTemplate, AuthTemplate, SettingsTemplate).
  - Pages: templates con contenido real (DashboardPage, LoginPage, SettingsPage).
- **Creación de la arquitectura de carpetas** del proyecto Angular:

```
src/app/
├── shared/
│   ├── ui/                    # Átomos
│   │   ├── button/
│   │   ├── input/
│   │   ├── badge/
│   │   ├── avatar/
│   │   ├── icon/
│   │   ├── checkbox/
│   │   ├── radio/
│   │   ├── toggle/
│   │   ├── spinner/
│   │   └── divider/
│   ├── components/            # Moléculas
│   │   ├── input-field/
│   │   ├── search-bar/
│   │   ├── list-item/
│   │   ├── data-table/
│   │   └── file-upload/
│   ├── layouts/               # Templates (organismos de layout)
│   │   ├── auth-layout/
│   │   ├── dashboard-layout/
│   │   └── settings-layout/
│   └── services/              # Servicios compartidos
│       ├── theme.service.ts
│       └── ...
├── features/                  # Pages y feature-specific components
│   ├── auth/
│   │   ├── login/
│   │   ├── register/
│   │   └── ...
│   ├── dashboard/
│   │   ├── dashboard-page/
│   │   ├── widgets/
│   │   └── ...
│   └── settings/
└── app.component.ts           # Root component
```

- **Criterios de decisión**: ¿qué va en shared/ui, shared/components, shared/layouts, features? Reglas: en shared/ui van los átomos puramente presentacionales; en shared/components van moléculas reutilizables; en shared/layouts van templates de layout; en features van páginas completas y componentes específicos de una funcionalidad.

**FASE 5: Implementación de componentes**
- Proceso iterativo para cada componente:
  1. Analizar el componente en Figma: dimensiones, variantes, estados.
  2. Crear el componente Angular con CLI: `ng g c shared/ui/button --standalone`.
  3. Definir los inputs (usando la función `input<T>()`) y outputs (`output<T>()`).
  4. Implementar el template HTML con clases Tailwind.
  5. Implementar la lógica de variantes (clases condicionales basadas en inputs).
  6. Comparar visualmente con el diseño de Figma (abrir Figma en Dev Mode + la app en el navegador lado a lado).
  7. Ajustar hasta que la implementación coincida con el diseño (dentro de márgenes razonables de 1-2px).
  8. Escribir las stories de Storybook cubriendo todas las variantes y estados.
  9. Escribir tests unitarios básicos (renderización, cambios de estado al modificar inputs).
  10. Documentar el componente en Storybook Docs (descripción, props, ejemplos).
  11. Pasar al siguiente componente.

**FASE 6: Exportación y optimización de assets**
- Iconos:
  - **Exportación desde Figma**: seleccionar capa → Export → SVG.
  - Alternativa mejor: usar una librería de iconos (Lucide, Heroicons, Iconify) que ya está optimizada.
  - **Optimización de SVGs**: usar SVGO para eliminar metadata, comentarios y código innecesario.
  - **Estrategias**: SVG inline (para iconos que necesitan cambiar de color dinámicamente) vs SVG como imagen (para iconos estáticos) vs SVG sprite (para rendimiento con muchos iconos).
- Imágenes:
  - **Exportación desde Figma**: PNG (rasterizado) o SVG (si es vectorial simple).
  - **Formatos web**: PNG (con transparencia), JPEG (fotos sin transparencia), WebP (formato moderno, mejor compresión), AVIF (aún mejor compresión, soporte creciente).
  - **Optimización**: usar herramientas como Squoosh, Sharp, ImageOptim, o plugins de build (vite-plugin-imagemin).
  - **Responsive images**: atributo `srcset` y elemento `<picture>` para servir diferentes resoluciones según el dispositivo.
- Fuentes:
  - Opción A: Google Fonts con `@import` en el CSS global (fácil, CDN rápida).
  - Opción B: Auto-hospedaje (las fuentes se descargan y se sirven desde el mismo dominio). Mejor para rendimiento y privacidad (no leak a Google).
  - **Configuración**: `@font-face` en `@layer base` del CSS, con `font-display: swap` para evitar FOIT (Flash of Invisible Text).

**FASE 7: Construcción de pantallas completas**
- Composición de organismos y moléculas para construir páginas completas.
- Implementación de la navegación (Angular Router) conectando las páginas.
- Gestión de estado global con Signals (señales compartidas mediante servicios).
- Implementación de layouts de página (usando los templates de shared/layouts).
- Conexión con datos (mockeados en esta fase, APIs reales en proyectos posteriores).
- Implementación de todos los estados de la página: ideal, loading (skeleton screens), empty (sin datos), error (fallo al cargar), edge cases (datos extremadamente largos, caracteres especiales, etc.).

**FASE 8: Testing y aseguramiento de la calidad**
- **Testing unitario**: tests para componentes individuales verificando renderización condicional basada en inputs.
- **Testing de integración**: tests para organismos que componen múltiples átomos/moléculas.
- **Testing visual**: comparación Storybook vs Figma (manual o automatizada con Chromatic).
- **Auditoría de accesibilidad**: usar axe DevTools, WAVE, o el addon de Storybook para detectar problemas.
- **Auditoría de rendimiento**: Lighthouse audit para verificar métricas de Core Web Vitals (LCP, FID/INP, CLS).
- **Revisión de código**: eslint y prettier sin errores, código TypeScript tipado sin `any`, cobertura de tests adecuada.

## Desarrollo teórico

### FASE 1: Inspección de diseños en Figma

La inspección de un diseño es el primer paso crítico en el proceso de implementación. ==Un diseño mal inspeccionado conduce a una implementación incorrecta==, retrabajo, frustración y, en última instancia, una interfaz que no coincide con la visión del diseñador. Lejos de ser una tarea mecánica, inspeccionar bien un diseño requiere método, atención al detalle y comprensión de los patrones de diseño.

**Metodología de inspección sistemática**

Cuando recibes un diseño en Figma, la tentación es empezar inmediatamente a programar el componente más visible o más interesante. Esta aproximación es ineficiente. En su lugar, sigue un proceso estructurado:

**Paso 1: Visión general.** Antes de inspeccionar ningún detalle, recorre el diseño completo. Entiende el propósito de la pantalla: ¿qué tarea realiza el usuario aquí? ¿Qué información es la más importante? ¿Cuál es el flujo esperado? Esta comprensión de alto nivel te ayudará a priorizar y a entender por qué ciertos elementos tienen el tamaño, color o posición que tienen.

**Paso 2: Identificación de patrones recurrentes.** Busca elementos que se repiten a lo largo del diseño: ¿Hay un estilo consistente de botones? ¿Todas las tarjetas tienen el mismo padding y border-radius? ¿Hay un patrón de lista que se repite? Estas recurrencias son los futuros componentes reutilizables. Marca mentalmente (o con notas en Figma) estos patrones.

**Paso 3: Descomposición por capas (de fuera hacia dentro).** Empieza por el frame más externo (la pantalla completa) y ve profundizando. Para cada nivel de la jerarquía, pregúntate: ¿Qué sistema de layout usa? (Auto Layout horizontal, Auto Layout vertical, Grid, posicionamiento libre). ¿Cuáles son sus dimensiones? ¿Qué espaciado (padding, gap) tiene?

**Paso 4: Inspección detallada de cada elemento.** Para cada elemento significativo, utiliza el **Dev Mode** de Figma (atajo Shift+D) para extraer:
- Dimensiones exactas (width × height en px).
- Distancias a elementos adyacentes y a los bordes del contenedor padre.
- Colores: fills (relleno), strokes (borde). Anota el valor hex y, crucialmente, el NOMBRE de la variable de Figma si se utilizó una variable.
- Tipografía: font family, weight, size, line height, letter spacing, paragraph spacing, text align, color.
- Bordes: corner radius (independiente por esquina o uniforme), stroke weight, stroke align (inside, center, outside).
- Efectos: drop shadow (X, Y, blur, spread, color), inner shadow, layer blur, background blur.
- Opacidad (del elemento completo y de fills/strokes individuales).

**Paso 5: Identificación de estados.** El diseño que recibes normalmente muestra el "happy path": todo cargado correctamente, datos ideales, ningún error. Pero en la aplicación real, la pantalla pasará por múltiples estados:
- **Ideal:** El diseño que recibes.
- **Loading / Skeleton:** ¿Cómo se ve mientras se cargan los datos? ¿Spinner central? ¿Esqueletos de contenido (skeleton screens)?
- **Empty:** ¿Qué muestra cuando no hay datos? (ej: "No tienes tareas pendientes. ¡Crea tu primera tarea!")
- **Error:** ¿Cómo se muestra un error de red o de servidor? ¿Un toast? ¿Un mensaje inline? ¿Un estado de error en el componente afectado?
- **Edge cases:** ¿Qué pasa si el nombre del usuario tiene 50 caracteres? ¿Si una celda de la tabla contiene una URL de 300 caracteres? ¿Si se cargan 10,000 items en la lista? (Aquí el desarrollador probablemente necesitará virtualización, pero el diseñador debe ser consciente de estos límites).

!!! warning "Trampa"

    Si el diseño no incluye estos estados, consulta con el diseñador antes de implementar. Implementar estados adivinando es una de las principales causas de inconsistencia visual en las aplicaciones.

**Paso 6: Documentación de la inspección.** Crea un documento (puede ser un Notion, un Google Doc, o incluso comentarios en el propio Figma) con:
- Un checklist de elementos inspeccionados.
- Duda y preguntas para el diseñador.
- Observaciones sobre posibles problemas técnicos (animaciones costosas, fuentes no disponibles gratuitamente, assets en resoluciones insuficientes, etc.).

Este documento será tu referencia durante la implementación y evitará que tengas que volver a Figma cada 5 minutos para "¿cuánto padding tenía esta tarjeta?".

**Uso del Dev Mode de Figma**

El Dev Mode es la herramienta principal para la inspección. Al activarlo (Shift+D), la interfaz de Figma cambia para mostrar información orientada al desarrollo:

- **Panel de inspección:** Al seleccionar un elemento, muestra sus propiedades en formato de código (CSS por defecto, configurable a Tailwind, SwiftUI, Compose). No copies ciegamente este código (a veces es incorrecto o incompleto), pero úsalo como referencia rápida.

- **Medidas:** Al seleccionar un elemento, muestra su width y height. Al pasar el cursor sobre otros elementos, muestra la distancia entre ellos (muy útil para verificar gaps y paddings).

- **Variables:** Si el diseño usa variables de Figma, Dev Mode muestra el nombre de la variable y su valor actual. Esto es extremadamente valioso para la FASE 2 (extracción de design tokens).

- **Assets:** Panel que lista los elementos exportables en la selección. Puedes descargar iconos, imágenes e ilustraciones directamente.

- **Comparación de cambios:** Si el diseño fue modificado, Dev Mode resalta los frames/capas que cambiaron desde la última vez que los inspeccionaste (marcados con un punto azul). Puedes ver exactamente qué cambió y decidir si necesitas actualizar tu implementación.

**Checklist de inspección (para imprimir o tener a mano)**

Al inspeccionar un diseño antes de implementar, verifica que tienes respuesta para todo esto:

- [ ] Dimensiones del viewport/pantalla (width × height).
- [ ] **Layout principal**: ¿flex? ¿grid? ¿combinación?
- [ ] **Breakpoints responsive**: ¿el diseño muestra versiones móvil/tablet/desktop?
- [ ] **Colores utilizados** (con nombres de variables si las hay): primario, secundario, neutros (fondo, superficie, texto primario, texto secundario, borde), semánticos (success, warning, error, info).
- [ ] Tipografías: familias, escala de tamaños, pesos, interlineados.
- [ ] Espaciados: padding y gap en cada contenedor significativo.
- [ ] Border-radius: valores para botones, tarjetas, inputs, modales, etc.
- [ ] Sombras y efectos: elevaciones (si las hay), blurs.
- [ ] Estados de componentes interactivos (hover, focus, active, disabled, loading).
- [ ] Estados de página (loading, empty, error).
- [ ] Iconos: ¿están disponibles como SVG? ¿Qué librería de iconos usa el diseño?
- [ ] Imágenes y assets: ¿son placeholder o finales? ¿En qué resolución?
- [ ] Animaciones y transiciones: ¿están descritas? (duración, easing, qué propiedades cambian).
- [ ] Comportamiento responsive: ¿cómo cambia el layout en móvil? (sidebar → drawer off-canvas, columnas → apiladas, etc.).

### FASE 2: Extracción del sistema de diseño (Design Tokens)

Los **design tokens** son la "materia prima" del diseño. Extraerlos correctamente del archivo Figma es posiblemente la tarea más importante de todo el proceso: si los tokens son incorrectos o incompletos, cada componente que implementes será ligeramente inexacto, y corregirlo después requerirá tocar decenas de archivos.

**Proceso de extracción**

1. **Abrir el panel de variables de Figma** (icono de variable en la barra lateral o panel "Local variables"). Identificar todas las colecciones de variables definidas (Colors, Typography, Spacing, Effects, etc.).

2. Si el diseño NO usa variables de Figma (usa estilos o valores hardcodeados), debes **inferir los tokens** inspeccionando múltiples componentes y buscando patrones:
   - Inspecciona todos los botones: ¿qué color de fondo usan? ¿Son consistentes? Anota.
   - Inspecciona todos los textos: ¿qué color usan los títulos? ¿y el texto normal? ¿y el texto secundario? ¿Son consistentes? Anota.
   - Mide los paddings de todas las tarjetas, botones, inputs, etc. ¿Hay un patrón? Anota.

**Paleta de colores**

Organiza los colores en categorías:

**Colores de marca (Brand):**
- `primary-50`, `primary-100`, ..., `primary-900`, `primary-950` (escala completa).
- `secondary-50` a `secondary-950` (si la marca tiene color secundario).

**Colores neutros (Neutral/Gray):**
- `neutral-0` (blanco), `neutral-50` (casi blanco, fondos sutiles), `neutral-100`, `neutral-200`, `neutral-300` (bordes), `neutral-400`, `neutral-500` (texto secundario), `neutral-600`, `neutral-700`, `neutral-800`, `neutral-900` (texto principal), `neutral-950` (casi negro).

**Colores semánticos:**
- `success-500` (verde para éxito/positivo), `success-100` (fondo sutil verde).
- `warning-500` (ámbar/naranja para advertencias), `warning-100`.
- `error-500` (rojo para errores), `error-100`.
- `info-500` (azul claro para información), `info-100`.

**Variantes de modo oscuro (si aplica):**
- En modo oscuro, los neutros se invierten (neutral-900 para fondo, neutral-50 para texto).
- Los colores de marca suelen mantenerse pero con ajustes de saturación/luminosidad para mantener el contraste.
- Documenta ambas versiones (Light y Dark) en tu tabla de tokens.

**Escala tipográfica**

Define tokens para cada nivel tipográfico, no solo los valores crudos. Por ejemplo, en lugar de solo `font-size: 14px`, define `--text-sm` con toda la información asociada:

| Token | font-family | font-size | font-weight | line-height | letter-spacing | Uso |
|---|---|---|---|---|---|---|
| `--text-xs` | Inter | 0.75rem (12px) | 400 | 1rem (16px) | 0 | Captions, badges |
| `--text-sm` | Inter | 0.875rem (14px) | 400 | 1.25rem (20px) | 0 | Texto secundario, labels |
| `--text-base` | Inter | 1rem (16px) | 400 | 1.5rem (24px) | 0 | Texto de cuerpo |
| `--text-lg` | Inter | 1.125rem (18px) | 500 | 1.75rem (28px) | 0 | Subtítulos |
| `--text-xl` | Inter | 1.25rem (20px) | 600 | 1.75rem (28px) | 0 | Títulos de tarjeta |
| `--text-2xl` | Inter | 1.5rem (24px) | 600 | 2rem (32px) | 0 | Títulos de página |
| `--text-3xl` | Inter | 1.875rem (30px) | 700 | 2.25rem (36px) | -0.025em | Headings principales |
| `--text-4xl` | Inter | 2.25rem (36px) | 700 | 2.5rem (40px) | -0.025em | Hero headings |

!!! info "Dato clave"

    Nota: Tailwind 4 usa rem como unidad base (1rem = 16px por defecto). Es recomendable trabajar en rem en lugar de px para respetar las preferencias de tamaño de fuente del usuario.

**Escala de espaciado**

Define una escala basada en un múltiplo consistente (generalmente 4px = 0.25rem, que coincide con la escala por defecto de Tailwind):

| Token | Valor (px) | Valor (rem) | Uso típico |
|---|---|---|---|
| `--spacing-0` | 0 | 0 | Sin espaciado |
| `--spacing-1` | 4 | 0.25rem | Micro-espaciado (icono-texto) |
| `--spacing-2` | 8 | 0.5rem | Gap pequeño, padding de chips |
| `--spacing-3` | 12 | 0.75rem | Gap medio, padding de inputs |
| `--spacing-4` | 16 | 1rem | Padding estándar de componentes |
| `--spacing-5` | 20 | 1.25rem | Padding amplio |
| `--spacing-6` | 24 | 1.5rem | Gap entre secciones |
| `--spacing-8` | 32 | 2rem | Padding de página |
| `--spacing-10` | 40 | 2.5rem | Gap grande entre secciones |
| `--spacing-12` | 48 | 3rem | Muy grande |
| `--spacing-16` | 64 | 4rem | Macro-espaciado |

**Border-radius**

| Token | Valor | Uso |
|---|---|---|
| `--radius-none` | 0 | Sin redondeo |
| `--radius-sm` | 0.125rem (2px) | Casi sin redondeo |
| `--radius` | 0.25rem (4px) | Redondeo por defecto |
| `--radius-md` | 0.375rem (6px) | Inputs, botones pequeños |
| `--radius-lg` | 0.5rem (8px) | Botones estándar |
| `--radius-xl` | 0.75rem (12px) | Tarjetas, modales |
| `--radius-2xl` | 1rem (16px) | Tarjetas grandes |
| `--radius-3xl` | 1.5rem (24px) | Contenedores muy redondeados |
| `--radius-full` | 9999px | Píldoras, círculos, avatares |

**Sombras**

| Token | Valor CSS | Uso |
|---|---|---|
| `--shadow-sm` | `0 1px 2px 0 rgb(0 0 0 / 0.05)` | Elevación sutil |
| `--shadow` | `0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)` | Elevación estándar |
| `--shadow-md` | `0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)` | Elevación media |
| `--shadow-lg` | `0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)` | Elevación alta (tarjetas, modales) |
| `--shadow-xl` | `0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)` | Elevación muy alta |

### FASE 3: Configuración de Tailwind @theme

Con los design tokens documentados en tu tabla, el siguiente paso es traducirlos a la configuración de Tailwind 4. A diferencia de Tailwind 3 (que usaba `tailwind.config.js`), Tailwind 4 usa CSS puro con la directiva `@theme`.

**Archivo styles.css completo comentado**

```css
/* Importar Tailwind (esto incluye reset, base, componentes y utilidades) */
@import "tailwindcss";

/* ============================================
   DESIGN TOKENS - extraídos del diseño Figma
   ============================================ */

@theme {
  /* --- COLORES DE MARCA --- */
  --color-primary-50: #eff6ff;
  --color-primary-100: #dbeafe;
  --color-primary-200: #bfdbfe;
  --color-primary-300: #93c5fd;
  --color-primary-400: #60a5fa;
  --color-primary-500: #3b82f6;
  --color-primary-600: #2563eb;
  --color-primary-700: #1d4ed8;
  --color-primary-800: #1e40af;
  --color-primary-900: #1e3a8a;
  --color-primary-950: #172554;

  /* Colores semánticos (atajos a tokens primitivos) */
  --color-primary: var(--color-primary-600);
  --color-primary-hover: var(--color-primary-700);
  --color-primary-light: var(--color-primary-100);
  --color-primary-dark: var(--color-primary-800);

  /* --- COLORES NEUTROS --- */
  --color-neutral-0: #ffffff;
  --color-neutral-50: #f8fafc;
  --color-neutral-100: #f1f5f9;
  --color-neutral-200: #e2e8f0;
  --color-neutral-300: #cbd5e1;
  --color-neutral-400: #94a3b8;
  --color-neutral-500: #64748b;
  --color-neutral-600: #475569;
  --color-neutral-700: #334155;
  --color-neutral-800: #1e293b;
  --color-neutral-900: #0f172a;
  --color-neutral-950: #020617;

  /* Semánticos neutros */
  --color-bg-primary: var(--color-neutral-0);
  --color-bg-secondary: var(--color-neutral-50);
  --color-bg-tertiary: var(--color-neutral-100);
  --color-text-primary: var(--color-neutral-900);
  --color-text-secondary: var(--color-neutral-500);
  --color-text-tertiary: var(--color-neutral-400);
  --color-text-disabled: var(--color-neutral-300);
  --color-border-default: var(--color-neutral-200);
  --color-border-strong: var(--color-neutral-300);

  /* --- COLORES SEMÁNTICOS DE ESTADO --- */
  --color-success-50: #f0fdf4;
  --color-success-500: #22c55e;
  --color-success-700: #15803d;
  --color-success: var(--color-success-500);
  --color-success-light: var(--color-success-50);
  --color-success-dark: var(--color-success-700);

  --color-warning-50: #fffbeb;
  --color-warning-500: #f59e0b;
  --color-warning-700: #b45309;
  --color-warning: var(--color-warning-500);
  --color-warning-light: var(--color-warning-50);
  --color-warning-dark: var(--color-warning-700);

  --color-error-50: #fef2f2;
  --color-error-500: #ef4444;
  --color-error-700: #b91c1c;
  --color-error: var(--color-error-500);
  --color-error-light: var(--color-error-50);
  --color-error-dark: var(--color-error-700);

  --color-info-50: #eff6ff;
  --color-info-500: #3b82f6;
  --color-info-700: #1d4ed8;
  --color-info: var(--color-info-500);
  --color-info-light: var(--color-info-50);
  --color-info-dark: var(--color-info-700);

  /* --- TIPOGRAFÍA --- */
  --font-sans: 'Inter', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, monospace;

  /* --- BORDER RADIUS --- */
  --radius-sm: 0.125rem;
  --radius-default: 0.25rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-xl: 0.75rem;
  --radius-2xl: 1rem;
  --radius-3xl: 1.5rem;
  --radius-full: 9999px;

  /* --- SOMBRAS --- */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-default: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
}

/* ============================================
   MODO OSCURO
   ============================================ */

.dark {
  --color-bg-primary: #0f172a;      /* neutral-900 */
  --color-bg-secondary: #1e293b;    /* neutral-800 */
  --color-bg-tertiary: #334155;     /* neutral-700 */
  --color-text-primary: #f8fafc;    /* neutral-50 */
  --color-text-secondary: #94a3b8;  /* neutral-400 */
  --color-text-tertiary: #64748b;   /* neutral-500 */
  --color-text-disabled: #475569;   /* neutral-600 */
  --color-border-default: #334155;  /* neutral-700 */
  --color-border-strong: #475569;   /* neutral-600 */

  /* Ajustes de sombras para modo oscuro */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.3);
  --shadow-default: 0 1px 3px 0 rgb(0 0 0 / 0.4);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.4);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.5);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.5);
}

/* ============================================
   ESTILOS BASE
   ============================================ */

@layer base {
  /* Importar fuentes (ejemplo con Google Fonts) */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

  html {
    scroll-behavior: smooth;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  body {
    font-family: var(--font-sans);
    color: var(--color-text-primary);
    background-color: var(--color-bg-primary);
    line-height: 1.5;
  }

  /* Scrollbar estilizada (webkit) */
  ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
  }
  ::-webkit-scrollbar-track {
    background: var(--color-bg-secondary);
  }
  ::-webkit-scrollbar-thumb {
    background: var(--color-neutral-300);
    border-radius: 9999px;
  }
  ::-webkit-scrollbar-thumb:hover {
    background: var(--color-neutral-400);
  }

  /* Selección de texto */
  ::selection {
    background-color: var(--color-primary-light);
    color: var(--color-primary-dark);
  }
}
```

**Verificación de la configuración**

Crea un componente de prueba simple que utilice los nuevos tokens para verificar que todo funciona:

```html
<div class="min-h-screen bg-bg-primary p-8">
  <h1 class="text-3xl font-bold text-primary mb-4">Verificación de Design Tokens</h1>
  
  <div class="grid grid-cols-2 gap-4">
    <!-- Muestras de colores semánticos -->
    <div class="bg-primary text-white p-4 rounded-xl">Primary (bg-primary)</div>
    <div class="bg-bg-secondary text-text-primary p-4 rounded-xl border border-border-default">Secondary surface</div>
    <div class="bg-success text-white p-4 rounded-xl">Success</div>
    <div class="bg-error text-white p-4 rounded-xl">Error</div>
    <div class="bg-warning text-white p-4 rounded-xl">Warning</div>
    
    <!-- Sombras -->
    <div class="bg-bg-primary p-4 rounded-xl shadow-default">shadow-default</div>
    <div class="bg-bg-primary p-4 rounded-xl shadow-lg">shadow-lg</div>
    
    <!-- Radio -->
    <div class="bg-primary p-4 rounded-sm text-white">rounded-sm</div>
    <div class="bg-primary p-4 rounded-lg text-white">rounded-lg</div>
    <div class="bg-primary p-4 rounded-2xl text-white">rounded-2xl</div>
    <div class="bg-primary p-4 rounded-full text-white text-center">rounded-full</div>
  </div>
</div>
```

Si todo se renderiza correctamente (los colores coinciden con los del diseño de Figma, las sombras y los border-radius se ven como esperas), la configuración está lista. Este paso, aunque parezca administrativo, es la inversión más rentable del proceso: ==definir correctamente los tokens ahora evita discrepancias visuales en todos los componentes que implementaremos después==.

### FASE 4: Organización de componentes Angular

Con los tokens configurados, volvemos al diseño de Figma para identificar los componentes que necesitamos implementar. Aplicamos la metodología **Atomic Design** (Brad Frost) que ya practicamos conceptualmente en la Unidad 1.

**Proceso de identificación de componentes**

1. Abre el diseño de Figma con las pantallas completas.
2. En un papel o documento aparte, lista todos los elementos visuales que ves.
3. Agrúpalos por nivel atómico:

**Átomos (elementos indivisibles, no tienen sentido por sí solos):**
- Button (con variantes: primary, secondary, outline, ghost, danger)
- Input (con estados: default, focus, error, disabled; con variantes: text, password, number, textarea)
- Label (texto asociado a un input)
- Icon (SVG individual, de una librería como Lucide o Heroicons)
- Badge (etiqueta pequeña: colores, tamaños)
- Avatar (imagen circular con fallback a iniciales)
- Checkbox (individual, con estados checked/unchecked/indeterminate, disabled)
- Radio (individual)
- Toggle/Switch
- Divider (línea separadora horizontal o vertical)
- Spinner (indicador de carga)

**Moléculas (combinaciones de átomos que funcionan juntos):**
- InputField = Label + Input + ErrorMessage (texto de error debajo del input)
- SearchBar = Input + Icon (lupa) + botón de limpiar (X) opcional
- CheckboxField = Checkbox + Label
- RadioGroup = múltiples RadioField (Radio + Label) con un Label del grupo
- ToggleField = Toggle + Label
- ListItem = Avatar + texto (título + subtítulo) + Badge/Icon opcional a la derecha
- Breadcrumb = lista de enlaces con separadores
- Pagination = botones de página + anterior/siguiente
- Toast/Notification = Icon + mensaje + botón de cerrar

**Organismos (secciones complejas de la interfaz):**
- Navbar (barra de navegación superior: logo + menú + acciones + avatar)
- Sidebar (barra lateral: navegación jerárquica)
- Card (tarjeta contenedora: header opcional, contenido, footer opcional)
- Modal/Dialog (overlay + ventana emergente con título, contenido, acciones)
- Dropdown/Menu (menú desplegable con items)
- Table (tabla de datos con cabeceras, filas, ordenación, selección)
- DataGrid (tabla avanzada con filtros, paginación, ordenación, selección múltiple)
- Form (formulario con múltiples InputFields, validación, botón de submit)
- Tabs (barra de pestañas con contenido asociado)
- Chart/Graph (contenedor de gráfico con título, leyenda, tooltips)

**Templates (layouts de página):**
- DashboardLayout (sidebar + header + contenido con grid para widgets)
- AuthLayout (layout centrado para login/registro, sin sidebar ni header complejo)
- SettingsLayout (sidebar de secciones de configuración + área de contenido)
- DocsLayout (sidebar de navegación de documentación + área de contenido con tabla de contenidos)

**Pages (instancias de templates con contenido real):**
- DashboardPage
- LoginPage
- RegisterPage
- UserProfilePage
- SettingsPage
- NotFoundPage (404)

**Jerarquía de implementación**

No implementes los componentes en orden alfabético ni en el orden de la lista. Implementa siguiendo la cadena de dependencias:

1. Primero los átomos (no dependen de nada).
2. Luego las moléculas (dependen de átomos).
3. Luego los organismos (dependen de moléculas y átomos).
4. Luego los templates (dependen de organismos).
5. Finalmente las pages (dependen de templates).

Dentro de los átomos, empieza por los más usados y los más simples: **Button, Input, Icon, Badge**. Deja para después los más complejos (Table, DataGrid, Chart).

### FASE 5: Implementación de componentes

Para cada componente, seguimos un proceso iterativo de 10 pasos. Vamos a detallarlo con un ejemplo real: la implementación de un componente `InputField` (molécula que combina Label, Input, Error Message).

**Iteración: Implementación de InputFieldComponent**

**Paso 1: Analizar el componente en Figma**

En Figma, abrimos Dev Mode y seleccionamos un InputField. Observamos:
- Estructura: label (texto superior, weight medium, size 14px, color neutral-700), input (height 40px, padding horizontal 12px, border 1px neutral-300, border-radius 8px), mensaje de error (texto inferior, size 12px, color error-500, margin-top 4px).
- Estados: default (borde neutral-300), focus (borde primary-500, ring de 3px primary-100), error (borde error-500, texto error debajo), disabled (opacity 50%, fondo neutral-100).
- Variantes: con leading icon, con trailing icon.

**Paso 2: Crear el componente Angular CLI**

```bash
ng g c shared/components/input-field --standalone --inline-template --inline-style
```

**Paso 3: Definir inputs y outputs**

```typescript
import { Component, input, output, model } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-input-field',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './input-field.component.html',
  styleUrl: './input-field.component.css',
})
export class InputFieldComponent {
  readonly label = input.required<string>();
  readonly type = input<'text' | 'password' | 'email' | 'number' | 'search'>('text');
  readonly placeholder = input('');
  readonly error = input<string | null>(null);
  readonly disabled = input(false);
  readonly leadingIcon = input<string | undefined>(undefined);
  readonly trailingIcon = input<string | undefined>(undefined);

  // Two-way binding con el padre ([(value)]="miValor")
  readonly value = model('');
}
```

**Paso 4: Implementar el template HTML con Tailwind**

```html
<div class="flex flex-col gap-1.5">
  <!-- Label -->
  <label
    [for]="label().toLowerCase().replace(/\s+/g, '-')"
    class="text-sm font-medium"
    [class.text-neutral-700]="!disabled() && !error()"
    [class.text-error]="!!error()"
    [class.text-neutral-400]="disabled()"
  >
    {{ label() }}
  </label>

  <!-- Input wrapper -->
  <div class="relative">
    <!-- Leading icon -->
    @if (leadingIcon()) {
      <div class="absolute left-3 top-1/2 -translate-y-1/2 text-neutral-400 pointer-events-none">
        <app-icon [name]="leadingIcon()!" size="sm" />
      </div>
    }

    <!-- Input -->
    <input
      [type]="type()"
      [placeholder]="placeholder()"
      [disabled]="disabled()"
      [id]="label().toLowerCase().replace(/\s+/g, '-')"
      [ngModel]="value()"
      (ngModelChange)="value.set($event)"
      class="w-full px-3 py-2 text-sm rounded-lg border bg-white transition-colors duration-150
        placeholder:text-neutral-400
        focus:outline-none focus:ring-2 focus:ring-offset-0
        disabled:opacity-50 disabled:bg-neutral-50 disabled:cursor-not-allowed"
      [class.border-neutral-300]="!error() && !disabled()"
      [class.border-error]="!!error()"
      [class.focus:ring-primary-100]="!error()"
      [class.focus:border-primary-500]="!error()"
      [class.focus:ring-error-100]="!!error()"
      [class.focus:border-error]="!!error()"
      [class.pl-10]="!!leadingIcon()"
      [class.pr-10]="!!trailingIcon()"
    />

    <!-- Trailing icon -->
    @if (trailingIcon()) {
      <div class="absolute right-3 top-1/2 -translate-y-1/2 text-neutral-400 pointer-events-none">
        <app-icon [name]="trailingIcon()!" size="sm" />
      </div>
    }
  </div>

  <!-- Error message -->
  @if (error()) {
    <p class="text-xs text-error mt-0.5 flex items-center gap-1">
      <app-icon name="alert-circle" size="xs" />
      {{ error() }}
    </p>
  }
</div>
```

**Paso 5: Clases condicionales basadas en inputs**

!!! tip "Consejo"

    Observa que en lugar de concatenar strings manualmente, usamos `[class.clase]="condicion"` de Angular para activar/desactivar clases condicionalmente. Esta técnica es más limpia y mantenible que construir un string de clases con ternarios anidados.

**Paso 6: Comparar visualmente con Figma**

Abrir la aplicación Angular (`npm start`) en una ventana del navegador, y Figma en otra (o en VS Code con el plugin Figma). Comparar lado a lado: ¿los colores son exactamente iguales? ¿El padding coincide? ¿El border-radius es correcto? ¿El tamaño de fuente es el mismo? Ajustar según sea necesario.

**Paso 7: Ajustes**

Errores comunes que se detectan en la comparación:
- El interlineado es diferente en Figma que en el navegador (Figma renderiza tipografías de manera ligeramente distinta).
- El color en Figma parece más claro/oscuro por la configuración de gestión de color del sistema operativo.
- El espaciado entre label e input no coincide (en Figma podrían ser 6px y nosotros pusimos `gap-1.5` = 6px = 0.375rem; correcto).
- El borde en focus es más grueso en implementación que en diseño (en Figma sumaron el stroke al tamaño del frame; en CSS el borde NO se suma si usamos `box-sizing: border-box`, que es el comportamiento por defecto de Tailwind).

**Paso 8: Escribir las stories de Storybook**

```typescript
import type { Meta, StoryObj } from '@storybook/angular';
import { InputFieldComponent } from './input-field.component';
import { userEvent, within, expect } from '@storybook/test';

const meta: Meta<InputFieldComponent> = {
  title: 'Components/InputField',
  component: InputFieldComponent,
  tags: ['autodocs'],
  argTypes: {
    label: { control: 'text' },
    type: { control: 'select', options: ['text', 'password', 'email', 'number', 'search'] },
    placeholder: { control: 'text' },
    error: { control: 'text' },
    disabled: { control: 'boolean' },
    leadingIcon: { control: 'select', options: [undefined, 'user', 'mail', 'search', 'lock'] },
    trailingIcon: { control: 'select', options: [undefined, 'eye', 'eye-off', 'x', 'check'] },
  },
  render: (args) => ({
    props: {
      ...args,
      value: args.value ?? '',
      valueChange: (val: string) => { /* noop en Storybook */ },
    },
    template: `<app-input-field [label]="label" [type]="type" [placeholder]="placeholder" [error]="error" [disabled]="disabled" [leadingIcon]="leadingIcon" [trailingIcon]="trailingIcon" [(value)]="value" />`,
  }),
};

export default meta;
type Story = StoryObj<InputFieldComponent>;

// Historias para cada estado y variante
export const Default: Story = {
  args: { label: 'Email', type: 'email', placeholder: 'tu@email.com' },
};

export const WithLeadingIcon: Story = {
  args: { label: 'Email', type: 'email', placeholder: 'tu@email.com', leadingIcon: 'mail' },
};

export const Password: Story = {
  args: { label: 'Password', type: 'password', placeholder: '••••••••', trailingIcon: 'eye' },
};

export const WithError: Story = {
  args: { label: 'Email', type: 'email', placeholder: 'tu@email.com', error: 'Email no válido' },
};

export const Disabled: Story = {
  args: { label: 'Email', type: 'email', placeholder: 'tu@email.com', disabled: true },
};

export const WithValue: Story = {
  args: { label: 'Nombre', value: 'María García', type: 'text' },
};

// Story con test de interacción
export const TypingInteraction: Story = {
  args: { label: 'Nombre', type: 'text' },
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    const input = canvas.getByPlaceholderText('') as HTMLInputElement; // placeholder vacío
    await userEvent.type(input, 'Hello', { delay: 100 });
    await expect(input).toHaveValue('Hello');
  },
};
```

**Paso 9: Tests unitarios**

```typescript
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { InputFieldComponent } from './input-field.component';
import { FormsModule } from '@angular/forms';

describe('InputFieldComponent', () => {
  let component: InputFieldComponent;
  let fixture: ComponentFixture<InputFieldComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InputFieldComponent, FormsModule],
    }).compileComponents();

    fixture = TestBed.createComponent(InputFieldComponent);
    component = fixture.componentInstance;
    fixture.componentRef.setInput('label', 'Test Label');
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should display the label', () => {
    const labelElement: HTMLLabelElement = fixture.nativeElement.querySelector('label');
    expect(labelElement.textContent?.trim()).toBe('Test Label');
  });

  it('should display error message when error input is set', () => {
    fixture.componentRef.setInput('error', 'Campo requerido');
    fixture.detectChanges();
    const errorElement = fixture.nativeElement.querySelector('p.text-error');
    expect(errorElement).toBeTruthy();
    expect(errorElement.textContent?.trim()).toContain('Campo requerido');
  });

  it('should disable input when disabled input is true', () => {
    fixture.componentRef.setInput('disabled', true);
    fixture.detectChanges();
    const input: HTMLInputElement = fixture.nativeElement.querySelector('input');
    expect(input.disabled).toBeTrue();
  });

  it('should apply error border class when error is set', () => {
    fixture.componentRef.setInput('error', 'Error');
    fixture.detectChanges();
    const input: HTMLInputElement = fixture.nativeElement.querySelector('input');
    expect(input.classList).toContain('border-error');
  });
});
```

**Paso 10: Documentar en Storybook Docs**

Añadir JSDoc al componente y sus inputs:

```typescript
/**
 * InputField es un componente de formulario que combina un label,
 * un input y un mensaje de error opcional.
 *
 * Soporta iconos a izquierda y derecha del input,
 * múltiples tipos de input (text, email, password, number, search),
 * y estados de error y disabled.
 *
 * @example
 * <app-input-field
 *   label="Email"
 *   type="email"
 *   placeholder="tu@email.com"
 *   [(value)]="email"
 *   [error]="emailError"
 *   leadingIcon="mail"
 * />
 */
export class InputFieldComponent {
  /** Etiqueta descriptiva del campo. Se renderiza como `<label>` asociado al input. */
  readonly label = input.required<string>();
  /** Tipo de input HTML (text, email, password, number, search). Por defecto 'text'. */
  readonly type = input<'text' | 'password' | 'email' | 'number' | 'search'>('text');
  // ... etc.
}
```

**Repetir para todos los componentes**

Este proceso de 10 pasos se repite para cada componente del sistema de diseño. Con práctica, los átomos más simples (Badge, Avatar, Icon) se pueden implementar en 15-20 minutos cada uno. Moléculas como InputField o SearchBar pueden llevar 30-45 minutos. Organismos como Table o Modal pueden llevar 1-2 horas.

### FASE 6: Exportación y optimización de assets

Los assets gráficos (iconos, imágenes, fuentes) son parte integral de la interfaz. Una mala gestión de assets ralentiza la carga de la página, consume ancho de banda del usuario y da una impresión de baja calidad.

**Iconos**

La decisión más importante es **qué estrategia de iconos usar**:

**Opción A: Librería de iconos (RECOMENDADA)**

En lugar de exportar manualmente iconos SVG de Figma uno por uno, usa una **librería de iconos** profesional que:
- Ya está optimizada (SVGs limpios, sin metadatos innecesarios).
- Ofrece consistencia (todos los iconos tienen el mismo estilo visual, grosor, grid).
- Proporciona el icono como componente Angular, no como archivo estático.
- Soporta cambiar color, tamaño y stroke-width dinámicamente.

Librerías recomendadas:
- **Lucide Angular:** `npm install lucide-angular` (fork de Feather Icons, mantenido y con soporte para Angular, más de 1000 iconos).
- **Angular Material Icons:** `@angular/material` incluye `MatIconModule` (si ya usas Angular Material).
- **Heroicons (Tailwind team):** Iconos SVG diseñados por el equipo de Tailwind, perfectos para estilos Tailwind. Se copian como SVG directo o se usa la librería `@ng-icons/heroicons`.

```bash
npm install lucide-angular
```

```typescript
// icon.component.ts
import { Component, input } from '@angular/core';
import { LucideAngularModule, icons } from 'lucide-angular'; // Importa solo los iconos que uses

@Component({
  selector: 'app-icon',
  standalone: true,
  imports: [LucideAngularModule],
  template: `<lucide-icon [name]="name()" [size]="size()" [class]="customClass()"></lucide-icon>`,
})
export class IconComponent {
  readonly name = input.required<string>();
  readonly size = input<number>(20);
  readonly customClass = input('');
}
```

**Opción B: Exportación manual desde Figma**

Si necesitas iconos muy específicos diseñados a medida:
1. En Figma, selecciona la capa del icono.
2. En el panel Export (modo diseño), configura: formato SVG, resolución 1x, y activa "Show in export" para que aparezca en Dev Mode.
3. Descarga el SVG.
4. Pásalo por SVGO (optimizador de SVG) para eliminar código innecesario: comentarios, metadatos de Figma, IDs de capa, etc.
5. Incrústalo como SVG inline en tu componente Angular, o guárdalo en `assets/icons/` y usa `<img src="assets/icons/mi-icono.svg" />`.

**Opción C: SVG Sprite (para muchos iconos)**

Para aplicaciones con docenas o cientos de iconos, genera un sprite SVG (un archivo SVG que contiene todos los iconos como `<symbol>`s) y refiérete a cada icono con `<use href="sprite.svg#icon-name" />`. Esto reduce las peticiones HTTP.

**Imágenes**

**Exportación desde Figma:**
- Para gráficos vectoriales (ilustraciones, diagramas, logos): exportar como SVG.
- Para imágenes raster (fotos, texturas): exportar como PNG (2x para pantallas retina) o mejor aún, como PNG original y luego convertir a WebP/AVIF con herramientas externas.

**Formatos y optimización:**
- **WebP:** Soporta transparencia y ofrece un 25-35% mejor compresión que PNG/JPEG. Soporte universal en navegadores modernos (>96% en 2025).
- **AVIF:** Aún mejor compresión que WebP (hasta 50% mejor que JPEG). Soporte creciente (>90% en navegadores modernos en 2025).
- **Estrategia**: servir WebP como formato principal, con fallback a PNG/JPEG para navegadores antiguos (usando el elemento `<picture>` o la librería de build de Vite que genera automáticamente múltiples formatos).

**Responsive images:**
```html
<img
  src="producto-800w.webp"
  srcset="producto-400w.webp 400w, producto-800w.webp 800w, producto-1200w.webp 1200w"
  sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
  alt="Descripción del producto"
  loading="lazy"
  decoding="async"
/>
```

!!! info "Definición"

    El atributo `loading="lazy"` difiere la carga de imágenes que no están en el viewport inicial, mejorando el LCP (Largest Contentful Paint). El atributo `decoding="async"` permite al navegador decodificar la imagen de forma no bloqueante.

**Fuentes**

**Estrategia recomendada: auto-hospedaje con `@font-face`**

!!! tip "Consejo"

    Aunque Google Fonts es conveniente, auto-hospedar las fuentes en tu propio servidor ofrece mejor rendimiento (sin petición DNS a Google, sin round-trips adicionales) y mejor privacidad (no filtras datos de tus usuarios a Google).

```css
/* fonts.css */
@layer base {
  @font-face {
    font-family: 'Inter';
    src: url('/assets/fonts/inter-var.woff2') format('woff2');
    font-weight: 300 700;
    font-style: normal;
    font-display: swap; /* Muestra texto con fallback mientras carga la fuente */
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }
}
```

La propiedad `font-display: swap` es crítica: sin ella, el navegador oculta el texto hasta que la fuente se descarga (FOIT - Flash of Invisible Text). Con `swap`, el navegador muestra el texto inmediatamente con una fuente fallback y la intercambia cuando la fuente real se ha cargado.

### FASE 7: Construcción de pantallas completas

Con todos los componentes implementados, documentados y probados, el paso final es componerlos en pantallas completas funcionales. Este es el momento donde todo el trabajo previo rinde frutos: construir una pantalla se convierte en ensamblar componentes preexistentes, no en implementar desde cero.

**Ejemplo: Implementación de DashboardPage**

```typescript
import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashboardLayoutComponent } from '../../shared/layouts/dashboard-layout/dashboard-layout.component';
import { ButtonComponent } from '../../shared/ui/button/button.component';
import { CardComponent } from '../../shared/ui/card/card.component';
import { BadgeComponent } from '../../shared/ui/badge/badge.component';
import { SpinnerComponent } from '../../shared/ui/spinner/spinner.component';

@Component({
  selector: 'app-dashboard-page',
  standalone: true,
  imports: [CommonModule, DashboardLayoutComponent, ButtonComponent, CardComponent, BadgeComponent, SpinnerComponent],
  template: `
    <app-dashboard-layout pageTitle="Dashboard">
      <!-- Estado de carga -->
      @if (loading()) {
        <div class="flex items-center justify-center py-20">
          <app-spinner size="lg" />
        </div>
      }
      <!-- Estado de error -->
      @else if (error()) {
        <div class="flex flex-col items-center justify-center py-20 text-center">
          <div class="w-16 h-16 bg-error-light rounded-full flex items-center justify-center mb-4">
            <span class="text-3xl">!</span>
          </div>
          <h2 class="text-lg font-semibold mb-2">Error al cargar los datos</h2>
          <p class="text-sm text-text-secondary mb-4">{{ error() }}</p>
          <app-button variant="primary" (clicked)="loadData()">Reintentar</app-button>
        </div>
      }
      <!-- Estado vacío -->
      @else if (stats().length === 0) {
        <div class="flex flex-col items-center justify-center py-20 text-center">
          <div class="w-16 h-16 bg-bg-secondary rounded-full flex items-center justify-center mb-4">
            <span class="text-3xl">📊</span>
          </div>
          <h2 class="text-lg font-semibold mb-2">No hay datos disponibles</h2>
          <p class="text-sm text-text-secondary mb-4">Comienza añadiendo tu primer proyecto para ver estadísticas.</p>
          <app-button variant="primary">Crear proyecto</app-button>
        </div>
      }
      <!-- Estado ideal -->
      @else {
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
          @for (stat of stats(); track stat.id) {
            <app-card>
              <div class="flex items-start justify-between">
                <div>
                  <p class="text-sm text-text-secondary">{{ stat.label }}</p>
                  <p class="text-2xl font-bold mt-1">{{ stat.value }}</p>
                  <div class="flex items-center gap-1 mt-2">
                    <span [class.text-success]="stat.change > 0" [class.text-error]="stat.change < 0" class="text-sm font-medium">
                      {{ stat.change > 0 ? '↑' : '↓' }} {{ Math.abs(stat.change) }}%
                    </span>
                    <span class="text-xs text-text-secondary">vs. mes anterior</span>
                  </div>
                </div>
                <div class="w-10 h-10 rounded-lg bg-primary-light flex items-center justify-center">
                  <app-icon [name]="stat.icon" size="lg" class="text-primary" />
                </div>
              </div>
            </app-card>
          }
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <app-card class="lg:col-span-2">
            <h3 class="text-lg font-semibold mb-4">Ingresos mensuales</h3>
            <div class="h-80 bg-bg-secondary rounded-lg flex items-center justify-center text-text-secondary text-sm">
              [Gráfico placeholder]
            </div>
          </app-card>
          <app-card>
            <h3 class="text-lg font-semibold mb-4">Actividad reciente</h3>
            <div class="flex flex-col gap-4">
              @for (activity of recentActivity(); track activity.id) {
                <div class="flex items-start gap-3">
                  <div class="w-2 h-2 rounded-full flex-shrink-0 mt-1.5" [class.bg-primary]="activity.type === 'info'" [class.bg-success]="activity.type === 'success'" [class.bg-warning]="activity.type === 'warning'"></div>
                  <div>
                    <p class="text-sm font-medium">{{ activity.title }}</p>
                    <p class="text-xs text-text-secondary">{{ activity.time }}</p>
                  </div>
                </div>
              }
            </div>
          </app-card>
        </div>
      }
    </app-dashboard-layout>
  `,
})
export class DashboardPageComponent {
  protected readonly Math = Math;

  protected loading = signal(true);
  protected error = signal<string | null>(null);
  protected stats = signal<Stat[]>([]);
  protected recentActivity = signal<Activity[]>([]);

  constructor() {
    this.loadData();
  }

  protected loadData() {
    this.loading.set(true);
    this.error.set(null);
    // Simular carga de datos (en proyecto real, llamada HTTP)
    setTimeout(() => {
      try {
        // Simular éxito
        this.stats.set([
          { id: 1, label: 'Usuarios totales', value: '24,521', change: 12.5, icon: 'users' },
          { id: 2, label: 'Ingresos', value: '€45,231', change: 20.1, icon: 'dollar-sign' },
          { id: 3, label: 'Pedidos', value: '1,234', change: -5.2, icon: 'shopping-cart' },
          { id: 4, label: 'Tasa de conversión', value: '3.24%', change: 8.1, icon: 'trending-up' },
        ]);
        this.recentActivity.set([
          { id: 1, title: 'Nuevo usuario registrado', time: 'Hace 2 minutos', type: 'info' },
          { id: 2, title: 'Pago recibido por €129.00', time: 'Hace 10 minutos', type: 'success' },
          { id: 3, title: 'Alerta de stock bajo', time: 'Hace 1 hora', type: 'warning' },
          { id: 4, title: 'Nuevo pedido #ORD-042', time: 'Hace 2 horas', type: 'success' },
          { id: 5, title: 'Informe semanal generado', time: 'Hace 3 horas', type: 'info' },
        ]);
        this.loading.set(false);
      } catch (e) {
        this.error.set('No se pudieron cargar los datos. Verifica tu conexión.');
        this.loading.set(false);
      }
    }, 1500);
  }
}

interface Stat {
  id: number;
  label: string;
  value: string;
  change: number;
  icon: string;
}

interface Activity {
  id: number;
  title: string;
  time: string;
  type: 'info' | 'success' | 'warning';
}
```

**Puntos clave de esta implementación:**

1. **Todos los estados cubiertos:** loading (spinner centrado), error (mensaje con botón de reintentar), empty (mensaje con acción sugerida), ideal (datos reales). El usuario nunca ve una pantalla en blanco o rota.

2. **Componentes reutilizados:** DashboardLayout, Card, Button, Badge, Spinner, Icon. Ninguno de estos fue implementado en esta página; simplemente se importan y se usan.

3. **Layout responsive:** KPI cards en grid de 1, 2 o 4 columnas según viewport. Gráfico y actividad en grid de 3 columnas (2/3 + 1/3) en escritorio, apiladas en móvil.

4. **Datos tipados:** Interfaces `Stat` y `Activity` aseguran que los datos tienen la forma correcta. TypeScript detectaría cualquier error al pasar datos mal formados.

5. **Signals para estado:** Loading, error, datos y actividad son signals. Los cambios de estado son reactivos y la UI se actualiza automáticamente.

### FASE 8: Testing y aseguramiento de la calidad

**Testing unitario (Jasmine/Karma o Jest + Angular Testing Library)**

Tests para verificar que los componentes renderizan correctamente según sus inputs:

- **Button**: renderiza con cada variante (primary, secondary, outline, ghost), cada tamaño (sm, md, lg), estado disabled, estado loading.
- **InputField**: renderiza label, input con placeholder, muestra error cuando se proporciona, deshabilita el input cuando disabled es true.
- **Card**: renderiza contenido proyectado con `<ng-content>`, aplica padding y border-radius correctos.
- **Badge**: renderiza con cada variante de color, cada tamaño.

**Testing visual (Storybook + Chromatic o manual)**

Para cada componente, verificar que:
- La story coincide visualmente con el diseño de Figma.
- Todas las variantes y estados se ven correctamente.
- El responsive funciona (usar el addon Viewport de Storybook para simular diferentes tamaños).

**Auditoría de accesibilidad**

Usar el addon `@storybook/addon-a11y` (basado en axe-core) para detectar automáticamente problemas:
- Contraste insuficiente.
- Elementos interactivos sin etiquetas accesibles.
- Imágenes sin alt text.
- Orden de tabulación incorrecto.
- Roles ARIA mal utilizados.

Ejecutar en cada story y corregir todos los problemas detectados.

**Auditoría de rendimiento**

Ejecutar Lighthouse en la aplicación compilada en producción:
- **Performance**: objetivo >= 90. Optimizar imágenes, diferir CSS/JS no crítico, usar lazy loading para componentes/rutas.
- **Accessibility**: objetivo >= 95.
- **Best Practices**: objetivo >= 90.
- **SEO**: objetivo >= 90 (si la aplicación es pública).

## Ejemplos guiados

### Ejemplo guiado 1: Del diseño Figma al componente (Button)

**Objetivo:** Recorrer el flujo completo para un componente atómico simple.

**Duración:** 40 minutos.

**Desarrollo:** El docente comparte un archivo Figma con un design system simple (colores, tipografía, y un component set de Button con variantes Primary/Secondary/Outline × Small/Medium/Large). El alumnado sigue los pasos:

1. Inspeccionar el Button en Dev Mode: anotar dimensiones, paddings, colores, tipografía, border-radius.
2. Verificar que los tokens de color y tipografía están en el archivo CSS (FASE 3).
3. Crear el componente con Angular CLI.
4. Implementar el template con Tailwind según el diseño.
5. Implementar la lógica de variantes (clases condicionales).
6. Comparar lado a lado con Figma.
7. Crear stories en Storybook.
8. Escribir tests unitarios básicos.
9. Verificar accesibilidad (contraste, target size >= 44px).

### Ejemplo guiado 2: Extracción de tokens y configuración de @theme

**Objetivo:** Realizar el proceso completo de extracción de design tokens desde un diseño Figma y configurarlos en Tailwind.

**Duración:** 35 minutos.

**Desarrollo:** A partir de un diseño proporcionado por el docente (un archivo Figma con varias pantallas de una aplicación), el alumnado:

1. Inspecciona el diseño para identificar la paleta de colores (primarios, neutros, semánticos).
2. Identifica la escala tipográfica (familias, tamaños, pesos, interlineados).
3. Identifica la escala de espaciado (midiendo paddings y gaps en múltiples componentes).
4. Identifica border-radius y sombras.
5. Documenta todo en una tabla de Design Tokens.
6. Configura el archivo `styles.css` con la directiva `@theme` de Tailwind 4.
7. Configura el modo oscuro (usando los colores invertidos si el diseño lo incluye, o infiriendo la paleta oscura).
8. Verifica la configuración renderizando un componente de prueba que use los tokens.

### Ejemplo guiado 3: Construcción de una pantalla completa (Dashboard)

**Objetivo:** Integrar todos los componentes en una pantalla funcional.

**Duración:** 45 minutos.

**Desarrollo:** El docente guía al alumnado en la construcción de la pantalla DashboardPage descrita en la FASE 7. Se enfatiza:

1. **Uso del layout template:** Importar y usar `DashboardLayoutComponent` que proporciona sidebar + header.
2. **Composición de componentes:** Usar Card, Badge, Spinner, Icon, Button — todos previamente implementados y documentados en Storybook.
3. **Gestión de estados con Signals:** Implementar loading, error, empty e ideal.
4. **Tipado TypeScript:** Definir interfaces Stat y Activity para los datos.
5. **Responsive:** Verificar que el grid de KPI cards y el layout de gráfico+actividad se adaptan correctamente.

## Actividades guiadas

### Actividad guiada 1: Inspección colaborativa de un diseño

**Duración:** 25 minutos

**Desarrollo:** El docente proyecta un diseño de Figma y el alumnado, trabajando en parejas, completa un checklist de inspección para una pantalla asignada. Cada pareja debe identificar: layout principal, paleta de colores, tipografías, espaciados, componentes reutilizables, estados necesarios (loading, empty, error). Puesta en común donde cada pareja expone sus hallazgos y el docente complementa o corrige.

### Actividad guiada 2: Code review de un componente

**Duración:** 20 minutos

**Desarrollo:** El docente proporciona la implementación de un componente (por ejemplo, un InputField con 3-4 errores intencionados: falta `min-w-0`, clases condicionales incorrectas, falta estado disabled visual, tipado `any` en lugar de tipos literales). El alumnado, en parejas, realiza una code review:
1. Identificar los errores.
2. Proponer correcciones.
3. Comparar la corrección con el diseño original en Figma.
4. Puesta en común.

### Actividad guiada 3: Auditoría de accesibilidad de un componente

**Duración:** 20 minutos

**Desarrollo:** El docente proporciona un componente Card implementado pero con problemas de accesibilidad (imagen sin alt text, botones sin aria-label, texto con contraste insuficiente, no navegable por teclado). Usando el addon a11y de Storybook o axe DevTools, el alumnado debe:
1. Ejecutar la auditoría.
2. Identificar todos los problemas.
3. Proponer soluciones concretas (código HTML/Tailwind específico).
4. Implementar las correcciones y verificar que la auditoría pasa.

## Actividades propuestas

### Actividad 1

**Nivel:** Básico-Medio
**Objetivo:** Implementar 3 átomos del sistema de diseño a partir de diseños Figma.
**Enunciado:** Se te proporciona un archivo Figma (enlace o capturas) que contiene el diseño de tres componentes atómicos: Badge, Avatar y Divider.

1. **Inspecciona** cada componente en Dev Mode y completa la tabla de especificaciones para cada uno: dimensiones, variantes (colores, tamaños), padding, border-radius, tipografía (para Badge), colores de fondo y texto por variante.

2. **Implementa** los tres componentes como componentes standalone de Angular + Tailwind en `src/app/shared/ui/`. Deben usar los design tokens del `@theme` proporcionado (no colores hardcodeados).

3. **Crea stories en Storybook** cubriendo TODAS las variantes: Badge (5 variantes de color × 3 tamaños mínimo), Avatar (4 tamaños × con imagen, sin imagen/fallback), Divider (horizontal, vertical).

4. **Escribe tests unitarios** para Badge (verificar que se renderiza con la clase de color correcta según input) y Avatar (verificar que muestra iniciales cuando no hay imagen o la imagen falla).

5. **Verifica visualmente** que tu implementación coincide con el diseño de Figma (márgenes de 1-2px aceptables).

**Requisitos:** Todos los estilos con Tailwind. Sin CSS personalizado excepto la configuración `@theme`. Tipado TypeScript sin `any`. Cobertura de tests > 80%.
**Pistas:** Para Avatar con fallback a iniciales, usa el evento `(error)` en la etiqueta `<img>` para cambiar un flag en una signal y mostrar las iniciales en lugar de la imagen.
**Criterios de evaluación:** (1) Fidelidad visual al diseño Figma. (2) Completitud de variantes en Storybook. (3) Calidad de los tests unitarios. (4) Uso correcto de los design tokens del tema.

### Actividad 2

**Nivel:** Medio
**Objetivo:** Implementar un organismo completo (DataTable con búsqueda, filtros y paginación).
**Enunciado:** Implementa un componente `DataTableComponent` en `src/app/shared/components/data-table/` que funcione como una tabla de datos genérica reutilizable. El componente debe aceptar datos tipados mediante un input genérico y ofrecer:

1. **Columnas configurables:** Input que recibe un array de definiciones de columna (key, label, sortable: boolean, filterable: boolean, template opcional para renderizado personalizado).

2. **Búsqueda global:** Input de búsqueda que filtra la tabla en tiempo real (debounced a 300ms) en todas las columnas de texto. Implementar con un signal computado.

3. **Ordenación:** Al hacer clic en el header de una columna, alternar orden ascendente/descendente/ninguno. Indicar visualmente la dirección con un icono de flecha.

4. **Paginación:** División de datos en páginas de N elementos (configurable, default 10). Controles de página anterior/siguiente, número de página actual, y selector de elementos por página (10, 25, 50).

5. **Selección de filas:** Checkbox en cada fila y "seleccionar todos" en el header. Las filas seleccionadas se emiten mediante un output.

6. **Estados:** Loading (skeleton de tabla), Empty ("No se encontraron resultados"), Error (mensaje con botón de reintentar).

**Requisitos:** Tipo genérico en el componente `DataTableComponent<T>`. Las columnas deben definirse con una interfaz tipada que infiera correctamente las claves de T. Tailwind para todos los estilos. Storybook con historias para: tabla con datos, tabla vacía, tabla en loading, tabla con error, tabla con todas las funcionalidades activadas.
**Pistas:** Para el debounce de la búsqueda, investiga cómo implementar debounce con Signals o usa RxJS (`Subject` + `debounceTime`). Para el tipado genérico en Angular, declara el componente con `export class DataTableComponent<T extends Record<string, unknown>>` y usa `@Input() data: T[]`.
**Criterios de evaluación:** (1) Funcionalidad completa (búsqueda, ordenación, paginación, selección). (2) Tipado genérico correcto. (3) Estados loading/empty/error implementados. (4) Calidad visual y alineación con el diseño proporcionado.

### Actividad 3

**Nivel:** Avanzado
**Objetivo:** Implementar el flujo completo Figma → Tokens → Tailwind → Componentes → Storybook → App.
**Enunciado:** Se te proporciona un archivo Figma con el diseño de una aplicación de gestión de biblioteca personal (3 pantallas: Dashboard de resumen, Listado de libros, Detalle de libro). Tu tarea es implementar la aplicación completa siguiendo TODAS las fases del flujo completo:

**Fase 1 (documento):** Checklist de inspección de las 3 pantallas. Identificar layout, colores, tipografías, espaciados, componentes, estados necesarios.

**Fase 2 (documento):** Tabla completa de Design Tokens extraídos del diseño (colores primitivos, colores semánticos, tipografía, espaciado, border-radius, sombras).

**Fase 3 (código):** Archivo `styles.css` con la configuración `@theme` de Tailwind 4 reflejando los tokens extraídos. Incluir modo oscuro (inferir la paleta oscura basada en la clara). Verificar con componente de prueba.

**Fase 4 (documento + código):** Identificación de componentes según Atomic Design. Estructura de carpetas en `src/app/`. Crear la estructura con Angular CLI (al menos los directorios).

**Fase 5 (código):** Implementar AL MENOS los siguientes componentes (átomos + moléculas):
- Button (4 variantes, 3 tamaños)
- Input / InputField (con label, error, iconos)
- Badge (4 colores, 2 tamaños)
- Avatar (con fallback a iniciales)
- Card (contenedor con variantes: default, hoverable)
- BookCard (organismo: Card + imagen + título + autor + badge de estado)
- SearchBar (Input + Icon)
- Modal (overlay + ventana centrada + título + contenido + acciones)

**Fase 5b (código):** Implementar las 3 pantallas:
- **LibraryDashboardPage:** KPI cards (total libros, libros leídos, préstamos activos), gráfico de lectura por mes (placeholder), lista de libros prestados actualmente (tabla simplificada).
- **BookListPage:** SearchBar + grid de BookCards + filtros (por estado: todos, leyendo, leído, pendiente, por género).
- **BookDetailPage:** Abre en modal o página aparte. Muestra: portada grande, título, autor, género, estado, rating (estrellas), sinopsis, notas personales.

**Fase 6 (código):** Exportar o generar los iconos necesarios (usar Lucide). Configurar fuentes (Inter desde Google Fonts o auto-hospedada). Optimizar imágenes de ejemplo.

**Fase 7 (código):** Navegación con Angular Router. Layout template (sidebar + header). Las 3 páginas enrutadas. Estado de la aplicación con Signals en servicio.

**Fase 8 (código + docs):** Tests unitarios para al menos 3 componentes. Historias de Storybook para todos los componentes implementados. Auditoría de accesibilidad (axe) y Lighthouse de la app construida en producción.

**Requisitos:** Código TypeScript sin `any`. Angular standalone components. Tailwind CSS para todos los estilos. Angular Signals para estado (no RxJS). Mínimo 90% de fidelidad visual al diseño Figma.
**Pistas:** Divide la actividad en sprints de 2-3 días. Sprint 1: FASES 1-3 + componentes atómicos. Sprint 2: componentes moleculares + organismos. Sprint 3: pantallas + navegación + Storybook + tests. Entrega incremental con revisión del docente entre sprints.
**Criterios de evaluación:** (1) Fidelidad al diseño Figma. (2) Completitud de la tabla de design tokens y correlación con @theme. (3) Organización de componentes (estructura de carpetas, Atomic Design). (4) Implementación de todos los estados (loading, empty, error, edge cases). (5) Calidad del código (TypeScript, tests, accesibilidad, Storybook docs). (6) Navegación y experiencia de usuario funcional.

### Actividad 4

**Nivel:** Avanzado
**Objetivo:** Implementar un sistema de temas dinámicos (theme switcher) con persistencia y personalización.
**Enunciado:** Implementa un sistema de temas completo para tu aplicación Angular que permita:

1. **Temas predefinidos (mínimo 3):** Tema Claro (Light), Tema Oscuro (Dark), Tema de Alto Contraste (High Contrast para accesibilidad). Cada tema es un conjunto de tokens CSS que se aplican al elemento `:root` o a `<html>`.

2. **Selector de tema:** Un componente `ThemeSwitcher` (dropdown o toggle) en la barra de navegación que permita cambiar entre los temas disponibles.

3. **Persistencia:** La selección del usuario se guarda en `localStorage` y se restaura al recargar la página. Antes de cargar la app, el tema correcto debe aplicarse para evitar un "flash" del tema por defecto (investiga cómo evitarlo: script inline en `index.html` o Angular APP_INITIALIZER).

4. **Detección de preferencia del sistema:** Si el usuario no ha seleccionado un tema manualmente, la app debe respetar la preferencia del sistema operativo (`prefers-color-scheme: dark`). Cambiar automáticamente si el usuario cambia la preferencia del SO mientras la app está abierta.

5. **Tema personalizado por el usuario (avanzado):** Pantalla de configuración donde el usuario puede personalizar colores individuales: color primario (color picker), color de fondo, color de texto, border-radius base, tamaño de fuente base. Estos valores se guardan en localStorage y se aplican como variables CSS que sobreescriben el tema seleccionado.

6. **Transición suave entre temas:** Al cambiar de tema, los colores deben transicionar suavemente (usar `transition: background-color 0.3s, color 0.3s, border-color 0.3s` en elementos clave, o mejor, usar `* { transition: background-color 0.3s ease, color 0.3s ease }` con moderación).

**Requisitos:** Usar Angular Signals + servicios. Implementar `APP_INITIALIZER` para cargar el tema antes de renderizar. CSS Custom Properties (variables CSS) como mecanismo para aplicar temas.
**Pistas:** Crea un `ThemeService` que gestione el tema actual. El servicio expone una signal con el tema activo y métodos para cambiarlo. Usa `DOCUMENT` token de Angular para manipular las clases del `<html>`. Para evitar el flash, añade un pequeño script bloqueante en `<head>` de `index.html` que lea `localStorage` y aplique la clase `dark` o el atributo `data-theme` antes de que se renderice nada.
**Criterios de evaluación:** (1) Correcta gestión de temas (cambio inmediato, sin recarga). (2) Persistencia en localStorage. (3) Sin flash del tema incorrecto al cargar. (4) Respeto de preferencia del sistema. (5) Transiciones suaves. (6) Documentación de la arquitectura del sistema de temas (diagrama de flujo).

### Actividad 5

**Nivel:** Experto (proyecto de síntesis)
**Objetivo:** Proyecto completo aplicando TODO el módulo.
**Enunciado:** Desarrolla una aplicación web completa de gestión de proyectos (tipo Jira/Linear/Trello simplificado) que demuestre el dominio de todas las competencias del módulo. La aplicación debe incluir:

1. **Sistema de diseño completo implementado en código** (Button, Input, Select, Badge, Avatar, Card, Modal, Table, Tabs, Tooltip, entre otros). Mínimo 15 componentes documentados en Storybook.

2. **Design tokens completos** extraídos de un diseño propio en Figma (o uno proporcionado por el docente), configurados en Tailwind @theme con modo claro y oscuro.

3. **Layout responsive** (sidebar + header + contenido) usando Grid y Flexbox con Tailwind, adaptado a móvil, tablet y escritorio.

4. **3-4 pantallas funcionales:**
   - Dashboard: resumen de proyectos, tareas pendientes, actividad reciente.
   - Board / Proyecto: vista kanban con columnas (To Do, In Progress, Review, Done). Arrastrar tareas entre columnas (Angular CDK Drag & Drop).
   - Detalle de tarea: modal o página con título, descripción, estado, prioridad, asignado, fecha, comentarios.
   - Configuración: perfil de usuario, preferencias de tema, notificaciones.

5. **Gestión de estado con Angular Signals:** Servicios con signals para proyectos, tareas, usuario. Datos mockeados pero estructurados como si vinieran de una API (servicios con métodos asíncronos que devuelven Promises/Observables).

6. **Navegación con Angular Router** con lazy loading de features.

7. **Testing:** Tests unitarios para al menos 5 componentes. Tests de integración para al menos 1 pantalla. Storybook con stories para todos los componentes. Auditoría de accesibilidad axe aprobada.

8. **Calidad de código:** ESLint sin errores, Prettier formateado, TypeScript strict, sin `any`, JSDoc en componentes y servicios.

9. **Despliegue:** Aplicación desplegada en Vercel, Netlify o GitHub Pages. Storybook desplegado en Chromatic o GitHub Pages (build estático).

**Requisitos:** Proyecto individual. Repositorio GitHub con README completo (descripción, tecnologías, estructura del proyecto, instrucciones de instalación y ejecución, enlaces a la app y Storybook desplegados). Commits convencionales (feat:, fix:, docs:, test:, etc.). Mínimo 20 commits sustantivos.
**Pistas:** Planifica las tareas en un kanban simple (GitHub Projects o similar). Empieza por los design tokens y la configuración del tema. Luego los átomos. Luego las moléculas y organismos. Luego las pantallas. No intentes implementar todo de golpe; avanza incrementalmente validando cada paso.
**Criterios de evaluación:** Esta actividad puede usarse como proyecto de evaluación final del módulo. Se evaluará según una rúbrica que incluya todas las dimensiones: diseño (tokens, Figma), implementación (componentes, layouts, estado), calidad (tests, lint, tipado, accesibilidad), documentación (Storybook, README), y despliegue (app + Storybook accesibles públicamente).

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Sistema de plugins de temas para aplicaciones Angular empresariales

    Investiga e implementa un sistema de "plugins de temas" inspirado en cómo funcionan los temas de VS Code o los plugins de Figma. La idea es que un "tema" no sea solo un conjunto de colores, sino un módulo autocontenido (un archivo TypeScript/JSON) que exporta:

    1. **Design tokens completos** en un formato estandarizado (JSON Schema validable).
    2. **Metadatos:** nombre, autor, versión, descripción, preview (imagen).
    3. **Reglas de transformación:** cómo derivar tokens semánticos a partir de tokens primitivos (funciones de transformación).
    4. **Assets opcionales:** fuentes, texturas de fondo, iconos personalizados.

    El sistema debe permitir:
    - Cargar temas desde archivos JSON locales o desde una URL (API).
    - Validar el schema del tema antes de aplicarlo.
    - Previsualizar el tema sin necesidad de aplicarlo completamente (aplicar solo a un frame/preview).
    - Componer temas (tema base + overrides del usuario).
    - Exportar el tema actual como archivo descargable.

    Implementa también un "Theme Editor" visual (página dentro de la app Angular) que permita editar y guardar temas sin tocar código. El editor usa color pickers, sliders para tipografía y espaciado, y previsualización en tiempo real.

    Entrega: código fuente del sistema de temas + theme editor + documentación de arquitectura + al menos 3 temas de ejemplo (incluyendo uno de alto contraste para accesibilidad).

    ### Actividad de ampliación 2: Integración real Figma ↔ Storybook con Figma Plugin API

    Desarrolla un flujo de trabajo automatizado que conecte Figma con Storybook usando las APIs de ambas plataformas:

    1. **Plugin de Figma:** Crea un plugin que, al seleccionar un componente en Figma, haga una petición a la API de Storybook (o a un servicio intermedio) para verificar si ese componente ya está implementado y documentado. Si está implementado, muestra un embed del Storybook del componente dentro de Figma. Si no está implementado, muestra un checklist de lo que falta y permite crear un "issue" de implementación (en GitHub Issues, Linear, Jira, etc.).

    2. **GitHub Action:** Crea una acción de GitHub que, al modificar variables de Figma (exportadas a JSON mediante el plugin Design Tokens), genere automáticamente un PR en el repositorio Angular actualizando el archivo `styles.css` con los nuevos tokens.

    3. **Sincronización de estados:** Sistema que compare los componentes documentados en Storybook con los componentes diseñados en Figma y genere un informe de cobertura: "85% de los componentes de Figma están implementados en Storybook. Faltan: DatePicker, FileUpload, RichTextEditor."

    Entrega: código del plugin de Figma, GitHub Action, y README con diagramas del flujo de trabajo y la arquitectura.

    ### Actividad de ampliación 3: Accesibilidad avanzada y testing con usuarios reales

    Amplía la aplicación de gestión de proyectos de la Actividad 5 para alcanzar un nivel de accesibilidad WCAG 2.2 AAA (el más exigente). Esto implica:

    1. **Auditoría completa con herramientas especializadas:** axe-core, WAVE, Lighthouse, Accessibility Insights, ANDI.
    2. **Navegación completa solo con teclado:** Cada pantalla, cada componente, cada modal, cada dropdown debe ser completamente operable sin ratón ni pantalla táctil. Implementa atajos de teclado para acciones frecuentes.
    3. **Compatibilidad con lectores de pantalla:** Prueba con NVDA (Windows) o VoiceOver (macOS). Verifica que cada elemento tiene el rol correcto, nombre accesible, estado comunicado correctamente.
    4. **Redacción accesible:** Textos claros, lenguaje llano, sin jerga técnica innecesaria. Mensajes de error descriptivos que explican cómo solucionar el problema.
    5. **Motion y animaciones:** Respeta `prefers-reduced-motion`. Proporciona alternativas estáticas a las animaciones para usuarios con sensibilidad al movimiento.
    6. **Testing con usuarios reales:** Organiza una sesión de test de accesibilidad con al menos 2 personas que usen tecnologías de asistencia (lector de pantalla, magnificador, navegación por voz). Documenta los problemas encontrados y las soluciones implementadas.

    Entrega: informe de auditoría WCAG 2.2 AAA con evidencias (capturas, vídeos), lista de issues resueltos, y vídeo/write-up del test con usuarios reales.

!!! tip "Buenas prácticas"

    1. **Implementa los átomos primero.** Cada hora invertida en definir correctamente los átomos (Button, Input, Icon, Badge...) se amortiza exponencialmente cuando construyes moléculas y organismos. Un átomo mal implementado propaga sus defectos a todo el sistema.

    2. **Mantén el diseño de Figma abierto durante TODA la implementación.** No lo mires una vez al principio y luego "ya me acuerdo". Consulta Figma constantemente, compara lado a lado, verifica medidas. La memoria visual es traicionera.

    3. **Un componente, una responsabilidad.** Si un componente hace demasiadas cosas, divídelo. Un Button no debería gestionar lógica de negocio. Un InputField no debería conocer la API. La lógica de negocio va en servicios; los componentes solo renderizan y emiten eventos.

    4. **Documenta mientras implementas, no después.** Escribir las stories y los tests DESPUÉS de implementar es tedioso y se procrastina. Hazlo como parte del flujo: implementas un estado, escribes su story, escribes su test. El componente se construye junto con su documentación y su cobertura de pruebas.

    5. **Usa los tokens semánticos del @theme, no valores hardcodeados.** `bg-primary` no `bg-blue-600`. Si mañana el color primario cambia de azul a verde, modificas una línea en `@theme` y toda la aplicación se actualiza. Si usaste `bg-blue-600` en 47 componentes, tienes que editar 47 archivos.

    6. **No te cases con la precisión milimétrica.** Figma renderiza tipografías de forma diferente a los navegadores. Diferencias de 1-2px en espaciados o alineaciones son aceptables y no deben perseguirse obsesivamente. Lo importante es la consistencia visual global.

    7. **Optimiza los assets ANTES de usarlos, no como una tarea "pendiente" para el final.** Iconos sin optimizar, imágenes en PNG de 2MB, fuentes que bloquean el renderizado... estos problemas son fáciles de prevenir y costosos de corregir cuando la aplicación está terminada.

    8. **Prioriza la accesibilidad como un requisito funcional, no como un "nice to have".** Un botón sin aria-label, una tabla sin headers, una imagen sin alt text... son bugs, igual que un botón que no funciona al hacer clic. Trata los problemas de accesibilidad como bugs en tu backlog, no como una lista de deseos para "cuando tengamos tiempo".

!!! warning "Errores frecuentes"

    1. **Empezar por las pantallas en lugar de por los componentes.** Síndrome del "quiero ver algo funcionando ya". Construyes la pantalla de login con HTML + Tailwind directamente, sin componentes. Luego necesitas reutilizar ese input estilizado en el formulario de registro y acabas duplicando código. Implementa los componentes antes de las pantallas.

    2. **No definir los design tokens y usar colores hardcodeados.** "Total, #3B82F6 es fácil de recordar". Tres semanas después, tienes 15 tonalidades ligeramente diferentes de azul porque en algunos sitios pusiste #3b82f6, en otros #3B82F6 (no es lo mismo con opacidad), en otros #4a90d9 "porque me parecía que quedaba mejor"...

    3. **Ignorar los estados (loading, empty, error, edge cases).** Implementas el "happy path" y pasas al siguiente componente. Cuando integras la pantalla con datos reales, todo se rompe: la tabla no tiene datos y muestra cabeceras huérfanas sin un mensaje empty, la API falla y la pantalla se queda en blanco, la imagen del avatar tarda 3 segundos en cargar y el layout baila.

    4. **Copiar y pegar componentes en lugar de reutilizarlos con inputs.** Necesitas un botón rojo para "Eliminar". En lugar de añadir una variante `danger` a tu componente Button (5 minutos), creas un nuevo componente `DangerButton` copiando y pegando (30 segundos). Multiplica esto por 20 componentes y tienes un sistema de diseño que es una colección de copias ligeramente diferentes en lugar de un sistema coherente.

    5. **No tipar correctamente los inputs de los componentes.** Usar `@Input() variant: string` en lugar de `variant = input<'primary' | 'secondary' | 'outline'>('primary')`. El primero acepta cualquier string ("primari", "secundario", "loquesea"). El segundo te da autocompletado, verificación en tiempo de compilación y documentación viva.

    6. **No verificar la implementación contra Figma durante el desarrollo.** Implementas "de memoria" y al final comparas con Figma. Hay 15 discrepancias. Modificar el padding de un componente desencadena ajustes en cascada en moléculas y organismos que lo usan, que ya habías dado por terminados. Compara constantemente.

    7. **No documentar los componentes en Storybook porque "no tengo tiempo".** Storybook es una inversión, no un coste. Los 15 minutos que "ahorras" no documentando un componente los pagarás con creces cuando en 3 semanas no recuerdes qué variantes tiene ese componente o cuando un nuevo miembro del equipo te pregunte "¿cómo se usa este componente?".

    8. **No gestionar correctamente el ciclo de vida del componente.** Dejar suscripciones a Observables abiertas (si usas RxJS), no limpiar event listeners, no destruir timers/intervals. Angular maneja la memoria bien, pero las fugas de memoria por suscripciones no cerradas son difíciles de depurar y degradan el rendimiento con el tiempo.

!!! abstract "Resumen"

    Esta unidad ha sido la culminación del módulo de Desarrollo de Interfaces. Hemos recorrido el flujo profesional completo, desde la inspección de un diseño en Figma hasta la implementación de una aplicación funcional en Angular con componentes documentados en Storybook, pasando por todas las etapas intermedias: extracción de design tokens, configuración del tema de Tailwind, organización de componentes con Atomic Design, implementación iterativa, exportación de assets, y testing de calidad.

    La FASE 1 nos enseñó a leer diseños de manera sistemática, utilizando el **Dev Mode** de Figma como nuestra herramienta principal de inspección. Aprendimos a no confiar en la memoria ni en el "a ojo", sino a extraer medidas precisas, identificar patrones y documentar todo antes de escribir una sola línea de código.

    La FASE 2 nos mostró cómo los diseños contienen un sistema de diseño implícito (o explícito, si se usaron variables de Figma) que podemos extraer en forma de design tokens: colores, tipografías, espaciados, bordes y sombras que constituyen la "materia prima" atómica de la interfaz.

    La FASE 3 convirtió esos design tokens en configuración de Tailwind 4, utilizando la directiva `@theme` para crear un puente directo entre los nombres de las variables en Figma y las clases utilitarias en Tailwind. Con soporte para tema oscuro a través de la estrategia `class` de Tailwind.

    La FASE 4 aplicó **Atomic Design** para organizar los componentes en una arquitectura de carpetas coherente: átomos (shared/ui), moléculas (shared/components), organismos, templates y páginas. Una estructura que escala desde proyectos pequeños hasta aplicaciones empresariales.

    La FASE 5 nos sumergió en la implementación iterativa de componentes: un proceso de 10 pasos que, repetido disciplinadamente para cada componente, garantiza fidelidad al diseño, documentación y cobertura de tests. Implementamos InputField como caso de estudio detallado.

    La FASE 6 cubrió la exportación y optimización de assets: iconos (con librerías como Lucide), imágenes (formatos modernos WebP/AVIF, responsive images, lazy loading), y fuentes (auto-hospedaje con font-display swap para evitar FOIT).

    La FASE 7 compuso todos los componentes en pantallas completas funcionales, implementando todos los estados (loading, error, empty, ideal) y utilizando **Angular Signals** para una gestión de estado reactiva y predecible.

    La FASE 8 cerró con el aseguramiento de la calidad: testing unitario, testing visual con Storybook, auditoría de accesibilidad con axe, y auditoría de rendimiento con Lighthouse.

    El viaje desde la Unidad 1 (conceptos fundamentales de interfaces) hasta esta Unidad 15 (implementación completa) ha sido largo y exigente, pero os ha equipado con las competencias necesarias para enfrentar el desarrollo profesional de interfaces web modernas: desde la comprensión del usuario y el diseño visual hasta la implementación técnica con las herramientas más demandadas en la industria (Angular, TypeScript, Tailwind CSS, Figma, Storybook).

## Recursos complementarios

### Documentación oficial

- **Angular Documentation (angular.dev):** https://angular.dev/overview — Guías de componentes, signals, routing, forms, testing.
- **Tailwind CSS 4 Documentation:** https://tailwindcss.com/docs/v4 — Configuración @theme, valores arbitrarios, directivas.
- **Storybook for Angular:** https://storybook.js.org/docs/angular/get-started
- **Figma Dev Mode Guide:** https://help.figma.com/hc/en-us/articles/15033890310167-Guide-to-Dev-Mode
- **Figma Variables Guide:** https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma
- **Angular CDK Drag & Drop:** https://material.angular.io/cdk/drag-drop/overview

### Libros

- Frost, B. (2016). *Atomic Design*. https://atomicdesign.bradfrost.com — La metodología de organización de componentes (gratuito online).
- Kholmatova, A. (2017). *Design Systems*. Smashing Magazine. Guía práctica para construir sistemas de diseño.
- Freeman, A. (2023). *Pro Angular*. Apress. Referencia profesional completa de Angular.

### Herramientas

- **Lucide Angular:** https://lucide.dev/icons — Libería de iconos con soporte nativo Angular.
- **SVGO:** https://github.com/svg/svgo — Optimizador de SVG (elimina metadatos, reduce tamaño).
- **Squoosh:** https://squoosh.app — Compresor de imágenes web (Google) con comparación lado a lado.
- **Chromatic (Storybook):** https://www.chromatic.com — Testing visual automatizado para Storybook.
- **axe DevTools:** https://www.deque.com/axe/devtools/ — Extensión de navegador y tests automatizados de accesibilidad.
- **Lighthouse:** Herramienta integrada en Chrome DevTools. Auditoría de rendimiento, accesibilidad, SEO, mejores prácticas.
- **WAVE:** https://wave.webaim.org — Evaluador de accesibilidad web (extensión y online).

### Recursos de diseño

- **Figma Community:** https://www.figma.com/community — Miles de sistemas de diseño, componentes y plantillas gratuitas.
- **Material Design 3 (Google):** Sistema de diseño público con todas las especificaciones, tokens y componentes.
- **Design Tokens W3C Community Group:** https://design-tokens.github.io/community-group/format/ — Especificación del formato estándar de design tokens.

### Artículos y guías

- **Refactoring UI (Adam Wathan & Steve Schoger):** https://www.refactoringui.com — Principios prácticos de diseño para desarrolladores.
- **Practical Accessibility (Sara Soueidan):** https://practical-accessibility.today — Curso práctico de accesibilidad web para desarrolladores.
- **CSS for JavaScript Developers (Josh Comeau):** https://css-for-js.dev — Curso exhaustivo de CSS moderno (de pago, excelente).

### Comunidades

- **Angular Discord:** Servidor oficial de Angular (angular.dev/community).
- **Storybook Discord:** Comunidad de Storybook con canales de ayuda.
- **Friends of Figma España:** Comunidad local de usuarios de Figma con eventos y recursos en español.
- **GitHub Universe / Config (Figma):** Conferencias anuales con charlas sobre sistemas de diseño y flujos diseño-desarrollo.
