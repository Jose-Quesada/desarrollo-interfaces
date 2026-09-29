---
icon: lucide/library
---

# Documentación de Componentes con Storybook

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:
- Instalar y configurar **Storybook** en un proyecto Angular con Standalone Components, TypeScript y Tailwind CSS 4.
- Escribir stories completas utilizando el formato **CSF3 (Component Story Format 3)** para documentar todas las variantes y estados de un componente.
- Utilizar los addons esenciales de Storybook: Controls, Actions, Viewport, Backgrounds, Accessibility, Interactions y Design (Figma).
- Crear documentación narrativa con **MDX** que combine texto explicativo, ejemplos de código y stories interactivas.
- Implementar testing de interacciones (play functions) y testing de accesibilidad automatizado en Storybook.
- Integrar Storybook con Figma para mantener sincronizados el diseño visual y los componentes desarrollados.
- Publicar un Storybook estático para compartir con el equipo de diseño y stakeholders.
- Configurar **Chromatic** para visual testing y detección de regresiones visuales.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 3** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 3.** Crea componentes visuales valorando y empleando herramientas específicas.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE a) Se han identificado las herramientas para diseño y prueba de componentes.
- CE e) Se han realizado pruebas unitarias sobre los componentes desarrollados.
- CE f) Se han documentado los componentes creados.

> Nota: la documentación de componentes con Storybook es también el vehículo técnico del **RA 6** («Documenta aplicaciones seleccionando y utilizando herramientas específicas»), en particular su CE e) «Se ha confeccionado el manual de usuario y la guía de referencia».

!!! note "Conocimientos previos"

    El alumnado debe poseer los siguientes conocimientos antes de abordar esta unidad:
    - **Angular**: Standalone Components, Signals, @Input/@Output, proyección de contenido, ciclo de vida (Unidades 10, 11 y 12).
    - **TypeScript**: tipos avanzados, genéricos, const assertions, satisfies operator.
    - **Tailwind CSS 4**: clases utilitarias, personalización con @theme, variantes (Unidad 6).
    - **Control de versiones con Git**: commits, ramas, Pull Requests.
    - **Nociones básicas de testing**: unit tests con Jest o Karma, concepto de snapshot testing.
    - **Markdown**: sintaxis básica y avanzada (tablas, bloques de código, enlaces).

## Contenidos

1. Fundamentos de Storybook
2. Instalación y configuración en proyecto Angular
3. Escritura de Stories con CSF3
4. Documentación con MDX
5. Addons esenciales
6. Testing con Storybook
7. Integración con Figma
8. Publicación y despliegue

## Desarrollo teórico

### SECCIÓN A — QUÉ ES STORYBOOK

!!! info "Definición"

    **Storybook** es una herramienta de desarrollo frontend que permite construir, documentar y testear componentes de interfaz de usuario de forma aislada, fuera del contexto de la aplicación completa. Funciona como un "taller" o "laboratorio" donde cada componente se presenta en un entorno controlado, con la capacidad de manipular sus propiedades (inputs) en tiempo real y observar su comportamiento en diferentes estados, tamaños de pantalla y condiciones visuales.

En el ecosistema profesional de desarrollo de interfaces, Storybook ocupa un lugar central por varias razones fundamentales:

**Desarrollo aislado (Component-Driven Development):** Con Storybook, un desarrollador puede trabajar en un componente (por ejemplo, un Button) sin necesidad de arrancar la aplicación completa ni navegar hasta la página donde se utiliza ese componente. El componente se renderiza en un iframe aislado, con todas sus dependencias resueltas y sin interferencias del resto de la aplicación. Esto acelera el ciclo de desarrollo (cambiar código → ver resultado → iterar) y reduce la carga cognitiva al centrarse en una sola pieza.

**Documentación viva:** A diferencia de la documentación estática (wikis, PDFs, READMEs) que inevitablemente queda desactualizada, ==las stories de Storybook son código que se ejecuta==. Si un componente cambia su API (se añade un input, se elimina un output), la story asociada fallará al compilar, forzando su actualización. Esto garantiza que la documentación siempre refleja el estado real de los componentes. La documentación vive y respira junto al código.

**Catálogo de componentes para todo el equipo:** Storybook sirve como un catálogo centralizado donde diseñadores, product managers, QA y otros stakeholders pueden explorar todos los componentes disponibles, ver sus variantes y estados, copiar ejemplos de código y comprender cómo usarlos. Esto reduce la dependencia de los desarrolladores para responder preguntas como "¿tenemos un componente de tabla con ordenación?" o "¿cómo se ve el botón en estado disabled?".

**Testing visual automatizado:** Storybook se integra con servicios como Chromatic o Percy que capturan una screenshot de cada story y la comparan píxel a píxel con versiones anteriores. Si un cambio en el código altera accidentalmente la apariencia de un componente (por ejemplo, un cambio en un token de color que afecta a 37 componentes), el testing visual lo detecta inmediatamente y muestra un diff visual. Esto es imposible de lograr con tests unitarios tradicionales, que verifican lógica pero no apariencia.

**Colaboración diseño-desarrollo:** Storybook cierra la brecha entre diseño y desarrollo de múltiples maneras: permite incrustar diseños de Figma junto a los componentes desarrollados (addon-designs), facilita que los diseñadores revisen la implementación y comparen con el diseño original, y establece un lenguaje común donde "Button/primary" significa lo mismo en Figma y en Storybook.

### SECCIÓN B — INSTALACIÓN Y CONFIGURACIÓN EN PROYECTO ANGULAR

#### Instalación automática

La forma más sencilla de añadir Storybook a un proyecto Angular existente es mediante el comando de inicialización automática, que detecta el framework y configura todo lo necesario:

```
npx storybook@latest init
```

Este comando realiza las siguientes acciones:
1. Detecta automáticamente que el proyecto es Angular (por la presencia de `angular.json`).
2. Instala las dependencias necesarias: `@storybook/angular`, `@storybook/addon-essentials`, `@storybook/addon-interactions` y sus peer dependencies.
3. Crea la carpeta `.storybook/` en la raíz del proyecto con dos archivos de configuración.
4. Añade scripts a `package.json`: `storybook` (para desarrollo) y `build-storybook` (para build estático).
5. Crea ejemplos de stories en `src/stories/` para que el desarrollador vea cómo funciona.

#### Archivos de configuración generados

**.storybook/main.ts** — Configuración principal de Storybook:

