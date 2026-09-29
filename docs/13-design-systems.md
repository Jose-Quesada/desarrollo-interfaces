---
icon: lucide/palette
---

# Design Systems

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:
- Comprender qué es un **Design System**, sus componentes y su valor estratégico en el desarrollo de interfaces profesionales.
- Aplicar la metodología **Atomic Design** para descomponer una interfaz en átomos, moléculas, organismos, templates y páginas, y trasladar esta estructura a un proyecto Angular.
- Definir, implementar y gestionar **Design Tokens** como fuente única de verdad visual, sincronizándolos entre Figma y código mediante **Tailwind CSS 4**.
- Construir un Design System completo paso a paso, desde la auditoría visual hasta la documentación y el versionado.
- Establecer escalas consistentes de tipografía, espaciado, color, sombras y bordes como base de un lenguaje visual coherente.
- Analizar y extraer aprendizajes de **Design Systems reales** (Material Design 3, Ant Design, Carbon, Spectrum, Lightning) para aplicarlos en proyectos propios.
- Implementar un **ThemeProvider** en Angular con **Signals** para alternar entre temas visuales (claro, oscuro, high-contrast).

## Resultado de aprendizaje asociado

Esta unidad contribuye, como RA principal, al **RA 3** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 3.** Crea componentes visuales valorando y empleando herramientas específicas.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE a) Se han identificado las herramientas para diseño y prueba de componentes.
- CE b) Se han creado componentes visuales.
- CE c) Se han definido sus métodos y propiedades con asignación de valores por defecto.
- CE f) Se han documentado los componentes creados.
- CE h) Se han programado aplicaciones cuyo interfaz gráfico utiliza los componentes creados.

Como RA secundario, se vincula al **RA 4** («Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad»):

- CE g) Se ha diseñado el aspecto de la interfaz de usuario (colores y fuentes entre otros) atendiendo a su legibilidad.

!!! note "Conocimientos previos"

    El alumnado debe dominar los siguientes conocimientos antes de abordar esta unidad:
    - **Angular Standalone Components**, **Signals**, @Input/@Output, proyección de contenido (Unidades 10 y 11).
    - **Tailwind CSS 4**: sistema de clases utilitarias, configuración con @theme, capas (base, components, utilities).
    - **Figma**: fundamentos de diseño de interfaces, manejo de estilos compartidos, componentes y variantes.
    - **TypeScript**: tipos avanzados, interfaces, objetos de configuración.
    - **CSS avanzado**: custom properties (variables CSS), herencia, especificidad.
    - **Principios de diseño**: teoría del color, tipografía, espaciado, jerarquía visual, accesibilidad (contraste WCAG).
    - Control de versiones con **Git** y convenciones de commit semántico.

## Contenidos

1. Fundamentos de Design Systems
2. Atomic Design aplicado a Angular
3. Design Tokens: de Figma a Tailwind
4. Construcción de un Design System paso a paso
5. Escalas y sistemas visuales
6. Casos reales de Design Systems
7. ThemeProvider y cambio de tema

## Desarrollo teórico

### SECCIÓN A — QUÉ ES UN DESIGN SYSTEM

!!! info "Definición"

    Un **Design System** es mucho más que una librería de componentes o una guía de estilos. Es un **lenguaje visual compartido** que establece las reglas, los principios y los activos que permiten a equipos multidisciplinares (diseño, desarrollo, producto, marketing) construir interfaces coherentes, escalables y eficientes. Un Design System es, en esencia, la materialización de la identidad visual de un producto o marca en un conjunto de herramientas reutilizables y documentadas.

Los componentes fundamentales de un Design System son:

1. **Principios de diseño:** Los valores y creencias que guían las decisiones de diseño. Por ejemplo: "Claridad sobre consistencia", "Accesibilidad primero", "Menos es más". Estos principios ayudan a decidir cuando surgen dudas sobre qué enfoque tomar.

2. **Design Tokens:** Las unidades atómicas del sistema visual. Colores, tipografía, espaciado, sombras, bordes y animaciones expresadas como variables que pueden consumirse tanto en herramientas de diseño (Figma) como en código (CSS custom properties, Tailwind @theme, TypeScript). Los tokens son ==la fuente única de verdad que garantiza la coherencia entre diseño y desarrollo==.

3. **Componentes:** Bloques de construcción de la interfaz implementados como componentes Angular reutilizables (Button, Input, Card, Modal, etc.), cada uno con sus variantes, estados y documentación.

4. **Patrones:** Combinaciones frecuentes de componentes que resuelven problemas comunes de interfaz (formulario de búsqueda con filtros, tabla con paginación y ordenación, wizard multi-paso).

5. **Documentación:** Storybook, guías de uso, principios de diseño, tokens disponibles, ejemplos de código, consideraciones de accesibilidad y directrices de contribución.

Los beneficios de invertir en un Design System son sustanciales y medibles:
- **Consistencia visual:** La misma paleta de colores, la misma tipografía, los mismos espaciados en toda la aplicación, sin desviaciones accidentales.
- **Velocidad de desarrollo:** Los desarrolladores ensamblan interfaces a partir de componentes existentes en lugar de construir cada pantalla desde cero. Se estima que un Design System reduce el tiempo de desarrollo de nuevas funcionalidades entre un 25% y un 50%.
- **Escalabilidad:** Nuevas features y nuevos productos pueden construirse sobre la misma base, garantizando que se vean y se comporten como parte de la misma familia.
- **Comunicación diseño-desarrollo:** Un lenguaje compartido (tokens, componentes nombrados) elimina ambigüedades y reduce el ida y vuelta entre diseñadores y desarrolladores.
- **Onboarding más rápido:** Los nuevos miembros del equipo tienen un catálogo documentado de lo que existe y cómo usarlo, en lugar de tener que descubrirlo explorando el código.

### SECCIÓN B — ATOMIC DESIGN APLICADO A ANGULAR

**Atomic Design**, metodología creada por **Brad Frost**, propone descomponer las interfaces en cinco niveles jerárquicos de complejidad creciente. Esta metodología se adapta perfectamente a la arquitectura de componentes de Angular y proporciona un marco mental para organizar el catálogo de componentes de un Design System.

#### Átomos: los bloques fundamentales

Los **átomos** son los elementos más básicos de la interfaz: etiquetas HTML nativas estilizadas y los **tokens de diseño** aplicados a ellas. En el contexto de Angular + Tailwind, los átomos no suelen ser componentes independientes, sino que se implementan como:
- **Design Tokens en Tailwind:** La configuración `@theme` define los átomos de color (colores primitivos y semánticos), tipografía (familias, tamaños, pesos, alturas de línea) y espaciado (escala base de 4px).
- **Estilos base (layer base de Tailwind):** Estilos globales para elementos HTML nativos como `h1-h6`, `p`, `a`, `ul`, `ol`, `blockquote`, `code`, que se definen una sola vez y afectan a toda la aplicación.
- **Componentes atómicos simples:** `BadgeComponent`, `AvatarComponent`, `IconComponent`, `DividerComponent` — componentes que envuelven un único concepto visual sin composición de otros componentes.

Ejemplo de átomos como tokens en Tailwind 4:

```
/* styles/tokens.css - Capa @theme de Tailwind 4 */
@import "tailwindcss";

@theme {
  /* Colores primitivos */
  --color-blue-50: #eff6ff;
  --color-blue-100: #dbeafe;
  --color-blue-500: #3b82f6;
  --color-blue-600: #2563eb;
  --color-blue-700: #1d4ed8;

  --color-gray-50: #f9fafb;
  --color-gray-100: #f3f4f6;
  --color-gray-200: #e5e7eb;
  --color-gray-500: #6b7280;
  --color-gray-700: #374151;
  --color-gray-900: #111827;

  /* Colores semanticos */
  --color-primary: var(--color-blue-600);
  --color-primary-hover: var(--color-blue-700);
  --color-primary-light: var(--color-blue-50);
  --color-success: #059669;
  --color-warning: #d97706;
  --color-error: #dc2626;
  --color-info: #2563eb;

  /* Tipografia */
  --font-family-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;
  --font-family-mono: 'JetBrains Mono', ui-monospace, monospace;

  /* Escala tipografica modular */
  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 1.875rem;  /* 30px */
  --font-size-4xl: 2.25rem;   /* 36px */
  --font-size-5xl: 3rem;      /* 48px */

  /* Escala de espaciado (baseline grid 4px) */
  --spacing-1: 0.25rem;   /* 4px */
  --spacing-2: 0.5rem;    /* 8px */
  --spacing-3: 0.75rem;   /* 12px */
  --spacing-4: 1rem;      /* 16px */
  --spacing-5: 1.25rem;   /* 20px */
  --spacing-6: 1.5rem;    /* 24px */
  --spacing-8: 2rem;      /* 32px */
  --spacing-10: 2.5rem;   /* 40px */
  --spacing-12: 3rem;     /* 48px */
  --spacing-16: 4rem;     /* 64px */

  /* Sombras (escala de elevacion) */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);

  /* Bordes */
  --radius-sm: 0.375rem;   /* 6px */
  --radius-md: 0.5rem;     /* 8px */
  --radius-lg: 0.75rem;    /* 12px */
  --radius-xl: 1rem;       /* 16px */
  --radius-full: 9999px;
}
```

#### Moléculas: combinación de átomos

Las **moléculas** son combinaciones de átomos que funcionan juntos como una unidad. En Angular, las moléculas son componentes que combinan elementos HTML (átomos) y posiblemente otros componentes atómicos para formar una unidad funcional con propósito específico.

Ejemplos de moléculas en Angular:
- **FormFieldComponent:** Combina un `label` (átomo), un `input` (átomo HTML), un mensaje de `error` (átomo de texto) y posiblemente un `icon` (átomo visual) en una unidad cohesiva de entrada de datos.
- **SearchBarComponent:** Combina un `FormField` o un `input` con un `Button` de búsqueda y posiblemente un `Dropdown` de filtros.
- **NavItemComponent:** Combina un `icon` con un texto y un enlace, con estado activo basado en la ruta actual.
- **StatCardComponent:** Combina un `Card` (molécula/átomo), texto (átomo), badge de tendencia (átomo) y posiblemente un icono.
- **ListItemComponent:** Combina un `Avatar`, texto primario, texto secundario y acciones (botones o iconos).

Ejemplo de molécula SearchBar:

```
@Component({
  selector: 'ui-search-bar',
  standalone: true,
  template: `
    <div class="relative">
      <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
        <svg class="h-5 w-5 text-gray-400" aria-hidden="true" ...><!-- icono lupa --></svg>
      </div>
      <input
        type="search"
        [placeholder]="placeholder()"
        [value]="value()"
        (input)="onInput($event)"
        (keydown.escape)="clear()"
        class="block w-full rounded-lg border border-gray-300 bg-white py-2 pl-10 pr-10 text-sm
               placeholder:text-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-500" />
      @if (value()) {
        <button
          type="button"
          class="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-gray-600"
          (click)="clear()">
          <svg class="h-5 w-5" aria-label="Limpiar busqueda" ...><!-- icono X --></svg>
        </button>
      }
    </div>
  `,
})
export class SearchBarComponent {
  value = model('');
  placeholder = input('Buscar...');
  search = output<string>();

  onInput(event: Event): void { ... }
  clear(): void { this.value.set(''); }
}
```

#### Organismos: secciones funcionales complejas

Los **organismos** son conjuntos de moléculas y átomos que forman una sección distintiva de la interfaz. Son lo suficientemente complejos como para tener una función autónoma dentro de la página, pero no son páginas completas. En Angular, los organismos son **Smart Components** o componentes compuestos que orquestan múltiples moléculas.

Ejemplos de organismos:
- **HeaderComponent:** Contiene el logotipo, la navegación principal (múltiples NavItem), la barra de búsqueda (SearchBar), el menú de usuario (Dropdown) y el toggle de tema (ThemeToggle).
- **DataTableWithFiltersComponent:** Combina una barra de filtros (SearchBar + Dropdowns + DatePicker), una tabla de datos (DataTable) con paginación, y un contador de resultados.
- **ProductFormComponent:** Formulario completo con secciones de datos básicos, imágenes, precios y variantes, cada una con múltiples FormField.
- **NotificationCenterComponent:** Panel que lista notificaciones (ListItem + Badge) con un botón "Marcar todas como leídas".

```
@Component({
  selector: 'app-header',
  standalone: true,
  imports: [SearchBarComponent, ThemeToggleComponent, DropdownComponent, RouterLink],
  template: `
    <header class="sticky top-0 z-40 border-b border-gray-200 bg-white">
      <div class="flex h-16 items-center gap-4 px-4 sm:px-6">
        <!-- Logo -->
        <a routerLink="/" class="flex items-center gap-2">
          <img src="logo.svg" alt="Logo" class="h-8 w-auto" />
          <span class="text-lg font-bold text-gray-900">Brand</span>
        </a>

        <!-- Navegacion principal -->
        <nav class="hidden md:flex items-center gap-1 ml-8" aria-label="Navegacion principal">
          @for (item of navItems(); track item.label) {
            <a [routerLink]="item.route"
               class="rounded-lg px-3 py-2 text-sm font-medium transition-colors"
               [routerLinkActive]="'bg-gray-100 text-gray-900'"
               [routerLinkActiveOptions]="{ exact: item.exact }">
              {{ item.label }}
            </a>
          }
        </nav>

        <!-- Espaciador -->
        <div class="flex-1"></div>

        <!-- Busqueda (escritorio) -->
        <div class="hidden lg:block w-80">
          <ui-search-bar placeholder="Buscar..." />
        </div>

        <!-- Acciones -->
        <div class="flex items-center gap-2">
          <ui-theme-toggle />
          <ui-dropdown [items]="userMenuItems()" placement="bottom-end">
            <button dropdown-trigger class="flex items-center gap-2">
              <ui-avatar [name]="userName()" size="sm" />
              <span class="hidden sm:block text-sm font-medium">{{ userName() }}</span>
            </button>
          </ui-dropdown>
        </div>
      </div>
    </header>
  `,
})
export class HeaderComponent { ... }
```

#### Templates: estructura de página

Los **templates** son la estructura de página donde los organismos se combinan para formar el layout completo. Definen la disposición espacial y el esqueleto, pero sin contenido real. En Angular, el template por excelencia es el `LayoutComponent` que contiene el header, sidebar, área de contenido y footer.

#### Páginas: instancias concretas

Las **páginas** son instancias específicas de templates rellenas con contenido real. Por ejemplo, el `DashboardPageComponent` es una página que utiliza el `LayoutComponent` como template y lo rellena con datos reales de estadísticas, gráficos y tablas. Las páginas son donde se prueba que el Design System funciona en condiciones reales.

