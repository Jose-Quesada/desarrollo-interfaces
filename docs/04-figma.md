---
icon: lucide/pen-tool
---

# Unidad 4: Diseño de Interfaces con Figma

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Navegar con soltura por el espacio de trabajo de Figma, utilizando frames, capas, páginas, componentes y paneles de propiedades para organizar proyectos de diseño de interfaces de forma profesional.
2. Diseñar layouts responsivos y flexibles utilizando Auto Layout, comprendiendo la equivalencia directa entre las propiedades de Auto Layout en Figma y las propiedades de Flexbox en CSS/Tailwind.
3. Crear y gestionar variables de diseño (colores, tipografías, espaciados, border-radius) en Figma, organizadas en colecciones y con soporte para múltiples modos (light/dark).
4. Construir componentes reutilizables con propiedades configurables y conjuntos de variantes, aplicando los principios de Atomic Design y los sistemas de diseño profesionales.
5. Exportar correctamente assets (SVG, PNG, PDF) y especificaciones de diseño (código CSS, medidas, colores, tipografías) para el handoff a desarrollo.
6. Utilizar el modo desarrollador de Figma (Dev Mode) para inspeccionar diseños, extraer medidas, colores y fragmentos de código CSS/Tailwind.
7. Diseñar un sistema de diseño básico completo (Design System) utilizando las funcionalidades avanzadas de Figma, preparado para su posterior implementación en Angular + Tailwind CSS.
8. Valorar la importancia del handoff eficiente entre diseño y desarrollo, identificando los problemas comunes en este proceso y las prácticas que los previenen.

## Resultado de aprendizaje asociado

Esta unidad contribuye, como RA principal, al **RA 4** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 4.** Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE c) Se han creado diferentes tipos de menús cuya estructura y contenido siguen los estándares establecidos.
- CE d) Se han distribuido las acciones en menús, barras de herramientas, botones de comando, entre otros, siguiendo un criterio coherente.
- CE e) Se han distribuido adecuadamente los controles en la interfaz de usuario.
- CE f) Se ha utilizado el tipo de control más apropiado en cada caso.
- CE g) Se ha diseñado el aspecto de la interfaz de usuario (colores y fuentes entre otros) atendiendo a su legibilidad.

Como RA secundario, esta unidad se vincula al **RA 1** («Genera interfaces gráficos de usuario mediante editores visuales utilizando las funcionalidades del editor y adaptando el código generado»), en particular:

- CE a) Se han analizado las herramientas y librerías disponibles para la generación de interfaces gráficos.
- CE b) Se ha creado un interfaz gráfico utilizando las herramientas de un editor visual (Figma como entorno de diseño).

!!! note "Conocimientos previos"

    El alumnado debe poseer los siguientes conocimientos y habilidades antes de abordar esta unidad:

    - Comprensión sólida de los conceptos de UX y UI tratados en la Unidad 1, incluyendo la distinción entre ambas disciplinas y las fases del proceso de diseño.
    - Familiaridad con los fundamentos de HTML5 y CSS3: modelo de caja, selectores, propiedades de layout (display, position, flex), colores (hex, rgb, hsl), tipografía y espaciado. Esta base es esencial porque Figma utiliza conceptos análogos (Auto Layout = Flexbox, constraints = posicionamiento CSS, variables = custom properties).
    - Familiaridad con la nomenclatura básica de Tailwind CSS (colores, espaciado y sistema responsive; se trabaja en la Unidad 6). Figma y Tailwind comparten filosofía de sistema de diseño, y estableceremos equivalencias directas entre ambos.
    - Familiaridad con el entorno de desarrollo (Angular + Tailwind + Storybook + VS Code), que se configura a lo largo de las Unidades 9 y 10; aunque esta unidad se centre en Figma, los diseños que creemos serán implementados posteriormente en Angular + Tailwind. La Unidad 15 (del diseño a la implementación) cerrará el ciclo.
    - Cuenta de Figma (gratuita, plan Starter) creada y verificada. Figma ofrece el plan gratuito con todas las funcionalidades necesarias para esta unidad. Opcionalmente, el alumnado puede solicitar el plan educativo (Figma for Education) que incluye funcionalidades adicionales.

## Contenidos

**Bloque 1: Fundamentos de Figma**
- Qué es Figma: herramienta de diseño de interfaces basada en web, colaborativa en tiempo real, con soporte para diseño vectorial, prototipado interactivo, sistemas de diseño y modo desarrollador.
- Por qué Figma es el estándar de la industria: accesibilidad multiplataforma (funciona en navegador, no requiere macOS como Sketch), colaboración en tiempo real tipo Google Docs, gratuito para educación, único source of truth para diseño y desarrollo.
- Espacio de trabajo: toolbar (herramientas de creación y edición), panel izquierdo (capas, assets, páginas), canvas (área de trabajo infinita), panel derecho (propiedades de diseño, prototipado, inspección).
- Herramientas fundamentales: Move (V), Frame (F), Rectangle (R), Text (T), Pen (P), Hand (H), Comment (C). Atajos de teclado para productividad.
- Navegación por capas y páginas: jerarquía padre-hijo, agrupación (Ctrl+G), bloqueo, ocultación, renombrado semántico.
- Plugins: qué son, cómo instalarlos desde Figma Community, plugins esenciales para el flujo de trabajo (Tailwind CSS, Iconify, Unsplash, Stark, Content Reel).

**Bloque 2: Frames y elementos básicos**
- Concepto de Frame: contenedor fundamental de Figma, equivalente a un div en HTML o una pantalla/componente en diseño.
- Tamaños predefinidos de Frame: dispositivos (iPhone, Android, tablet, desktop presets), tamaños personalizados.
- Constraints: sistema de anclaje de elementos hijos respecto al frame padre (left, right, top, bottom, center, scale), equivalente al posicionamiento CSS (relative, absolute, fixed).
- Propiedades de rectángulo y formas: dimensiones (W, H), radio de esquina (corner radius), rotación, opacidad, relleno (fill), trazo (stroke), efectos (shadows: drop shadow, inner shadow; blur: layer blur, background blur).
- Texto en Figma: propiedades tipográficas (font family, weight, size, line height, letter spacing, paragraph spacing), alineación, color, estilos de texto.

**Bloque 3: Auto Layout (función estrella de Figma)**
- Qué es Auto Layout: sistema de layout dinámico que permite crear diseños flexibles que se adaptan al contenido. Es el equivalente directo de CSS Flexbox.
- Propiedades de Auto Layout:
  - Direction: horizontal (→ flex-row) o vertical (↓ flex-col).
  - Gap: espacio entre elementos hijos (equivalente a gap en CSS/Tailwind).
  - Padding: espacio interior en los cuatro lados (equivalente a padding en CSS).
  - Alignment: alineación de hijos en ambos ejes (equivalente a justify-content + align-items).
  - Resizing: hug contents (el frame se adapta al tamaño del contenido, equivalente a width: fit-content), fill container (el frame se expande para llenar el espacio disponible, equivalente a flex: 1), fixed (tamaño fijo).
- Auto Layout anidado: combinar frames con Auto Layout dentro de otros frames con Auto Layout para construir layouts complejos.
- Comparación directa Tabla Figma ↔ Tailwind CSS: mapear cada propiedad de Auto Layout a su clase Tailwind equivalente para que el alumnado entienda el puente entre diseño y código.
- Wrap: habilitar ajuste de línea en Auto Layout horizontal (equivalente a flex-wrap en CSS).

**Bloque 4: Variables en Figma**
- Concepto de variables: valores reutilizables y centralizados que pueden aplicarse a fills, strokes, effects, texto, dimensiones, etc. Equivalente a Design Tokens y a CSS Custom Properties (variables CSS).
- Tipos de variables: Color, Number (dimensiones, spacing, border-radius, opacidad), String (textos reutilizables), Boolean (toggles true/false).
- Colecciones: agrupación de variables por categoría (Colors, Typography, Spacing, Radius, Effects).
- Modos: el mismo nombre de variable puede tener diferentes valores según el modo (light/dark mode, high contrast mode, diferentes marcas de la misma empresa). Equivalente a aplicar diferentes valores de custom properties según `prefers-color-scheme`.
- Vinculación de variables: una variable puede referenciar a otra (ej: el color de texto por defecto referencia a la variable de color neutral-900).
- Organización profesional: jerarquía de variables (primitivas → semánticas → componentes), convenciones de nomenclatura (categoría/nombre-tono, ej: color/primary-500).

**Bloque 5: Componentes en Figma**
- Qué es un componente: elemento reutilizable con un "master" (componente principal) y múltiples "instances" (copias vinculadas). Equivalente a un componente de Angular o React.
- Creación de un componente: seleccionar elementos, Ctrl+Alt+K (Create component).
- Instancias: copias de un componente que mantienen vínculo con el master. Modificar el master actualiza todas las instancias.
- Propiedades de componente:
  - Propiedad de texto: permite editar texto en instancias sin desvincular.
  - Propiedad booleana (toggle): mostrar/ocultar capas dentro del componente (ej: mostrar u ocultar un icono en un botón).
  - Propiedad de intercambio de instancia (instance swap): reemplazar un componente hijo por otro del mismo conjunto (ej: cambiar el icono de un botón).
  - Propiedad de variante: seleccionar entre variantes de un componente set (ej: cambiar un botón de primary a secondary).
- Buenas prácticas en la creación de componentes: nomenclatura consistente, descripción (para documentación en el panel Assets), organización en subcarpetas.

**Bloque 6: Variantes (Component Sets)**
- Concepto de variantes: conjunto de estados o versiones de un mismo componente que se agrupan en un "component set". Equivalente a las variantes de un componente en Angular (prop input `variant: 'primary' | 'secondary' | 'outline'`).
- Creación de un component set: seleccionar dos o más componentes relacionados, "Combine as variants".
- Propiedades de variante: se definen automáticamente como propiedades del component set. Cada variante tendrá un valor para cada propiedad.
- Ejemplo completo: Button component set con propiedades:
  - Variant: Primary, Secondary, Outline, Ghost
  - Size: Small (sm), Medium (md), Large (lg)
  - State: Default, Hover, Focus, Disabled, Loading
  - Icon: None, Left, Right
- Esto genera 4 × 3 × 5 × 3 = 180 variantes teóricas. No es necesario diseñarlas todas manualmente (se pueden derivar con propiedades booleanas para estados como hover), pero el sistema lo permite.
- Organización visual del component set en el canvas de Figma para mantener la cordura con muchos componentes.

**Bloque 7: Design Tokens**
- Definición formal de Design Tokens: valores indivisibles que almacenan decisiones de diseño y pueden aplicarse consistentemente a través del sistema. Según la especificación W3C Design Tokens Community Group.
- Implementación de Design Tokens en Figma con variables: crear todas las variables necesarias (colores, tipografías, espaciados, bordes, sombras) como fuente de verdad única.
- Mapeo Figma → Código: correspondencia entre:
  - Variable de color en Figma → `--color-*` en `@theme` de Tailwind 4.
  - Variable de número (spacing) en Figma → `--spacing-*` en `@theme`.
  - Variable de número (font-size) en Figma → `--text-*` en `@theme`.
- Plugins de exportación de tokens: Design Tokens (plugin para exportar JSON), Tailwind CSS (plugin para generar configuración), Tokens Studio for Figma (plugin avanzado para gestionar tokens con soporte para múltiples plataformas de destino: CSS, SCSS, JS, Tailwind, Android, iOS).

**Bloque 8: Sistemas de diseño (Design Systems) en Figma**
- Qué es un sistema de diseño: colección de componentes reutilizables, guiados por estándares claros, que pueden ensamblarse para construir aplicaciones.
- Componentes del sistema de diseño en Figma:
  - Foundations (cimientos): colores, tipografía, espaciado, iconografía, border-radius, sombras, grid. Todo basado en variables.
  - Components (componentes): botones, inputs, selects, checkboxes, radios, toggles, cards, modals, tooltips, tabs, tables, avatars, badges, etc. Construidos con Auto Layout y organizados en component sets con variantes.
  - Patterns (patrones): combinaciones de componentes que resuelven necesidades comunes (header con navegación, tabla con filtros y paginación, formulario de búsqueda avanzada).
  - Pages (pantallas de ejemplo): layouts completos que muestran cómo se combinan los componentes en situaciones reales.
