---
icon: lucide/workflow
---

# Arquitectura de Interfaces con Angular

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:
- Diseñar y estructurar la arquitectura de una interfaz de aplicación Angular siguiendo patrones profesionales.
- Diferenciar entre componentes Smart (contenedores) y Presentational (de presentación) y aplicarlos correctamente en el desarrollo de interfaces.
- Configurar y utilizar **Standalone Components** con imports explícitos en el diseño de interfaces complejas.
- Integrar clases de **Tailwind CSS** en plantillas Angular estableciendo un sistema de estilos robusto y mantenible.
- Dominar la comunicación entre componentes mediante @Input, @Output, Model Inputs y Signals para la gestión del estado de interfaz.
- Manipular el DOM de forma reactiva mediante **viewChild y contentChild** en contextos de interfaz de usuario.
- Organizar proyectos Angular con estructura profesional feature-based para interfaces escalables.
- Aplicar el principio de responsabilidad única en el diseño de componentes orientados a interfaz de usuario.

## Resultado de aprendizaje asociado

Esta unidad contribuye, como RA principal, al **RA 1** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 1.** Genera interfaces gráficos de usuario mediante editores visuales utilizando las funcionalidades del editor y adaptando el código generado.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE c) Se han utilizado las funciones del editor para ubicar los componentes del interfaz.
- CE d) Se han modificado las propiedades de los componentes para adecuarlas a las necesidades de la aplicación.
- CE g) Se han asociado a los eventos las acciones correspondientes.
- CE h) Se ha desarrollado una aplicación que incluye el interfaz gráfico obtenido.

Como RA secundario, se vincula al **RA 3** («Crea componentes visuales valorando y empleando herramientas específicas»):

- CE b) Se han creado componentes visuales.
- CE d) Se han determinado los eventos a los que debe responder el componente y se les han asociado las acciones correspondientes.

!!! note "Conocimientos previos"

    El alumnado debe poseer los siguientes conocimientos antes de abordar esta unidad:
    - **Fundamentos de Angular**: uso de Angular CLI, estructura básica de un proyecto, comprensión del sistema de módulos y componentes.
    - **TypeScript**: tipos básicos, interfaces, genéricos, decoradores y programación orientada a objetos aplicada a Angular.
    - **HTML semántico y CSS**: comprensión de selectores, especificidad, modelo de caja, flexbox y grid.
    - **Tailwind CSS**: conocimiento de clases utilitarias básicas, sistema de espaciado, colores y tipografía en Tailwind.
    - **Fundamentos de programación orientada a eventos**: eventos del DOM, delegación de eventos, propagación.
    - **Diseño de interfaces de usuario**: principios básicos de composición visual, jerarquía y layout.

## Contenidos

1. Fundamentos de componentes para interfaces
2. Organización de proyectos profesionales
3. Patrón Smart vs Presentational Components
4. Comunicación entre componentes
5. Manipulación del DOM con viewChild y contentChild

## Desarrollo teórico

### SECCIÓN A — FUNDAMENTOS DE COMPONENTES PARA INTERFACES

#### Standalone Components orientados a interfaces

Los **Standalone Components** representan la evolución del modelo de componentes en Angular desde la versión 15. En el contexto del diseño de interfaces, cada componente standalone es autónomo y declara explícitamente todas sus dependencias mediante la propiedad `imports` del decorador `@Component`. Esta independencia elimina la necesidad de NgModules para componentes de interfaz, simplificando drásticamente la estructura del proyecto y facilitando la reutilización.

Un componente standalone para interfaz se caracteriza por tres atributos fundamentales en el decorador: `selector`, que define el nombre de la etiqueta HTML personalizada que utilizará el componente en las plantillas; `template` o `templateUrl`, que contiene el marcado HTML del componente incluyendo las clases utilitarias de Tailwind; y `styles` o `styleUrls`, donde se definen los estilos específicos del componente. La propiedad `standalone: true` marca explícitamente el componente como autónomo, indicando al compilador de Angular que debe tratarlo como una unidad independiente sin necesidad de ser declarado en un NgModule.

La estructura típica de un componente standalone para interfaz se asemeja al siguiente patrón:

```
import { Component, Input, Output, EventEmitter } from '@angular/core';
import { NgClass, NgStyle } from '@angular/common';

@Component({
  selector: 'app-stat-card',
  standalone: true,
  imports: [NgClass, NgStyle],
  template: `
    <div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm transition-shadow hover:shadow-md">
      <div class="flex items-center justify-between">
        <h3 class="text-sm font-medium text-gray-500">{{ title }}</h3>
        <span class="rounded-full bg-blue-100 px-2 py-1 text-xs font-semibold text-blue-700">{{ badge }}</span>
      </div>
      <p class="mt-3 text-3xl font-bold text-gray-900">{{ value }}</p>
      <p class="mt-1 text-sm" [ngClass]="trend >= 0 ? 'text-green-600' : 'text-red-600'">
        {{ trend >= 0 ? '+' : '' }}{{ trend }}%
      </p>
    </div>
  `,
  styles: [`
    :host {
      display: block;
    }
  `]
})
export class StatCardComponent {
  @Input({ required: true }) title!: string;
  @Input({ required: true }) value!: string;
  @Input({ required: true }) badge!: string;
  @Input() trend: number = 0;
}
```

La declaración explícita de imports es fundamental para mantener la transparencia en las dependencias de cada componente. Cuando un componente de interfaz necesita directivas estructurales como `NgIf` o `NgFor`, o pipes como `DatePipe` o `CurrencyPipe`, debe importarlos explícitamente en el array `imports`. Esta práctica, aunque más verbosa inicialmente, produce código más mantenible y facilita el tree-shaking durante la compilación, eliminando código no utilizado y reduciendo el tamaño del bundle final.

#### Templates con Tailwind CSS

La integración de **Tailwind CSS** en plantillas Angular supone un cambio de paradigma respecto al CSS tradicional. En lugar de escribir hojas de estilo separadas con selectores de clase semánticos, aplicamos clases utilitarias directamente en los elementos HTML del template. Esta aproximación ofrece beneficios sustanciales para el desarrollo de interfaces: eliminación de la fricción por nombrar clases, consistencia garantizada por el sistema de diseño predefinido, y un flujo de desarrollo más rápido al no alternar constantemente entre archivos de template y de estilos.

El template de un componente Angular con Tailwind se convierte en un documento denso en clases utilitarias que describen cada aspecto visual del elemento. Por ejemplo, un campo de formulario con estados de error se expresaría de la siguiente manera:

```
<div class="space-y-1">
  <label for="email" class="block text-sm font-medium text-gray-700">
    Correo electrónico
  </label>
  <input
    id="email"
    type="email"
    [formControl]="emailControl"
    class="block w-full rounded-lg border px-3 py-2 text-sm shadow-sm transition-colors duration-150
           focus:outline-none focus:ring-2 focus:ring-offset-0
           [&.ng-invalid.ng-touched]:border-red-400 [&.ng-invalid.ng-touched]:focus:ring-red-400
           [&.ng-valid.ng-touched]:border-green-400 [&.ng-valid.ng-touched]:focus:ring-green-400
           [&:not(.ng-touched)]:border-gray-300 [&:not(.ng-touched)]:focus:ring-blue-500"
    placeholder="usuario@dominio.com"
  />
  <p class="text-xs text-red-500" *ngIf="emailControl.invalid && emailControl.touched">
    Introduce un correo electrónico válido
  </p>
</div>
```

La sintaxis de variantes arbitrarias de Tailwind como `[&.ng-invalid.ng-touched]:border-red-400` permite reaccionar a las clases CSS que Angular añade automáticamente a los controles de formulario según su estado de validación. Esta capacidad es especialmente potente porque elimina la necesidad de lógica TypeScript adicional para gestionar clases condicionales, manteniendo toda la lógica de presentación en el template.

Para proyectos con configuración avanzada, puede ser necesario personalizar el archivo `tailwind.config.js` o su equivalente en Tailwind 4 para incluir los directorios donde residen los templates de Angular y garantizar que el analizador de clases de Tailwind detecte todas las clases utilizadas:

```
// tailwind.config.js
export default {
  content: [
    './src/**/*.{html,ts}',
    './src/**/*.component.ts',
  ],
  theme: {
    extend: {
      // ...
    },
  },
  plugins: [],
}
```

#### Estilos en componentes Angular para interfaces

Angular proporciona tres estrategias de encapsulación de estilos mediante la propiedad `encapsulation` del decorador `@Component`, y la elección de una u otra tiene implicaciones profundas en la arquitectura de estilos de la interfaz.

`ViewEncapsulation.Emulated`, el valor por defecto, emula el Shadow DOM añadiendo atributos únicos a los elementos del componente y a los selectores CSS correspondientes. Esta estrategia aísla los estilos del componente sin depender del soporte nativo del navegador para Shadow DOM. Para el desarrollo de interfaces con Tailwind, esta configuración funciona aceptablemente bien porque las clases utilitarias de Tailwind no se ven afectadas por el aislamiento; sin embargo, los estilos personalizados escritos en el array `styles` del componente quedan contenidos y no afectan a otros componentes.

`ViewEncapsulation.None` desactiva completamente el encapsulamiento, haciendo que los estilos del componente sean globales. Esta opción rara vez es recomendable en producción para componentes de interfaz ordinarios, pero puede resultar necesaria para componentes que deben estilizar elementos fuera de su ámbito (como tooltips renderizados en el body o modales teleportados). También puede emplearse en el componente raíz o en hojas de estilo globales que definan las variables CSS del design system.