```
import type { StorybookConfig } from '@storybook/angular';

const config: StorybookConfig = {
  stories: ['../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  addons: [
    '@storybook/addon-essentials',
    '@storybook/addon-interactions',
    '@storybook/addon-a11y',
    '@storybook/addon-links',
    '@storybook/addon-designs',
  ],
  framework: {
    name: '@storybook/angular',
    options: {},
  },
  docs: {
    autodocs: 'tag',
  },
  staticDirs: ['../public'],
};

export default config;
```

- **stories:** Patrón glob que indica dónde se encuentran los archivos de stories. La configuración por defecto busca cualquier archivo `.stories.ts` o `.stories.tsx` en `src/`.
- **addons:** Lista de addons que se cargan. `@storybook/addon-essentials` incluye Controls, Actions, Viewport, Backgrounds, Toolbars y Docs. `@storybook/addon-interactions` permite testing de interacciones con play functions. `@storybook/addon-a11y` añade auditoría de accesibilidad. `@storybook/addon-designs` permite incrustar Figma.
- **framework:** Especifica el framework (Angular) y sus opciones.
- **docs:** Configuración de documentación automática. `autodocs: 'tag'` genera documentación automática para los componentes que tengan el tag `'autodocs'` en sus metadatos.

**.storybook/preview.ts** — Configuración global de cómo se renderizan las stories:

```
import type { Preview } from '@storybook/angular';
import { setProjectAnnotations } from '@storybook/angular';
import { applicationConfig } from '@storybook/angular';
import { provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';

// Importar Tailwind global
import '!style-loader!css-loader!postcss-loader!../src/styles.css';

const preview: Preview = {
  parameters: {
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/i,
      },
    },
    backgrounds: {
      default: 'light',
      values: [
        { name: 'light', value: '#ffffff' },
        { name: 'dark', value: '#1f2937' },
        { name: 'gray', value: '#f3f4f6' },
      ],
    },
    viewport: {
      viewports: {
        mobile: { name: 'Mobile', styles: { width: '375px', height: '812px' } },
        tablet: { name: 'Tablet', styles: { width: '768px', height: '1024px' } },
        desktop: { name: 'Desktop', styles: { width: '1280px', height: '800px' } },
        wide: { name: 'Wide', styles: { width: '1920px', height: '1080px' } },
      },
    },
  },
  decorators: [
    applicationConfig({
      providers: [
        provideZoneChangeDetection({ eventCoalescing: true }),
        provideHttpClient(),
        provideRouter([]),
      ],
    }),
  ],
  tags: ['autodocs'],
};

export default preview;
```

!!! warning "Atención"

    La línea `import '!style-loader!css-loader!postcss-loader!../src/styles.css'` es crucial: le dice a Storybook que cargue los estilos globales de la aplicación incluyendo el CSS de Tailwind. Sin esta línea, los componentes aparecerían sin estilos en Storybook. En Tailwind 4, el archivo `styles.css` contiene la directiva `@import "tailwindcss"` que carga todo el framework.

#### Integración con Tailwind 4

Para que Storybook procese correctamente **Tailwind 4**, es necesario asegurarse de que:
1. El archivo `styles.css` importado en `preview.ts` contiene `@import "tailwindcss"`.
2. El archivo de configuración de Storybook usa PostCSS (que ya viene configurado por defecto en proyectos Angular con Tailwind).
3. Si se usan tokens personalizados con `@theme`, el archivo que los define debe estar importado en `styles.css` para que Storybook los tenga disponibles.

#### Scripts NPM

El comando `npx storybook@latest init` añade estos scripts a `package.json`:

```
{
  "scripts": {
    "storybook": "storybook dev -p 6006",
    "build-storybook": "storybook build"
  }
}
```

- `npm run storybook` arranca el servidor de desarrollo en `http://localhost:6006` con hot reload.
- `npm run build-storybook` genera una versión estática lista para desplegar en cualquier hosting (GitHub Pages, Netlify, Vercel, Chromatic).

### SECCIÓN C — ESCRITURA DE STORIES CON CSF3

**CSF3** (Component Story Format 3) es el formato más reciente para escribir stories en Storybook. Introduce mejoras significativas respecto a CSF2: menos boilerplate, mejor inferencia de tipos, soporte para `satisfies` de TypeScript, y una API más limpia.

#### Estructura de un archivo de stories

Un archivo de stories típico para un componente Angular con CSF3 tiene la siguiente estructura:

```
import type { Meta, StoryObj } from '@storybook/angular';
import { ButtonComponent } from './button.component';

const meta: Meta<ButtonComponent> = {
  title: 'UI/Button',
  component: ButtonComponent,
  tags: ['autodocs'],
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'outline', 'ghost', 'danger'],
      description: 'Variante visual del botón',
    },
    size: {
      control: 'radio',
      options: ['sm', 'md', 'lg'],
      description: 'Tamaño del botón',
    },
    disabled: {
      control: 'boolean',
      description: 'Deshabilita el botón',
    },
    loading: {
      control: 'boolean',
      description: 'Muestra un spinner y deshabilita la interacción',
    },
    label: {
      control: 'text',
      description: 'Texto del botón',
    },
    clicked: {
      action: 'clicked',
      description: 'Se emite cuando el usuario hace click',
    },
  },
  args: {
    variant: 'primary',
    size: 'md',
    disabled: false,
    loading: false,
    label: 'Botón',
  },
  render: (args) => ({
    props: args,
  }),
};

export default meta;
type Story = StoryObj<ButtonComponent>;
```

Desglose de cada parte:

- **`meta: Meta<ButtonComponent>`:** Objeto de metadatos que describe el componente. Incluye el título (jerarquía en la barra lateral con `/`), el componente en sí, tags para configurar autodocs, y la configuración de argTypes y args.

- **`title: 'UI/Button'`:** Define la posición del componente en la barra lateral de navegación de Storybook. La barra `/` crea una jerarquía de carpetas: `UI` es la carpeta contenedora y `Button` es el componente. Otras convenciones comunes son `Atoms/Button`, `Molecules/SearchBar`, `Organisms/Header`.

- **`tags: ['autodocs']`:** Habilita la generación automática de documentación para este componente. Storybook analizará el componente (sus inputs, outputs, tipos) y generará automáticamente una tabla de argumentos y documentación básica.

