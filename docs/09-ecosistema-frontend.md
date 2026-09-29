---
icon: lucide/network
---

# Unidad 9: Ecosistema Profesional del Desarrollo Frontend

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Instalar y configurar un **entorno completo de desarrollo frontend profesional** utilizando Node.js, Angular CLI, Tailwind CSS 4, ESLint y Prettier, verificando el correcto funcionamiento de todas las herramientas.
2. Explicar el rol de cada herramienta en el flujo de trabajo profesional de desarrollo de interfaces, desde el diseño en **Figma** hasta el despliegue de la aplicación.
3. Crear componentes Angular utilizando **TypeScript** con tipado estático, interfaces, genéricos y decoradores, comprendiendo las ventajas del **tipado fuerte** en aplicaciones empresariales.
4. Aplicar **Tailwind CSS 4** para el estilado de componentes, utilizando las clases utility-first y la nueva configuración basada en CSS con la directiva `@theme`.
5. Documentar y testear visualmente componentes de interfaz utilizando **Storybook**, comprendiendo su valor en el desarrollo colaborativo y la comunicación con stakeholders.
6. Describir el flujo de trabajo profesional completo "del diseño al código", identificando las herramientas involucradas en cada etapa y los artefactos que se generan.
7. Utilizar **Git** y **GitHub** para el control de versiones de proyectos frontend, aplicando flujos de trabajo con ramas y pull requests.
8. Valorar críticamente la elección de herramientas del ecosistema frontend, argumentando ventajas e inconvenientes de cada alternativa en diferentes contextos de proyecto.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 1** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 1.** Genera interfaces gráficos de usuario mediante editores visuales utilizando las funcionalidades del editor y adaptando el código generado.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE a) Se han analizado las herramientas y librerías disponibles para la generación de interfaces gráficos (Angular, Tailwind CSS, Figma, Storybook, Node.js, npm, Git).

> Nota: esta unidad sienta el contexto profesional y del ecosistema de herramientas que se utilizarán a lo largo del módulo; el análisis comparado de herramientas y librerías corresponde al CE a) del RA 1.

!!! note "Conocimientos previos"

    Para el correcto aprovechamiento de esta unidad, el alumnado debe contar con:

    - Conocimientos de **HTML5 y CSS3** a nivel intermedio: estructura semántica de documentos, selectores CSS avanzados (combinadores, pseudo-clases, pseudo-elementos), modelo de caja, posicionamiento (static, relative, absolute, fixed, sticky), y principios de diseño responsive con media queries.
    - Nociones fundamentales de **JavaScript**: variables (let, const), funciones (declaración, expresión, arrow functions), arrays y sus métodos (map, filter, reduce, forEach), objetos literales, promesas y async/await, y manejo básico del DOM (querySelector, addEventListener).
    - Experiencia práctica con **Visual Studio Code** como editor de código, incluyendo el uso de extensiones y la terminal integrada.
    - Familiaridad con la **terminal de comandos** (Bash/Zsh en Linux/macOS, PowerShell o Git Bash en Windows) para navegación de directorios, creación y eliminación de archivos, y ejecución de comandos.
    - Conceptos elementales de control de versiones con **Git**: init, clone, add, commit, push, pull, y la plataforma **GitHub** para alojamiento de repositorios remotos.

    Se realizará una actividad de diagnóstico inicial consistente en un breve cuestionario y un ejercicio práctico de maquetación HTML+CSS para verificar estos conocimientos previos y, en caso necesario, derivar al alumnado a recursos de refuerzo personalizados.

## Contenidos

**Bloque 1: Node.js y el gestor de paquetes npm**
- **Qué es Node.js**: runtime de JavaScript fuera del navegador, arquitectura basada en eventos, motor V8.
- **npm (Node Package Manager)**: repositorio de paquetes, gestión de dependencias, ficheros package.json y package-lock.json.
- **Dependencias de desarrollo** (devDependencies) vs **dependencias de producción** (dependencies).
- **Scripts npm**: automatización de tareas (start, build, test, lint, format).
- **npx**: ejecución de paquetes sin instalación global.
- **Gestión de versiones semánticas (SemVer)**: major.minor.patch.
- **.gitignore**: archivos y directorios a excluir del control de versiones (node_modules, dist, .env).

**Bloque 2: Angular: el framework completo para interfaces empresariales**
- **Filosofía y posicionamiento en el ecosistema**: comparativa con React, Vue, Svelte, Solid.
- **Arquitectura**: módulos (NgModules) vs componentes standalone, el cambio de paradigma.
- **Angular CLI**: scaffolding (ng new), generación de componentes/servicios/directivas/pipes (ng generate), servidor de desarrollo (ng serve), build de producción (ng build), testing (ng test).
- **TypeScript en Angular**: tipado de inputs y outputs, interfaces para modelos de datos, genéricos en servicios HTTP, decoradores (@Component, @Injectable, @Input, @Output).
- **Angular Signals**: signal(), computed(), effect(), actualización con set/update/mutate. Comparativa con RxJS y Zone.js.
- **Estructura de un proyecto Angular**: src/app, assets, environments, angular.json, tsconfig.json.
- **Versiones de Angular**: historial de cambios clave desde Angular 2 hasta la última versión estable (v19 en 2025).

**Bloque 3: TypeScript como lenguaje fundamental**
- **Qué es TypeScript**: superset tipado de JavaScript desarrollado por Microsoft.
- **Compilación**: de .ts a .js mediante tsc (TypeScript Compiler).
- **Sistema de tipos**: tipos primitivos (string, number, boolean, null, undefined), tipos complejos (arrays, tuples, enums, objetos literales tipados), tipos especiales (any, unknown, void, never).
- **Interfaces y type aliases**: definición de contratos, propiedades opcionales, readonly, extensión de interfaces, tipos de unión e intersección.
- **Genéricos**: funciones, interfaces y clases genéricas, restricciones con extends.
- **Decoradores**: qué son, cómo funcionan (aún en stage 3 de ECMAScript), uso en Angular.
- **tsconfig.json**: configuración del compilador (target, module, strict, paths).
- Por qué **TypeScript** es fundamental en el desarrollo de interfaces: detección temprana de errores, autocompletado en IDE, documentación viva del código, refactorización segura, mantenibilidad en equipos grandes.

**Bloque 4: Tailwind CSS 4 - Sistema de estilos utility-first**
- **Filosofía utility-first**: clases atómicas que aplican una única propiedad CSS, composición en el HTML.
- **Ventajas frente a CSS tradicional, SASS/SCSS y CSS-in-JS**: sin cambios de contexto, sin nombrar clases, estilos predecibles y fáciles de leer en el template, bundle CSS mínimo (solo las clases usadas), consistencia forzada (sistema de diseño implícito a través de la configuración).
- **Novedades de Tailwind CSS 4**:
  - **Configuración 100% CSS**: ya no se necesita `tailwind.config.js` (aunque sigue siendo compatible). La configuración se hace mediante CSS con `@theme`, `@import "tailwindcss"`, etc.
  - Integración con **Vite** como plugin nativo.
  - **Sistema de capas en CSS** (@layer base, components, utilities).
  - Nuevas utilidades y mejoras de rendimiento.
- **Clases utilitarias principales categorizadas**:
  - **Layout** (flex, grid, container, columns, display, position, z-index).
  - **Spacing** (padding, margin, gap, space-between).
  - **Sizing** (width, height, min/max).
  - **Typography** (font-family, font-size, font-weight, line-height, letter-spacing, text-align, text-color, text-decoration).
  - **Backgrounds** (background-color, background-image, gradient).
  - **Borders** (border-width, border-color, border-radius, outline, ring).
  - **Effects** (box-shadow, opacity, blend mode).
  - **Transitions y Animations** (transition, animate).
  - **Interactivity** (cursor, user-select, pointer-events, scroll behavior).
  - **Responsive Design** (prefijos sm:, md:, lg:, xl:, 2xl: aplicando mobile-first).
- **Configuración del tema** con `@theme`: personalización de colores, tipografía, espaciado, breakpoints.
- Directiva `@apply`: **uso y controversia** (cuándo sí, cuándo no).
- **Modo oscuro** con la clase `dark:` y la estrategia `class` o `media`.
- **Plugin oficial de Tailwind CSS para Vite**.

**Bloque 5: Figma - Diseño colaborativo**
- **Rol de Figma en el ecosistema profesional**: herramienta de diseño basada en navegador, colaboración en tiempo real, único source of truth del diseño.
- **Comparativa con alternativas**: Sketch (macOS, no colaborativo nativo), Adobe XD (en desuso tras la compra de Figma por Adobe -frustrada- y el giro estratégico).
- **Figma en modo desarrollador (Dev Mode)**: inspección de medidas, colores, tipografías, assets exportables, snippets de código (CSS, Tailwind, SwiftUI, Compose).
- **Plugins relevantes para desarrolladores**: Tailwind CSS, html.to.design (convierte web a Figma), Stark (accesibilidad), Iconify.
- **Handoff diseño-desarrollo**: cómo los diseñadores entregan los diseños a los desarrolladores. Buenas prácticas para un handoff eficiente.
- La **Unidad 4** está dedicada íntegramente a Figma.

**Bloque 6: Storybook - Desarrollo y documentación de componentes**
- **Qué es Storybook**: entorno aislado para desarrollar, probar y documentar componentes de interfaz.
- **Por qué es estándar en la industria**: permite desarrollar componentes de forma aislada (sin necesidad de navegar por la app completa), documenta visualmente el sistema de diseño (catálogo vivo), facilita el testing visual (Chromatic, Percy), mejora la comunicación entre diseño y desarrollo.
- **Stories**: definición (archivos *.stories.ts), estructura (args, argTypes, decorators, parameters).
- **Addons esenciales**: Controls (interactividad con props), Actions (registro de eventos), Docs (documentación automática), Viewport (testeo responsive), Accessibility (auditoría automática), Figma (incrustar diseños en Storybook).
- **Integración de Storybook con Angular**: soporte nativo, configuración con storybookConfig, compatibilidad con standalone components.
- **Flujo de trabajo con Storybook**: desarrollador crea componente en Angular, escribe sus stories, ejecuta Storybook localmente, comparte el enlace con diseñador, diseñador valida, desarrollador itera. Reducción de ciclos de feedback.
- **Chromatic**: servicio cloud de Storybook para revisión visual, UI tests y capturas de pantalla automatizadas.