`ViewEncapsulation.ShadowDom` utiliza el Shadow DOM nativo del navegador, proporcionando el aislamiento más estricto. Aunque es técnicamente la opción más correcta, presenta limitaciones prácticas con Tailwind CSS, ya que las clases utilitarias definidas globalmente no penetran el Shadow DOM por defecto. Esta estrategia se reserva para casos muy específicos donde el aislamiento total es un requisito innegociable, como en widgets embebidos en aplicaciones de terceros.

Los pseudo-selectores `:host` y `::ng-deep` merecen atención especial en el contexto de interfaces. `:host` selecciona el elemento anfitrión del componente, es decir, la etiqueta HTML personalizada (como `<app-stat-card>`) que contiene al componente. Es particularmente útil para definir estilos que afectan al propio elemento contenedor, como márgenes, display o dimensiones.

```
styles: [`
  :host {
    display: block;
    width: 100%;
  }
  :host(.highlighted) {
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
  }
`]
```

`::ng-deep`, por su parte, fuerza a que los estilos de un componente atraviesen las barreras de encapsulación y afecten a componentes hijos. Aunque es una herramienta poderosa, su uso se considera una mala práctica en la mayoría de los casos porque rompe el principio de encapsulación y crea dependencias frágiles entre componentes. Las notas de la documentación oficial de Angular lo marcan como deprecado y recomiendan alternativas como variables CSS o inputs de estilo. No obstante, en el contexto del desarrollo de interfaces, `::ng-deep` sigue siendo la única solución viable para estilizar componentes de terceros cuyo markup interno no podemos modificar:

```
styles: [`
  ::ng-deep .third-party-slider .track {
    background-color: theme('colors.blue.500');
  }
`]
```

La decisión entre estilos inline (definidos en el array `styles`), estilos externos (archivo CSS/SASS referenciado por `styleUrls`) y Tailwind como sistema principal debe basarse en la naturaleza del componente. Para componentes simples o de tamaño medio, los estilos inline combinados con Tailwind son la mejor opción porque mantienen toda la definición del componente en un solo archivo. Para componentes complejos con gran cantidad de estilos personalizados, puede ser preferible extraerlos a un archivo separado o, mejor aún, migrar esos estilos al sistema de diseño basado en tokens de Tailwind.

#### Ciclo de vida relevante para interfaces

El ciclo de vida de un componente Angular incluye múltiples hooks, pero tres de ellos son particularmente relevantes para el desarrollo de interfaces de usuario: `ngOnInit`, `ngAfterViewInit` y `ngOnDestroy`. Comprender cuándo y cómo utilizar cada uno es esencial para construir interfaces reactivas y eficientes.

`ngOnInit` se ejecuta una única vez, después de que Angular haya inicializado todas las propiedades enlazadas con datos (inputs) y antes de que se renderice la vista. Es el lugar idóneo para:
- Inicializar datos del componente mediante llamadas a servicios.
- Inicializar Signals de estado de interfaz con valores por defecto.
- Configurar suscripciones a streams de datos (Observables) que alimentarán la interfaz.
- Realizar cálculos iniciales que no dependen del DOM.

Un ejemplo típico de inicialización de interfaz en ngOnInit:

```
private dataService = inject(DashboardService);

loading = signal(true);
stats = signal<Stat[]>([]);
error = signal<string | null>(null);

ngOnInit(): void {
  this.dataService.getDashboardStats().pipe(
    takeUntilDestroyed()
  ).subscribe({
    next: (data) => {
      this.stats.set(data);
      this.loading.set(false);
    },
    error: (err) => {
      this.error.set('No se pudieron cargar las estadísticas');
      this.loading.set(false);
    }
  });
}
```

!!! info "Dato clave"

    Obsérvese el uso de `takeUntilDestroyed()` introducido en Angular 16, que simplifica la limpieza de suscripciones vinculando su ciclo de vida al del componente, eliminando la necesidad de gestionar manualmente `Subject` de destrucción.

`ngAfterViewInit` se ejecuta una vez que la vista del componente y las vistas de sus hijos han sido completamente inicializadas. En este punto, el DOM está disponible para ser manipulado. Es el hook adecuado para:
- Inicializar librerías externas que requieren acceso al DOM, como bibliotecas de gráficos (Chart.js, D3.js, ApexCharts), editores de texto enriquecido (Quill, Monaco), o mapas (Leaflet, Mapbox).
- Realizar mediciones del DOM (tamaños, posiciones) para cálculos de layout.
- Implementar scroll programático a elementos específicos.
- Configurar observadores de intersección (**Intersection Observer**) para animaciones basadas en scroll o lazy loading.

Un ejemplo práctico de inicialización de un gráfico:

```
private chartContainer = viewChild<ElementRef>('chartContainer');

ngAfterViewInit(): void {
  const container = this.chartContainer();
  if (container) {
    this.initializeChart(container.nativeElement);
  }
}

private initializeChart(element: HTMLElement): void {
  const ctx = element.querySelector('canvas')?.getContext('2d');
  if (ctx) {
    new Chart(ctx, {
      type: 'line',
      data: { ... },
      options: { ... }
    });
  }
}
```

Es importante destacar que el uso de `viewChild` con señales (sintaxis `viewChild<ElementRef>('chartContainer')`) devuelve una señal que se actualiza reactivamente cuando el elemento está disponible, proporcionando una garantía más robusta que la versión imperativa tradicional.

`ngOnDestroy` se invoca inmediatamente antes de que Angular destruya el componente. Es el momento crítico para realizar tareas de limpieza que eviten fugas de memoria y comportamientos indeseados:
- Cancelar suscripciones a Observables que no utilicen `takeUntilDestroyed()`.
- Eliminar event listeners añadidos manualmente al `document`, `window` u otros elementos globales.
- Destruir instancias de librerías externas (gráficos, mapas, editores).
- Limpiar timers (setTimeout, setInterval) y animaciones en curso.
- Invalidar observadores de intersección o de redimensionamiento.

Aunque `takeUntilDestroyed()` maneja automáticamente la limpieza de suscripciones en Observables, otras fuentes de fugas deben gestionarse explícitamente:

```
private resizeObserver?: ResizeObserver;
private chartInstance?: Chart;

ngAfterViewInit(): void {
  this.chartInstance = new Chart(...);
  this.resizeObserver = new ResizeObserver(() => this.chartInstance?.resize());
  this.resizeObserver.observe(this.chartContainer()!.nativeElement);
}

ngOnDestroy(): void {
  this.chartInstance?.destroy();
  this.resizeObserver?.disconnect();
}
```

---

### SECCIÓN B — ORGANIZACIÓN DE PROYECTOS PARA INTERFACES

#### Estructura de carpetas profesional

La organización de un proyecto Angular profesional destinado a interfaces de usuario debe seguir una estructura clara y predecible que facilite la navegación, el desarrollo en equipo y la escalabilidad. La disposición de carpetas recomendada, basada en una arquitectura **feature-based**, es la siguiente:

```
src/
├── app/
│   ├── core/            # Servicios singleton, guards, interceptors, modelos
│   │   ├── guards/
│   │   ├── interceptors/
│   │   ├── models/
│   │   └── services/
│   ├── shared/          # Componentes UI reutilizables y directivas
│   │   ├── components/
│   │   │   ├── button/
│   │   │   │   ├── button.component.ts
│   │   │   │   ├── button.component.html
│   │   │   │   └── button.component.spec.ts
│   │   │   ├── modal/
│   │   │   ├── card/
│   │   │   ├── input/
│   │   │   ├── dropdown/
│   │   │   └── data-table/
│   │   ├── directives/
│   │   └── pipes/
│   ├── features/        # Pantallas completas o módulos funcionales
│   │   ├── dashboard/
│   │   │   ├── dashboard.page.ts
│   │   │   ├── dashboard.page.html
│   │   │   └── components/
│   │   │       ├── stat-card/
│   │   │       ├── chart-widget/
│   │   │       └── recent-activity/
│   │   ├── products/
│   │   │   ├── products.page.ts
│   │   │   ├── product-detail.page.ts
│   │   │   └── components/
│   │   │       ├── product-form/
│   │   │       ├── product-list/
│   │   │       └── product-filter/
│   │   ├── users/
│   │   │   ├── users.page.ts
│   │   │   └── components/
│   │   └── settings/
│   ├── layout/          # Shell de la aplicación
│   │   ├── header/
│   │   ├── sidebar/
│   │   ├── footer/
│   │   └── layout.component.ts
│   └── design-system/   # Configuración de diseño, tokens, tema
│       ├── tokens.ts
│       ├── typography.ts
│       └── theme.service.ts
```

Cada una de estas carpetas cumple un rol específico en la arquitectura de la interfaz:

La carpeta `core/` contiene servicios singleton que se instancian una única vez durante toda la vida de la aplicación. Estos servicios incluyen autenticación, acceso a APIs REST, gestión del estado global de interfaz (tema, idioma, preferencias de visualización), interceptores HTTP para añadir tokens de autenticación o manejar errores globalmente, y guards de ruta que protegen el acceso a determinadas páginas. Los modelos de datos (interfaces y tipos TypeScript) que representan las entidades del dominio también residen aquí, garantizando una única fuente de verdad para la forma de los datos.

La carpeta `shared/` alberga componentes de interfaz de usuario verdaderamente reutilizables, sin dependencia alguna de la lógica de negocio de features específicas. Estos componentes son los bloques de construcción fundamentales de la interfaz: botones, tarjetas, modales, campos de formulario, tablas de datos, dropdowns, tooltips, badges, avatares y cualquier otro elemento visual genérico. Cada componente debe ser completamente autónomo, con sus propios inputs, outputs y estilos, y no debe importar servicios de features ni modelos de dominio específicos. Las directivas reutilizables (como directivas de permisos, de tooltip, de lazy-load) y los pipes personalizados también residen en esta carpeta.

