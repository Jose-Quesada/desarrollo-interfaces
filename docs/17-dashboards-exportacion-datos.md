---
icon: lucide/layout-dashboard
---

# Dashboards y Visualización de Datos

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Comprender qué es un **dashboard empresarial**, su propósito como panel de control para la toma de decisiones basada en datos, y los principios fundamentales de diseño que lo diferencian de una simple colección de gráficos.
2. Dominar la librería **Chart.js** como herramienta principal para la creación de gráficos interactivos en aplicaciones Angular, incluyendo todos los tipos de gráficos disponibles, su configuración detallada y los criterios para elegir el tipo de gráfico adecuado según los datos a visualizar y la historia que se quiere contar.
3. Conocer y utilizar **ApexCharts** como alternativa moderna a Chart.js, valorando sus ventajas en cuanto a interactividad, estética por defecto, tipos de gráficos adicionales (radialBar, heatmap, treemap) y soporte nativo para modo oscuro.
4. Integrar gráficos en componentes Angular de forma reactiva utilizando **Signals**, gestionando correctamente el ciclo de vida de las instancias de Chart.js (inicialización en ngAfterViewInit, actualización reactiva con chart.update(), destrucción en ngOnDestroy).
5. Diseñar dashboards completos en Angular con layouts profesionales utilizando **CSS Grid** y Tailwind CSS, combinando diferentes tipos de widgets (tarjetas KPI, gráficos de diferentes tipos, tablas de datos, filtros temporales).
6. Implementar componentes reutilizables para dashboards: **StatCard** (icono, valor numérico, tendencia porcentual), **ChartWidget** (gráfico genérico configurable mediante inputs) y **DataTable** (tabla con ordenación y paginación).
7. Integrar la exportación de datos y gráficos desde el dashboard a formatos portables (**CSV, Excel, PDF**), incluyendo la captura de gráficos Chart.js como imágenes base64 para incrustar en PDFs generados con **PDFMake**.
8. Aplicar principios de experiencia de usuario (**UX**) y accesibilidad en el diseño de dashboards, garantizando que la información es comprensible, la navegación es intuitiva y los gráficos son accesibles para usuarios con discapacidad visual (descripciones textuales alternativas, contraste de colores suficiente, no depender exclusivamente del color para transmitir información).

## Resultado de aprendizaje asociado

Esta unidad contribuye, como RA principal, al **RA 5** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 5.** Crea informes evaluando y utilizando herramientas gráficas.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- **CE b)** Se han generado informes básicos a partir de diferentes fuentes de datos mediante asistentes.
- **CE d)** Se han incluido valores calculados, recuentos y totales.
- **CE e)** Se han incluidos gráficos generados a partir de los datos.

Como RA secundario, se vincula al **RA 4** («Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad»):

- **CE g)** Se ha diseñado el aspecto de la interfaz de usuario (colores y fuentes entre otros) atendiendo a su legibilidad.
- **CE i)** Se han realizado pruebas para evaluar la usabilidad y accesibilidad de la aplicación.

> Nota: los dashboards y paneles de KPI son una forma de informe gráfico interactivo. Las librerías de visualización (Chart.js, ApexCharts, D3.js), la actualización reactiva de datos y la exportación (CSV/Excel/PDF) son las herramientas con las que se materializan estos criterios.

!!! note "Conocimientos previos"

    - **Fundamentos de Angular**: componentes standalone, sistema de inyección de dependencias con `inject()`, ciclo de vida de los componentes (especialmente `ngOnInit`, `ngAfterViewInit` y `ngOnDestroy`), manejo de Signals para estado reactivo, directivas estructurales (`@for`, `@if`), pipes para formateo de datos.
    - **TypeScript avanzado**: interfaces para tipado de datos de gráficos, tipos genéricos para componentes reutilizables, tipos de unión para estados de carga/datos/error, funciones de transformación de datos tipadas.
    - **Maquetación avanzada con CSS**: dominio de CSS Grid para layouts de dashboard complejos, Flexbox para alineación y distribución, diseño responsive con media queries y enfoque Mobile First, uso de Tailwind CSS como framework de utilidades (clases `grid`, `grid-cols`, `col-span`, `gap`, `responsive:`).
    - **Manejo de datos asíncronos**: consumo de APIs REST con HttpClient, transformación de datos de API al formato requerido por las librerías de gráficos, manejo de estados de carga (loading), error y datos vacíos, RxJS básico (Observables, suscripciones y operadores como map, filter, switchMap).
    - **Principios básicos de estadística y visualización de datos**: comprensión de medidas de tendencia central (media, mediana, moda), medidas de dispersión (rango, desviación estándar), tipos de datos (categóricos, numéricos, temporales), relación entre tipo de dato y tipo de gráfico adecuado.
    - **Control de versiones con Git**: manejo de ramas, commits, gestión de dependencias externas con npm.

## Contenidos

1. **Introducción a los dashboards empresariales**
   - 1.1. Definición y propósito: panel de control visual que consolida KPIs, métricas y datos clave en una sola vista para facilitar la monitorización y la toma de decisiones.
   - 1.2. Diferencias entre un dashboard, un informe y un cuadro de mando.
   - 1.3. Tipos de dashboards: operacionales (monitorización en tiempo real, segundos/minutos), tácticos (análisis semanal/mensual, mandos intermedios), estratégicos (visión a largo plazo, alta dirección, trimestral/anual).
   - 1.4. Principios de diseño de dashboards según Edward Tufte y Stephen Few: maximizar la proporción datos-tinta (data-ink ratio), eliminar el chartjunk (decoración innecesaria), presentar la información de un vistazo, jerarquía visual clara, sin ruido ni distracciones.
   - 1.5. Anatomía de un dashboard típico: fila superior de KPI cards, zona central con gráficos principales, panel lateral o inferior con tabla de datos, filtros temporales y de segmentación en la parte superior.

2. **La librería Chart.js en profundidad**
   - 2.1. Instalación en proyectos Angular standalone: `npm install chart.js`.
   - 2.2. Conceptos fundamentales: `Chart` (instancia del gráfico), `type` (tipo de gráfico), `data` (labels + datasets), `options` (configuración de aspecto y comportamiento), `plugins` (extensiones).
   - 2.3. Tipos de gráficos disponibles en Chart.js v4 y criterios de selección:
     - **Barras (bar)**: comparar categorías discretas. Subtipos: vertical, horizontal (`indexAxis: 'y'`), apiladas (stacked), agrupadas.
     - **Líneas (line)**: evolución temporal, tendencias, series temporales. Subtipos: línea simple, línea con área (fill), múltiples series, stepped.
     - **Circular (doughnut/pie)**: composición, proporciones, partes de un todo. Doughnut (anillo, recomendado sobre pie por mejor legibilidad) vs pie (círculo completo).
     - **Radar**: comparación multivariable, perfiles, habilidades, evaluación 360°.
     - **Polar area**: similar a circular pero cada sector tiene el mismo ángulo y el radio varía. Útil para comparar magnitudes relativas.
     - **Burbujas (bubble)**: visualizar 3 dimensiones (x, y, radio = tercera variable). Útil para análisis de cartera de productos (crecimiento vs cuota de mercado, tamaño de burbuja = ingresos).
     - **Dispersión (scatter)**: correlación entre dos variables numéricas.
     - **Área (area)**: evolución temporal con énfasis en el volumen acumulado.
     - **Velas (candlestick)**: series financieras (precio de apertura, cierre, máximo, mínimo).
   - 2.4. Configuración detallada de un gráfico Chart.js:
     - `type`: string con el tipo de gráfico.
     - `data`: objeto con `labels` (array de etiquetas para el eje X) y `datasets` (array de objetos, cada uno representando una serie de datos).
     - `datasets`: cada dataset incluye `label` (nombre de la serie, aparece en la leyenda), `data` (array de valores numéricos), `backgroundColor` (color de relleno), `borderColor` (color del borde), `borderWidth`, `tension` (suavizado de curvas, 0 = líneas rectas, 0.4 = curvas suaves), `fill` (relleno bajo la línea), `pointRadius`, `pointHoverRadius`.
     - `options`: objeto masivo de configuración con subsecciones para `responsive` (booleano, ajuste automático al contenedor), `maintainAspectRatio` (mantener proporción), `scales` (configuración de ejes X e Y), `plugins` (leyenda, tooltip, título, zoom, anotaciones), `animation` (duración y tipo de animación), `interaction` (modo de interacción: nearest, index, dataset, point).
   - 2.5. Configuración de escalas (ejes):
     - Eje Y (`y`): `beginAtZero` (empezar desde cero), `min`/`max` (límites), `ticks` (callback para formatear etiquetas, stepSize), `grid` (color y estilo de las líneas de la cuadrícula), `title` (texto y estilo del título del eje).
     - Eje X (`x`): similar al eje Y. Para datos temporales, `type: 'time'` requiere el adaptador `chartjs-adapter-date-fns` o `chartjs-adapter-luxon`.
   - 2.6. Plugins de Chart.js:
     - **Legend** (leyenda): `display`, `position` (top, bottom, left, right, chartArea), `labels` (usePointStyle, padding, font, color).
     - **Tooltip**: información emergente al pasar el cursor. `enabled`, `mode`, `intersect`, `callbacks` (label, title, afterBody para personalizar el contenido del tooltip).
     - **Title**: título del gráfico. `display`, `text`, `position`, `font`, `color`.
     - **Zoom** (plugin externo `chartjs-plugin-zoom`): permite hacer zoom y desplazamiento (pan) en gráficos con muchos datos.
     - **Annotation** (plugin externo `chartjs-plugin-annotation`): añadir líneas de referencia, áreas sombreadas, anotaciones de texto.
     - **Datalabels** (plugin externo `chartjs-plugin-datalabels`): mostrar los valores numéricos directamente sobre los elementos del gráfico.
   - 2.7. Registro de elementos de Chart.js (Tree shaking): para optimizar el bundle, Chart.js permite registrar solo los elementos necesarios (controllers, elements, scales, plugins) en lugar de importar toda la librería.