- **`argTypes`:** Define los controles que aparecerán en el panel de Controls de Storybook. Cada propiedad del componente puede tener un control específico: `select` para opciones enumeradas, `radio` para pocas opciones, `boolean` para true/false, `text` para strings, `number` para números, `color` para colores, `date` para fechas. La propiedad `action` en un argType configura el panel de Actions para que muestre cada vez que el evento se emite.

- **`args`:** Valores por defecto que se aplican a todas las stories del componente. Pueden ser sobrescritos por stories individuales.

#### Creando stories para cada variante

Una vez definidos los metadatos, se crean las stories individuales, cada una representando una variante o estado del componente:

```
// Primary (usando los args por defecto)
export const Primary: Story = {};

// Secondary
export const Secondary: Story = {
  args: {
    variant: 'secondary',
    label: 'Cancelar',
  },
};

// Outline
export const Outline: Story = {
  args: {
    variant: 'outline',
    label: 'Ver más',
  },
};

// Ghost
export const Ghost: Story = {
  args: {
    variant: 'ghost',
    label: 'Editar',
  },
};

// Danger
export const Danger: Story = {
  args: {
    variant: 'danger',
    label: 'Eliminar cuenta',
  },
};

// Estados
export const Disabled: Story = {
  args: {
    disabled: true,
    label: 'Deshabilitado',
  },
};

export const Loading: Story = {
  args: {
    loading: true,
    label: 'Guardando...',
  },
};

// Con icono
export const WithIcon: Story = {
  args: {
    label: 'Descargar',
    icon: `<svg class="h-4 w-4" ...><!-- icono download --></svg>`,
  },
};

// Agrupación de variantes por tamaño
export const Small: Story = {
  args: {
    size: 'sm',
    label: 'Pequeño',
  },
};

export const Large: Story = {
  args: {
    size: 'lg',
    label: 'Grande',
  },
};
```

#### Stories para componentes con proyección de contenido

Para componentes que usan `<ng-content>` (como Card, Modal, Tabs), las stories deben proporcionar el contenido proyectado mediante la propiedad `render`:

```
const meta: Meta<CardComponent> = {
  title: 'UI/Card',
  component: CardComponent,
  tags: ['autodocs'],
  args: {
    variant: 'default',
    padding: 'md',
  },
};

export default meta;
type Story = StoryObj<CardComponent>;

export const Default: Story = {
  render: (args) => ({
    props: args,
    template: `
      <ui-card [variant]="variant" [padding]="padding">
        <h3 class="text-lg font-semibold">Título de la tarjeta</h3>
        <p class="text-gray-600">Contenido de ejemplo de la tarjeta con información relevante.</p>
      </ui-card>
    `,
  }),
};

export const WithHeaderAndFooter: Story = {
  render: (args) => ({
    props: args,
    template: `
      <ui-card>
        <div card-header>
          <h3 class="text-lg font-semibold">Tarjeta con header y footer</h3>
        </div>
        <p class="text-gray-600">Contenido principal de la tarjeta.</p>
        <div card-footer>
          <div class="flex justify-end gap-2">
            <ui-button variant="ghost" size="sm">Cancelar</ui-button>
            <ui-button variant="primary" size="sm">Aceptar</ui-button>
          </div>
        </div>
      </ui-card>
    `,
  }),
};
```

#### Stories para componentes con estado (Smart Components)

Para Smart Components que inyectan servicios y obtienen datos, se pueden crear stories mockeando los servicios mediante Angular providers en los decoradores:

```
const meta: Meta<DashboardPageComponent> = {
  title: 'Pages/Dashboard',
  component: DashboardPageComponent,
  decorators: [
    applicationConfig({
      providers: [
        {
          provide: DashboardService,
          useValue: {
            getStats: () => of(MOCK_STATS),
            getChartData: () => of(MOCK_CHART_DATA),
            getRecentTransactions: () => of(MOCK_TRANSACTIONS),
          },
        },
      ],
    }),
  ],
};
```

### SECCIÓN D — DOCUMENTACIÓN CON MDX

!!! info "Formato MDX"

    **MDX** es un formato de archivo que combina Markdown (para texto narrativo y documentación) con JSX (para insertar componentes React/Storybook interactivos). En Storybook, los archivos `.mdx` permiten crear páginas de documentación ricas que mezclan explicaciones, ejemplos de código, tablas de propiedades y stories interactivas.

#### Página de introducción del Design System con MDX

```
// src/stories/Introduction.mdx
import { Meta, Story, Canvas, Controls, Description } from '@storybook/blocks';

<Meta title="Introducción" />

# Bienvenido al Design System de MiApp

Este Design System contiene todos los componentes de interfaz de usuario utilizados en MiApp. Aquí encontrarás:

- **Componentes atómicos** como botones, inputs, badges y avatares.
- **Componentes moleculares** como campos de formulario, barras de búsqueda y elementos de navegación.
- **Organismos** como tablas de datos, modales y cabeceras.

## Principios de diseño

El Design System se rige por los siguientes principios:

1. **Consistencia:** Elementos similares deben verse y comportarse de forma similar.
2. **Accesibilidad:** Todo componente cumple WCAG 2.1 AA como mínimo.
3. **Simplicidad:** La API de cada componente debe ser intuitiva y predecible.
4. **Flexibilidad:** Los componentes se adaptan a diferentes contextos sin perder coherencia.

## Cómo usar este Storybook

- Navega por los componentes en la barra lateral izquierda.
- Usa el panel **Controls** para modificar propiedades en tiempo real.
- Cambia el **Viewport** para ver cómo se adaptan los componentes a distintos dispositivos.
- Consulta la pestaña **Docs** para ver la documentación completa de cada componente.
- Revisa la pestaña **Accessibility** para verificar el cumplimiento de estándares ARIA.

## Design Tokens

| Token | Valor | Uso |
|-------|-------|-----|
| `--color-primary` | `#2563eb` | Acciones principales, enlaces |
| `--color-success` | `#059669` | Estados positivos, confirmaciones |
| `--color-warning` | `#d97706` | Advertencias |
| `--color-error` | `#dc2626` | Errores, acciones destructivas |
| `--font-size-base` | `1rem` | Texto de cuerpo |
| `--spacing-4` | `1rem` | Padding estándar de componentes |

## Instalación y uso

Para usar un componente en tu feature, impórtalo desde `shared/components`:

```
import { ButtonComponent } from '@shared/components/button';

@Component({
  standalone: true,
  imports: [ButtonComponent],
  template: `
    <ui-button variant="primary" (clicked)="handleSave()">
      Guardar cambios
    </ui-button>
  `,
})
export class MyFeatureComponent {}
```
```

#### Documentación de componente con MDX + Stories incrustadas

```
// button.stories.mdx
import { Meta, Story, Canvas, Controls, Primary, Source } from '@storybook/blocks';
import * as ButtonStories from './button.stories';