La carpeta `features/` contiene las páginas o pantallas completas de la aplicación, organizadas por funcionalidad de negocio. Cada feature es un módulo funcional autocontenido que puede incluir su propia página principal (normalmente un Smart Component que actúa como contenedor), páginas de detalle, y componentes específicos de esa feature que no son lo suficientemente genéricos para residir en `shared/`. Por ejemplo, un `StatCard` que muestra métricas de ventas con formato específico pertenece a la feature `dashboard/`, no a `shared/`, porque su propósito está acoplado a un dominio concreto.

La carpeta `layout/` contiene los componentes que conforman el shell o estructura exterior de la aplicación: la cabecera superior con el logotipo y la navegación del usuario, la barra lateral de navegación con los enlaces a las distintas secciones, el pie de página, y el componente `LayoutComponent` que los ensambla. Este componente de layout típicamente utiliza `router-outlet` para renderizar las páginas de features en el área de contenido principal.

La carpeta `design-system/` es el núcleo de la configuración visual de la aplicación. Contiene la definición de tokens de diseño (paletas de colores, escalas tipográficas, espaciado, sombras, bordes), la configuración extendida de Tailwind (que en Tailwind 4 se realiza mediante `@theme` en CSS), y servicios relacionados con el tema visual como el `ThemeService` que permite alternar entre modo claro y oscuro. Centralizar la configuración de diseño en un solo lugar garantiza la coherencia visual y facilita cambios globales.

#### Feature-based architecture vs layer-based

La arquitectura **feature-based** organiza el código agrupando archivos por funcionalidad de negocio, mientras que la arquitectura **layer-based** agrupa por tipo técnico (todos los componentes juntos, todos los servicios juntos, todos los modelos juntos). Para proyectos de desarrollo de interfaces, la arquitectura feature-based es claramente superior por varias razones.

En una arquitectura layer-based tradicional, la estructura sería similar a:

```
src/app/
├── components/      # Todos los componentes juntos
├── services/        # Todos los servicios juntos
├── models/          # Todos los modelos juntos
└── pipes/           # Todos los pipes juntos
```

Este enfoque presenta problemas significativos cuando la aplicación crece: la carpeta de componentes se convierte en un vertedero con decenas o cientos de archivos sin relación entre sí; un cambio en una funcionalidad requiere modificar archivos dispersos en múltiples carpetas; y resulta imposible determinar qué componentes dependen de qué servicios sin examinar cada importación.

La arquitectura feature-based resuelve estos problemas encapsulando todo lo relacionado con una funcionalidad dentro de su propia carpeta. Cada feature contiene sus páginas, sus componentes específicos, sus servicios (si no son compartidos) y sus modelos locales. Esta co-localización reduce la carga cognitiva, facilita la incorporación de nuevos desarrolladores y permite trabajar en features de forma independiente sin riesgo de conflictos.

!!! tip "Regla práctica"

    El compromiso consiste en mantener `shared/` para componentes verdaderamente reutilizables y `core/` para servicios globales, evitando duplicar código común en cada feature. La regla práctica es: si un componente se utiliza en dos o más features, debe migrar a `shared/`; si un servicio gestiona estado que trasciende una feature individual, pertenece a `core/`.

#### Principio de responsabilidad única aplicado a componentes de interfaz

!!! info "Definición"

    El **Principio de Responsabilidad Única (SRP)**, la "S" de SOLID, establece que un componente ==debe tener una, y solo una, razón para cambiar==. Aplicado al desarrollo de interfaces, esto significa que cada componente debe tener un propósito claramente definido y acotado.

!!! warning "Error común"

    Un error común es crear "componentes página" que acumulan toda la lógica de negocio, la obtención de datos, las transformaciones, el estado de interfaz, los manejadores de eventos y el template completo en un solo archivo. Estos componentes monolíticos son difíciles de testear, imposibles de reutilizar, y propensos a errores cuando múltiples desarrolladores trabajan simultáneamente.

La aplicación del SRP conduce naturalmente a una descomposición en componentes más pequeños y especializados. Una página de dashboard, por ejemplo, no debería contener directamente el HTML de las tarjetas de estadísticas, los gráficos y las tablas de actividad reciente. En su lugar, debería delegar cada sección visual en un componente específico:

```
<!-- dashboard.page.html -->
<div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
  <app-page-header title="Dashboard" description="Resumen de métricas y actividad reciente" />

  <div class="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
    @for (stat of stats(); track stat.id) {
      <app-stat-card [data]="stat" />
    }
  </div>

  <div class="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-3">
    <div class="lg:col-span-2">
      <app-chart-widget [series]="chartData()" [loading]="loading()" />
    </div>
    <div>
      <app-recent-activity [activities]="recentActivity()" />
    </div>
  </div>
</div>
```

El `DashboardPage` (Smart Component) mantiene la responsabilidad de orquestar: obtiene los datos, los transforma según sea necesario y los distribuye a componentes presentacionales especializados. Los componentes presentacionales, a su vez, tienen la única responsabilidad de renderizar los datos que reciben y emitir eventos de interacción.

---

### SECCIÓN C — SMART VS PRESENTATIONAL COMPONENTS

#### El patrón fundamental para interfaces

La distinción entre **Smart Components** (contenedores inteligentes) y **Presentational Components** (componentes de presentación o "dumb") es uno de los patrones arquitectónicos más importantes en el desarrollo de interfaces con Angular. Originado en el ecosistema React y popularizado por Dan Abramov, este patrón se adapta perfectamente a Angular y proporciona una separación clara de responsabilidades que mejora la mantenibilidad, la testabilidad y la reutilización del código.

Los **Smart Components** —también conocidos como Containers o Page Components— son los componentes que poseen la inteligencia de la aplicación. Sus responsabilidades incluyen:
- Obtener y gestionar datos desde servicios (HTTP, estado global, almacenamiento local).
- Contener la lógica de negocio específica de la página o sección.
- Mantener el estado de interfaz mediante Signals para esa sección.
- Orquestar la comunicación entre servicios y componentes presentacionales.
- Manejar eventos de los componentes presentacionales y decidir qué acciones de negocio disparar.

La característica más distintiva de un Smart Component es que no contiene prácticamente HTML de presentación. Su template es una composición de componentes presentacionales conectados entre sí. Un Smart Component típico tiene un template similar al del dashboard mostrado anteriormente: contiene otros componentes, pero muy pocos elementos HTML nativos o clases de estilo.

```
@Component({
  selector: 'app-dashboard-page',
  standalone: true,
  imports: [StatCardComponent, ChartWidgetComponent, RecentActivityComponent, PageHeaderComponent],
  template: `
    <app-page-header [title]="'Dashboard'" [description]="'Vista general del negocio'" />
    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
      @for (stat of stats(); track stat.id) {
        <app-stat-card [data]="stat" />
      }
    </div>
    <!-- más componentes presentacionales -->
  `,
})
export class DashboardPageComponent implements OnInit {
  private dashboardService = inject(DashboardService);

  stats = signal<StatData[]>([]);
  loading = signal(true);
  error = signal<string | null>(null);

  ngOnInit(): void {
    this.loadDashboardData();
  }

  private loadDashboardData(): void {
    this.dashboardService.getStats().subscribe({
      next: (data) => {
        this.stats.set(data);
        this.loading.set(false);
      },
      error: (err) => {
        this.error.set('Error al cargar el dashboard');
        this.loading.set(false);
      }
    });
  }
}
```

Los **Presentational Components** —también llamados Dumb Components— son componentes puramente visuales que no tienen conocimiento de la lógica de negocio ni dependencias de servicios. Sus responsabilidades son exclusivamente dos: renderizar los datos que reciben y emitir eventos hacia arriba cuando el usuario interactúa con ellos.

Las reglas de oro para un Presentational Component son:
1. Reciben TODO lo que necesitan mediante `@Input()`.
2. Emiten TODO lo que sucede mediante `@Output()`.
3. No inyectan servicios de datos ni de estado global.
4. No conocen la estructura de la aplicación (rutas, módulos, features).
5. Son altamente reutilizables en diferentes contextos.

Un ejemplo paradigmático de Presentational Component es un `StatCard`:

```
@Component({
  selector: 'app-stat-card',
  standalone: true,
  imports: [NgClass],
  template: `
    <div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
      <div class="flex items-center justify-between">
        <p class="text-sm font-medium text-gray-500">{{ data.label }}</p>
        <span class="rounded-full px-2 py-1 text-xs font-semibold"
              [ngClass]="data.trend >= 0 ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'">
          {{ data.trend >= 0 ? '+' : '' }}{{ data.trend }}%
        </span>
      </div>
      <p class="mt-3 text-3xl font-bold text-gray-900">{{ data.value | number }}</p>
      <p class="mt-1 text-xs text-gray-400">vs. periodo anterior</p>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class StatCardComponent {
  @Input({ required: true }) data!: StatData;
}
```

#### Cómo aplicarlo en una aplicación real

En una aplicación Angular de tamaño medio o grande, la aplicación del patrón **Smart/Presentational** conduce a un árbol de componentes con una jerarquía clara. En la raíz se encuentra el `AppComponent`, que típicamente es un Smart Component ligero que renderiza el `LayoutComponent`. El `LayoutComponent` es un híbrido: contiene componentes estructurales como `Header`, `Sidebar` y `Footer`, y utiliza `<router-outlet>` para renderizar las páginas de features.

Cada página de feature (DashboardPage, ProductsPage, UserProfilePage) es un Smart Component que orquesta los datos y los distribuye a componentes presentacionales específicos de esa feature. Estos componentes presentacionales específicos (como ProductCard, UserAvatar, InvoiceRow) pueden a su vez estar compuestos por componentes presentacionales genéricos de `shared/` (como Button, Card, Badge, Input).

==El flujo de datos es unidireccional descendente==: los Smart Components obtienen datos de los servicios y los pasan hacia abajo a través de inputs. Los eventos fluyen hacia arriba: los Presentational Components emiten eventos que los Smart Components capturan y transforman en acciones de negocio (llamadas a servicios, navegación, actualizaciones de estado).

Este flujo unidireccional facilita enormemente la depuración y el razonamiento sobre la aplicación, ya que en cualquier momento dado el estado de la interfaz está determinado predeciblemente por los datos que fluyen desde los servicios a través de los Smart Components hacia los Presentational Components.

---

### SECCIÓN D — COMUNICACIÓN ENTRE COMPONENTES

#### @Input: recibir datos desde el padre

El decorador `@Input` es el mecanismo fundamental para pasar datos desde un componente padre a un componente hijo. En Angular moderno (versión 16+), los inputs han evolucionado significativamente con nuevas capacidades que mejoran la seguridad de tipos y la expresividad.

La opción `required: true` en la configuración del input garantiza que el componente padre debe proporcionar obligatoriamente un valor para ese input, y el compilador de Angular emitirá un error si se omite. Esta característica elimina una categoría entera de errores en tiempo de ejecución donde un componente intentaba acceder a un input que nunca fue proporcionado:

```
@Input({ required: true }) title!: string;
@Input({ required: true }) items!: MenuItem[];
```

El operador de afirmación no nula `!` después del tipo indica a TypeScript que la propiedad se inicializará por Angular antes de ser utilizada, evitando errores de compilación por propiedades no inicializadas.

La función `transform` disponible en la configuración del input permite aplicar una transformación al valor recibido antes de asignarlo a la propiedad. Esta capacidad es extremadamente útil para adaptar datos al formato de presentación requerido por el componente sin necesidad de getters, setters o lógica adicional:

```
@Input({
  required: true,
  transform: (value: string) => value.toLowerCase().trim()
}) email!: string;

@Input({
  transform: (value: Date | string) => value instanceof Date ? value : new Date(value)
}) createdAt!: Date;
```

Con `transform`, un componente puede aceptar un tipo de dato en crudo (como una cadena ISO de fecha) y automáticamente convertirlo a la representación interna que necesita (un objeto Date). Esto simplifica el código del componente y centraliza la lógica de transformación en un lugar predecible.

#### @Output: emitir eventos hacia arriba

El decorador `@Output` combinado con `EventEmitter` permite que los componentes hijos comuniquen eventos hacia sus componentes padres. Es el mecanismo complementario a `@Input` y completa el flujo de datos bidireccional en la jerarquía de componentes.

Un Presentational Component emite eventos describiendo qué acción realizó el usuario, sin preocuparse de cómo se manejará esa acción. El Smart Component padre recibe el evento y decide la acción de negocio correspondiente:

```
// En el componente hijo (Presentational)
@Output() itemSelected = new EventEmitter<MenuItem>();
@Output() actionClicked = new EventEmitter<string>();

selectItem(item: MenuItem): void {
  this.itemSelected.emit(item);
}

// En el componente padre (Smart)
onItemSelected(item: MenuItem): void {
  this.router.navigate([item.route]);
}
```

!!! tip "Recomendación"

    Es recomendable utilizar tipos genéricos con `EventEmitter<T>` para especificar el tipo de dato emitido, proporcionando seguridad de tipos tanto en la emisión como en la recepción del evento.

#### Model Inputs: two-way binding entre componentes

Los **Model Inputs**, introducidos en Angular 17.2, representan una evolución significativa en la comunicación entre componentes. Utilizando la función `model()`, un componente puede declarar una propiedad que actúa simultáneamente como input y como output para two-way data binding, emulando el comportamiento del `[(ngModel)]` pero aplicado a propiedades personalizadas.

La sintaxis de un model input es notablemente concisa:

```
// En el componente hijo
checked = model(false);
label = model<string>('');

// En el componente padre
<app-toggle [(checked)]="isDarkMode" label="Modo oscuro" />
```

El componente hijo puede leer y escribir la propiedad `checked` como si fuera una señal normal (`this.checked()`, `this.checked.set(true)`), y Angular se encarga de propagar los cambios al componente padre automáticamente. Esta sintaxis reemplaza el patrón tradicional de `@Input` + `@Output` con nombre `xxxChange` que era necesario para el two-way binding.

Los model inputs son particularmente útiles para componentes de formulario personalizados que necesitan sincronizar su estado con el componente padre de forma bidireccional, como interruptores, selectores, sliders, y cualquier control que represente un valor modificable por el usuario.

#### Signals para estado de interfaz

Las **Signals** representan el nuevo sistema de reactividad de Angular y son especialmente adecuadas para gestionar el estado de interfaz de usuario. A diferencia de los Observables con RxJS, las Signals proporcionan una API síncrona y siempre tienen un valor actual, lo que las hace más intuitivas para el estado de UI.

El estado local de un componente se modela naturalmente con Signals:

```
searchTerm = signal('');
isSidebarOpen = signal(true);
selectedFilters = signal<Filter[]>([]);
```

Los **computed signals** (`computed()`) son ideales para valores derivados de interfaz: clases CSS condicionales, visibilidad de elementos, textos dinámicos o cualquier propiedad de presentación que dependa de otras señales. Al ser lazy y memoizadas, los computed son eficientes y solo se recalculan cuando alguna de sus dependencias cambia:

```
sidebarWidth = computed(() => this.isSidebarOpen() ? '16rem' : '4rem');
mainContentClass = computed(() =>
  this.isSidebarOpen() ? 'ml-64' : 'ml-16'
);
isEmptyState = computed(() =>
  this.data().length === 0 && !this.loading()
);
```

El estado compartido entre múltiples componentes se implementa mediante servicios que exponen Signals. Este patrón proporciona una gestión de estado global simple pero potente sin necesidad de librerías externas como NgRx, especialmente adecuado para el estado de interfaz global:

```
@Injectable({ providedIn: 'root' })
export class UIStateService {
  private sidebarOpen = signal(true);
  private theme = signal<'light' | 'dark'>('light');

  isSidebarOpen = this.sidebarOpen.asReadonly();
  currentTheme = this.theme.asReadonly();

  toggleSidebar(): void {
    this.sidebarOpen.update(v => !v);
  }

  setTheme(theme: 'light' | 'dark'): void {
    this.theme.set(theme);
    document.documentElement.classList.toggle('dark', theme === 'dark');
  }
}
```

El uso de `asReadonly()` expone la señal de forma que los consumidores pueden leer su valor pero no modificarla directamente, garantizando que las mutaciones de estado solo ocurran a través de los métodos definidos en el servicio. Esta encapsulación mantiene la integridad del estado y facilita la depuración al concentrar todos los puntos de modificación en un solo lugar.

---

### SECCIÓN E — VIEWCHILD Y CONTENTCHILD PARA INTERFACES

#### viewChild: acceso a elementos del DOM propio

La función `viewChild` (y su versión basada en señales introducida en Angular 17) permite acceder a elementos del DOM o a instancias de componentes hijos dentro del template del propio componente. En el contexto del desarrollo de interfaces, `viewChild` es esencial para escenarios que requieren manipulación directa del DOM que no puede lograrse mediante binding declarativo.

Los casos de uso más comunes incluyen:
- **Inicialización de gráficos y visualizaciones**: acceder a un elemento `<canvas>` o `<div>` contenedor para pasar su contexto a una librería de gráficos.
- **Gestión del foco**: enfocar automáticamente un campo de formulario cuando se abre un modal o se navega a una página.
- **Scroll programático**: desplazar la vista a un elemento específico (primer error de formulario, nuevo elemento añadido a una lista).
- **Animaciones imperativas**: controlar animaciones complejas que requieren la API Web Animations.
- **Medición del DOM**: leer dimensiones y posiciones para cálculos de layout dinámico.

La sintaxis moderna con señales:

```
@Component({
  selector: 'app-chart',
  template: `
    <div #chartContainer class="relative h-80 w-full">
      <canvas #chartCanvas></canvas>
    </div>
  `,
})
export class ChartComponent implements AfterViewInit {
  chartCanvas = viewChild<ElementRef<HTMLCanvasElement>>('chartCanvas');
  private chartInstance?: Chart;

  ngAfterViewInit(): void {
    const canvas = this.chartCanvas();
    if (canvas) {
      this.initializeChart(canvas.nativeElement);
    }
  }

  private initializeChart(canvas: HTMLCanvasElement): void {
    this.chartInstance = new Chart(canvas.getContext('2d')!, {
      type: 'bar',
      data: { ... },
      options: { responsive: true, maintainAspectRatio: false }
    });
  }

  ngOnDestroy(): void {
    this.chartInstance?.destroy();
  }
}
```

Es importante destacar que `viewChild` con señales permite un enfoque reactivo: la señal se actualiza automáticamente cuando el elemento referenciado está disponible, y se puede utilizar en `computed` para derivar valores dependientes de la presencia del elemento.

#### contentChild: acceso a contenido proyectado

Mientras `viewChild` accede a elementos que forman parte del template del componente, `contentChild` accede a elementos que han sido proyectados desde el componente padre mediante `<ng-content>`. Esta distinción es fundamental para construir componentes de interfaz compuestos que aceptan contenido externo.

Los casos de uso típicos incluyen:
- **Componentes de panel/Tab/TabGroup**: cada Tab proyecta su contenido, y el TabGroup necesita acceder a los tabs hijos proyectados para gestionar cuál está activo.
- **Acordeón**: los items del acordeón se proyectan desde el padre, y el componente acordeón necesita coordinar cuál está expandido.
- **Wizard/Stepper**: los pasos se proyectan como contenido, y el wizard accede a ellos para validar y navegar.

Ejemplo de un componente Accordion que utiliza `contentChildren` (la versión plural) para acceder a todos los items proyectados:

```
@Component({
  selector: 'app-accordion',
  standalone: true,
  template: `
    <div class="divide-y divide-gray-200 rounded-lg border border-gray-200">
      <ng-content />
    </div>
  `,
})
export class AccordionComponent {
  items = contentChildren(AccordionItemComponent);