#### Aplicación práctica de la estructura Atomic Design en el proyecto Angular

La estructura de carpetas del proyecto refleja naturalmente la jerarquía de Atomic Design:

```
src/app/
├── design-system/          # Átomos (tokens, configuración)
│   ├── tokens.css          # Design Tokens (@theme de Tailwind)
│   └── theme.service.ts    # Servicio de tema
├── shared/                 # Átomos y moléculas reutilizables
│   └── components/
│       ├── button/         # Átomo
│       ├── badge/          # Átomo
│       ├── avatar/         # Átomo
│       ├── form-field/     # Molécula (label + input + error)
│       ├── search-bar/     # Molécula (input + icono + boton)
│       ├── data-table/     # Organismo (tabla + paginacion + estados)
│       └── modal/          # Organismo (overlay + panel + animaciones)
├── layout/                 # Templates
│   ├── layout.component.ts
│   ├── header/             # Organismo
│   ├── sidebar/            # Organismo
│   └── footer/             # Organismo
└── features/               # Páginas
    ├── dashboard/
    │   └── dashboard.page.ts
    └── products/
        └── products.page.ts
```

### SECCIÓN C — DESIGN TOKENS EN PROFUNDIDAD

#### Categorías de tokens

Los **Design Tokens** se organizan en **tres niveles jerárquicos**, cada uno con un propósito y un ámbito de uso específico:

**Tokens globales (opciones primitivas):** Son los valores más básicos y atómicos. No tienen significado semántico, solo representan opciones disponibles en la paleta. Ejemplos:
- `--color-blue-500: #3b82f6`
- `--color-red-500: #ef4444`
- `--font-size-16: 1rem`
- `--spacing-16: 1rem`

!!! warning "Precaución"

    Estos tokens no deberían usarse directamente en componentes, porque si se decide cambiar el color primario de azul a verde, habría que modificar todos los componentes individualmente.

**Tokens de alias (semánticos):** Mapean los tokens globales a significados funcionales en el contexto de la aplicación. Son el nivel que los componentes deben consumir:
- `--color-primary: var(--color-blue-600)`
- `--color-success: var(--color-green-600)`
- `--color-text-primary: var(--color-gray-900)`
- `--color-text-secondary: var(--color-gray-500)`

Si el color primario cambia de azul a verde, solo se modifica la definición del alias, y todos los componentes que usan `--color-primary` se actualizan automáticamente. ==Esta indirección es la clave de la flexibilidad de un Design System==.

**Tokens de componente:** Valores específicos para componentes concretos que heredan de los tokens semánticos pero pueden sobrescribirse:
- `--button-primary-bg: var(--color-primary)`
- `--button-primary-text: var(--color-white)`
- `--card-padding-x: var(--spacing-6)`
- `--card-border-radius: var(--radius-xl)`

#### Implementación en Tailwind 4 con @theme

**Tailwind 4** introduce la directiva `@theme` que permite definir tokens directamente en CSS, reemplazando el antiguo archivo de configuración `tailwind.config.js`. Los tokens definidos en `@theme` se integran automáticamente con el motor de clases utilitarias y están disponibles mediante la función `theme()`:

```
/* styles/tokens.css */
@import "tailwindcss";

@theme {
  /* Colores semanticos */
  --color-primary: var(--color-blue-600);
  --color-primary-light: var(--color-blue-50);
  --color-primary-dark: var(--color-blue-700);
  --color-surface: var(--color-white);
  --color-surface-secondary: var(--color-gray-50);
  --color-text-primary: var(--color-gray-900);
  --color-text-secondary: var(--color-gray-500);
  --color-text-disabled: var(--color-gray-400);
  --color-border: var(--color-gray-200);
  --color-border-focus: var(--color-blue-500);
}

/* En componentes: usar las clases generadas automaticamente */
/* bg-primary, text-primary, border-primary, etc. */
```

#### Tokens en TypeScript

En ocasiones, los tokens de diseño necesitan estar disponibles en la lógica TypeScript del componente (por ejemplo, para pasarlos como datos a una librería de gráficos, para configurar colores de un canvas, o para animaciones procedurales). Para estos casos, se define un archivo de tokens en TypeScript que replica la misma información que el CSS:

```
// design-system/tokens.ts
export const tokens = {
  colors: {
    primary: {
      50: '#eff6ff',
      100: '#dbeafe',
      500: '#3b82f6',
      600: '#2563eb',
      700: '#1d4ed8',
    },
    success: '#059669',
    warning: '#d97706',
    error: '#dc2626',
  },
  spacing: {
    1: '0.25rem',
    2: '0.5rem',
    4: '1rem',
    6: '1.5rem',
    8: '2rem',
  },
  fontSize: {
    xs: '0.75rem',
    sm: '0.875rem',
    base: '1rem',
    lg: '1.125rem',
    xl: '1.25rem',
  },
  borderRadius: {
    sm: '0.375rem',
    md: '0.5rem',
    lg: '0.75rem',
    xl: '1rem',
  },
  shadow: {
    sm: '0 1px 2px 0 rgb(0 0 0 / 0.05)',
    md: '0 4px 6px -1px rgb(0 0 0 / 0.1)',
    lg: '0 10px 15px -3px rgb(0 0 0 / 0.1)',
  },
} as const;
```

!!! tip "Consejo"

    Para mantener la sincronización entre los tokens CSS y TypeScript, se pueden utilizar herramientas como **Style Dictionary**, que genera ambos formatos a partir de una única fuente en JSON o YAML.

#### Sincronización Figma ↔ Código

La sincronización entre Figma (diseño) y el código (Tailwind + Angular) es uno de los mayores desafíos en la implementación de Design Systems. Existen varias estrategias y herramientas:

**Figma Tokens (plugin):** Este plugin permite definir Design Tokens directamente en Figma y exportarlos a formato JSON. Luego, herramientas como Style Dictionary pueden transformar ese JSON en variables CSS de Tailwind y en el archivo `tokens.ts` de TypeScript. El flujo es: Figma → JSON → Style Dictionary → CSS + TypeScript.

**Variables de Figma:** Las variables nativas de Figma (introducidas en 2023) permiten definir tokens directamente en la herramienta de diseño. A través de la API REST de Figma, se pueden extraer estas variables y transformarlas a código mediante scripts automatizados.

**Workflow bidireccional ideal:**
1. Los diseñadores definen/actualizan tokens en Figma (usando Figma Tokens o Variables).
2. Un pipeline de CI/CD (GitHub Actions) ejecuta un script que: extrae los tokens de Figma vía API, los transforma a CSS (@theme) y TypeScript usando Style Dictionary, y crea un Pull Request automático con los cambios.
3. Los desarrolladores revisan y aprueban el PR, integrando los tokens actualizados.
4. Los componentes Angular consumen los nuevos tokens automáticamente gracias a Tailwind y al archivo `tokens.ts`.

### SECCIÓN D — CONSTRUCCIÓN DE UN DESIGN SYSTEM PASO A PASO

#### Paso 1: Auditoría de interfaz

La auditoría consiste en inventariar sistemáticamente todos los elementos visuales existentes en la aplicación. El objetivo es identificar:
- **Colores utilizados** (muchas veces hay 15 azules ligeramente diferentes).
- **Tamaños de fuente** y familias tipográficas presentes.
- **Tipos de botones** y sus variaciones visuales.
- **Tipos de tarjetas**, modales, formularios.
- **Patrones de espaciado** utilizados (márgenes, paddings).
- **Inconsistencias**: elementos que deberían ser iguales pero son diferentes.