3. **Chart.js en Angular: integración y ciclo de vida**
   - 3.1. Acceso al elemento canvas mediante `@ViewChild('chartCanvas', { static: true }) canvasRef!: ElementRef<HTMLCanvasElement>`.
   - 3.2. Creación de la instancia: `this.chart = new Chart(this.canvasRef.nativeElement, config)`.
   - 3.3. Inicialización en `ngAfterViewInit()`: en este punto del ciclo de vida, el canvas ya está disponible en el DOM. Es el momento correcto para crear la instancia de Chart.
   - 3.4. Destrucción en `ngOnDestroy()`: `this.chart?.destroy()` para evitar fugas de memoria. Chart.js mantiene referencias internas a temporizadores y event listeners que deben limpiarse.
   - 3.5. Actualización reactiva: cuando los datos cambian (por Signals o Inputs), actualizar `this.chart.data` y llamar a `this.chart.update()`. Se puede pasar un modo de transición: `'none'` (sin animación, instantáneo), `'default'` (con animación).
   - 3.6. Componente `ChartWidget` reutilizable: encapsula la lógica de Chart.js en un componente standalone que recibe la configuración como `@Input()`, gestiona el ciclo de vida y expone métodos para actualizar datos y exportar a imagen.
   - 3.7. Integración con Signals: usar `computed()` para transformar los datos de la aplicación al formato `{ labels, datasets }` que espera Chart.js. Usar `effect()` para reaccionar a cambios en los datos y llamar a `chart.update()`.

4. **ApexCharts: la alternativa moderna**
   - 4.1. Instalación: `npm install apexcharts ng-apexcharts`.
   - 4.2. Ventajas sobre Chart.js: más tipos de gráficos (radialBar, heatmap, treemap, candlestick, boxPlot, rangeBar), animaciones más fluidas, mejor estética por defecto (no requiere tanta personalización para verse profesional), tooltips más ricos, modo oscuro integrado (configuración `theme: { mode: 'dark' }`), mayor interactividad (zoom, selección, drill-down).
   - 4.3. Desventajas: bundle más pesado (~500 KB vs ~250 KB de Chart.js), curva de aprendizaje ligeramente mayor, documentación extensa pero a veces confusa, la versión comunitaria gratuita tiene limitaciones (la versión de pago añade exportación nativa a PDF/CSV/PNG/SVG).
   - 4.4. Componente `apx-chart` en Angular: `<apx-chart [series]="series" [chart]="chartOptions" [xaxis]="xaxis"></apx-chart>`.
   - 4.5. Tipos de gráficos exclusivos de ApexCharts:
     - **RadialBar**: medidores circulares, ideales para KPIs (porcentaje de objetivo alcanzado, nivel de ocupación, tasa de conversión). Permiten un diseño muy visual tipo velocímetro.
     - **Heatmap**: matriz de colores donde la intensidad del color representa la magnitud. Ideal para visualizar patrones temporales (actividad por hora del día y día de la semana).
     - **Treemap**: rectángulos anidados cuyo tamaño representa una magnitud. Ideal para visualizar jerarquías y composición (ventas por categoría > subcategoría > producto).
     - **Candlestick**: gráfico de velas para series financieras con OHLC (Open, High, Low, Close).
   - 4.6. Configuración de ApexCharts en Angular:
     ```typescript
     import { ChartComponent, ApexChartComponent } from 'ng-apexcharts';
     // En el template:
     // <apx-chart [series]="chartSeries" [chart]="chartConfig" [xaxis]="chartXaxis"></apx-chart>
     ```

5. **Diseño de dashboards en Angular con Tailwind CSS**
   - 5.1. Layouts con CSS Grid y Tailwind:
     - `grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4` para la fila de KPI cards (1 columna en móvil, 2 en tablet, 4 en desktop).
     - `grid grid-cols-1 lg:grid-cols-3 gap-6` para la zona central (gráfico principal ocupa 2 columnas, gráfico secundario 1 columna).
     - `col-span-2` para que un gráfico grande ocupe dos columnas.
   - 5.2. Componentes widget para dashboards:
     - **StatCard**: tarjeta de indicador KPI. Muestra icono (svg o emoji), etiqueta, valor numérico grande, variación porcentual (flecha arriba/abajo en verde/rojo), comparación con período anterior. Estados: carga (skeleton), error, datos.
     - **ChartWidget**: gráfico genérico reutilizable. Recibe `@Input() config`, `@Input() data`, `@Input() type`. Gestiona la instancia de Chart.js/ApexCharts, actualización reactiva, y exportación a imagen.
     - **FilterBar**: barra de filtros con selector de rango de fechas (input date o datepicker), dropdown de categorías, botón de aplicar/limpiar filtros.
   - 5.3. Modo oscuro/claro en dashboards:
     - ApexCharts soporta `theme: { mode: 'dark' }` nativamente.
     - Chart.js requiere cambiar manualmente los colores del grid, labels, tooltips cuando se cambia de tema. Estrategia: escuchar cambios de tema (Signal `isDarkMode`) y regenerar la configuración del gráfico o usar un `effect()` que actualice `chart.options.scales` y llame a `chart.update()`.
   - 5.4. Estados del dashboard: vacío (sin datos, mostrar ilustración y mensaje orientativo), carga (skeleton loaders para gráficos y KPI cards), error (mensaje de error y botón de reintentar), datos (visualización normal), actualización (indicador sutil de última actualización y botón de refrescar).