- Bibliotecas compartidas (Shared Libraries): publicar componentes y estilos como una librería de equipo, accesible desde cualquier archivo de Figma. Los cambios en la librería se propagan a todos los archivos que la usan (con aceptación explícita de actualizaciones para control de versiones).
- Analogía con el desarrollo: el sistema de diseño en Figma es el equivalente al sistema de diseño en código (componentes Angular + estilos Tailwind). El objetivo de las Unidades 4 y 15 es alinear ambos.

**Bloque 9: Plugins útiles para desarrolladores**
- Tailwind CSS: convierte selecciones de Figma a clases Tailwind (versión gratuita limitada, de pago completo). Alternativamente, usar el Dev Mode que genera CSS y traducir mentalmente.
- Iconify: búsqueda e inserción de iconos SVG de más de 150 sets (Material Design, Heroicons, Lucide, Phosphor, etc.) directamente en Figma.
- Unsplash: inserción de imágenes de stock gratuitas para rellenar diseños de forma realista.
- Content Reel: generación de contenido placeholder realista (nombres, direcciones, emails, avatares, textos).
- Stark: herramientas de accesibilidad (simulación de daltonismo, verificación de contraste WCAG, simulación de visión borrosa).
- Figma to Code (varios plugins): generación de código HTML/CSS/React/Angular desde diseños. Útiles como punto de partida, pero requieren revisión y ajuste manual (no son "mágicos").
- html.to.design: convierte cualquier página web en un diseño Figma editable (útil para analizar interfaces existentes).

**Bloque 10: Modo desarrollador (Dev Mode) y handoff**
- Activación y uso del Dev Mode: toggle en la barra superior (o atajo Shift+D).
- Información disponible en Dev Mode:
  - Medidas entre elementos seleccionados (distancia, dimensiones).
  - Código CSS generado automáticamente (con unidades, colores en hex, tipografía en px).
  - Variables de Figma con sus nombres.
  - Assets exportables (seleccionar capa → Export → formato y resolución).
  - Comparación de cambios entre versiones del diseño (diff visual).
- Configuración de la salida de código: Tailwind (si el plugin está instalado y configurado), CSS, SwiftUI, Compose.
- Plugins de VS Code para Figma: Figma for VS Code (incrustar diseños en el editor), Figma Embed.
- Handoff: proceso de transferencia del diseño al desarrollo:
  - Qué información necesita el desarrollador: medidas exactas, colores, tipografías, assets, comportamiento interactivo (estados: hover, focus, disabled, loading), flujo de navegación (prototipo).
  - Buenas prácticas del diseñador: nombrar capas semánticamente, agrupar lógicamente, limpiar capas ocultas, anotar decisiones de diseño, proporcionar specs.
  - Buenas prácticas del desarrollador: revisar el diseño completo antes de empezar a programar, preguntar dudas antes de asumir, verificar medidas y colores en Dev Mode, no adivinar.

**Bloque 11: Figma ↔ Tailwind ↔ Angular: el puente completo**
- Mapeo semántico: entender que lo que se hace en Figma tiene una traducción directa al código.
- Tabla de correspondencias:
  - Color Fill → `bg-{color}-{shade}` en Tailwind.
  - Text → componente `<p>`, `<h1>`-`<h6>` con clases `text-*`, `font-*`.
  - Auto Layout direction horizontal → `class="flex flex-row"`.
  - Auto Layout direction vertical → `class="flex flex-col"`.
  - Auto Layout gap → `class="gap-{size}"`.
  - Auto Layout padding → `class="p-{size}"`.
  - Corner radius → `class="rounded-{size}"`.
  - Drop shadow → `class="shadow-{size}"`.
  - Component (Figma) → Component (Angular standalone).
  - Variant property → `@Input() variant`.
  - Instance → Uso del componente en un template padre: `<app-button variant="primary">`.

## Desarrollo teórico

### 1. Introducción a Figma: por qué es el estándar

Figma irrumpió en 2016 y en menos de cinco años desplazó a herramientas establecidas como Sketch (que dominaba el mercado de diseño UI desde 2010) y Adobe XD (el intento de Adobe por competir). Este desplazamiento no fue casual: Figma resolvió problemas que las herramientas anteriores, por su arquitectura, no podían abordar.

El primero y más fundamental: **Figma es una aplicación web**. No requiere instalación de software nativo (aunque tiene aplicación de escritorio Electron), funciona en cualquier sistema operativo (Windows, macOS, Linux, ChromeOS), y los archivos se almacenan en la nube y están siempre sincronizados. Cualquier persona con un navegador puede abrir el mismo archivo, desde cualquier ordenador, sin preocuparse de versiones ni compatibilidad.

El segundo: **colaboración en tiempo real**. Múltiples personas pueden editar el mismo archivo simultáneamente, viendo los cursores de los demás en tiempo real, como Google Docs. Esto transforma las revisiones de diseño: en lugar de exportar PNGs, enviar por email, recibir feedback descontextualizado, implementar cambios, re-exportar, etc., el diseñador y el desarrollador pueden reunirse en el mismo archivo Figma, señalar elementos, hacer cambios en directo y validarlos instantáneamente.

El tercero: **modo desarrollador integrado**. Figma entiende que sus usuarios no son solo diseñadores. El Dev Mode proporciona a los desarrolladores exactamente lo que necesitan (medidas, colores, código CSS, assets exportables) sin las funcionalidades de diseño que les son irrelevantes. Esta integración ha acortado drásticamente la distancia entre diseño y desarrollo.

El cuarto: **comunidad y plugins**. Figma Community aloja miles de recursos gratuitos (plantillas, componentes, iconos, sistemas de diseño completos) y plugins que extienden la funcionalidad de la herramienta. Esto permite a equipos pequeños acceder a recursos de nivel profesional sin presupuesto.

Para los estudiantes de Desarrollo de Interfaces, Figma es la herramienta donde aprenderéis a pensar visualmente, a materializar ideas de interfaz y a comunicaros con diseñadores. Aunque vuestro perfil profesional es más técnico (Angular, TypeScript, Tailwind), la capacidad de entender, inspeccionar e incluso crear diseños en Figma os hará profesionales mucho más completos y valorados.

### 2. El espacio de trabajo de Figma

Al abrir Figma por primera vez, la interfaz puede resultar abrumadora. Vamos a descomponerla en sus partes principales, estableciendo analogías con herramientas que ya conocéis (VS Code, explorador de archivos, etc.).

**La toolbar (barra de herramientas superior)**

Es el equivalente a la barra de herramientas de VS Code, pero en diseño. Contiene:

- **Herramientas de creación:** Frame (F), Rectangle (R), Line (L), Arrow (Shift+L), Ellipse (O), Polygon, Star, Place image (Ctrl+Shift+K), Pen (P) para dibujo vectorial, Pencil (Shift+P) para dibujo libre, Text (T).

- **Herramientas de manipulación:** Move (V) para seleccionar y mover elementos, Scale (K) para redimensionar proporcionalmente, Slice (S) para definir áreas de exportación.

- **Herramientas de navegación:** Hand (H) para desplazarse por el canvas, Comment (C) para dejar comentarios (estilo Google Docs) en puntos específicos del diseño.

- **Controles contextuales:** Según el elemento seleccionado, la toolbar muestra acciones específicas (Create component, Add auto layout, Mask, Boolean operations, etc.).

- **Toggle Dev Mode:** Interruptor para cambiar entre el modo Diseño (completo, para diseñadores) y el modo Desarrollador (información técnica para implementación).

**El panel izquierdo (Layers, Assets, Pages)**

Es el equivalente al explorador de archivos de VS Code + la paleta de componentes de Angular:

- **Pestaña Layers (Capas):** Muestra la jerarquía de elementos en el canvas, del más externo al más interno. Cada frame, grupo y elemento es una capa. Pueden renombrarse (doble clic), reordenarse (drag & drop), agruparse (Ctrl+G), bloquearse (candado) y ocultarse (ojo). Una nomenclatura semántica y organizada es fundamental para que el desarrollador entienda el diseño (nada de "Rectangle 47" o "Frame 12").

- **Pestaña Assets (Recursos):** Muestra los componentes locales (creados en este archivo) y los componentes de librerías externas habilitadas. Organizados en carpetas y subcarpetas. Es el equivalente al `shared/ui/` de Angular y a la galería de Storybook. Arrastrar un componente desde Assets al canvas crea una instancia.

- **Pestaña Pages (Páginas):** Cada archivo Figma puede contener múltiples páginas (como pestañas de un navegador). Una organización típica: 🗂️ Cover (portada del proyecto), 🎨 Design Tokens (variables y fundamentos), 🧩 Components (todos los componentes del sistema de diseño), 📱 Screens (pantallas de la aplicación, prototipo).

**El canvas (área de trabajo)**

Es el espacio infinito donde se crean los diseños. No tiene bordes (como un canvas de HTML5 o un mapa mental infinito). La navegación se realiza con scroll (zoom) y arrastrando con la rueda del ratón pulsada (pan). Los frames se organizan en el canvas con espacio entre ellos para mantener la claridad visual.

**El panel derecho (propiedades)**

El panel más importante para el trabajo cotidiano. Dividido en tres secciones principales según el modo:

En **Modo Diseño**:
- **Design:** Propiedades del elemento seleccionado. Se subdivide en:
  - *Alignment & Distribution*: alinear y distribuir elementos seleccionados (equivalente a justify-content + align-items en Flexbox).
  - *Position & Dimensions*: coordenadas X/Y, ancho/alto, rotación, radio de esquina, constraints.
  - *Auto Layout*: dirección, gap, padding, alignment, resizing, wrap.
  - *Fill & Stroke*: colores de relleno (sólido, gradiente, imagen) y trazo (borde).
  - *Effects*: sombras (drop, inner), desenfoques (layer, background), texturas.
  - *Export*: configuración de exportación para el elemento seleccionado (formato, resolución, sufijo).
- **Prototype:** Configuración de interacciones para prototipado (al hacer clic en elemento A, navegar al frame B, con animación de transición).
- **Inspect (en versiones antiguas, ahora Dev Mode):** Información técnica para desarrollo. En la versión actual, esta información se accede desde el Dev Mode.

En **Modo Desarrollador (Dev Mode)**:
- Información optimizada para implementación: medidas respecto al frame padre, código CSS/Tailwind, nombres de variables, assets listos para descargar, comparación de cambios.

### 3. Auto Layout: Flexbox en Figma

**Auto Layout** es, sin exageración, la funcionalidad más importante de Figma para un desarrollador de interfaces. Comprender Auto Layout es comprender cómo los diseñadores piensan en layouts flexibles, y establecer un puente mental directo entre el diseño visual y el código CSS (Flexbox) o las clases de Tailwind.

**Concepto fundamental**

Auto Layout es un sistema de layout dinámico aplicado a un frame. Cuando activas Auto Layout en un frame (Shift+A), éste deja de ser un contenedor estático y se comporta como un contenedor flex de CSS: sus hijos se organizan automáticamente según la dirección y las reglas de espaciado y alineación definidas. Si cambias el contenido (añades, eliminas o modificas hijos), el contenedor se redimensiona automáticamente según las reglas de resizing.

**Propiedades y equivalencias con Tailwind/CSS**

| Propiedad en Figma | Descripción | Equivalencia CSS | Clase Tailwind |
|---|---|---|---|
| Direction: Horizontal | Hijos en fila | `flex-direction: row` | `flex flex-row` (por defecto) |
| Direction: Vertical | Hijos en columna | `flex-direction: column` | `flex flex-col` |
| Gap (horizontal y vertical) | Espacio entre hijos | `gap: {valor}` | `gap-{n}` |
| Padding (top, right, bottom, left) | Espacio interior | `padding: {valor}` | `p-{n}`, `px-{n}`, `py-{n}`, `pt-{n}`, etc. |
| Alignment: Horizontal | Alineación en eje X | `justify-content` | `justify-start`, `justify-center`, `justify-end`, `justify-between` |
| Alignment: Vertical | Alineación en eje Y | `align-items` | `items-start`, `items-center`, `items-end`, `items-stretch` |
| Hug contents | Tamaño se adapta al contenido | `width: fit-content` / `height: fit-content` | `w-fit`, `h-fit` (Tailwind 3.2+) |
| Fill container | Se expande hasta llenar contenedor padre | `flex: 1` | `flex-1` |
| Fixed | Tamaño fijo en píxeles | `width: Npx` / `height: Npx` | `w-[Npx]`, `h-[Npx]` |
| Wrap | Ajuste de línea | `flex-wrap: wrap` | `flex-wrap` |