**Bloque 7: Electron - Aplicaciones de escritorio con tecnologías web**
- **Arquitectura de Electron**: proceso principal (Main) con Node.js, procesos renderizadores (Renderer) con Chromium, IPC (Inter-Process Communication) para comunicación entre procesos.
- **Configuración de un proyecto Electron**: instalación, main.js, preload.js, BrowserWindow.
- **Integración con Angular**: empaquetado de la aplicación Angular como Electron app. Herramientas como electron-builder para generar instaladores (Windows .exe/.msi, macOS .dmg/.pkg, Linux .AppImage/.deb/.rpm).
- **Seguridad en Electron**: contexto isolation, nodeIntegration deshabilitado, preload scripts controlados, Content Security Policy (CSP).
- **Casos de uso reales de Electron** (analizados en detalle): Visual Studio Code (proceso principal gestiona extension host, terminal, sistema de archivos; procesos renderizadores para cada ventana del editor), Discord (proceso principal gestiona notificaciones del sistema, estado de presencia; renderizadores para la UI de chat).
- **Cuándo usar Electron y cuándo no**: electron para apps multiplataforma de escritorio con necesidades web, no electron para apps que requieran ultra-bajo consumo de recursos o máximo rendimiento nativo (juegos, edición de vídeo profesional).

**Bloque 8: Herramientas de productividad y flujo de trabajo profesional**
- **Visual Studio Code**: extensiones esenciales para el stack:
  - **Angular Language Service** (autocompletado, navegación en templates, diagnóstico de errores).
  - **Tailwind CSS IntelliSense** (autocompletado de clases, hover preview, linting).
  - **ESLint** (integración en editor, corrección automática al guardar).
  - **Prettier** (formateo automático de código, configuración .prettierrc).
  - **Figma for VS Code** (incrustar diseños de Figma en el editor).
  - **GitLens** (información de Git inline, blame, historial).
  - **GitHub Copilot** o alternativa gratuita (asistente de código AI).
- **Git y GitHub**:
  - **Repaso**: clone, add, commit (conventional commits: feat:, fix:, docs:, refactor:, style:, test:, chore:), push, pull, fetch.
  - **Ramas** (feature branches, main/master, develop, release).
  - **Pull requests**: creación, revisión de código, resolución de conflictos.
  - **.gitignore** para proyectos Angular + Tailwind (node_modules, dist, .angular, .env, etc.).
  - **GitHub Actions**: integración continua (CI) básica para lint, test y build.
- **ESLint y Prettier**:
  - **ESLint**: qué es, cómo funciona (reglas, plugins, parser TypeScript), configuración (.eslintrc.json o eslint.config.js en nuevo formato flat config).
  - **Prettier**: qué es, filosofía (opinionated, decisions made), configuración (.prettierrc, .prettierignore), integración con ESLint (eslint-config-prettier para evitar conflictos).
  - **Husky y lint-staged**: ejecución de linting y formateo antes del commit (pre-commit hooks).
- **Metodologías ágiles en el desarrollo de interfaces**:
  - **Scrum**: roles (Product Owner, Scrum Master, Development Team), ceremonias (Sprint Planning, Daily Standup, Sprint Review, Sprint Retrospective), artefactos (Product Backlog, Sprint Backlog, Increment).
  - **Kanban**: tablero visual (To Do, In Progress, Review, Done), limitación de WIP (Work In Progress).
  - Cómo las metodologías ágiles afectan al desarrollo de interfaces: entregas incrementales de componentes, iteración sobre feedback de diseño, integración continua del sistema de diseño.

**Bloque 9: Configuración completa del entorno de desarrollo**
- **Guía paso a paso** (detallada en los ejemplos guiados):
  1. Instalación de Node.js (LTS) con nvm (Node Version Manager).
  2. Verificación: node --version, npm --version.
  3. Instalación global de Angular CLI: npm install -g @angular/cli.
  4. Creación de proyecto Angular con Tailwind CSS 4: ng new mi-proyecto --standalone --style css.
  5. Instalación de Tailwind CSS 4 como plugin Vite.
  6. Configuración de Tailwind en styles.css (@import "tailwindcss"; @theme).
  7. Verificación: crear un componente de prueba con clases Tailwind.
  8. Instalación de ESLint (si no viene con Angular) y Prettier.
  9. Configuración de reglas y scripts npm (lint, format).
  10. Inicialización de Git y primer commit.
  11. Instalación de Storybook: npx storybook init (para Angular).
  12. Configuración de Storybook con Tailwind.
  13. Verificación: story de un componente simple (Button).
  14. Creación de repositorio en GitHub y primer push.

## Desarrollo teórico

### 1. Node.js y npm: la base del ecosistema

**Node.js** representa uno de los hitos tecnológicos más importantes en el desarrollo web moderno. Creado por Ryan Dahl en 2009, permite ejecutar código JavaScript fuera del navegador, abriendo la posibilidad de desarrollar servidores, herramientas de línea de comandos y scripts de automatización con el mismo lenguaje utilizado en el frontend. Su arquitectura asíncrona y basada en eventos, sobre el motor **V8** de Google (el mismo que utiliza Chrome), lo hace especialmente eficiente para aplicaciones con muchas conexiones concurrentes.

!!! info "Dato clave"

    Pero la verdadera revolución de Node.js no fue el runtime en sí, sino el ecosistema que se construyó a su alrededor. **npm (Node Package Manager)**, lanzado en 2010, es hoy el mayor registro de paquetes de software del mundo, con más de dos millones de paquetes disponibles. Para el desarrollo de interfaces, cada herramienta que utilizamos está disponible como paquete npm: Angular, Tailwind CSS, TypeScript, ESLint, Prettier, Storybook, Electron, Cypress, Playwright... todas son dependencias gestionadas por npm.

**package.json: el manifiesto del proyecto**

Cada proyecto Node.js contiene un archivo `package.json` que actúa como manifiesto: nombre del proyecto, versión, descripción, scripts personalizados, dependencias de producción, dependencias de desarrollo y metadatos de configuración. Este archivo debe versionarse en **Git** (a diferencia de `node_modules/`, que debe excluirse mediante `.gitignore`). Al clonar un proyecto, `npm install` reconstruye el directorio `node_modules` leyendo las dependencias declaradas.

La distinción entre dependencias de producción y desarrollo es crucial:

- **dependencies:** Paquetes requeridos en tiempo de ejecución. Por ejemplo, Angular es una dependencia de producción (el código de Angular se ejecuta en el navegador del usuario). `npm install angular --save` (o `-S`, aunque ahora es el comportamiento por defecto).

- **devDependencies:** Paquetes requeridos solo durante el desarrollo o build. Por ejemplo: TypeScript (el navegador ejecuta JavaScript compilado, no TypeScript), Tailwind CSS (genera CSS durante el build), ESLint, Prettier, Jest, Storybook. Se instalan con `npm install --save-dev` (o `-D`).

**Scripts npm**

La sección `scripts` de `package.json` permite definir comandos personalizados ejecutables mediante `npm run <script>`. Esta es una de las funcionalidades más valiosas de npm porque encapsula la complejidad de las herramientas subyacentes y unifica la interfaz de comandos para todo el equipo. Un proyecto Angular típico define scripts como:

```json
{
  "scripts": {
    "start": "ng serve --open",
    "build": "ng build --configuration production",
    "watch": "ng build --watch --configuration development",
    "test": "ng test",
    "lint": "ng lint",
    "format": "prettier --write \"src/**/*.{ts,html,css}\"",
    "storybook": "storybook dev -p 6006",
    "build-storybook": "storybook build"
  }
}
```

**npx: ejecución sin instalación**

npx, incluido con npm desde la versión 5.2, permite ejecutar paquetes sin instalarlos globalmente. Es la forma recomendada de usar herramientas como `@angular/cli` para crear proyectos (sin necesidad de `npm install -g`). Ejemplo: `npx @angular/cli new mi-proyecto`. También se usa para ejecutar Storybook, Prettier u otras herramientas sin preocuparse de si están instaladas globalmente.

**Versionado semántico (SemVer)**

El ecosistema npm sigue el versionado semántico: `MAJOR.MINOR.PATCH`. Los cambios en MAJOR indican **breaking changes** (API incompatible), MINOR indica nuevas funcionalidades retrocompatibles y PATCH indica correcciones de bugs. El operador ^ en `package.json` (ej: `"angular": "^19.0.0"`) permite actualizaciones automáticas de MINOR y PATCH, pero no de MAJOR. El operador ~ ("~19.0.0") solo permite PATCH. Entender SemVer es esencial para gestionar dependencias sin sorpresas.

### 2. Angular: el framework completo

**Angular** (sin el sufijo "JS", esa fue la primera versión de 2010) es el framework elegido para este módulo por varias razones pedagógicas y profesionales. En primer lugar, su carácter completo (*batteries included*) nos permite concentrarnos en aprender el desarrollo de interfaces sin tener que investigar, evaluar e integrar múltiples bibliotecas separadas para enrutamiento, gestión de estado, HTTP, formularios y testing. En segundo lugar, su uso de **TypeScript** como lenguaje nativo nos introduce en el tipado estático, una competencia profesional cada vez más demandada. En tercer lugar, su arquitectura modular y su inyección de dependencias enseñan patrones de diseño de software aplicables más allá del frontend. Por último, Angular es ampliamente utilizado en el sector empresarial andaluz y español, ofreciendo oportunidades laborales reales a los egresados.

**Arquitectura: de NgModules a Standalone**

Históricamente, Angular organizaba el código en **NgModules** (clases decoradas con `@NgModule`), que agrupaban componentes, directivas, pipes y servicios relacionados. Cada aplicación requería al menos un módulo raíz (`AppModule`) y opcionalmente módulos de funcionalidad (feature modules) para organizar el código.

Desde Angular 14 (2022), se introdujeron los **Standalone Components** —componentes que no necesitan ser declarados en un NgModule— y con Angular 17 se convirtieron en el comportamiento por defecto al crear nuevos componentes. Esta evolución simplifica la estructura del proyecto, facilita el lazy loading y reduce el boilerplate.

Un componente standalone se reconoce por la propiedad `standalone: true` en los metadatos del decorador `@Component`, y por importar explícitamente las dependencias que necesita (módulos de Angular como `CommonModule`, `ReactiveFormsModule`, u otros componentes):

```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-mi-componente',
  standalone: true,
  imports: [CommonModule],
  template: `<p>Componente standalone</p>`,
  styles: []
})
export class MiComponente { }
```

**Angular CLI: productividad desde el inicio**

**Angular CLI** (Command Line Interface) es una herramienta de línea de comandos que automatiza las tareas más comunes del desarrollo con Angular. Sus comandos principales son:

- `ng new <nombre>`: Genera un nuevo proyecto Angular con estructura de directorios, configuración de TypeScript, scripts npm y dependencias instaladas. Las opciones relevantes son `--standalone` (proyecto sin NgModules), `--style` (css, scss, sass, less), `--ssr` (Server-Side Rendering) y `--strict` (TypeScript strict mode activado).

- `ng generate <esquema> <nombre>` (abreviado `ng g`): Genera código según esquemas predefinidos. Los esquemas más usados son component, service, directive, pipe, guard, interceptor, interface y enum. Cada uno coloca los archivos generados en el directorio correcto y actualiza las declaraciones necesarias.

- `ng serve`: Levanta un servidor de desarrollo con recarga en caliente (Hot Module Replacement) y compilación incremental. Es el comando que usarás durante el desarrollo para ver tus cambios en tiempo real en `http://localhost:4200`.