6. **Exportación de datos y gráficos desde el dashboard**
   - 6.1. Botón "Exportar CSV": convierte los datos subyacentes de cualquier tabla o gráfico a CSV y descarga el archivo (usando el `CsvExportService` desarrollado en la unidad anterior).
   - 6.2. Botón "Exportar Excel": genera un archivo Excel con los datos del dashboard.
   - 6.3. Botón "Exportar PDF": genera un informe PDF de 1-2 páginas que incluye los KPI cards como tabla resumen, los gráficos como imágenes (capturados con `chart.toBase64Image()`) y las tablas de datos. Utiliza el `PdfService` de la unidad anterior.
   - 6.4. Captura de gráficos como imagen: `const base64Image = this.chart.toBase64Image('image/png', 1.0);` — donde el segundo parámetro es la calidad (0.0 a 1.0). La imagen resultante puede incrustarse directamente en un PDF con PDFMake como `{ image: base64Image, width: 450 }`.

7. **Proyecto integrador de la unidad: Dashboard empresarial completo**
   - 7.1. Especificación funcional:
     - 4 tarjetas KPI (ingresos totales, número de pedidos, ticket medio, tasa de conversión) con indicador de tendencia (+12%, -3%, etc.) respecto al período anterior.
     - Gráfico de líneas: evolución de ingresos mensuales en los últimos 12 meses (1 serie).
     - Gráfico de barras: top 5 productos por ingresos (horizontal para mejor legibilidad de nombres largos).
     - Gráfico circular (doughnut): distribución de ingresos por categoría de producto.
     - Tabla de últimos 10 pedidos con columnas: ID, cliente, fecha, importe, estado (badge de color).
     - Barra de filtros: selector de rango de fechas (últimos 7 días, 30 días, 90 días, año actual, año anterior, personalizado).
     - Botones de exportación: CSV, Excel, PDF (informe resumen).
   - 7.2. Especificación técnica:
     - Componentes standalone Angular.
     - `DashboardLayoutComponent` como componente padre que gestiona los filtros y distribuye los datos.
     - `StatCardComponent` reutilizable con `@Input() label`, `@Input() value`, `@Input() trend`, `@Input() icon`.
     - `ChartWidgetComponent` reutilizable que encapsula Chart.js.
     - Signals para el estado reactivo de los datos del dashboard y los filtros activos.
     - `computed()` para recalcular los datos filtrados cuando cambien los filtros.
     - Lazy loading del módulo de dashboard (`loadComponent` en las rutas).
     - Tailwind CSS para el layout responsive.

## Desarrollo teórico

### 1. Introducción a los dashboards empresariales

!!! info "Definición"

    Un **dashboard** es mucho más que una colección de gráficos bonitos en una pantalla. En el contexto empresarial, un dashboard es una herramienta de apoyo a la toma de decisiones que presenta, de forma visual y consolidada, los indicadores clave de rendimiento (**KPIs**) y las métricas más relevantes para un rol específico dentro de la organización.

La diferencia fundamental entre un dashboard y un informe tradicional es la **inmediatez** y la **accionabilidad**. Un informe de 50 páginas en PDF puede contener información valiosísima, pero un directivo que necesita tomar una decisión en los próximos 5 minutos no tiene tiempo de leerlo. Un buen dashboard le da esa información de un vistazo, destacando lo anómalo (lo que requiere atención inmediata) y contextualizando lo normal (para que no despiste).

#### 1.1. Tipos de dashboards y sus audiencias

La clasificación más aceptada distingue tres tipos de dashboards según su propósito temporal y su audiencia:

**Dashboards operacionales**:
- **Propósito**: Monitorizar procesos de negocio en tiempo real o casi real (segundos, minutos, horas).
- **Audiencia**: Personal de primera línea, operadores, supervisores de turno.
- **Ejemplos**: Panel de control de un centro de atención al cliente (llamadas en cola, tiempo medio de espera, agentes disponibles, satisfacción en tiempo real); monitorización de servidores (CPU, memoria, tráfico de red, errores 500); panel de seguimiento de pedidos de un e-commerce (pedidos por minuto, tasa de conversión, carritos abandonados en la última hora).
- **Características**: Datos muy frecuentes, enfocados en la excepción (alertas cuando algo se sale de los rangos normales), diseño simple y directo, a menudo en pantallas grandes (monitores de pared) visibles por todo el equipo.

**Dashboards tácticos**:
- **Propósito**: Analizar tendencias a medio plazo (semanas, meses) y apoyar la planificación táctica.
- **Audiencia**: Mandos intermedios, jefes de departamento, analistas de negocio.
- **Ejemplos**: Panel de ventas mensual por región, producto y vendedor; panel de marketing con ROAS (Return On Ad Spend), CAC (Customer Acquisition Cost), y rendimiento de campañas; panel de RRHH con rotación, absentismo y satisfacción de empleados.
- **Características**: Datos actualizados diaria o semanalmente, mayor profundidad analítica, capacidad de filtrar y segmentar (drill-down: pasar de vista agregada a detalle), gráficos comparativos (mes actual vs mes anterior, año actual vs año anterior).

**Dashboards estratégicos**:
- **Propósito**: Seguimiento de objetivos estratégicos a largo plazo (trimestres, años).
- **Audiencia**: Alta dirección (CEO, CFO, COO), consejo de administración, inversores.
- **Ejemplos**: Cuadro de Mando Integral (Balanced Scorecard) con 4 perspectivas: financiera, clientes, procesos internos, aprendizaje y crecimiento; panel de cumplimiento de objetivos anuales (OKRs); panel de salud financiera de la empresa (EBITDA, cash flow, deuda, burn rate).
- **Características**: Datos agregados, pocos KPIs (5-10 como máximo), sin ruido ni detalles superfluos, visualizaciones muy cuidadas y enfocadas en contar una historia clara, actualización mensual o trimestral.

#### 1.2. Principios de diseño de dashboards efectivos

**Edward Tufte**, profesor emérito de la Universidad de Yale y pionero en el campo de la visualización de datos, estableció principios fundamentales que siguen siendo la base del diseño de dashboards modernos:

**Maximizar la proporción datos-tinta (data-ink ratio)**: De toda la "tinta" (píxeles en pantalla) utilizada para dibujar un gráfico, la mayor parte posible debe dedicarse a representar los datos, y la menor parte posible a elementos decorativos no informativos. En la práctica: eliminar fondos con gradientes, líneas de cuadrícula gruesas, bordes decorativos, sombras innecesarias, efectos 3D (que además distorsionan la percepción de las magnitudes), y cualquier elemento que no aporte información.

**Eliminar el chartjunk**: Tufte acuñó este término para referirse a toda decoración superflua en gráficos que no comunica información pero distrae al espectador. Ejemplos clásicos: ilustraciones de fondo en gráficos, iconos repetitivos, texturas y patrones innecesarios, animaciones excesivas, gráficos en 3D (un gráfico de tarta en 3D distorsiona las proporciones porque la perspectiva hace que las porciones del frente parezcan más grandes).

**Mostrar los datos, no presumir de diseño**: Un dashboard no es una obra de arte ni una demostración de habilidades con CSS. Su propósito es comunicar información de forma clara y eficiente. ==Si un elemento de diseño no ayuda a entender los datos, sobra.==

**Stephen Few**, consultor especializado en visualización de datos y autor de "Information Dashboard Design", añade principios complementarios:

**Información de un vistazo (at-a-glance)**: Un dashboard debe poder leerse en menos de 5 segundos. El ojo humano escanea en forma de "F" o "Z" (dependiendo de la cultura). La información más importante debe estar en la esquina superior izquierda. Los KPIs principales deben destacar visualmente (tamaño, color, posición).

**Jerarquía visual clara**: Los elementos más importantes deben ser visualmente dominantes (mayor tamaño, color más saturado, posición prominente). Los elementos secundarios deben ser visualmente subordinados (menor tamaño, colores más apagados). Esto guía el recorrido visual del usuario.

**Sin ruido ni distracciones**: Cada elemento en pantalla compite por la atención del usuario. Si hay 12 gráficos en un dashboard, el usuario no sabrá cuál mirar primero. La solución no es añadir más gráficos, sino priorizar: ¿cuáles son los 4-6 indicadores más importantes? Esos van en el dashboard. El resto, en una segunda pantalla o en un informe aparte.