**Auto Layout anidado**

La verdadera potencia aparece cuando anidas frames con Auto Layout. Por ejemplo, para construir una Card de una red social:

1. Frame exterior (Card) con Auto Layout vertical:
   - Padding: 16px todos lados.
   - Gap: 12px.

2. Frame hijo 1 (Header) con Auto Layout horizontal:
   - Gap: 8px.
   - Contiene: Avatar (frame fixed 40x40, corner radius 100 = círculo) + Frame vertical (Name + Timestamp).
   - Alignment: center (para alinear avatar y texto verticalmente).

3. Frame hijo 2 (Content) con Auto Layout vertical:
   - Contiene: Texto del post (fill container, multilínea) + Imagen (fixed width: fill container, height: fija).

4. Frame hijo 3 (Actions) con Auto Layout horizontal:
   - Gap: 24px.
   - Contiene: Like button (icono + texto), Comment button (icono + texto), Share button (icono).
   - Alignment: space-between (para distribuir acciones).

Cada nivel de anidamiento de Auto Layout en Figma se traduce en un `<div>` con clases flex en Tailwind cuando implementemos el componente en Angular. Este es el patrón mental que debéis desarrollar: **ver Auto Layout en Figma y visualizar inmediatamente el HTML + Tailwind correspondiente**.

### 4. Variables en Figma: Design Tokens nativos

Las variables de Figma, introducidas en 2023, representan la adopción formal de los **Design Tokens** dentro de la herramienta de diseño. Antes de las variables, los diseñadores usaban "Styles" (estilos de color, texto, efectos) que eran reutilizables pero tenían limitaciones importantes: no soportaban modos (light/dark), no podían referenciarse entre sí, y no se podían exportar fácilmente a código.

**Tipos de variables**

1. **Color:** El más común. Define valores de color que pueden usarse como relleno (fill), trazo (stroke) o efecto (sombra). Ejemplos: `color-primary-500: #3B82F6`, `color-neutral-100: #F1F5F9`.

2. **Number:** Valores numéricos que pueden usarse para dimensiones (width, height), espaciado (padding, gap), border-radius, corner radius, opacidad u otros valores numéricos. Ejemplos: `spacing-sm: 8`, `radius-md: 12`, `fontSize-lg: 18`.

3. **String:** Cadenas de texto reutilizables. Útil para nombres de fuentes (`fontFamily-sans: 'Inter'`) o cualquier metadata textual.

4. **Boolean:** Valores verdadero/falso. Útil para propiedades de componentes (mostrar icono sí/no, mostrar borde sí/no).

**Colecciones**

Las variables se organizan en **colecciones** (collections). Una colección agrupa variables relacionadas y, crucialmente, comparte los mismos modos. Una organización profesional típica:

- **Colección "Colors":** Todas las variables de color. Modos: Light, Dark, High Contrast.
- **Colección "Spacing":** Todas las variables de espaciado. Modos: Desktop, Mobile (móvil puede tener espaciados más compactos).
- **Colección "Typography":** Variables de familia tipográfica, tamaños, pesos. Modos: Desktop, Mobile.
- **Colección "Radius":** Variables de border-radius. Modos: Default.
- **Colección "Effects":** Variables de sombras y desenfoques. Modos: Light, Dark (las sombras se comportan diferente en modo oscuro).

**Modos**

Los **modos** son la clave para temas (light/dark) y adaptaciones multiplataforma. Una variable `color/bg-default` puede tener valor `#FFFFFF` en modo Light y `#1E293B` en modo Dark. Al cambiar el modo del frame, todos los elementos que usen variables se actualizan automáticamente. Este es exactamente el mismo concepto que las variables CSS con `prefers-color-scheme` o la estrategia `class` de Tailwind con el prefijo `dark:`.

**Vinculación entre variables**

Una variable puede hacer referencia a otra variable (aliasing). Esto permite crear capas de abstracción:

- Nivel 1 - Primitivas: `slate-500: #64748B`
- Nivel 2 - Semánticas: `color-text-secondary` hace referencia a `slate-500`
- Nivel 3 - Componentes: El color de texto secundario de un componente `Input` hace referencia a `color-text-secondary`

Si en el futuro se decide cambiar el gris del texto secundario, solo hay que modificar la variable semántica (o la primitiva que ésta referencia), y todos los componentes se actualizan automáticamente. Esto es exactamente lo mismo que haremos en Tailwind con `@theme`, donde definimos `--color-text-secondary: var(--color-slate-500)`.

### 5. Componentes en Figma: del diseño al código

Los componentes en Figma son el equivalente a los componentes en Angular/React/Vue: elementos reutilizables y autocontenidos con propiedades configurables y variantes predefinidas. Dominar los componentes de Figma os permitirá entender cómo piensan los diseñadores, y os facilitará la implementación posterior (cada componente de Figma se convertirá en un componente de Angular).

**Creación de un componente**

1. Diseña el elemento con todas sus capas (textos, rectángulos, iconos, Auto Layouts).
2. Selecciona todo.
3. Pulsa Ctrl+Alt+K (Windows/Linux) o Cmd+Option+K (macOS), o haz clic en "Create component" en la toolbar.
4. El elemento se convierte en un componente (**master**), indicado por un icono de rombo púrpura en el panel de capas.
5. Nómbralo adecuadamente (ej: `Button / Primary / Default`).

**Instancias**

Cuando arrastras un componente desde el panel Assets al canvas, creas una **instancia** (copia vinculada al master). Las instancias tienen un icono de rombo hueco. Puedes modificar ciertas propiedades de la instancia (si el componente las ha definido como propiedades), pero no su estructura interna (a menos que hagas "Detach instance" que la rompe la vinculación, algo que debería evitarse en el flujo normal).

**Propiedades de componente**

Las propiedades permiten configurar las instancias sin romper el vínculo con el master:

- **Propiedad de texto:** Define capas de texto como editables en las instancias. Por ejemplo, un botón con texto "Label" editable. El diseñador que usa la instancia puede cambiar "Label" por "Guardar cambios" sin desvincular.

- **Propiedad booleana (toggle):** Muestra u oculta capas. Ejemplo: un botón con un icono opcional. La instancia puede mostrar u ocultar el icono mediante un toggle en el panel de propiedades.

- **Propiedad de intercambio de instancia (instance swap):** Permite reemplazar un componente hijo por otro del mismo conjunto. Ejemplo: un botón con icono permite intercambiar el icono (de "check" a "arrow-right" a "plus") siempre que todos los iconos sean parte del mismo component set.

- **Propiedad de variante:** Si el componente pertenece a un component set (ver siguiente sección), la instancia expone la selección de variante.

**Buenas prácticas en componentes Figma**

1. **Nombre semántico y jerárquico:** Usa la barra `/` para crear jerarquía: `Button / Primary / Default`, `Input / Text / Default`, `Card / Vertical / With Image`. Esto se refleja en el panel Assets como carpetas anidadas.

2. **Añade descripción:** En el panel de propiedades del componente master, hay un campo "Description". Documenta qué hace el componente, cuándo usarlo y cualquier consideración relevante. Esta descripción es visible para cualquiera que seleccione una instancia.

3. **Auto Layout desde el principio:** Todos los componentes deben usar Auto Layout para que las instancias se redimensionen correctamente al cambiar contenido.

4. **Diseña con contenido realista:** No uses "Lorem ipsum" o textos placeholder irreales. Usa contenido que refleje casos de uso reales (nombres reales, emails realistas, textos de longitud típica). Esto evita sorpresas cuando el componente se use con contenido real (textos que se desbordan, nombres demasiado largos, etc.).

### 6. Variantes (Component Sets): todos los estados de un componente

Un **component set** es una agrupación de componentes relacionados que comparten las mismas propiedades pero con diferentes valores. Es la forma que tiene Figma de modelar lo que en código llamaríamos "variantes" o "estados" de un componente.

**Creación de un component set**

1. Crea varias variantes de un mismo componente (por ejemplo: Button Primary, Button Secondary, Button Outline).
2. Selecciona todas ellas.
3. Haz clic en "Combine as variants" en la toolbar (o Ctrl+Alt+K sobre la selección múltiple).
4. Figma las agrupa en un component set (indicado por un recuadro púrpura). Cada miembro del set es ahora una variante.

**Propiedades de variante**

Figma crea automáticamente una propiedad de variante basada en las diferencias entre los componentes originales. Si los componentes se llamaban `Button/Primary`, `Button/Secondary`, `Button/Outline`, la propiedad se llamará "Property 1" (puedes renombrarla a "Variant") y tendrá los valores Primary, Secondary, Outline.

Puedes añadir múltiples propiedades de variante. Por ejemplo, para un Button con Variant × Size × State, crearías las combinaciones necesarias y las nombrarías adecuadamente. Figma detecta los patrones y crea las propiedades correspondientes.

**Ejemplo completo: Component Set de Input**

Propiedades:
- **Variant:** Default (borde gris), Filled (fondo gris claro), Outline (sin fondo, borde azul).
- **Size:** Small (height: 32px), Medium (height: 40px), Large (height: 48px).
- **State:** Default, Hover (borde azul), Focus (borde azul + ring), Disabled (opacity 50%, cursor not-allowed), Error (borde rojo, texto de error debajo), Success (borde verde, check icon).
- **Element:** None, Leading Icon (icono a la izquierda), Trailing Icon (icono a la derecha), Both Icons.
- **Type:** Text, Password, Email, Number, Textarea (este es problemático porque cambia la estructura; a veces es mejor separarlo como componente diferente).

Organizar tantas variantes visualmente en el canvas puede ser complejo. Figma permite reorganizar las variantes en una cuadrícula (arrastrando los divisores de propiedades). Para un set con propiedades A y B, se organiza como una cuadrícula 2D: filas = valores de A, columnas = valores de B.

**Traducción a Angular**

Cada propiedad de variante en Figma se convertirá en un `@Input()` en Angular. Por ejemplo:

```typescript
@Component({
  selector: 'app-input',
  standalone: true,
})
export class InputComponent {
  readonly variant = input<'default' | 'filled' | 'outline'>('default');
  readonly size = input<'sm' | 'md' | 'lg'>('md');
  readonly state = input<'default' | 'error' | 'success'>('default');
  readonly leadingIcon = input<string | undefined>(undefined);
  readonly trailingIcon = input<string | undefined>(undefined);
  readonly type = input<'text' | 'password' | 'email' | 'number'>('text');
  readonly disabled = input(false);
}
```

Y las variantes visuales de Figma (colores, bordes, tamaños) se traducirán a clases condicionales de Tailwind en el template, de forma similar a como hicimos con el componente Button en la Unidad 7.

### 7. Design Tokens: concretando los átomos del diseño

Los Design Tokens son la capa más fundamental de un sistema de diseño: los valores indivisibles que almacenan todas las decisiones de diseño. Colores, tipografías, espaciados, bordes, sombras... todo se define como tokens y se consume consistentemente a través de componentes y pantallas.

**Jerarquía de tokens**

La especificación W3C Design Tokens Community Group (aún en desarrollo) propone tres niveles de tokens:

1. **Tokens primitivos (global tokens):** Los valores base, sin significado semántico. Ejemplo: `blue-500: #3B82F6`. Estos tokens definen "qué colores están disponibles en la paleta" pero no "dónde deben usarse".

2. **Tokens semánticos (alias tokens):** Apuntan a tokens primitivos pero añaden significado. Ejemplo: `color-action-primary-default: {blue-500}`. Definen "el color de la acción primaria", no "el azul concreto". Si mañana la marca cambia el azul por un verde, se modifica el token semántico y todo el sistema se actualiza.

3. **Tokens de componente:** Apuntan a tokens semánticos para contextos específicos. Ejemplo: `button-primary-background-default: {color-action-primary-default}`. Añaden una capa extra de abstracción que permite variaciones por componente (el botón primary usa el color action-primary, pero el enlace primary podría usar un color diferente).

**Implementación en Figma con variables**

En Figma, esta jerarquía se implementa con variables y vinculación:

- **Colección "Primitives":** Todas las variables de color base (slate-50 a slate-950, blue-50 a blue-950, green-50 a green-950, red-50 a red-950, etc.). Sin modos (o modos light/dark que cambian los valores hex).