- `ng build`: Compila la aplicación para producción. El resultado se escribe en `dist/`. La opción `--configuration production` activa optimizaciones como minificación, tree-shaking, Ahead-of-Time compilation y cache busting con hashes en los nombres de archivo.

- `ng test`: Ejecuta tests unitarios (por defecto con Karma y Jasmine, aunque configurable para Jest).

- `ng lint`: Ejecuta el linter (TSLint en versiones antiguas, ESLint a partir de Angular 12).

**Angular Signals: reactividad moderna**

Los **Signals** representan el cambio más significativo en la reactividad de Angular desde su creación. Tradicionalmente, Angular detectaba cambios mediante **Zone.js**, una biblioteca que "parcheaba" todas las APIs asíncronas del navegador (setTimeout, Promise, eventos, XMLHttpRequest) y disparaba la detección de cambios en todo el árbol de componentes cada vez que algo podría haber cambiado. Esto funcionaba, pero era ineficiente (se revisaban componentes que no habían cambiado) y creaba una dependencia de Zone.js.

Los Signals, inspirados por frameworks como Solid.js, Svelte y Preact Signals, introducen un modelo de **reactividad fina y explícita**:

```typescript
import { signal, computed, effect } from '@angular/core';

// Signal escribible
const contador = signal(0);
contador.set(5);       // Establecer valor
contador.update(n => n + 1);  // Actualizar basándose en valor anterior
contador.mutate(n => n++);    // Mutar objeto mutable (no recomendado para primitivos)

// Signal computada (derivada, solo lectura)
const doble = computed(() => contador() * 2);
// Se recalcula automáticamente cuando alguna de las signals que lee cambia.

// Efecto (reacción lateral)
effect(() => {
  console.log(`Contador: ${contador()}, Doble: ${doble()}`);
  // Se ejecuta cuando contador o doble cambian.
  // Angular maneja la suscripción/desuscripción automáticamente.
});
```

Las ventajas de Signals sobre Zone.js son sustanciales: detección de cambios más eficiente (solo se re-renderizan los componentes que realmente cambiaron), reactividad explícita y predecible (no hay "magia" de Zone.js), código más legible y depurable, y mejor integración con **RxJS** (los signals pueden convertirse a Observables y viceversa mediante las funciones `toObservable()` y `toSignal()`).

En este módulo adoptaremos Signals como mecanismo principal de gestión de estado local en componentes, reservando RxJS para flujos asíncronos complejos (comunicación HTTP, WebSockets, debounce de búsquedas, combinación de streams).

### 3. TypeScript: tipado estático para interfaces robustas

**JavaScript** es un lenguaje dinámicamente tipado: las variables no tienen tipo fijo, lo que permite flexibilidad pero también provoca errores difíciles de detectar en tiempo de desarrollo (pasas un string donde se esperaba un número, accedes a una propiedad de undefined, olvidas pasar un argumento obligatorio). Estos errores, en aplicaciones grandes con múltiples desarrolladores, se vuelven muy costosos.

**TypeScript**, desarrollado por Microsoft y liderado por el mismo creador de C# y Delphi (Anders Hejlsberg), añade un sistema de tipos estático opcional sobre JavaScript. ==Todo código JavaScript válido es código TypeScript válido==, pero TypeScript añade anotaciones de tipo que son eliminadas durante la compilación (el navegador nunca ejecuta TypeScript, sino el JavaScript resultante).

**Sistema de tipos**

Los tipos básicos incluyen los primitivos de JavaScript más algunos añadidos:

```typescript
let nombre: string = "María";
let edad: number = 25;
let activo: boolean = true;
let fecha: Date = new Date();
let cualquiera: any = 4;      // Desactiva el tipado (evitar siempre que sea posible)
let desconocido: unknown = 4; // Como any, pero obliga a type narrowing antes de usar
let sinValor: void = undefined;// Usado para funciones que no retornan nada
let nuncaTermina: never;       // Funciones que lanzan excepción o bucle infinito

// Arrays
let numeros: number[] = [1, 2, 3];
let tupla: [string, number] = ["hola", 42];

// Enums
enum EstadoTarea {
  Pendiente = "PENDING",
  EnProgreso = "IN_PROGRESS",
  Completada = "COMPLETED"
}
```

**Interfaces y tipos**

Las interfaces definen la forma de un objeto, estableciendo un **contrato** que otros objetos deben cumplir:

```typescript
interface Usuario {
  id: number;
  nombre: string;
  email: string;
  edad?: number;           // Propiedad opcional
  readonly fechaAlta: Date; // Solo lectura (no se puede modificar tras creación)
}

function saludar(usuario: Usuario): string {
  return `Hola, ${usuario.nombre}`;
}

// La función solo acepta objetos que cumplan la interfaz Usuario
```

Los **type aliases** permiten crear tipos personalizados, incluyendo uniones e intersecciones:

```typescript
type Estado = "pendiente" | "en_curso" | "completado"; // Union type
type Coordenadas = [number, number];                     // Tuple type
type UsuarioAdmin = Usuario & { rol: "admin" };         // Intersection type
```

**Genéricos**

Los genéricos permiten escribir funciones, clases e interfaces que trabajan con cualquier tipo, manteniendo la **seguridad de tipos**:

```typescript
function primerElemento<T>(array: T[]): T | undefined {
  return array[0];
}

const numero = primerElemento([1, 2, 3]); // TypeScript infiere: number
const texto = primerElemento(["a", "b"]); // TypeScript infiere: string

interface RespuestaAPI<T> {
  datos: T;
  mensaje: string;
  codigo: number;
}

type RespuestaUsuarios = RespuestaAPI<Usuario[]>;
```

**Decoradores**

Los decoradores son una característica experimental de TypeScript (**Stage 3 en TC39**) que Angular utiliza intensivamente. Un decorador es una función que modifica una clase, método, propiedad o parámetro:

```typescript
@Component({
  selector: 'app-boton',
  standalone: true,
  template: `<button class="..."><ng-content /></button>`
})
class BotonComponent {
  @Input() tipo: 'primary' | 'secondary' = 'primary';
  @Output() click = new EventEmitter<void>();
}
```

`@Component`, `@Input`, `@Output`, `@Injectable`, `@HostListener` son decoradores proporcionados por Angular. Como desarrollador de interfaces, los usarás constantemente pero raramente escribirás decoradores propios (a menos que desarrolles librerías).

**Por qué TypeScript en desarrollo de interfaces**

1. **Detección temprana de errores:** Errores de tipo se detectan en el editor, no en tiempo de ejecución. Si pasas un objeto con forma incorrecta a un componente, TypeScript te avisa inmediatamente.

2. **Autocompletado y documentación:** El editor conoce la forma de los objetos y puede sugerir propiedades, métodos y parámetros. Esto acelera el desarrollo y reduce la consulta a documentación externa.

3. **Refactorización segura:** Renombrar una propiedad o método en una interfaz actualiza todas las referencias de forma segura. No habrá propiedades huérfanas ni errores silenciosos.

4. **Mantenibilidad en equipos:** En equipos grandes, las interfaces actúan como documentación viva y contratos entre componentes. Un nuevo desarrollador puede entender la forma de los datos navegando las interfaces.

5. **Integración con Angular:** Angular está escrito en TypeScript y sus APIs aprovechan al máximo el sistema de tipos. Usar JavaScript plano con Angular es posible pero desaprovecha la mayoría de las ventajas del framework.

### 4. Tailwind CSS 4: estilado utility-first

**Tailwind CSS** representa un cambio de paradigma en la forma de escribir CSS. Frente al enfoque tradicional (escribir CSS semántico con clases con nombre, tipo `.card-header`, `.btn-primary`, `.sidebar`, y luego aplicar esas clases en el HTML), Tailwind propone ==clases utilitarias de una sola propiedad que se aplican directamente en el HTML==.

**Filosofía utility-first**

Un botón con CSS tradicional:
```css
.btn-primary {
  background-color: #3b82f6;
  color: white;
  font-weight: 600;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: background-color 0.15s;
}
.btn-primary:hover {
  background-color: #2563eb;
}
```

El mismo botón con Tailwind:
```html
<button class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-md transition-colors duration-150">
  Click me
</button>
```

Las críticas iniciales a Tailwind ("ensucia el HTML", "parece inline styles", "si cambio el diseño tengo que cambiar 100 archivos") han sido refutadas por la práctica profesional y el respaldo mayoritario de la industria. La realidad es que:

- **Sin cambio de contexto:** No necesitas nombrar clases en CSS y luego recordar esos nombres en el HTML. Todo está en el mismo archivo, visible y modificable.
- **Estilos predecibles:** Leyendo el HTML sabes exactamente cómo se ve el elemento. No hay herencia inesperada ni especificidad en cascada que produzca sorpresas.
- **Bundle CSS mínimo:** Tailwind genera solo las clases que realmente usas en tu HTML. Un proyecto típico produce un CSS de 5-10 KB comprimido (gzip), frente a cientos de KB de CSS tradicional que crece indefinidamente.
- **Consistencia forzada:** Tailwind proporciona un sistema de diseño implícito (escala de colores, tamaños, espaciado) que naturalmente homogeniza el estilo visual sin requerir reuniones de diseño para cada decisión de padding.

**Novedades de Tailwind CSS 4**

La versión 4 de **Tailwind CSS**, publicada en 2024, introduce cambios arquitectónicos significativos que simplifican la configuración y mejoran el rendimiento:

1. **Configuración con CSS en lugar de JavaScript:** Se elimina la necesidad del archivo `tailwind.config.js`. La configuración se realiza directamente en el CSS mediante las nuevas directivas:

```css
@import "tailwindcss";

@theme {
  --color-primary: #3b82f6;
  --color-primary-dark: #2563eb;
  --font-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;
  --spacing-gutter: 1.5rem;
}
```

2. **Plugin Vite nativo:** Tailwind 4 se integra como un plugin Vite, sin necesidad de PostCSS como paso separado. Esto mejora significativamente los tiempos de compilación (hasta 10x más rápido en builds incrementales).

3. **Sistema de capas mejorado:** `@layer base`, `@layer components`, `@layer utilities` permiten organizar el CSS personalizado, controlando la especificidad y el orden de aplicación.

4. **Rendimiento:** El nuevo motor (denominado "Oxide") está escrito en Rust y ofrece un rendimiento sustancialmente superior al motor JavaScript anterior (que a su vez ya era rápido).

**Clases utilitarias esenciales**

