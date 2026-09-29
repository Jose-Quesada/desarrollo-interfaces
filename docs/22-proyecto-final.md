---
icon: lucide/flag
---

# Proyecto Final Integrador: Aplicación Empresarial Completa "GesFlow"

## Objetivos de aprendizaje

Al finalizar este proyecto final integrador, el alumnado habrá demostrado la capacidad de:

1. **Integrar todos los conocimientos y competencias del módulo** en un único proyecto completo, aplicando de forma transversal los saberes adquiridos en las 19 unidades didácticas anteriores: diseño de interfaces con Figma, maquetación con Tailwind CSS, desarrollo de componentes Angular standalone, implementación de Design Systems con Storybook, manejo de formularios reactivos, gestión de estado con Signals, consumo de APIs REST con HttpClient, visualización de datos con Chart.js, generación de documentos PDF, exportación de datos, desarrollo de aplicaciones de escritorio con Electron, y empaquetado y distribución multiplataforma.

2. **Planificar, diseñar y ejecutar un proyecto de software profesional** siguiendo una metodología en fases, desde la conceptualización y el diseño en Figma hasta la distribución del producto final empaquetado como aplicación de escritorio, pasando por la implementación del Design System, el desarrollo de las funcionalidades de negocio, las auditorías de UX y accesibilidad, y el despliegue de la documentación.

3. **Diseñar interfaces de usuario profesionales en Figma** aplicando principios de diseño visual, Auto Layout, componentes reutilizables, variantes, variables de diseño (Design Tokens), estilos compartidos, y exportación de assets para desarrollo.

4. **Implementar un Design System completo** con componentes reutilizables, accesibles y documentados en Storybook, aplicando tokens de diseño extraídos de Figma e implementados en Tailwind CSS mediante la directiva `@theme`.

5. **Desarrollar una arquitectura Angular profesional** siguiendo el patrón feature-based (organización por funcionalidades), con separación clara entre componentes Smart (contenedores, con lógica de negocio) y Dumb (presentacionales, solo muestran datos), servicios con `inject()`, Signals para estado reactivo, lazy loading de módulos, guards de autenticación e interceptores HTTP.

6. **Construir funcionalidades empresariales completas**: autenticación con JWT, dashboard con KPIs y gráficos interactivos, CRUD de entidades (clientes, facturas, productos) con formularios reactivos y validación, generación de documentos PDF profesionales, exportación de datos a CSV y Excel, y configuración de preferencias de usuario (tema oscuro/claro).

7. **Garantizar la accesibilidad WCAG AA** mediante auditorías con Lighthouse, WAVE y axe, implementando navegación por teclado completa, contraste de color suficiente, etiquetas ARIA, textos alternativos, focus visible y estructura semántica correcta.

8. **Aplicar principios de UX** (heurísticas de Nielsen) en todas las pantallas, incluyendo estados de carga (skeleton loaders), estados vacíos (empty states con ilustraciones y guías), estados de error (mensajes claros y acciones de recuperación), microcopy revisado y consistencia en la interfaz.

9. **Empaquetar la aplicación como producto de escritorio** con Electron para Windows, macOS y Linux, añadiendo funcionalidades nativas (menú, diálogos, notificaciones), configurando electron-builder para generar instaladores, y documentando el proceso completo.

10. **Elaborar documentación técnica y de usuario profesional**: README del proyecto, guía de instalación y uso, documentación de la arquitectura (decisiones técnicas, diagrama de componentes), Storybook desplegado como referencia del Design System, y memoria final del proyecto en formato PDF.

## Resultado de aprendizaje asociado

!!! info "Normativa"

    Este proyecto final integrador evalúa de forma conjunta los resultados de aprendizaje del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

- **RA 1.** Genera interfaces gráficos de usuario mediante editores visuales utilizando las funcionalidades del editor y adaptando el código generado (Figma como entorno de diseño, interfaz Angular).
- **RA 3.** Crea componentes visuales valorando y empleando herramientas específicas (componentes Angular standalone, Storybook).
- **RA 4.** Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad (WCAG, diseño responsive, legibilidad de paneles KPI).
- **RA 5.** Crea informes evaluando y utilizando herramientas gráficas (PDFMake, facturas PDF, gráficos Chart.js, exportación CSV/Excel).
- **RA 6.** Documenta aplicaciones seleccionando y utilizando herramientas específicas (guía de referencia, documentación de componentes en Storybook).
- **RA 7.** Prepara aplicaciones para su distribución evaluando y utilizando herramientas específicas (Electron, electron-builder, instaladores multiplataforma).
- **RA 8.** Evalúa el funcionamiento de aplicaciones diseñando y ejecutando pruebas (estrategia de pruebas, tests unitarios e integración).

> El **RA 2** («Genera interfaces naturales de usuario») se trabaja de forma específica en la Unidad 3; su incorporación al proyecto es opcional como ampliación.

Cada uno de los criterios de evaluación de estos RA se evalúa en la rúbrica detallada del proyecto que se presenta más adelante en este documento.

!!! note "Conocimientos previos"

    Este proyecto integrador presupone que el alumnado ha cursado y superado las 21 unidades didácticas anteriores del módulo 0488 *Desarrollo de interfaces*, así como los módulos de primero y segundo curso que proporcionan la base de programación, bases de datos, entornos de desarrollo y sistemas informáticos.

    En particular, se requiere dominio de:

    - **Angular 18+ standalone**: componentes, servicios con `inject()`, Signals (`signal`, `computed`, `effect`), Reactive Forms, HttpClient, Router con lazy loading, guards, interceptores, pipes, directivas estructurales (`@if`, `@for`, `@switch`).
    - **Tailwind CSS 4**: sistema de utilidades, responsive design (breakpoints `sm`, `md`, `lg`, `xl`, `2xl`), dark mode con `dark:`, personalización con `@theme`, CSS Grid y Flexbox con utilidades de Tailwind.
    - **Figma**: diseño de interfaces, Auto Layout, componentes y variantes, variables (Design Tokens), estilos de texto y color, exportación de assets.
    - **Storybook**: creación de historias, documentación de componentes, tests de interacción, controls, acciones y docs automáticos.
    - **Chart.js**: tipos de gráficos, configuración, integración en Angular, ciclo de vida, exportación a imagen base64.
    - **PDFMake**: definición declarativa de documentos, tablas, estilos, imágenes, métodos de salida.
    - **Electron**: arquitectura de procesos, main.js, preload.js, IPC, integración con Angular, electron-builder.
    - **TypeScript avanzado**: interfaces, tipos genéricos, tipos de unión, narrowing, utility types.
    - **Control de versiones con Git y GitHub**: ramas, commits, pull requests, GitHub Pages, GitHub Actions.

## Contenidos

1. **Enunciado completo del proyecto "GesFlow"**
2. **Planificación del proyecto en 9 fases**
3. **Especificación funcional detallada**
4. **Especificación técnica detallada**
5. **Arquitectura del proyecto Angular**
6. **Guía de implementación fase por fase**
7. **Rúbrica de evaluación completa**
8. **Entregables requeridos**
9. **Ampliaciones opcionales**
10. **Fragmentos de código de referencia**

## Desarrollo teórico

### 1. Enunciado completo del proyecto "GesFlow"

!!! info "Definición"

    GesFlow es un **sistema de gestión empresarial integral** desarrollado como proyecto final del módulo 0488 Desarrollo de Interfaces. La aplicación cubre el flujo completo de una pequeña/mediana empresa: gestión de clientes, facturación, productos, dashboard de indicadores, informes y configuración.

**Contexto de negocio**: GesFlow está dirigido a **autónomos, pymes y microempresas** andaluzas que necesitan una herramienta sencilla pero completa para gestionar su negocio diario. La aplicación debe funcionar tanto en navegador web (accesible desde cualquier dispositivo) como en escritorio (para uso intensivo en oficina), compartiendo la misma base de código.

**Módulos funcionales**:

1. **Autenticación**: Registro de nuevos usuarios, inicio de sesión, recuperación de contraseña, cierre de sesión. Protección de rutas mediante guardas de autenticación. Simulación de JWT mediante json-server + json-server-auth o implementación real con Firebase Auth.

2. **Dashboard**: Panel de control con 5 **KPI cards** (ingresos totales del mes, número de facturas emitidas, número de clientes activos, ticket medio, tasa de cobro), 3 gráficos interactivos (evolución de ingresos mensual —líneas, top 5 productos por ingresos —barras horizontales, distribución de ingresos por categoría —doughnut), tabla de últimas 10 facturas emitidas, y filtro de rango de fechas.

3. **Clientes (CRUD)**: Listado con tabla paginada, búsqueda en tiempo real, filtrado por ciudad y estado (activo/inactivo), ordenación por columnas (nombre, fecha de alta, total facturado), formulario de creación/edición con validación (nombre, NIF/CIF, email, teléfono, dirección, ciudad, código postal, notas), vista de detalle con historial de facturas del cliente, y acciones (editar, desactivar, eliminar con confirmación).