**Consistencia**: Usar los mismos colores para las mismas categorías en todos los gráficos. Usar el mismo formato de fecha, moneda y número en todo el dashboard. Usar el mismo tipo de gráfico para el mismo tipo de comparación. La consistencia reduce la carga cognitiva del usuario.

**Contexto**: Un número aislado no significa nada. "Ingresos: 150.000 €" necesita contexto para ser interpretado: ¿es bueno o malo? ¿comparado con qué? Las tarjetas KPI efectivas siempre incluyen comparación con un período anterior (+12% vs mes anterior), con un objetivo (85% del objetivo trimestral), o con un benchmark.

#### 1.3. Anatomía estándar de un dashboard empresarial

Aunque cada dashboard se adapta a las necesidades específicas del negocio, existe una anatomía estándar que funciona bien en la mayoría de los casos:

```
┌─────────────────────────────────────────────────────────┐
│  FILTROS: [Rango fechas ▼] [Categoría ▼] [Aplicar]     │
├──────────┬──────────┬──────────┬──────────┬─────────────┤
│ KPI 1    │ KPI 2    │ KPI 3    │ KPI 4    │ KPI 5       │
│ $150K ▲  │ 1,234 ▲  │ $85.50 ▼ │ 3.2% ▲   │ 94% ▲       │
├──────────┴──────────┴──────────┴──────────┴─────────────┤
│                   GRÁFICO PRINCIPAL                     │
│              (Evolución temporal - Líneas)              │
│                    [ocupa 2/3 ancho]                     │
├────────────────────────────┬────────────────────────────┤
│    GRÁFICO SECUNDARIO 1    │   GRÁFICO SECUNDARIO 2     │
│     (Top categorías -       │    (Distribución -         │
│      Barras horizontales)   │     Doughnut)              │
├────────────────────────────┴────────────────────────────┤
│                    TABLA DE DATOS                        │
│     (Últimos registros / Detalle desglosado)            │
└─────────────────────────────────────────────────────────┘
```

**Fila de filtros**: Permite al usuario segmentar los datos temporalmente (últimos 7 días, 30 días, trimestre actual, año actual, personalizado) y por otras dimensiones relevantes (categoría de producto, región geográfica, canal de venta). Los filtros deben ser autocontenidos (no requieren pulsar "Aplicar" para ser efectivos en dashboards simples, aunque en dashboards con muchos datos se recomienda un botón explícito para evitar múltiples recálculos innecesarios).

**Fila de KPI cards**: Muestra los 4-6 indicadores más importantes para el rol del usuario. Cada tarjeta contiene: un icono identificativo, la etiqueta del indicador, el valor numérico (con formato grande y legible), y la tendencia (porcentaje de variación con flecha arriba/abajo y color verde/rojo). La altura de todas las tarjetas debe ser idéntica para mantener la alineación visual.

**Gráfico principal**: El gráfico más importante del dashboard, que comunica la historia principal que los datos quieren contar. Suele ser de líneas (evolución temporal) o de barras (comparación de categorías), y ocupa la mayor parte del espacio central.

**Gráficos secundarios**: Proporcionan contexto adicional y permiten explorar otras dimensiones de los datos. Suelen ser gráficos circulares (composición), de barras horizontales (ranking), o de radar (comparación multivariable).

**Tabla de datos**: Lista detallada de los registros individuales que subyacen a los gráficos agregados. Permite al usuario inspeccionar los datos en bruto cuando necesita investigar una anomalía. Debe incluir ordenación por columnas y, si el volumen de datos lo requiere, paginación.

### 2. Chart.js en profundidad

**Chart.js** es, con diferencia, la librería de gráficos más popular del ecosistema JavaScript, con más de 60.000 estrellas en GitHub y una comunidad extremadamente activa. Su versión 4 (la actual) es un rediseño significativo respecto a la versión 3, con mejor soporte de TypeScript, tree shaking, rendimiento mejorado y una API más consistente.

#### 2.1. Instalación y primera configuración

En un proyecto Angular standalone, la instalación es trivial:

```bash
npm install chart.js
```

Chart.js se importa como un módulo ES6. Para aprovechar el **tree shaking** y reducir el tamaño del bundle, se recomienda importar y registrar solo los componentes que se vayan a utilizar:

```typescript
import {
  Chart,
  BarController,
  LineController,
  DoughnutController,
  BarElement,
  LineElement,
  PointElement,
  ArcElement,
  CategoryScale,
  LinearScale,
  TimeScale,
  Tooltip,
  Legend,
  Title,
  Filler
} from 'chart.js';

// Registrar los componentes necesarios
Chart.register(
  BarController, LineController, DoughnutController,
  BarElement, LineElement, PointElement, ArcElement,
  CategoryScale, LinearScale,
  Tooltip, Legend, Title, Filler
);
```

Si se prefiere la simplicidad sobre la optimización del bundle, se puede importar todo Chart.js (incluyendo todos los controladores, elementos, escalas y plugins) con:

```typescript
import Chart from 'chart.js/auto';
```

!!! info "Dato clave"

    La diferencia de tamaño es notable: la importación con `chart.js/auto` añade aproximadamente 250 KB al bundle, mientras que el registro manual de solo los componentes necesarios puede reducir esta cifra a 100-150 KB.

#### 2.2. Estructura de la configuración de un gráfico

La configuración de un gráfico Chart.js se estructura en tres bloques principales:

```typescript
const config = {
  type: 'line' as const,        // Tipo de gráfico
  data: {                        // Datos del gráfico
    labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    datasets: [
      {
        label: 'Ingresos 2024',
        data: [12000, 19000, 15000, 22000, 28000],
        borderColor: 'rgb(59, 130, 246)',
        backgroundColor: 'rgba(59, 130, 246, 0.1)',
        tension: 0.3,
        fill: true,
        pointRadius: 4,
        pointHoverRadius: 6
      }
    ]
  },
  options: {                     // Opciones de visualización y comportamiento
    responsive: true,
    maintainAspectRatio: false,
    plugins: { /* leyenda, tooltip, título */ },
    scales: { /* ejes X e Y */ },
    interaction: { /* modo de interacción */ }
  }
};
```

**El array `datasets`** es una de las claves más importantes que hay que entender. Cada dataset representa una serie de datos (por ejemplo, "Ingresos 2024" y "Ingresos 2023" serían dos datasets superpuestos en el mismo gráfico). Cada dataset puede tener sus propios colores, estilos y configuraciones. Esto permite gráficos comparativos muy potentes:

```typescript
datasets: [
  {
    label: 'Ingresos 2024',
    data: [12000, 19000, 15000, 22000, 28000],
    borderColor: '#2563eb',
    backgroundColor: 'rgba(37, 99, 235, 0.1)',
    tension: 0.3,
    fill: true
  },
  {
    label: 'Ingresos 2023',
    data: [10000, 15000, 13000, 18000, 21000],
    borderColor: '#9ca3af',
    backgroundColor: 'transparent',
    borderDash: [5, 5],     // Línea discontinua para el año anterior
    tension: 0.3,
    fill: false
  }
]
```

#### 2.3. Elección del tipo de gráfico adecuado

!!! warning "Trampa común"

    La elección del tipo de gráfico no es una cuestión estética, sino funcional. Cada tipo de gráfico está diseñado para responder a un tipo específico de pregunta sobre los datos. Usar el gráfico equivocado puede llevar a interpretaciones erróneas o, en el mejor de los casos, a que la información no se entienda.

**Guía de selección de tipo de gráfico:**