!!! tip "Consejo"

    No es necesario memorizar todas las clases de Tailwind (la extensión **IntelliSense** para VS Code las autocompleta). Pero es importante comprender la nomenclatura y el sistema subyacente:

    - **Colores:** `bg-{color}-{tono}`, `text-{color}-{tono}`, `border-{color}-{tono}`, `ring-{color}-{tono}`. Ejemplo: `bg-red-500`. Los tonos van de 50 (más claro) a 950 (más oscuro).

    - **Espaciado:** `p-{tamaño}` (padding todos lados), `pt-{tamaño}` (padding-top), `pr`, `pb`, `pl`, `px` (horizontal), `py` (vertical). Ídem para margin con `m-`. Los tamaños van de 0 a 96 (en incrementos de 0.25rem).

    - **Tipografía:** `text-{tamaño}` (xs, sm, base, lg, xl, 2xl...), `font-{peso}` (thin, light, normal, medium, semibold, bold, extrabold, black), `leading-{interlineado}`, `tracking-{letter-spacing}`.

    - **Responsive con mobile-first:** `sm:{clase}`, `md:{clase}`, `lg:{clase}`, `xl:{clase}`, `2xl:{clase}`. La clase base se aplica a móviles; los prefijos añaden/quitan estilos en pantallas más grandes. Ejemplo: `class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3"`.

    - **Estados:** `hover:{clase}`, `focus:{clase}`, `active:{clase}`, `disabled:{clase}`, `dark:{clase}`, `group-hover:{clase}` (cuando el padre tiene clase group y se hace hover), `peer-focus:{clase}` (cuando un hermano tiene clase peer y recibe foco).

**Directiva @apply: uso responsable**

La directiva `@apply` permite componer clases Tailwind en CSS personalizado:

```css
.btn-primary {
  @apply bg-blue-500 text-white font-semibold py-2 px-4 rounded-lg hover:bg-blue-600 transition-colors;
}
```

!!! tip "Recomendación"

    **Adam Wathan**, creador de Tailwind, recomienda usar @apply con moderación, principalmente cuando se necesita reutilizar un conjunto de clases y no es práctico crear un componente (por ejemplo, estilos para contenido generado por un CMS o markdown). La postura oficial de Tailwind es "prefiere componentes sobre @apply". Dado que Angular nos proporciona componentes como unidad natural de reutilización, en este módulo usaremos @apply excepcionalmente y priorizaremos la composición de clases directamente en los templates.

### 5. Figma: diseño colaborativo en la nube

**Figma** ha sustituido a herramientas como Sketch y Adobe XD como el estándar de facto para diseño de interfaces. Hay dos razones principales para su dominio: es una aplicación web (no requiere instalación, funciona en cualquier sistema operativo, los archivos están siempre sincronizados en la nube) y permite colaboración en tiempo real (varios diseñadores —y desarrolladores— pueden trabajar simultáneamente sobre el mismo archivo, como Google Docs pero para diseño).

!!! info "Definición"

    Para los desarrolladores de interfaces, Figma es mucho más que una herramienta de diseño. Es la **fuente de verdad del diseño** (*source of truth*): el lugar donde encontramos los diseños aprobados, las especificaciones de colores y tipografías, las medidas exactas, los assets exportables, y el prototipo navegable para entender flujos de interacción.

Figma ofrece un modo específico para desarrolladores (**Dev Mode**) accesible mediante un toggle en la interfaz, que proporciona:
- Medidas en píxeles entre elementos.
- Código CSS generado automáticamente para cada elemento seleccionado (con soporte para Tailwind CSS mediante plugin o configuración).
- Valores de variables (colores, tipografías, espaciados) con nombres semánticos.
- Assets descargables en SVG, PNG, JPG, PDF.
- Comparación automática de cambios entre versiones del diseño (como un diff de Git pero visual).

La Unidad 4 se dedica íntegramente a Figma, donde se diseñan componentes, se crean sistemas de diseño con variables y se preparan diseños para la implementación. En esta unidad es suficiente entender su rol en el ecosistema y familiarizarse con su interfaz.

### 6. Storybook: desarrollo aislado y documentación de componentes

En el desarrollo tradicional, para ver visualmente un componente en sus diferentes estados (un botón: normal, hover, focus, disabled, loading; variantes: primary, secondary, outline, ghost; tamaños: sm, md, lg) el desarrollador debe navegar por la aplicación hasta encontrar la pantalla donde aparece ese botón, o bien crear páginas de prueba temporales. Este proceso es ineficiente, no escalable y no documenta el componente para otros miembros del equipo.

**Storybook** resuelve este problema proporcionando ==un entorno aislado (sandbox) donde cada componente se desarrolla, prueba y documenta de forma independiente==. Se ejecuta como una aplicación web separada (por defecto en `http://localhost:6006`) que muestra una galería navegable de todos los componentes del proyecto.

**Conceptos clave de Storybook**

- **Story:** Cada variante o estado de un componente se define como una "story". Una story es una función que devuelve el componente renderizado con unas props (en Angular, inputs) específicas. Por ejemplo, el componente Button tendrá stories para Primary, Secondary, Outline (variantes), para Small, Medium, Large (tamaños), y para Default, Hover, Disabled, Loading (estados).

- **Args:** Los argumentos que recibe la story. En el panel de Controls de Storybook, estos args se convierten en controles interactivos (text inputs, selectores, toggles, sliders de números y colores) que permiten modificar el componente en tiempo real sin escribir código. Un diseñador o product manager puede "jugar" con el componente y ver todos sus estados sin necesidad de saber programar.

- **Docs:** Storybook genera automáticamente documentación para cada componente a partir de sus stories, incluyendo tabla de props (inputs/outputs en Angular), descripción (tomada de JSDoc/TSDoc en el código fuente), y ejemplos renderizados.

- **Addons:** El ecosistema de addons extiende Storybook con funcionalidades como: pruebas de accesibilidad automatizadas (`@storybook/addon-a11y`), medición de viewports responsive (`@storybook/addon-viewport`), registro de eventos y acciones (`@storybook/addon-actions`), integración con Figma (incrustar el diseño original junto al componente implementado para comparar), temas (light/dark mode) y testing visual con Chromatic.

**Storybook con Angular**

Storybook tiene **soporte nativo** para Angular, configurable con un simple comando (`npx storybook@latest init`). Las stories se escriben en archivos `*.stories.ts` junto al componente:

```typescript
import type { Meta, StoryObj } from '@storybook/angular';
import { ButtonComponent } from './button.component';

const meta: Meta<ButtonComponent> = {
  title: 'UI/Button',
  component: ButtonComponent,
  tags: ['autodocs'],
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'outline', 'ghost'],
    },
    size: {
      control: 'select',
      options: ['sm', 'md', 'lg'],
    },
  },
};

export default meta;
type Story = StoryObj<ButtonComponent>;

export const Primary: Story = {
  args: {
    variant: 'primary',
    size: 'md',
    label: 'Button',
  },
};

export const Secondary: Story = {
  args: {
    variant: 'secondary',
    size: 'md',
    label: 'Button',
  },
};
```

**Flujo de trabajo con Storybook**

1. El desarrollador implementa un componente en Angular + Tailwind.
2. Escribe sus stories cubriendo todas las variantes y estados significativos.
3. Ejecuta Storybook localmente y verifica visualmente que todo es correcto.
4. Comparte la URL de Storybook (o despliega la versión estática con Chromatic) con el equipo de diseño.
5. El diseñador compara la implementación con el diseño original en Figma.
6. Si encuentra discrepancias, reporta issues; el desarrollador corrige y el ciclo se repite.
7. Una vez validado, el componente está listo para integrarse en las pantallas de la aplicación.

Este flujo reduce drásticamente los **ciclos de feedback** (de días a minutos), evita retrabajos en etapas tardías del proyecto cuando integrar cambios es costoso, y mantiene una documentación viva del sistema de diseño que nunca queda obsoleta (porque forma parte del código y se genera automáticamente).

### 7. Electron: la web en el escritorio

**Electron**, creado por GitHub en 2013 (originalmente como Atom Shell para el editor Atom), permite empaquetar aplicaciones web como aplicaciones de escritorio nativas para Windows, macOS y Linux. Su arquitectura combina **Chromium** (para renderizar la interfaz) con Node.js (para acceder a las APIs del sistema operativo).

**Arquitectura de procesos**

Electron mantiene una estricta separación entre dos tipos de procesos, que se comunican mediante **IPC (Inter-Process Communication)**:

1. **Proceso principal (Main Process):** Un único proceso Node.js por aplicación. Gestiona el ciclo de vida de la aplicación (crear ventanas, cerrar la aplicación, eventos del sistema), crea objetos `BrowserWindow` (cada uno abrirá su propio proceso renderizador), y tiene acceso completo al sistema: sistema de archivos (fs), menús nativos (Menu), accesos directos de teclado (globalShortcut), notificaciones del sistema (Notification), bandeja del sistema (Tray), diálogos nativos (dialog).

2. **Procesos renderizadores (Renderer Processes):** Uno por cada `BrowserWindow` creada por el proceso principal. Ejecutan Chromium y cargan una página web (HTML, CSS, JavaScript). Por defecto, por seguridad, NO tienen acceso a las APIs de Node.js. Si la página renderizada necesita comunicarse con el proceso principal (por ejemplo, para leer un archivo del disco), debe hacerlo a través de un script de precarga (preload script) que expone una API segura y controlada mediante `contextBridge`.

**Seguridad en Electron**

!!! warning "Seguridad"

    Electron ha tenido históricamente problemas de seguridad porque muchos desarrolladores deshabilitaban las protecciones por conveniencia. Las prácticas actuales de seguridad son:

    - `nodeIntegration: false` (valor por defecto desde Electron 5): El renderer no puede usar `require()` ni acceder a APIs de Node.
    - `contextIsolation: true` (valor por defecto desde Electron 12): Separa el contexto JavaScript del preload script del contexto de la página web, previniendo que código malicioso inyectado en la página acceda a las APIs expuestas.
    - **Preload scripts controlados:** Solo las funciones explícitamente expuestas mediante `contextBridge.exposeInMainWorld()` son accesibles desde la página. Esto crea una API segura y limitada.
    - **Content Security Policy (CSP):** Cabeceras HTTP que restringen qué scripts pueden ejecutarse y desde dónde pueden cargarse recursos.

**Integración con Angular**

El flujo típico para una aplicación Angular + Electron es:

1. Desarrollar la aplicación Angular normalmente (con `ng serve` durante el desarrollo).
2. Configurar el proceso principal de Electron (archivo `main.js` o `main.ts`) que crea una `BrowserWindow` apuntando a `http://localhost:4200` durante el desarrollo, o al archivo `index.html` compilado en producción.
3. Usar un script npm que levante Angular y Electron simultáneamente durante el desarrollo: `concurrently "ng serve" "electron ."`
4. Para producción, compilar Angular con `ng build`, y luego empaquetar con `electron-builder` que genera los instaladores para cada plataforma.

**Cuándo usar Electron y cuándo no**

Electron es ideal cuando: necesitas una aplicación de escritorio multiplataforma, tu equipo domina tecnologías web, la aplicación no requiere rendimiento extremo de cómputo nativo (no es un editor de vídeo 4K ni un videojuego AAA), y el tamaño de la aplicación (100-150 MB) es aceptable para tu caso de uso.

Electron **NO** es adecuado cuando: requieres el menor consumo de recursos posible (utilitario residente en bandeja del sistema que debe consumir < 10 MB de RAM), necesitas máximo rendimiento gráfico nativo (videojuegos, 3D en tiempo real), o distribuyes en entornos con restricciones severas de tamaño de descarga.