<Meta of={ButtonStories} />

# Button

El componente `Button` es el bloque de construcción fundamental para las acciones del usuario. Soporta múltiples variantes, tamaños, estados y configuraciones de icono.

## Cuándo usar este componente

- Para **acciones principales** en formularios, modales y páginas.
- Para **acciones secundarias** que complementan una acción principal.
- Para **acciones de navegación** que llevan al usuario a otra página.
- Para **acciones destructivas** como eliminar o cancelar.

## Cuándo NO usar este componente

- Para **navegación entre páginas**: usa `routerLink` en un elemento `<a>` estilizado.
- Para **enlaces externos**: usa un `<a>` nativo con estilos de botón.

## Variantes

<Canvas of={ButtonStories.Primary} />
<Canvas of={ButtonStories.Secondary} />
<Canvas of={ButtonStories.Outline} />
<Canvas of={ButtonStories.Ghost} />
<Canvas of={ButtonStories.Danger} />

## Estados

<Canvas of={ButtonStories.Disabled} />
<Canvas of={ButtonStories.Loading} />

## Tamaños

<Canvas of={ButtonStories.Small} />
<Canvas of={ButtonStories.Primary} />
<Canvas of={ButtonStories.Large} />

## Con icono

<Canvas of={ButtonStories.WithIcon} />

## API del componente

<Controls />

## Accesibilidad

- El botón tiene `role="button"` implícito (es un `<button>` nativo).
- `aria-disabled` se usa en lugar de `disabled` para mantener el foco.
- `aria-busy="true"` cuando está en estado `loading`.
- Texto visible para lectores de pantalla durante la carga.
- Contraste de color verificado (WCAG AA).

## Código de ejemplo

```
<ui-button variant="primary" size="md" (clicked)="handleClick()">
  Guardar
</ui-button>
```
```

### SECCIÓN E — ADDONS ESENCIALES

#### @storybook/addon-essentials

Este addon es un paquete que incluye múltiples addons fundamentales preconfigurados:

- **Controls:** Panel que permite modificar los inputs (args) del componente en tiempo real mediante controles de formulario (selects, checkboxes, inputs de texto, color pickers). Es la funcionalidad más utilizada de Storybook.

- **Actions:** Panel que muestra en tiempo real los eventos emitidos por el componente (outputs en Angular). Cuando un componente emite un `@Output()`, el panel de Actions lo registra con los argumentos correspondientes, permitiendo verificar que los eventos se emiten correctamente y con los datos esperados.

- **Viewport:** Toolbar que permite cambiar el tamaño del viewport para simular diferentes dispositivos (móvil, tablet, desktop, pantalla ancha). Esencial para verificar la responsividad de los componentes.

- **Backgrounds:** Toolbar para cambiar el color de fondo del canvas, permitiendo probar cómo se ve el componente sobre fondos claros, oscuros y de colores.

- **Docs:** Generación automática de documentación a partir de los metadatos y las stories.

- **Toolbars:** Barras de herramientas contextuales configurables.

#### @storybook/addon-a11y

Este addon integra **axe-core** en Storybook y ejecuta automáticamente una auditoría de accesibilidad sobre cada story. Los resultados se muestran en un panel que lista las violaciones (violations), las buenas prácticas cumplidas (passes) y las revisiones manuales necesarias (incomplete).

Configuración básica en `main.ts`:

```
addons: ['@storybook/addon-a11y'],
```

En `preview.ts`, se puede configurar para que se ejecute automáticamente en todas las stories:

```
parameters: {
  a11y: {
    config: {
      rules: [
        { id: 'color-contrast', enabled: true },
        { id: 'button-name', enabled: true },
      ],
    },
    element: '#storybook-root',
  },
},
```

#### @storybook/addon-interactions

Permite escribir tests de interacción directamente en las stories mediante `play` functions. Una `play` function es una función async que simula interacciones del usuario (clicks, escritura, hover, navegación por teclado) y verifica el comportamiento resultante:

```
import { within, userEvent, expect } from '@storybook/test';
import type { Meta, StoryObj } from '@storybook/angular';
import { ButtonComponent } from './button.component';

const meta: Meta<ButtonComponent> = {
  title: 'UI/Button',
  component: ButtonComponent,
};

export default meta;
type Story = StoryObj<ButtonComponent>;

export const ClickInteraction: Story = {
  args: {
    label: 'Haz clic',
    variant: 'primary',
  },
  play: async ({ canvasElement, args }) => {
    const canvas = within(canvasElement);
    const button = canvas.getByRole('button', { name: /haz clic/i });

    // Verificar estado inicial
    await expect(button).toBeEnabled();
    await expect(button).toHaveTextContent('Haz clic');

    // Simular click
    await userEvent.click(button);
  },
};

export const KeyboardNavigation: Story = {
  args: {
    label: 'Teclado',
  },
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    const button = canvas.getByRole('button');

    await userEvent.tab();
    await expect(button).toHaveFocus();

    await userEvent.keyboard('{Enter}');
  },
};

export const DisabledNoInteraction: Story = {
  args: {
    label: 'Deshabilitado',
    disabled: true,
  },
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    const button = canvas.getByRole('button');

    await expect(button).toBeDisabled();

    // Verificar que no se puede hacer click
    await userEvent.click(button, { skipPointerEventsCheck: true });
    await expect(button).toBeDisabled();
  },
};
```

#### @storybook/addon-designs

Permite incrustar diseños de Figma (o URLs de imágenes) junto a los componentes en Storybook. El diseño aparece en una pestaña "Design" en el panel de addons:

```
const meta: Meta<ButtonComponent> = {
  title: 'UI/Button',
  component: ButtonComponent,
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/xxxxx/Design-System?node-id=42-123',
    },
  },
};
```

También se puede usar directamente en el archivo MDX:

```
import { Figma } from '@storybook/addon-designs/blocks';

<Figma url="https://www.figma.com/file/xxxxx/Design-System?node-id=42-123" />
```

#### @storybook/addon-links

Permite crear enlaces entre stories, facilitando la navegación entre componentes relacionados. Por ejemplo, desde la story de un FormField se puede enlazar a la story del Button que se usa como submit:

```
import { linkTo } from '@storybook/addon-links';