**Herramientas para la auditoría**: capturas de pantalla de todas las pantallas, extensión "CSS Peeper" para extraer estilos, e inspección manual con DevTools. El resultado de la auditoría es un documento que lista todos los hallazgos y las inconsistencias detectadas.

#### Paso 2: Definir principios de diseño

Los principios de diseño son 3-5 frases que resumen los valores que guiarán las decisiones del Design System. Ejemplos de principios comunes:

- **"Claridad ante todo":** La interfaz debe comunicar la información de forma inequívoca. Si un elemento puede malinterpretarse, debe rediseñarse.
- **"Accesibilidad por defecto":** Todo componente debe cumplir WCAG AA desde su primera implementación. La accesibilidad no es opcional ni un añadido posterior.
- **"Consistencia, no uniformidad":** Elementos similares deben comportarse de forma similar, pero la consistencia no debe sacrificar la usabilidad específica de cada contexto.
- **"Menos es más":** Ante la duda, eliminar. Cada elemento en pantalla debe justificar su presencia.
- **"Progressive enhancement":** La funcionalidad básica debe funcionar en todos los navegadores y dispositivos; las mejoras visuales y de interacción se añaden progresivamente.

#### Paso 3: Definir Design Tokens

Con la auditoría completada, se procede a consolidar todos los valores en un conjunto coherente de tokens:
- **Consolidar colores**: elegir una paleta principal con escalas de 50 a 950 para cada matiz, definir colores semánticos (primary, success, warning, error, info) y colores de superficie y texto.
- **Definir la escala tipográfica**: elegir una o dos familias tipográficas, definir la escala modular de tamaños y sus pesos y alturas de línea asociados.
- **Definir la escala de espaciado**: baseline grid de 4px u 8px, definiendo los valores de spacing desde 1 (4px) hasta 16 (64px) o más.
- **Definir sombras/elevación** (1-5 niveles) y **bordes redondeados** (escala de 3 valores: sm, md, lg).

#### Paso 4: Implementar tokens en Tailwind

Crear el archivo `design-system/tokens.css` con la directiva `@theme` de Tailwind 4 que contiene todos los tokens definidos. Importar este archivo en el `styles.css` global:

```
/* styles.css */
@import './app/design-system/tokens.css';

/* Estilos base para elementos HTML (atomos de tipografia) */
@layer base {
  h1 { font-size: var(--font-size-3xl); font-weight: 700; line-height: 1.2; }
  h2 { font-size: var(--font-size-2xl); font-weight: 600; line-height: 1.3; }
  h3 { font-size: var(--font-size-xl); font-weight: 600; line-height: 1.4; }
  body { font-family: var(--font-family-sans); color: var(--color-text-primary); }
}
```

#### Paso 5: Construir componentes atómicos

!!! warning "Precaución"

    Comenzar por los componentes más básicos (Botón, Input, Badge, Avatar, Icon) y construirlos siguiendo estrictamente los tokens definidos. Cada componente debe usar exclusivamente las clases de Tailwind generadas a partir de los tokens, nunca valores hardcodeados como `#3b82f6` o `16px`.

#### Paso 6: Construir componentes moleculares y organismos

Con la base atómica sólida, construir las moléculas (FormField, SearchBar, NavItem) y los organismos (Header, Sidebar, DataTable, ProductForm) componiendo los átomos y moléculas ya existentes.

#### Paso 7: Documentar en Storybook

Cada componente debe documentarse en Storybook con:
- **Descripción** del propósito y uso del componente.
- **Stories** para cada variante y estado.
- **Tabla** de inputs, outputs y slots de contenido.
- **Notas de accesibilidad**.
- **Código de ejemplo** listo para copiar y pegar.

#### Paso 8: Versionar y mantener

El Design System es un **producto vivo** que evoluciona con la aplicación. Debe versionarse semánticamente (MAJOR.MINOR.PATCH):
- **MAJOR:** Cambios que rompen la compatibilidad (eliminación de un componente, cambio en la API de inputs).
- **MINOR:** Nuevos componentes o nuevas variantes en componentes existentes.
- **PATCH:** Corrección de bugs visuales o de accesibilidad.

!!! tip "Consejo"

    Cada cambio debe documentarse en un **CHANGELOG** y comunicarse al equipo. Las deprecaciones deben anunciarse con al menos una versión de antelación, ofreciendo una migración clara.

### SECCIÓN E — ESCALAS Y SISTEMAS

#### Escala tipográfica

!!! info "Definición"

    Una **escala tipográfica** define un conjunto limitado y armonioso de tamaños de fuente. La **escala modular** (basada en una razón matemática, comúnmente 1.25 o 1.333) produce tamaños que guardan una relación proporcional entre sí, creando un ritmo visual agradable.

Escala modular típica (razón 1.25):
```
xs:   12px  (0.75rem)   — Texto auxiliar, notas legales
sm:   14px  (0.875rem)  — Texto de cuerpo pequeño, labels
base: 16px  (1rem)      — Texto de cuerpo principal
lg:   18px  (1.125rem)  — Texto de cuerpo destacado
xl:   20px  (1.25rem)   — Subtítulos
2xl:  24px  (1.5rem)    — Títulos de sección
3xl:  30px  (1.875rem)  — Títulos de página (H1)
4xl:  36px  (2.25rem)   — Títulos principales (Hero)
5xl:  48px  (3rem)      — Títulos de landing page
6xl:  60px  (3.75rem)   — Títulos muy grandes (marketing)
7xl:  72px  (4.5rem)    — Super-títulos
```

#### Escala de espaciado (baseline grid)

El **baseline grid** establece que todos los espacios verticales y horizontales deben ser múltiplos de una **unidad base (normalmente 4px)**. Esto garantiza un ritmo vertical consistente y alineación perfecta entre columnas y elementos.

Escala de espaciado base 4px:
```
Token     REM        PX       Uso
spacing-1  0.25rem    4px     Espacio mínimo entre icono y texto
spacing-2  0.5rem     8px     Padding interior pequeño, gap entre badges
spacing-3  0.75rem   12px     Padding interior de inputs
spacing-4  1rem      16px     Padding de tarjetas, margen entre párrafos
spacing-5  1.25rem   20px     Margen entre secciones pequeñas
spacing-6  1.5rem    24px     Padding de tarjetas grandes
spacing-8  2rem      32px     Margen entre secciones
spacing-10 2.5rem    40px     Margen de página
spacing-12 3rem      48px     Separación entre grandes bloques
spacing-16 4rem      64px     Márgenes de layout en desktop
```

#### Paletas de color

Cada color en el Design System debe tener una **escala completa (50-950)** que permita seleccionar el tono adecuado según el contexto. Las escalas se definen matemáticamente para que cada paso sea perceptiblemente diferente del anterior.

Estructura de paleta semántica:
```
primary:    blue-600      — Acciones principales, enlaces, elementos activos
success:    green-600     — Confirmaciones, estados positivos
warning:    yellow-600    — Advertencias, estados de atención
error:      red-600       — Errores, acciones destructivas
info:       blue-500      — Información, estados neutrales
```

Además de los colores semánticos, se necesitan **colores de superficie y texto**:
```
surface:         white        — Fondo principal
surface-secondary: gray-50    — Fondo secundario (filas alternas, aside)
surface-tertiary: gray-100    — Fondo terciario (hover, seleccionado)
text-primary:    gray-900     — Texto principal
text-secondary:  gray-500     — Texto secundario, placeholders
text-disabled:   gray-400     — Texto deshabilitado
border:          gray-200     — Bordes
border-focus:    blue-500     — Borde en foco
```