- **Colección "Semantic":** Variables como `color-bg-primary`, `color-bg-secondary`, `color-text-primary`, `color-text-secondary`, `color-border-default`, `color-action-primary`, `color-status-success`, etc. Cada una referencia a una variable de la colección Primitives. Esta colección sí tiene modos light/dark: en light, `color-bg-primary` apunta a `white`; en dark, apunta a `slate-900`.

- **Colección "Component":** (Opcional para sistemas grandes) Variables como `button-primary-bg-default`, `button-primary-bg-hover`, `input-border-default`, etc. Referencian a la colección Semantic.

**Del token de Figma al `@theme` de Tailwind**

La traducción es directa porque Tailwind 4 soporta la definición de tokens personalizados:

```css
/* styles.css de Angular con Tailwind 4 */
@import "tailwindcss";

@theme {
  /* Tokens primitivos (paleta de colores) */
  --color-slate-50: #f8fafc;
  --color-slate-100: #f1f5f9;
  /* ... resto de tonos */
  --color-slate-900: #0f172a;

  --color-blue-500: #3b82f6;
  --color-blue-600: #2563eb;
  --color-blue-700: #1d4ed8;

  /* Tokens semánticos (significado funcional) */
  --color-primary: var(--color-blue-600);
  --color-primary-hover: var(--color-blue-700);
  --color-primary-light: var(--color-blue-500);
  --color-bg: var(--color-white);
  --color-bg-secondary: var(--color-slate-50);
  --color-text: var(--color-slate-900);
  --color-text-secondary: var(--color-slate-500);
  --color-border: var(--color-slate-200);

  /* Tokens de espaciado */
  --spacing-section: 2rem;
  --spacing-component: 1rem;
  --spacing-element: 0.5rem;

  /* Tokens de tipografía */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;

  /* Tokens de border-radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
  --radius-full: 9999px;
}
```

Una vez definidos, se usan en los componentes con las clases Tailwind personalizadas: `bg-primary`, `text-text-secondary`, `rounded-lg`, `gap-element`, `text-xl`. Esto garantiza que cualquier cambio en los tokens se propaga automáticamente a todos los componentes que los utilizan. Un cambio de diseño que en CSS tradicional requeriría buscar y reemplazar en docenas de archivos, aquí se resuelve modificando una línea en el `@theme`.

### 8. Sistemas de diseño en Figma: el blueprint de la interfaz

Un sistema de diseño completo en Figma es la culminación de todo lo aprendido: variables (design tokens), componentes con variantes, Auto Layouts anidados, páginas organizadas y librerías compartidas. Vamos a definir la estructura de un sistema de diseño profesional adaptado a proyectos de Desarrollo de Interfaces.

**Estructura de páginas en el archivo Figma del sistema de diseño**

```text
📁 Design System - [Nombre del proyecto]
├── 📄 Cover                    (portada, nombre, versión, fecha, autores)
├── 📄 Foundations               (cimientos del sistema)
│   ├── 🎨 Colors               (paletas con variables)
│   ├── 🔤 Typography           (escala tipográfica con variables)
│   ├── 📏 Spacing              (escala de espaciado con variables)
│   ├── 🔲 Radius & Shadows     (border-radius y sombras con variables)
│   └── 🖼️ Iconography          (set de iconos, grid de iconos)
├── 📄 Components                (todos los componentes del sistema)
│   ├── 🔘 Buttons              (component set con variantes)
│   ├── ✏️ Inputs               (component set con variantes)
│   ├── ☑️ Checkboxes & Radios  (component set con variantes)
│   ├── 🔘 Toggles              (component set)
│   ├── ⬇️ Selects & Dropdowns  (component set)
│   ├── 🃏 Cards                (component set: horizontal, vertical, con imagen,
│   │                            sin imagen, actionable, non-actionable)
│   ├── 🧭 Navigation           (navbar, sidebar, tabs, breadcrumbs)
│   ├── 📊 Data Display         (tables, data grids, lists, avatars, badges,
│   │                            chips, tooltips)
│   ├── 🪟 Overlays             (modals, dialogs, drawers, popovers)
│   └── 📄 Feedback             (alerts, toasts, progress bars, skeletons,
│                                empty states)
├── 📄 Patterns                  (combinaciones frecuentes de componentes)
│   ├── 🔍 Search & Filter      (barra de búsqueda + filtros + resultados)
│   ├── 📝 Forms                (formularios complejos con validación)
│   ├── 📊 Dashboard Widgets    (widgets con gráficos, KPIs, tablas)
│   └── 📧 Inbox / Feed         (listados con búsqueda, filtros, paginación)
├── 📄 Screens                   (pantallas completas de la aplicación)
│   ├── 🔐 Auth                 (login, registro, recuperación, verificación)
│   ├── 🏠 Dashboard            (dashboard principal)
│   ├── 📋 List + Detail        (pantalla de listado + detalle)
│   └── ⚙️ Settings             (pantalla de configuración)
└── 📄 Prototype                 (prototipo interactivo conectando pantallas)
```

Esta estructura no es dogmática; cada equipo la adapta a sus necesidades. Pero proporciona una base sólida y profesional que comunica profesionalidad y rigor, tanto al equipo de diseño como al de desarrollo.

**Bibliotecas compartidas (Shared Libraries)**

En equipos con múltiples proyectos, los componentes y estilos se publican como una librería compartida. Cualquier archivo Figma puede "suscribirse" a esa librería, obteniendo acceso a todos sus componentes y estilos. Cuando el equipo de diseño central actualiza un componente en la librería, todos los archivos que la usan reciben una notificación de actualización disponible. El diseñador de cada proyecto puede aceptar la actualización (manteniendo sus archivos sincronizados) o posponerla.

Esto resuelve el clásico problema de "tenemos componentes inconsistentes en diferentes partes del producto". En código, el equivalente es publicar una librería npm con los componentes Angular y que cada aplicación la importe. De hecho, el sistema de diseño profesional completo une Figma (librerías compartidas de diseño), Angular (librería npm de componentes), Tailwind (tema compartido) y Storybook (catálogo vivo de componentes implementados) en un ecosistema coherente.

### 9. Plugins para el flujo de trabajo diseño-desarrollo

Los plugins son extensiones que añaden funcionalidad a Figma. Se instalan desde Figma Community (accesible desde el menú principal → Plugins → Browse plugins). Los más relevantes para desarrolladores de interfaces son:

**Tailwind CSS (plugin de Figma):** Convierte elementos seleccionados a clases Tailwind. Seleccionas un botón, ejecutas el plugin, y genera algo como `class="bg-blue-500 text-white px-4 py-2 rounded-lg"`. La versión gratuita tiene limitaciones; la versión de pago es más completa. Alternativa: usar el Dev Mode que genera CSS y traducir manualmente (buen ejercicio para aprender las equivalencias).

**Iconify:** Accede a más de 150 sets de iconos (Material Design, Heroicons, Lucide, Phosphor, Tabler, Font Awesome, etc.) y los inserta como SVG vectoriales en Figma. Buscas "search", eliges el estilo, y se inserta en tu diseño. En desarrollo, usarás la versión web/React/Angular de Iconify o directamente Heroicons/Lucide.

**Stark:** Herramientas de accesibilidad integradas en Figma:
- Contraste: selecciona dos elementos (texto y fondo) y verifica si cumplen WCAG AA (ratio >= 4.5) o AAA (ratio >= 7).
- Daltonismo: simula cómo ve el diseño una persona con deuteranopia, protanopia, tritanopia.
- Visión borrosa: simula diferentes niveles de agudeza visual.
- Recomendaciones: sugiere colores alternativos que sí cumplen contraste.

**Content Reel:** Genera contenido placeholder realista para poblar tus diseños: nombres de persona, emails, direcciones, números de teléfono, avatares, textos. Mucho más profesional que "Lorem ipsum" o "John Doe".

**Unsplash:** Inserta imágenes de stock gratuitas y de alta calidad directamente en Figma. Útil para dar realismo a tarjetas de producto, avatares de usuario, imágenes de fondo, etc.

**Design Tokens (plugin):** Exporta todas las variables de Figma (o los estilos, en su defecto) a un archivo JSON estructurado. Este JSON puede ser utilizado por herramientas como Style Dictionary (de Amazon) para generar archivos de tokens en múltiples formatos (CSS, SCSS, JS, Android XML, iOS Swift, etc.). Es el puente automatizado entre las variables de Figma y el código.

**Tokens Studio for Figma (plugin avanzado):** Gestiona de forma integral los design tokens: múltiples sets de tokens (global, semantic, component), modos (themes), integración con GitHub (versionado de tokens como archivos JSON), exportación a múltiples plataformas (CSS, Tailwind, SCSS, JS, Android, iOS). Es utilizado en sistemas de diseño grandes y profesionales.

### 10. Dev Mode y Handoff: entregar el diseño a desarrollo

El momento del handoff (entrega del diseño al desarrollo) es crítico. Una mala comunicación en este punto genera malentendidos, implementaciones incorrectas, retrabajo, frustración en ambos equipos y, en última instancia, un producto que no coincide con la visión de diseño.

**Figma Dev Mode**

Accesible como toggle en la barra superior (o Shift+D), transforma la interfaz de Figma para mostrar solo la información relevante para implementación:

- **Medidas:** Al seleccionar un elemento, Dev Mode muestra sus dimensiones (width × height) y las distancias a los bordes del frame padre o a otros elementos. Pasar el cursor entre elementos muestra la distancia entre ellos.

- **Código sugerido:** Basado en tu configuración de lenguaje (CSS, Tailwind, SwiftUI, Compose, etc.), Figma genera fragmentos de código. Para CSS, muestra las propiedades relevantes. Para Tailwind, las clases necesarias. No es perfecto pero acelera significativamente.

- **Variables:** Muestra los nombres de las variables utilizadas y sus valores actuales en el modo activo.

- **Assets:** Panel que lista todos los elementos exportables en la selección actual. Permite descargar en SVG, PNG, JPG, PDF con diferentes resoluciones (@1x, @2x, @3x).

- **Comparación de versiones:** Si un compañero modificó el diseño, Dev Mode resalta qué ha cambiado (nuevos elementos, modificados, eliminados). El desarrollador puede ver exactamente qué debe actualizar en el código.

- **Plugins de sección:** El diseñador puede añadir plugins informativos en secciones específicas del diseño (anotaciones sobre comportamiento, enlaces a documentación, especificaciones de API). Es un "Post-it digital" incrustado en el diseño.

**Handoff: mejores prácticas**

**Responsabilidades del diseñador:**

1. Nombrar capas semánticamente. "Rectangle 47" no comunica nada; "ButtonBackground" sí.
2. Eliminar capas ocultas antes del handoff. Las capas ocultas confunden al desarrollador (¿esto se usa o no?).
3. Proporcionar todas las variantes y estados. El desarrollador necesita ver el componente en default, hover, focus, disabled, error, loading. Si no están en Figma, el desarrollador adivinará (y probablemente se equivocará).
4. Añadir anotaciones sobre comportamiento interactivo: "Este tooltip aparece al hacer hover después de 300ms", "Esta tabla ordena al hacer clic en el header", "El modal se cierra con Escape o clic fuera".
5. Crear un prototipo navegable que conecte las pantallas principales, para que el desarrollador entienda el flujo de la aplicación.
6. Mantener actualizado el diseño. Si se toma una decisión de diseño en una conversación de Slack, debe reflejarse en Figma. Figma es la fuente de verdad única; si no está en Figma, no existe.

**Responsabilidades del desarrollador:**

1. Revisar el diseño completo ANTES de empezar a programar. Identificar dudas, inconsistencias o elementos faltantes y comunicarlos al diseñador.
2. Preguntar, no asumir. "No vi el estado de error del formulario, ¿cómo debe verse?" es mejor que implementar algo inventado.
3. Inspeccionar, no adivinar. "A ojo, ese padding parece de 16px" → No. Usa Dev Mode, mide exactamente.
4. Informar de limitaciones técnicas. Si un efecto de diseño es extremadamente costoso en rendimiento, comunícalo. Propón alternativas. El diseñador no siempre conoce las implicaciones técnicas de sus decisiones.
5. Mantener Storybook sincronizado con Figma. Cuando implementes un componente, sus stories deben reflejar fielmente las variantes diseñadas en Figma. Si el diseñador puede validar el componente en Storybook comparándolo con el diseño en Figma, el ciclo de feedback se cierra de forma eficiente.

## Ejemplos guiados

### Ejemplo guiado 1: Diseñar un botón con todas sus variantes