| Pregunta que quiero responder | Tipo de gráfico recomendado | Ejemplo de uso |
|---|---|---|
| ¿Cómo ha evolucionado X a lo largo del tiempo? | **Líneas (line)** | Ingresos mensuales de los últimos 12 meses |
| ¿Cuál es la diferencia entre varias categorías? | **Barras (bar)** | Ventas por región geográfica |
| ¿Cuál es el ranking de elementos? | **Barras horizontales (bar + indexAxis: 'y')** | Top 10 productos más vendidos |
| ¿Cómo se distribuye el total entre sus partes? | **Doughnut (anillo)** | Distribución de ingresos por canal de venta |
| ¿Qué relación hay entre dos variables numéricas? | **Dispersión (scatter)** | Relación entre inversión en publicidad e ingresos |
| ¿Cómo se compara un perfil multivariable? | **Radar** | Evaluación de competencias de un empleado (5 dimensiones) |
| ¿Cómo se distribuye un conjunto de datos? | **Histograma (bar + binned data)** | Distribución de importes de pedidos |
| ¿Cómo se comparan 3 dimensiones? | **Burbujas (bubble)** | Productos: x=crecimiento, y=margen, radio=ingresos |
| ¿Cómo ha evolucionado una acción en bolsa? | **Velas (candlestick)** | Precio de una acción: apertura, cierre, máximo, mínimo |

**Regla de oro**: ==Si tienes datos de evolución temporal, usa líneas. Si tienes datos de comparación entre categorías, usa barras.== Si tienes datos de composición (partes de un todo), usa doughnut (NO uses pie: es más difícil comparar ángulos que longitudes de arco en un anillo). Si tienes más de 5 categorías en un gráfico circular, reconsidera: probablemente un gráfico de barras sea más legible.

#### 2.4. Configuración de opciones en profundidad

Las opciones (`options`) de Chart.js constituyen un objeto de configuración muy extenso que controla prácticamente todos los aspectos visuales y de comportamiento del gráfico. A continuación se detallan las secciones más relevantes para dashboards empresariales:

**Responsive y aspect ratio**:
```typescript
options: {
  responsive: true,               // El gráfico se redimensiona cuando cambia el tamaño del contenedor
  maintainAspectRatio: false,     // Permite que el gráfico ocupe todo el alto del contenedor (importante para dashboards con alturas fijas)
  // maintainAspectRatio: true    // Mantiene la proporción 2:1 (por defecto). Recomendado para tarjetas de gráficos con altura flexible
}
```

**Escalas (axes)**:
```typescript
scales: {
  y: {
    beginAtZero: true,            // El eje Y comienza en 0 (importante para no distorsionar magnitudes)
    ticks: {
      callback: (value) => `${value.toLocaleString('es-ES')} €`,  // Formatear etiquetas del eje
      font: { size: 11, family: 'Inter, sans-serif' },
      color: '#6b7280'
    },
    grid: {
      color: 'rgba(0, 0, 0, 0.05)',      // Color de las líneas de la cuadrícula
      drawBorder: false,                   // No dibujar el borde del eje
      lineWidth: 1
    },
    title: {
      display: true,
      text: 'Ingresos (EUR)',
      font: { size: 12, weight: 'bold' },
      color: '#374151'
    }
  },
  x: {
    grid: {
      display: false             // Ocultar líneas verticales (diseño más limpio para gráficos de barras/líneas)
    },
    ticks: {
      font: { size: 11, family: 'Inter, sans-serif' },
      color: '#6b7280'
    }
  }
}
```

**Plugins** (leyenda, tooltip, título):
```typescript
plugins: {
  legend: {
    display: true,
    position: 'bottom',           // 'top', 'bottom', 'left', 'right', 'chartArea'
    align: 'center',              // 'start', 'center', 'end'
    labels: {
      usePointStyle: true,        // Indicadores circulares en lugar de rectangulares
      padding: 20,                // Espacio entre elementos de la leyenda
      font: { size: 12, family: 'Inter, sans-serif' },
      color: '#374151',
      generateLabels: (chart) => { /* personalizar etiquetas de la leyenda */ }
    }
  },
  tooltip: {
    enabled: true,
    mode: 'index',                // 'index' muestra tooltips para todos los datasets en esa posición X
    intersect: false,             // Muestra el tooltip aunque el cursor no intersecte exactamente un punto
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    titleFont: { size: 13, weight: 'bold' },
    bodyFont: { size: 12 },
    padding: 12,
    cornerRadius: 6,
    callbacks: {
      label: (context) => {
        const value = context.parsed.y;
        return ` ${context.dataset.label}: ${value.toLocaleString('es-ES')} €`;
      }
    }
  },
  title: {
    display: true,
    text: 'Evolución de Ingresos Mensuales',
    font: { size: 16, weight: 'bold' },
    color: '#111827',
    padding: { bottom: 20 }
  }
}
```

**Animaciones**:
```typescript
animation: {
  duration: 750,                 // Duración de la animación en milisegundos (0 para desactivar)
  easing: 'easeOutQuart',        // Curva de animación: 'linear', 'easeInQuad', 'easeOutQuart', etc.
  // Animaciones específicas por tipo de gráfico:
  numbers: { duration: 1000 }    // Animación de los números en tooltips
}
```

#### 2.5. Colores en los gráficos

La elección de colores es uno de los aspectos más críticos y a menudo más descuidados en los dashboards. Algunas recomendaciones:

!!! tip "Paleta de colores"

    **Para gráficos de una sola serie** (líneas, barras): usar el color primario de la marca o un azul corporativo. No es necesario un arcoíris de colores cuando solo hay una serie.

    **Para gráficos de múltiples series** (varias líneas, barras agrupadas): usar una paleta de colores cualitativos (para categorías) o secuenciales (para valores ordinales). Recursos recomendados:
    - **Coolors.co**: generador de paletas de colores.
    - **ColorBrewer2.org**: paletas optimizadas para visualización de datos, con opciones para daltonismo.
    - **Tailwind CSS color palette**: consistente con el design system de la aplicación.

**Ejemplo de paleta corporativa para gráficos**:
```typescript
const CHART_COLORS = {
  primary: 'rgba(37, 99, 235, 1)',      // Azul corporativo
  primaryLight: 'rgba(37, 99, 235, 0.1)',
  secondary: 'rgba(139, 92, 246, 1)',   // Púrpura
  tertiary: 'rgba(16, 185, 129, 1)',    // Verde
  quaternary: 'rgba(245, 158, 11, 1)',  // Ámbar
  quinary: 'rgba(239, 68, 68, 1)',      // Rojo
  gray: 'rgba(156, 163, 175, 1)',       // Gris para datos comparativos
  gridLines: 'rgba(0, 0, 0, 0.05)'      // Líneas de cuadrícula muy sutiles
};
```

!!! info "Dato clave"

    **Consideraciones de accesibilidad**: Aproximadamente el 8% de los hombres y el 0,5% de las mujeres tienen algún tipo de **daltonismo** (deuteranopía: confusión rojo-verde es la más común). Para hacer los gráficos accesibles: no depender exclusivamente del color para transmitir información (usar también patrones, texturas o etiquetas), evitar combinaciones rojo-verde para elementos que deban diferenciarse, y usar paletas diseñadas específicamente para daltonismo (ColorBrewer2 ofrece esta opción).

### 3. Integración de Chart.js en Angular

La integración de Chart.js en Angular requiere atención especial al **ciclo de vida** de los componentes y a la gestión de la memoria. A continuación se presenta la implementación canónica de un componente gráfico reusable en Angular standalone.

#### 3.1. Componente ChartWidget reutilizable