#### Escala de sombras

Las sombras comunican **elevación y jerarquía**. Una escala de 1 a 5 niveles, de menor a mayor elevación, es suficiente para la mayoría de aplicaciones:

```
Nivel 1 (sm):   0 1px 2px 0 rgb(0 0 0 / 0.05)           — Tarjetas, inputs
Nivel 2 (md):   0 4px 6px -1px rgb(0 0 0 / 0.1)         — Tarjetas con hover, dropdowns
Nivel 3 (lg):   0 10px 15px -3px rgb(0 0 0 / 0.1)       — Modales, paneles desplegables
Nivel 4 (xl):   0 20px 25px -5px rgb(0 0 0 / 0.1)       — Modales grandes, drawers
Nivel 5 (2xl):  0 25px 50px -12px rgb(0 0 0 / 0.25)     — Solo para elementos muy destacados
```

#### Border radius

Una escala de **4-5 valores** cubre todas las necesidades de redondeo:

```
sm:    0.375rem (6px)   — Checkboxes, badges pequeños
md:    0.5rem (8px)     — Botones, inputs, tabs
lg:    0.75rem (12px)   — Tarjetas, modales, dropdowns
xl:    1rem (16px)      — Tarjetas grandes, contenedores principales
full:  9999px           — Elementos circulares (avatares, badges circulares)
```

### SECCIÓN F — CASOS REALES DE DESIGN SYSTEMS

#### Material Design 3 (Google)

**Material Design 3 (Material You)** representa la evolución más reciente del sistema de diseño de Google. Sus características distintivas incluyen:
- **Dynamic Color:** Extrae colores del wallpaper del usuario y genera automáticamente una paleta de colores completa (primario, secundario, terciario, neutral y sus variantes), demostrando el poder de los tokens semánticos.
- **Tokens en 3 niveles:** Reference tokens (valores crudos de color, tipografía, forma), System tokens (mapeo semántico de los reference tokens al contexto), y Component tokens (valores específicos de cada componente Material).
- **Tipografía:** Escala de 15 tamaños agrupados en 5 categorías (Display, Headline, Title, Body, Label), cada una con 3 tamaños.
- **Forma (Shape):** Sistema de redondeo con 4 familias (none, extra small, small, medium, large, extra large, full) aplicables a 3 categorías de componentes.

Lecciones para nuestro Design System:
- La separación en **3 niveles de tokens** es muy poderosa y debería adoptarse.
- La generación dinámica de temas a partir de una semilla de color demuestra la importancia de los tokens semánticos.
- La documentación exhaustiva y las guías de uso son tan importantes como los componentes mismos.

#### Ant Design (Alibaba)

**Ant Design** es el sistema de diseño enterprise más popular del mundo, creado por Alibaba. Sus características:
- **Enfoque enterprise:** Diseñado para aplicaciones de gestión con mucha densidad de datos: tablas complejas, formularios extensos, flujos de trabajo.
- **Sistema de 10 colores:** Paleta con 12 tonos por color, más colores funcionales (success, warning, error, info, link).
- **Componentes de alto nivel:** Más de 60 componentes que cubren casos de uso enterprise (Transfer, Cascader, ProTable, ProForm).
- **Internacionalización integrada:** Todos los componentes soportan i18n como ciudadano de primera clase.

Lecciones: La densidad de información no está reñida con un diseño limpio si se gestiona adecuadamente el espaciado, el color y la jerarquía tipográfica. Ant Design demuestra que las aplicaciones de datos pueden ser visualmente agradables.

#### Carbon (IBM)

**Carbon** es el sistema de diseño open-source de IBM, orientado a productos enterprise con un fuerte énfasis en accesibilidad e inclusión:
- **Accesibilidad como requisito fundamental:** Cada componente está diseñado y testeado para cumplir WCAG AA, con documentación específica de accesibilidad.
- **Sistema de grid 2x:** El grid de Carbon usa el concepto de "2x grid" donde cada unidad de grid es 8px, y todo el layout se construye sobre múltiplos de 8.
- **Temas:** Soporte para 4 temas (White, Gray 10, Gray 90, Gray 100) que cubren desde claro hasta oscuro extremo.
- **Data visualization:** Componentes específicos para gráficos y visualizaciones de datos, un área que muchos Design Systems descuidan.

Lecciones: ==La accesibilidad debe ser un pilar fundacional, no un añadido==. El sistema de grid 2x (8px) es superior al tradicional 4px para aplicaciones enterprise porque reduce las opciones y fuerza decisiones más consistentes.

#### Spectrum (Adobe)

**Spectrum** es el sistema de diseño de Adobe para sus productos Creative Cloud y Experience Cloud. Sus características:
- **Multiplataforma:** Diseñado para funcionar en web, desktop y mobile con adaptaciones específicas para cada plataforma pero manteniendo el lenguaje visual.
- **Escala de títulos y cuerpos separadas:** Spectrum distingue entre "heading" (para títulos) y "body" (para texto de lectura), con escalas diferentes.
- **Sistema de slots visuales:** Componentes como Card, Dialog y Popover tienen "slots" predefinidos (imagen, encabezado, cuerpo, acciones) que guían la composición.

Lecciones: La distinción entre plataformas es importante; un botón en web puede necesitar 40px de altura mínima (para touch), mientras que en desktop 32px es suficiente. El Design System debe contemplar estas diferencias.

#### Lightning (Salesforce)

**Lightning Design System** es la base de todas las interfaces de Salesforce. Su enfoque:
- **Consistencia ecosistema:** Cientos de aplicaciones construidas por equipos diferentes deben verse y comportarse como una sola.
- **Componentes accesibles e internacionalizados:** Todo componente funciona con lectores de pantalla y soporta RTL (right-to-left) y traducción.
- **Sistema de iconos:** Más de 500 iconos SVG personalizados y categorizados, disponibles como componentes o como URLs de sprite.

Lecciones: Para grandes ecosistemas, la **gobernanza** del Design System es tan importante como su implementación técnica. Se necesita un proceso claro de contribución, revisión y aprobación de cambios.

### SECCIÓN G — THEME PROVIDER

El **ThemeProvider** es el mecanismo que permite cambiar el tema visual de toda la aplicación en tiempo real (claro ↔ oscuro, o entre diferentes paletas corporativas). En Angular, se implementa como un servicio con **Signals** que manipula clases CSS a nivel de documento y, opcionalmente, variables CSS.

#### Implementación del ThemeService

```
@Injectable({ providedIn: 'root' })
export class ThemeService {
  private readonly THEME_KEY = 'app-theme';

  private themeSignal = signal<'light' | 'dark' | 'high-contrast'>(
    this.loadInitialTheme()
  );
  currentTheme = this.themeSignal.asReadonly();

  // Opcional: color primario personalizable
  private primaryColorSignal = signal('#2563eb');
  primaryColor = this.primaryColorSignal.asReadonly();

  constructor() {
    this.applyTheme(this.themeSignal());
  }

  setTheme(theme: 'light' | 'dark' | 'high-contrast'): void {
    this.themeSignal.set(theme);
    this.applyTheme(theme);
    localStorage.setItem(this.THEME_KEY, theme);
  }

  toggleTheme(): void {
    const next = this.themeSignal() === 'dark' ? 'light' : 'dark';
    this.setTheme(next);
  }

  setPrimaryColor(color: string): void {
    this.primaryColorSignal.set(color);
    document.documentElement.style.setProperty('--color-primary', color);
  }

  private applyTheme(theme: string): void {
    const root = document.documentElement;

    // Limpiar clases de tema anteriores
    root.classList.remove('light', 'dark', 'high-contrast');
    root.classList.add(theme);

    // Establecer color-scheme CSS para barras nativas del navegador
    root.style.colorScheme = theme === 'dark' ? 'dark' : 'light';
  }

  private loadInitialTheme(): 'light' | 'dark' | 'high-contrast' {
    const stored = localStorage.getItem(this.THEME_KEY) as any;
    if (stored && ['light', 'dark', 'high-contrast'].includes(stored)) {
      return stored;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
}
```