**Objetivo:** Crear un component set completo de Button en Figma utilizando Auto Layout, variables de color y propiedades de componente. Este es el "Hola Mundo" del diseño de componentes y sienta las bases para todo lo demás.

**Duración estimada:** 50 minutos (guiado paso a paso, el alumnado sigue en sus equipos).

**Desarrollo paso a paso:**

**Paso 1 - Configurar las variables de color (si no están creadas):**
1. Abrir el panel de Variables (o el panel Local variables en el lateral derecho, según la versión de Figma).
2. Crear colección "Primitives" con modos "Light".
3. Añadir variables: `blue-500 (#3B82F6)`, `blue-600 (#2563EB)`, `blue-700 (#1D4ED8)`, `white (#FFFFFF)`, `slate-200 (#E2E8F0)`, `slate-400 (#94A3B8)`, `transparent`.

**Paso 2 - Diseñar la variante Primary / Default:**
1. Crear un frame (F) de dimensiones arbitrarias (luego se ajustará).
2. Añadir Auto Layout (Shift+A): horizontal, gap 8px, padding 16px top/bottom, 20px left/right, alineación center.
3. Fill: usar variable `blue-600`. Stroke: none.
4. Añadir capa de texto (T): "Button", font Inter, weight Semibold, size 14px (equivale a `text-sm`), line height 20px, fill white.
5. Corner radius: 8px (`rounded-lg`).
6. Renombrar el frame a "Button / Primary / Default".

**Paso 3 - Crear variante Secondary / Default:**
1. Duplicar (Ctrl+D) el frame Primary.
2. Cambiar fill a `slate-200` y texto a `slate-900` (o `blue-600` según preferencia de diseño).
3. Renombrar a "Button / Secondary / Default".

**Paso 4 - Crear variante Outline / Default:**
1. Duplicar Primary.
2. Quitar fill. Añadir stroke: 1.5px, color `blue-600`. Texto: `blue-600`.
3. Renombrar a "Button / Outline / Default".

**Paso 5 - Crear variante Ghost / Default:**
1. Duplicar Primary.
2. Fill: `transparent`. Texto: `blue-600`. Stroke none.
3. Renombrar a "Button / Ghost / Default".

**Paso 6 - Crear variantes de hover para cada una:**
Para cada variante, duplicar y modificar el estado hover:
- Primary Hover: fill `blue-700`.
- Secondary Hover: fill `slate-400`.
- Outline Hover: fill `blue-600`, texto `white`.
- Ghost Hover: fill `blue-600` con opacidad 10% (o variable específica).

**Paso 7 - Crear variantes de tamaño:**
Duplicar cada variante Default y ajustar padding:
- Small (sm): padding 8px top/bottom, 12px left/right, texto 12px.
- Medium (md): padding 12px top/bottom, 16px left/right, texto 14px (este es el que ya tenemos, renombrar para claridad).
- Large (lg): padding 16px top/bottom, 24px left/right, texto 16px.

Nombrar en consecuencia: `Button / Primary / Small / Default`, `Button / Primary / Large / Default`, etc.

**Paso 8 - Crear variantes con icono:**
Duplicar algunas variantes Default, añadir un icono (Insert → Iconify → search icon "arrow-right"), posicionarlo a la izquierda del texto mediante Auto Layout. Añadir propiedad booleana "Has Left Icon" o crear como variante adicional.

**Paso 9 - Crear variante Disabled y Loading:**
- Disabled: opacity 50%, fill `slate-200`, texto `slate-400`.
- Loading: añadir un spinner SVG junto al texto "Loading...". (Puede insertarse desde Iconify → "spinner").

**Paso 10 - Combinar en Component Set:**
1. Seleccionar TODAS las variantes creadas.
2. Click derecho → "Combine as variants" (o desde la toolbar).
3. Figma crea automáticamente las propiedades de variante. Renombrar las propiedades: "Variant", "Size", "State", "Icon".
4. Organizar la cuadrícula de variantes arrastrando los divisores de propiedad.

**Resultado:** Un component set profesional con 4 variantes × 3 tamaños × 5 estados × 2 configuraciones de icono = 120 combinaciones, listo para ser usado en cualquier diseño y, posteriormente, implementado como componente Angular.

### Ejemplo guiado 2: Crear un sistema de colores y tipografía con variables

**Objetivo:** Crear las variables de diseño fundamentales (colores y tipografía) que servirán como base para todos los componentes del sistema de diseño.

**Duración:** 30 minutos.

**Desarrollo paso a paso:**

**Parte A - Sistema de colores:**

1. Crear colección "Primitives/Colors" con modos: Light, Dark.

2. Rellenar la colección con la paleta Slate (escala de grises/neutros) y la paleta Blue (color primario):

| Variable | Light | Dark |
|---|---|---|
| `slate-50` | `#F8FAFC` | `#0F172A` |
| `slate-100` | `#F1F5F9` | `#1E293B` |
| `slate-200` | `#E2E8F0` | `#334155` |
| `slate-300` | `#CBD5E1` | `#475569` |
| `slate-400` | `#94A3B8` | `#64748B` |
| `slate-500` | `#64748B` | `#94A3B8` |
| `slate-600` | `#475569` | `#CBD5E1` |
| `slate-700` | `#334155` | `#E2E8F0` |
| `slate-800` | `#1E293B` | `#F1F5F9` |
| `slate-900` | `#0F172A` | `#F8FAFC` |
| `blue-50` | `#EFF6FF` | `#172554` |
| `blue-500` | `#3B82F6` | `#3B82F6` |
| `blue-600` | `#2563EB` | `#60A5FA` |
| `blue-700` | `#1D4ED8` | `#93BBFD` |
| `red-500` | `#EF4444` | `#EF4444` (error) |
| `green-500` | `#22C55E` | `#22C55E` (success) |
| `white` | `#FFFFFF` | `#0F172A` |
| `black` | `#000000` | `#FFFFFF` |

Notar la inversión en modo dark: los slates se invierten, el blue-600 (más oscuro) en light se convierte en blue-400 (más claro) en dark para mantener el contraste.

3. Crear colección "Semantic/Colors" con modos: Light, Dark. Esta colección referencia a las primitivas.

| Variable | Light (alias) | Dark (alias) |
|---|---|---|
| `color-bg-primary` | `white` | `slate-900` |
| `color-bg-secondary` | `slate-50` | `slate-800` |
| `color-bg-tertiary` | `slate-100` | `slate-700` |
| `color-text-primary` | `slate-900` | `slate-50` |
| `color-text-secondary` | `slate-500` | `slate-400` |
| `color-text-disabled` | `slate-400` | `slate-600` |
| `color-border-default` | `slate-200` | `slate-700` |
| `color-action-primary` | `blue-600` | `blue-500` |
| `color-action-hover` | `blue-700` | `blue-400` |
| `color-status-error` | `red-500` | `red-400` |
| `color-status-success` | `green-500` | `green-400` |

**Parte B - Sistema tipográfico:**

1. Crear colección "Typography" con modos: Desktop, Mobile.

2. Variables de familia tipográfica:
   - `font-family-sans`: 'Inter', sans-serif
   - `font-family-heading`: 'Inter', sans-serif (puede ser diferente)
   - `font-family-mono`: 'JetBrains Mono', monospace

3. Variables de tamaño de fuente (en px, que luego se traducirán a rem en CSS):

| Variable | Desktop | Mobile | Uso |
|---|---|---|---|
| `font-size-xs` | 12 | 11 | Captions, labels pequeños |
| `font-size-sm` | 14 | 13 | Texto secundario, botones pequeños |
| `font-size-base` | 16 | 15 | Texto de cuerpo principal |
| `font-size-lg` | 18 | 17 | Subtítulos |
| `font-size-xl` | 20 | 18 | Títulos de sección |
| `font-size-2xl` | 24 | 20 | Títulos de página |
| `font-size-3xl` | 30 | 24 | Headings principales |
| `font-size-4xl` | 36 | 28 | Hero titles |

4. Variables de peso de fuente (`font-weight`):
   - `font-weight-normal`: 400
   - `font-weight-medium`: 500
   - `font-weight-semibold`: 600
   - `font-weight-bold`: 700

5. Variables de line-height:
   - `line-height-tight`: 1.25 (headings)
   - `line-height-normal`: 1.5 (cuerpo de texto)
   - `line-height-relaxed`: 1.625 (texto extenso)

**Parte C - Documentación visual:**

En la página "Foundations → Colors" del archivo Figma:
1. Crear frames para cada paleta de color (Slate, Blue, Red, Green) mostrando todos los tonos.
2. Debajo de cada muestra, escribir el nombre de la variable y el valor hex.
3. En una sección aparte, mostrar los tokens semánticos aplicados a elementos de ejemplo (un texto primary sobre fondo primary, un texto secondary sobre fondo primary, etc.).

En la página "Foundations → Typography":
1. Crear frames con muestras de cada nivel tipográfico (desde xs hasta 4xl).
2. Especificar para cada muestra: nombre de la variable, font-family, font-size, font-weight, line-height.

Esta documentación es la que el equipo de desarrollo consultará para implementar el `@theme` de Tailwind. La correspondencia es directa: cada variable de Figma se convierte en una custom property en `@theme`.

### Ejemplo guiado 3: Diseñar una pantalla de login completa

**Objetivo:** Integrar todos los conocimientos de Figma (frames, Auto Layout, variables, componentes, texto) en el diseño de una pantalla real de aplicación.

**Duración:** 40 minutos.

**Desarrollo:**

**Paso 1 - Configurar el frame de pantalla:**
- Frame (F) → Desktop → 1440 × 900.
- Renombrar: "Login Screen".
- Auto Layout: no en el frame principal (lo usaremos en sub-frames). Layout: centrar elementos con constraints.

**Paso 2 - Diseñar el panel de login:**
1. Crear frame hijo (F), dimensiones: 400 × auto (hug contents).
2. Auto Layout (Shift+A): vertical, gap 24px, padding 32px, alineación stretch.
3. Posicionar en el centro del frame principal (X: 520, Y: 150, aproximadamente).
4. Corner radius: 16px. Fill: white (usar variable `color-bg-primary`). Efecto: drop shadow (shadow-lg en Tailwind).

**Paso 3 - Añadir contenido al panel:**

1. **Logo / Nombre de la app:**
   - Frame con Auto Layout horizontal, gap 8px, alineación center.
   - Icono (cuadrado 32×32, color `color-action-primary`, insertar desde Iconify o crear rectángulo).
   - Texto "AppName", fuente Inter, weight Bold, size `font-size-2xl`, color `color-text-primary`.

2. **Texto de bienvenida:**
   - Frame con Auto Layout vertical, gap 4px.
   - Texto "Iniciar sesión", weight Semibold, size `font-size-2xl`.
   - Texto "Accede a tu cuenta para continuar", weight Regular, size `font-size-sm`, color `color-text-secondary`.

3. **Campos del formulario:**
   - **Email input:**
     - Frame con Auto Layout vertical, gap 6px, alineación stretch.
     - Label: Texto "Correo electrónico", weight Medium, size `font-size-sm`.
     - Input: Frame con Auto Layout horizontal, gap 8px, padding 12px, corner radius 8px, border 1px (color `color-border-default`), fill `color-bg-primary`. Contiene icono mail (18×18) + texto "tu@email.com" (color `color-text-secondary`, size `font-size-sm`).
   - **Password input:** Similar pero con icono lock y un icono eye (toggle visibilidad) a la derecha.

4. **Opciones:**
   - Frame con Auto Layout horizontal, gap (space-between en distribución).
   - Checkbox + label "Recordarme".
   - Link "¿Olvidaste tu contraseña?" (color `color-action-primary`, weight Medium, size `font-size-sm`).

5. **Botón de login:**
   - Insertar instancia del componente Button creado en el Ejemplo Guiado 1.
   - Configurar: Variant = Primary, Size = Large, Width = Fill container, Texto = "Iniciar sesión".

6. **Separador "o":**
   - Frame con Auto Layout horizontal, gap 12px, alineación center.
   - Línea (rectángulo 1px de alto, fill `color-border-default`, resize: fill container).
   - Texto "o continuar con" (size `font-size-sm`, color `color-text-secondary`).
   - Línea (ídem a la primera).

7. **Botones sociales:**
   - Frame con Auto Layout horizontal, gap 12px.
   - Dos botones (instancias de Button, variante Outline, size Medium, width fill container): "Google" y "GitHub", cada uno con su icono.