4. **Facturas**: Listado de facturas con filtros (estado: pendiente, pagada, vencida; rango de fechas; cliente), creación de factura con selección de cliente (dropdown con búsqueda), líneas de factura dinámicas (añadir/eliminar productos/servicios con cantidad, precio unitario, tipo de IVA), cálculos automáticos en tiempo real (base imponible, cuota IVA, total), vista previa del PDF antes de emitir, generación y descarga del PDF profesional, cambio de estado (pendiente → pagada), y envío simulado por correo electrónico.

5. **Productos**: CRUD simple (nombre, descripción, categoría, precio base, tipo de IVA, stock). Listado con tabla, formulario de creación/edición, activación/desactivación.

6. **Informes**: Selector de tipo de informe (ventas por período, ventas por cliente, productos más vendidos, resumen de IVA), selector de rango de fechas, visualización de datos en tabla y gráfico, exportación a PDF (con gráficos incrustados), CSV y Excel.

7. **Configuración y perfil**: Datos del perfil de usuario (nombre, email, avatar, cambio de contraseña), datos de la empresa (nombre, CIF, dirección, logo, datos bancarios para facturas), preferencias de la aplicación (tema: claro/oscuro/sistema, idioma, moneda), y configuración de notificaciones.

### 2. Planificación del proyecto en 9 fases

!!! info "Dato clave"

    El proyecto se estructura en **9 fases**, diseñadas para ser ejecutadas de forma secuencial aunque algunas pueden solaparse. La carga horaria estimada es de 40 horas (2 semanas completas de clase a razón de 4 horas diarias de trabajo práctico).

| **Fase** | **Descripción** | **Horas estimadas** | **Semana** |
|---|---|---|---|
| FASE 1 | Diseño en Figma | 6h | Semana 1 |
| FASE 2 | Configuración del proyecto Angular | 2h | Semana 1 |
| FASE 3 | Design System + Storybook | 8h | Semana 1 |
| FASE 4 | Layout y navegación | 3h | Semana 1 |
| FASE 5 | Features (funcionalidades de negocio) | 10h | Semana 1-2 |
| FASE 6 | UX y Accesibilidad | 3h | Semana 2 |
| FASE 7 | Responsive Design | 3h | Semana 2 |
| FASE 8 | Empaquetado con Electron | 3h | Semana 2 |
| FASE 9 | Documentación final | 2h | Semana 2 |

### 3. Fase 1: Diseño en Figma

**Objetivo**: Diseñar la interfaz de usuario completa de GesFlow en Figma antes de escribir una sola línea de código. El diseño debe ser de alta fidelidad (píxel perfect), con todas las pantallas, estados y componentes definidos.

**Pantallas a diseñar** (mínimo 5 principales):

1. **Login / Registro**: Formulario de inicio de sesión con campos email y contraseña, botón "Iniciar sesión", enlace "¿Olvidaste tu contraseña?" y "¿No tienes cuenta? Regístrate". Diseño limpio, centrado vertical y horizontalmente, con el logo de GesFlow en la parte superior. Versión para registro con campos adicionales (nombre, confirmar contraseña). Validación visual de campos (borde rojo en campos con error, mensaje de error bajo el campo).

2. **Dashboard principal**: Layout completo con header (logo, barra de búsqueda global, iconos de notificaciones, avatar del usuario con menú desplegable), sidebar (con items de navegación: Dashboard, Clientes, Facturas, Productos, Informes, Configuración, colapsable, con iconos y textos, ítem activo resaltado), contenido principal con la fila de 5 KPI cards, gráfico de líneas ocupando 2/3 del ancho, gráfico doughnut en el 1/3 restante, y tabla de últimas facturas abajo. Versión dark mode del dashboard.

3. **Listado de clientes**: Header con título "Clientes" y botón "Nuevo cliente". Barra de herramientas con campo de búsqueda (input con icono de lupa), filtro dropdown (por ciudad, por estado), y botón de exportar (dropdown con CSV, Excel). Tabla de datos con columnas (nombre, email, ciudad, facturas totales, estado, acciones). Paginación al pie de la tabla. Estado vacío (cuando no hay clientes): ilustración, texto "No hay clientes todavía" y botón "Crear primer cliente". Estado de carga: skeleton de la tabla.

4. **Creación/edición de factura**: Formulario dividido en secciones: "Datos generales" (selector de cliente con dropdown buscable, fecha de emisión, fecha de vencimiento, número de factura auto-generado), "Líneas de factura" (tabla editable con columnas: concepto, cantidad, precio unitario, IVA%, importe, acción eliminar; botón "Añadir línea"), "Resumen" (base imponible, IVA desglosado por tipo, total). Botones de acción: "Vista previa", "Guardar borrador", "Emitir factura". Validación visual de campos requeridos.

5. **Detalle de factura / Vista previa**: Representación visual de cómo se verá la factura impresa (simulación del PDF en pantalla). Cabecera con logo de la empresa y datos fiscales. Datos del cliente. Tabla de líneas. Totales. Pie con datos bancarios y código QR de verificación. Botones: "Descargar PDF", "Enviar por email", "Marcar como pagada", "Editar", "Volver".

**Creación del Design System en Figma**:

El Design System debe incluir:

- **Paleta de colores (Design Tokens)**: Colores primarios (azul corporativo), secundarios, de acento, de éxito (verde), de advertencia (ámbar), de error (rojo), neutros (escala de grises del 50 al 950), y variantes para modo oscuro.
- **Tipografía**: Familia tipográfica (Inter, sistema), tamaños (escala tipográfica: xs, sm, base, lg, xl, 2xl, 3xl, 4xl), pesos (regular, medium, semibold, bold), alturas de línea.
- **Espaciado**: Escala de espaciado (4, 8, 12, 16, 20, 24, 32, 40, 48, 64 px).
- **Sombras**: Elevaciones (sm, md, lg, xl).
- **Bordes y radios**: Radios de borde (none, sm, md, lg, xl, full).
- **Componentes base** (usando Auto Layout, componentes y variantes de Figma):
  - `Button`: Variantes de estilo (primary, secondary, outline, ghost, danger), tamaños (sm, md, lg), estados (default, hover, focus, active, disabled, loading), con/sin icono.
  - `Input`: Variantes (text, email, password, number, textarea), estados (default, focus, error, disabled), con/sin label, con/sin helper text, con/sin icono (prepend/append).
  - `Card`: Variantes (default, hoverable, bordered), con/sin header, con/sin footer.
  - `Modal`: Tamaños (sm, md, lg, xl), con/sin overlay, animación de entrada.
  - `Table`: Variantes (default, striped, bordered), con/sin paginación, con/sin ordenación, filas seleccionables.
  - `Badge`: Variantes de color (primary, success, warning, danger, info), tamaños (sm, md).
  - `Toast / Notificación`: Posiciones (top-right, top-left, bottom-right, bottom-left), variantes (success, error, warning, info), con/sin acción.
  - `Dropdown`: Variantes (click, hover), alineación (left, right), con/sin icono.
  - `Tabs`: Variantes (underline, pills), con/sin icono, con/sin badge.
  - `Spinner / Loader`: Tamaños (sm, md, lg), variantes de color.
  - `EmptyState`: Ilustración, título, descripción, acción opcional.
  - `Skeleton`: Variantes para texto, tarjeta, tabla, gráfico.

### 4. Fase 2: Configuración del proyecto Angular

**Objetivo**: Crear un proyecto Angular standalone correctamente configurado con todas las dependencias necesarias y una estructura de carpetas profesional.

**Paso a paso**:

1. Crear proyecto Angular:
   ```bash
   ng new gesflow --standalone --routing --style=css --skip-tests=false
   cd gesflow
   ```

2. Instalar dependencias:
   ```bash
   # Tailwind CSS 4
   npm install tailwindcss @tailwindcss/vite

   # Chart.js
   npm install chart.js

   # PDFMake
   npm install pdfmake

   # SheetJS (Excel)
   npm install xlsx

   # ApexCharts (opcional, alternativa a Chart.js)
   npm install apexcharts ng-apexcharts

   # Electron (dev)
   npm install --save-dev electron electron-builder concurrently wait-on cross-env

   # Storybook (dev)
   npx storybook@latest init --type angular

   # Otras herramientas
   npm install --save-dev prettier eslint
   ```

3. Configurar Tailwind CSS 4 con `@theme`:
   En `src/styles.css`:
   ```css
   @import "tailwindcss";

   @theme {
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

     --color-success-500: #10b981;
     --color-success-600: #059669;
     --color-warning-500: #f59e0b;
     --color-warning-600: #d97706;
     --color-danger-500: #ef4444;
     --color-danger-600: #dc2626;

     --font-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;
     --font-mono: 'JetBrains Mono', ui-monospace, monospace;
   }
   ```