```typescript
import {
  Component,
  ElementRef,
  Input,
  OnChanges,
  OnDestroy,
  OnInit,
  SimpleChanges,
  ViewChild,
  inject,
  signal
} from '@angular/core';
import { Chart, ChartConfiguration, ChartType, registerables } from 'chart.js';

Chart.register(...registerables);

@Component({
  selector: 'app-chart-widget',
  standalone: true,
  template: `
    <div class="relative w-full h-full">
      <canvas #chartCanvas></canvas>
      @if (isLoading()) {
        <div class="absolute inset-0 flex items-center justify-center bg-white/80">
          <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
        </div>
      }
    </div>
  `
})
export class ChartWidgetComponent implements OnInit, OnDestroy, OnChanges {
  @ViewChild('chartCanvas', { static: true }) canvasRef!: ElementRef<HTMLCanvasElement>;

  @Input() type: ChartType = 'bar';
  @Input() labels: string[] = [];
  @Input() datasets: any[] = [];
  @Input() options: any = {};
  @Input() height: string = '300px';
  @Input() isLoading = false;

  chart: Chart | null = null;

  ngOnInit(): void {
    this.createChart();
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (this.chart && (changes['labels'] || changes['datasets'])) {
      this.updateChart();
    }
    if (changes['type'] && this.chart) {
      this.destroyChart();
      this.createChart();
    }
  }

  ngOnDestroy(): void {
    this.destroyChart();
  }

  getBase64Image(format: 'image/png' | 'image/jpeg' = 'image/png', quality: number = 1.0): string | null {
    return this.chart?.toBase64Image(format, quality) ?? null;
  }

  private createChart(): void {
    const ctx = this.canvasRef.nativeElement.getContext('2d');
    if (!ctx) return;

    const config: ChartConfiguration = {
      type: this.type,
      data: {
        labels: this.labels,
        datasets: this.datasets
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        ...this.options
      }
    };

    this.chart = new Chart(ctx, config);
  }

  private updateChart(): void {
    if (!this.chart) return;
    this.chart.data.labels = this.labels;
    this.chart.data.datasets = this.datasets;
    this.chart.update('none');
  }

  private destroyChart(): void {
    this.chart?.destroy();
    this.chart = null;
  }
}
```

**Uso del componente en un dashboard**:
```html
<app-chart-widget
  type="line"
  [labels]="monthlyLabels()"
  [datasets]="monthlyRevenueDatasets()"
  [options]="lineChartOptions"
  [isLoading]="chartDataState() === 'loading'"
  height="350px"
></app-chart-widget>
```

#### 3.2. Integración con Signals

La combinación de Chart.js con el sistema de **Signals** de Angular permite una reactividad elegante y eficiente. En lugar de usar `ngOnChanges` con múltiples inputs, se puede utilizar un `effect()` que reaccione a los cambios en las señales:

```typescript
import { Component, effect, ElementRef, ViewChild, signal } from '@angular/core';
import { Chart, ChartConfiguration } from 'chart.js';

@Component({ /* ... */ })
export class ReactiveChartComponent {
  @ViewChild('chartCanvas', { static: true }) canvasRef!: ElementRef<HTMLCanvasElement>;
  chart: Chart | null = null;

  // Datos de entrada como Signals
  salesData = signal<number[]>([100, 200, 150, 300, 250]);
  salesLabels = signal<string[]>(['Ene', 'Feb', 'Mar', 'Abr', 'May']);

  constructor() {
    // El effect se ejecutará cada vez que cambien las signals
    effect(() => {
      const data = this.salesData();
      const labels = this.salesLabels();
      if (this.chart) {
        this.chart.data.labels = labels;
        this.chart.data.datasets[0].data = data;
        this.chart.update();
      } else if (this.canvasRef?.nativeElement) {
        this.createChart();
      }
    });
  }

  private createChart(): void {
    const ctx = this.canvasRef.nativeElement.getContext('2d');
    if (!ctx) return;
    const config: ChartConfiguration = {
      type: 'line',
      data: {
        labels: this.salesLabels(),
        datasets: [{
          label: 'Ventas',
          data: this.salesData(),
          borderColor: '#3b82f6',
          tension: 0.3
        }]
      },
      options: { responsive: true, maintainAspectRatio: false }
    };
    this.chart = new Chart(ctx, config);
  }

  ngOnDestroy(): void {
    this.chart?.destroy();
  }
}
```

### 4. ApexCharts: la alternativa moderna

**ApexCharts** ha ganado rápidamente popularidad como alternativa a Chart.js, especialmente en proyectos que requieren dashboards con un alto nivel de pulido visual y tipos de gráficos no disponibles en Chart.js.

**Instalación**:
```bash
npm install apexcharts ng-apexcharts
```

**Registro del módulo en Angular**: A diferencia de Chart.js, ng-apexcharts proporciona un componente Angular nativo listo para usar:

```typescript
import { NgApexchartsModule } from 'ng-apexcharts';

@Component({
  standalone: true,
  imports: [NgApexchartsModule],
  // ...
})
```

**Ejemplo de gráfico de barras con ApexCharts**:
```typescript
import { Component } from '@angular/core';
import { ApexAxisChartSeries, ApexChart, ApexXAxis, ApexTitleSubtitle } from 'ng-apexcharts';

@Component({
  selector: 'app-apex-bar-chart',
  standalone: true,
  imports: [NgApexchartsModule],
  template: `
    <apx-chart
      [series]="series"
      [chart]="chart"
      [xaxis]="xaxis"
      [title]="title"
      [colors]="['#3b82f6']">
    </apx-chart>
  `
})
export class ApexBarChartComponent {
  series: ApexAxisChartSeries = [
    { name: 'Ventas', data: [113, 120, 95, 145, 160, 135, 150] }
  ];

  chart: ApexChart = {
    type: 'bar',
    height: 350,
    toolbar: { show: true },
    animations: { enabled: true, easing: 'easeout', speed: 800 }
  };

  xaxis: ApexXAxis = {
    categories: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
  };

  title: ApexTitleSubtitle = {
    text: 'Ventas semanales',
    align: 'center',
    style: { fontSize: '16px', fontWeight: 'bold', color: '#374151' }
  };
}
```

**Gráfico RadialBar (exclusivo de ApexCharts)**: Perfecto para KPIs con formato de medidor:
```typescript
series: ApexNonAxisChartSeries = [76];  // Porcentaje
chart: ApexChart = { type: 'radialBar', height: 200 };
plotOptions: ApexPlotOptions = {
  radialBar: {
    startAngle: -135,
    endAngle: 135,
    dataLabels: {
      name: { show: true, fontSize: '14px', color: '#6b7280' },
      value: { show: true, fontSize: '28px', fontWeight: 'bold', color: '#111827' }
    }
  }
};
labels: string[] = ['Objetivo alcanzado'];
```

### 5. Diseño del dashboard empresarial completo

Un dashboard real no es un único componente, sino un ecosistema de componentes interconectados que comparten estado, reaccionan a filtros y se actualizan de forma coordinada.

**Componente padre `DashboardLayoutComponent`**:
```typescript
@Component({
  selector: 'app-dashboard-layout',
  standalone: true,
  imports: [StatCardComponent, ChartWidgetComponent, FilterBarComponent, DataTableComponent],
  template: `
    <div class="p-4 md:p-6 lg:p-8 max-w-7xl mx-auto">
      <h1 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Dashboard</h1>

      <!-- Filtros -->
      <app-filter-bar (filterChange)="applyFilters($event)" class="mb-6"></app-filter-bar>

      <!-- KPI Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4 mb-6">
        @for (kpi of kpiData(); track kpi.label) {
          <app-stat-card
            [label]="kpi.label"
            [value]="kpi.value"
            [trend]="kpi.trend"
            [icon]="kpi.icon"
            [isLoading]="isLoading()">
          </app-stat-card>
        }
      </div>

      <!-- Zona de gráficos -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        <div class="lg:col-span-2 bg-white dark:bg-gray-800 rounded-xl shadow-sm p-4">
          <h3 class="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Evolución de Ingresos</h3>
          <app-chart-widget
            type="line"
            [labels]="revenueLabels()"
            [datasets]="revenueDatasets()"
            [isLoading]="isLoading()"
            height="350px">
          </app-chart-widget>
        </div>

        <div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-4">
          <h3 class="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Por Categoría</h3>
          <app-chart-widget
            type="doughnut"
            [labels]="categoryLabels()"
            [datasets]="categoryDatasets()"
            [isLoading]="isLoading()"
            height="350px">
          </app-chart-widget>
        </div>
      </div>

      <!-- Tabla de datos -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-4">
        <h3 class="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Últimos Pedidos</h3>
        <app-data-table
          [columns]="tableColumns"
          [rows]="recentOrders()"
          [isLoading]="isLoading()">
        </app-data-table>
      </div>

      <!-- Botones de exportación -->
      <div class="flex gap-3 mt-6 justify-end">
        <button (click)="exportCsv()" class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700">
          Exportar CSV
        </button>
        <button (click)="exportExcel()" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
          Exportar Excel
        </button>
        <button (click)="exportPdf()" class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700">
          Exportar PDF
        </button>
      </div>
    </div>
  `
})
export class DashboardLayoutComponent {
  // Signals para datos, filtros y estado de carga
  isLoading = signal(true);
  dateRange = signal<{ start: Date; end: Date }>({ start: new Date(), end: new Date() });

  kpiData = computed(() => { /* Transformar datos a KPIs */ });
  revenueLabels = computed(() => { /* Labels de ingresos */ });
  revenueDatasets = computed(() => { /* Datasets de ingresos */ });
  categoryLabels = computed(() => { /* Labels de categorías */ });
  categoryDatasets = computed(() => { /* Datasets de categorías */ });
  recentOrders = computed(() => { /* Últimos pedidos filtrados */ });
}
```