8. **Link de registro:**
   - Frame con Auto Layout horizontal, gap 4px, alineación center.
   - Texto "¿No tienes cuenta?" + Link "Regístrate" (weight Semibold, color `color-action-primary`).

9. **Verificar espaciado y alineación:** Todo debe usar las variables de espaciado definidas. Los gaps y paddings deben ser consistentes (múltiplos de 4px: 4, 8, 12, 16, 20, 24, 32).

**Paso 4 - Versión con modo oscuro:**

1. Duplicar el frame de login.
2. Cambiar el modo del frame a "Dark" (en el panel de variables o propiedades del frame).
3. Todos los elementos que usan variables semánticas se actualizarán automáticamente: fondo blanco → fondo oscuro, texto oscuro → texto claro, bordes claros → bordes oscuros, etc.

**Paso 5 - Preparar para desarrollo:**

1. Seleccionar todos los elementos y verificar nombres semánticos en el panel Layers.
2. Seleccionar cada elemento y verificar en Dev Mode que las medidas, colores y tipografías son correctas.
3. Anotar (con el plugin de comentarios o con la herramienta de notas) cualquier comportamiento interactivo no obvio (al hacer clic en "Regístrate", redirigir a la pantalla de registro; al escribir en el campo de contraseña, validar que tenga al menos 8 caracteres).

**Resultado:** Una pantalla de login profesional, completa, con modo claro y oscuro, utilizando componentes reutilizables (Button, Input — si lo creamos como componente), variables semánticas y Auto Layout en toda su jerarquía. Preparada para ser implementada en Angular + Tailwind en la Unidad 5 (layout) y la Unidad 15 (handoff a código).

!!! example "Casos reales"

    ### Caso 1: El Design System de Shopify (Polaris)

    Shopify, plataforma de ecommerce canadiense, mantiene Polaris, uno de los sistemas de diseño más completos y accesibles públicamente. Polaris se gestiona en Figma como fuente de verdad de diseño y se implementa en React como librería de componentes. Es un caso de estudio notable porque Shopify ha compartido públicamente su proceso.

    En Figma, el equipo de Shopify organiza Polaris con múltiples archivos de librería:
    - **Polaris Foundations:** Variables de color, tipografía, espaciado, iconografía.
    - **Polaris Components:** Todos los componentes con todas sus variantes y estados. Cada componente tiene una página dedicada con explicaciones de uso, ejemplos y consideraciones de accesibilidad.
    - **Polaris Patterns:** Combinaciones de componentes para flujos comunes (creación de producto, configuración de envíos, gestión de pedidos).

    El equipo de desarrollo de Polaris utiliza Storybook para documentar los componentes implementados. Mantienen un riguroso alineamiento Figma ↔ Storybook: cada variante en Figma debe tener su story correspondiente. Cualquier discrepancia se considera un bug. El resultado es un sistema de diseño que reduce drásticamente el tiempo de desarrollo de nuevas funcionalidades (los equipos de producto no diseñan ni implementan componentes desde cero, solo los ensamblan).

    ### Caso 2: Startup andaluza: sistema de diseño para una app de turismo

    Imaginemos una startup malagueña desarrollando una aplicación de turismo sostenible para la Costa del Sol. La app incluye un dashboard para gestores de alojamientos (escritorio) y una app para viajeros (móvil, PWA). El equipo tiene un diseñador UI y dos desarrolladores (frontend Angular y backend).

    Flujo de trabajo con Figma:

    1. **El diseñador crea el sistema de diseño en Figma:** define los colores inspirados en la Costa del Sol (ocres, azules mediterráneos, blancos rotos), la tipografía (una serif para headings evocando tradición, una sans-serif para cuerpo para legibilidad en móvil), y diseña los componentes (botones, tarjetas de experiencias, barras de búsqueda, filtros, galerías de fotos, calendarios de disponibilidad).

    2. **El diseñador comparte la librería** con los desarrolladores, que pueden inspeccionar cada componente en Dev Mode: ver exactamente cuánto padding tiene una tarjeta, qué tipografía usa, cómo se comporta en hover.

    3. **Los desarrolladores implementan progresivamente** los componentes en Angular + Tailwind y los documentan en Storybook. El diseñador revisa cada componente en Storybook contra su diseño en Figma.

    4. **Cuando el diseñador actualiza** un componente en Figma (ej: ajusta el espaciado de las tarjetas de 16px a 20px porque los tests con usuarios mostraron que se sentían "apretadas"), los desarrolladores reciben una notificación (Figma comenta automáticamente en el componente actualizado), revisan el cambio en Dev Mode para ver exactamente qué ha cambiado, y actualizan el código correspondiente.

    Este flujo, aparentemente simple, es revolucionario respecto a prácticas anteriores (diseñador exporta PNGs → desarrollador mide "a ojo" con una regla en pantalla → implementa aproximadamente → diseñador ve el resultado en el staging → enumera discrepancias → desarrollador ajusta → iterar hasta converger). Figma + Storybook reducen los ciclos de feedback de semanas a horas.

## Actividades guiadas

### Actividad guiada 1: Reproducción de un componente existente

**Duración:** 30 minutos

**Desarrollo:** El docente proporciona una captura de pantalla de un componente de una interfaz conocida (por ejemplo, una Card de Spotify, un Tweet de Twitter, una tarjeta de producto de Amazon). El alumnado, siguiendo las indicaciones del docente, reproduce ese componente en Figma paso a paso, prestando especial atención a:

1. Jerarquía de frames y Auto Layouts.
2. Dimensiones exactas (medir desde la captura o usar valores razonables).
3. Tipografías (identificar pesos, tamaños, interlineados aproximados).
4. Colores (usar el cuentagotas sobre la captura o valores aproximados).
5. Espaciados y alineación.

El docente guía enfatizando la importancia de la nomenclatura de capas y el uso de Auto Layout incluso en componentes simples ("parece que este texto y este icono van en horizontal con un gap de 8px... ¿cómo lo haríamos en Figma?" → "Frame con Auto Layout horizontal, gap 8px").

**Objetivos:** Familiarizarse con la mecánica de Figma, practicar la observación analítica de interfaces y comenzar a desarrollar el "ojo" para traducir interfaces visuales a estructuras de diseño.

### Actividad guiada 2: Creación de un mini sistema de diseño

**Duración:** 40 minutos

**Desarrollo:** El alumnado crea, guiado por el docente, las bases de un sistema de diseño en Figma. El docente va dando instrucciones progresivas:

1. "Creamos una página 'Foundations' y dentro un frame para colores."
2. "Ahora creamos las variables de color primitivas (Slate 50-900, Blue 50-900). Usad la colección 'Primitives'."
3. "Ahora creamos la colección 'Semantic' y vinculamos a las primitivas. Necesitamos bg-primary, bg-secondary, text-primary, text-secondary, border-default, action-primary, action-hover."
4. "Añadimos modo Dark a las colecciones. Invertimos los slates. Verificamos que al cambiar el modo de un frame, los colores se actualizan."
5. "Creamos variables de espaciado (4, 8, 12, 16, 20, 24, 32, 40, 48, 64). ¿Usamos múltiplos de 4, de 8? Debate breve sobre sistemas de espaciado."
6. "Creamos una página 'Components' y creamos nuestro primer componente: Badge. Usamos Auto Layout, variables de color y texto."

El docente circula entre el alumnado resolviendo dudas y verificando que las vinculaciones de variables funcionan correctamente.

### Actividad guiada 3: Inspección de diseño en Dev Mode

**Duración:** 20 minutos

**Desarrollo:** El docente comparte un enlace a un archivo Figma con varios diseños de interfaces (pueden ser los ejemplos de Figma Community o diseños propios). El alumnado abre el archivo, activa el Dev Mode (Shift+D) y debe extraer la siguiente información para un componente asignado:

1. Dimensiones exactas (width × height).
2. Distancias a los bordes del frame padre (top, right, bottom, left).
3. Colores (fills, strokes) con sus valores hex.
4. Tipografía (font family, weight, size, line height, letter spacing).
5. Bordes (corner radius) y sombras (drop shadow, inner shadow).
6. Variables utilizadas (nombres y valores actuales).
7. Código CSS generado por Figma.

A continuación, deben traducir el CSS generado a clases Tailwind: `padding: 16px` → `p-4`, `border-radius: 8px` → `rounded-lg`, `display: flex; flex-direction: column; gap: 12px` → `flex flex-col gap-3`.

Puesta en común: ¿Es precisa la traducción automática de Figma a CSS? ¿Y a Tailwind? ¿Hay propiedades que Figma no captura correctamente? ¿Es mejor confiar en el código generado o inspeccionar manualmente?

## Actividades propuestas

### Actividad 1

**Nivel:** Básico
**Objetivo:** Familiarizarse con la interfaz de Figma y el concepto de Auto Layout.
**Enunciado:** Crea un archivo Figma llamado `apellido1-apellido2-practica-figma`. Dentro de él, crea una página llamada "Ejercicio 1 - Auto Layout". En esa página, reproduce los siguientes elementos usando EXCLUSIVAMENTE frames con Auto Layout:

1. **Una barra de navegación horizontal** con: logo (icono + texto a la izquierda), 4 enlaces de navegación (Inicio, Productos, Servicios, Contacto) en el centro, y un botón "Login" a la derecha. Usa Auto Layout horizontal con space-between.

2. **Una tarjeta de red social (tipo Tweet/Card)** con: avatar + nombre + @usuario + timestamp en la cabecera (Auto Layout horizontal, gap 8px), texto del post (multilínea, fill container), una imagen (fill container, altura fija 200px), y barra de acciones (me gusta, comentar, compartir, guardar) con Auto Layout horizontal y space-between. Todos los sub-elementos deben usar Auto Layout anidados.

3. **Una lista de ítems** (tipo lista de tareas) con 5 ítems. Cada ítem es un frame con Auto Layout horizontal (gap 12px, padding 12px, border-bottom 1px gris claro) que contiene: checkbox (cuadrado 20×20 con borde), texto de la tarea (fill container), badge de prioridad (Auto Layout, padding 4px 8px, background de color según prioridad, texto pequeño).

**Requisitos:** Todos los elementos deben usar Auto Layout sin excepción. Las capas deben tener nombres semánticos (nada de "Rectangle 7" o "Frame 23"). Usa variables de color (crea algunas básicas en la colección local si quieres practicar; si no, usa valores directos pero sé consistente).
**Pistas:** Para space-between en Auto Layout horizontal, usa la opción de distribución "Space between" en el panel de Auto Layout. Para que un elemento ocupe todo el ancho, configura su resizing a "Fill container".
**Criterios de evaluación:** (1) Uso correcto y generalizado de Auto Layout. (2) Nomenclatura semántica de capas. (3) Estructura jerárquica clara y lógica. (4) Fidelidad visual razonable (no se evalúa "belleza" sino corrección técnica).

### Actividad 2

**Nivel:** Medio
**Objetivo:** Crear un component set completo con variantes y propiedades.
**Enunciado:** En una página llamada "Ejercicio 2 - Componentes", crea los siguientes component sets con TODAS sus variantes. Para cada uno, extrae también la información necesaria para implementarlo en Angular + Tailwind (documenta en texto: nombre de los inputs, tipos TypeScript, clases Tailwind correspondientes a cada variante).

1. **Tabs:** Component set con propiedades: Variant (underline, pills, enclosed), Size (sm, md, lg). Cada tab individual debe ser un componente (con propiedad active: boolean, texto: string, badge opcional: number). El component set representa la barra de tabs completa (3-4 tabs). Implementa los estados active e inactive para cada combinación.

2. **Toggle / Switch:** Component set con propiedades: Size (sm, md, lg), State (off, on, disabled-off, disabled-on). Diseña el track (fondo) y el thumb (círculo que se desplaza). Para el estado "on", el thumb debe estar a la derecha del track y el track debe tener color primario.

3. **Select / Dropdown:** Component set con propiedades: Size (sm, md, lg), State (default, open, disabled, error). El componente debe mostrar: label (texto superior), input (con texto seleccionado y chevron abajo), y en el estado "open", una lista desplegable con opciones (3-4 ítems, uno con estado hover).