4. Estructura de carpetas profesional:
   ```
   src/app/
   ├── core/
   │   ├── services/          # Servicios globales (auth, api, electron, pdf, csv, excel)
   │   │   ├── auth.service.ts
   │   │   ├── api.service.ts
   │   │   ├── electron.service.ts
   │   │   ├── pdf.service.ts
   │   │   ├── csv-export.service.ts
   │   │   └── excel-export.service.ts
   │   ├── guards/            # Guards de ruta
   │   │   └── auth.guard.ts
   │   ├── interceptors/      # Interceptores HTTP
   │   │   └── auth.interceptor.ts
   │   └── models/            # Interfaces y tipos compartidos
   │       ├── user.model.ts
   │       ├── client.model.ts
   │       ├── invoice.model.ts
   │       └── product.model.ts
   ├── shared/
   │   ├── components/        # Componentes del Design System
   │   │   ├── button/
   │   │   │   ├── button.component.ts
   │   │   │   ├── button.component.html
   │   │   │   └── button.stories.ts
   │   │   ├── input/
   │   │   ├── card/
   │   │   ├── modal/
   │   │   ├── table/
   │   │   ├── badge/
   │   │   ├── toast/
   │   │   ├── dropdown/
   │   │   ├── tabs/
   │   │   ├── spinner/
   │   │   ├── empty-state/
   │   │   ├── skeleton/
   │   │   ├── stat-card/
   │   │   └── chart-widget/
   │   ├── directives/        # Directivas reutilizables
   │   └── pipes/             # Pipes reutilizables
   ├── features/
   │   ├── auth/              # Módulo de autenticación
   │   │   ├── login/
   │   │   ├── register/
   │   │   └── auth.routes.ts
   │   ├── dashboard/         # Dashboard principal
   │   │   ├── dashboard.component.ts
   │   │   └── dashboard.routes.ts
   │   ├── clients/           # CRUD de clientes
   │   │   ├── client-list/
   │   │   ├── client-form/
   │   │   ├── client-detail/
   │   │   └── clients.routes.ts
   │   ├── invoices/          # Gestión de facturas
   │   │   ├── invoice-list/
   │   │   ├── invoice-form/
   │   │   ├── invoice-detail/
   │   │   └── invoices.routes.ts
   │   ├── products/          # CRUD de productos
   │   │   └── products.routes.ts
   │   ├── reports/           # Informes y estadísticas
   │   │   └── reports.routes.ts
   │   └── settings/          # Configuración
   │       └── settings.routes.ts
   ├── layout/                # Componentes de layout
   │   ├── main-layout/
   │   ├── header/
   │   ├── sidebar/
   │   └── footer/
   ├── app.component.ts
   ├── app.config.ts
   └── app.routes.ts
   ```

5. Scripts en `package.json`:
   ```json
   "scripts": {
     "start": "ng serve",
     "build": "ng build --configuration production",
     "lint": "ng lint",
     "format": "prettier --write \"src/**/*.{ts,html,css}\"",
     "storybook": "storybook dev -p 6006",
     "build-storybook": "storybook build -o storybook-static",
     "electron:dev": "cross-env NODE_ENV=development concurrently \"ng serve\" \"wait-on http://localhost:4200 && electron .\"",
     "electron:build": "ng build --configuration production && electron-builder",
     "electron:build:win": "ng build --configuration production && electron-builder --win",
     "electron:build:mac": "ng build --configuration production && electron-builder --mac",
     "electron:build:linux": "ng build --configuration production && electron-builder --linux"
   }
   ```

### 5. Fase 3: Design System + Storybook

**Objetivo**: Implementar todos los componentes del Design System como componentes Angular standalone, asegurando que son reutilizables, accesibles y están documentados en Storybook.

**Componentes obligatorios del Design System** (mínimo 10):

Para cada componente, se debe implementar:
- Componente Angular standalone con todas las variantes y estados.
- Propiedades de entrada (`@Input()`) correctamente tipadas.
- Eventos de salida (`@Output()`) para las interacciones.
- Accesibilidad: atributos ARIA, navegación por teclado, focus visible, roles semánticos.
- Historias de Storybook cubriendo todos los estados y variantes.
- Tests de interacción en Storybook (play functions) para verificar el comportamiento interactivo.

**Ejemplo de implementación del componente Button**:

```typescript
import { Component, Input, Output, EventEmitter, signal } from '@angular/core';
import { NgClass } from '@angular/common';

export type ButtonVariant = 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
export type ButtonSize = 'sm' | 'md' | 'lg';

@Component({
  selector: 'gfl-button',
  standalone: true,
  imports: [NgClass],
  template: `
    <button
      [type]="type"
      [disabled]="disabled || isLoading"
      [class]="buttonClasses()"
      (click)="onClick.emit($event)"
      (focus)="onFocus.emit($event)"
      (blur)="onBlur.emit($event)"
      [attr.aria-label]="ariaLabel"
      [attr.aria-busy]="isLoading"
      [attr.aria-disabled]="disabled">
      @if (isLoading) {
        <gfl-spinner [size]="spinnerSize()" class="mr-2"></gfl-spinner>
      }
      @if (icon && iconPosition === 'left' && !isLoading) {
        <span class="material-icons-outlined" [class.mr-2]="!!label">{{ icon }}</span>
      }
      @if (label) {
        <span>{{ label }}</span>
      }
      @if (icon && iconPosition === 'right' && !isLoading) {
        <span class="material-icons-outlined ml-2">{{ icon }}</span>
      }
    </button>
  `
})
export class ButtonComponent {
  @Input() variant: ButtonVariant = 'primary';
  @Input() size: ButtonSize = 'md';
  @Input() label = '';
  @Input() icon = '';
  @Input() iconPosition: 'left' | 'right' = 'left';
  @Input() type: 'button' | 'submit' | 'reset' = 'button';
  @Input() disabled = false;
  @Input() isLoading = false;
  @Input() fullWidth = false;
  @Input() ariaLabel = '';

  @Output() onClick = new EventEmitter<MouseEvent>();
  @Output() onFocus = new EventEmitter<FocusEvent>();
  @Output() onBlur = new EventEmitter<FocusEvent>();

  buttonClasses(): string {
    const baseClasses = 'inline-flex items-center justify-center font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2';

    const sizeClasses = {
      sm: 'px-3 py-1.5 text-sm',
      md: 'px-4 py-2 text-base',
      lg: 'px-6 py-3 text-lg'
    };

    const variantClasses = {
      primary: 'bg-primary-600 text-white hover:bg-primary-700 focus:ring-primary-500 disabled:bg-primary-300',
      secondary: 'bg-gray-100 text-gray-700 hover:bg-gray-200 focus:ring-gray-400 disabled:bg-gray-50 disabled:text-gray-400',
      outline: 'border-2 border-primary-600 text-primary-600 hover:bg-primary-50 focus:ring-primary-500 disabled:border-gray-300 disabled:text-gray-400',
      ghost: 'text-gray-600 hover:bg-gray-100 focus:ring-gray-400 disabled:text-gray-400',
      danger: 'bg-danger-600 text-white hover:bg-danger-700 focus:ring-danger-500 disabled:bg-danger-300'
    };

    return [
      baseClasses,
      sizeClasses[this.size],
      variantClasses[this.variant],
      this.fullWidth ? 'w-full' : '',
      this.disabled ? 'cursor-not-allowed' : 'cursor-pointer'
    ].join(' ');
  }

  spinnerSize(): 'sm' | 'md' | 'lg' {
    return this.size === 'lg' ? 'md' : 'sm';
  }
}
```

**Historia de Storybook para Button** (`button.stories.ts`):
```typescript
import type { Meta, StoryObj } from '@storybook/angular';
import { ButtonComponent } from './button.component';
import { userEvent, within } from '@storybook/test';

const meta: Meta<ButtonComponent> = {
  title: 'Design System/Button',
  component: ButtonComponent,
  tags: ['autodocs'],
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'outline', 'ghost', 'danger']
    },
    size: { control: 'select', options: ['sm', 'md', 'lg'] },
    onClick: { action: 'clicked' }
  },
  args: {
    label: 'Botón',
    variant: 'primary',
    size: 'md',
    disabled: false,
    isLoading: false,
    fullWidth: false
  }
};

export default meta;
type Story = StoryObj<ButtonComponent>;

export const Primary: Story = { args: { variant: 'primary' } };
export const Secondary: Story = { args: { variant: 'secondary' } };
export const Outline: Story = { args: { variant: 'outline' } };
export const Ghost: Story = { args: { variant: 'ghost' } };
export const Danger: Story = { args: { variant: 'danger' } };
export const Small: Story = { args: { size: 'sm' } };
export const Large: Story = { args: { size: 'lg' } };
export const Disabled: Story = { args: { disabled: true } };
export const Loading: Story = { args: { isLoading: true } };
export const FullWidth: Story = { args: { fullWidth: true } };
export const WithIcon: Story = { args: { icon: 'add', iconPosition: 'left' } };
export const IconOnly: Story = { args: { icon: 'search', label: '', ariaLabel: 'Buscar' } };

export const ClickInteraction: Story = {
  args: { label: 'Haz clic aquí' },
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    const button = canvas.getByRole('button');
    await userEvent.click(button);
  }
};
```