La mayoría de aplicaciones de negocio, productividad y comunicación caen en el primer caso, lo que explica la enorme popularidad de Electron.

### 8. Flujo de trabajo profesional completo

El desarrollo profesional de interfaces no es un acto aislado de escritura de código, sino un **proceso multidisciplinar** que integra diseño, implementación, testing, colaboración y despliegue. Comprender este flujo completo es esencial para contextualizar cada herramienta y cada habilidad que aprenderemos en el módulo.

**Fase 1: Investigación y conceptualización**
- **Herramientas**: entrevistas con usuarios, análisis competitivo, encuestas.
- **Artefactos**: personas, escenarios, mapas de empatía, journey maps.
- **Responsables principales**: UX researcher, Product Manager.

**Fase 2: Diseño de experiencia (UX)**
- **Herramientas**: Figma, Miro, Whimsical (para diagramas de flujo y wireframes).
- **Artefactos**: diagramas de flujo, wireframes de baja fidelidad, arquitectura de la información.
- **Responsables principales**: UX Designer.

**Fase 3: Diseño visual (UI)**
- **Herramientas**: Figma (componentes, variantes, Auto Layout, variables).
- **Artefactos**: diseños de alta fidelidad, prototipo interactivo, sistema de diseño (componentes + tokens), assets exportables.
- **Responsables principales**: UI Designer.

**Fase 4: Handoff diseño → desarrollo**
- **Herramientas**: Figma Dev Mode, Zeplin (alternativa legacy), plugins de exportación de tokens.
- **Artefactos**: especificaciones de diseño (medidas, colores, tipografías), assets en formatos de desarrollo (SVG, PNG, fuentes).
- **Responsables**: UI Designer (prepara) + Frontend Developer (recibe e inspecciona).

**Fase 5: Configuración del proyecto**
- **Herramientas**: Angular CLI, npm, Vite, Tailwind CSS, ESLint, Prettier, Git, GitHub.
- **Artefactos**: repositorio Git inicializado, proyecto Angular andando, configuración de Tailwind con design tokens, ESLint y Prettier configurados, scripts npm funcionales.
- **Responsables**: Frontend Developer (posiblemente asignado a un Lead Frontend).

**Fase 6: Desarrollo de componentes (donde pasaremos la mayor parte del módulo)**
- **Herramientas**: Angular (standalone components, signals), Tailwind CSS (clases utilitarias), Storybook (desarrollo aislado y documentación).
- **Artefactos**: componentes unitarios (átomos y moléculas), componentes compuestos (organismos), stories con todas las variantes documentadas, tests unitarios (Jasmine/Jest + Angular Testing Library).
- **Responsables**: Frontend Developer.

**Fase 7: Integración y construcción de pantallas**
- **Herramientas**: Angular (composición de componentes, enrutamiento, servicios, signals para estado global).
- **Artefactos**: pantallas completas (páginas) integrando organismos y componentes, navegación funcional, conexión con APIs reales (o mockeadas durante desarrollo), gestión de estado de la aplicación.
- **Responsables**: Frontend Developer.

**Fase 8: Testing y calidad**
- **Herramientas**: Storybook (testing visual), ESLint + Prettier (calidad de código), Jest/Karma (tests unitarios), Cypress/Playwright (tests end-to-end), Lighthouse (auditoría de rendimiento y accesibilidad), axe-core/WAVE (auditoría de accesibilidad).
- **Artefactos**: informes de tests, informes de auditoría, issues de bugs.
- **Responsables**: Frontend Developer + QA Engineer + Diseñador (para validación visual).

**Fase 9: Build y despliegue**
- **Herramientas**: Angular CLI build (producción), CI/CD (GitHub Actions, GitLab CI, Jenkins), servicios de hosting (Vercel, Netlify, Firebase Hosting, AWS S3/CloudFront, Azure Static Web Apps) para web; electron-builder para escritorio.
- **Artefactos**: bundle de producción optimizado (minificado, tree-shaken, code-splitted), instaladores para escritorio, aplicación desplegada en producción.
- **Responsables**: Frontend Developer (build y configuración) + DevOps (pipeline CI/CD y despliegue).

**Fase 10: Monitorización e iteración**
- **Herramientas**: Google Analytics, Sentry (errores), Hotjar/FullStory (grabaciones de sesión y mapas de calor), encuestas NPS (Net Promoter Score), feedback de usuarios.
- **Artefactos**: informes de uso (métricas cuantitativas) e investigación continua (feedback cualitativo), backlog de mejoras priorizado.
- **Responsables**: Product Manager + Frontend Developer + UX Researcher.

Este flujo no es lineal ni rígido; en equipos pequeños una misma persona asume múltiples roles, y las iteraciones ágiles hacen que diseño y desarrollo se solapen y avancen en paralelo. Pero tener el mapa completo permite entender el contexto de cada tarea y colaborar más eficazmente con todos los perfiles implicados.

## Ejemplos guiados

### Ejemplo guiado 1: Instalación y configuración del stack completo

**Objetivo:** Configurar desde cero un entorno de desarrollo profesional con Node.js, Angular, Tailwind CSS 4, ESLint, Prettier y Git, verificando cada paso.

**Duración estimada:** 45 minutos (guiado, paso a paso en el aula).

**Desarrollo:**

**Paso 1 - Verificar Node.js:**
```bash
node --version  # Debe ser >= 18.x LTS
npm --version   # Debe ser >= 9.x
```
Si no está instalado, usar nvm (Node Version Manager) para instalar la última LTS.

**Paso 2 - Crear proyecto Angular con configuración standalone:**
```bash
npx @angular/cli new desarrollo-interfaces \
  --standalone \
  --style css \
  --ssr false \
  --routing true

cd desarrollo-interfaces
```
Opciones: `--standalone` crea el proyecto sin NgModules. `--style css` usa CSS plano (Tailwind se integrará sobre él). `--ssr false` sin Server-Side Rendering (no lo necesitaremos). `--routing true` incluye enrutamiento.

**Paso 3 - Instalar Tailwind CSS 4:**
```bash
npm install -D tailwindcss @tailwindcss/vite
```
La versión 4 elimina la necesidad de PostCSS; se integra como plugin de Vite.

**Paso 4 - Configurar Tailwind en Vite:**
Editar `vite.config.ts` (Angular 17+ usa Vite como builder por defecto en nuevos proyectos):
```typescript
import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [tailwindcss()],
});
```

**Paso 5 - Añadir las directivas de Tailwind al CSS global:**
Editar `src/styles.css`:
```css
@import "tailwindcss";

@theme {
  --color-primary: #3b82f6;
  --color-secondary: #8b5cf6;
  --font-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;
}

@layer base {
  body {
    @apply bg-gray-50 text-gray-900 antialiased;
  }
}
```

**Paso 6 - Verificar funcionamiento:**
Modificar `src/app/app.component.html`:
```html
<div class="min-h-screen flex items-center justify-center">
  <div class="bg-white p-8 rounded-2xl shadow-lg max-w-md">
    <h1 class="text-3xl font-bold text-primary mb-4">
      Angular + Tailwind ✓
    </h1>
    <p class="text-gray-600">
      Si ves este texto estilado, la configuración funciona.
    </p>
  </div>
</div>
```

Ejecutar `npm start` y verificar en `http://localhost:4200` que la página muestra estilos de Tailwind correctamente.

**Paso 7 - Instalar ESLint y Prettier:**
```bash
npm install -D prettier eslint-config-prettier
```

Crear `.prettierrc`:
```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "all",
  "printWidth": 100
}
```

Añadir scripts a `package.json`:
```json
"format": "prettier --write \"src/**/*.{ts,html,css,json}\"",
"format:check": "prettier --check \"src/**/*.{ts,html,css,json}\"",
"lint": "ng lint"
```

Ejecutar `npm run format` y verificar que formatea el código correctamente.

**Paso 8 - Inicializar Git:**
```bash
git init
git add .
git commit -m "feat: proyecto inicial Angular + Tailwind CSS 4"
```

Crear repositorio en GitHub (desde la web) y conectar:
```bash
git remote add origin https://github.com/tu-usuario/desarrollo-interfaces.git
git branch -M main
git push -u origin main
```

**Paso 9 - Instalar Storybook:**
```bash
npx storybook@latest init --type angular
```

Esto detecta automáticamente que el proyecto es Angular, instala las dependencias necesarias, crea archivos de configuración (`.storybook/main.ts`, `.storybook/preview.ts`) y genera stories de ejemplo.

**Paso 10 - Configurar Storybook para que use Tailwind:**
Editar `.storybook/preview.ts`:
```typescript
import type { Preview } from '@storybook/angular';
import '../src/styles.css'; // Importa Tailwind

const preview: Preview = {
  parameters: {
    controls: { matchers: { color: /(background|color)$/i, date: /Date$/i } },
  },
};

export default preview;
```

**Paso 11 - Verificar Storybook:**
```bash
npm run storybook
```
Abrir `http://localhost:6006`, verificar que se muestran las stories de ejemplo y que los estilos de Tailwind están aplicados.

**Resultado:** Entorno completamente configurado y listo para desarrollar componentes de interfaz de forma profesional.

### Ejemplo guiado 2: Flujo completo con un componente simple

**Objetivo:** Demostrar el flujo de trabajo profesional completo con un componente simple (Button), desde la creación con Angular CLI hasta la documentación en Storybook.

**Desarrollo:**

**Paso 1 - Generar componente:**
```bash
ng g component shared/ui/button --standalone --inline-template --inline-style
```

**Paso 2 - Implementar el componente (button.component.ts):**
```typescript
import { Component, Input, Output, EventEmitter, input, output } from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button
      [type]="type()"
      [disabled]="disabled()"
      (click)="onClick.emit()"
      class="inline-flex items-center justify-center gap-2 rounded-lg font-semibold transition-all duration-150
        focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary
        disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none
        {{ variantClasses() }}
        {{ sizeClasses() }}"
    >
      <ng-content />
    </button>
  `,
  styles: [],
})
export class ButtonComponent {
  readonly type = input<'button' | 'submit' | 'reset'>('button');
  readonly variant = input<'primary' | 'secondary' | 'outline' | 'ghost'>('primary');
  readonly size = input<'sm' | 'md' | 'lg'>('md');
  readonly disabled = input(false);

  readonly onClick = output<void>();

  protected variantClasses(): string {
    const classes: Record<string, string> = {
      primary: 'bg-primary text-white hover:bg-primary-dark active:bg-primary-dark',
      secondary: 'bg-secondary text-white hover:bg-secondary/90 active:bg-secondary/90',
      outline: 'border-2 border-primary text-primary hover:bg-primary hover:text-white',
      ghost: 'text-primary hover:bg-primary/10',
    };
    return classes[this.variant()] ?? '';
  }