Para cada component set: (a) Crea las variables de diseño necesarias (colores, tamaños) en una colección. (b) Usa Auto Layout en todos los frames. (c) Añade descripción en el componente explicando su uso. (d) Crea instancias de prueba en una página aparte para verificar que las propiedades funcionan correctamente.
**Requisitos:** Mínimo 15 variantes por component set (todas las combinaciones de propiedades). Documenta la traducción Angular/Tailwind de cada componente como comentario en Figma o como nota en la página.
**Pistas:** Para Tabs, recuerda que los tabs individuales también pueden ser componentes independientes que luego se instancian dentro del componente "Tabs bar". Para evitar complejidad excesiva, puedes hacer que Tab sea un componente y TabsBar sea un frame que contiene instancias de Tab.
**Criterios de evaluación:** (1) Completitud de las variantes. (2) Correcto uso de propiedades de componente. (3) Calidad de la documentación de traducción a código. (4) Nomenclatura y organización.

### Actividad 3

**Nivel:** Medio
**Objetivo:** Crear un sistema de Design Tokens completo con variables, colecciones y modos.
**Enunciado:** En una página llamada "Ejercicio 3 - Design Tokens", implementa un sistema completo de design tokens como se describió en el Ejemplo Guiado 2, pero ampliado:

1. **Colección Primitives/Colors:** Paleta completa de 5 colores con 10 tonos cada uno (Slate, Blue, Emerald, Amber, Red). Incluye modos Light y Dark.

2. **Colección Semantic/Colors:** Al menos 20 tokens semánticos vinculando a las primitivas, con modos Light y Dark. No copies exactamente los del ejemplo; piensa qué tokens semánticos necesitaría una aplicación real (incluye tokens para estados: success, warning, error, info, además de los de superficie, texto, borde, acción).

3. **Colección Typography:** Variables de font-family, font-size (escala completa xs a 4xl), font-weight, line-height, letter-spacing. Con modos Desktop y Mobile.

4. **Colección Spacing:** Variables de espaciado (escala 0-64, múltiplos de 4px). Opcional: modos Desktop y Mobile si crees que los espaciados deben variar.

5. **Colección Radius:** Variables de border-radius (none: 0, sm: 4, md: 8, lg: 12, xl: 16, 2xl: 20, full: 9999).

6. **Colección Effects:** Variables de sombra (sm, md, lg, xl, 2xl) con modos Light y Dark (las sombras en dark mode suelen ser más sutiles o con color en lugar de negro).

Además, crea una página "Foundations" donde documentes visualmente todos los tokens: muestras de color con nombres y valores hex, muestras tipográficas, escala de espaciado, etc. Esta página debe ser comprensible para un desarrollador que no ha participado en el diseño.
**Requisitos:** Todas las variables de las colecciones Semantic deben referenciar variables de Primitives (vinculación real, no copia de valores). Los modos Light/Dark deben ser funcionales (al cambiar el modo de un frame, los colores cambian correctamente).
**Pistas:** Para verificar la vinculación correcta, cambia el valor de una primitiva en modo Light y verifica que los frames que usan variables semánticas vinculadas también cambian. Si no cambian, es que hiciste copia de valor en lugar de vinculación.
**Criterios de evaluación:** (1) Correcta vinculación entre variables primitivas y semánticas. (2) Funcionalidad de los modos Light/Dark. (3) Completitud y pertinencia de los tokens definidos. (4) Calidad de la documentación visual.

### Actividad 4

**Nivel:** Avanzado
**Objetivo:** Diseñar 3 pantallas completas de una aplicación aplicando el sistema de diseño.
**Enunciado:** Siguiendo con tu sistema de diseño de la Actividad 3 y los componentes de la Actividad 2, diseña en una página llamada "Ejercicio 4 - Pantallas" las siguientes pantallas completas para una aplicación de gestión de tareas (tipo Todoist/TickTick):

1. **Dashboard principal (1440×900):** Sidebar izquierdo con navegación (menú de proyectos, etiquetas, filtros), área de contenido principal con un resumen (tarjetas de estadísticas: tareas pendientes, completadas hoy, productividad semanal) y lista de tareas del día (lista de ítems con checkbox, texto, proyecto, prioridad, fecha). Barra superior con búsqueda, notificaciones y avatar de usuario.

2. **Pantalla de detalle de tarea (1440×900):** Panel central con el detalle de una tarea: título editable, descripción (multilínea), propiedades (fecha de vencimiento con date picker, prioridad con select, proyecto con select, etiquetas con multi-select), lista de subtareas (con checkboxes y barra de progreso), sección de comentarios (lista de comentarios con avatar, nombre, timestamp, texto).

3. **Pantalla de login (responsive: 1440×900 y 375×812):** Diseña la pantalla de login para escritorio y para móvil. Aplica el diseño del Ejemplo Guiado 3 pero con TU sistema de diseño (tus colores, tu tipografía, tus componentes). La adaptación móvil debe hacerse usando Auto Layout y las variables de tamaño responsive (typography y spacing con modos Desktop/Mobile si las definiste).

Para cada pantalla: (a) Usa exclusivamente instancias de componentes (no diseñes nada "ad-hoc", todo debe venir del sistema de diseño). (b) Si algún elemento necesario no está en tu sistema de diseño, créalo como componente primero. (c) Nombra todos los frames y capas semánticamente. (d) Crea un prototipo que conecte las pantallas: clic en una tarea del dashboard → navega al detalle.
**Requisitos:** Mínimo 80% de los elementos deben ser instancias de componentes. El prototipo debe ser interactivo (navegable en modo presentación).
**Pistas:** Crea componentes auxiliares según los necesites: DatePicker (aunque sea simplificado), ProgressBar, CommentItem, SubtaskItem, etc. No necesitas que sean funcionales, solo visualmente correctos.
**Criterios de evaluación:** (1) Consistencia visual (todo parece parte del mismo sistema). (2) Porcentaje de uso de componentes del sistema de diseño vs elementos ad-hoc. (3) Organización y nomenclatura de capas. (4) Funcionalidad del prototipo interactivo.

### Actividad 5

**Nivel:** Avanzado
**Objetivo:** Realizar un handoff completo de diseño a "desarrollo" (simulación documentada).
**Enunciado:** Elige UNA de las pantallas que diseñaste en la Actividad 4 (recomendada: el Dashboard principal). Vas a realizar un handoff simulado como si fueras a entregar el diseño al equipo de desarrollo. Prepara un documento de handoff (PDF o página Figma con anotaciones) que incluya:

1. **Resumen visual:** Captura de la pantalla completa con anotaciones numéricas que referencien a las especificaciones detalladas.

2. **Jerarquía de componentes:** Diagrama de árbol (hecho con Auto Layout en Figma o con cualquier herramienta) que muestre la estructura de componentes de la pantalla, desde el frame raíz hasta los átomos. Usa nombres de componentes Angular (app-sidebar, app-task-list, app-task-item, etc.).

3. **Especificaciones por componente:** Para cada componente personalizado de la pantalla, captura de pantalla del componente en Figma + especificaciones: dimensiones, paddings, gaps, colores (nombres de variables y valores), tipografía (nombres de variables y valores), bordes y sombras.

4. **Tokens utilizados:** Tabla de todos los design tokens utilizados en la pantalla, con sus valores actuales en modo Light.

5. **Código Tailwind sugerido:** Para los 3 componentes más complejos de la pantalla, escribe el código HTML + clases Tailwind que implementarían ese componente. Puedes ayudarte del código CSS generado por Figma en Dev Mode y traducirlo manualmente a Tailwind.

6. **Assets a exportar:** Lista de iconos, imágenes e ilustraciones necesarias, con indicación de formato de exportación recomendado (SVG para iconos e ilustraciones, PNG para imágenes raster, WebP como alternativa optimizada).

7. **Consideraciones de implementación:** Notas sobre comportamientos interactivos, animaciones, estados (loading, empty, error, edge cases), accesibilidad (roles ARIA, navegación por teclado, contraste).