### 6. Fase 4: Layout y navegación

**Objetivo**: Implementar el layout principal de la aplicación con header, sidebar responsive y sistema de navegación con lazy loading.

**Componentes de layout**:

1. `MainLayoutComponent`: componente contenedor que organiza header + sidebar + contenido principal + footer.
2. `HeaderComponent`: logo de la aplicación, barra de búsqueda global, iconos (notificaciones con badge, modo oscuro/claro), menú de usuario (avatar, nombre, dropdown con perfil, configuración, cerrar sesión).
3. `SidebarComponent`: navegación principal con items (Dashboard, Clientes, Facturas, Productos, Informes, Configuración), iconos, tooltips en modo colapsado, item activo resaltado, responsive (overlay en móvil con backdrop, colapsado por defecto en tablet, expandido en desktop).
4. `FooterComponent`: información de versión, copyright, enlaces.

**Sistema de routing con lazy loading**:

```typescript
// app.routes.ts
import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full'
  },
  {
    path: 'auth',
    loadChildren: () => import('./features/auth/auth.routes').then(m => m.AUTH_ROUTES)
  },
  {
    path: '',
    canActivate: [authGuard],
    loadComponent: () => import('./layout/main-layout/main-layout.component').then(m => m.MainLayoutComponent),
    children: [
      {
        path: 'dashboard',
        loadChildren: () => import('./features/dashboard/dashboard.routes').then(m => m.DASHBOARD_ROUTES),
        data: { title: 'Dashboard', icon: 'dashboard' }
      },
      {
        path: 'clients',
        loadChildren: () => import('./features/clients/clients.routes').then(m => m.CLIENTS_ROUTES),
        data: { title: 'Clientes', icon: 'people' }
      },
      {
        path: 'invoices',
        loadChildren: () => import('./features/invoices/invoices.routes').then(m => m.INVOICES_ROUTES),
        data: { title: 'Facturas', icon: 'receipt' }
      },
      {
        path: 'products',
        loadChildren: () => import('./features/products/products.routes').then(m => m.PRODUCTS_ROUTES),
        data: { title: 'Productos', icon: 'inventory' }
      },
      {
        path: 'reports',
        loadChildren: () => import('./features/reports/reports.routes').then(m => m.REPORTS_ROUTES),
        data: { title: 'Informes', icon: 'assessment' }
      },
      {
        path: 'settings',
        loadChildren: () => import('./features/settings/settings.routes').then(m => m.SETTINGS_ROUTES),
        data: { title: 'Configuración', icon: 'settings' }
      }
    ]
  },
  { path: '**', redirectTo: 'dashboard' }
];
```

### 7. Fase 5: Features (funcionalidades de negocio)

Esta es la **fase más extensa del proyecto** (10 horas). Se implementan todas las funcionalidades de negocio. A continuación se detalla la especificación para cada feature.

#### 7.1. Autenticación

- **Login**: Formulario reactivo con email (validación de formato) y contraseña (mínimo 6 caracteres). Al enviar, llamar al `AuthService.login()`, almacenar el **token JWT** en `localStorage`, redirigir al dashboard. Manejar errores: credenciales inválidas (mostrar mensaje genérico "Email o contraseña incorrectos"), error de red (mostrar "Error de conexión, intente de nuevo").
- **Register**: Formulario con nombre, email, contraseña, confirmar contraseña (validación de coincidencia). Al enviar, llamar al `AuthService.register()`, redirigir al login con mensaje de éxito. Manejar errores: email ya registrado.
- **AuthGuard**: Comprobar si existe token en `localStorage`. Si no, redirigir a `/auth/login`. Si sí, permitir acceso.
- **AuthInterceptor**: Interceptar todas las peticiones HTTP salientes y añadir cabecera `Authorization: Bearer <token>`.

#### 7.2. Dashboard

- **Datos**: Simular datos con un `DashboardService` que devuelva datos mock o los obtenga de json-server.
- **KPI Cards**: 5 tarjetas de indicadores con icono, valor formateado, tendencia (+/- X% vs mes anterior) con flecha y color. Estados: carga (skeleton), datos, error.
- **Gráficos**: Usar `ChartWidgetComponent` (de la unidad 17). Gráfico de líneas (ingresos últimos 12 meses), gráfico de barras horizontales (top 5 productos), gráfico doughnut (distribución por categoría). Los datos se obtienen del `DashboardService` y se transforman con `computed()`.
- **Tabla de últimas facturas**: Tabla con 10 filas como máximo, columnas (número, cliente, fecha, importe, estado). El estado se muestra con `BadgeComponent` (pendiente = amarillo, pagada = verde, vencida = rojo).
- **Filtro de fechas**: Selector de período (últimos 7 días, 30 días, trimestre, año, personalizado). Al cambiar, se recalculan todos los datos del dashboard.
- **Exportación**: Botones "Exportar CSV" y "Exportar PDF" que generan informes con los datos del dashboard.

#### 7.3. Clientes (CRUD)

- **Listado**: Tabla con paginación, búsqueda en tiempo real (debounce 300ms), filtros por ciudad y estado, ordenación por columnas. Cada fila tiene acciones (ver detalle, editar, eliminar con modal de confirmación). Estados: vacío, carga, datos, error.
- **Formulario**: Reactive Form con validación. Campos: nombre (required, minLength: 2), nif (required, validación de formato DNI/NIF español), email (required, email), teléfono (formato español), dirección, ciudad (required), código postal (formato 5 dígitos), notas. Al enviar: POST (crear) o PUT (editar). Feedback: toast de éxito/error.
- **Detalle**: Vista con todos los datos del cliente y una tabla con el historial de facturas de ese cliente (últimas 20). Acciones: editar, volver, nueva factura para este cliente.

#### 7.4. Facturas

- **Listado**: Tabla con filtros (estado, rango de fechas, cliente —dropdown con búsqueda). Columnas (número, cliente, fecha, vencimiento, total, estado). Botones de acción (ver, descargar PDF, cambiar estado).
- **Creación**: Formulario complejo con:
  - Cabecera: selector de cliente (dropdown con búsqueda entre clientes activos), fecha de emisión (por defecto hoy), fecha de vencimiento (por defecto +30 días), número auto-generado (secuencial por año: F2024-0001).
  - Líneas de factura: array dinámico (FormArray). Cada línea: concepto (input text), cantidad (input number, min 1), precio unitario (input number, min 0, step 0.01), tipo de IVA (select: 21%, 10%, 4%, 0%), importe (campo calculado readonly = cantidad * precio unitario). Botón "Añadir línea" y botón X para eliminar línea.
  - Resumen: base imponible (suma de importes), IVA desglosado por tipo (agrupado), total (base + IVA). Todo calculado en tiempo real con `computed()`.
  - Acciones: "Vista previa" (abre PDF en nueva pestaña), "Guardar borrador" (estado = pendiente), "Emitir" (guarda y genera número definitivo).
- **Detalle / Vista previa**: Simulación visual del PDF. Botones: descargar PDF, marcar como pagada, editar (solo si pendiente), eliminar.
- **PDF de factura**: PDFMake con diseño profesional (como el desarrollado en la unidad 16).

#### 7.5. Productos

**CRUD estándar** con listado paginado, formulario de creación/edición con campos (nombre, descripción, categoría, precio base, tipo de IVA, stock), y toggle de activo/inactivo.

#### 7.6. Informes

Selector de tipo de informe (ventas por período, por cliente, top productos, resumen IVA). Selector de rango de fechas. Tabla de resultados y gráfico correspondiente. Exportación a PDF (con gráfico incrustado), CSV y Excel.

#### 7.7. Configuración y perfil

- **Perfil**: Editar nombre, email, avatar (subir imagen/URL). Cambiar contraseña (formulario con contraseña actual, nueva, confirmar).
- **Empresa**: Editar datos de la empresa (nombre, CIF, dirección, logo, datos bancarios) que se usan en las plantillas de facturas.
- **Preferencias**: Tema (claro/oscuro/sistema), idioma (ES, EN), moneda (EUR, USD, GBP).

### 8. Fase 6: UX y Accesibilidad

**Objetivo**: Realizar una auditoría completa de UX y accesibilidad y corregir todos los problemas encontrados.

**Actividades**:

1. **Auditoría de accesibilidad con Lighthouse**: Ejecutar Lighthouse en modo accesibilidad para cada pantalla. Objetivo: puntuación >= 95.
2. **Auditoría con WAVE**: Analizar cada pantalla con la extensión WAVE. Corregir errores (missing labels, contrast errors, empty buttons, missing alt text).
3. **Auditoría con axe DevTools**: Ejecutar tests automatizados de accesibilidad con axe-core.
4. **Verificar navegación por teclado**: Navegar por todas las pantallas usando solo el teclado (Tab, Shift+Tab, Enter, Escape, flechas). Verificar que todos los elementos interactivos son accesibles y el focus es visible.
5. **Verificar textos y contrastes**: Todos los textos de la interfaz deben tener un **contraste mínimo de 4.5:1** (WCAG AA) para texto normal y 3:1 para texto grande.
6. **Estados de la interfaz**: Verificar que todas las pantallas manejan correctamente los estados de carga (skeleton loaders), vacío (empty states con ilustración, texto y acción), error (mensaje de error y botón de reintentar) y datos (visualización normal).
7. **Microcopy**: Revisar todos los textos de la interfaz (etiquetas, placeholders, mensajes de error, tooltips, textos de botones) para que sean claros, concisos y útiles.

### 9. Fase 7: Responsive Design

**Objetivo**: Asegurar que la aplicación funciona y se ve correctamente en todos los tamaños de pantalla (móvil 320px, tablet 768px, desktop 1024px, desktop grande 1440px, desktop ultra-wide 1920px+).

**Actividades**:

1. Probar cada pantalla en 5 **breakpoints** diferentes usando las herramientas de desarrollo del navegador.
2. Adaptar el sidebar: overlay con backdrop en móvil, colapsado en tablet, expandido en desktop.
3. Adaptar las tablas: scroll horizontal en pantallas pequeñas, ocultar columnas menos importantes en móvil.
4. Adaptar los gráficos: reducir altura, apilar verticalmente en lugar de horizontalmente.
5. Adaptar los formularios: campos a ancho completo en móvil, en columnas en desktop.
6. Adaptar el dashboard: KPI cards en 1 columna (móvil) → 2 columnas (tablet) → 4-5 columnas (desktop).
7. Verificar que los modales, dropdowns y tooltips no se salen de la pantalla en resoluciones pequeñas.
8. Verificar que los botones y elementos táctiles tienen un tamaño mínimo de 44x44px (recomendación de Apple y Google para touch targets).

### 10. Fase 8: Empaquetado con Electron

**Objetivo**: Convertir la aplicación Angular en una aplicación de escritorio nativa para Windows, macOS y Linux.

**Actividades**:

1. Configurar el proceso principal (`main.js`), preload (`preload.js`) y `ElectronService` en Angular (siguiendo los patrones de la unidad 20).
2. Añadir funcionalidades nativas: menú nativo (Archivo, Edición, Ver, Ayuda), diálogos de archivo para exportar datos, notificaciones nativas para facturas vencidas, atajos de teclado globales (Ctrl+B para abrir/cerrar sidebar, Ctrl+D para toggle dark mode).
3. Configurar electron-builder (siguiendo la unidad 21) para generar instaladores para las 3 plataformas.
4. Generar instaladores de prueba.
5. Probar los instaladores (al menos en la plataforma del alumno, idealmente en una VM de otra plataforma).

### 11. Fase 9: Documentación final

**Objetivo**: Elaborar la documentación completa del proyecto.

**Entregables documentales**:

1. **README.md** en el repositorio de GitHub:
   - Título y descripción del proyecto.
   - Capturas de pantalla de las 5 pantallas principales.
   - Tecnologías utilizadas (badges de shields.io).
   - Instrucciones de instalación y ejecución (desarrollo y producción).
   - Estructura del proyecto (árbol de directorios).
   - Enlaces al despliegue de Storybook, Figma y demo.
   - Licencia.

2. **Memoria del proyecto (PDF)** con:
   - Portada (título, autor, fecha, logo).
   - Índice.
   - Introducción y objetivos.
   - Análisis y diseño: diagrama de casos de uso, diagrama de componentes, diseño en Figma (capturas de las 5 pantallas).
   - Implementación: arquitectura Angular, Design System implementado, decisiones técnicas justificadas.
   - Pruebas y validación: resultados de auditorías (Lighthouse, WAVE), capturas responsive.
   - Empaquetado con Electron: proceso, capturas del instalador y la app en escritorio.
   - Conclusiones y líneas futuras.
   - Referencias.

3. **Storybook desplegado**: Ejecutar `npm run build-storybook` y desplegar la carpeta `storybook-static` en GitHub Pages, Netlify o Vercel.

### 12. Rúbrica de evaluación detallada

| **Criterio** | **Peso** | **Excelente (10)** | **Notable (7-8)** | **Suficiente (5-6)** | **Insuficiente (<5)** |
|---|---|---|---|---|---|
| **Diseño en Figma** | 10% | Design System completo con componentes, variantes, Auto Layout, variables de diseño. 5+ pantallas diseñadas a alta fidelidad. Consistencia visual total. | 5 pantallas diseñadas correctamente. Uso de Auto Layout en la mayoría de componentes. Cierta consistencia visual. | Diseño básico con algunas pantallas. Poco uso de componentes y Auto Layout. | Sin diseño en Figma o diseño extremadamente pobre. |
| **Design System + Storybook** | 15% | 10+ componentes documentados en Storybook. Todas las variantes y estados cubiertos. Tests de interacción implementados. Accesibilidad verificada en cada componente. | 6-9 componentes documentados. Mayoría de variantes cubiertas. Storybook desplegado. | 3-5 componentes básicos documentados. Storybook funcional pero incompleto. | Sin Design System o sin Storybook. |
| **Funcionalidad** | 20% | Todas las funcionalidades (login, dashboard, clientes, facturas, productos, informes, configuración) implementadas y funcionando correctamente. Datos persistentes (localStorage/json-server). | ~80% de funcionalidades implementadas. Pequeños bugs no críticos. | ~60% de funcionalidades implementadas. Funcionalidad básica. | <50% de funcionalidades. Apenas funciona. |
| **Arquitectura Angular** | 10% | Feature-based, Smart/Dumb components, Signals para estado, lazy loading en todas las features, guards, interceptores, tipado estricto. Código limpio y organizado. | Buena organización. Uso de Signals en la mayoría de componentes. Lazy loading presente. Código aceptable. | Estructura básica (servicios, componentes). Poco uso de Signals. Sin lazy loading. | Sin estructura clara. Código desordenado, componentes gigantes. |
| **Tailwind + Responsive** | 10% | Design System implementado en Tailwind con `@theme`. Responsive verificado en 5 breakpoints. Dark mode funcional con transición suave. | Tailwind bien usado en toda la app. Responsive en la mayoría de pantallas. Dark mode implementado. | Tailwind usado de forma básica. Responsive en algunas pantallas. Sin dark mode. | Mal uso de Tailwind (clases repetitivas, no responsive). |
| **UX y Accesibilidad** | 10% | Lighthouse accesibilidad >= 95. Navegación por teclado completa. WAVE sin errores. Estados de carga/vacío/error en todas las pantallas. Microcopy revisado. | Lighthouse >= 85. Mayoría de criterios de accesibilidad cumplidos. Estados de UI implementados en la mayoría de pantallas. | Lighthouse >= 70. Algunos criterios de accesibilidad. Estados de UI parciales. | Sin consideración de UX o accesibilidad. Errores graves de contraste, focus, etiquetas. |
| **PDF / Exportación** | 10% | Facturas profesionales con diseño corporativo. Informes con gráficos incrustados. Exportación CSV/Excel funcional con datos correctos. | Facturas funcionales con diseño aceptable. Exportación CSV/Excel implementada. | PDF básico (texto + tabla simple). Exportación parcial. | No genera documentos o genera documentos rotos. |
| **Electron** | 10% | App empaquetada como instalador funcional. Menú nativo. Diálogos de archivo. Notificaciones. Probado en al menos 1 plataforma. | App ejecutable en Electron. Configuración básica de Electron. Menú nativo presente. | Configuración básica de Electron (main.js + preload.js). App se abre en ventana nativa. | Sin configuración de Electron. |
| **Código y buenas prácticas** | 5% | Código limpio, bien tipado, sin `any`, sin console.log, documentado, sin código comentado. ESLint sin errores. Prettier aplicado. | Código aceptable. Tipado mayoritario. Pocos `any`. ESLint con pocos warnings. | Código mejorable. Uso de `any` en varias partes. ESLint con varios warnings. | Código desordenado, sin tipado, con errores de compilación. |

**Criterios de evaluación oficiales mapeados**:

| **Criterio de evaluación** | **Dónde se evalúa en GesFlow** |
|---|---|
| RA1.a - Identifica elementos de diseño | Fase 1 (Figma), Fase 3 (Design System) |
| RA1.b - Aplica principios de diseño | Fase 1 (Figma) |
| RA1.c - Crea componentes reutilizables | Fase 3 (Design System + Storybook) |
| RA1.d - Diseña interfaces responsive | Fase 7 (Responsive Design) |
| RA2.a - Implementa interfaces con frameworks | Fase 2-5 (Angular) |
| RA2.b - Utiliza eventos y validación | Fase 5 (Formularios, Signals) |
| RA2.c - Gestiona el estado de la UI | Fase 5 (Signals, estado carga/vacío/error) |
| RA2.d - Aplica estilos | Fase 2 (Tailwind CSS 4) |
| RA3.a - Crea apps multiplataforma | Fase 8 (Electron) |
| RA3.b - Configura entorno escritorio | Fase 8 (Electron + Angular) |
| RA3.c - Implementa IPC | Fase 8 (Main Process + Preload) |
| RA3.d - Integra APIs nativas | Fase 8 (menú, diálogos, notificaciones) |
| RA4.a - Distribuye apps | Fase 8 (electron-builder) |
| RA4.b - Configura empaquetado | Fase 8 (electron-builder config) |
| RA4.c - Genera instaladores | Fase 8 (build) |
| RA5.a - Diseña dashboards | Fase 5 (Dashboard) |
| RA5.b - Utiliza librerías de gráficos | Fase 5 (Chart.js) |
| RA5.c - Integra gráficos en UI | Fase 5 (Dashboard, Informes) |
| RA5.d - Exporta datos de dashboards | Fase 5 (Exportación CSV/PDF) |
| RA6.a - Identifica tipos de informes | Fase 5 (Facturas, Informes) |
| RA6.b - Utiliza librerías PDF | Fase 5 (PDFMake) |
| RA6.c - Diseña plantillas | Fase 5 (Plantilla de factura PDF) |
| RA6.d - Genera documentos | Fase 5 (Factura PDF, informes, CSV, Excel) |
| RA6.e - Integra en flujo de app | Fase 5 (Botones generar/descargar) |

### 13. Entregables requeridos

1. **Enlace al repositorio GitHub** (público o privado con acceso al profesor). El repositorio debe incluir:
   - Código fuente completo de la aplicación Angular.
   - Archivos de configuración de Electron (`main.js`, `preload.js`).
   - Archivo `README.md` completo.
   - Archivo `.gitignore` correctamente configurado (sin `node_modules`, `dist`, `release`, `storybook-static`).

2. **Enlace al proyecto Figma** (archivo `.fig` o enlace de solo lectura al proyecto en Figma Community/Teams).

3. **Enlace a Storybook desplegado** (GitHub Pages, Netlify, Vercel o similar).

4. **Instaladores** (al menos 1 plataforma, idealmente 3):
   - Windows: archivo `.exe` (NSIS o portable).
   - macOS: archivo `.dmg`.
   - Linux: archivo `.AppImage` o `.deb`.

5. **Memoria del proyecto** en formato PDF.

### 14. Fragmentos de código de referencia

#### Servicio de facturas PDF completo (invoice-pdf.service.ts)

```typescript
import { Injectable } from '@angular/core';
import pdfMake from 'pdfmake/build/pdfmake';
import pdfFonts from 'pdfmake/build/vfs_fonts';
import { TDocumentDefinitions } from 'pdfmake/interfaces';
import { Invoice } from '../../core/models/invoice.model';
import { CompanyData } from '../../core/models/company.model';

@Injectable({ providedIn: 'root' })
export class InvoicePdfService {
  constructor() {
    pdfMake.vfs = pdfFonts.vfs;
  }

  generateInvoicePdf(invoice: Invoice, company: CompanyData): void {
    const docDef = this.buildInvoiceDocument(invoice, company);
    pdfMake.createPdf(docDef).download(`Factura_${invoice.number}.pdf`);
  }

  previewInvoicePdf(invoice: Invoice, company: CompanyData): void {
    const docDef = this.buildInvoiceDocument(invoice, company);
    pdfMake.createPdf(docDef).open();
  }

  private buildInvoiceDocument(invoice: Invoice, company: CompanyData): TDocumentDefinitions {
    const formatCurrency = (amount: number): string =>
      new Intl.NumberFormat('es-ES', { style: 'currency', currency: 'EUR' }).format(amount);

    const formatDate = (date: Date): string =>
      new Intl.DateTimeFormat('es-ES').format(date);

    const subtotal = invoice.lines.reduce((sum, line) => sum + line.quantity * line.unitPrice, 0);
    const taxGroups = this.groupTaxes(invoice.lines);
    const taxTotal = taxGroups.reduce((sum, g) => sum + g.amount, 0);
    const grandTotal = subtotal + taxTotal;

    return {
      pageSize: 'A4',
      pageMargins: [45, 50, 45, 50],
      header: (currentPage: number) => currentPage > 1 ? { text: `Factura ${invoice.number}`, style: 'headerText', alignment: 'right', margin: [0, 20, 45, 0] } : null,
      footer: (currentPage: number, pageCount: number) => ({
        text: `Página ${currentPage} de ${pageCount}`,
        alignment: 'center',
        style: 'footerText',
        margin: [0, 0, 0, 20]
      }),
      images: company.logoBase64 ? { companyLogo: company.logoBase64 } : {},
      defaultStyle: { font: 'Roboto', fontSize: 10, color: '#1f2937' },
      styles: {
        headerText: { fontSize: 8, color: '#9ca3af', italics: true },
        footerText: { fontSize: 8, color: '#9ca3af', italics: true },
        companyName: { fontSize: 16, bold: true, color: '#1e40af' },
        invoiceTitle: { fontSize: 26, bold: true, color: '#1e40af' },
        sectionTitle: { fontSize: 10, bold: true, color: '#6b7280', margin: [0, 0, 0, 4] },
        tableHeader: { fontSize: 9, bold: true, fillColor: '#1e40af', color: '#ffffff', alignment: 'center' },
        tableCell: { fontSize: 9 },
        tableCellRight: { fontSize: 9, alignment: 'right' },
        tableCellCenter: { fontSize: 9, alignment: 'center' },
        totalLabel: { fontSize: 10, bold: true, alignment: 'right', margin: [0, 3, 8, 0] },
        totalAmount: { fontSize: 11, bold: true, alignment: 'right', color: '#1e40af' }
      },
      content: [
        { image: 'companyLogo', width: 120, margin: [0, 0, 0, 15] },
        { text: 'FACTURA', style: 'invoiceTitle', margin: [0, 0, 0, 5] },
        { canvas: [{ type: 'line', x1: 0, y1: 0, x2: 470, y2: 0, lineWidth: 1, lineColor: '#e5e7eb' }], margin: [0, 0, 0, 15] },

        {
          columns: [
            { width: '55%', stack: [
              { text: 'DATOS DE LA EMPRESA', style: 'sectionTitle' },
              { text: company.name, style: 'companyName', margin: [0, 2, 0, 0] },
              { text: `CIF: ${company.taxId}`, fontSize: 9 },
              { text: company.address, fontSize: 9 },
              { text: `${company.postalCode} ${company.city}`, fontSize: 9 }
            ]},
            { width: '45%', stack: [
              { text: 'DATOS DE FACTURA', style: 'sectionTitle', alignment: 'right' },
              { text: `N.º: ${invoice.number}`, alignment: 'right', fontSize: 9 },
              { text: `Fecha: ${formatDate(invoice.issueDate)}`, alignment: 'right', fontSize: 9 },
              { text: `Vencimiento: ${formatDate(invoice.dueDate)}`, alignment: 'right', fontSize: 9 }
            ]}
          ],
          margin: [0, 0, 0, 20]
        },

        { text: 'DATOS DEL CLIENTE', style: 'sectionTitle' },
        { text: invoice.client.name, bold: true, margin: [0, 2, 0, 0] },
        { text: `NIF: ${invoice.client.taxId}`, fontSize: 9 },
        { text: invoice.client.address, fontSize: 9 },
        { margin: [0, 0, 0, 20] },

        {
          table: {
            headerRows: 1,
            widths: ['*', 50, 75, 50, 75],
            body: [
              [{ text: 'Concepto', style: 'tableHeader' }, { text: 'Cant.', style: 'tableHeader' }, { text: 'Precio Ud.', style: 'tableHeader' }, { text: 'IVA', style: 'tableHeader' }, { text: 'Importe', style: 'tableHeader' }],
              ...invoice.lines.map(line => {
                const lineTotal = line.quantity * line.unitPrice;
                return [
                  { text: line.description, style: 'tableCell' },
                  { text: line.quantity.toString(), style: 'tableCellCenter' },
                  { text: formatCurrency(line.unitPrice), style: 'tableCellRight' },
                  { text: `${line.taxRate}%`, style: 'tableCellCenter' },
                  { text: formatCurrency(lineTotal), style: 'tableCellRight' }
                ];
              }),
              [{ text: 'Base imponible', colSpan: 4, style: 'totalLabel' }, {}, {}, {}, { text: formatCurrency(subtotal), style: 'totalAmount' }],
              ...taxGroups.map(group => [
                { text: `IVA (${group.rate}%)`, colSpan: 4, style: 'totalLabel' }, {}, {}, {},
                { text: formatCurrency(group.amount), style: 'totalAmount' }
              ]),
              [{ text: 'TOTAL', colSpan: 4, style: { ...this.styles.totalLabel, fontSize: 12 } as any }, {}, {}, {}, { text: formatCurrency(grandTotal), style: { ...this.styles.totalAmount, fontSize: 13 } as any }]
            ]
          }
        },

        { text: '', margin: [0, 20, 0, 0] },

        {
          columns: [
            { width: '60%', stack: [
              { text: 'DATOS BANCARIOS', style: 'sectionTitle' },
              { text: company.bankAccount || 'ES00 0000 0000 0000 0000 0000', fontSize: 9 },
              { text: company.paymentTerms || 'Pago a 30 días', fontSize: 9, margin: [0, 5, 0, 0] }
            ]},
            { width: '40%', stack: [
              { qr: `https://gesflow.app/verify/${invoice.number}`, fit: 80, alignment: 'right' },
              { text: 'Verificar factura', fontSize: 8, alignment: 'center', margin: [0, 5, 0, 0], color: '#9ca3af' }
            ]}
          ]
        },

        { text: 'Gracias por su confianza', alignment: 'center', margin: [0, 30, 0, 0], color: '#9ca3af', italics: true }
      ]
    };
  }

  private groupTaxes(lines: any[]): { rate: number; amount: number }[] {
    const groups = new Map<number, number>();
    lines.forEach(line => {
      const lineTotal = line.quantity * line.unitPrice;
      const taxAmount = lineTotal * line.taxRate / 100;
      groups.set(line.taxRate, (groups.get(line.taxRate) || 0) + taxAmount);
    });
    return Array.from(groups.entries()).map(([rate, amount]) => ({ rate, amount }));
  }
}
```

#### Dashboard con Chart.js y Signals

```typescript
import { Component, inject, signal, computed, OnInit, effect } from '@angular/core';
import { DashboardService } from '../../core/services/dashboard.service';
import { ChartWidgetComponent } from '../../shared/components/chart-widget/chart-widget.component';
import { StatCardComponent } from '../../shared/components/stat-card/stat-card.component';
import { BadgeComponent } from '../../shared/components/badge/badge.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [ChartWidgetComponent, StatCardComponent, BadgeComponent],
  templateUrl: './dashboard.component.html'
})
export class DashboardComponent implements OnInit {
  private dashboardService = inject(DashboardService);