  protected sizeClasses(): string {
    const classes: Record<string, string> = {
      sm: 'px-3 py-1.5 text-sm',
      md: 'px-4 py-2 text-sm',
      lg: 'px-6 py-3 text-base',
    };
    return classes[this.size()] ?? '';
  }
}
```

**Paso 3 - Crear stories (button.stories.ts):**
```typescript
import type { Meta, StoryObj } from '@storybook/angular';
import { ButtonComponent } from './button.component';

const meta: Meta<ButtonComponent> = {
  title: 'UI/Button',
  component: ButtonComponent,
  tags: ['autodocs'],
  argTypes: {
    variant: { control: 'select', options: ['primary', 'secondary', 'outline', 'ghost'] },
    size: { control: 'select', options: ['sm', 'md', 'lg'] },
    type: { control: 'select', options: ['button', 'submit', 'reset'] },
    disabled: { control: 'boolean' },
  },
  render: (args) => ({
    props: args,
    template: `<app-button [variant]="variant" [size]="size" [disabled]="disabled" [type]="type">Button</app-button>`,
  }),
};

export default meta;
type Story = StoryObj<ButtonComponent>;

export const Primary: Story = { args: { variant: 'primary', size: 'md' } };
export const Secondary: Story = { args: { variant: 'secondary', size: 'md' } };
export const Outline: Story = { args: { variant: 'outline', size: 'md' } };
export const Ghost: Story = { args: { variant: 'ghost', size: 'md' } };
export const Small: Story = { args: { variant: 'primary', size: 'sm' } };
export const Large: Story = { args: { variant: 'primary', size: 'lg' } };
export const Disabled: Story = { args: { variant: 'primary', size: 'md', disabled: true } };
```

**Paso 4 - Ejecutar Storybook y verificar:**
```bash
npm run storybook
```

Navegar por las diferentes stories, usar el panel Controls para cambiar variantes en tiempo real, verificar que todos los estados son correctos visualmente.

**Paso 5 - Usar el componente en la aplicación principal:**
Modificar `app.component.html`:
```html
<div class="min-h-screen flex flex-col gap-4 items-center justify-center p-8">
  <app-button variant="primary" size="lg">Primary Large</app-button>
  <app-button variant="secondary">Secondary Medium</app-button>
  <app-button variant="outline" size="sm">Outline Small</app-button>
  <app-button variant="ghost" disabled>Ghost Disabled</app-button>
</div>
```

Ejecutar `npm start` y verificar en `http://localhost:4200`.

Este flujo —crear componente, implementar con Angular + Tailwind, documentar en Storybook, integrar en la aplicación— es el que seguiremos durante todo el módulo para cada componente que desarrollemos.

!!! example "Casos reales"

    ### Caso 1: El sistema de diseño del Servicio Andaluz de Salud (SAS)

    El **Servicio Andaluz de Salud** mantiene múltiples aplicaciones web para ciudadanos (ClicSalud+, app de cita previa, portal del paciente) y para profesionales sanitarios (historia clínica digital, gestión de farmacia hospitalaria, sistema de laboratorios). La consistencia visual y funcional entre todas estas aplicaciones es crítica: un médico que usa tres aplicaciones diferentes durante su jornada no puede enfrentarse a tres interfaces completamente diferentes.

    Imaginemos que el SAS aborda la creación de un **sistema de diseño unificado**. El equipo de desarrollo de interfaces utilizaría:

    - **Figma:** Para diseñar y mantener los componentes del sistema de diseño (botones, formularios, tablas, modales, etc.) con sus variantes.
    - **Variables de Figma:** Para definir los design tokens (colores corporativos de la Junta de Andalucía, tipografía institucional, espaciado).
    - **Tailwind CSS @theme:** Para trasladar esos tokens al código, garantizando que cualquier aplicación que use el sistema herede automáticamente los colores y estilos corporativos.
    - **Angular:** Para implementar los componentes como una biblioteca de componentes standalone, que cada aplicación del SAS importaría según necesite.
    - **Storybook:** Como catálogo vivo del sistema de diseño, accesible para desarrolladores, diseñadores y responsables de producto. Cualquier persona puede consultar el componente "Tabla con datos clínicos" y ver todos sus estados, variantes y código de ejemplo.
    - **Electron:** Para empaquetar las aplicaciones de escritorio utilizadas en los centros de salud (donde el acceso web puede ser problemático por restricciones de red) como aplicaciones nativas.

    Este caso ilustra cómo las herramientas del ecosistema no son fines en sí mismas, sino medios para resolver problemas organizacionales reales: consistencia, eficiencia, colaboración entre equipos distribuidos, y accesibilidad para diversos perfiles de usuario.

    ### Caso 2: Startup sevillana de logística

    Una startup sevillana ha desarrollado un algoritmo de optimización de rutas de reparto. Necesitan dos interfaces: un dashboard para el gestor de flotas (escritorio, consulta de rutas, KPIs, gráficos) y una app para el repartidor (móvil, funcionamiento offline, escaneo de códigos de barras, firma digital del destinatario).

    Su stack de desarrollo de interfaces:
    - **Angular:** Framework único para ambas interfaces (dashboard SPA y PWA para el repartidor), compartiendo modelos TypeScript (interfaces para Rutas, Pedidos, Clientes) y servicios.
    - **Tailwind CSS:** Estilado consistente en ambas plataformas.
    - **PWA (Service Workers):** Para el funcionamiento offline de la app del repartidor (cacheo de rutas del día, cola de sincronización cuando recupere conexión).
    - **Electron:** Empaquetando el dashboard como aplicación de escritorio para los gestores de flota, con notificaciones nativas de nuevas incidencias.
    - **Storybook:** Documentando los componentes compartidos entre ambas aplicaciones.

    La decisión de usar Angular + Tailwind en lugar de desarrollar nativo para iOS y Android por separado les permitió lanzar un **MVP (Producto Mínimo Viable)** en 3 meses con un equipo de 2 desarrolladores, validar el modelo de negocio, y solo entonces plantearse desarrollo nativo si las necesidades de rendimiento o acceso a hardware lo justificaran.

## Actividades guiadas

### Actividad guiada 1: Configuración colaborativa del entorno

**Duración:** 60 minutos (sesión completa de aula)

**Desarrollo:** El docente guía al grupo completo, paso a paso, la instalación y configuración del entorno descrita en el Ejemplo Guiado 1. Cada alumno sigue los pasos en su equipo. El docente verifica cada paso pidiendo al alumnado que confirme outputs específicos: "¿Qué versión de Node muestra `node --version`?", "¿Se ha creado el proyecto? Deberíais ver un directorio `desarrollo-interfaces/`.", "¿Funciona `npm start`? ¿Veis la página en http://localhost:4200?". Los compañeros que terminen antes ayudan a quienes encuentren problemas.

**Objetivos:** Garantizar que TODO el alumnado tiene un entorno funcional idéntico antes de avanzar. Detectar problemas de instalación tempranamente (versiones incorrectas, conflictos con instalaciones previas, configuraciones heredadas).

### Actividad guiada 2: Exploración de Storybook en proyectos open source

**Duración:** 25 minutos

**Desarrollo:** El docente proyecta y el alumnado accede simultáneamente a Storybooks públicos de proyectos open source conocidos:
- GitHub Primer (sistema de diseño de GitHub): https://primer.style/react/storybook
- Shopify Polaris: https://polaris.shopify.com
- Carbon Design System (IBM): https://carbondesignsystem.com

Para cada uno, deben identificar: ¿Cómo está organizada la navegación? ¿Qué variantes documentan de los componentes? ¿Usan Controls interactivos? ¿Tienen documentación de accesibilidad? ¿Integran diseños de Figma?

Puesta en común: ¿Qué características de estos Storybooks profesionales os gustaría adoptar en vuestros proyectos?

### Actividad guiada 3: Primer componente con TypeScript estricto

**Duración:** 30 minutos

**Desarrollo:** Siguiendo el Ejemplo Guiado 2, el alumnado crea el componente Button. El docente hace hincapié en la configuración estricta de TypeScript (verificar que `tsconfig.json` tiene `"strict": true`, `"strictNullChecks": true`, `"noImplicitAny": true`) y en cómo el tipado ayuda a prevenir errores comunes.

**Variaciones para practicar:** El docente propone modificaciones al componente para que el alumnado vea cómo TypeScript les protege:
- "Añadid una nueva variante 'danger' a Button. ¿Qué pasa si no actualizáis el Record de variantClasses?"
- "Intentad pasar un valor numérico a la prop variant. ¿Qué error da TypeScript?"
- "Añadid una prop opcional `icon` de tipo string. Haced que el icono se renderice solo si está definida. ¿Cómo tratáis el condicional con tipado seguro?"

## Actividades propuestas

### Actividad 1

**Nivel:** Básico
**Objetivo:** Configurar un entorno de desarrollo completo funcional y verificar cada herramienta.
**Enunciado:** Reproduce exactamente los Pasos 1 al 11 del Ejemplo Guiado 1 para configurar tu entorno de desarrollo. Como evidencia, entrega capturas de pantalla de: (a) `node --version` y `npm --version` en la terminal, (b) `npm start` con la aplicación Angular + Tailwind funcionando en el navegador, (c) `npm run storybook` con las stories de ejemplo funcionando, (d) salida de `npm run format` sin errores, (e) `git log --oneline` mostrando al menos un commit, (f) tu repositorio GitHub con el código subido. Además, crea un pequeño README.md (300-500 palabras) explicando para qué sirve cada herramienta instalada y cómo se relacionan entre sí en el flujo de trabajo.
**Requisitos:** El proyecto debe llamarse `apellido1_apellido2_di_setup`. Todo el código debe estar correctamente versionado en un repositorio público de GitHub con al menos 3 commits significativos (commit inicial, commit de configuración de Tailwind, commit de Storybook).
**Pistas:** Si encuentras errores con versiones de Node, usa nvm (Node Version Manager) para instalar y gestionar múltiples versiones. Si el comando `ng` no se reconoce, comprueba que Angular CLI está instalado globalmente o usa `npx @angular/cli`.
**Criterios de evaluación:** (1) Correcto funcionamiento de todas las herramientas (Angular + Tailwind + Storybook). (2) Calidad y claridad del README explicativo. (3) Uso correcto de Git y GitHub (commits con mensajes descriptivos, .gitignore adecuado).

### Actividad 2

**Nivel:** Medio
**Objetivo:** Implementar 3 componentes atómicos (Badge, Avatar, Icon) con TypeScript, Tailwind y Storybook.
**Enunciado:** Crea los siguientes componentes standalone en `src/app/shared/ui/` siguiendo el patrón del Ejemplo Guiado 2:

1. **Badge:** Props: `variant` (default, success, warning, danger, info), `size` (sm, md, lg). Renderiza un span con el texto pasado mediante `<ng-content />`. Cada variant define colores de fondo y texto (ej: success = bg-green-100 text-green-800).

2. **Avatar:** Props: `src` (string, URL de la imagen), `alt` (string), `size` (sm: 32px, md: 40px, lg: 56px, xl: 80px), `fallback` (string, iniciales a mostrar si la imagen no carga). Implementa lógica: si la imagen falla (evento error), muestra un círculo con el fallback.