  collapseAll(): void {
    this.items().forEach(item => item.collapse());
  }

  expandAll(): void {
    this.items().forEach(item => item.expand());
  }
}
```

La comunicación entre el componente contenedor y sus hijos proyectados por contenido debe realizarse a través de sus APIs públicas (inputs, outputs, métodos). El componente contenedor accede a las instancias de los componentes hijos mediante las referencias obtenidas con `contentChildren` e invoca sus métodos directamente.

#### Patrones de interfaz con viewChild y contentChild

**Patrón de foco automático**: cuando se abre un modal o se muestra un formulario de búsqueda, es una buena práctica de UX enfocar automáticamente el primer campo interactivo. Con `viewChild`, este patrón es directo:

```
private searchInput = viewChild<ElementRef<HTMLInputElement>>('searchInput');

showSearch(): void {
  this.isSearchVisible.set(true);
  // Usar setTimeout para esperar al siguiente ciclo de detección de cambios
  setTimeout(() => {
    this.searchInput()?.nativeElement.focus();
  });
}
```

Alternativamente, con Angular 17+ se puede utilizar `afterNextRender` en lugar de `setTimeout`:

```
import { afterNextRender } from '@angular/core';

showSearch(): void {
  this.isSearchVisible.set(true);
  afterNextRender(() => {
    this.searchInput()?.nativeElement.focus();
  });
}
```

**Patrón de scroll al primer error**: en formularios largos, tras un intento de envío fallido, es buena práctica desplazar la vista hasta el primer campo con error:

```
private formContainer = viewChild<ElementRef>('formContainer');

onSubmit(): void {
  if (this.form.invalid) {
    afterNextRender(() => {
      const firstError = this.formContainer()?.nativeElement.querySelector('.ng-invalid');
      firstError?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      firstError?.focus();
    });
  }
}
```

**Patrón de inicialización de librerías externas**: muchas librerías de UI requieren un elemento DOM como punto de montaje. Este patrón encapsula la inicialización en `ngAfterViewInit` y la destrucción en `ngOnDestroy`:

```
ngAfterViewInit(): void {
  const container = this.editorContainer()?.nativeElement;
  if (container) {
    this.quill = new Quill(container, {
      theme: 'snow',
      modules: { toolbar: true }
    });
    this.quill.on('text-change', () => {
      this.contentChange.emit(this.quill!.root.innerHTML);
    });
  }
}