**Requisitos:** El documento debe ser usable sin necesidad de abrir Figma (un desarrollador debería poder implementar la pantalla solo con este documento + los componentes de Storybook equivalentes). Incluye capturas reales de tu Figma.
**Pistas:** Usa el plugin "Annotations" o simplemente frames con texto para las anotaciones en Figma. Para exportar a PDF, Figma permite File → Export frames to PDF.
**Criterios de evaluación:** (1) Exhaustividad (¿está TODO lo que un desarrollador necesita?). (2) Organización y claridad. (3) Precisión de las traducciones a Tailwind. (4) Calidad de las consideraciones de implementación (no solo describir lo obvio, sino anticipar dificultades).

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Design system completo listo para producción

    Desarrolla un sistema de diseño completo en Figma que cubra TODOS los componentes necesarios para una aplicación CRUD empresarial típica. Requisitos mínimos:

    1. **Foundations:** Paleta de colores completa (primitivas + semánticas), tipografía, espaciado, radius, sombras, iconografía (mínimo 20 iconos) — todo con variables y modos Light/Dark.

    2. **Componentes (18 mínimo):** Button, Input, Textarea, Select, Checkbox, Radio, Toggle, Badge, Chip/Tag, Avatar, Card, Modal/Dialog, Tooltip, Dropdown/Menu, Table, Tabs, Breadcrumbs, Pagination, Alert/Toast, Skeleton loader, Empty state, Progress bar.

    3. **Patrones (5 mínimo):** Formulario de creación/edición, Tabla con búsqueda y filtros, Dashboard con widgets, Wizard multi-paso, Layout de aplicación (sidebar + header + contenido).

    4. **Pantallas de ejemplo (3 mínimo):** Listado CRUD, detalle de elemento, formulario de creación, pantalla de login.

    5. **Documentación:** Página de "Getting Started" en Figma explicando cómo usar el sistema de diseño. Página de "Changelog" para versionado. Anotaciones de accesibilidad en al menos los 5 componentes más críticos.

    6. **Prototipo interactivo:** Conecta las pantallas de ejemplo para simular flujos de usuario reales.

    Entrega: enlace al archivo Figma (acceso público como view-only) + breve informe (500 palabras) sobre las decisiones de diseño más importantes que tomaste (¿por qué elegiste esos colores? ¿qué escala de espaciado usaste y por qué? ¿cómo organizaste las variables?).

    ### Actividad de ampliación 2: Plugin de Figma para auditoría de accesibilidad visual

    Desarrolla un plugin de Figma que, al ejecutarse sobre un frame seleccionado, audite los siguientes aspectos de accesibilidad visual y muestre un informe en el panel del plugin:

    1. **Contraste de color:** Para cada elemento de texto, detecta el color del texto y del fondo (inmediato y fondos intermedios con opacidad) y verifica si cumple WCAG AA (ratio ≥ 4.5:1 para texto normal, ≥ 3:1 para texto grande > 18px o bold > 14px).

    2. **Tamaño de texto:** Identifica todos los textos menores de 12px (difíciles de leer) y los marca como warning.

    3. **Tamaño de target táctil:** Identifica todos los elementos interactivos (botones, inputs, checkboxes, links) cuyas dimensiones sean menores a 44×44px (mínimo recomendado por Apple y Google para targets táctiles).

    4. **Espaciado entre targets táctiles:** Identifica targets táctiles que estén a menos de 8px de distancia entre sí (riesgo de pulsación errónea).

    El plugin debe usar la API de plugins de Figma (https://www.figma.com/plugin-docs/) y mostrar los resultados en el panel de UI del plugin (iframe HTML). Entrega: código del plugin en GitHub + README con instrucciones de instalación y uso.

    ### Actividad de ampliación 3: Automatización de Design Tokens con Style Dictionary

    Utiliza Style Dictionary (de Amazon, https://amzn.github.io/style-dictionary/) para crear un pipeline automatizado que:

    1. Toma como entrada un archivo JSON con design tokens (puedes exportar tus variables de Figma con un plugin como "Design Tokens" y convertirlo a JSON, o escribir el JSON manualmente).

    2. Genera como salida:
       - Archivo CSS con custom properties (listo para copiar en `styles.css` de Angular).
       - Archivo de configuración `@theme` para Tailwind CSS 4 (con la sintaxis correcta de `@theme { ... }`).
       - Archivo TypeScript con las variables como objetos tipados (para usar en Angular si se necesita acceso programático a los tokens).
       - Archivo SCSS (opcional, para compatibilidad con proyectos legacy).
       - Documentación Markdown con tabla de tokens y muestras de color.

    3. Configura un script npm que ejecute Style Dictionary como parte del build, de modo que una modificación del JSON de entrada regenere automáticamente todos los archivos de salida.

    4. Documenta todo el proceso en un README: estructura del JSON de entrada, comandos, archivos de salida, cómo integrarlo en el flujo de trabajo Angular + Tailwind.

    Entrega: repositorio GitHub con el JSON de entrada, la configuración de Style Dictionary, los archivos de salida generados (como demostración) y el README.

!!! tip "Buenas prácticas"

    1. **Diseña con Auto Layout desde el primer frame.** El Auto Layout no debe ser un añadido posterior ("voy a diseñar y luego le pongo Auto Layout"). Es la forma natural de construir layouts en Figma, equivalente a usar `display: flex` en CSS mental. Todo frame que contenga otros elementos debe tener Auto Layout.

    2. **Usa variables desde el principio, no valores hardcodeados.** Antes de diseñar el primer componente, define las variables de color, tipografía y espaciado. Conforme avances, añadir variables se vuelve exponencialmente más difícil. Si empiezas con valores hardcodeados, la migración a variables es tediosa y propensa a errores.

    3. **Nombra las capas con significado.** "Frame 47" no dice nada. "Card / Header / Avatar" es comprensible para cualquier persona que abra el archivo. En sistemas grandes con cientos de frames, la nomenclatura semántica es la diferencia entre un archivo navegable y uno incomprensible.

    4. **Mantén las librerías de componentes al día.** Los componentes no deben ser estáticos. A medida que el producto evoluciona, el sistema de diseño debe evolucionar con él. Dedica tiempo a revisar, actualizar y refinar los componentes. Un sistema de diseño desactualizado es contraproducente (los diseñadores dejan de usarlo porque "los componentes no se parecen a lo que necesitamos").

    5. **Diseña para el peor caso, no solo para el caso ideal.** ¿Qué pasa si el nombre del usuario es "María del Carmen Fernández de la Torre y Rodríguez de la Fuente"? ¿Qué pasa si no hay datos y hay que mostrar un empty state? ¿Qué pasa si hay un error de red? Diseñar todos los estados (ideal, vacío, error, carga, borde) evita que el desarrollador tenga que improvisar.

    6. **Comunica el comportamiento, no solo la apariencia.** Una interfaz no es una imagen estática. ¿Qué animación ocurre al cambiar de pantalla? ¿Aparece un tooltip con delay o instantáneamente? ¿El modal se cierra con Escape? Estas decisiones impactan la implementación y deben ser comunicadas explícitamente, no inferidas.

    7. **Establece un solo source of truth.** Figma debe ser el lugar donde se responde a la pregunta "¿cómo debe verse este componente?". Si las decisiones de diseño se toman en Slack, en emails o en conversaciones de pasillo, pero no se reflejan en Figma, el archivo deja de ser la fuente de verdad y pierde su valor. Todo cambio de diseño debe pasar por Figma.

    8. **Valida la accesibilidad en Figma, no solo en código.** Plugins como Stark permiten verificar contraste y simular daltonismo en tiempo de diseño. Corregir un problema de contraste en Figma cuesta 30 segundos (cambiar un color). Hacerlo en código después de implementar 20 componentes cuesta horas. Adelanta la validación de accesibilidad al diseño.

!!! warning "Errores frecuentes"

    1. **No usar Auto Layout y posicionar elementos manualmente con coordenadas X/Y absolutas.** Es el equivalente a maquetar una web con `position: absolute` para todo. Funciona para diseños estáticos, pero se rompe en cuanto el contenido cambia. Cualquier desarrollador que intente implementar un diseño sin Auto Layout tendrá que adivinar cómo debe comportarse cuando el texto es más largo o cuando se añaden más elementos.

    2. **No usar variables o usar variables incorrectamente.** Usar colores hardcodeados (#3B82F6 repetido 50 veces en lugar de usar la variable `blue-600`) crea una pesadilla de mantenimiento. Si el color primario cambia, hay que editar 50 elementos manualmente. Peor aún: definir una variable `blue-600` y luego usar otra variable `blue-600-duplicated` porque "no me acordaba de que ya existía". Mantén una única fuente de verdad para cada valor.

    3. **Crear componentes demasiado específicos que no son reutilizables.** "CardProductWithDiscountBadgeAndFreeShippingBanner" no es un componente, es una instancia configurada de un componente Card genérico. Los componentes base deben ser genéricos y configurables; las instancias se configuran para casos específicos. Si cada pantalla necesita su propio componente, has fallado en la abstracción.

    4. **No diseñar estados (hover, focus, disabled, error, loading, empty).** El desarrollador recibe el diseño del estado "ideal" de la pantalla y nada más. Cuando implementa los estados de error y loading, los inventa sobre la marcha. El resultado: inconsistencia visual entre pantallas (cada una tiene su propio estilo de loading spinner, su propio color de error, su propio mensaje de empty state).

    5. **No nombrar capas y luego pretender que el desarrollador entienda el diseño.** Abrir un Figma y ver "Rectangle 1, Rectangle 2, Group 3, Frame 4" es desmoralizador. El desarrollador tiene que hacer ingeniería inversa del diseño para entender qué es cada cosa. Invertir 30 segundos en nombrar cada capa ahorra horas de confusión.

    6. **No alinear diseño y código en cuanto a sistema de espaciado.** El diseñador usa espaciados de 3px, 7px, 11px, 13px... valores que no están en la escala de Tailwind ni en su propio sistema de diseño. El desarrollador tiene que decidir entre usar valores arbitrarios (w-[13px]) rompiendo la consistencia, o redondear a 12px o 16px y tener una discrepancia con el diseño. Define y usa una escala de espaciado clara, y que sea compatible con Tailwind (múltiplos de 4px = 0.25rem).

    7. **Exportar PNG de todo en lugar de usar SVG para gráficos vectoriales.** Iconos, logos, ilustraciones simples deben exportarse como SVG (infinitamente escalables, tamaño mínimo, editables). Exportarlos como PNG los pixeliza en pantallas de alta densidad y aumenta el peso de la aplicación. La regla: si es vectorial, SVG; si es fotográfico, PNG/WebP.

    8. **Olvidar que Figma NO es un navegador web.** Figma renderiza texto de forma diferente a los navegadores (especialmente en cuanto a line-height y espaciado). Un diseño que se ve perfecto en Figma puede tener diferencias sutiles al implementarlo en HTML/CSS. No te obsesiones con la precisión al píxel; el objetivo es la consistencia visual general, no la réplica exacta (que es técnicamente imposible). Las diferencias de 1-2px son aceptables.

!!! abstract "Resumen"

    Esta unidad ha sido un viaje completo por Figma, desde los fundamentos del espacio de trabajo hasta la construcción de sistemas de diseño profesionales listos para handoff a desarrollo. Hemos establecido el puente conceptual y práctico entre el mundo del diseño visual y el mundo del desarrollo frontend, un puente que transitaremos constantemente durante todo el módulo.

    Comenzamos con los fundamentos: el canvas, las capas, los frames, las herramientas de creación. Conceptualmente simples, pero la base sobre la que se construye todo lo demás. Aprendimos a crear y organizar diseños como jerarquías de frames, entendiendo que cada frame de Figma es un futuro `<div>` en HTML y que cada grupo es un futuro componente.

    Auto Layout se reveló como la funcionalidad estrella: el equivalente en Figma a Flexbox en CSS y a las clases `flex` de Tailwind. Dominar Auto Layout significa pensar en layouts flexibles y dinámicos, no en composiciones estáticas. Cada propiedad de Auto Layout (dirección, gap, padding, alineación, resizing) tiene una traducción directa a código, y ejercitar esta traducción mental es una de las competencias más valiosas de esta unidad.

    Las variables llevaron el diseño al siguiente nivel de profesionalización. Definir paletas de colores, escalas tipográficas y sistemas de espaciado como variables reutilizables, vinculables y con soporte para modos (light/dark) transforma un archivo de diseño en un verdadero sistema. La equivalencia con los Design Tokens y con las custom properties de CSS (y por extensión con `@theme` de Tailwind) hace que la transición del diseño al código sea fluida y predecible.

    Los componentes y variantes de Figma son el corazón del sistema de diseño. Aprendimos a crearlos, configurarlos con propiedades (texto, boolean, instance swap), agruparlos en component sets con múltiples dimensiones de variación (variant × size × state × icon), y a pensar en ellos como los futuros componentes Angular con sus inputs y sus clases condicionales de Tailwind.

    El Dev Mode y las estrategias de handoff cierran el círculo: el diseño no es un fin en sí mismo, sino el plano de construcción para el desarrollo. Aprendimos a inspeccionar diseños, extraer especificaciones precisas, exportar assets y comunicar decisiones de diseño de forma que el equipo de desarrollo pueda implementarlas fielmente sin ambigüedades.

    En la Unidad 5 nos centraremos en los layouts modernos con Flexbox y CSS Grid implementados con Tailwind CSS, construyendo las estructuras sobre las que se asentarán los componentes diseñados en esta unidad. En la Unidad 15 (del diseño a la implementación) recorreremos el camino completo: desde un diseño en Figma hasta una aplicación Angular completa, pasando por la extracción de tokens, la configuración de Tailwind y la implementación de componentes documentados en Storybook.

## Recursos complementarios

### Documentación oficial

- **Figma Learn (oficial):** https://help.figma.com/hc/en-us — Documentación oficial con guías, tutoriales y referencia completa de funcionalidades.
- **Figma YouTube Channel:** https://www.youtube.com/c/Figmadesign — Webinars oficiales, tutoriales de funcionalidades, charlas de la conferencia Config.
- **Figma Developer Docs:** https://www.figma.com/developers — Documentación de la API de plugins, REST API y guías para desarrolladores.
- **Figma Best Practices (guía oficial):** https://www.figma.com/best-practices/ — Artículos sobre Auto Layout, componentes, sistemas de diseño y handoff.

### Tutoriales y cursos

- **Figma for Beginners (Figma, gratuito):** Curso interactivo dentro de la propia herramienta. Accesible desde Help → Learn.
- **Figma 101 (Figma, gratuito):** Curso de 7 lecciones en la web de Figma Learn.
- **Design Systems with Figma (Figma, gratuito):** Curso específico sobre sistemas de diseño en Figma.
- **Auto Layout Playground (Figma Community):** Archivo Figma interactivo para practicar Auto Layout.

### Figma Community (archivos de ejemplo)

- **Material Design 3 (Google):** Design system oficial de Google en Figma. Excelente ejemplo de organización profesional.
- **iOS 18 UI Kit (Apple, no oficial):** Componentes de iOS para estudiar patrones de diseño móvil.
- **Tailwind CSS UI Kit:** Kits de componentes diseñados específicamente para traducir a Tailwind.
- **Accessibility Annotation Kit:** Herramientas para anotar consideraciones de accesibilidad en diseños.

### Plugins recomendados

- **Tailwind CSS** — Generación de clases Tailwind desde diseños.
- **Iconify** — Más de 150,000 iconos SVG de sets como Material Design, Heroicons, Lucide, Phosphor.
- **Stark** — Herramientas de accesibilidad (contraste, daltonismo, visión borrosa).
- **Design Tokens** — Exportar tokens de diseño a JSON.
- **Tokens Studio for Figma** — Gestión avanzada de design tokens con Git sync.
- **Unsplash** — Imágenes de stock gratuitas.
- **Content Reel** — Contenido placeholder realista.
- **html.to.design** — Convertir páginas web en diseños Figma editables.
- **Autoflow** — Dibujar flechas de flujo entre frames (para diagramas de navegación).
- **Remove BG** — Eliminar fondos de imágenes.

### Libros recomendados

- Vesselov, S. y Davis, T. (2022). *Building Design Systems: Unify User Experiences through a Shared Design Language*. Apress.
- Kholmatova, A. (2017). *Design Systems: A practical guide to creating design languages for digital products*. Smashing Magazine.
- Pérez, D. y Maldonado, S. (2023). *Diseño de interfaces web*. Editorial Síntesis. (En español, adaptado al currículo de ciclos formativos).

### Comunidades

- **Figma Community (oficial):** https://www.figma.com/@community — Foros, archivos de ejemplo, grupos de usuarios.
- **r/Figma (Reddit):** https://reddit.com/r/Figma — Comunidad activa de usuarios.
- **Friends of Figma (grupos locales):** Encuentros y comunidades locales en varias ciudades españolas.
- **Design Systems (GitHub):** https://github.com/alexpate/awesome-design-systems — Colección curada de sistemas de diseño públicos.