#### Uso de variables CSS para temas

En lugar de depender exclusivamente del selector `.dark` de Tailwind, se pueden usar **variables CSS** para definir los colores del tema y luego cambiarlas con JavaScript cuando el tema cambia:

```
/* tokens.css - Definicion de variables para temas */
@theme {
  --color-surface: var(--surface-color);
  --color-text-primary: var(--text-primary-color);
  --color-border: var(--border-color);
}

/* Tema claro (por defecto) */
:root, .light {
  --surface-color: #ffffff;
  --text-primary-color: #111827;
  --border-color: #e5e7eb;
}

/* Tema oscuro */
.dark {
  --surface-color: #1f2937;
  --text-primary-color: #f9fafb;
  --border-color: #374151;
}

/* Tema high-contrast */
.high-contrast {
  --surface-color: #000000;
  --text-primary-color: #ffffff;
  --border-color: #ffffff;
}
```

#### Componente ThemeToggle

```
@Component({
  selector: 'ui-theme-toggle',
  standalone: true,
  template: `
    <button
      type="button"
      class="rounded-lg p-2 text-gray-500 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700"
      (click)="themeService.toggleTheme()"
      [attr.aria-label]="'Cambiar a modo ' + nextThemeLabel()">
      @if (themeService.currentTheme() === 'dark') {
        <!-- Icono sol -->
        <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
        </svg>
      } @else {
        <!-- Icono luna -->
        <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
        </svg>
      }
    </button>
  `,
})
export class ThemeToggleComponent {
  themeService = inject(ThemeService);

  nextThemeLabel = computed(() =>
    this.themeService.currentTheme() === 'dark' ? 'claro' : 'oscuro'
  );
}
```

---

## Ejemplos guiados

### Ejemplo guiado 1: Crear un Design System desde cero para una aplicación SaaS

**Objetivo:** Construir paso a paso todos los elementos de un Design System para una aplicación SaaS de gestión de proyectos, desde los tokens hasta los componentes base.

**Paso 1 — Auditoría visual de una app existente:** El docente proporciona capturas de una aplicación SaaS con múltiples pantallas (dashboard, lista de proyectos, detalle de proyecto, configuración). El alumnado identifica y lista todos los elementos visuales: colores (primario azul, éxito verde, error rojo, fondo gris claro, texto gris oscuro), tipografía (Inter para todo), tamaños de texto, tipos de tarjetas, botones (primario relleno azul, secundario outline, ghost para acciones de tabla), inputs y modales.

**Paso 2 — Definición de tokens:** A partir de la auditoría, se definen los tokens globales y semánticos. Se crea el archivo `tokens.css` con la directiva `@theme` de Tailwind 4.

**Paso 3 — Implementación de componentes atómicos:** Se construyen los componentes Button, Input/FormField, Badge, Avatar y Skeleton siguiendo estrictamente los tokens definidos.

**Paso 4 — Implementación de moléculas y organismos:** SearchBar, DataTable, Modal, EmptyState.

**Paso 5 — Documentación:** Cada componente se documenta con un archivo README.md provisional y se prepara para Storybook (Unidad 14).

### Ejemplo guiado 2: Implementar Atomic Design en Angular

**Objetivo:** Reorganizar un proyecto Angular existente para que refleje la estructura de Atomic Design.

**Desarrollo:** Partiendo de un proyecto con componentes desorganizados, el alumnado:
1. Identifica qué componentes son átomos, cuáles moléculas, cuáles organismos.
2. Reubica los componentes en la estructura de carpetas adecuada.
3. Asegura que los átomos no dependen de moléculas ni organismos.
4. Verifica el cumplimiento de la jerarquía de dependencias.

### Ejemplo guiado 3: Crear un ThemeProvider con múltiples temas

**Objetivo:** Implementar el `ThemeService` y `ThemeToggle` para soportar 3 temas (claro, oscuro, high-contrast).

**Desarrollo:**
1. Definir las variables CSS para los 3 temas en `tokens.css`.
2. Implementar `ThemeService` con Signals.
3. Crear `ThemeToggleComponent` con ciclo entre los 3 temas o toggle claro/oscuro.
4. Verificar que todos los componentes del Design System responden correctamente al cambio de tema.
5. Persistir la preferencia del usuario en `localStorage`.

---

## Actividades guiadas

### Actividad guiada 1: Auditoría visual de una aplicación web

**Duración:** 60 minutos.

**Objetivo:** Realizar una auditoría visual completa de una aplicación web existente para identificar todos sus elementos de diseño.

**Desarrollo:**
1. El docente proporciona la URL de una aplicación web real (puede ser una demo de un template de SaaS).
2. El alumnado, en equipos de 2, navega por al menos 5 pantallas diferentes y documenta:
   - Todos los colores utilizados (fondo, texto, primario, secundario, error, éxito, bordes).
   - Todas las familias y tamaños tipográficos encontrados.
   - Tipos de botones y sus variantes.
   - Tipos de tarjetas, modales y contenedores.
   - Espaciados (márgenes entre secciones, padding de tarjetas).
   - Inconsistencias detectadas (mismo elemento con diferente estilo en distintas pantallas).
3. El alumnado presenta sus hallazgos en una tabla y propone una paleta consolidada de colores y tipografía.

**Entregable:** Documento de auditoría visual con capturas y tabla de hallazgos.

### Actividad guiada 2: Definir Design Tokens para una aplicación de e-commerce

**Duración:** 90 minutos.

**Objetivo:** Definir el conjunto completo de Design Tokens para una aplicación de comercio electrónico.

**Desarrollo:**
1. A partir de un briefing de diseño (proporcionado por el docente), el alumnado define:
   - Paleta de colores completa (primarios, semánticos, superficie, texto, borde).
   - Escala tipográfica (familia, tamaños, pesos, alturas de línea).
   - Escala de espaciado (baseline grid de 4px).
   - Escala de sombras (1-5 niveles de elevación).
   - Escala de border radius (3-4 valores).
   - Animaciones: duraciones y curvas de easing estándar.
2. Implementar los tokens en dos formatos: CSS con `@theme` de Tailwind 4 y TypeScript (`tokens.ts`).
3. Verificar que los tokens TypeScript y CSS están sincronizados (mismos nombres, mismos valores).

**Entregable:** Archivos `tokens.css` y `tokens.ts` completos y sincronizados.

### Actividad guiada 3: Construir un ThemeProvider con 3 temas

**Duración:** 60 minutos.

**Objetivo:** Implementar un sistema de temas múltiples usando el patrón de ThemeService con Signals.