  isLoading = signal(true);
  error = signal<string | null>(null);
  dateRange = signal<{ start: Date; end: Date }>({
    start: new Date(new Date().getFullYear(), 0, 1),
    end: new Date()
  });

  dashboardData = signal<any>(null);

  kpis = computed(() => {
    const data = this.dashboardData();
    if (!data) return [];
    return [
      { label: 'Ingresos totales', value: new Intl.NumberFormat('es-ES', { style: 'currency', currency: 'EUR' }).format(data.totalRevenue), trend: data.revenueTrend, icon: 'payments' },
      { label: 'Facturas emitidas', value: data.totalInvoices.toString(), trend: data.invoicesTrend, icon: 'receipt_long' },
      { label: 'Clientes activos', value: data.activeClients.toString(), trend: data.clientsTrend, icon: 'people' },
      { label: 'Ticket medio', value: new Intl.NumberFormat('es-ES', { style: 'currency', currency: 'EUR' }).format(data.averageTicket), trend: data.ticketTrend, icon: 'shopping_cart' },
      { label: 'Tasa de cobro', value: `${data.collectionRate}%`, trend: data.collectionTrend, icon: 'check_circle' }
    ];
  });

  revenueChartLabels = computed(() => {
    const data = this.dashboardData();
    return data?.monthlyRevenue?.map((m: any) => m.month) ?? [];
  });

  revenueChartDatasets = computed(() => {
    const data = this.dashboardData();
    return [{
      label: 'Ingresos',
      data: data?.monthlyRevenue?.map((m: any) => m.amount) ?? [],
      borderColor: '#3b82f6',
      backgroundColor: 'rgba(59, 130, 246, 0.1)',
      tension: 0.3,
      fill: true
    }];
  });

  topProductsLabels = computed(() => {
    const data = this.dashboardData();
    return data?.topProducts?.map((p: any) => p.name) ?? [];
  });

  topProductsDatasets = computed(() => {
    const data = this.dashboardData();
    return [{
      label: 'Ingresos',
      data: data?.topProducts?.map((p: any) => p.revenue) ?? [],
      backgroundColor: ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444']
    }];
  });

  categoryLabels = computed(() => this.dashboardData()?.revenueByCategory?.map((c: any) => c.category) ?? []);
  categoryDatasets = computed(() => [{
    data: this.dashboardData()?.revenueByCategory?.map((c: any) => c.amount) ?? [],
    backgroundColor: ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444', '#ec4899']
  }]);

  recentInvoices = computed(() => this.dashboardData()?.recentInvoices ?? []);

  constructor() {
    effect(() => {
      // Cuando cambie el rango de fechas, recargar datos
      this.loadDashboardData();
    });
  }

  ngOnInit(): void {
    this.loadDashboardData();
  }

  loadDashboardData(): void {
    this.isLoading.set(true);
    this.error.set(null);

    this.dashboardService.getDashboardData(this.dateRange()).subscribe({
      next: (data) => {
        this.dashboardData.set(data);
        this.isLoading.set(false);
      },
      error: (err) => {
        this.error.set('Error al cargar los datos del dashboard. Intente de nuevo.');
        this.isLoading.set(false);
      }
    });
  }

  changeDateRange(range: string): void {
    const now = new Date();
    let start: Date;

    switch (range) {
      case '7d': start = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000); break;
      case '30d': start = new Date(now.getTime() - 30 * 24 * 60 * 60 * 1000); break;
      case '90d': start = new Date(now.getTime() - 90 * 24 * 60 * 60 * 1000); break;
      case '1y': start = new Date(now.getFullYear(), 0, 1); break;
      default: start = new Date(now.getTime() - 30 * 24 * 60 * 60 * 1000);
    }