export const WithSubmitLink: Story = {
  args: { ... },
  play: async ({ canvasElement }) => {
    // Después de interactuar con el formulario, navegar a la story del botón
    await linkTo('UI/Button', 'Primary')();
  },
};
```

### SECCIÓN F — TESTING CON STORYBOOK

Storybook habilita tres niveles de testing que se complementan entre sí para garantizar la calidad de los componentes:

#### Testing de interacciones (Interaction Testing)

Las `play` functions ejecutan secuencias de interacciones del usuario y verifican el estado resultante. Se ejecutan en el navegador real (no en JSDOM), lo que significa que renderizan CSS, ejecutan animaciones y responden a eventos reales del DOM. Las `play` functions se ejecutan automáticamente como parte del proceso de build de Storybook y pueden integrarse en CI/CD.

#### Testing de accesibilidad (Accessibility Testing)

El addon `@storybook/addon-a11y` ejecuta axe-core automáticamente en cada story y reporta violaciones de accesibilidad. Puede configurarse para que falle el build si se detectan violaciones críticas. Ejemplo de configuración estricta:

```
// .storybook/test-runner.ts
import { getStoryContext } from '@storybook/test-runner';
import { injectAxe, checkA11y, configureAxe } from 'axe-playwright';

module.exports = {
  async preVisit(page, context) {
    await injectAxe(page);
  },
  async postVisit(page, context) {
    const storyContext = await getStoryContext(page, context);

    // Solo auditar componentes (no páginas de documentación)
    if (storyContext.component) {
      await configureAxe(page, {
        rules: [
          { id: 'color-contrast', enabled: true },
          { id: 'html-has-lang', enabled: true },
        ],
      });

      const violations = await checkA11y(page, '#storybook-root', {
        detailedReport: true,
        detailedReportOptions: { html: true },
      });

      expect(violations).toHaveLength(0);
    }
  },
};
```

#### Testing visual (Visual Testing)

**Chromatic** es el servicio de testing visual de Storybook (creado por los mismos desarrolladores). Funciona de la siguiente manera:

1. Por cada story, Chromatic captura una screenshot del componente renderizado.
2. Cuando se hace un Pull Request, Chromatic vuelve a capturar screenshots de todas las stories y las compara píxel a píxel con la versión base (main branch).
3. Si detecta diferencias, las muestra en una interfaz de revisión donde se puede aceptar el cambio (era intencionado) o rechazarlo (es una regresión).
4. Los revisores (diseñadores y desarrolladores) aprueban o rechazan los cambios visuales.

Configuración de Chromatic:

```
npm install --save-dev chromatic
npx chromatic --project-token=<token>
```

La ejecución se integra fácilmente en GitHub Actions u otras plataformas de CI/CD:

```
# .github/workflows/chromatic.yml
name: Chromatic
on: push
jobs:
  chromatic:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npx chromatic --project-token=${{ secrets.CHROMATIC_TOKEN }}
```

#### Snapshot testing

El test runner de Storybook también puede generar snapshot tests comparando el HTML renderizado de cada story:

```
// .storybook/test-runner.ts
import { expect } from '@storybook/jest';