**Desarrollo:**
1. Implementar `ThemeService` (como se muestra en la Sección G).
2. Crear `ThemeToggleComponent` con selector de 3 temas (no solo toggle binario).
3. Definir variables CSS para los 3 temas en `tokens.css`.
4. Probar el cambio de tema en tiempo real en una página de demostración.
5. Persistir la preferencia en `localStorage` y respetar `prefers-color-scheme`.

**Entregable:** `ThemeService`, `ThemeToggleComponent` y `tokens.css` con soporte multi-tema.

---

## Actividades propuestas

### Actividad propuesta 1: Construir un Design System completo para una aplicación de banca digital

**Duración:** 300 minutos.

**Descripción:** Diseñar e implementar un Design System completo para una aplicación de banca digital ficticia.

**Requisitos:**
- Definir al menos 30 Design Tokens organizados en 3 niveles (globales, semánticos, de componente).
- Implementar 8 componentes atómicos: Button (5 variantes), Input (5 estados), Card (3 variantes), Badge (5 tipos), Avatar, Modal, Tabs, y DataTable.
- Todos los componentes deben estar correctamente tematizados (responder a los temas claro, oscuro y high-contrast aplicando solo las clases de Tailwind generadas).
- Crear un `ThemeService` que permita cambiar entre los 3 temas.
- Implementar un ThemeProvider (componente wrapper opcional) que aplique el tema a sus hijos mediante CSS custom properties.
- Documentar la API de cada componente (inputs, outputs, slots) en formato JSDoc y en un README.md.

**Entregable:** Proyecto Angular con el Design System completo en la carpeta `design-system/` y los componentes en `shared/components/`.

### Actividad propuesta 2: Sincronizar Design Tokens entre Figma y código con Style Dictionary

**Duración:** 150 minutos.

**Descripción:** Implementar un pipeline automatizado que extraiga Design Tokens desde Figma y los transforme a CSS y TypeScript usando Style Dictionary.

**Requisitos:**
- Definir los tokens en Figma usando el plugin "Figma Tokens" o las Variables nativas.
- Exportar los tokens a un archivo JSON.
- Configurar Style Dictionary para transformar el JSON a: variables CSS de Tailwind 4 (@theme), archivo TypeScript de tokens, y documentación en Markdown.
- Crear un script npm (`npm run build:tokens`) que ejecute la transformación.
- Documentar el flujo de trabajo para que otros desarrolladores puedan replicarlo.

**Entregable:** Configuración de Style Dictionary, script de build, archivos generados y documentación del flujo.

### Actividad propuesta 3: Implementar Atomic Design en un proyecto Angular existente

**Duración:** 120 minutos.

**Descripción:** Refactorizar un proyecto Angular existente (proporcionado por el docente) aplicando la metodología Atomic Design.

**Requisitos:**
- Clasificar todos los componentes existentes como átomos, moléculas u organismos.
- Reorganizar la estructura de carpetas del proyecto para reflejar esta clasificación.
- Asegurar que los componentes atómicos no dependen de moléculas ni organismos.
- Identificar componentes que deberían dividirse (violan SRP) y proponer una refactorización.
- Documentar la nueva estructura y la justificación de cada decisión.

**Entregable:** Proyecto refactorizado y documento de análisis.

### Actividad propuesta 4: Crear un Theme Switcher avanzado con previsualización

**Duración:** 120 minutos.

**Descripción:** Construir un componente de configuración de tema que permita al usuario personalizar visualmente los colores primarios y ver los cambios en tiempo real.

**Requisitos:**
- Panel de configuración con: selector de tema (claro, oscuro, sistema), color picker para el color primario, selector de radio de borde (sharp, rounded, pill), y selector de densidad (compact, default, comfortable).
- Previsualización en tiempo real: una miniatura de la aplicación que muestra los cambios instantáneamente.
- Los cambios se aplican al tema global mediante el ThemeService.
- Las preferencias se persisten en localStorage.
- Botón "Restablecer valores por defecto".

**Entregable:** `ThemeConfigComponent` con panel de configuración y previsualización.

### Actividad propuesta 5: Auditoría de accesibilidad del Design System

**Duración:** 90 minutos.

**Descripción:** Realizar una auditoría completa de accesibilidad sobre todos los componentes del Design System construido.

**Requisitos:**
- Evaluar cada componente contra los criterios WCAG 2.1 AA: contraste de color, navegación por teclado, etiquetas ARIA, foco visible, texto alternativo.
- Utilizar herramientas: axe DevTools, Lighthouse, y comprobación manual con lector de pantalla (NVDA en Windows o VoiceOver en macOS).
- Documentar los problemas encontrados, su severidad y la solución propuesta.
- Implementar las correcciones y verificar que los problemas han sido resueltos.

**Entregable:** Informe de auditoría de accesibilidad y componentes corregidos.

---

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Implementar un Theme Builder visual (WYSIWYG)

    **Duración:** 300 minutos.

    **Descripción:** Construir una herramienta visual que permita a diseñadores o desarrolladores crear nuevos temas para el Design System sin escribir código.

    **Requisitos:**
    - Interfaz visual con controles para modificar: color primario (con generación automática de la paleta completa), color de fondo, color de texto, familia tipográfica, radio de borde base, y densidad de espaciado.
    - Previsualización en vivo de una página de muestra con todos los componentes del Design System.
    - Exportación del tema creado a: archivo CSS de variables, archivo de configuración de Tailwind, y archivo JSON de tokens.
    - Los temas exportados deben ser directamente importables en el proyecto Angular.

    **Entregable:** Theme Builder funcional con al menos 3 temas de ejemplo exportados.

    ### Actividad de ampliación 2: Migrar un Design System de CSS tradicional a Tailwind 4

    **Duración:** 180 minutos.

    **Descripción:** Tomar un Design System existente implementado con CSS tradicional (clases BEM o similares) y migrarlo completamente a Tailwind 4 con Design Tokens.

    **Requisitos:**
    - Analizar el Design System de origen (proporcionado por el docente o uno público como Bootstrap).
    - Mapear todas las variables CSS y clases a tokens de Tailwind (@theme).
    - Reescribir los componentes usando exclusivamente clases utilitarias de Tailwind.
    - Verificar que el resultado visual es pixel-perfect comparado con el original.
    - Documentar el proceso de migración y las decisiones tomadas.

    **Entregable:** Design System migrado a Tailwind 4 + documento de migración.

    ### Actividad de ampliación 3: Crear un plugin de Figma para exportar componentes a Angular

    **Duración:** 240 minutos.

    **Descripción:** Desarrollar un plugin de Figma que, dado un componente de diseño seleccionado, genere automáticamente el código Angular correspondiente con Tailwind.

    **Requisitos:**
    - El plugin detecta las propiedades del componente en Figma: dimensiones, colores, tipografía, espaciado, bordes, sombras.
    - Mapea los estilos de Figma a tokens del Design System (si el componente usa estilos de Figma que coinciden con tokens definidos).
    - Genera un archivo TypeScript con el componente Angular (decorador, inputs/outputs deducidos de las variantes de Figma) y un template HTML con las clases de Tailwind correspondientes.
    - No se requiere generación 100% automática perfecta, pero sí una base sólida que un desarrollador pueda refinar.

    **Entregable:** Plugin de Figma funcional (puede ser en desarrollo, no necesariamente publicado) + documentación.

---