3. **Icon:** Props: `name` (string), `size` (sm: 16px, md: 20px, lg: 24px, xl: 32px). Renderiza un SVG inline (puedes utilizar una librería de iconos como Lucide, Heroicons, o simplemente 4-5 iconos hardcodeados con paths SVG).

Para cada componente: (a) Tipa correctamente todas las properties usando inputs de Angular. (b) Define las variantes visuales con Tailwind. (c) Crea stories en Storybook cubriendo todas las variantes y tamaños. (d) Añade documentación JSDoc a las propiedades. (e) Escribe al menos 1 test unitario por componente usando Jasmine o Jest (pista: TestBed.createComponent).
**Requisitos:** Código TypeScript con tipado estricto (no usar `any`). Al menos 4 stories por componente. Tests que verifiquen al menos la renderización condicional de clases CSS según inputs.
**Pistas:** Para los iconos SVG, puedes usar la librería Lucide (npm install lucide-angular) o crear tus propios SVGs en archivos separados. Para el fallback del Avatar, usa el evento `(error)` en la etiqueta `<img>`.
**Criterios de evaluación:** (1) Calidad del tipado TypeScript (interfaces, uniones, tipos literales). (2) Cobertura de variantes en Storybook. (3) Funcionalidad de los tests unitarios.

### Actividad 3

**Nivel:** Medio
**Objetivo:** Personalizar el tema de Tailwind y crear un mini sistema de diseño.
**Enunciado:** Imagina que trabajas para una empresa que te ha proporcionado su paleta de colores y su tipografía:

- Colores: Primary (blue-600: #2563eb, blue-700: #1d4ed8), Secondary (violet-500: #8b5cf6), Neutral (slate-50 a slate-900).
- Tipografía: 'Plus Jakarta Sans' para headings, 'Inter' para body text.
- Border radius: botones y tarjetas a 12px (rounded-xl en Tailwind), inputs a 8px (rounded-lg).

Tu tarea: (1) Configura estos tokens en el archivo CSS de Tailwind usando la directiva `@theme`. (2) Crea variables personalizadas para los colores con nombres semánticos (por ejemplo, `--color-primary: #2563eb`, `--color-primary-hover: #1d4ed8`). (3) Importa las fuentes desde Google Fonts. (4) En `@layer base`, define estilos base: body con la fuente Inter, antialiasing, color de texto por defecto (slate-900). (5) Crea un componente `Card` que utilice los nuevos tokens (fondo blanco, border-radius personalizado, sombra, padding). (6) Demuestra el tema claro (por defecto) y añade una versión oscura usando el selector `.dark` (invierte colores: fondo oscuro, texto claro, etc.). (7) Documenta en un README.md dentro de una carpeta `docs/` cómo se ha configurado el tema, mapeando cada variable a su uso en componentes. Incluye una tabla de todos los tokens definidos.
**Requisitos:** El modo oscuro debe funcionar añadiendo/quitando la clase `dark` al elemento `<html>`. No usar `tailwind.config.js`; usar exclusivamente configuración basada en CSS con Tailwind 4.
**Pistas:** Para el modo oscuro con estrategia `class`, necesitas configurar `@variant dark (&:where(.dark, .dark *))` o usar el plugin de dark mode. Investiga la sintaxis exacta de Tailwind 4. Para las fuentes, en `@theme` define `--font-heading` y `--font-body`.
**Criterios de evaluación:** (1) Correcta configuración del tema solo con CSS (sin archivo JS de configuración). (2) Uso de nombres semánticos para los tokens (no `blue-500` sino `primary`). (3) Funcionalidad del modo oscuro. (4) Calidad de la documentación (tabla de tokens, explicación del mapeo).

### Actividad 4

**Nivel:** Avanzado
**Objetivo:** Integrar Electron en el proyecto Angular.
**Enunciado:** Siguiendo la documentación oficial de Electron, integra Electron en tu proyecto Angular de la Actividad 1 para empaquetarlo como aplicación de escritorio. Los pasos principales son: (1) Instalar Electron como dependencia de desarrollo. (2) Crear el archivo `main.js` con la configuración del proceso principal (crear BrowserWindow, cargar la URL del servidor de desarrollo en desarrollo o el archivo index.html en producción). (3) Configurar el preload script para exponer una API segura entre el proceso principal y el renderizador. (4) Añadir scripts npm: `"electron:dev": "concurrently \"ng serve\" \"wait-on http://localhost:4200 && electron .\""` y `"electron:build": "ng build --configuration production && electron-builder"`. (5) Añadir al menos una funcionalidad nativa: por ejemplo, un botón en la interfaz Angular que, al pulsarse, abra el diálogo nativo de "Abrir archivo" del sistema operativo (usando IPC: el renderizador envía un mensaje al proceso principal, este abre el diálogo con `dialog.showOpenDialog()`, y devuelve la ruta del archivo seleccionado). (6) Configurar `electron-builder` para generar instaladores. (7) Documentar todo el proceso en un README.md específico de Electron con capturas de la app funcionando como aplicación de escritorio independiente.
**Requisitos:** El preload script debe usar `contextBridge.exposeInMainWorld()` para exponer una API tipada. `nodeIntegration` debe estar en false y `contextIsolation` en true. La comunicación Angular ↔ Electron debe hacerse mediante la API expuesta, no mediante `require()` en el renderer.
**Pistas:** La librería `concurrently` ejecuta múltiples comandos simultáneamente. `wait-on` espera a que un recurso (URL) esté disponible antes de continuar. Ambas se instalan como devDependencies.
**Criterios de evaluación:** (1) Correcta arquitectura de seguridad de Electron (contextIsolation, preload script). (2) Funcionalidad nativa funcionando a través de IPC. (3) Calidad de la documentación del proceso de integración.

### Actividad 5

**Nivel:** Avanzado
**Objetivo:** Configurar integración continua (CI) con GitHub Actions.
**Enunciado:** Configura un pipeline de integración continua en GitHub Actions para tu proyecto Angular + Tailwind que se ejecute en cada push y pull request a la rama `main`. El pipeline debe incluir los siguientes jobs secuenciales: (1) Checkout del código y setup de Node.js. (2) Instalación de dependencias (`npm ci` para instalación limpia y reproducible). (3) Linting (`npm run lint` - no debe haber errores). (4) Formateo (`npm run format:check` - no debe haber archivos sin formatear). (5) Tests unitarios (`npm test -- --watch=false --browsers=ChromeHeadless`). (6) Build de producción (`npm run build` - debe completarse sin errores). (7) Build de Storybook (`npm run build-storybook` - debe completarse sin errores). (8) Despliegue del Storybook a GitHub Pages (opcional, suma puntos adicionales).

El archivo de workflow debe crearse en `.github/workflows/ci.yml`. Investiga la sintaxis de GitHub Actions, los actions oficiales (`actions/checkout`, `actions/setup-node`) y cómo cachear `node_modules` para acelerar las ejecuciones.
**Requisitos:** El pipeline debe fallar (marcarse como ❌) si algún paso no se completa correctamente, bloqueando el merge de la PR. Incluye un badge en el README.md que muestre el estado del último build.
**Pistas:** Necesitarás ChromeHeadless para ejecutar los tests en el entorno de CI. Angular CLI ya incluye la configuración, pero verifica que en el archivo `karma.conf.js` (o jest.config.js si usas Jest) esté configurado `browsers: ['ChromeHeadlessCI']` o similar.
**Criterios de evaluación:** (1) Pipeline completo y funcional (todos los pasos se ejecutan y pasan). (2) Correcta gestión de la cache de dependencias. (3) Integración del badge de estado en el README.

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Análisis comparativo de frameworks frontend

    Elige una aplicación sencilla (por ejemplo, un TODO list con filtros, o un dashboard con gráficos y una tabla) e implementa exactamente la misma interfaz y funcionalidad en Angular y en otro framework de tu elección (React, Vue, Svelte o Solid). La interfaz debe ser idéntica visualmente (usa Tailwind CSS en ambos casos para que el CSS no sea una variable de confusión). Documenta el proceso comparando: (1) Configuración inicial y tooling (¿cuánto tiempo hasta tener un "Hola Mundo" funcional?). (2) Curva de aprendizaje (¿qué conceptos necesitaste entender antes de ser productivo?). (3) Sistema de tipos (¿TypeScript es nativo, opcional, o requiere configuración?). (4) Gestión de estado (¿cómo se comparte estado entre componentes en cada framework?). (5) Experiencia de desarrollo (calidad del autocompletado, mensajes de error, velocidad de recarga en caliente). (6) Tamaño del bundle de producción. (7) Madurez del ecosistema (liberías de componentes, herramientas, comunidad). Concluye con una recomendación razonada sobre qué framework usarías para un proyecto empresarial a largo plazo con un equipo de 5 desarrolladores.

    ### Actividad de ampliación 2: Auditoría de rendimiento y accesibilidad automatizada

    Amplía el pipeline de CI/CD configurado en la Actividad 5 para incluir auditorías automatizadas de rendimiento y accesibilidad: (1) Integra Lighthouse CI en el pipeline para realizar auditorías de rendimiento, accesibilidad, SEO y buenas prácticas en cada PR. Configura umbrales mínimos: Performance >= 90, Accessibility >= 95, Best Practices >= 90, SEO >= 90. Si alguna métrica está por debajo del umbral, el pipeline debe fallar (bloqueando el merge). (2) Integra axe-core para tests de accesibilidad automatizados en los tests unitarios o en tests E2E. Añade al menos 5 tests específicos de accesibilidad (verificar que todos los inputs tienen label, que las imágenes tienen alt text, que el contraste de color es suficiente, que la navegación por teclado funciona, que los landmarks ARIA están correctamente usados). (3) Configura Chromatic (el servicio de testing visual de Storybook) o, si prefieres una alternativa gratuita, configura Percy. El objetivo es que cualquier cambio visual en un componente sea detectado y revisado antes del merge. Documenta la configuración completa, los umbrales elegidos y la justificación de cada uno.

    ### Actividad de ampliación 3: Creación de un plugin de Figma para exportar design tokens

    Investiga la API de plugins de Figma (figma.com/plugin-docs) y desarrolla un plugin simple que, al ejecutarse, lea todas las variables de color definidas localmente en el archivo de Figma (Paint styles, Color variables del nuevo sistema) y genere automáticamente un bloque `@theme` de Tailwind CSS 4 listo para copiar y pegar en el archivo `styles.css` del proyecto Angular. El plugin debe: (1) Leer las variables de color y sus valores. (2) Sanitizar los nombres (convertir espacios a guiones, eliminar caracteres especiales, aplicar camelCase si es necesario). (3) Generar el código CSS formateado con la directiva `@theme` de Tailwind 4 y las variables de color. (4) Mostrar el resultado en un panel dentro de Figma con un botón de "Copiar al portapapeles". (5) Opcionalmente, mapear automáticamente los nombres de Figma a nombres semánticos de Tailwind (si la variable se llama "Primary/500", generar `--color-primary-500`). Entrega el código del plugin y un README con instrucciones de instalación y uso.

!!! tip "Buenas prácticas"

    1. **Versiona siempre `package.json` y `package-lock.json`, NUNCA `node_modules`.** El `package-lock.json` garantiza instalaciones reproducibles (mismas versiones exactas para todo el equipo y en CI). El directorio `node_modules` se reconstruye con `npm ci` (en CI) o `npm install` (en desarrollo) y debe estar en `.gitignore`.

    2. **Usa `npx` en lugar de instalaciones globales siempre que sea posible.** Las instalaciones globales (`npm i -g @angular/cli`) atan el proyecto a una versión específica de la herramienta. Con `npx @angular/cli@19 ng new ...`, cada proyecto puede usar su propia versión, evitando conflictos y garantizando reproducibilidad.

    3. **Prefiere componentes standalone en Angular.** Aunque los NgModules siguen siendo compatibles, los standalone components simplifican la estructura del proyecto (menos archivos, menos boilerplate), facilitan el lazy loading y preparan el código para el futuro de Angular. Todo el ecosistema está migrando hacia standalone.

    4. **Prioriza `@theme` sobre `tailwind.config.js` en Tailwind 4.** La nueva configuración basada en CSS es más simple, más cercana a los estándares web y mejor integrada con herramientas como Figma (que exporta CSS, no JavaScript). Aprovecha esta simplificación.

    5. **No abuses de `@apply` en Tailwind.** La recomendación del propio creador de Tailwind es usar `@apply` con moderación. En Angular, donde cada componente encapsula su template y sus estilos, la reutilización se consigue mediante composición de componentes, no mediante clases CSS reutilizables. Mantén las clases Tailwind en el template.

    6. **Mantén las stories de Storybook sincronizadas con el código.** Una story desactualizada es peor que no tener story: genera confianza falsa en un componente que ya no se comporta como la story indica. Automatiza su verificación con Chromatic o al menos revísalas en cada PR que modifique componentes.

    7. **No deshabilites las protecciones de seguridad de Electron por conveniencia.** `nodeIntegration: true` y `contextIsolation: false` son atajos peligrosos que exponen tu aplicación (y el sistema del usuario) a vulnerabilidades de ejecución remota de código. Aprende a usar `preload.js` con `contextBridge` desde el principio.

    8. **Automatiza la calidad del código con pre-commit hooks.** Configura Husky y lint-staged para ejecutar ESLint y Prettier automáticamente antes de cada commit. Esto evita que código mal formateado o con errores de linting llegue al repositorio, eliminando discusiones sobre estilos en las code reviews.

!!! warning "Errores frecuentes"

    1. **Confundir dependencias de producción y desarrollo.** Instalar todo como `dependencies` (sin `-D`) infla innecesariamente el bundle de producción y puede incluir herramientas como ESLint en el código que se sirve al usuario. Pregúntate siempre: ¿necesito esta librería para que la aplicación funcione en el navegador del usuario? Si la respuesta es no, es `devDependency`.

    2. **Ignorar los mensajes de error de TypeScript usando `any`.** Cuando TypeScript se queja de un tipo y la respuesta del desarrollador es "pues le pongo `any`", se está anulando completamente el propósito de usar TypeScript. `any` es el "apagafuegos" que silencia el compilador pero mantiene el riesgo. Si no sabes qué tipo usar, usa `unknown` (obliga a hacer type narrowing) y dedica tiempo a entender el problema.

    3. **Combatir Tailwind en lugar de abrazarlo.** El reflejo inicial de muchos desarrolladores acostumbrados a CSS tradicional es "esto es un asco, ensucia el HTML". Este prejuicio suele desaparecer tras dos semanas de uso productivo al experimentar la productividad y la ausencia de problemas de cascada y especificidad. Dale una oportunidad real antes de juzgar.

    4. **No instalar las extensiones de VS Code (Angular Language Service, Tailwind CSS IntelliSense).** Sin autocompletado, desarrollar con Angular y Tailwind es frustrante y propenso a errores tipográficos. La extensión de Tailwind, en particular, muestra una previsualización del color al hacer hover, sugiere clases, y avisa de clases conflictivas (ej: `p-2 p-4` en el mismo elemento).

    5. **No configurar ESLint y Prettier desde el inicio del proyecto.** Añadirlos a mitad del proyecto genera cientos o miles de warnings que abruman y desmotivan. Configúralos en el commit inicial y el proyecto se mantendrá limpio desde el principio.

    6. **Ignorar Storybook "porque ya veré el componente en la app".** A medida que la aplicación crece, navegar hasta la pantalla donde aparece un componente concreto para verificar sus 12 variantes se vuelve insostenible. Storybook es una inversión que se amortiza exponencialmente con el tamaño del proyecto.

    7. **Ejecutar Electron con `nodeIntegration: true` en producción.** Es un vector de ataque grave. Todo el ecosistema Electron ha migrado hacia el modelo seguro (contextIsolation + preload). No aprendas el modelo inseguro solo porque los tutoriales antiguos lo muestran.

    8. **No leer los mensajes de error del compilador y buscar en Google inmediatamente.** Los mensajes de error de TypeScript, Angular y Tailwind son sorprendentemente buenos y descriptivos. Leer y comprender el mensaje de error es una habilidad profesional fundamental que evita dependencia de soluciones copiadas sin entender.

!!! abstract "Resumen"

    Esta unidad ha configurado el ecosistema profesional completo sobre el que trabajaremos durante el resto del módulo. Hemos partido de **Node.js** y **npm** como base del desarrollo moderno en JavaScript, comprendiendo la gestión de dependencias, los scripts y el versionado semántico. Sobre esta base, hemos desplegado las herramientas específicas que definen el stack de Desarrollo de Interfaces.

    **Angular** se posiciona como nuestro framework de implementación: completo, tipado con TypeScript, orientado a aplicaciones empresariales, con un modelo de componentes standalone moderno y un sistema de reactividad basado en **Signals** que representa el presente y el futuro del framework. TypeScript, como lenguaje fundamental, nos proporciona seguridad de tipos, autocompletado y refactorización segura, competencias profesionales cada vez más demandadas en la industria.

    **Tailwind CSS 4** introduce un cambio de paradigma en el estilado de interfaces: clases utilitarias, configuración con CSS nativo, plugin Vite y un enfoque utility-first que maximiza la productividad y la consistencia. Hemos aprendido a configurar el tema con la directiva `@theme` y a aplicar estilos mediante composición de clases en los templates.

    Figma, Storybook y Electron completan el ecosistema cubriendo diseño, documentación y distribución multiplataforma respectivamente. Figma es la fuente de verdad del diseño; Storybook es el catálogo vivo de componentes; Electron nos permite empaquetar nuestras aplicaciones web como aplicaciones de escritorio nativas.

    Las herramientas de productividad —VS Code con extensiones, ESLint + Prettier para calidad de código, **Git** y **GitHub** para control de versiones y CI/CD— constituyen la infraestructura sobre la que se desarrolla software profesional en la actualidad. No son opcionales ni accesorias: son parte integral de la competencia profesional.

    Finalmente, hemos trazado el flujo completo del desarrollo de interfaces, desde la investigación inicial hasta la monitorización en producción, para que cada herramienta y cada técnica que aprendamos en las siguientes unidades esté contextualizada en un proceso profesional real.

    En la Unidad 4 nos sumergimos en **Figma** para dominar el diseño de interfaces: componentes, sistemas de diseño con variables, prototipos interactivos y especificaciones para desarrollo. En la Unidad 5 abordamos los layouts modernos con Flexbox, CSS Grid y Tailwind. Más adelante, en la Unidad 15 (del diseño a la implementación), conectaremos todos los extremos recorriendo el camino completo desde un diseño en Figma hasta una aplicación Angular funcional con componentes documentados en Storybook.

## Recursos complementarios

### Documentación oficial (referencias primarias)

- **Node.js Documentation:** https://nodejs.org/docs/latest
- **npm Documentation:** https://docs.npmjs.com
- **Angular Official Documentation (angular.dev):** https://angular.dev — La documentación oficial renovada con tutoriales interactivos, guías y referencias de API.
- **TypeScript Handbook:** https://www.typescriptlang.org/docs/handbook/intro.html — La referencia completa del lenguaje.
- **Tailwind CSS 4 Documentation:** https://tailwindcss.com/docs/v4 — Novedades, migración desde v3 y referencia de configuración.
- **Storybook for Angular:** https://storybook.js.org/docs/angular — Guía de instalación, escritura de stories, addons y despliegue.
- **Electron Documentation:** https://www.electronjs.org/docs/latest — Guías, API reference, tutoriales y mejores prácticas de seguridad.
- **Vite Documentation:** https://vitejs.dev — Referencia del bundler utilizado por Angular moderno.
- **ESLint Documentation:** https://eslint.org/docs/latest
- **Prettier Documentation:** https://prettier.io/docs/en
- **Git Documentation:** https://git-scm.com/doc
- **Figma Docs (for developers):** https://www.figma.com/developers

### Libros recomendados

- Freeman, A. (2023). *Pro Angular: Build Powerful and Dynamic Web Apps*. Apress. Referencia exhaustiva para Angular a nivel profesional.
- Goldberg, J. y col. (2023). *Learning TypeScript*. O'Reilly. Introducción completa a TypeScript para desarrolladores que conocen JavaScript.
- Rappin, N. (2023). *Modern Angular*. Independiente. Enfoque práctico en las características modernas de Angular: standalone, signals, control flow.

### Tutoriales y cursos online

- **Angular.dev Tutorials:** El tutorial interactivo "Tour of Heroes" en la web oficial, actualizado para standalone components y signals.
- **TypeScript Official Playground:** https://www.typescriptlang.org/play — Prueba código TypeScript en el navegador y ve la salida JavaScript.
- **Tailwind CSS Screencasts:** https://tailwindcss.com/screencasts — Serie de vídeos oficiales cubriendo desde los fundamentos hasta técnicas avanzadas.

### Herramientas mencionadas

- **nvm (Node Version Manager):** https://github.com/nvm-sh/nvm
- **Husky:** https://typicode.github.io/husky — Git hooks para automatizar tareas pre-commit.
- **lint-staged:** https://github.com/okonet/lint-staged — Ejecuta linters solo en archivos staged para Git.
- **concurrently:** https://github.com/open-cli-tools/concurrently — Ejecuta comandos en paralelo.
- **electron-builder:** https://www.electron.build — Empaqueta y distribuye aplicaciones Electron.
- **Chromatic (Storybook):** https://www.chromatic.com — Revisión visual automatizada para Storybook (plan gratuito disponible).

### Comunidades

- **Angular Spain Community:** Grupo de Telegram y meetups en varias ciudades españolas.
- **Angular Discord:** Servidor oficial de Discord de Angular con canales de ayuda en español.
- **GitHub Discussions (Angular):** https://github.com/angular/angular/discussions
- **Tailwind CSS Discord:** Comunidad activa con canales de soporte.