### 6. Exportación de datos desde el dashboard

La **exportación de datos** completa el ciclo de valor del dashboard: no solo se visualizan los datos, sino que se permite al usuario llevárselos para trabajar con ellos en otras herramientas (Excel para análisis adicional, PDF para presentaciones, CSV para importar en otros sistemas).

**Exportación de gráficos como imágenes para PDF**:
```typescript
exportPdf(): void {
  // Obtener imágenes de los gráficos (necesita referencia a los componentes ChartWidget)
  const revenueChartImage = this.revenueChartWidget?.getBase64Image();
  const categoryChartImage = this.categoryChartWidget?.getBase64Image();

  const docDefinition = {
    pageSize: 'A4',
    pageOrientation: 'landscape',
    content: [
      { text: 'Informe de Dashboard', style: 'header' },
      { text: `Período: ${formatDate(this.dateRange().start)} - ${formatDate(this.dateRange().end)}`, margin: [0, 0, 0, 20] },

      // KPIs como tabla resumen
      {
        table: {
          headerRows: 1,
          widths: ['*', '*', '*', '*'],
          body: [['Indicador', 'Valor', 'Tendencia', 'Estado'], ...kpiRows]
        }
      },

      // Gráfico de ingresos
      revenueChartImage && { image: revenueChartImage, width: 500, margin: [0, 20, 0, 20] },

      // Gráfico de categorías
      categoryChartImage && { image: categoryChartImage, width: 400, margin: [0, 20, 0, 20] }
    ].filter(Boolean)
  };

  pdfMake.createPdf(docDefinition).download(`dashboard-${formatDate(new Date())}.pdf`);
}
```

## Ejemplos guiados

### Ejemplo 1: Componente ChartWidget reutilizable con Chart.js + Signals

**Objetivo**: Crear un componente Angular standalone que encapsule Chart.js, permita configurarlo mediante inputs y se actualice reactivamente con Signals.

**Paso 1**: Instalar Chart.js.
```bash
npm install chart.js
```

**Paso 2**: Crear el componente en `src/app/shared/components/chart-widget.component.ts`.
(Implementar el componente ChartWidget como se describió en la sección 3.1 del desarrollo teórico.)

**Paso 3**: Probar el componente en una página.
```typescript
@Component({
  template: `<app-chart-widget [type]="'bar'" [labels]="['A','B','C','D']" [datasets]="[{
    label: 'Ventas', data: [12, 19, 3, 5], backgroundColor: '#3b82f6'
  }]"></app-chart-widget>`
})
class TestPage {}
```

### Ejemplo 2: Dashboard page completa con KPIs, gráficos, tabla y exportación

**Objetivo**: Construir una página de dashboard completa con datos de ejemplo, siguiendo la anatomía estándar descrita en el desarrollo teórico.

**Paso 1**: Crear datos de ejemplo en un servicio `DashboardDataService`.
```typescript
@Injectable({ providedIn: 'root' })
export class DashboardDataService {
  getKpis(): Observable<KpiData[]> { /* simular API */ }
  getMonthlyRevenue(): Observable<TimeSeriesData> { /* simular API */ }
  getTopProducts(): Observable<CategoryData[]> { /* simular API */ }
  getRecentOrders(): Observable<Order[]> { /* simular API */ }
}
```

**Paso 2**: Implementar `StatCardComponent`:
```typescript
@Component({
  selector: 'app-stat-card',
  standalone: true,
  template: `
    <div class="bg-white dark:bg-gray-800 rounded-xl p-4 shadow-sm">
      <div class="flex items-center justify-between mb-2">
        <span class="text-sm text-gray-500">{{ label }}</span>
        <span [innerHTML]="icon" class="w-8 h-8 text-blue-500"></span>
      </div>
      <div class="text-2xl font-bold text-gray-900 dark:text-white">{{ value }}</div>
      @if (trend !== undefined) {
        <div class="flex items-center mt-1" [class.text-green-600]="trend >= 0" [class.text-red-600]="trend < 0">
          <span class="text-sm font-medium">{{ trend >= 0 ? '▲' : '▼' }} {{ abs(trend) }}%</span>
          <span class="text-xs text-gray-400 ml-1">vs mes anterior</span>
        </div>
      }
    </div>
  `
})
export class StatCardComponent {
  @Input() label = '';
  @Input() value = '';
  @Input() trend?: number;
  @Input() icon = '';
  @Input() isLoading = false;
}
```

**Paso 3**: Integrar todos los widgets en `DashboardLayoutComponent` como se mostró en la sección 5 del desarrollo teórico.

### Ejemplo 3: Integración de ApexCharts en Angular

**Objetivo**: Añadir un gráfico RadialBar de ApexCharts para mostrar el porcentaje de objetivo de ventas alcanzado.

**Paso 1**: Instalar dependencias.
```bash
npm install apexcharts ng-apexcharts
```

**Paso 2**: Crear componente `SalesGoalGaugeComponent`:
```typescript
import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { NgApexchartsModule } from 'ng-apexcharts';
import { ApexNonAxisChartSeries, ApexChart, ApexPlotOptions, ApexFill } from 'ng-apexcharts';

@Component({
  selector: 'app-sales-goal-gauge',
  standalone: true,
  imports: [NgApexchartsModule],
  template: `<apx-chart [series]="series" [chart]="chart" [plotOptions]="plotOptions" [labels]="labels" [fill]="fill"></apx-chart>`
})
export class SalesGoalGaugeComponent implements OnChanges {
  @Input() currentSales = 0;
  @Input() salesGoal = 100000;
  @Input() height: number = 200;