!!! tip "Buenas prácticas"

    1. **Una única fuente de verdad para los tokens.** Los valores de color, tipografía y espaciado deben definirse en un solo lugar (archivo de tokens CSS + TypeScript) y todo el código debe referenciarlos. Nunca usar valores literales como `#3b82f6` en componentes.

    2. **Tres niveles de tokens.** Mantener la jerarquía: tokens globales (paleta cruda) → tokens semánticos (significado funcional) → tokens de componente (específicos). Los componentes solo deben consumir tokens semánticos o de componente, nunca globales directamente.

    3. **Nombrar tokens por su función, no por su valor.** `--color-primary` es un buen nombre; `--color-blue-600` es un nombre de token global, no semántico. Si el azul cambia a verde, `primary` sigue teniendo sentido; `blue` no.

    4. **Versionar el Design System con semver.** Tratar el Design System como una librería software: MAJOR para breaking changes, MINOR para nuevas funcionalidades, PATCH para correcciones. Mantener un CHANGELOG.

    5. **Documentar el "por qué" de cada decisión de diseño.** No basta con mostrar el token o el componente; explicar por qué existe, cuándo usarlo y cuándo no. Esta información es invaluable para nuevos miembros del equipo.

    6. **Probar el tema oscuro desde el principio.** Diseñar el tema claro primero y luego "traducirlo" al oscuro es un error común que resulta en temas oscuros deficientes. Ambos temas deben diseñarse y probarse simultáneamente.

    7. **Mantener el Design System desacoplado de la aplicación.** Los tokens y componentes del Design System no deben importar nada de la aplicación (modelos, servicios de features, rutas). El Design System es un producto independiente que la aplicación consume.

    8. **WCAG AA como requisito mínimo.** Todo componente del Design System debe cumplir AA en contraste, navegación por teclado, y ARIA. Si un componente no cumple, no está terminado.

    9. **Los cambios en el Design System deben ser revisados por diseño y desarrollo.** Un cambio en un token o componente afecta a toda la aplicación. Establecer un proceso de revisión cruzada (design review + code review) antes de mergear cualquier cambio.

    10. **Proporcionar migraciones para breaking changes.** Si un cambio rompe la API de un componente, proporcionar una guía de migración clara y, cuando sea posible, un script automatizado que realice la migración.

---

!!! warning "Errores frecuentes"

    1. **Construir una librería de componentes y llamarla Design System.** Un Design System incluye componentes, pero también principios, tokens, patrones, documentación y gobernanza. Reducirlo a solo componentes es perder la mayor parte de su valor.

    2. **No separar tokens globales de tokens semánticos.** Si los componentes usan directamente `--color-blue-500` en lugar de `--color-primary`, cambiar el color primario de azul a verde requiere modificar decenas de componentes en lugar de un solo token.

    3. **Crear demasiados tokens demasiado pronto.** Definir tokens para cada posible valor lleva a un sistema inflado e inmanejable. Es mejor comenzar con los tokens mínimos necesarios e ir añadiendo según surjan necesidades reales.

    4. **Ignorar el tema oscuro hasta el final.** Añadir soporte para tema oscuro a posteriori es costoso y suele resultar en un tema oscuro de baja calidad. Todos los componentes deben diseñarse desde el principio con ambos temas en mente.

    5. **Romper la encapsulación atómica.** Un átomo no debe importar una molécula. Si `BadgeComponent` importa `ButtonComponent`, la jerarquía está rota y se generan dependencias circulares.

    6. **No testear los componentes en todos los temas y breakpoints.** Un componente que se ve bien en tema claro y desktop puede ser ilegible en tema oscuro o móvil. Testear cada variante en cada combinación de tema y viewport.

    7. **Usar medidas absolutas (px) en lugar de relativas (rem).** Los tokens de espaciado y tipografía deben estar en `rem` para respetar la configuración de zoom del usuario y las preferencias de tamaño de fuente del navegador.

    8. **Cambiar tokens sin revisar el impacto.** Modificar un token de espaciado o color puede causar efectos en cascada en docenas de componentes. Antes de cambiar un token, revisar todos los lugares donde se utiliza.

    9. **Sobrecargar los tokens de componente.** No es necesario crear un token para cada propiedad CSS de cada componente. Los tokens de componente deben reservarse para valores que realmente necesitan ser tematizables o variables.

    10. **Olvidar los estados de los componentes en el Design System.** Un Design System no está completo si solo define el estado default de cada componente. Debe incluir hover, active, focus, disabled, loading, error, success y empty.

---

!!! abstract "Resumen"

    Esta unidad ha cubierto la teoría y práctica de los Design Systems aplicados al desarrollo de interfaces con Angular y Tailwind:

    - Un **Design System** es un lenguaje visual compartido que abarca principios, Design Tokens, componentes, patrones, documentación y gobernanza, proporcionando consistencia, velocidad y escalabilidad.

    - La metodología **Atomic Design** de Brad Frost descompone las interfaces en átomos, moléculas, organismos, templates y páginas, proporcionando un marco que se alinea naturalmente con la arquitectura de componentes de Angular.

    - Los **Design Tokens** son la unidad atómica del sistema visual y se organizan en tres niveles: globales (valores crudos), semánticos (significado funcional) y de componente (específicos). En Tailwind 4 se implementan con la directiva `@theme`.

    - La **construcción de un Design System** sigue un proceso de 8 pasos: auditoría visual, definición de principios, definición de tokens, implementación en código, construcción de componentes atómicos, construcción de componentes compuestos, documentación y versionado.

    - Las **escalas** (tipográfica, espaciado, color, sombras, bordes) son la base matemática que garantiza un ritmo visual consistente y armonioso.

    - El estudio de **Design Systems reales** (Material Design 3, Ant Design, Carbon, Spectrum, Lightning) proporciona patrones y lecciones aplicables a nuestros propios sistemas.

    - El **ThemeProvider** implementado mediante un servicio Angular con Signals permite cambiar entre temas visuales en tiempo real, persistiendo la preferencia del usuario.

---

## Recursos complementarios

### Documentación oficial
- Tailwind CSS 4 — @theme directive: https://tailwindcss.com/docs/theme
- Angular — Style Guide: https://angular.dev/style-guide
- WCAG 2.1 (Web Content Accessibility Guidelines): https://www.w3.org/WAI/WCAG21/quickref/

### Herramientas
- Figma Tokens (plugin): https://www.figmatokens.com
- Style Dictionary: https://styledictionary.com (generación de tokens multi-plataforma)
- Storybook: https://storybook.js.org (documentación de componentes, Unidad 14)
- Chromatic: https://www.chromatic.com (testing visual y revisión de cambios)

### Libros
- "Atomic Design" — Brad Frost (gratuito online: https://atomicdesign.bradfrost.com)
- "Design Systems" — Alla Kholmatova (arquitectura y gobernanza de sistemas de diseño)
- "Refactoring UI" — Adam Wathan y Steve Schoger (diseño práctico con Tailwind)
- "Designing Design Systems" — Jina Anne

### Design Systems de referencia
- Material Design 3: https://m3.material.io
- Ant Design: https://ant.design
- Carbon Design System (IBM): https://carbondesignsystem.com
- Spectrum (Adobe): https://spectrum.adobe.com
- Lightning Design System (Salesforce): https://lightningdesignsystem.com
- Polaris (Shopify): https://polaris.shopify.com

### Artículos y guías
- "Design Tokens: What They Are and How to Use Them" — Adobe Spectrum Blog
- "Building a Design System with Angular and Tailwind" — Angular Addicts
- "The Anatomy of a Design System" — UX Collective
- "Design Tokens in Figma and Code" — Jan Six (Figma blog)