    this.dateRange.set({ start, end: now });
  }

  getStatusBadge(status: string): { variant: string; label: string } {
    switch (status) {
      case 'paid': return { variant: 'success', label: 'Pagada' };
      case 'pending': return { variant: 'warning', label: 'Pendiente' };
      case 'overdue': return { variant: 'danger', label: 'Vencida' };
      default: return { variant: 'neutral', label: status };
    }
  }

  exportCsv(): void { /* implementar exportación CSV */ }
  exportPdf(): void { /* implementar exportación PDF con gráficos */ }
}
```

??? "Actividades de ampliación"

    ### Ampliación 1: Tests unitarios con Jasmine/Karma

    Implementa tests unitarios para al menos 5 servicios y 5 componentes:
    - `AuthService`: test de login exitoso, login fallido, registro, logout.
    - `InvoicePdfService`: test de generación de documento PDF (verificar estructura).
    - `ButtonComponent`: test de renderizado con diferentes inputs, test de emisión de eventos.
    - `StatCardComponent`: test de renderizado de KPI positivo/negativo.
    - `ClientFormComponent`: test de validación de formulario.

    ### Ampliación 2: Tests end-to-end con Cypress o Playwright

    Implementa al menos 5 tests e2e que cubran flujos completos:
    - Login → Dashboard → Navegación a Clientes → Crear cliente → Verificar en listado.
    - Crear factura con líneas → Vista previa → Emitir → Verificar estado.
    - Dashboard → Cambiar rango de fechas → Verificar que los gráficos se actualizan.
    - Exportar CSV de clientes → Verificar descarga.
    - Modo oscuro → Cambiar tema → Verificar que persiste al recargar.

    ### Ampliación 3: CI/CD completo con GitHub Actions

    Implementa un pipeline CI/CD que ejecute: lint → tests unitarios → build de Angular → build de Storybook → deploy de Storybook a GitHub Pages → build de Electron → release de GitHub con instaladores (todo automatizado al pushear un tag).

    ### Ampliación 4: PWA (Progressive Web Application)

    Convierte la aplicación Angular en una PWA instalable en dispositivos móviles y escritorio:
    - Añade `@angular/pwa` (`ng add @angular/pwa`).
    - Configura el Service Worker para cache offline.
    - Personaliza el manifest (nombre, iconos, colores, orientación).
    - Prueba la instalación en un dispositivo Android y en Chrome Desktop.

    ### Ampliación 5: Backend real con Firebase o Supabase

    Sustituye el json-server por un backend real:
    - Firebase: Authentication (login/registro con email/password), Firestore (base de datos NoSQL para clientes, facturas, productos), Storage (para logos y avatares).
    - Supabase: alternativa open source a Firebase con PostgreSQL, autenticación y storage.

    ### Ampliación 6: Internacionalización (i18n)

    Añade soporte para español e inglés:
    - Implementa `@angular/localize` o `ngx-translate`.
    - Traduce toda la interfaz (menús, etiquetas, mensajes de error, tooltips, textos de botones).
    - Añade un selector de idioma en la configuración.
    - Adapta formatos de fecha, moneda y número según el idioma seleccionado.

    ### Ampliación 7: Versión móvil con Capacitor

    Migra la aplicación a una app móvil nativa para Android e iOS usando Capacitor:
    - Instala Capacitor: `npm install @capacitor/core @capacitor/cli`.
    - Adapta la UI para pantallas táctiles pequeñas.
    - Añade funcionalidades nativas móviles (cámara para avatar, GPS para dirección, compartir factura por WhatsApp).

!!! tip "Buenas prácticas"

    1. **Empieza por el diseño, no por el código**: Invierte tiempo en Figma al principio. ==Un diseño bien pensado ahorra horas de refactorización de código.== Los componentes del Design System deben diseñarse en Figma antes de implementarse en Angular.

    2. **Un componente a la vez**: No intentes implementar todos los componentes del Design System de golpe. Implementa uno, documéntalo en Storybook, verifica su accesibilidad, y solo entonces pasa al siguiente.

    3. **Commits frecuentes y con mensajes descriptivos**: Sigue el estándar de conventional commits: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`. Cada commit debe ser atómico (un solo cambio lógico).

    4. **Prueba en el navegador antes que en Electron**: La aplicación debe funcionar perfectamente en el navegador (`ng serve`). Electron es una capa adicional que añade funcionalidades nativas, no un requisito para que la funcionalidad básica funcione.

    5. **No dejes la accesibilidad para el final**: Incorpora consideraciones de accesibilidad desde el primer componente. Añadir accesibilidad al final es mucho más costoso que incluirla desde el diseño.

    6. **Separa lógica de presentación**: Componentes Smart (contenedores) manejan la lógica de negocio y el estado. Componentes Dumb (presentacionales) reciben datos por `@Input()` y emiten eventos por `@Output()`. Esta separación facilita el testing y la reutilización.

    7. **Usa Signals para estado reactivo, no para todo**: Signals son excelentes para estado de UI (tema, sidebar, formularios, datos cargados). Para estado de servidor (datos que vienen de API), considera usar RxJS con `HttpClient`, que ya es reactivo.

    8. **Documenta mientras desarrollas**: No dejes el README y la memoria para el último día. Ve tomando capturas, documentando decisiones y escribiendo secciones de la memoria a medida que avanzas en las fases.

    9. **Prioriza funcionalidad sobre perfección**: Es preferible tener todas las funcionalidades implementadas de forma aceptable que 2 funcionalidades perfectas y el resto sin hacer. La rúbrica valora la completitud.

    10. **Pide feedback**: Muestra tu progreso a compañeros y al profesor regularmente. Un par de ojos frescos detectan problemas de usabilidad y bugs que el desarrollador pasa por alto por estar inmerso en el código.

!!! warning "Errores frecuentes"

    1. **Empezar a programar sin tener el diseño en Figma**: Sin un diseño previo, la implementación carece de dirección y el resultado es inconsistente visualmente. ==Es el error más común y el que más tiempo hace perder.==

    2. **No tipar correctamente con TypeScript**: Usar `any` en los modelos de datos, en los servicios o en las respuestas de la API. Esto anula las ventajas de TypeScript y hace que los errores aparezcan en tiempo de ejecución en lugar de en tiempo de compilación.

    3. **Crear componentes gigantes (God Components)**: Un componente de 500 líneas que hace de todo (tabla + formulario + filtros + paginación) es difícil de mantener, testear y reutilizar. Divide en componentes más pequeños con responsabilidades claras.

    4. **Olvidar destruir instancias de Chart.js**: Si no se llama a `chart.destroy()` en `ngOnDestroy`, cada vez que se navega al dashboard se crea una nueva instancia sin liberar la anterior, causando fugas de memoria.

    5. **No probar en diferentes navegadores y dispositivos**: "En mi Chrome funciona" no es suficiente. La aplicación debe probarse en Firefox, Edge, Safari, Chrome, y en diferentes tamaños de pantalla. Electron usa Chromium, pero la versión web puede ser usada en cualquier navegador.

    6. **Ignorar los estados de carga, vacío y error**: Mostrar una pantalla en blanco mientras se cargan los datos, no mostrar nada cuando no hay resultados, o que la app se rompa cuando falla una petición HTTP. Son errores de UX graves y fáciles de prevenir.

    7. **Hardcodear valores en lugar de usar Design Tokens**: Poner colores en hexadecimal directamente en los componentes en lugar de usar las variables de Tailwind `@theme`. Cuando se quiera cambiar el color primario, habrá que modificar cientos de archivos.

    8. **No configurar correctamente el routing y la navegación**: URLs que no reflejan la estructura de la aplicación, navegación que no actualiza el breadcrumb, botones "volver" que usan `history.back()` en lugar del router de Angular.

    9. **Generar el PDF con datos no validados**: Si la factura tiene datos incorrectos (importes negativos, fechas inválidas, cliente no seleccionado), el PDF se generará con esos errores. Valida los datos antes de pasarlos al generador de PDF.

    10. **No probar el instalador generado**: Asumir que si electron-builder termina sin errores, el instalador funciona. Siempre se debe probar el instalador en una máquina limpia (o VM).

!!! abstract "Resumen"

    El Proyecto Final Integrador "GesFlow" constituye la culminación del módulo 0488 Desarrollo de Interfaces, integrando todos los conocimientos, competencias y habilidades adquiridos a lo largo de las 19 unidades didácticas anteriores en un único proyecto completo de aplicación empresarial.

    La metodología en 9 fases —diseño, configuración, Design System, layout, funcionalidades, UX/accesibilidad, responsive, Electron y documentación— proporciona una estructura clara y realista para la ejecución del proyecto, simulando el flujo de trabajo de un equipo profesional de desarrollo de software.

    El proyecto abarca todas las áreas del módulo: diseño de interfaces con Figma (aplicando Auto Layout, componentes, variantes y Design Tokens), implementación del Design System con Storybook (10+ componentes documentados y accesibles), desarrollo Angular standalone con arquitectura feature-based (lazy loading, Signals, Reactive Forms, guards, interceptores), maquetación con Tailwind CSS 4 y `@theme`, dashboard con Chart.js, generación de documentos PDF profesionales con PDFMake, exportación de datos (CSV, Excel), empaquetado de escritorio con Electron (main.js, preload.js, electron-builder), y documentación técnica completa.

    La rúbrica de evaluación detallada, con 9 criterios y pesos específicos, y el mapeo a los criterios de evaluación oficiales del currículo DAM, garantizan una evaluación objetiva, transparente y alineada con la normativa educativa de Andalucía.

    Las actividades de ampliación (tests, CI/CD, PWA, backend real, i18n, Capacitor) ofrecen al alumnado avanzado la oportunidad de profundizar y diferenciar su proyecto, preparándolos para los requisitos del mercado laboral actual.

## Recursos complementarios

- **Angular - Documentación oficial**: https://angular.dev/
- **Tailwind CSS 4 - Documentación**: https://tailwindcss.com/docs/theme
- **Chart.js - Documentación**: https://www.chartjs.org/docs/
- **PDFMake - Playground**: http://pdfmake.org/playground.html
- **Electron - Documentación**: https://www.electronjs.org/docs/
- **electron-builder - Configuración**: https://www.electron.build/
- **Storybook para Angular**: https://storybook.js.org/docs/angular/get-started
- **Figma - Guía de Design Systems**: https://help.figma.com/hc/en-us
- **WCAG 2.2 - Pautas de accesibilidad**: https://www.w3.org/WAI/WCAG22/quickref/
- **Lighthouse - Extensión de Chrome**: https://chromewebstore.google.com/detail/lighthouse/
- **WAVE - Herramienta de accesibilidad**: https://wave.webaim.org/
- **axe DevTools**: https://www.deque.com/axe/devtools/
- **json-server**: https://github.com/typicode/json-server
- **json-server-auth**: https://github.com/jeremyben/json-server-auth
- **Conventional Commits**: https://www.conventionalcommits.org/
- **GitHub Pages para Storybook**: https://storybook.js.org/docs/sharing/publish-storybook

**Plantillas y ejemplos de referencia**:
- Repositorio de ejemplo completo (búsqueda recomendada): "angular standalone tailwind dashboard github"
- Colección de componentes accesibles: https://www.w3.org/WAI/ARIA/apg/patterns/
- Ejemplos de facturas con PDFMake: http://pdfmake.org/playground.html (buscar "invoice")