ngOnDestroy(): void {
  this.quill?.enable(false);
  this.quill = undefined;
}
```

---

## Ejemplos guiados

### Ejemplo 1: Construir un layout dashboard completo

En este ejemplo guiado, construiremos paso a paso la arquitectura completa de un panel de control (dashboard) aplicando el patrón **Smart/Presentational**.

**Paso 1: Crear el Smart Component DashboardPage**

```
@Component({
  selector: 'app-dashboard-page',
  standalone: true,
  imports: [
    HeaderBarComponent,
    SidebarComponent,
    StatCardComponent,
    ChartWidgetComponent,
    DataTableComponent,
  ],
  template: `
    <div class="flex h-screen bg-gray-50">
      <app-sidebar [collapsed]="sidebarCollapsed()" />

      <div class="flex flex-1 flex-col overflow-hidden">
        <app-header-bar
          (menuToggle)="toggleSidebar()"
          [userName]="userName()"
        />

        <main class="flex-1 overflow-y-auto p-6">
          <h1 class="text-2xl font-bold text-gray-900">Dashboard</h1>

          <div class="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
            @for (stat of stats(); track stat.id) {
              <app-stat-card [data]="stat" />
            }
          </div>

          <div class="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-3">
            <div class="lg:col-span-2">
              <app-chart-widget
                [title]="'Ingresos mensuales'"
                [series]="chartData()"
                [loading]="loading()"
              />
            </div>
            <div>
              <app-data-table
                [title]="'Últimas transacciones'"
                [columns]="transactionColumns"
                [rows]="recentTransactions()"
                [loading]="loading()"
              />
            </div>
          </div>
        </main>
      </div>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DashboardPageComponent implements OnInit {
  private dashboardService = inject(DashboardService);

  stats = signal<StatData[]>([]);
  chartData = signal<ChartSeries[]>([]);
  recentTransactions = signal<Transaction[]>([]);
  loading = signal(true);
  sidebarCollapsed = signal(false);
  userName = signal('María García');

  transactionColumns: Column[] = [
    { key: 'description', label: 'Descripción' },
    { key: 'amount', label: 'Importe', type: 'currency' },
    { key: 'status', label: 'Estado', type: 'badge' },
    { key: 'date', label: 'Fecha', type: 'date' },
  ];

  ngOnInit(): void {
    forkJoin({
      stats: this.dashboardService.getStats(),
      chart: this.dashboardService.getChartData(),
      transactions: this.dashboardService.getRecentTransactions(),
    }).pipe(takeUntilDestroyed()).subscribe({
      next: ({ stats, chart, transactions }) => {
        this.stats.set(stats);
        this.chartData.set(chart);
        this.recentTransactions.set(transactions);
        this.loading.set(false);
      },
      error: () => this.loading.set(false),
    });
  }

  toggleSidebar(): void {
    this.sidebarCollapsed.update(v => !v);
  }
}
```

**Paso 2: Crear los Presentational Components**

El `StatCardComponent` recibe datos y los renderiza sin lógica de negocio:

```
@Component({
  selector: 'app-stat-card',
  standalone: true,
  imports: [NgClass, CurrencyPipe],
  template: `
    <div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm transition-shadow hover:shadow-md">
      <div class="flex items-center justify-between">
        <p class="text-sm font-medium text-gray-500">{{ data.label }}</p>
        <span
          class="inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium"
          [ngClass]="{
            'bg-green-100 text-green-800': data.trend >= 0,
            'bg-red-100 text-red-800': data.trend < 0
          }">
          <span class="mr-1">{{ data.trend >= 0 ? '↑' : '↓' }}</span>
          {{ data.trend | number:'1.0-1' }}%
        </span>
      </div>
      <p class="mt-3 text-3xl font-bold text-gray-900">{{ data.value | currency:'EUR' }}</p>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class StatCardComponent {
  @Input({ required: true }) data!: StatData;
}
```

**Paso 3: Verificar el flujo de datos unidireccional**

El flujo de datos es claro y predecible: `DashboardService` → `DashboardPageComponent` (Smart, obtiene y almacena en Signals) → `StatCardComponent`, `ChartWidgetComponent`, `DataTableComponent` (Presentational, renderizan vía @Input). Los eventos de interacción fluyen en dirección contraria mediante @Output.

### Ejemplo 2: Componente de acordeón con contentChild

Construiremos un componente de acordeón que utiliza `contentChildren` para gestionar items proyectados:

```
// accordion-item.component.ts
@Component({
  selector: 'app-accordion-item',
  standalone: true,
  template: `
    <div class="border-b border-gray-200">
      <button
        type="button"
        class="flex w-full items-center justify-between px-4 py-4 text-left text-sm font-medium text-gray-900 hover:bg-gray-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500"
        (click)="toggle()"
        [attr.aria-expanded]="expanded()">
        <span>{{ title() }}</span>
        <svg
          class="h-5 w-5 transform transition-transform duration-200"
          [class.rotate-180]="expanded()"
          fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
        </svg>
      </button>
      <div
        #contentWrapper
        class="overflow-hidden transition-all duration-200"
        [style.maxHeight.px]="expanded() ? contentHeight() : 0">
        <div #content class="px-4 pb-4 text-sm text-gray-600">
          <ng-content />
        </div>
      </div>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class AccordionItemComponent implements AfterViewInit {
  @Input() title = input('');
  expanded = signal(false);
  contentHeight = signal(0);

  private content = viewChild<ElementRef>('content');

  ngAfterViewInit(): void {
    this.measureContent();
  }

  toggle(): void {
    this.expanded.update(v => !v);
    if (this.expanded()) {
      this.measureContent();
    }
  }

  collapse(): void {
    this.expanded.set(false);
  }

  expand(): void {
    this.expanded.set(true);
    this.measureContent();
  }

  private measureContent(): void {
    afterNextRender(() => {
      const el = this.content()?.nativeElement;
      if (el) {
        this.contentHeight.set(el.scrollHeight);
      }
    });
  }
}

// accordion.component.ts
@Component({
  selector: 'app-accordion',
  standalone: true,
  template: `
    <div class="divide-y divide-gray-200 rounded-lg border border-gray-200 bg-white">
      <ng-content />
    </div>
  `,
})
export class AccordionComponent {
  items = contentChildren(AccordionItemComponent);

  collapseAll(): void {
    this.items().forEach(item => item.collapse());
  }

  expandAll(): void {
    this.items().forEach(item => item.expand());
  }
}
```

### Ejemplo 3: Sistema de tema oscuro/claro con Signal compartido en servicio

Implementaremos un sistema de cambio de tema que afecta a toda la interfaz:

```
// theme.service.ts
@Injectable({ providedIn: 'root' })
export class ThemeService {
  private readonly THEME_KEY = 'app-theme-preference';

  private themeSignal = signal<'light' | 'dark'>(this.loadInitialTheme());
  currentTheme = this.themeSignal.asReadonly();

  constructor() {
    this.applyTheme(this.themeSignal());
  }

  toggleTheme(): void {
    const newTheme = this.themeSignal() === 'light' ? 'dark' : 'light';
    this.themeSignal.set(newTheme);
    this.applyTheme(newTheme);
    this.persistTheme(newTheme);
  }

  setTheme(theme: 'light' | 'dark'): void {
    this.themeSignal.set(theme);
    this.applyTheme(theme);
    this.persistTheme(theme);
  }

  private applyTheme(theme: 'light' | 'dark'): void {
    const root = document.documentElement;
    if (theme === 'dark') {
      root.classList.add('dark');
    } else {
      root.classList.remove('dark');
    }
  }

  private loadInitialTheme(): 'light' | 'dark' {
    const stored = localStorage.getItem(this.THEME_KEY);
    if (stored === 'dark' || stored === 'light') return stored;

    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  private persistTheme(theme: 'light' | 'dark'): void {
    localStorage.setItem(this.THEME_KEY, theme);
  }
}

// theme-toggle.component.ts
@Component({
  selector: 'app-theme-toggle',
  standalone: true,
  template: `
    <button
      type="button"
      class="rounded-lg p-2 text-gray-500 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700"
      (click)="toggleTheme()"
      [attr.aria-label]="'Cambiar a modo ' + (isDark() ? 'claro' : 'oscuro')">
      @if (isDark()) {
        <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
        </svg>
      } @else {
        <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
        </svg>
      }
    </button>
  `,
})
export class ThemeToggleComponent {
  private themeService = inject(ThemeService);
  isDark = computed(() => this.themeService.currentTheme() === 'dark');

  toggleTheme(): void {
    this.themeService.toggleTheme();
  }
}
```

---

!!! example "Casos reales"

    ### Caso 1: Arquitectura de un clon de Spotify Web

    Analicemos la arquitectura de componentes de un clon de Spotify Web construido con Angular, un excelente ejemplo de aplicación intensiva en interfaz de usuario.

    La aplicación se organiza en las siguientes features:
    - `browse/`: página de exploración con géneros, listas de reproducción destacadas y nuevos lanzamientos.
    - `library/`: biblioteca del usuario con playlists, álbumes guardados, artistas seguidos y podcasts.
    - `search/`: búsqueda global con resultados en tiempo real categorizados por canciones, artistas, álbumes y playlists.
    - `playlist/`: vista detallada de una playlist con lista de canciones, controles de reproducción e información del creador.
    - `player/`: reproductor de música en la parte inferior con controles, barra de progreso, información de la pista actual y cola de reproducción.

    Los **Smart Components** principales son `BrowsePage`, `LibraryPage`, `SearchPage`, `PlaylistDetailPage` y `PlayerBar`. Cada uno orquesta los datos desde `SpotifyService` (en `core/`) y los distribuye a componentes presentacionales.

    Los **Presentational Components** del catálogo incluyen:
    - `MediaCard`: tarjeta con imagen de portada, título, artista y botón de reproducir (hover).
    - `TrackRow`: fila de canción con número, título, artista, álbum, duración y botón de favorito.
    - `MediaGrid`: grid responsive de `MediaCard` con scroll infinito.
    - `SearchInput`: campo de búsqueda con debounce, historial de búsquedas y sugerencias.
    - `GenrePill`: pastilla de género musical coloreada.
    - `PlayButton`: botón circular verde con icono de play/pause, animación de escala al hacer hover.

    El `LayoutComponent` contiene la estructura persistente: `Sidebar` (navegación principal, playlists del usuario), `TopBar` (botones de navegación hacia atrás/adelante, barra de búsqueda, avatar del usuario) y `PlayerBar` (reproductor siempre visible en la parte inferior).

    La comunicación sigue estrictamente el patrón **Smart/Presentational**. El estado de reproducción actual se gestiona en un `PlayerService` (core) que expone Signals: `currentTrack`, `isPlaying`, `progress`, `volume`. Cualquier componente puede inyectar este servicio y reaccionar a los cambios de estado de reproducción.

    ### Caso 2: Dashboard de análisis de ventas empresarial

    Un dashboard de análisis de ventas para una empresa de comercio electrónico representa otro caso de uso paradigmático de la arquitectura de interfaces con Angular.

    La estructura de features incluye:
    - `overview/`: dashboard principal con KPIs, gráficos de tendencia y mapa de ventas por región.
    - `products/`: análisis de productos con tabla clasificable, filtros avanzados y vista de detalle de producto.
    - `customers/`: segmentación de clientes, cohortes y valor de vida del cliente (LTV).
    - `reports/`: generación de informes personalizados con selector de período, métricas y formato de exportación.

    El sistema de diseño se basa en un conjunto de tokens definidos en `design-system/` que incluyen una paleta de colores corporativa, una escala tipográfica con la fuente Inter para datos y tablas, y un sistema de espaciado de 4px.

    Los componentes presentacionales clave son:
    - `KpiCard`: tarjeta de indicador clave con valor principal, variación porcentual, minigráfico sparkline y tooltip con datos históricos.
    - `FilterBar`: barra horizontal con filtros de fecha (selector de rango con calendario), filtros de categoría (dropdown multiselección) y botón de aplicar.
    - `SortableTable`: tabla de datos con ordenación por columna (click en cabecera), redimensionamiento de columnas, selección de filas y paginación.
    - `ChartContainer`: envoltorio para gráficos de ApexCharts con estados de carga, error y vacío, botones de exportación (PNG, SVG, CSV) y selector de tipo de gráfico.
    - `DateRangePicker`: selector de rango de fechas con accesos rápidos (hoy, ayer, últimos 7 días, últimos 30 días, este mes, personalizado).

    El Smart Component `OverviewPage` inyecta `AnalyticsService` y `DateRangeService` (core), gestiona el estado de filtros y período seleccionado, y orquesta las llamadas a la API para obtener los datos que alimentan a los componentes presentacionales. La detección de cambios **OnPush** en todos los componentes garantiza un rendimiento fluido incluso con grandes volúmenes de datos actualizándose en tiempo real.

---

## Actividades guiadas

### Actividad guiada 1: Identificar Smart y Presentational Components

**Duración estimada:** 45 minutos.

**Objetivo:** Analizar una aplicación Angular existente y clasificar sus componentes según el patrón Smart/Presentational.

**Desarrollo:**
1. El docente proporciona el código fuente de una aplicación Angular de comercio electrónico con al menos 15 componentes (puede ser un proyecto de ejemplo o un repositorio público simplificado).
2. El alumnado, en parejas, examina la estructura de carpetas y los archivos de componentes, identificando para cada uno:
   - Si es Smart o Presentational.
   - Qué servicios inyecta (si es Smart).
   - Qué inputs y outputs expone (si es Presentational).
   - Si cumple o viola el principio de responsabilidad única.
3. El alumnado anota en un documento compartido sus hallazgos para cada componente, justificando la clasificación.
4. Puesta en común: cada pareja expone sus conclusiones sobre dos componentes, y se debate si la clasificación es correcta.
5. El alumnado propone al menos dos refactorizaciones: componentes que deberían dividirse (SRP) o componentes que deberían migrar de Smart a Presentational (o viceversa).

**Entregable:** Documento con la clasificación de cada componente y las propuestas de refactorización justificadas.

### Actividad guiada 2: Refactorizar un componente monolítico a Smart + Presentational

**Duración estimada:** 90 minutos.

**Objetivo:** Transformar un componente página que mezcla lógica y presentación en una arquitectura Smart/Presentational limpia.

**Desarrollo:**
1. El docente proporciona un componente `ProductListPage` monolítico (~300 líneas) que contiene en un solo archivo: inyección del servicio HTTP, obtención de datos, filtrado, ordenación, y un template HTML extenso con tarjetas de producto, barra de filtros y paginación.
2. El alumnado, individualmente o en parejas, sigue estos pasos:
   - **Paso 1:** Crear `ProductListPage` como Smart Component que mantenga la lógica de obtención de datos y gestión de estado (filtros, paginación, ordenación) en Signals.
   - **Paso 2:** Extraer la barra de filtros a `ProductFiltersComponent` (Presentational) con inputs para categorías, rango de precio y término de búsqueda, y outputs para los eventos de cambio de filtro.
   - **Paso 3:** Extraer la tarjeta de producto individual a `ProductCardComponent` (Presentational) con input para los datos del producto y output para click y añadir al carrito.
   - **Paso 4:** Extraer la cuadrícula de productos a `ProductGridComponent` (Presentational) con inputs para el array de productos y el estado de carga.
   - **Paso 5:** Extraer la paginación a `PaginationComponent` (Presentational) con inputs para página actual, total de páginas y outputs para cambio de página.
   - **Paso 6:** Ensamblar todos los componentes en el template del Smart Component `ProductListPage`.
3. Verificar que la funcionalidad completa se ha preservado y que cada nuevo componente cumple estrictamente su rol.
4. Ejecutar tests y comprobar que la cobertura no ha disminuido.

**Entregable:** Código refactorizado con los nuevos componentes y una breve memoria explicando las decisiones de diseño.

### Actividad guiada 3: Implementar comunicación con Model Inputs y Signals

**Duración estimada:** 60 minutos.

**Objetivo:** Implementar un componente de selector de talla con two-way binding usando `model()` y Signals para el estado de UI.

**Desarrollo:**
1. El docente explica el componente a construir: un selector de talla de producto (XS, S, M, L, XL) que muestra botones de selección, resalta la talla seleccionada y notifica al componente padre.
2. El alumnado implementa el componente paso a paso:
   - **Paso 1:** Crear `SizeSelectorComponent` standalone.
   - **Paso 2:** Definir el model input: `selectedSize = model<string>('M')`.
   - **Paso 3:** Definir inputs: `availableSizes = input<string[]>(['XS', 'S', 'M', 'L', 'XL'])`, `disabled = input(false)`.
   - **Paso 4:** Implementar un computed signal `disabledSizes` que devuelva las tallas sin stock (simulado).
   - **Paso 5:** Crear el template con Tailwind: grid de botones, el seleccionado con borde azul y fondo azul claro, los no disponibles tachados y sin interacción.
   - **Paso 6:** Manejar el click en un botón: actualizar la señal `selectedSize` mediante `.set()`.
   - **Paso 7:** Crear un componente padre `ProductDetailPage` (Smart) que use `SizeSelectorComponent` con `[(selectedSize)]` y reaccione al cambio mostrando un mensaje de confirmación mediante un Toast.
3. El alumnado comprueba que el two-way binding funciona correctamente: al seleccionar una talla en el selector, el valor se actualiza en el padre, y si el padre cambia el valor programáticamente, el selector se actualiza.

**Entregable:** Componentes `SizeSelector` y `ProductDetailPage` funcionales.

---

## Actividades propuestas

### Actividad propuesta 1: Diseñar la arquitectura de componentes para una aplicación de gestión de tareas

**Duración estimada:** 120 minutos.

**Descripción:** El alumnado debe diseñar la arquitectura completa de componentes para una aplicación de gestión de tareas (tipo Trello) con Angular, aplicando todos los patrones estudiados:

- **Requisitos funcionales:** La aplicación debe permitir crear tableros, crear listas dentro de cada tablero, añadir tarjetas a las listas, mover tarjetas entre listas (drag and drop), asignar etiquetas de colores, establecer fechas de vencimiento y filtrar por etiqueta o fecha.
- **Entregables:**
  1. Diagrama de árbol de componentes con la jerarquía completa, indicando para cada componente si es Smart (S) o Presentational (P).
  2. Estructura de carpetas propuesta siguiendo la arquitectura feature-based.
  3. Definición de las interfaces TypeScript para los modelos de datos (Board, List, Card, Label).
  4. Listado de servicios necesarios y qué Signals o métodos expone cada uno.
  5. Para los cinco componentes más importantes: especificación de inputs, outputs y responsabilidades.
  6. Justificación escrita de las decisiones arquitectónicas (por qué ciertos componentes son Smart, por qué ciertos servicios residen en core o en feature).

**Criterios de evaluación:**
- Correcta aplicación del patrón Smart/Presentational (30%).
- Coherencia de la estructura de carpetas feature-based (20%).
- Definición precisa de interfaces y tipos (15%).
- Diseño adecuado de la comunicación entre componentes (20%).
- Justificación razonada de las decisiones (15%).

### Actividad propuesta 2: Implementar un sistema de notificaciones con Signals compartidas

**Duración estimada:** 90 minutos.

**Descripción:** Implementar un sistema de notificaciones toast global utilizando un servicio con Signals y componentes presentacionales.

**Requisitos:**
- El servicio `NotificationService` debe exponer una Signal de solo lectura con el array de notificaciones activas.
- Debe tener métodos `show(message, type)`, `success(message)`, `error(message)`, `warning(message)`, `info(message)` y `dismiss(id)`.
- Las notificaciones deben auto-desaparecer tras 5 segundos (configurable).
- El componente `NotificationContainer` debe posicionarse fijo en la esquina superior derecha y renderizar las notificaciones activas con animación de entrada (slide + fade) y salida.
- El componente `NotificationToast` (Presentational) debe recibir la notificación por input y emitir el evento de cierre.

**Entregable:** Servicio `NotificationService`, componente `NotificationContainer`, componente `NotificationToast`, y un componente de prueba que muestre los cuatro tipos de notificación.

### Actividad propuesta 3: Construir un componente de tabla con ordenación y paginación

**Duración estimada:** 120 minutos.

**Descripción:** Construir un componente `DataTable` reutilizable completo siguiendo el patrón Presentational.

**Requisitos:**
- Inputs: `columns` (definición de columnas), `data` (datos genéricos), `loading`, `emptyMessage`, `sortable`.
- Outputs: `sortChange`, `rowClick`.
- Funcionalidades: ordenación por columna (ascendente, descendente, sin ordenar), resaltado de fila al hacer hover, estado de carga (skeleton), estado vacío (mensaje e icono), filas seleccionables.
- Template con Tailwind: diseño limpio y profesional, responsivo con scroll horizontal en móvil.
- Accesibilidad: roles ARIA correctos, navegación por teclado.

**Entregable:** Componente `DataTable` completamente funcional con al menos 5 tests unitarios.

### Actividad propuesta 4: Migrar un proyecto de módulos NgModules a Standalone Components

**Duración estimada:** 90 minutos.

**Descripción:** El docente proporciona un proyecto Angular pequeño (~10 componentes) estructurado con NgModules tradicionales. El alumnado debe migrarlo completamente a Standalone Components.

**Pasos:**
1. Identificar las dependencias reales de cada componente.
2. Añadir `standalone: true` a cada componente.
3. Migrar los `imports` de los NgModules a los arrays `imports` de cada componente.
4. Eliminar los NgModules que ya no sean necesarios.
5. Actualizar el `AppModule` o migrar a bootstrap standalone en `main.ts`.
6. Verificar que la aplicación compila y funciona exactamente igual que antes.

**Entregable:** Proyecto migrado completamente a Standalone Components, con un documento que liste los NgModules eliminados y las decisiones tomadas.

### Actividad propuesta 5: Implementar un layout responsivo con sidebar colapsable

**Duración estimada:** 60 minutos.

**Descripción:** Construir un `LayoutComponent` con sidebar colapsable, header fijo y área de contenido con scroll.

**Requisitos:**
- Sidebar: navegación con iconos y texto, colapsable a versión solo iconos, resaltado del enlace activo basado en la ruta actual.
- Header: barra superior fija con botón de toggle de sidebar, breadcrumb, barra de búsqueda y menú de usuario (dropdown).
- Contenido: área principal con scroll vertical independiente.
- Responsivo: en móvil, el sidebar se oculta completamente y se muestra como overlay al tocar el botón de menú.
- Tema oscuro/claro: el layout debe responder a la clase `dark` en el elemento `<html>`.

**Entregable:** `LayoutComponent` con sus subcomponentes (`Sidebar`, `Header`, `Breadcrumb`, `UserMenu`) completamente funcional y responsivo.

---

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Implementar virtual scrolling para listas de gran tamaño

    **Duración estimada:** 120 minutos.

    **Descripción:** Investigar e implementar la API `@angular/cdk/scrolling` para crear una tabla de datos con scroll virtual que maneje eficientemente 10.000+ filas. El alumnado debe:
    1. Estudiar la documentación de Angular CDK Virtual Scrolling.
    2. Implementar una versión de `DataTable` que utilice `cdk-virtual-scroll-viewport` en lugar de renderizar todas las filas.
    3. Comparar el rendimiento (tiempo de renderizado, memoria) entre la versión normal y la versión con scroll virtual para 1.000, 5.000 y 10.000 filas.
    4. Presentar resultados en una tabla comparativa.

    **Entregable:** Componente `VirtualDataTable`, benchmark de rendimiento y breve informe de conclusiones.

    ### Actividad de ampliación 2: Crear una librería de componentes compartida con Angular CLI

    **Duración estimada:** 150 minutos.

    **Descripción:** Aprender a crear una librería Angular independiente que contenga los componentes reutilizables del proyecto, permitiendo su uso en múltiples aplicaciones. El alumnado debe:
    1. Generar un workspace Angular con una aplicación de prueba y una librería.
    2. Migrar los componentes de `shared/` a la librería.
    3. Configurar la librería para que exporte los componentes, modelos y servicios públicos.
    4. Consumir la librería desde la aplicación de prueba.
    5. Documentar el proceso de build, versionado y publicación (simulada) de la librería.

    **Entregable:** Workspace Angular con aplicación + librería funcional y guía de uso.

    ### Actividad de ampliación 3: Implementar un sistema de plugins de UI con content projection dinámico

    **Duración estimada:** 180 minutos.

    **Descripción:** Diseñar e implementar un sistema que permita a diferentes features de la aplicación registrar componentes en zonas predefinidas del layout (por ejemplo, añadir widgets al dashboard, acciones al menú contextual de tabla, o pestañas a la página de detalle de producto). El alumnado debe:
    1. Crear un servicio `UIPluginService` que gestione el registro de plugins por zona.
    2. Utilizar `ngComponentOutlet` para renderizar dinámicamente los plugins registrados.
    3. Implementar un sistema de prioridades para ordenar los plugins dentro de cada zona.
    4. Crear al menos tres zonas de plugins (dashboard widgets, table row actions, detail page tabs) y dos plugins para cada una.
    5. Demostrar que añadir un nuevo plugin no requiere modificar el componente anfitrión.

    **Entregable:** Sistema de plugins completo con demostración funcional y documentación de la API.

---

!!! tip "Buenas prácticas"

    1. **Nombrado consistente de archivos.** Utilizar sufijos descriptivos: `.component.ts`, `.service.ts`, `.page.ts` para Smart Components, `.model.ts` para interfaces, `.tokens.ts` para design tokens. Esto permite identificar el rol de cada archivo sin necesidad de abrirlo.

    2. **Un componente por archivo.** Cada componente debe residir en su propio archivo. En Angular, esta práctica es especialmente importante porque cada componente suele tener al menos dos archivos (TypeScript y template/estilos). Agruparlos en una carpeta con el nombre del componente mantiene la estructura ordenada.

    3. **Inputs requeridos siempre que sea posible.** Utilizar `@Input({ required: true })` para aquellos inputs sin los cuales el componente no puede funcionar correctamente. Esta práctica convierte errores de tiempo de ejecución en errores de compilación, mucho más fáciles de detectar y corregir.

    4. **OnPush como estrategia de detección de cambios por defecto.** `ChangeDetectionStrategy.OnPush` mejora significativamente el rendimiento de la interfaz al limitar la detección de cambios solo a cuando los inputs cambian por referencia o se emite un evento desde el componente. Combinado con Signals, OnPush produce aplicaciones extremadamente eficientes.

    5. **Inyección de dependencias con `inject()` en lugar de constructor.** La función `inject()` introducida en Angular 14 permite una inyección más limpia y funcional, elimina la necesidad de declarar propiedades en el constructor y facilita la composición de lógica reutilizable mediante funciones.

    6. **Evitar lógica compleja en templates.** Los templates de Angular deben limitarse a bindings simples y directivas estructurales. Cualquier transformación de datos, filtrado o cálculo debe realizarse en la clase del componente y exponerse como una propiedad o Signal.

    7. **Utilizar la nueva sintaxis de control de flujo.** La sintaxis `@if`, `@for`, `@switch` introducida en Angular 17 reemplaza a las directivas `*ngIf`, `*ngFor`, `*ngSwitch` y ofrece mejor rendimiento, soporte para tipado estricto en el template y una sintaxis más legible.

    8. **Componentes pequeños y enfocados.** Un componente no debería superar las 200-300 líneas de código TypeScript (excluyendo imports). Si un componente crece más, es señal de que debería dividirse en subcomponentes más pequeños.

    9. **Documentar inputs y outputs con JSDoc.** Añadir comentarios JSDoc a las propiedades decoradas con `@Input` y `@Output` proporciona documentación inline que los editores muestran como tooltips y que herramientas como Compodoc pueden extraer para generar documentación automática.

    10. **Centralizar la lógica de estilos condicionales.** Cuando un componente tiene muchas clases condicionales en el template, extraer la lógica a un `computed` signal que devuelva un objeto de clases mantiene el template limpio y la lógica testeable.

    11. **Utilizar `takeUntilDestroyed()` para limpieza automática.** Esta función, disponible desde Angular 16, vincula automáticamente la vida de una suscripción al ciclo de vida del componente o servicio, eliminando la necesidad de gestionar manualmente Subjects de destrucción.

    12. **Separar estrictamente responsabilidades Smart/Presentational.** Esta separación no es opcional ni cosmética: es la base de una arquitectura mantenible. Un componente que inyecta `HttpClient` no debería contener clases de Tailwind en su template.

---

!!! warning "Errores frecuentes"

    1. **Mezclar lógica de negocio y presentación en el mismo componente.** Es el error más común: un componente que obtiene datos del servidor Y además tiene un template complejo con estilos condicionales. Este antipatrón produce componentes difíciles de testear, imposibles de reutilizar y propensos a conflictos en trabajo en equipo.

    2. **Usar `any` en inputs y outputs.** Tipificar correctamente los inputs y outputs con interfaces específicas es fundamental para la seguridad de tipos y la experiencia de desarrollo. El uso de `any` anula las ventajas de TypeScript y puede causar errores sutiles en tiempo de ejecución.

    3. **No limpiar suscripciones en `ngOnDestroy`.** Las suscripciones a Observables que no utilizan `takeUntilDestroyed()` deben cancelarse manualmente. Olvidar esta limpieza causa memory leaks y comportamientos impredecibles, especialmente en aplicaciones con navegación intensiva donde los componentes se crean y destruyen frecuentemente.

    4. **Usar `::ng-deep` sin necesidad.** Muchos desarrolladores recurren a `::ng-deep` por comodidad cuando otras soluciones son más adecuadas: variables CSS, inputs de estilo, o reestructuración para que el estilo se defina en el componente correcto. `::ng-deep` crea acoplamiento entre componentes y dificulta el mantenimiento.

    5. **Inicializar librerías externas en `ngOnInit` en lugar de `ngAfterViewInit`.** Intentar acceder a elementos del DOM en `ngOnInit` resultará en `undefined` porque la vista aún no se ha renderizado. Las librerías que requieren un elemento DOM deben inicializarse en `ngAfterViewInit`.

    6. **No utilizar `trackBy` en `@for` con listas mutables.** Sin una función `trackBy`, Angular destruye y recrea todos los elementos del DOM cuando la lista cambia, incluso si solo se modificó un elemento. Esto causa pérdida de rendimiento y pérdida de estado de interfaz (foco, scroll, animaciones en curso).

    7. **Exponer Signals mutables desde servicios sin `asReadonly()`.** Permitir que cualquier consumidor de un servicio modifique directamente una Signal rompe la encapsulación y hace imposible razonar sobre el flujo de estado. Los servicios deben exponer versiones de solo lectura de sus Signals.

    8. **Abusar de `EventEmitter` para comunicación entre componentes hermanos.** `EventEmitter` está diseñado para comunicación padre → hijo (input) e hijo → padre (output). Para comunicación entre hermanos, la solución correcta es un servicio compartido con Signals o un patrón de estado global.

    9. **Ignorar la accesibilidad en la arquitectura de componentes.** Los roles ARIA, la navegación por teclado y la gestión del foco no son añadidos posteriores; deben ser parte integral del diseño del componente desde el principio.

    10. **Anidar demasiados niveles de componentes sin necesidad.** Una jerarquía de componentes con 6 o 7 niveles de profundidad es difícil de razonar y depurar. Antes de crear un nuevo componente, evaluar si realmente aporta reutilización o simplificación.

    11. **Utilizar el constructor para lógica de inicialización compleja.** El constructor debe limitarse a la inyección de dependencias. Cualquier lógica de inicialización que dependa de inputs o que realice efectos secundarios debe ir en `ngOnInit`.

    12. **No configurar correctamente `content` en `tailwind.config` para proyectos Angular.** Si los paths de `content` no incluyen los archivos `.ts` y `.html` de los componentes, Tailwind no generará las clases utilitarias necesarias y la interfaz aparecerá sin estilos.

---

!!! abstract "Resumen"

    Esta unidad ha abordado la arquitectura de interfaces con Angular desde una perspectiva profesional y orientada a la práctica. Los puntos clave son:

    - Los **Standalone Components** simplifican la estructura del proyecto eliminando la necesidad de NgModules y haciendo explícitas las dependencias de cada componente de interfaz mediante imports declarados.

    - La integración de **Tailwind CSS** en plantillas Angular permite un desarrollo de interfaces más rápido y consistente, con clases utilitarias aplicadas directamente en el HTML y variantes arbitrarias para reaccionar a estados dinámicos de Angular.

    - Los hooks del ciclo de vida más relevantes para interfaces son `ngOnInit` (inicialización de datos y estado), `ngAfterViewInit` (manipulación del DOM e inicialización de librerías externas) y `ngOnDestroy` (limpieza de recursos).

    - La **arquitectura feature-based** organiza el proyecto por funcionalidades de negocio (`features/`), con componentes reutilizables en `shared/`, servicios globales en `core/` y el shell estructural en `layout/`, superando en escalabilidad a la arquitectura tradicional layer-based.

    - El patrón **Smart vs Presentational Components** es la piedra angular de una arquitectura de interfaz mantenible: los Smart Components contienen lógica y orquestan; los Presentational Components reciben datos y emiten eventos.

    - La comunicación entre componentes se articula mediante `@Input` (con soporte para required y transform), `@Output` (EventEmitter), `model()` para two-way binding y **Signals** para estado reactivo local y compartido.

    - `viewChild` y `contentChild` permiten acceder al DOM propio y al contenido proyectado respectivamente, habilitando patrones de interfaz como foco automático, inicialización de gráficos y coordinación de componentes compuestos.

---

## Recursos complementarios

### Documentación oficial
- Angular Documentation — Standalone Components: https://angular.dev/guide/components
- Angular Documentation — Signals: https://angular.dev/guide/signals
- Angular Documentation — Lifecycle Hooks: https://angular.dev/guide/components/lifecycle
- Tailwind CSS Documentation: https://tailwindcss.com/docs

### Libros recomendados
- "Angular Architecture and Best Practices" — Dan Wahlin (Pluralsight)
- "Clean Code" — Robert C. Martin (capítulos sobre arquitectura y responsabilidad única)
- "Atomic Design" — Brad Frost (principios de composición de componentes)

### Artículos y guías
- "Container and Presentation Components in Angular" — Angular University Blog
- "Angular Standalone Components: A Complete Guide" — This Dot Labs
- "Using Tailwind CSS with Angular" — Tailwind CSS Blog
- "State Management in Angular with Signals" — Angular Addicts

### Herramientas
- Angular DevTools: extensión del navegador para inspeccionar la jerarquía de componentes y la detección de cambios.
- Nx DevTools: para monorepos con múltiples aplicaciones y librerías Angular.
- Compodoc: generador de documentación para proyectos Angular.
- ESLint con plugin de Angular: análisis estático para detectar malas prácticas en componentes.

### Comunidad
- Angular Discord: comunidad oficial de Angular en Discord con canales específicos de arquitectura y componentes.
- r/Angular2 en Reddit: foro comunitario con discusiones técnicas diarias.
- Angular Meetups locales (muchos grupos en Andalucía: Málaga, Sevilla, Granada).

### Vídeos y cursos
- "Angular Signals: The Complete Guide" — Deborah Kurata (YouTube, freeCodeCamp)
- "Angular Architecture" — Manfred Steyer (Angular Vienna)
- "Tailwind CSS with Angular" — Academind (YouTube)
- "Smart vs Dumb Components Pattern" — Decoded Frontend (YouTube)