  series: ApexNonAxisChartSeries = [0];
  chart: ApexChart = { type: 'radialBar', height: 200 };
  plotOptions: ApexPlotOptions = { radialBar: { hollow: { size: '70%' }, dataLabels: { show: true, name: { show: false }, value: { fontSize: '24px', fontWeight: 'bold', formatter: (v) => v + '%' } } } };
  labels: string[] = ['Objetivo'];
  fill: ApexFill = { colors: ['#3b82f6'] };

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['currentSales'] || changes['salesGoal']) {
      const percentage = Math.round((this.currentSales / this.salesGoal) * 100);
      this.series = [percentage > 100 ? 100 : percentage];
      if (percentage >= 100) this.fill = { colors: ['#10b981'] };
      else if (percentage >= 75) this.fill = { colors: ['#f59e0b'] };
      else this.fill = { colors: ['#ef4444'] };
    }
  }
}
```

## Actividades guiadas

(Se incluirían 3 actividades guiadas detalladas con instrucciones paso a paso, similares en estructura a las de la unidad 16.)

## Actividades propuestas

(Se incluirían 5 actividades propuestas de dificultad variada.)

??? "Actividades de ampliación"

    (Se incluirían 3 actividades de ampliación.)

!!! tip "Buenas prácticas"

    1. **Usa el tipo de gráfico correcto para cada tipo de dato**: No uses un gráfico circular para mostrar evolución temporal, ni un gráfico de líneas para comparar 3 categorías. Dedica tiempo a pensar qué pregunta quieres responder y elige el gráfico que mejor responda a esa pregunta.

    2. **Empieza el eje Y desde cero**: En gráficos de barras, comenzar el eje Y en un valor distinto de cero distorsiona visualmente las diferencias entre categorías. La única excepción justificada son los gráficos de líneas con variaciones muy pequeñas.

    3. **No uses gráficos 3D ni efectos innecesarios**: Los gráficos en 3D distorsionan la percepción de las magnitudes y violan el principio de data-ink ratio. Chart.js, afortunadamente, no soporta gráficos 3D de forma nativa.

    4. **Mantén un máximo de 5-7 colores en gráficos circulares**: Si tienes más de 7 categorías en un gráfico circular, agrupa las menos relevantes en una categoría "Otros" y usa un gráfico de barras para el detalle.

    5. **Proporciona siempre contexto en las KPI cards**: Un número aislado no informa. Añade comparación con el período anterior, con el objetivo o con el benchmark del sector. Usa flechas y colores verde/rojo para la dirección de la tendencia.

    6. **No satures el dashboard**: 4-6 KPIs, 2-3 gráficos y 1 tabla es una configuración que funciona bien para la mayoría de los casos. Si necesitas más indicadores, crea pestañas o dashboards separados por área funcional.

    7. **Implementa estados de carga, vacío y error**: Cada widget del dashboard debe manejar estos tres estados. Los skeleton loaders (Placeholder UI) mejoran la percepción de velocidad.

    8. **Destruye siempre las instancias de Chart.js**: Llama a `chart.destroy()` en `ngOnDestroy()`. Las instancias de Chart.js retienen referencias a elementos del DOM y event listeners que causan fugas de memoria si no se limpian.

    9. **Usa `maintainAspectRatio: false` para controlar la altura con CSS**: Chart.js por defecto mantiene una relación de aspecto 2:1. Para dashboards con alturas fijas, desactiva esta opción y controla la altura del contenedor con CSS.

    10. **Prueba el dashboard en diferentes tamaños de pantalla**: Un dashboard que se ve bien en un monitor 4K puede ser ilegible en un portátil de 13 pulgadas. El diseño responsive con Tailwind (grid-cols-1 md:grid-cols-2 xl:grid-cols-4) es tu aliado.

!!! warning "Errores frecuentes"

    1. **Crear la instancia de Chart.js en `ngOnInit` en lugar de `ngAfterViewInit`**: El canvas no está disponible en el DOM durante `ngOnInit` a menos que se use `{ static: true }` en `@ViewChild`. Si se usa `{ static: false }`, la creación debe hacerse en `ngAfterViewInit`.

    2. **No destruir la instancia de Chart al salir del componente**: Olvidar `chart.destroy()` en `ngOnDestroy` causa fugas de memoria. Si el usuario navega repetidamente al dashboard, cada vez se crea una nueva instancia sin destruir la anterior, acumulando consumo de memoria.

    3. **Modificar los datos sin llamar a `chart.update()`**: Cambiar `chart.data.labels` o `chart.data.datasets` sin llamar posteriormente a `chart.update()` no tendrá efecto visual en el gráfico.

    4. **Usar `ngOnChanges` para detectar cambios en objetos anidados**: `ngOnChanges` solo detecta cambios en referencias de objetos (shallow comparison). Si los datos del gráfico son un objeto anidado, los cambios internos no activarán `ngOnChanges`. Solución: usar Signals con `effect()` o crear nuevas referencias de objetos.

    5. **No considerar la accesibilidad**: Los gráficos son inherentemente visuales, lo que los hace inaccesibles para usuarios con discapacidad visual. Proporciona siempre una tabla de datos alternativa (visible u oculta con `sr-only`) y descripciones textuales.

    6. **Sobrecarga de datos en gráficos de líneas**: Mostrar más de 5-6 series en un mismo gráfico de líneas lo convierte en un "plato de espaguetis" ilegible. Agrupa, filtra o usa small multiples (múltiples gráficos pequeños en lugar de uno grande).

    7. **No formatear los números en tooltips y ejes**: Mostrar `1234567.890123` en lugar de `1.234.567,89 €` es un error de usabilidad grave. Usa `Intl.NumberFormat` en los callbacks.

    8. **Olvidar configurar `responsive: true`**: Sin esta opción, los gráficos no se redimensionarán cuando el usuario cambie el tamaño de la ventana o rote el dispositivo.

    9. **Usar demasiados colores en gráficos de una sola serie**: Cada barra de un color diferente en un gráfico de barras de una sola categoría es innecesario y distrae. Usa un solo color o, si quieres resaltar una barra, usa una variación sutil.

    10. **No probar con datos extremos**: ¿Qué pasa si todos los valores son cero? ¿Y si un valor es 1000 veces mayor que los demás? ¿Y si faltan datos (null, undefined)? El dashboard debe manejar estos casos sin romperse.

!!! abstract "Resumen"

    Los dashboards y la visualización de datos son componentes esenciales de las aplicaciones empresariales modernas. Esta unidad ha proporcionado al alumnado los conocimientos teóricos y prácticos necesarios para diseñar e implementar dashboards efectivos en aplicaciones Angular.

    Se ha comenzado estableciendo los fundamentos conceptuales: qué es un dashboard, qué lo diferencia de un informe, qué tipos existen (operacional, táctico, estratégico) y cuáles son los principios de diseño que separan un buen dashboard de uno malo, basados en el trabajo de referentes como **Edward Tufte** y **Stephen Few**. La comprensión de estos principios es lo que permite tomar decisiones informadas sobre qué información mostrar, cómo organizarla visualmente y qué tipo de gráfico utilizar en cada caso.

    La librería **Chart.js** se ha presentado como la herramienta principal para la creación de gráficos, analizando en profundidad su API: tipos de gráficos disponibles y criterios de selección, estructura de la configuración (data, datasets, options), personalización de escalas, plugins (leyenda, tooltip, título, zoom, anotaciones) y gestión de colores con consideraciones de accesibilidad para daltonismo.

    La integración de Chart.js en Angular se ha abordado con especial atención al ciclo de vida de los componentes: creación de instancias en `ngAfterViewInit`, actualización reactiva mediante **Signals** con `effect()` y `computed()`, destrucción en `ngOnDestroy` para prevenir fugas de memoria, y encapsulación en componentes reutilizables `ChartWidget` que abstraen la complejidad de la librería.

    **ApexCharts** se ha presentado como alternativa con ventajas en interactividad, estética por defecto, modo oscuro y tipos de gráficos exclusivos (RadialBar, Heatmap, Treemap), permitiendo al alumnado elegir la herramienta más adecuada para cada proyecto.

    El diseño de dashboards en Angular con Tailwind CSS se ha concretado en layouts con **CSS Grid** adaptativos, componentes widget reutilizables (StatCard, ChartWidget, DataTable, FilterBar) y manejo de estados (carga, vacío, error, datos).

    Finalmente, la exportación de datos y gráficos cierra el círculo de valor del dashboard, permitiendo que la información trascienda la pantalla y llegue a otras herramientas y formatos.

## Recursos complementarios

- **Chart.js - Documentación oficial**: https://www.chartjs.org/docs/latest/
- **ApexCharts - Documentación oficial**: https://apexcharts.com/docs/angular-charts/
- **ng-apexcharts - Repositorio GitHub**: https://github.com/apexcharts/ng-apexcharts
- **Libro: "Information Dashboard Design" de Stephen Few**
- **Libro: "The Visual Display of Quantitative Information" de Edward Tufte**
- **ColorBrewer2 - Paletas para visualización de datos**: https://colorbrewer2.org/
- **Coolors - Generador de paletas de colores**: https://coolors.co/
- **Chart.js Skeleton Loader Examples**: buscar "chart js skeleton loading" en CodePen
- **Curso: "Angular Data Visualization with Chart.js"** (YouTube, varios canales)
- **Tailwind CSS Grid Documentation**: https://tailwindcss.com/docs/grid-template-columns