module.exports = {
  async postVisit(page, context) {
    const elementHandler = await page.$('#storybook-root');
    const innerHTML = await elementHandler.innerHTML();
    expect(innerHTML).toMatchSnapshot();
  },
};
```

### SECCIÓN G — INTEGRACIÓN CON FIGMA

La integración entre **Storybook** y **Figma** cierra la brecha entre diseño y desarrollo, permitiendo la trazabilidad bidireccional:

#### Plugin Storybook Connect para Figma

Este plugin de Figma permite:
1. Vincular componentes de Figma con stories de Storybook.
2. Ver en Figma si un componente de diseño tiene una implementación correspondiente en Storybook.
3. Navegar directamente desde Figma a la story de Storybook del componente.

!!! info "Vinculación Figma ↔ Storybook"

    Flujo de trabajo: el diseñador selecciona un componente en Figma y lo vincula a la URL de su story en Storybook. A partir de ese momento, cualquiera que vea ese componente en Figma sabrá que está implementado y podrá verlo en acción.

#### Incrustar Figma en Storybook

En sentido inverso, el addon `@storybook/addon-designs` permite incrustar diseños de Figma en Storybook, para que los desarrolladores y revisores puedan comparar directamente el componente desarrollado con el diseño original:

```
const meta: Meta<ButtonComponent> = {
  title: 'UI/Button',
  component: ButtonComponent,
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/design/team-file/Design-System?node-id=42-123&t=abc',
    },
  },
};
```

El diseño incrustado de Figma es interactivo: se puede hacer zoom, paneo y selección de capas.

### SECCIÓN H — PUBLICACIÓN Y DESPLIEGUE

#### Build estático

Storybook puede generar un build estático (HTML + CSS + JS) que se puede servir desde cualquier hosting sin necesidad de un servidor Node.js:

```
npm run build-storybook
```

Este comando genera una carpeta `storybook-static/` con la documentación completa lista para desplegar.

#### Despliegue en Chromatic

Chromatic no solo hace testing visual, sino que también ofrece hosting gratuito para proyectos open-source y de equipos pequeños. Cada PR despliega automáticamente una versión de Storybook en una URL única y efímera que se puede compartir con stakeholders para revisión.

#### Despliegue en GitHub Pages

Integración con GitHub Actions para desplegar automáticamente Storybook en GitHub Pages al hacer push a main:

```
# .github/workflows/storybook.yml
name: Deploy Storybook
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm run build-storybook
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./storybook-static
```

#### Despliegue en Netlify o Vercel

Tanto Netlify como Vercel pueden desplegar automáticamente la carpeta `storybook-static/` a partir de un repositorio de GitHub, ofreciendo URL pública, SSL automático y preview deployments para cada PR.

---

## Ejemplos guiados

### Ejemplo guiado 1: Crear stories para todos los estados de un componente Button

**Objetivo:** Escribir un archivo de stories exhaustivo para el componente Button que cubra todas las variantes, tamaños, estados y configuraciones.

**Pasos:**

1. **Crear el archivo `button.stories.ts`** con los metadatos y argTypes completos (5 variantes, 3 tamaños, 5 propiedades booleanas).
2. **Crear la story Primary** (usa los args por defecto).
3. **Crear las stories de variantes:** Secondary, Outline, Ghost, Danger — cada una sobrescribiendo solo el arg `variant`.
4. **Crear las stories de tamaño:** Small (size=sm), Medium (size=md, por defecto), Large (size=lg).
5. **Crear las stories de estado:** Disabled, Loading.
6. **Crear las stories con icono:** IconLeft, IconRight, IconOnly (sin texto, solo icono).
7. **Añadir una play function** a la story Primary que verifique: el botón se renderiza, se puede hacer click, emite el evento clicked.
8. **Añadir la incrustación de Figma** con el parámetro `design`.

Resultado: una documentación completa del Button con 12+ stories que cubren todas las combinaciones relevantes.

### Ejemplo guiado 2: Storybook completo de un componente Card con MDX + play functions + a11y

**Objetivo:** Documentar exhaustivamente el componente Card usando todos los recursos: CSF3, MDX, play functions y auditoría de accesibilidad.

**Pasos:**

1. **Crear `card.stories.ts`** con stories para: Default, WithHeader, WithFooter, WithImage, Clickable, Elevated, Bordered, SmallPadding.
2. **Crear `card.stories.mdx`** con documentación narrativa: introducción, cuándo usar, cuándo no usar, variantes, ejemplos de código, notas de accesibilidad.
3. **Añadir play function** a la story Clickable que verifique: al hacer click, se emite el evento `cardClick`.
4. **Verificar la auditoría de accesibilidad:** ejecutar el addon a11y y comprobar que no hay violaciones.

### Ejemplo guiado 3: Configurar Chromatic para visual testing

**Objetivo:** Integrar Chromatic en el flujo de CI/CD para detectar regresiones visuales automáticamente.

**Pasos:**

1. **Crear cuenta en Chromatic** y obtener el project token.
2. **Instalar chromatic** como dependencia de desarrollo: `npm install --save-dev chromatic`.
3. **Añadir el script** a `package.json`: `"chromatic": "chromatic"`.
4. **Ejecutar localmente** para verificar que funciona: `npx chromatic --project-token=<token>`.
5. **Crear el workflow de GitHub Actions** (`.github/workflows/chromatic.yml`) que ejecute Chromatic en cada push a cualquier rama.
6. **Crear un PR de prueba** con un cambio visual (cambiar un color) y verificar que Chromatic detecta la diferencia y la muestra en la UI de revisión.

---

## Actividades guiadas

### Actividad guiada 1: Instalar y configurar Storybook en el proyecto

**Duración:** 60 minutos.

**Objetivo:** Realizar la instalación y configuración completa de Storybook en el proyecto Angular del curso.

**Desarrollo:**
1. El alumnado ejecuta `npx storybook@latest init` en el proyecto Angular donde tiene los componentes de unidades anteriores.
2. Verifica que Storybook arranca correctamente (`npm run storybook`) y muestra las stories de ejemplo.
3. Configura `preview.ts` para importar Tailwind (estilos globales) y añadir viewports personalizados.
4. Configura `main.ts` para añadir los addons de a11y, designs e interactions.
5. Crea al menos una story de prueba para un componente existente (Button).
6. Ejecuta el addon a11y sobre la story y comprueba los resultados.

**Entregable:** Storybook funcionando con la configuración completa y al menos una story.

### Actividad guiada 2: Crear stories para el catálogo de componentes

**Duración:** 120 minutos.

**Objetivo:** Escribir stories para los 14 componentes del catálogo de la Unidad 11.

**Desarrollo:**
1. El alumnado crea un archivo `.stories.ts` para cada componente del catálogo.
2. Para cada componente, escribe al menos: una story por variante (3-5), una story por cada estado especial (disabled, loading, empty y error), y una story con caso de uso real.
3. Configura los argTypes con controles apropiados y descripciones JSDoc.
4. Añade `tags: ['autodocs']` a los metadatos de cada componente.
5. Organiza los componentes en la jerarquía de Storybook según Atomic Design: `Atoms/Button`, `Atoms/Badge`, `Molecules/FormField`, `Molecules/SearchBar`, `Organisms/DataTable`, `Organisms/Modal`.

**Entregable:** 14 archivos `.stories.ts` con cobertura exhaustiva.

### Actividad guiada 3: Escribir documentación MDX para 3 componentes clave

**Duración:** 90 minutos.

**Objetivo:** Crear documentación narrativa en MDX para los componentes Button, DataTable y Modal.

**Desarrollo:**
1. Crear archivos `.stories.mdx` (o `.mdx`) para los 3 componentes.
2. Incluir: introducción, cuándo usar/no usar, variantes visuales (con Canvas embebidos), tabla de API (Controls), consideraciones de accesibilidad, ejemplos de código y enlaces a componentes relacionados.
3. Añadir incrustación de Figma (usar URLs de ejemplo si no hay diseños reales).
4. Verificar que la documentación se renderiza correctamente en la pestaña Docs de Storybook.

**Entregable:** 3 archivos MDX con documentación completa y profesional.

---

## Actividades propuestas

### Actividad propuesta 1: Stories exhaustivas para el componente FormField

**Duración:** 120 minutos.

**Descripción:** Escribir un archivo de stories para el componente FormField (de la Unidad 11) que cubra todos los estados y variantes.

**Requisitos:**
- Stories para cada tipo de input: text, email, password, number, search.
- Stories para cada estado: default, focus, filled, error, disabled.
- Stories con y sin: label, placeholder, hint, icono, indicador de requerido.
- Story con validación asíncrona (estado pending con spinner).
- Play functions que verifiquen: escribir texto actualiza el valor, al hacer blur se marca como touched, el mensaje de error aparece cuando el control es inválido y touched.
- Auditoría de accesibilidad limpia (sin violaciones).

**Entregable:** Archivo `form-field.stories.ts` con al menos 15 stories y play functions.

### Actividad propuesta 2: Documentación MDX del Design System completo

**Duración:** 180 minutos.

**Descripción:** Crear la página de introducción y las páginas de documentación para las categorías principales del Design System usando MDX.

**Requisitos:**
- **Página de introducción** (`Introduction.mdx`): bienvenida, principios, cómo usar, tokens.
- **Página de átomos** (`Atoms.mdx`): resumen de todos los componentes atómicos con ejemplos.
- **Página de moléculas** (`Molecules.mdx`): resumen de todos los componentes moleculares con ejemplos.
- **Página de organismos** (`Organisms.mdx`): resumen de todos los organismos con ejemplos.
- Cada página debe tener: descripción, lista de componentes con enlaces a sus stories, ejemplos de código y buenas prácticas.

**Entregable:** 4 archivos MDX de documentación.

### Actividad propuesta 3: Implementar testing de interacciones para el componente DataTable

**Duración:** 150 minutos.

**Descripción:** Escribir play functions exhaustivas para el componente DataTable que prueben todas las interacciones del usuario.

**Requisitos:**
- Play function para ordenación: hacer click en la cabecera de una columna, verificar que cambia la dirección del icono de ordenación.
- Play function para paginación: hacer click en "Siguiente", verificar que cambia la página mostrada.
- Play function para selección: hacer click en un checkbox de fila, verificar que la fila se selecciona.
- Play function para "Seleccionar todas": hacer click en el checkbox de la cabecera, verificar que todas las filas se seleccionan.
- Play function para estado vacío: pasar datos vacíos, verificar que se muestra el mensaje de empty state.
- Play function para estado de error: pasar un mensaje de error, verificar que se muestra y que el botón "Reintentar" funciona.
- Play function para estado de carga: verificar que se muestran los skeletons correctamente.

**Entregable:** Archivo `data-table.stories.ts` con al menos 8 play functions.

### Actividad propuesta 4: Configurar CI/CD con Chromatic y GitHub Actions

**Duración:** 120 minutos.

**Descripción:** Configurar un pipeline completo de integración continua que ejecute los tests de Storybook y Chromatic en cada Pull Request.

**Requisitos:**
- Workflow que ejecute `npm run build-storybook` para verificar que el build no tiene errores.
- Workflow que ejecute Chromatic para detectar cambios visuales.
- Workflow que ejecute el test runner de Storybook para verificar play functions y a11y.
- Configurar el job para que falle si hay violaciones de accesibilidad o play functions rotas.
- Añadir el badge de Chromatic al README del proyecto.
- Documentar el proceso para que otros desarrolladores puedan replicarlo.

**Entregable:** Archivos de workflow (`.github/workflows/`) y documentación del pipeline.

### Actividad propuesta 5: Crear una galería de componentes con Storybook

**Duración:** 120 minutos.

**Descripción:** Construir una story compuesta (Composite Story) que muestre todos los componentes del Design System juntos en una sola página, a modo de galería o "showcase".

**Requisitos:**
- Crear una página "Showcase" que renderice una grid con todos los componentes.
- Incluir: una barra de navegación (Header), tarjetas de estadísticas (StatCard), una tabla de datos (DataTable), un formulario (con varios FormField + Button), modales, toasts, badges, avatares.
- La galería debe ser interactiva: los botones deben funcionar, los modales deben abrirse, las notificaciones deben aparecer.
- Utilizar datos mock realistas para que la galería parezca una aplicación real en miniatura.

**Entregable:** Story "Showcase" con la galería de componentes interactiva.

---

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Crear un addon personalizado para Storybook

    **Duración:** 240 minutos.

    **Descripción:** Desarrollar un addon de Storybook personalizado que añada una pestaña con información específica del Design System (por ejemplo, un panel que muestre los Design Tokens aplicados al componente seleccionado).

    **Requisitos:**
    - El addon debe aparecer como una pestaña adicional en el panel de addons.
    - Debe mostrar los tokens de diseño (colores, tipografía, espaciado) que el componente está utilizando.
    - Debe estar empaquetado como un paquete npm instalable.
    - Documentar el proceso de creación, instalación y uso del addon.

    **Entregable:** Addon funcional + documentación.

    ### Actividad de ampliación 2: Configurar un portal de Design System con Storybook y Zeroheight

    **Duración:** 180 minutos.

    **Descripción:** Integrar Storybook con Zeroheight (plataforma de documentación de Design Systems) para crear un portal unificado que combine documentación de diseño (Figma) y desarrollo (Storybook).

    **Requisitos:**
    - Crear una cuenta en Zeroheight (plan gratuito).
    - Integrar las stories de Storybook mediante embeds.
    - Sincronizar los design tokens y componentes entre Figma, Storybook y Zeroheight.
    - Crear páginas para cada categoría de componentes con diseño de Figma y código de Storybook lado a lado.
    - Compartir el enlace del portal para revisión.

    **Entregable:** Portal de Design System en Zeroheight con integraciones funcionales.

    ### Actividad de ampliación 3: Implementar visual testing con múltiples navegadores y temas

    **Duración:** 150 minutos.

    **Descripción:** Configurar Chromatic u otra herramienta de visual testing para que capture screenshots de cada story en diferentes temas (claro, oscuro) y diferentes navegadores (Chrome, Firefox, Safari).

    **Requisitos:**
    - Configurar Chromatic para capturar screenshots en los temas claro y oscuro (usando el background addon o el ThemeService).
    - Configurar Chromatic para ejecutarse en al menos dos navegadores.
    - Crear stories específicas para tema oscuro que activen la clase `.dark` en el contenedor.
    - Analizar los resultados y documentar las diferencias encontradas entre navegadores.

    **Entregable:** Configuración multi-tema y multi-navegador + informe de diferencias.

---

!!! tip "Buenas prácticas"

    1. **Una story por estado, no una story monolítica.** ==Cada variante y estado significativo de un componente merece su propia story==. "Primary", "Secondary", "Disabled", "Loading" como stories separadas es mucho más útil que una sola story "Button" con todos los controles.

    2. **Usar `tags: ['autodocs']` en todos los componentes.** Esto habilita la generación automática de documentación, incluyendo la tabla de argumentos inferida de los tipos TypeScript de los inputs y outputs.

    3. **Nombres de stories descriptivos y en CamelCase.** Los nombres de las stories exportadas deben ser descriptivos para que aparezcan correctamente en la barra lateral: `Primary`, `WithIcon`, `DisabledState`, `EmptyState`.

    4. **Jerarquía de títulos consistente.** Usar una convención de nomenclatura para los títulos de los metadatos: `Atoms/Button`, `Molecules/SearchBar`, `Organisms/Header`, `Pages/Dashboard`. Esto agrupa los componentes por nivel de Atomic Design en la barra lateral.

    5. **Añadir play functions para interacciones críticas.** Las play functions son tests de integración que se ejecutan en un navegador real. Priorizar escribir play functions para las interacciones más importantes: clicks que emiten outputs, navegación por teclado, cambios de estado.

    6. **Ejecutar el addon a11y en cada story y corregir todas las violaciones.** Un componente no está "done" hasta que pasa la auditoría de accesibilidad sin violaciones. Las violaciones de a11y deben tratarse con la misma seriedad que los bugs funcionales.

    7. **Documentar con MDX el "por qué" y el "cuándo", no solo el "qué".** La documentación generada automáticamente (Docs) cubre el "qué" (API del componente). El MDX debe cubrir el "por qué" (decisiones de diseño) y el "cuándo" (casos de uso apropiados e inapropiados).

    8. **Mantener las stories cerca de los componentes.** Los archivos `.stories.ts` deben residir en la misma carpeta que el componente que documentan (`button.component.ts` y `button.stories.ts` juntos), no en una carpeta centralizada de stories. Esto facilita encontrar y mantener la documentación.

    9. **Usar datos mock realistas.** Las stories deben mostrar datos que parezcan reales, no "Lorem ipsum" y "John Doe" genérico. Datos realistas ayudan a diseñadores y stakeholders a evaluar mejor los componentes.

    10. **Versionar las stories junto con los componentes.** Si un componente cambia su API, sus stories deben actualizarse en el mismo commit. Esto mantiene la documentación siempre sincronizada con el código.

    11. **No mockear servicios en stories de componentes presentacionales.** Los componentes presentacionales no deben inyectar servicios. Si una story necesita mockear un servicio, es una señal de que el componente es Smart y probablemente debería dividirse.

    12. **Publicar Storybook regularmente.** Un Storybook desplegado y accesible vía URL es infinitamente más valioso que uno que solo existe en local. Automatizar el despliegue para que siempre refleje la última versión de main.

---

!!! warning "Errores frecuentes"

    1. **No importar Tailwind en `preview.ts`.** El error más común al configurar Storybook con Angular y Tailwind es olvidar importar los estilos globales en `preview.ts`. El resultado: todos los componentes aparecen sin estilos. La línea `import '!style-loader!css-loader!postcss-loader!../src/styles.css'` es obligatoria.

    2. **Stories que no reflejan el estado real del componente.** Si un componente añade un nuevo input requerido, las stories existentes deben actualizarse. No hacerlo resulta en stories que fallan al renderizar o, peor, que muestran un estado incorrecto (por ejemplo, un botón sin texto).

    3. **No configurar los viewports.** Sin viewports configurados, Storybook solo muestra los componentes en el tamaño por defecto. Muchos bugs de diseño solo son visibles en móvil o tablet.

    4. **Ignorar las violaciones de a11y.** Acumular violaciones de accesibilidad en las stories es una mala práctica. Cada violación debe corregirse o, si es un falso positivo, configurarse como excepción justificada.

    5. **Usar `any` en los argTypes.** Si un argType no está correctamente tipado, el panel de Controls no ofrecerá los controles adecuados (por ejemplo, un campo de texto en lugar de un select para una variante).

    6. **Crear stories demasiado complejas.** Una story con 15 argumentos modificables es difícil de entender. Es preferible tener 10 stories con 2-3 args cada una que una sola story con todos los args.

    7. **No añadir `autodocs` tag.** Sin este tag, Storybook no genera la documentación automática del componente, y los usuarios no pueden ver la tabla de argumentos ni la descripción.

    8. **Olvidar limpiar el estado entre play functions.** Si una play function modifica el estado del componente (por ejemplo, abre un modal) y no lo restaura, puede afectar a las play functions siguientes que se ejecuten en la misma story.

    9. **No incluir el build de Storybook en CI.** Si Storybook no se construye en CI, los errores de compilación en las stories pueden pasar desapercibidos hasta que alguien intenta ejecutarlo localmente.

    10. **Documentación desactualizada en MDX.** El MDX no se regenera automáticamente como las stories. Si un componente cambia, el texto explicativo en el MDX debe revisarse manualmente para asegurar que sigue siendo preciso.

---

!!! abstract "Resumen"

    Esta unidad ha abordado la documentación de componentes con Storybook en el contexto de Angular profesional:

    - **Storybook** es una herramienta de desarrollo aislado que funciona como taller, documentación viva, catálogo de componentes y plataforma de testing visual.
    - La **instalación** se realiza con `npx storybook@latest init`, que configura automáticamente el proyecto Angular. La integración con Tailwind requiere importar los estilos globales en `preview.ts`.
    - El formato **CSF3** simplifica la escritura de stories con menos boilerplate y mejor inferencia de tipos, usando `Meta<>` y `StoryObj<>`.
    - **MDX** permite crear documentación narrativa que combina texto, código y stories interactivas en un solo archivo.
    - Los **addons esenciales** incluyen Controls (modificar inputs), Actions (ver outputs), Viewport (responsive), Backgrounds, a11y (auditoría de accesibilidad), Interactions (play functions) y Designs (incrustar Figma).
    - El **testing** en Storybook abarca tres niveles: interacciones (simular clicks/teclado), accesibilidad (axe-core) y visual (comparación píxel a píxel con Chromatic).
    - La **integración con Figma** permite vincular bidireccionalmente componentes de diseño con sus implementaciones en código.
    - La **publicación** del build estático puede realizarse en Chromatic, GitHub Pages, Netlify o Vercel, idealmente automatizada mediante CI/CD.

---

## Recursos complementarios

### Documentación oficial
- Storybook para Angular: https://storybook.js.org/docs/get-started/frameworks/angular
- CSF3 (Component Story Format 3): https://storybook.js.org/docs/api/csf
- Storybook MDX: https://storybook.js.org/docs/writing-docs/mdx
- Addon Interactions: https://storybook.js.org/docs/writing-tests/interaction-testing
- Addon a11y: https://storybook.js.org/docs/writing-tests/accessibility-testing

### Herramientas
- Chromatic: https://www.chromatic.com (testing visual y hosting)
- Figma Tokens: https://www.figmatokens.com (sincronización Figma ↔ código)
- Zeroheight: https://zeroheight.com (portal de Design System)
- Percy (BrowserStack): https://percy.io (testing visual alternativo)

### Cursos y tutoriales
- "Storybook for Angular Developers" — Storybook Team (YouTube)
- "Component-Driven Development with Angular and Storybook" — Angular Addicts
- "Visual Testing with Storybook and Chromatic" — Chromatic Academy

### Libros
- "Storybook in Action" — Varun Vachhar
- "Design Systems" — Alla Kholmatova (capítulos sobre documentación)

### Comunidad
- Storybook Discord: https://discord.gg/storybook
- Storybook Blog: https://storybook.js.org/blog
- Chromatic Blog: https://www.chromatic.com/blog
