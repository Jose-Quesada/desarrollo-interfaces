---
icon: lucide/file-down
---

# Generación de Informes y Documentos

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Comprender la necesidad de generar documentos desde aplicaciones empresariales y los casos de uso más habituales (facturas, informes, certificados, albaranes, reportes de ventas, comprobantes fiscales, contratos, presupuestos).
2. Diferenciar entre los enfoques de generación de documentos en el lado del cliente (navegador) y en el lado del servidor (API REST que genera el PDF y lo envía como respuesta), identificando ventajas, desventajas y criterios de elección para cada caso.
3. Dominar la librería PDFMake como herramienta principal para la generación de documentos PDF en aplicaciones Angular, incluyendo su instalación, configuración, estructura de documentos, estilos, tablas, imágenes, fuentes personalizadas y métodos de salida (descarga, apertura en nueva pestaña, impresión directa).
4. Conocer librerías alternativas como jsPDF (con el plugin jsPDF-AutoTable) y PDF-LIB, comprendiendo sus diferencias con PDFMake y los escenarios donde cada una resulta más adecuada.
5. Implementar casos prácticos completos de generación de documentos profesionales: facturas con datos de empresa, tablas de líneas de factura y cálculos automáticos; informes de ventas con portada, índice, gráficos y tablas de datos; certificados y diplomas con diseños decorativos.
6. Diseñar una arquitectura de servicios en Angular que encapsule la lógica de generación de documentos, aplicando patrones como la inyección de dependencias con `inject()`, interfaces para estandarizar generadores de documentos, y componentes opcionales de vista previa antes de la descarga.
7. Comprender y aplicar la exportación de datos en otros formatos habituales: CSV (generación manual con manejo de codificación UTF-8 y BOM, descarga mediante Blob y URL.createObjectURL) y Excel (utilizando la librería SheetJS/xlsx para crear libros de trabajo, hojas de cálculo y aplicar estilos básicos).
8. Integrar la generación de informes dentro del flujo de trabajo de una aplicación Angular completa, conectando los datos provenientes de servicios HTTP, Signals para el estado reactivo y formularios para la configuración de parámetros de los informes.
9. Aplicar buenas prácticas de desarrollo en la generación de documentos: separación de responsabilidades, tipado estricto con TypeScript, reutilización de plantillas, manejo de errores en la generación de PDFs y optimización del rendimiento en documentos extensos.
10. Identificar y evitar los errores más frecuentes en la generación de documentos, tales como problemas de codificación de caracteres especiales (tildes, eñes), configuraciones incorrectas de márgenes y tamaños de página, imágenes que no se renderizan o tablas que se desbordan.

## Resultado de aprendizaje asociado

Esta unidad contribuye, como RA principal, al **RA 5** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 5.** Crea informes evaluando y utilizando herramientas gráficas.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE a) Se ha establecido la estructura del informe.
- CE b) Se han generado informes básicos a partir de diferentes fuentes de datos mediante asistentes.
- CE c) Se han establecidos filtros sobre los valores a presentar en los informes.
- CE d) Se han incluido valores calculados, recuentos y totales.
- CE f) Se han utilizado herramientas para generar el código correspondiente a los informes de una aplicación.
- CE g) Se ha modificado el código correspondiente a los informes.
- CE h) Se ha desarrollado una aplicación que incluye informes incrustados.

Como RA secundario, se vincula al **RA 6** («Documenta aplicaciones seleccionando y utilizando herramientas específicas»), en particular:

- CE e) Se ha confeccionado el manual de usuario y la guía de referencia (documentos generados como PDF).

!!! note "Conocimientos previos"

    Para abordar con éxito esta unidad, el alumnado debe poseer los siguientes conocimientos previos, adquiridos en unidades anteriores del módulo y en otros módulos del ciclo formativo:

    - **Fundamentos de Angular**: creación de componentes standalone, uso de servicios con el patrón `inject()`, manejo de Signals para estado reactivo, comprensión del sistema de inyección de dependencias, uso de HttpClient para consumo de APIs REST, y conocimiento del ciclo de vida de los componentes (especialmente `ngOnInit` y `ngOnDestroy`).
    - **TypeScript avanzado**: definición de interfaces y tipos para modelar datos estructurados, uso de genéricos cuando sea necesario, comprensión de los tipos de unión e intersección, manejo de promesas y programación asíncrona con async/await, y conocimiento de los módulos de ES6 para importaciones y exportaciones.
    - **Maquetación web con CSS**: comprensión del modelo de caja, posicionamiento, diseño responsive, uso de medidas relativas y absolutas, y nociones de diseño visual (jerarquía, contraste, alineación) que serán trasladables al diseño de documentos PDF.
    - **Programación orientada a objetos**: comprensión de clases, interfaces, herencia y composición, principios **SOLID** aplicados a la arquitectura de servicios, y patrones de diseño básicos como el patrón estrategia (útil para estandarizar diferentes generadores de documentos).
    - **Conceptos de HTTP y APIs REST**: conocimiento de los verbos HTTP (GET, POST, PUT, DELETE), interpretación de códigos de estado, manejo de cabeceras HTTP (especialmente Content-Type y Content-Disposition para la descarga de archivos), y comprensión del formato JSON para el intercambio de datos.
    - **Sistema de archivos del sistema operativo**: comprensión de los formatos de archivo binarios y de texto, codificación de caracteres (UTF-8, ASCII, BOM), tipos MIME y su relación con la descarga de archivos desde el navegador, y conocimiento básico del objeto Blob y las URLs de objeto (URL.createObjectURL).
    - **Control de versiones con Git**: manejo básico de ramas, commits y gestión de dependencias con npm, ya que se instalarán y gestionarán varias librerías externas durante la unidad.

## Contenidos

1. **La necesidad de generar documentos desde aplicaciones empresariales**
   - 1.1. Tipos de documentos generados por aplicaciones: facturas, informes, certificados, albaranes, reportes, comprobantes, contratos, presupuestos, diplomas, cartas, etiquetas.
   - 1.2. Requisitos legales y fiscales que afectan a la generación de documentos (formato de facturas, numeración, datos obligatorios, conservación).
   - 1.3. Flujo de generación de documentos: obtención de datos → transformación → maquetación → renderizado → salida.

2. **Enfoques de generación de documentos: cliente vs servidor**
   - 2.1. Generación en el lado del cliente (navegador): ventajas (sin carga para el servidor, respuesta inmediata, offline), desventajas (limitaciones de rendimiento, dependencia de las capacidades del navegador), casos de uso recomendados.
   - 2.2. Generación en el lado del servidor: ventajas (mayor potencia de procesamiento, acceso a librerías nativas, documentos más complejos), desventajas (latencia de red, carga del servidor, dependencia de conectividad), casos de uso recomendados.
   - 2.3. Criterios de decisión: volumen de datos, complejidad del documento, necesidad de procesamiento en lote, requisitos de seguridad, disponibilidad offline.

3. **Librerías de generación de PDF en el ecosistema JavaScript/Angular**
   - 3.1. PDFMake: librería principal. Enfoque declarativo basado en definición de documento como objeto JavaScript. Instalación, tipos TypeScript, estructura del documento, elementos de contenido, estilos, tablas, imágenes, fuentes personalizadas.
   - 3.2. jsPDF: librería alternativa. Enfoque imperativo basado en API de dibujo. Plugin jsPDF-AutoTable para tablas. Comparativa con PDFMake.
   - 3.3. PDF-LIB: librería avanzada. Creación y manipulación de PDFs existentes. Rellenado de formularios, fusión de documentos, modificación de páginas.
   - 3.4. Tabla comparativa de las tres librerías: facilidad de uso, potencia, tamaño del bundle, documentación, comunidad, licencia.

4. **PDFMake en profundidad**
   - 4.1. Instalación y configuración en proyectos Angular.
   - 4.2. Estructura de la definición de documento: `content[]`, `styles{}`, `pageSize`, `pageOrientation`, `pageMargins`, `header`, `footer`, `background`, `images`, `defaultStyle`.
   - 4.3. Elementos de contenido: texto (`text`), columnas (`columns`), tablas (`table` con `body`, `widths`, `layout`, `headerRows`), imágenes (`image`), stacks (`stack`), listas ordenadas y no ordenadas (`ol`, `ul`), saltos de página (`pageBreak`), líneas horizontales (`canvas`), código QR (`qr`).
   - 4.4. Sistema de estilos: `fontSize`, `bold`, `italics`, `color`, `alignment`, `margin` (array de 4 valores o número único), `lineHeight`, `decoration`, `decorationStyle`, `decorationColor`, `background`, `fillColor`, `fillOpacity`.
   - 4.5. Tablas avanzadas: anchos de columna (porcentajes, `'*'`, `'auto'`), layouts predefinidos (`noBorders`, `headerLineOnly`, `lightHorizontalLines`), layouts personalizados, combinación de celdas (`colSpan`, `rowSpan`), alineación vertical (`fillColor`), cabeceras repetidas en cada página (`headerRows`).
   - 4.6. Imágenes en PDFMake: formatos soportados (JPEG, PNG, WebP), data URLs, imágenes en base64, dimensionamiento y relación de aspecto, imágenes desde URL remota (precarga y conversión a base64).
   - 4.7. Fuentes personalizadas: el sistema `pdfMake.vfs`, inclusión de fuentes adicionales (Roboto, Open Sans, Lato), fuentes para caracteres especiales (UTF-8, símbolos), peso de las fuentes y rendimiento.
   - 4.8. Métodos de salida: `download(defaultFilename)`, `open()` (nueva pestaña con Blob URL), `print()` (diálogo de impresión del navegador), `getDataUrl()` (obtener representación base64), `getBuffer()` (obtener ArrayBuffer), `getBlob()` (obtener objeto Blob).

5. **jsPDF como alternativa**
   - 5.1. Instalación: `npm install jspdf` y `npm install jspdf-autotable`.
   - 5.2. API imperativa: `doc.text()`, `doc.setFontSize()`, `doc.setTextColor()`, `doc.addPage()`, `doc.line()`, `doc.rect()`, `doc.circle()`, `doc.addImage()`.
   - 5.3. jsPDF-AutoTable para tablas: `doc.autoTable({ head, body, startY, theme, styles, headStyles, bodyStyles, columnStyles })`.
   - 5.4. Cuándo elegir jsPDF sobre PDFMake: necesidad de control fino de posicionamiento, documentos con gráficos vectoriales, integración con bibliotecas de terceros.

6. **PDF-LIB: manipulación avanzada de PDFs**
   - 6.1. Instalación: `npm install pdf-lib`.
   - 6.2. Casos de uso: rellenar formularios PDF existentes, añadir páginas a documentos, fusionar múltiples PDFs, extraer páginas, añadir anotaciones, rotar páginas, modificar metadatos.
   - 6.3. Ejemplo básico: cargar un PDF existente, rellenar campos de formulario, guardar el resultado.

7. **Casos prácticos completos de generación de PDFs con Angular**
   - 7.1. Factura profesional: logo de empresa (imagen en base64), datos del emisor y receptor en columnas, numeración y fecha, tabla de líneas de factura con anchos calculados, subtotales, IVA y total general calculados con Signals/computed, pie de página con datos bancarios y condiciones de pago, estilos corporativos (colores, tipografía, márgenes).
   - 7.2. Informe de ventas: portada con título, nombre del autor, fecha, logo de la empresa y fondo de color corporativo, índice de contenidos generado dinámicamente, secciones con gráficos exportados desde Chart.js como imágenes en base64, tablas de datos formateadas con alternancia de colores en filas, conclusiones y recomendaciones con formato destacado.
   - 7.3. Certificado o diploma: diseño decorativo con bordes gruesos y colores institucionales, imagen de fondo semitransparente (marca de agua), datos del alumno centrados y con tipografía elegante (Georgia, Merriweather o similar), espacio para firmas digitalizadas al pie, fecha de emisión, número de registro o código de verificación, sello de la institución como imagen superpuesta.

8. **Arquitectura recomendada para generación de documentos en Angular**
   - 8.1. Servicio `PdfService` centralizado: contiene métodos específicos por cada tipo de documento (`generateInvoice()`, `generateReport()`, `generateCertificate()`) y métodos auxiliares privados para tareas comunes (cargar imagen como base64, formatear fechas, formatear importes monetarios, aplicar estilos corporativos por defecto).
   - 8.2. Interfaz `DocumentGenerator`: define el contrato que deben cumplir todos los generadores de documentos, facilitando la extensibilidad y el testing. Métodos: `generate(data: T): void`, `preview(data: T): void`.
   - 8.3. Componente opcional `DocumentPreviewComponent`: muestra una vista previa del PDF en un iframe antes de permitir la descarga, mejorando la experiencia de usuario y reduciendo errores.
   - 8.4. Plantillas de documento como objetos TypeScript tipados: cada plantilla es una función pura que recibe los datos y devuelve la definición del documento PDFMake (`TDocumentDefinitions`), facilitando el testing unitario y la reutilización.
   - 8.5. Estrategia de extensión: añadir un nuevo tipo de documento implica crear una nueva clase que implemente `DocumentGenerator` y registrarla en el sistema de inyección de dependencias de Angular.

9. **Exportación de datos en otros formatos**
   - 9.1. Formato CSV (Comma-Separated Values): generación manual construyendo cadenas de texto con los datos unidos por comas (o punto y coma para compatibilidad con Excel en español), inclusión del BOM (Byte Order Mark `\uFEFF`) para asegurar la correcta codificación UTF-8 en Excel, manejo de caracteres especiales (comillas dobles, saltos de línea dentro de celdas, comas dentro de valores), generación del Blob con tipo MIME `text/csv;charset=utf-8;` y descarga mediante `URL.createObjectURL` y enlace dinámico.
   - 9.2. Formato Excel con SheetJS/xlsx: instalación (`npm install xlsx`), creación de un libro de trabajo (`XLSX.utils.book_new()`), creación de hojas de cálculo a partir de arrays de objetos (`XLSX.utils.json_to_sheet()`), adición de hojas al libro (`XLSX.utils.book_append_sheet()`), aplicación de estilos básicos (anchos de columna, formato de fecha, formato de moneda), generación del archivo binario (`XLSX.write()` con tipo `array`), creación del Blob y descarga. Limitaciones de la versión comunitaria de SheetJS respecto a estilos avanzados.
   - 9.3. Integración de los botones de exportación en los componentes Angular: uso de servicios específicos (`CsvExportService`, `ExcelExportService`), manejo del estado de carga durante la generación de archivos grandes, retroalimentación al usuario mediante toasts o indicadores de progreso.

10. **Integración completa con el flujo de una aplicación Angular**
    - 10.1. Obtención de datos desde servicios HTTP para alimentar los documentos.
    - 10.2. Uso de Signals y `computed` para realizar cálculos en tiempo real (totales, subtotales, IVA) que se reflejan tanto en la interfaz de usuario como en el documento PDF.
    - 10.3. Integración con formularios reactivos para capturar parámetros de generación de informes (rango de fechas, filtros, selección de columnas).
    - 10.4. Consideraciones de rendimiento para documentos grandes (cientos de páginas): paginación, generación asíncrona, lazy loading de imágenes, compresión de fuentes.

## Desarrollo teórico

### 1. La necesidad de generar documentos desde aplicaciones empresariales

Toda aplicación empresarial, en algún momento de su ciclo de vida, necesita producir documentos que abandonen la pantalla y se materialicen en formatos que el usuario pueda almacenar, imprimir, enviar por correo electrónico o presentar ante terceros. Esta necesidad no es accesoria sino central en muchos sectores: una aplicación de facturación que no emite facturas en **PDF** es prácticamente inútil; un sistema de gestión académica que no expide certificados de notas no cumple su función; un ERP que no genera informes de ventas para la dirección no aporta valor estratégico.

Los documentos generados por aplicaciones informáticas se caracterizan por tres propiedades fundamentales: son **estructurados** (siguen plantillas predefinidas con campos fijos y variables), son **reproducibles** (se generan bajo demanda tantas veces como sea necesario, a partir de datos almacenados en bases de datos) y son **portables** (se distribuyen en formatos estándar que cualquier sistema puede abrir, siendo PDF el formato rey por su fidelidad de representación independientemente del dispositivo).

Los tipos de documentos que una aplicación empresarial típica puede necesitar generar abarcan un amplio espectro:

- **Documentos fiscales y comerciales**: facturas (ordinarias, rectificativas, proforma), presupuestos, albaranes o notas de entrega, pedidos, tickets de compra, extractos de cuenta, cartas de pago, liquidaciones de impuestos.
- **Documentos de recursos humanos**: nóminas, contratos de trabajo, certificados de empresa, informes de vida laboral, cartas de amonestación o despido, finiquitos.
- **Documentos académicos**: certificados de notas, títulos y diplomas, expedientes académicos, horarios, actas de evaluación, justificantes de matrícula.
- **Informes y reportes**: informes de ventas (diarios, semanales, mensuales, anuales), informes de inventario y stock, informes financieros (balance, cuenta de pérdidas y ganancias), informes de marketing (ROI de campañas, tasas de conversión), informes de calidad y auditoría, dashboards exportados a PDF.
- **Documentos legales y administrativos**: contratos, acuerdos de confidencialidad (NDA), poderes notariales, escrituras, instancias y solicitudes administrativas.

!!! info "Normativa"

    En el contexto normativo español y andaluz, la generación de documentos electrónicos está sujeta a requisitos legales específicos. Por ejemplo, la factura electrónica está regulada por el **Real Decreto 1619/2012** (Reglamento de facturación), que establece los datos obligatorios que debe contener toda factura: número y serie, fecha de expedición, nombre y apellidos o razón social del expedidor y del destinatario, NIF, domicilio, descripción de las operaciones, tipo impositivo, cuota tributaria, fecha de prestación del servicio si es distinta a la de expedición. Además, la **Ley 25/2013** impulsa el uso de la factura electrónica en las administraciones públicas. Cualquier aplicación que genere facturas debe, por tanto, asegurar la inclusión de todos estos campos obligatorios.

El flujo típico de generación de un documento sigue estas etapas:

1. **Obtención de datos**: los datos necesarios para el documento se recuperan de la fuente correspondiente (base de datos mediante API REST, estado de la aplicación en memoria, entrada del usuario a través de formularios, datos de configuración).
2. **Transformación**: los datos brutos se transforman al formato requerido por el documento (cálculo de totales, formateo de fechas al estándar local `dd/mm/aaaa`, formateo de importes monetarios con separadores de miles y dos decimales, traducción de códigos a descripciones legibles).
3. **Maquetación**: los datos transformados se insertan en una plantilla que define la estructura visual del documento (posiciones, tamaños, colores, tipografías, alineaciones, márgenes).
4. **Renderizado**: la plantilla poblada con datos se convierte en el formato final (PDF, CSV, Excel) mediante la librería correspondiente, generando los bytes que constituyen el archivo.
5. **Salida**: el documento generado se entrega al usuario (descarga en el navegador, envío por correo electrónico, almacenamiento en la nube, apertura en nueva pestaña, impresión directa).

### 2. Enfoques de generación: cliente vs servidor

La decisión sobre dónde ejecutar la generación del documento —en el navegador del cliente o en el servidor— es una **decisión arquitectónica** con implicaciones significativas en el rendimiento, la seguridad, la experiencia de usuario y los costes de infraestructura.

#### Generación en el lado del cliente (navegador)

En este enfoque, la aplicación Angular que se ejecuta en el navegador del usuario es la responsable de construir el PDF completo utilizando librerías JavaScript como **PDFMake** o **jsPDF**. Los datos necesarios para el documento se obtienen previamente de la API y residen en memoria (en Signals, servicios o el estado del componente). La generación del PDF se realiza íntegramente en el hilo principal del navegador (o en un Web Worker si se desea evitar bloquear la interfaz de usuario durante documentos muy grandes).

**Ventajas**:
- **Sin carga en el servidor**: el servidor solo necesita servir los datos (normalmente en formato JSON), que es una operación mucho más ligera que renderizar un PDF completo. Esto permite escalar la aplicación a miles de usuarios concurrentes sin que la generación de documentos sea un cuello de botella.
- **Respuesta inmediata**: al no existir latencia de red para la generación (los datos ya están en el cliente), el usuario percibe que el documento se genera instantáneamente al pulsar el botón de descarga.
- **Funcionamiento offline**: si la aplicación es una **PWA (Progressive Web Application)**, los documentos pueden generarse incluso sin conexión a internet, siempre que los datos estén cacheados localmente.
- **Previsualización en tiempo real**: el usuario puede ver cómo cambia el documento a medida que modifica los datos en un formulario, ya que la regeneración del PDF es instantánea y no requiere llamadas al servidor.

**Desventajas**:
- **Rendimiento limitado del cliente**: los navegadores tienen limitaciones de memoria y CPU. Generar un PDF de 500 páginas con cientos de imágenes puede bloquear la interfaz durante varios segundos e incluso causar que el navegador muestre el diálogo de "esta página no responde".
- **Dependencia de las capacidades del navegador**: navegadores antiguos o con soporte limitado de JavaScript pueden no ser capaces de ejecutar las librerías de generación de PDFs.
- **Peso del bundle**: las librerías de generación de PDFs como PDFMake añaden varios cientos de kilobytes al bundle de JavaScript que se descarga el usuario, incrementando el tiempo de carga inicial de la aplicación (mitigable con lazy loading de los módulos de generación de documentos).

**Casos de uso recomendados**: documentos de tamaño pequeño a mediano (1 a 50 páginas), aplicaciones con alta concurrencia de usuarios, aplicaciones que requieren funcionamiento offline, dashboards y herramientas de autoservicio donde el usuario genera sus propios informes bajo demanda, previsualización de documentos antes de enviar.

#### Generación en el lado del servidor

En este enfoque, la aplicación Angular envía una petición HTTP al servidor (por ejemplo, `POST /api/invoices/123/pdf`), el servidor recupera los datos de la base de datos, renderiza el PDF utilizando librerías del ecosistema del lenguaje de backend (Java, Node.js, Python, PHP, .NET) y devuelve el archivo PDF en el cuerpo de la respuesta HTTP con la cabecera `Content-Type: application/pdf`. El navegador, al recibir esta respuesta, muestra el PDF o lo descarga automáticamente.

**Ventajas**:
- **Mayor potencia de procesamiento**: el servidor tiene acceso a toda la CPU y memoria de la máquina, permitiendo generar documentos extremadamente complejos (miles de páginas, cientos de imágenes de alta resolución, gráficos vectoriales intrincados) sin afectar a la experiencia del usuario.
- **Acceso a librerías nativas**: los lenguajes de servidor tienen acceso a librerías de generación de PDFs mucho más potentes y maduras (iText en Java, ReportLab en Python, FPDF/TCPDF en PHP, Puppeteer/Playwright en Node.js para renderizar HTML a PDF con motores de navegador reales como Chromium), que permiten funcionalidades avanzadas como firmas digitales, cifrado, metadatos XMP, cumplimiento de estándares **PDF/A** para archivado a largo plazo, accesibilidad PDF/UA, relleno de formularios PDF, capas opcionales (OCG), etc.
- **Seguridad**: los datos sensibles nunca abandonan el servidor; solo se envía el producto final. Esto es crucial para documentos que contienen información confidencial (datos bancarios, historiales médicos, secretos comerciales). Además, ciertos procesos de negocio requieren que los documentos se generen en un entorno controlado y auditado.
- **Independencia del dispositivo cliente**: el usuario puede solicitar la generación de un documento desde un dispositivo de bajas prestaciones (móvil, tablet) y el servidor se encarga del trabajo pesado.

**Desventajas**:
- **Latencia de red**: el usuario debe esperar a que el servidor procese la petición y devuelva el PDF, lo que puede llevar varios segundos dependiendo de la complejidad del documento y la carga del servidor.
- **Carga computacional en el servidor**: cada petición de generación de PDF consume recursos del servidor, lo que puede requerir escalado horizontal (más instancias) y aumentar los costes de infraestructura para aplicaciones con alta demanda de generación de documentos.
- **Dependencia de conectividad**: sin conexión a internet, no es posible generar ni descargar documentos.
- **Mayor complejidad de desarrollo**: se necesita mantener código de generación de documentos en dos lenguajes/frameworks diferentes (Angular para la UI y el backend para los PDFs), lo que puede llevar a duplicidades e inconsistencias.

**Casos de uso recomendados**: documentos de gran tamaño (más de 100 páginas), documentos que requieren firma digital o cifrado, documentos que se generan en lote (miles de facturas a final de mes), aplicaciones que manejan datos altamente confidenciales, documentos que deben cumplir estándares estrictos (PDF/A para la administración pública), aplicaciones donde el cliente es un dispositivo de bajas prestaciones (móvil).

#### Criterios de decisión

| Factor | Recomendación |
|---|---|
| Número de páginas < 50 | **Cliente** (PDFMake, jsPDF) |
| Número de páginas > 100 | **Servidor** |
| Alta concurrencia (>1000 usuarios simultáneos) | **Cliente** (descarga el servidor) |
| Datos confidenciales (bancarios, médicos) | **Servidor** |
| Requiere firma digital | **Servidor** (obligatorio) |
| Funcionamiento offline necesario | **Cliente** |
| Previsualización interactiva | **Cliente** |
| Documentos en lote (miles) | **Servidor** |
| Cumplimiento PDF/A | **Servidor** |

En el contexto de este módulo de Desarrollo de Interfaces, nos centraremos en el enfoque cliente por ser el que involucra directamente las tecnologías que estamos estudiando (Angular, TypeScript, librerías JavaScript del ecosistema npm). No obstante, el alumnado debe conocer ambas posibilidades y saber argumentar cuál es la más adecuada para cada escenario profesional.

### 3. Librerías de generación de PDF en el ecosistema JavaScript

El ecosistema **npm** ofrece múltiples librerías para la generación de documentos PDF desde JavaScript/TypeScript. A continuación se presenta un análisis detallado de las tres principales, ordenadas de menor a mayor complejidad.

#### PDFMake (enfoque declarativo)

**PDFMake** es una librería que adopta un enfoque declarativo: el desarrollador define un documento como un objeto JavaScript que describe qué elementos contiene el documento (textos, tablas, imágenes, columnas) y cómo deben verse (estilos). PDFMake se encarga internamente del layout, el posicionamiento, los saltos de página y el renderizado final. Esta filosofía declarativa la hace extremadamente productiva para la mayoría de los casos de uso empresarial, ya que el desarrollador no necesita preocuparse por las coordenadas exactas de cada elemento ni por la paginación.

PDFMake utiliza internamente **pdfkit** como motor de renderizado y se distribuye como un paquete npm con soporte nativo para TypeScript (los tipos están disponibles como `@types/pdfmake`, aunque en versiones recientes se incluyen en el propio paquete).

**Instalación**:
```bash
npm install pdfmake
```

**Estructura mínima de un documento PDFMake**:
```typescript
import pdfMake from 'pdfmake/build/pdfmake';
import pdfFonts from 'pdfmake/build/vfs_fonts';

pdfMake.vfs = pdfFonts.vfs;

const docDefinition = {
  content: [
    { text: 'Título del documento', style: 'header' },
    { text: 'Este es un párrafo de texto normal con un salto de línea.\n\nY aquí otro párrafo.' },
    {
      table: {
        headerRows: 1,
        widths: ['*', 'auto', 100],
        body: [
          ['Concepto', 'Cantidad', 'Precio'],
          ['Producto A', '2', '10,50 €']
        ]
      }
    }
  ],
  styles: {
    header: { fontSize: 18, bold: true, margin: [0, 0, 0, 10] }
  },
  pageSize: 'A4',
  pageMargins: [40, 60, 40, 60]
};

pdfMake.createPdf(docDefinition).download('documento.pdf');
```

Esta sencillez es la razón principal por la que PDFMake es la librería recomendada en este módulo y la más utilizada en proyectos Angular reales para la generación de documentos empresariales.

#### jsPDF (enfoque imperativo)

**jsPDF** adopta un enfoque imperativo: el desarrollador dibuja el PDF paso a paso, indicando explícitamente las coordenadas (x, y) donde se coloca cada elemento. Esto proporciona un control total sobre el posicionamiento, pero a costa de una mayor verbosidad y complejidad, especialmente en documentos con tablas y contenido dinámico que requiere paginación automática.

Para mitigar la complejidad de las tablas, jsPDF cuenta con un plugin llamado **jsPDF-AutoTable** que permite generar tablas con un enfoque más declarativo y con paginación automática.

**Instalación**:
```bash
npm install jspdf
npm install jspdf-autotable
```

**Ejemplo mínimo con jsPDF y AutoTable**:
```typescript
import jsPDF from 'jspdf';
import 'jspdf-autotable';

const doc = new jsPDF();
doc.setFontSize(18);
doc.text('Título del documento', 14, 22);
doc.setFontSize(11);

(doc as any).autoTable({
  head: [['Concepto', 'Cantidad', 'Precio']],
  body: [['Producto A', '2', '10,50 €']],
  startY: 30
});

doc.save('documento.pdf');
```

**Cuándo elegir jsPDF sobre PDFMake**: cuando se necesita un control extremadamente fino sobre el posicionamiento (por ejemplo, para replicar exactamente el diseño de un formulario oficial escaneado), cuando se van a dibujar gráficos vectoriales complejos con la API de dibujo de jsPDF (`doc.line()`, `doc.circle()`, `doc.ellipse()`, `doc.triangle()`), o cuando se requiere integrar con otras librerías que producen salidas compatibles con jsPDF.

#### PDF-LIB (manipulación de PDFs existentes)

**PDF-LIB** ocupa un nicho diferente a las dos anteriores: no está pensada tanto para crear documentos desde cero, sino para **manipular PDFs ya existentes**. Sus casos de uso principales son:

- Rellenar formularios PDF con campos de texto, checkboxes, botones de radio, etc.
- Añadir, eliminar o reordenar páginas de un PDF existente.
- Fusionar múltiples PDFs en uno solo (muy útil para juntar varios documentos generados por separado).
- Extraer páginas específicas de un PDF grande.
- Añadir anotaciones, marcas de agua, sellos digitales, superposiciones de texto o imagen.
- Rotar páginas individuales.
- Modificar los metadatos del PDF (título, autor, tema, palabras clave).
- Incrustar fuentes personalizadas para garantizar la correcta visualización en cualquier dispositivo.
- Crear documentos PDF desde cero con control total (aunque para este caso suele ser más productivo usar PDFMake o jsPDF).

**Instalación**:
```bash
npm install pdf-lib
```

PDF-LIB es la elección correcta cuando la aplicación necesita partir de plantillas PDF diseñadas por un departamento de diseño gráfico o por un organismo oficial (por ejemplo, el modelo 303 de la AEAT en España) y rellenarlas programáticamente con los datos del usuario.

#### Tabla comparativa de las tres librerías

| Característica | PDFMake | jsPDF + AutoTable | PDF-LIB |
|---|---|---|---|
| Paradigma | Declarativo | Imperativo | Imperativo |
| Facilidad de uso | Muy alta | Media | Media-baja |
| Curva de aprendizaje | Baja | Media | Media-alta |
| Crear PDFs desde cero | Excelente | Bueno | Bueno pero verboso |
| Tablas | Excelente, nativas | Bueno, con plugin | No (implementación manual) |
| Manipular PDFs existentes | No | No | Excelente |
| Rellenar formularios | No | No | Excelente |
| Control de posicionamiento | Automático (layout) | Manual (coordenadas) | Manual (coordenadas) |
| Paginación automática | Sí (integrada) | Sí (AutoTable) | No (manual) |
| Tamaño del bundle | ~300 KB | ~200 KB + ~50 KB plugin | ~150 KB |
| Tipos TypeScript incluidos | Sí | Sí | Sí |
| Comunidad y mantenimiento | Activa, muy popular | Activa, muy popular | Activa |
| Licencia | MIT | MIT | MIT |

### 4. PDFMake en profundidad

**PDFMake** es la librería que utilizaremos de forma principal en esta unidad debido a su equilibrio entre potencia, facilidad de uso y productividad. A continuación se detalla en profundidad cada aspecto de la librería con ejemplos de código TypeScript aplicables directamente en proyectos Angular.

#### 4.1. Instalación y configuración en Angular

En un proyecto Angular standalone, la instalación de PDFMake se realiza mediante npm:

```bash
npm install pdfmake
```

Los tipos TypeScript están incluidos en el paquete a partir de la versión 0.2.0. Si por alguna razón no se reconocen, se pueden instalar explícitamente:

```bash
npm install --save-dev @types/pdfmake
```

La configuración básica que debe realizarse antes de usar PDFMake es cargar las fuentes virtuales (vfs_fonts). PDFMake incluye un sistema de archivos virtual que contiene las fuentes necesarias para renderizar el texto. Las fuentes por defecto incluyen **Roboto** (la familia tipográfica por defecto de PDFMake) en sus variantes normal, negrita, cursiva y negrita-cursiva.

```typescript
import pdfMake from 'pdfmake/build/pdfmake';
import pdfFonts from 'pdfmake/build/vfs_fonts';

pdfMake.vfs = pdfFonts.vfs;
```

!!! tip "Buenas prácticas"

    Es importante ejecutar esta configuración **una sola vez** durante el ciclo de vida de la aplicación. En Angular, el lugar ideal es en el constructor del servicio `PdfService`, que al ser un **singleton** proporcionado en `root` (`providedIn: 'root'`), se instanciará una única vez.

```typescript
import { Injectable } from '@angular/core';
import pdfMake from 'pdfmake/build/pdfmake';
import pdfFonts from 'pdfmake/build/vfs_fonts';
import { TDocumentDefinitions } from 'pdfmake/interfaces';

@Injectable({ providedIn: 'root' })
export class PdfService {
  constructor() {
    pdfMake.vfs = pdfFonts.vfs;
  }

  generate(documentDefinition: TDocumentDefinitions, filename: string = 'documento.pdf'): void {
    pdfMake.createPdf(documentDefinition).download(filename);
  }
}
```

#### 4.2. Estructura de la definición de documento

La definición de un documento PDFMake es un objeto JavaScript/TypeScript que sigue la interfaz `TDocumentDefinitions`. Los campos principales de esta interfaz son:

```typescript
interface TDocumentDefinitions {
  // El contenido del documento. Es el campo más importante.
  // Puede ser un string, un array de objetos de contenido, o un objeto de contenido.
  content: Content | Content[];

  // Estilos con nombre que se pueden referenciar mediante la propiedad 'style' en los elementos.
  styles?: { [styleName: string]: Style };

  // Tamaño de página. Valores típicos: 'A4', 'A3', 'LETTER', 'LEGAL', o un objeto { width, height }.
  // Por defecto: 'A4'
  pageSize?: PageSize;

  // Orientación de página: 'portrait' (vertical) o 'landscape' (horizontal).
  // Por defecto: 'portrait'
  pageOrientation?: PageOrientation;

  // Márgenes de página: array de 4 números [left, top, right, bottom] o un solo número para todos.
  // Por defecto: [40, 60, 40, 60] (en puntos, 1 punto ≈ 0.353 mm)
  pageMargins?: Margins;

  // Cabecera que se repite en cada página.
  // Puede ser una función (currentPage, pageCount, pageSize) => Content para numeración dinámica.
  header?: Content | ((currentPage: number, pageCount: number, pageSize: PageSize) => Content);

  // Pie de página que se repite en cada página.
  footer?: Content | ((currentPage: number, pageCount: number, pageSize: PageSize) => Content);

  // Fondo que se repite en cada página (marca de agua).
  background?: Content | ((currentPage: number, pageSize: PageSize) => Content);

  // Estilo por defecto aplicado a todo el documento si no se especifica otro.
  defaultStyle?: Style;

  // Diccionario de imágenes en base64 referenciables por nombre (clave) desde el contenido.
  images?: { [imageName: string]: string };

  // Compresión de la salida: true (por defecto) comprime el PDF, false lo desactiva.
  compress?: boolean;

  // Versión del PDF a generar: '1.3', '1.4', '1.5', '1.6', '1.7'.
  // Por defecto: '1.3' para máxima compatibilidad.
  version?: string;
}
```

#### 4.3. Elementos de contenido

El contenido del documento PDFMake se construye combinando diversos tipos de elementos. Cada elemento es un objeto con propiedades que definen su apariencia y comportamiento.

**Texto (`text`)**: el elemento más básico. Puede ser un simple string o un objeto con propiedades de estilo.

```typescript
// Texto simple
{ text: 'Hola mundo' }

// Texto con estilo inline
{ text: 'Importante', bold: true, color: 'red', fontSize: 16 }

// Texto con múltiples fragmentos de diferente estilo (equivalente a spans en HTML)
{
  text: [
    'Texto normal ',
    { text: 'texto en negrita ', bold: true },
    { text: 'y texto en rojo', color: 'red' }
  ]
}

// Texto con salto de línea explícito (equivalente a <br> en HTML)
{ text: 'Línea 1\nLínea 2\n\nLínea 4 después de línea en blanco' }
```

**Columnas (`columns`)**: permiten disponer elementos uno al lado del otro, creando layouts horizontales. Son fundamentales para documentos empresariales: datos del emisor a la izquierda, datos del receptor a la derecha.

```typescript
{
  columns: [
    {
      width: '60%',
      text: 'Datos del emisor:\nEmpresa S.L.\nCIF: B-12345678\nCalle Mayor, 1\n41001 Sevilla'
    },
    {
      width: '40%',
      text: 'Datos del receptor:\nCliente Ejemplo\nNIF: 12345678Z\nAv. de la Constitución, 5\n18001 Granada',
      alignment: 'right'
    }
  ]
}
```

Las columnas pueden contener cualquier tipo de contenido, incluyendo otras columnas anidadas, tablas, imágenes, stacks, etc. El ancho de las columnas se puede especificar en porcentaje, en píxeles, con `'*'` (ancho automático, ocupa el espacio restante) o con `'auto'` (ancho ajustado al contenido).

**Tablas (`table`)**: uno de los elementos más potentes y utilizados en documentos empresariales. PDFMake maneja automáticamente el layout de las tablas, los anchos de columna, la repetición de cabeceras en cada página y los estilos de borde.

```typescript
{
  table: {
    // Número de filas que se consideran cabecera y se repiten en cada página
    headerRows: 1,

    // Anchura de las columnas: array de números, strings ('*', 'auto') o porcentajes
    widths: ['*', 'auto', 80, 80, 80],

    // Cuerpo de la tabla: array de filas, cada fila es un array de celdas
    body: [
      // Fila de cabecera (primera fila, se repetirá en cada página)
      [
        { text: 'Concepto', style: 'tableHeader', bold: true, fillColor: '#eeeeee' },
        { text: 'Cant.', style: 'tableHeader', bold: true, fillColor: '#eeeeee', alignment: 'center' },
        { text: 'Precio', style: 'tableHeader', bold: true, fillColor: '#eeeeee', alignment: 'right' },
        { text: 'IVA%', style: 'tableHeader', bold: true, fillColor: '#eeeeee', alignment: 'center' },
        { text: 'Total', style: 'tableHeader', bold: true, fillColor: '#eeeeee', alignment: 'right' }
      ],
      // Fila de datos
      ['Desarrollo web frontend', '1', '2.500,00 €', '21%', '2.500,00 €'],
      ['Consultoría UX/UI', '2', '750,00 €', '21%', '1.500,00 €'],
      // Celdas combinadas: colSpan y rowSpan
      [
        { text: 'SUBTOTAL', colSpan: 4, alignment: 'right', bold: true, fillColor: '#f5f5f5' },
        {},
        {},
        {},
        { text: '4.000,00 €', alignment: 'right', bold: true, fillColor: '#f5f5f5' }
      ]
    ]
  }
}
```

Los layouts predefinidos para las tablas son:
- `noBorders`: sin bordes.
- `headerLineOnly`: solo una línea debajo de la cabecera.
- `lightHorizontalLines`: líneas horizontales finas.
- `lightHorizontalLinesAndVerticalLines`: líneas horizontales y verticales finas (recomendado para facturas).

Además, se pueden definir layouts personalizados mediante un objeto que especifique el ancho de línea y color para cada parte de la tabla: `hLineWidth`, `vLineWidth`, `hLineColor`, `vLineColor`, `paddingLeft`, `paddingRight`, `paddingTop`, `paddingBottom`, `fillColor`.

**Imágenes (`image`)**: PDFMake soporta imágenes en formato JPEG y PNG (incluyendo transparencias). Las imágenes deben proporcionarse como data URLs (base64) o como nombres referenciados en el diccionario `images` del documento.

```typescript
// Imagen desde data URL
{ image: 'data:image/png;base64,iVBORw0KGgo...', width: 150, height: 50 }

// Imagen referenciada en el diccionario de imágenes
const docDefinition = {
  images: {
    logo: 'data:image/png;base64,iVBORw0KGgo...',
    firma: 'data:image/png;base64,....'
  },
  content: [
    { image: 'logo', width: 150 },
    { image: 'firma', width: 100, alignment: 'right' }
  ]
};
```

Para obtener una imagen como base64 desde una URL remota, se puede utilizar la API `fetch` de JavaScript en combinación con `FileReader` o, más eficientemente, con la API `canvas.toDataURL()` si se necesita redimensionar la imagen antes de incrustarla.

```typescript
async getBase64ImageFromUrl(url: string): Promise<string> {
  const response = await fetch(url);
  const blob = await response.blob();
  return new Promise<string>((resolve, reject) => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result as string);
    reader.onerror = reject;
    reader.readAsDataURL(blob);
  });
}
```

**Stacks (`stack`)**: agrupan varios elementos verticalmente y permiten aplicar propiedades comunes (margen, alineación) a todo el grupo. Son útiles para crear secciones lógicas dentro del documento.

```typescript
{
  stack: [
    { text: 'Sección 1: Introducción', style: 'sectionHeader' },
    { text: 'Contenido de la introducción...' }
  ],
  margin: [0, 20, 0, 20]
}
```

**Listas**: las listas se implementan mediante el elemento `ul` (lista no ordenada, viñetas) y `ol` (lista ordenada, números). Los elementos pueden ser texto plano u objetos de contenido completos.

```typescript
{ ul: ['Primer elemento', 'Segundo elemento', 'Tercer elemento'] }

{ ol: ['Paso uno', 'Paso dos', 'Paso tres'] }
```

**Salto de página (`pageBreak`)**: fuerza un salto de página antes o después del contenido. Útil para separar secciones, insertar portadas o asegurar que cierto contenido siempre comienza en una página nueva.

```typescript
{ text: 'Este texto aparecerá en una página nueva', pageBreak: 'before' }
{ text: 'Después de este texto habrá un salto', pageBreak: 'after' }
```

**Líneas horizontales (`canvas`)**: se dibujan mediante un elemento `canvas` con una línea. Útiles como separadores visuales.

```typescript
{
  canvas: [
    {
      type: 'line',
      x1: 0, y1: 5,
      x2: 515, y2: 5,  // 515 es el ancho útil de A4 con márgenes de 40
      lineWidth: 1,
      lineColor: '#cccccc'
    }
  ]
}
```

**Código QR (`qr`)**: PDFMake soporta la generación de códigos QR directamente en el documento. Muy útil para facturas electrónicas con enlaces de verificación.

```typescript
{
  qr: 'https://miapp.com/verificar/INV-2024-0001',
  fit: 100,   // Tamaño en puntos
  margin: [0, 10, 0, 10]
}
```

#### 4.4. Sistema de estilos

PDFMake dispone de un sistema de estilos flexible que permite definir estilos con nombre en la sección `styles` del documento y luego aplicarlos a los elementos mediante la propiedad `style`. Esto promueve la coherencia visual y reduce la repetición de código.

```typescript
const docDefinition = {
  styles: {
    header: { fontSize: 22, bold: true, alignment: 'center', margin: [0, 0, 0, 20] },
    subheader: { fontSize: 16, bold: true, margin: [0, 10, 0, 5] },
    tableHeader: { fontSize: 10, bold: true, fillColor: '#2d3748', color: 'white' },
    footer: { fontSize: 8, italics: true, alignment: 'center', color: '#999999' },
    companyName: { fontSize: 14, bold: true, color: '#1a365d' },
    totalLabel: { fontSize: 12, bold: true, alignment: 'right' },
    totalAmount: { fontSize: 14, bold: true, alignment: 'right', color: '#2b6cb0' }
  },
  content: [
    { text: 'FACTURA', style: 'header' },
    // ...
  ]
};
```

Las propiedades de estilo más utilizadas son:

| Propiedad | Descripción | Valores de ejemplo |
|---|---|---|
| `fontSize` | Tamaño de fuente en puntos | `8`, `10`, `12`, `18` |
| `bold` | Texto en negrita | `true`, `false` |
| `italics` | Texto en cursiva | `true`, `false` |
| `color` | Color del texto (CSS) | `'#333333'`, `'red'`, `'rgb(0,0,255)'` |
| `alignment` | Alineación horizontal | `'left'`, `'center'`, `'right'`, `'justify'` |
| `margin` | Márgenes: [izq, arr, der, abj] o número único | `[0, 10, 0, 10]`, `10` |
| `lineHeight` | Altura de línea (multiplicador) | `1.2`, `1.5`, `2` |
| `background` | Color de fondo | `'#f0f0f0'` |
| `fillColor` | Color de relleno de celda (tablas) | `'#eeeeee'` |
| `decoration` | Decoración de texto | `'underline'`, `'lineThrough'`, `'overline'` |
| `decorationStyle` | Estilo de la decoración | `'solid'`, `'dashed'`, `'dotted'`, `'wavy'` |
| `decorationColor` | Color de la decoración | `'red'`, `'#cccccc'` |

#### 4.5. Tablas avanzadas

Las tablas son, con diferencia, el elemento más complejo y potente de PDFMake. Dominar su uso es esencial para generar documentos empresariales de calidad profesional.

**Anchos de columna**: PDFMake ofrece múltiples formas de especificar los anchos de columna en las tablas, y se pueden combinar en una misma tabla.

```typescript
widths: [
  'auto',   // La columna se ajusta al contenido más ancho de esa columna
  100,      // Ancho fijo en puntos
  '20%',    // Porcentaje del ancho disponible de la tabla
  '*'       // Ancho automático: el espacio restante se divide equitativamente entre las columnas con '*'
]
```

El cálculo de anchos sigue estas reglas:
1. Primero se asignan los anchos fijos (píxeles).
2. Luego los porcentajes.
3. Luego `'auto'`, que se ajusta al contenido más ancho.
4. El espacio restante se divide equitativamente entre las columnas marcadas con `'*'`.

**Layouts predefinidos**:

```typescript
layout: 'noBorders'
layout: 'headerLineOnly'
layout: 'lightHorizontalLines'
```

**Layout personalizado**: para un control total sobre el aspecto de la tabla, se puede definir un objeto de layout con las siguientes propiedades:

```typescript
layout: {
  hLineWidth: function (i: number, node: any) { return i === 0 || i === node.table.body.length ? 0 : 0.5; },
  vLineWidth: function (i: number, node: any) { return 0; },  // Sin líneas verticales
  hLineColor: function (i: number, node: any) { return '#cccccc'; },
  vLineColor: function (i: number, node: any) { return '#ffffff'; },
  paddingLeft: function (i: number, node: any) { return 8; },
  paddingRight: function (i: number, node: any) { return 8; },
  paddingTop: function (i: number, node: any) { return 6; },
  paddingBottom: function (i: number, node: any) { return 6; },
  fillColor: function (i: number, node: any) {
    // Alternar colores de fila para mejorar la legibilidad (efecto cebra)
    return i % 2 === 0 ? '#f7f7f7' : null;
  }
}
```

**Combinación de celdas**: `colSpan` y `rowSpan` permiten combinar celdas horizontal y verticalmente, similar a HTML.

```typescript
// Una celda que ocupa 3 columnas
[
  { text: 'Esta celda ocupa 3 columnas', colSpan: 3, alignment: 'center', bold: true },
  {},  // Las celdas combinadas deben representarse como objetos vacíos
  {},
  { text: 'Celda normal' }
]
```

**Manejo de saltos de página en tablas**: PDFMake intenta no partir una fila de tabla entre dos páginas. Si una fila es demasiado alta para caber en la página actual, se puede configurar `dontBreakRows: false` para permitir que las filas se rompan.

```typescript
table: {
  dontBreakRows: true,  // No romper filas (por defecto)
  headerRows: 1,
  // ...
}
```

#### 4.6. Fuentes personalizadas

PDFMake incluye por defecto la fuente Roboto en sus variantes normal, negrita, cursiva y negrita-cursiva. Para utilizar otras fuentes, es necesario cargarlas en el sistema de archivos virtual (`vfs`) de PDFMake.

El proceso para añadir una fuente personalizada es:

1. Obtener los archivos de fuente en formato **TrueType (.ttf)** y codificarlos en base64.
2. Construir un objeto de definición de fuente para PDFMake.
3. Asignar las fuentes al `vfs` y configurar PDFMake para usarlas.

```typescript
import pdfMake from 'pdfmake/build/pdfmake';

// Fuentes adicionales codificadas en base64 (en un proyecto real, importadas de archivos .ts separados)
const extraFonts = {
  Lato: {
    normal: 'AAEAAAAUAQAABABgR...',  // Contenido del .ttf en base64
    bold: 'AAEAAAAUAQAABABgR...',
    italics: 'AAEAAAAUAQAABABgR...',
    bolditalics: 'AAEAAAAUAQAABABgR...'
  }
};

// Asignar fuentes adicionales
pdfMake.fonts = {
  ...pdfMake.fonts,  // Mantener las fuentes preexistentes (Roboto)
  ...extraFonts
};

// Usar la fuente en el documento
const docDefinition = {
  defaultStyle: {
    font: 'Lato'
  },
  content: [...]
};
```

!!! tip "Rendimiento"

    Es importante considerar que cada fuente añadida incrementa el tamaño del bundle de JavaScript y el tiempo de carga de la aplicación. Para aplicaciones Angular, se recomienda cargar las fuentes adicionales mediante **lazy loading** (import dinámico) solo cuando se va a generar un documento, no en la carga inicial de la aplicación.

#### 4.7. Métodos de salida

PDFMake ofrece varios métodos para entregar el documento generado al usuario:

| Método | Descripción |
|---|---|
| `pdfMake.createPdf(docDef).download(filename)` | Descarga el PDF como archivo en el navegador. El parámetro `filename` es opcional y establece el nombre del archivo sugerido. |
| `pdfMake.createPdf(docDef).open()` | Abre el PDF en una nueva pestaña del navegador usando una URL Blob. Útil para vista previa. |
| `pdfMake.createPdf(docDef).print()` | Abre el diálogo de impresión del navegador con el PDF precargado. |
| `pdfMake.createPdf(docDef).getDataUrl()` | Devuelve una promesa que se resuelve con el PDF como data URL (base64). |
| `pdfMake.createPdf(docDef).getBuffer()` | Devuelve una promesa que se resuelve con el PDF como ArrayBuffer. |
| `pdfMake.createPdf(docDef).getBlob()` | Devuelve una promesa que se resuelve con el PDF como objeto Blob. |
| `pdfMake.createPdf(docDef).getStream()` | Devuelve el PDF como stream (solo en Node.js). |

Para el trabajo en Angular, los métodos más utilizados son `download()`, `open()` y `getBlob()`. Este último es especialmente útil cuando se necesita enviar el PDF generado a un servidor o adjuntarlo en un correo electrónico.

### 5. jsPDF como alternativa

Aunque PDFMake es la recomendación principal de esta unidad, es importante conocer **jsPDF** porque es ampliamente utilizado en la industria y puede ser la mejor opción para ciertos escenarios específicos.

jsPDF opera con un modelo de "lienzo": el desarrollador especifica coordenadas (x, y) para cada elemento, lo que proporciona un control absoluto sobre el posicionamiento. La contrapartida es que el manejo de saltos de página, tablas y contenido dinámico recae completamente sobre el desarrollador.

**Ventajas de jsPDF sobre PDFMake**:
- **Control de coordenadas absolutas**: ideal para replicar formularios oficiales donde cada campo debe estar en una posición exacta.
- **API de dibujo vectorial**: `doc.setDrawColor()`, `doc.setFillColor()`, `doc.rect()`, `doc.circle()`, `doc.ellipse()`, `doc.triangle()`, `doc.lines()`, `doc.roundedRect()`.
- **Soporte para múltiples formatos de imagen** (JPEG, PNG, WebP, BMP, TIFF, GIF).
- Posibilidad de añadir anotaciones, enlaces, y marcadores.
- **Integración con librerías de generación de gráficos** (Chart.js → imagen base64 → jsPDF).

**Ejemplo completo con jsPDF y AutoTable**:

```typescript
import jsPDF from 'jspdf';
import 'jspdf-autotable';

function generateInvoicePDF(invoiceData: any): void {
  const doc = new jsPDF();

  // Título
  doc.setFontSize(22);
  doc.setTextColor(44, 62, 80);
  doc.text('FACTURA', 105, 20, { align: 'center' });

  // Datos de empresa
  doc.setFontSize(10);
  doc.setTextColor(100, 100, 100);
  doc.text('Mi Empresa S.L.', 14, 40);
  doc.text('CIF: B-12345678', 14, 46);
  doc.text('Calle Mayor, 1 - 41001 Sevilla', 14, 52);

  // Datos del cliente
  doc.text('Cliente: ' + invoiceData.clientName, 14, 70);
  doc.text('NIF: ' + invoiceData.clientTaxId, 14, 76);

  // Tabla de líneas
  (doc as any).autoTable({
    startY: 90,
    head: [['Concepto', 'Cant.', 'Precio', 'IVA', 'Total']],
    body: invoiceData.lines.map((line: any) => [
      line.description,
      line.quantity,
      line.unitPrice.toFixed(2) + ' \u20AC',
      line.taxRate + '%',
      line.total.toFixed(2) + ' \u20AC'
    ]),
    theme: 'grid',
    headStyles: { fillColor: [44, 62, 80], textColor: [255, 255, 255] },
    bodyStyles: { fontSize: 9 },
    columnStyles: {
      1: { halign: 'center' },
      2: { halign: 'right' },
      3: { halign: 'center' },
      4: { halign: 'right' }
    }
  });

  // Total (después de la tabla, en la última página)
  const finalY = (doc as any).lastAutoTable.finalY + 10;
  doc.setFontSize(12);
  doc.text('TOTAL: ' + invoiceData.grandTotal.toFixed(2) + ' \u20AC', 195, finalY, { align: 'right' });

  doc.save(`factura-${invoiceData.invoiceNumber}.pdf`);
}
```

### 6. PDF-LIB: manipulación avanzada de PDFs existentes

**PDF-LIB** resuelve un problema diferente: no crear PDFs desde cero, sino manipular documentos ya existentes. Este enfoque es común en aplicaciones empresariales que necesitan trabajar con plantillas PDF proporcionadas por terceros.

**Ejemplo: rellenar un formulario PDF existente**:

```typescript
import { PDFDocument } from 'pdf-lib';

async function fillPdfForm(templateUrl: string, data: Record<string, string>): Promise<Uint8Array> {
  // Cargar la plantilla PDF
  const templateBytes = await fetch(templateUrl).then(res => res.arrayBuffer());
  const pdfDoc = await PDFDocument.load(templateBytes);

  // Obtener el formulario
  const form = pdfDoc.getForm();

  // Rellenar campos
  const nameField = form.getTextField('nombre');
  nameField.setText(data.name);

  const dateField = form.getTextField('fecha');
  dateField.setText(data.date);

  const amountField = form.getTextField('importe');
  amountField.setText(data.amount);

  // También se pueden marcar checkboxes...
  const checkField = form.getCheckBox('aceptado');
  checkField.check();

  // Guardar
  const pdfBytes = await pdfDoc.save();
  return pdfBytes;
}
```

**Ejemplo: fusionar varios PDFs en uno solo**:

```typescript
async function mergePDFs(pdfUrls: string[]): Promise<Uint8Array> {
  const mergedPdf = await PDFDocument.create();

  for (const url of pdfUrls) {
    const pdfBytes = await fetch(url).then(res => res.arrayBuffer());
    const pdf = await PDFDocument.load(pdfBytes);
    const copiedPages = await mergedPdf.copyPages(pdf, pdf.getPageIndices());
    copiedPages.forEach(page => mergedPdf.addPage(page));
  }

  return await mergedPdf.save();
}
```

### 7. Caso práctico 1: Generación de una factura profesional

A continuación se presenta el código completo en TypeScript para generar una factura profesional utilizando **PDFMake** en un servicio Angular. Este ejemplo integra todos los conceptos vistos hasta ahora: imágenes en base64, columnas, tablas con anchos personalizados, estilos corporativos, cabecera y pie de página repetidos en cada página, y formato de importes monetarios.

```typescript
import { Injectable, inject } from '@angular/core';
import pdfMake from 'pdfmake/build/pdfmake';
import pdfFonts from 'pdfmake/build/vfs_fonts';
import { TDocumentDefinitions, Content, StyleDictionary } from 'pdfmake/interfaces';

export interface InvoiceLine {
  description: string;
  quantity: number;
  unitPrice: number;
  taxRate: number;
}

export interface InvoiceData {
  invoiceNumber: string;
  issueDate: Date;
  dueDate: Date;
  company: {
    name: string;
    taxId: string;
    address: string;
    city: string;
    phone: string;
    email: string;
    logoBase64: string;
  };
  client: {
    name: string;
    taxId: string;
    address: string;
    city: string;
  };
  lines: InvoiceLine[];
  bankAccount: string;
  paymentTerms: string;
}

@Injectable({ providedIn: 'root' })
export class PdfService {
  constructor() {
    pdfMake.vfs = pdfFonts.vfs;
  }

  generateInvoice(data: InvoiceData): void {
    const docDefinition: TDocumentDefinitions = this.buildInvoiceDefinition(data);
    pdfMake.createPdf(docDefinition).download(`Factura_${data.invoiceNumber}.pdf`);
  }

  previewInvoice(data: InvoiceData): void {
    const docDefinition: TDocumentDefinitions = this.buildInvoiceDefinition(data);
    pdfMake.createPdf(docDefinition).open();
  }

  private buildInvoiceDefinition(data: InvoiceData): TDocumentDefinitions {
    const subtotal = data.lines.reduce((sum, line) => sum + line.quantity * line.unitPrice, 0);
    const taxTotal = data.lines.reduce((sum, line) => sum + (line.quantity * line.unitPrice * line.taxRate) / 100, 0);
    const grandTotal = subtotal + taxTotal;

    const formatCurrency = (amount: number): string =>
      new Intl.NumberFormat('es-ES', { style: 'currency', currency: 'EUR' }).format(amount);

    const formatDate = (date: Date): string =>
      new Intl.DateTimeFormat('es-ES', { day: '2-digit', month: '2-digit', year: 'numeric' }).format(date);

    const styles: StyleDictionary = {
      companyName: { fontSize: 16, bold: true, color: '#1a365d' },
      sectionTitle: { fontSize: 11, bold: true, color: '#4a5568', margin: [0, 0, 0, 2] },
      smallText: { fontSize: 9, color: '#718096' },
      tableHeader: { fontSize: 9, bold: true, fillColor: '#2d3748', color: '#ffffff', alignment: 'center' },
      tableCell: { fontSize: 9, color: '#2d3748' },
      tableCellRight: { fontSize: 9, color: '#2d3748', alignment: 'right' },
      tableCellCenter: { fontSize: 9, color: '#2d3748', alignment: 'center' },
      totalLabel: { fontSize: 11, bold: true, alignment: 'right', margin: [0, 4, 8, 0] },
      totalAmount: { fontSize: 13, bold: true, alignment: 'right', color: '#2b6cb0' },
      footerText: { fontSize: 8, italics: true, color: '#a0aec0' },
      watermark: { fontSize: 60, color: '#f7fafc', bold: true, alignment: 'center', margin: [0, 200, 0, 0] }
    };

    const headerContent: Content = {
      columns: [
        { image: 'companyLogo', width: 120, margin: [0, 10, 0, 0] },
        {
          stack: [
            { text: data.company.name, style: 'companyName' },
            { text: `CIF: ${data.company.taxId}`, style: 'smallText' },
            { text: data.company.address, style: 'smallText' },
            { text: data.company.city, style: 'smallText' }
          ],
          alignment: 'right', margin: [0, 5, 0, 0]
        }
      ],
      margin: [0, 0, 0, 10]
    };

    const footerContent: Content = (currentPage: number, pageCount: number): Content => ({
      columns: [
        { text: `Factura: ${data.invoiceNumber} | Emitida: ${formatDate(data.issueDate)}`, style: 'footerText', alignment: 'left' },
        { text: `Página ${currentPage} de ${pageCount}`, style: 'footerText', alignment: 'right' }
      ],
      margin: [40, 0, 40, 10]
    });

    const linesTableBody = [
      [
        { text: 'Concepto', style: 'tableHeader' },
        { text: 'Cantidad', style: 'tableHeader' },
        { text: 'Precio Ud.', style: 'tableHeader' },
        { text: 'IVA %', style: 'tableHeader' },
        { text: 'Importe', style: 'tableHeader' }
      ],
      ...data.lines.map((line) => {
        const lineTotal = line.quantity * line.unitPrice;
        return [
          { text: line.description, style: 'tableCell' },
          { text: line.quantity.toString(), style: 'tableCellCenter' },
          { text: formatCurrency(line.unitPrice), style: 'tableCellRight' },
          { text: `${line.taxRate}%`, style: 'tableCellCenter' },
          { text: formatCurrency(lineTotal), style: 'tableCellRight' }
        ];
      })
    ];

    const totalsRows = [
      [
        { text: 'Base imponible', colSpan: 4, style: 'totalLabel' },
        {}, {}, {},
        { text: formatCurrency(subtotal), style: 'totalAmount' }
      ],
      [
        { text: 'IVA (21%)', colSpan: 4, style: 'totalLabel' },
        {}, {}, {},
        { text: formatCurrency(taxTotal), style: 'totalAmount' }
      ],
      [
        { text: 'TOTAL', colSpan: 4, style: { ...styles.totalLabel, fontSize: 13, color: '#1a365d' } },
        {}, {}, {},
        { text: formatCurrency(grandTotal), style: { ...styles.totalAmount, fontSize: 15, color: '#1a365d' } }
      ]
    ];

    return {
      pageSize: 'A4',
      pageMargins: [45, 50, 45, 50],
      header: headerContent,
      footer: footerContent,
      images: { companyLogo: data.company.logoBase64 },

      content: [
        { text: 'FACTURA', fontSize: 28, bold: true, color: '#1a365d', alignment: 'right', margin: [0, 5, 0, 5] },
        { canvas: [{ type: 'line', x1: 0, y1: 0, x2: 470, y2: 0, lineWidth: 1, lineColor: '#e2e8f0' }], margin: [0, 8, 0, 8] },

        {
          columns: [
            {
              width: '55%',
              stack: [
                { text: 'DATOS DEL CLIENTE', style: 'sectionTitle' },
                { text: data.client.name, style: 'companyName', margin: [0, 2, 0, 0] },
                { text: `NIF: ${data.client.taxId}`, style: 'smallText' },
                { text: data.client.address, style: 'smallText' },
                { text: data.client.city, style: 'smallText' }
              ]
            },
            {
              width: '45%',
              stack: [
                { text: 'DETALLES DE FACTURA', style: 'sectionTitle', alignment: 'right' },
                { text: `N.º Factura: ${data.invoiceNumber}`, style: 'smallText', alignment: 'right' },
                { text: `Fecha emisión: ${formatDate(data.issueDate)}`, style: 'smallText', alignment: 'right' },
                { text: `Fecha vencimiento: ${formatDate(data.dueDate)}`, style: 'smallText', alignment: 'right' }
              ]
            }
          ],
          margin: [0, 10, 0, 20]
        },

        {
          table: {
            headerRows: 1,
            widths: ['*', 55, 75, 50, 80],
            body: [...linesTableBody, ...totalsRows]
          },
          layout: {
            hLineWidth: (i: number) => (i === 0 || i === linesTableBody.length - 1 ? 1.5 : 0.5),
            vLineWidth: () => 0,
            hLineColor: () => '#e2e8f0',
            paddingLeft: () => 8,
            paddingRight: () => 8,
            paddingTop: () => 6,
            paddingBottom: () => 6
          }
        },

        { text: '', margin: [0, 20, 0, 0] },

        {
          columns: [
            {
              width: '55%',
              stack: [
                { text: 'DATOS BANCARIOS', style: 'sectionTitle' },
                { text: data.bankAccount, style: 'smallText', margin: [0, 3, 0, 0] },
                { text: `Condiciones de pago: ${data.paymentTerms}`, style: 'smallText', margin: [0, 5, 0, 0] }
              ]
            },
            {
              width: '45%',
              stack: [
                { qr: `https://miapp.com/verificar/${data.invoiceNumber}`, fit: 80, alignment: 'right' },
                { text: 'Escanee para verificar esta factura', style: 'footerText', alignment: 'center', margin: [0, 5, 0, 0] }
              ]
            }
          ]
        },

        { text: 'Gracias por su confianza', style: { ...styles.footerText, margin: [0, 40, 0, 0] }, alignment: 'center' }
      ],

      styles: styles,
      defaultStyle: { font: 'Roboto', fontSize: 10, color: '#2d3748' }
    };
  }
}
```

### 8. Arquitectura recomendada para la generación de documentos

Para proyectos Angular de cierta envergadura, se recomienda estructurar el código de generación de documentos siguiendo los principios **SOLID** y los patrones de diseño de Angular.

**Estructura de carpetas propuesta**:

```
src/app/shared/services/
  pdf/
    pdf.service.ts                    # Servicio principal con métodos para cada tipo de documento
    templates/
      invoice.template.ts             # Función pura que devuelve TDocumentDefinitions para facturas
      report.template.ts              # Función pura para informes
      certificate.template.ts         # Función pura para certificados
    interfaces/
      document-generator.interface.ts # Interfaz para estandarizar generadores
    helpers/
      format.helper.ts                # Formateo de fechas, monedas, números
      image.helper.ts                 # Conversión de imágenes a base64
  csv/
    csv-export.service.ts            # Servicio de exportación CSV
  excel/
    excel-export.service.ts          # Servicio de exportación Excel
```

**Interfaz `DocumentGenerator`**:

```typescript
export interface DocumentGenerator<T> {
  generate(data: T, filename?: string): void;
  preview(data: T): void;
  getBlob(data: T): Promise<Blob>;
}
```

**Servicio `PdfService` implementando la interfaz para facturas**:

```typescript
@Injectable({ providedIn: 'root' })
export class PdfService implements DocumentGenerator<InvoiceData> {
  private readonly formatHelper = inject(FormatHelper);
  private readonly imageHelper = inject(ImageHelper);

  constructor() {
    pdfMake.vfs = pdfFonts.vfs;
  }

  generate(data: InvoiceData, filename?: string): void {
    const docDef = buildInvoiceDocument(data, this.formatHelper);
    pdfMake.createPdf(docDef).download(filename || `documento-${Date.now()}.pdf`);
  }

  preview(data: InvoiceData): void {
    const docDef = buildInvoiceDocument(data, this.formatHelper);
    pdfMake.createPdf(docDef).open();
  }

  async getBlob(data: InvoiceData): Promise<Blob> {
    const docDef = buildInvoiceDocument(data, this.formatHelper);
    return pdfMake.createPdf(docDef).getBlob();
  }
}
```

### 9. Exportación de datos en otros formatos

#### 9.1. Exportación a CSV

!!! info "Definición"

    El formato **CSV (Comma-Separated Values)** es el más sencillo y universal para el intercambio de datos tabulares. Aunque no existe un estándar oficial (solo el **RFC 4180** como recomendación), en la práctica se utiliza ampliamente por su simplicidad.

```typescript
import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class CsvExportService {
  exportToCsv<T extends Record<string, any>>(data: T[], filename: string, columns?: { key: keyof T; label: string }[]): void {
    if (data.length === 0) return;

    const keys = columns ? columns.map(c => c.key as string) : Object.keys(data[0]);
    const headers = columns ? columns.map(c => c.label) : keys;

    const csvRows: string[] = [];

    // Añadir BOM para que Excel reconozca UTF-8
    csvRows.push('\uFEFF' + headers.join(';'));

    for (const row of data) {
      const values = keys.map(key => {
        let value = row[key];

        if (value === null || value === undefined) {
          return '';
        }

        value = String(value);

        // Si el valor contiene punto y coma, comillas o saltos de línea, encerrar entre comillas
        if (value.includes(';') || value.includes('"') || value.includes('\n')) {
          value = '"' + value.replace(/"/g, '""') + '"';
        }

        return value;
      });

      csvRows.push(values.join(';'));
    }

    const blob = new Blob([csvRows.join('\n')], { type: 'text/csv;charset=utf-8;' });
    this.downloadBlob(blob, `${filename}.csv`);
  }

  private downloadBlob(blob: Blob, filename: string): void {
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    link.click();
    URL.revokeObjectURL(url);
  }
}
```

**Uso**: `csvService.exportToCsv(clientes, 'clientes', [{ key: 'name', label: 'Nombre' }, { key: 'email', label: 'Correo electrónico' }]);`

#### 9.2. Exportación a Excel con SheetJS

**SheetJS** es la librería de facto para trabajar con archivos Excel en JavaScript. Su instalación es sencilla:

```bash
npm install xlsx
```

```typescript
import { Injectable } from '@angular/core';
import * as XLSX from 'xlsx';

@Injectable({ providedIn: 'root' })
export class ExcelExportService {
  exportToExcel<T extends Record<string, any>>(
    data: T[],
    filename: string,
    sheetName: string = 'Datos',
    columns?: { key: keyof T; label: string }[]
  ): void {
    if (data.length === 0) return;

    const workbook = XLSX.utils.book_new();

    let sheetData: any[];

    if (columns) {
      sheetData = data.map(row => {
        const mappedRow: Record<string, any> = {};
        columns.forEach(col => {
          mappedRow[col.label] = row[col.key];
        });
        return mappedRow;
      });
    } else {
      sheetData = data;
    }

    const worksheet = XLSX.utils.json_to_sheet(sheetData);

    // Ajustar anchos de columna (estimación básica)
    const maxWidths: { width: number }[] = [];
    const sampleRow = sheetData[0];
    if (sampleRow) {
      Object.keys(sampleRow).forEach(key => {
        const maxLen = Math.max(
          key.length,
          ...sheetData.map(row => String(row[key] || '').length)
        );
        maxWidths.push({ width: Math.min(maxLen + 3, 50) });
      });
    }
    worksheet['!cols'] = maxWidths;

    XLSX.utils.book_append_sheet(workbook, worksheet, sheetName);

    const excelBuffer = XLSX.write(workbook, { bookType: 'xlsx', type: 'array' });
    const blob = new Blob([excelBuffer], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });

    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `${filename}.xlsx`;
    link.click();
    URL.revokeObjectURL(url);
  }
}
```

## Ejemplos guiados

### Ejemplo 1: Servicio PdfService completo con generación de factura

**Objetivo**: Implementar un servicio Angular completo capaz de generar facturas profesionales en formato PDF utilizando PDFMake.

**Paso 1**: Instalar pdfmake en el proyecto.

```bash
npm install pdfmake
```

**Paso 2**: Crear el servicio `PdfService` en `src/app/shared/services/pdf.service.ts`.

```typescript
import { Injectable } from '@angular/core';
import pdfMake from 'pdfmake/build/pdfmake';
import pdfFonts from 'pdfmake/build/vfs_fonts';

@Injectable({ providedIn: 'root' })
export class PdfService {
  constructor() {
    pdfMake.vfs = pdfFonts.vfs;
  }

  generateInvoice(invoice: any): void {
    const docDef = {
      pageSize: 'A4',
      pageMargins: [40, 60, 40, 60],
      content: [
        { text: 'FACTURA', fontSize: 24, bold: true, alignment: 'center', margin: [0, 0, 0, 20] },
        { text: `N.º: ${invoice.number}`, fontSize: 12, margin: [0, 0, 0, 5] },
        { text: `Fecha: ${new Date(invoice.date).toLocaleDateString('es-ES')}`, fontSize: 12, margin: [0, 0, 0, 10] },
        {
          table: {
            headerRows: 1,
            widths: ['*', 'auto', 'auto', 'auto'],
            body: [
              ['Concepto', 'Cantidad', 'Precio', 'Total'],
              ...invoice.items.map((item: any) => [
                item.description,
                item.quantity,
                `${item.price.toFixed(2)} €`,
                `${(item.quantity * item.price).toFixed(2)} €`
              ])
            ]
          }
        },
        { text: `TOTAL: ${invoice.total.toFixed(2)} €`, fontSize: 14, bold: true, alignment: 'right', margin: [0, 20, 0, 0] }
      ]
    };

    pdfMake.createPdf(docDef).download(`factura-${invoice.number}.pdf`);
  }
}
```

**Paso 3**: Utilizar el servicio en un componente.

```typescript
import { Component, signal } from '@angular/core';
import { PdfService } from '../../shared/services/pdf.service';

@Component({
  selector: 'app-invoice-detail',
  standalone: true,
  template: `
    <div class="p-6 max-w-4xl mx-auto">
      <h1 class="text-2xl font-bold mb-4">Factura {{ invoice().number }}</h1>
      <button (click)="downloadInvoice()"
              class="px-4 py-2 bg-blue-700 text-white rounded hover:bg-blue-800">
        Descargar factura
      </button>
    </div>
  `
})
export class InvoiceDetailComponent {
  private readonly pdfService = inject(PdfService);

  invoice = signal({
    number: 'F2024-0001',
    date: '2024-11-15',
    items: [
      { description: 'Desarrollo web', quantity: 1, price: 2500 },
      { description: 'Consultoría UX', quantity: 2, price: 750 }
    ],
    total: 4000
  });

  downloadInvoice(): void {
    this.pdfService.generateInvoice(this.invoice());
  }
}
```

**Explicación**: Se ha creado un servicio `PdfService` como singleton en `root` que encapsula toda la lógica de PDFMake. El componente solo necesita inyectar el servicio y llamar al método apropiado. La separación de responsabilidades es clara: el componente maneja la UI y los datos, el servicio maneja la generación del documento.

### Ejemplo 2: Componente Angular con botón "Descargar factura" que usa el servicio

**Objetivo**: Crear un componente con botón de descarga que utilice el sistema de **Signals** de Angular para reactividad.

```typescript
import { Component, inject, signal, computed } from '@angular/core';
import { PdfService } from '../../shared/services/pdf.service';

interface InvoiceItem {
  description: string;
  quantity: number;
  unitPrice: number;
}

@Component({
  selector: 'app-invoice-generator',
  standalone: true,
  template: `
    <div class="max-w-3xl mx-auto p-6">
      <h2 class="text-xl font-bold mb-4">Generar Factura</h2>

      <div class="space-y-3 mb-6">
        <input [(ngModel)]="clientName" placeholder="Nombre del cliente"
               class="w-full border rounded px-3 py-2" />

        <div *ngFor="let item of items(); let i = index" class="flex gap-2">
          <input [(ngModel)]="item.description" placeholder="Concepto"
                 class="flex-1 border rounded px-3 py-2" />
          <input [(ngModel)]="item.quantity" type="number" min="1"
                 class="w-20 border rounded px-3 py-2" />
          <input [(ngModel)]="item.unitPrice" type="number" min="0" step="0.01"
                 class="w-28 border rounded px-3 py-2" />
          <button (click)="removeItem(i)" class="px-3 py-2 bg-red-100 text-red-700 rounded">X</button>
        </div>

        <button (click)="addItem()" class="px-4 py-2 bg-gray-200 rounded">
          + Añadir línea
        </button>
      </div>

      <div class="flex justify-between items-center mb-6 p-4 bg-gray-50 rounded">
        <span class="text-lg font-bold">TOTAL:</span>
        <span class="text-xl font-bold text-blue-700">{{ totalFormatted() }}</span>
      </div>

      <button (click)="generateInvoice()"
              [disabled]="items().length === 0"
              class="px-6 py-3 bg-blue-700 text-white rounded-lg hover:bg-blue-800 disabled:opacity-50">
        Descargar factura
      </button>
    </div>
  `,
  imports: [/* FormsModule, NgFor, etc. */]
})
export class InvoiceGeneratorComponent {
  private readonly pdfService = inject(PdfService);

  clientName = '';
  items = signal<InvoiceItem[]>([{ description: '', quantity: 1, unitPrice: 0 }]);

  total = computed(() => this.items().reduce((sum, item) => sum + item.quantity * item.unitPrice, 0));
  totalFormatted = computed(() => this.total().toFixed(2) + ' €');

  addItem(): void {
    this.items.update(items => [...items, { description: '', quantity: 1, unitPrice: 0 }]);
  }

  removeItem(index: number): void {
    this.items.update(items => items.filter((_, i) => i !== index));
  }

  generateInvoice(): void {
    this.pdfService.generateInvoice({
      number: `F2024-${String(Date.now()).slice(-6)}`,
      date: new Date().toISOString().split('T')[0],
      items: this.items().filter(i => i.description.trim() !== ''),
      total: this.total()
    });
  }
}
```

### Ejemplo 3: Generar CSV desde datos de una tabla

**Objetivo**: Implementar la exportación de los datos mostrados en una tabla Angular a un archivo CSV descargable.

```typescript
import { Component, inject, signal } from '@angular/core';
import { CsvExportService } from '../../shared/services/csv-export.service';

interface Client {
  id: number;
  name: string;
  email: string;
  phone: string;
  city: string;
}

@Component({
  selector: 'app-clients-table',
  standalone: true,
  template: `
    <div class="p-6">
      <div class="flex justify-between mb-4">
        <h2 class="text-xl font-bold">Clientes</h2>
        <button (click)="exportCsv()"
                class="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700">
          Exportar CSV
        </button>
      </div>

      <table class="w-full border-collapse">
        <thead>
          <tr class="bg-gray-100">
            <th class="border p-2 text-left">Nombre</th>
            <th class="border p-2 text-left">Email</th>
            <th class="border p-2 text-left">Teléfono</th>
            <th class="border p-2 text-left">Ciudad</th>
          </tr>
        </thead>
        <tbody>
          <tr *ngFor="let client of clients()">
            <td class="border p-2">{{ client.name }}</td>
            <td class="border p-2">{{ client.email }}</td>
            <td class="border p-2">{{ client.phone }}</td>
            <td class="border p-2">{{ client.city }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  `
})
export class ClientsTableComponent {
  private readonly csvService = inject(CsvExportService);

  clients = signal<Client[]>([
    { id: 1, name: 'Ana García', email: 'ana@email.com', phone: '654321098', city: 'Sevilla' },
    { id: 2, name: 'Carlos Ruiz', email: 'carlos@email.com', phone: '612345678', city: 'Málaga' },
    { id: 3, name: 'Elena Martín', email: 'elena@email.com', phone: '698765432', city: 'Granada' },
    { id: 4, name: 'Miguel Sánchez', email: 'miguel@email.com', phone: '645678901', city: 'Córdoba' }
  ]);

  exportCsv(): void {
    this.csvService.exportToCsv(this.clients(), 'clientes', [
      { key: 'name', label: 'Nombre completo' },
      { key: 'email', label: 'Correo electrónico' },
      { key: 'phone', label: 'Teléfono' },
      { key: 'city', label: 'Ciudad' }
    ]);
  }
}
```

!!! example "Casos reales"

    ### Caso 1: Sistema de facturación de una asesoría andaluza

    Una asesoría fiscal en Sevilla necesita que su aplicación de gestión de clientes genere automáticamente facturas en **PDF** al cerrar cada servicio. Cada factura debe incluir el logo de la asesoría, los datos fiscales del cliente y de la asesoría, una tabla con los servicios prestados, el desglose de **IVA** (21% general y 10% reducido según el tipo de servicio), el total a pagar, los datos bancarios para la transferencia y un código QR con enlace de verificación de la factura en la sede electrónica. Además, al final de cada mes, la aplicación debe generar un archivo Excel con el listado de todas las facturas emitidas para el asesor contable.

    **Lecciones aprendidas**: La separación de la lógica de negocio (cálculo de impuestos) de la lógica de presentación (diseño del PDF) permite mantener el código mantenible. El servicio `PdfService` se amplió con un método `generateMonthlyReport()` que itera sobre todas las facturas del mes y genera un PDF resumen. Para los tipos de IVA variables, se implementó una función `getTaxRate(serviceType: string): number` que determina el tipo aplicable según el concepto.

    ### Caso 2: Plataforma de formación online en Granada

    Una academia de formación profesional en Granada necesita que su aplicación web genere diplomas y certificados de asistencia para los alumnos que completan cada curso. Cada diploma debe tener un diseño atractivo con los colores corporativos, el nombre del alumno, el nombre del curso, las horas de formación, la fecha de finalización y las firmas digitalizadas del director y del tutor. Además, cada diploma debe incluir un código de verificación único (**QR**) que enlace a una página pública donde cualquier persona pueda verificar la autenticidad del certificado.

    **Lecciones aprendidas**: Los diplomas se diseñaron como plantillas reutilizables en **PDFMake**, con el diseño artístico (bordes, colores de fondo, posición de las firmas) hardcodeado en la plantilla y los datos del alumno y del curso como parámetros variables. Se crearon 3 variantes de diseño de diploma para diferentes tipos de cursos (básico, avanzado y profesional). Las firmas de los profesores se almacenan como imágenes PNG con fondo transparente en base64. El código QR se genera con PDFMake usando la función `qr`.

    ### Caso 3: ERP de una distribuidora de productos ecológicos en Almería

    Una empresa distribuidora de productos ecológicos necesita que su ERP genere albaranes de entrega en PDF que los transportistas puedan imprimir en una impresora portátil desde su tablet. Los albaranes deben ser compactos (media página A5), sin elementos superfluos, con letra grande para facilitar la lectura a los clientes, e incluir una tabla con los productos entregados, cantidades y un espacio en blanco para la firma de conformidad del cliente. La aplicación está construida con Angular y se ejecuta en tablets con Android mediante una **PWA**.

    **Lecciones aprendidas**: Para albaranes en tablets, se configuró `pageSize: 'A5'` y márgenes reducidos. La tipografía se configuró con `fontSize: 12` para asegurar legibilidad. Se añadió un rectángulo vacío para la firma del cliente mediante el elemento `canvas`. La funcionalidad `print()` de PDFMake resultó especialmente útil, ya que los transportistas solo necesitan pulsar un botón para que el albarán se envíe directamente a la impresora Bluetooth/WiFi configurada en la tablet, sin necesidad de descargar un archivo intermedio.

## Actividades guiadas

### Actividad guiada 1: Mi primera factura en PDF

**Duración**: 45 minutos  
**Nivel**: Básico  
**Agrupamiento**: Individual

**Objetivo**: El alumnado generará su primer documento PDF desde una aplicación Angular, creando una factura sencilla con datos estáticos.

**Instrucciones**:

1. Clona el repositorio base proporcionado por el profesor, que contiene un proyecto Angular 18 standalone con Tailwind CSS configurado.
2. Instala **PDFMake**: `npm install pdfmake`.
3. Crea un servicio `FacturaService` en `src/app/shared/services/factura.service.ts` con el siguiente esqueleto:

```typescript
import { Injectable } from '@angular/core';
import pdfMake from 'pdfmake/build/pdfmake';
import pdfFonts from 'pdfmake/build/vfs_fonts';

@Injectable({ providedIn: 'root' })
export class FacturaService {
  constructor() {
    pdfMake.vfs = pdfFonts.vfs;
  }

  generarFactura(): void {
    // Completar aquí
  }
}
```

4. Dentro del método `generarFactura()`, define una definición de documento que incluya:
   - Título "FACTURA" centrado y en negrita.
   - Fecha de emisión y número de factura.
   - Una tabla con 3 columnas (Concepto, Cantidad, Precio) y 3 filas de datos inventados.
   - Total calculado manualmente al final de la tabla.
5. Configura el tamaño de página A4 y márgenes de 40 puntos a cada lado.
6. Llama a `pdfMake.createPdf(docDefinition).download('mi-factura.pdf')`.
7. Crea un componente `FacturaPage` con un botón que llame al servicio.
8. Verifica que al pulsar el botón se descarga el archivo `mi-factura.pdf`.
9. Abre el PDF y comprueba que todos los elementos se visualizan correctamente.

**Criterios de evaluación**:
- El PDF se genera y descarga correctamente.
- La factura contiene todos los elementos solicitados.
- El código está correctamente tipado con TypeScript.
- El servicio está correctamente inyectado en el componente.

### Actividad guiada 2: Exportación de datos a CSV y Excel

**Duración**: 45 minutos  
**Nivel**: Básico-Medio  
**Agrupamiento**: Parejas

**Objetivo**: Implementar las funcionalidades de exportación de datos tabulares a CSV y Excel desde una tabla de datos en Angular.

**Instrucciones**:

1. Partiendo del proyecto de la actividad anterior, crea un array de 10 objetos con datos de productos: `[{ id, nombre, categoria, precio, stock }]`.
2. Muestra estos datos en una tabla HTML en un nuevo componente `ProductosPage`.
3. Crea un servicio `ExportService` con dos métodos: `exportarCsv(datos, nombreArchivo)` y `exportarExcel(datos, nombreArchivo)`.
4. Implementa `exportarCsv`:
   - Genera una cadena CSV con BOM UTF-8 al inicio (`\uFEFF`).
   - Usa punto y coma (`;`) como separador para compatibilidad con Excel en España.
   - Escapa correctamente los valores que contengan comillas o saltos de línea.
   - Crea un Blob con tipo MIME `text/csv;charset=utf-8;`.
   - Descarga el archivo usando `URL.createObjectURL` y un enlace temporal.
5. Instala **SheetJS**: `npm install xlsx`. Implementa `exportarExcel`:
   - Crea un workbook con `XLSX.utils.book_new()`.
   - Convierte los datos a hoja con `XLSX.utils.json_to_sheet()`.
   - Añade la hoja al workbook con `XLSX.utils.book_append_sheet()`.
   - Ajusta los anchos de columna basándote en la longitud de los datos.
   - Genera el binario XLSX con `XLSX.write()` y descarga como Blob.
6. Añade dos botones en `ProductosPage`: "Exportar CSV" y "Exportar Excel".
7. Verifica que ambos archivos se descargan correctamente y que Excel/Calc los abre sin problemas de codificación.

**Criterios de evaluación**:
- El CSV se genera con codificación UTF-8 correcta (las tildes y eñes se ven bien).
- El Excel se abre correctamente con las columnas adecuadamente dimensionadas.
- El servicio separa correctamente las responsabilidades de exportación.

### Actividad guiada 3: Factura profesional con estilos corporativos

**Duración**: 60 minutos  
**Nivel**: Medio  
**Agrupamiento**: Parejas

**Objetivo**: Mejorar la factura generada en la actividad 1 aplicando estilos corporativos avanzados, imágenes de logo, cabecera y pie de página, y cálculos de IVA.

**Instrucciones**:

1. Busca un logo de empresa (puede ser uno inventado) y conviértelo a base64. Puedes usar un conversor online o escribir una pequeña función en TypeScript.
2. Modifica el servicio `FacturaService` de la actividad 1 para que acepte datos dinámicos mediante un parámetro de tipo `InvoiceData`.
3. Define la interfaz `InvoiceData` con los siguientes campos:
   ```typescript
   interface InvoiceData {
     numero: string;
     fecha: Date;
     empresa: { nombre: string; cif: string; direccion: string; logoBase64: string };
     cliente: { nombre: string; nif: string; direccion: string };
     lineas: { concepto: string; cantidad: number; precioUnitario: number; iva: number }[];
   }
   ```
4. Implementa una cabecera que se repita en cada página con el logo (imagen base64) a la izquierda y los datos de la empresa a la derecha.
5. Implementa un pie de página que muestre el número de factura a la izquierda y la numeración de página (`Página X de Y`) a la derecha.
6. Diseña una paleta de colores corporativos y defínela como estilos en el documento (usa al menos 4 estilos con nombre).
7. Implementa el cálculo automático de:
   - Base imponible (suma de todas las líneas sin IVA).
   - Cuota de IVA (suma del IVA de cada línea, calculado como `cantidad * precioUnitario * iva / 100`).
   - Total (base imponible + cuota de IVA).
8. Formatea todos los importes en euros usando `Intl.NumberFormat` con `style: 'currency'` y `currency: 'EUR'`.
9. Añade un código QR en la esquina inferior derecha.
10. Crea una vista previa que abra el PDF en una nueva pestaña antes de descargar, añadiendo un botón "Vista previa" junto al botón "Descargar".

**Criterios de evaluación**:
- La factura tiene apariencia profesional con colores corporativos coherentes.
- La cabecera y el pie se repiten correctamente en todas las páginas (probar con suficientes líneas de factura para que ocupe más de una página).
- Los cálculos de IVA y totales son correctos.
- Los importes se muestran formateados en euros con dos decimales.

## Actividades propuestas

### Actividad propuesta 1: Sistema de informes de ventas con gráficos (Dificultad: Alta)

Desarrolla un componente Angular y un servicio PDF capaces de generar un informe completo de ventas que incluya:

1. Una portada con título, logotipo de la empresa, fecha y nombre del autor.
2. Un índice de contenidos generado dinámicamente a partir de las secciones del informe.
3. Al menos dos gráficos exportados desde **Chart.js** como imágenes base64 e incrustados en el PDF:
   - Un gráfico de barras con las ventas de los 5 productos más vendidos del mes.
   - Un gráfico circular con la distribución de ventas por categoría de producto.
4. Tablas de datos con al menos 20 filas, incluyendo formato condicional (resaltar productos con stock bajo en rojo, productos más vendidos en verde).
5. Un apartado de "Conclusiones" con texto formateado.
6. Numeración de páginas y encabezados de sección.

### Actividad propuesta 2: Generador de certificados de asistencia (Dificultad: Media)

Crea una aplicación Angular que permita generar certificados de asistencia a un evento formativo:

1. Crea un formulario reactivo con los siguientes campos: nombre del asistente, DNI, nombre del evento, fecha de inicio, fecha de fin, número de horas, nombre del formador, nombre del responsable del centro.
2. Diseña un certificado con bordes decorativos (usando los elementos `canvas` y `rect` de PDFMake), colores institucionales de la Junta de Andalucía (verde #007A33 y blanco), y tipografía elegante.
3. Incluye espacios para dos firmas: la del formador y la del responsable del centro (usa imágenes base64 de firmas de ejemplo).
4. Genera un código de verificación alfanumérico único de 10 caracteres y muéstralo como texto y como código QR en el PDF.
5. Permite generar el certificado para un único asistente o en lote (múltiples certificados en un solo PDF con salto de página entre cada uno).

### Actividad propuesta 3: Exportador universal de datos (Dificultad: Media)

Desarrolla un componente `DataExporter` reutilizable que, dado cualquier conjunto de datos tabulares, ofrezca exportación en 3 formatos (PDF, CSV, Excel):

1. Crea una interfaz `ExportableData` que defina la estructura que debe tener cualquier dato para ser exportable.
2. El componente debe recibir los datos como `@Input()`, las columnas a mostrar como configuración, y opcionalmente un título.
3. Para la exportación PDF: genera una tabla simple con los datos y el título como encabezado.
4. Para la exportación CSV: usa el servicio creado anteriormente.
5. Para la exportación Excel: usa el servicio creado anteriormente.
6. Incluye un selector de formato (radio buttons o dropdown) y un solo botón "Exportar".
7. Añade un indicador de carga mientras se genera el archivo (especialmente para conjuntos de datos grandes, más de 1000 filas).
8. Documenta el componente para que cualquier compañero pueda reutilizarlo en su proyecto.

### Actividad propuesta 4: Manipulación de PDFs con PDF-LIB (Dificultad: Alta)

Investiga e implementa un caso de uso real con PDF-LIB:

1. Descarga de internet un formulario PDF oficial (por ejemplo, el modelo 036 de la Agencia Tributaria o una solicitud genérica).
2. Carga el PDF en tu aplicación Angular como un ArrayBuffer.
3. Utiliza PDF-LIB para rellenar los campos del formulario con los datos introducidos por el usuario en un formulario Angular.
4. Implementa también la funcionalidad de combinar (merge) dos PDFs en uno solo: por ejemplo, junta la portada de un informe con el cuerpo del informe.
5. Permite al usuario descargar el PDF resultante.
6. Explica en un breve documento las diferencias prácticas que has encontrado entre PDF-LIB y PDFMake y en qué casos usarías cada una.

### Actividad propuesta 5: Dashboard exportable (Dificultad: Alta)

Crea un mini-dashboard en Angular que muestre indicadores de negocio y permita exportarlos:

1. Diseña un dashboard con 4 tarjetas KPI (ingresos totales, número de pedidos, ticket medio, clientes nuevos) y 2 gráficos (líneas y barras) usando **Chart.js**.
2. Implementa un botón "Exportar informe" que genere un PDF de 1 página conteniendo:
   - Las 4 tarjetas KPI en una fila de 4 columnas de igual ancho.
   - Los 2 gráficos exportados como imágenes (usa `chart.toBase64Image()`).
   - Una tabla resumen con los datos subyacentes.
3. Para obtener las imágenes de los gráficos, necesitarás acceder a la instancia de Chart.js y llamar a `toBase64Image()`. Implementa un mecanismo para esperar a que todos los gráficos estén renderizados antes de generar el PDF.
4. Añade también botones para exportar solo los datos a CSV y Excel.
5. Aplica un diseño visual coherente entre la versión web del dashboard y la versión PDF exportada.

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Sistema de plantillas dinámicas (Dificultad: Alta)

    Desarrolla un sistema que permita a los usuarios administradores de la aplicación definir y modificar plantillas de documentos **PDF** sin necesidad de tocar el código fuente. Investiga y diseña:

    1. Una interfaz de administración donde el administrador pueda arrastrar y soltar elementos (cuadros de texto, imágenes, tablas, códigos QR) sobre un lienzo que representa una página A4.
    2. Un formato JSON para serializar/deserializar las plantillas (similar a la definición de documento de PDFMake pero más abstracto).
    3. Placeholders para datos dinámicos (`{{cliente.nombre}}`, `{{factura.total}}`) que se sustituyan en tiempo de generación.
    4. Una vista previa en tiempo real de la plantilla con datos de ejemplo.
    5. Almacenamiento de las plantillas en el backend (API REST con base de datos).

    ### Actividad de ampliación 2: Firma digital de documentos PDF (Dificultad: Alta)

    Investiga los conceptos de firma digital y aplica un mecanismo básico de firma de documentos PDF:

    1. Estudia el concepto de firma digital, certificados digitales y **PKI (Public Key Infrastructure)**.
    2. Investiga las limitaciones de las librerías JavaScript cliente para firmar digitalmente PDFs (las firmas digitales requieren acceso a claves privadas, lo cual es problemático en el navegador).
    3. Implementa una solución híbrida: el cliente genera el PDF con PDFMake/PDF-LIB, lo envía a un servidor Node.js que utiliza `node-signpdf` para firmarlo digitalmente con un certificado de prueba autofirmado, y devuelve el PDF firmado al cliente.
    4. Añade una marca visual de firma (un recuadro con nombre, fecha y sello) en el PDF, aunque la firma criptográfica se haga en el servidor.
    5. Documenta el flujo completo y las decisiones técnicas tomadas.

    ### Actividad de ampliación 3: Generación de documentos multilingües (Dificultad: Media)

    Extiende el `PdfService` para soportar generación de documentos en múltiples idiomas:

    1. Implementa un sistema de traducción para los textos estáticos de las plantillas (títulos, encabezados de tabla, pies de página, textos legales).
    2. Utiliza la API de internacionalización de Angular (**i18n**) o crea un sistema propio de diccionarios (`es.json`, `en.json`, `fr.json`, `de.json`).
    3. El idioma del documento se selecciona en un dropdown en la interfaz de usuario.
    4. Asegúrate de que los formatos de fecha, moneda y números se adaptan al idioma seleccionado (ej: `1,234.56` en inglés vs `1.234,56` en español).
    5. Prueba con al menos 3 idiomas (español, inglés y francés o alemán).
    6. Ten en cuenta la dirección del texto (LTR vs RTL) si se añadieran idiomas como árabe o hebreo.

!!! tip "Buenas prácticas"

    1. **Separación de responsabilidades**: Mantén la lógica de negocio (cálculos, formateo de datos) separada de la lógica de presentación (definición del documento PDFMake). Las plantillas deben ser funciones puras que reciben datos y devuelven una definición de documento. Esto facilita el testing unitario y la reutilización.

    2. **Tipado estricto con TypeScript**: Define interfaces para todos los datos que alimentan los documentos. No uses `any` en las definiciones de PDFMake. Utiliza la interfaz `TDocumentDefinitions` proporcionada por pdfmake/interfaces para asegurar que la definición del documento es correcta.

    3. **Carga lazy de librerías pesadas**: PDFMake, jsPDF y SheetJS son librerías que añaden un peso considerable al bundle de la aplicación. Configura la carga lazy (import dinámico) para que solo se carguen cuando el usuario realmente vaya a generar un documento, no en la carga inicial de la aplicación.

    4. **Manejo de errores robusto**: Las operaciones de generación de documentos pueden fallar por múltiples razones: datos incorrectos, imágenes que no cargan, errores en las librerías, memoria insuficiente en el navegador. Envuelve siempre las llamadas a PDFMake en bloques try-catch y proporciona retroalimentación al usuario mediante toasts o alertas en caso de error.

    5. **Previsualización antes de descargar**: Ofrece siempre la opción de vista previa (método `open()`) además de la descarga directa. Esto permite al usuario verificar el documento antes de guardarlo en su disco duro y reduce la frustración por errores en el documento.

    6. **Nombres de archivo significativos**: Genera nombres de archivo que incluyan información relevante para el usuario: `Factura_F2024-0001_20241115.pdf` en lugar de `documento.pdf`. Esto facilita la organización de archivos al usuario.

    7. **Formateo consistente de datos**: Centraliza el formateo de fechas, monedas y números en funciones auxiliares reutilizables. Utiliza la API `Intl` de JavaScript (`Intl.DateTimeFormat`, `Intl.NumberFormat`) para garantizar formatos localizados correctos.

    8. **Optimización de imágenes**: Antes de incrustar una imagen en un PDF, redimensiónala al tamaño necesario. Incrustar una imagen de 4000x3000 píxeles para mostrarla como un logo de 150x50 píxeles malgasta memoria y aumenta el tamaño del PDF innecesariamente.

    9. **Accesibilidad en PDFs**: Aunque PDFMake no genera PDFs con metadatos de accesibilidad (PDF/UA), se pueden tomar medidas básicas: usar tamaños de fuente legibles (mínimo 8pt), suficiente contraste de color, y estructura lógica del documento con encabezados jerárquicos.

    10. **Prueba en múltiples visores de PDF**: Los PDFs pueden visualizarse de forma ligeramente diferente según el visor utilizado (Adobe Acrobat, Chrome PDF Viewer, Firefox PDF.js, SumatraPDF, vista previa de macOS, visor de Android/iOS). Prueba los documentos generados en al menos 3 visores diferentes.

    11. **Versionado de plantillas**: Si las plantillas de documentos evolucionan con el tiempo (cambio de logo, de datos fiscales, de diseño), implementa un sistema de versionado para que los documentos antiguos puedan regenerarse con la plantilla correcta si es necesario.

    12. **Internacionalización de los PDFs**: Si la aplicación está disponible en varios idiomas, las plantillas de documentos también deben estarlo. Utiliza el mismo sistema de traducción que uses para la interfaz web, o crea plantillas específicas por idioma.

!!! warning "Errores frecuentes"

    1. **No inicializar PDFMake correctamente**: Olvidar la línea `pdfMake.vfs = pdfFonts.vfs;` es el error más común. Sin esta inicialización, PDFMake lanzará errores de "fuente no encontrada" al intentar renderizar cualquier texto. La solución es ejecutar esta línea una sola vez en el constructor del servicio PDF.

    2. **Problemas con caracteres especiales (tildes, eñes, caracteres acentuados)**: Las fuentes por defecto de PDFMake (Roboto) soportan perfectamente los caracteres del español y la mayoría de los idiomas europeos. Sin embargo, si se usan fuentes personalizadas, es necesario asegurarse de que incluyan los glifos necesarios. Si se ven cuadrados en lugar de tildes, la fuente no incluye esos caracteres.

    3. **Uso incorrecto de márgenes en tablas**: Los márgenes en las celdas de las tablas se controlan mediante el layout de la tabla, no mediante la propiedad `margin` de cada celda (que PDFMake ignora en tablas). Para cambiar el padding de las celdas, hay que configurar `paddingLeft`, `paddingRight`, `paddingTop` y `paddingBottom` en el layout de la tabla.

    4. **Imágenes que no se muestran**: Las imágenes en PDFMake deben estar en formato data URL (base64) o referenciadas en el diccionario `images`. Si se pasa una URL HTTP directamente, PDFMake no la cargará automáticamente. Es necesario precargar la imagen (con fetch), convertirla a base64 y luego usarla en el documento.

    5. **Desbordamiento de tablas fuera de la página**: Si una tabla tiene columnas con anchos fijos que suman más que el ancho disponible de la página (A4 con márgenes de 40: ancho útil ≈ 515 puntos), el contenido se saldrá de la página. Utiliza siempre al menos una columna con ancho `'*'` para absorber las diferencias de dimensionamiento.

    6. **Ignorar el BOM en la exportación CSV**: Al exportar CSV sin el BOM (Byte Order Mark `\uFEFF`), Excel abrirá el archivo asumiendo codificación Windows-1252 y los caracteres UTF-8 (tildes, eñes) se mostrarán como caracteres extraños. Siempre inicia el contenido CSV con `\uFEFF`.

    7. **No escapar correctamente los valores CSV**: Si un valor contiene el carácter separador (coma, punto y coma) o comillas dobles, debe encerrarse entre comillas dobles y las comillas dobles internas deben duplicarse. Ejemplo: `Juan "El Rápido" García, S.L.` → `"Juan ""El Rápido"" García, S.L."`.

    8. **Crear múltiples instancias de servicios de exportación**: Los servicios de exportación (PdfService, CsvExportService, ExcelExportService) deben ser singletons proporcionados en `root`. Crear una instancia nueva en cada componente malgasta memoria y puede causar problemas con las fuentes de PDFMake (que se configuran en el constructor).

    9. **Generar PDFs con datos no validados**: Si los datos que alimentan el PDF no están validados previamente (por ejemplo, un importe negativo, un texto vacío en un campo obligatorio, una fecha inválida), el PDF se generará con errores que el usuario solo descubrirá al abrirlo. Valida siempre los datos antes de pasarlos al generador de PDFs.

    10. **No destruir los Blob URLs**: Después de descargar un archivo mediante `URL.createObjectURL()` y un enlace temporal, es necesario llamar a `URL.revokeObjectURL(url)` para liberar la memoria. De lo contrario, cada descarga acumulará referencias en memoria y eventualmente degradará el rendimiento de la aplicación.

    11. **Confundir `open()` y `download()`**: `open()` abre el PDF en una nueva pestaña del navegador (lo que permite al usuario revisarlo y luego decidir si guardarlo o no). `download()` fuerza la descarga inmediata sin previsualización. Usar `open()` para vista previa y `download()` para descarga directa, o mejor aún, ofrecer ambas opciones.

    12. **No considerar el tiempo de carga de imágenes remotas**: Si el documento incluye imágenes obtenidas de URLs remotas (logos, firmas, etc.), la generación del PDF debe esperar a que todas las imágenes se hayan cargado y convertido a base64. Utiliza `Promise.all()` para paralelizar la carga y muestra un indicador de carga mientras tanto.

!!! abstract "Resumen"

    La generación de informes y documentos es una capacidad esencial de cualquier aplicación empresarial moderna. Esta unidad ha cubierto de forma integral todos los aspectos necesarios para que el alumnado sea capaz de implementar esta funcionalidad en aplicaciones Angular.

    Hemos comenzado comprendiendo la necesidad de negocio que subyace a la generación de documentos —facturas, informes, certificados y más— y los requisitos legales que afectan a ciertos tipos de documentos en el contexto español. La decisión arquitectónica entre generar documentos en el **cliente** (navegador) o en el **servidor** es crucial y depende de factores como el volumen de páginas, la concurrencia de usuarios, los requisitos de seguridad y la necesidad de funcionamiento offline.

    La librería **PDFMake** se ha presentado como la herramienta principal para la generación de PDFs en Angular, gracias a su enfoque declarativo, su facilidad de uso y su potencia para la mayoría de los casos de uso empresarial. Se ha explorado en profundidad su API: estructura del documento, elementos de contenido (texto, columnas, tablas, imágenes, stacks, listas, saltos de página, líneas, códigos QR), sistema de estilos, personalización de fuentes y métodos de salida (download, open, print, getBlob).

    Como alternativas, se han presentado **jsPDF** (enfoque imperativo con control fino de coordenadas, ideal para formularios oficiales y gráficos vectoriales) y **PDF-LIB** (manipulación de PDFs existentes, relleno de formularios, fusión de documentos), con criterios claros para elegir entre ellas según el caso de uso.

    Los tres casos prácticos completos —factura profesional, informe de ventas con gráficos, y certificado/diploma— constituyen el núcleo práctico de la unidad y demuestran cómo integrar todos los conceptos en código TypeScript real y funcional dentro de una arquitectura Angular limpia y mantenible.

    La arquitectura recomendada propone un `PdfService` centralizado, interfaces `DocumentGenerator` para estandarizar la generación de documentos, componentes opcionales de vista previa y plantillas tipadas como funciones puras, siguiendo los principios **SOLID** y facilitando el testing y la extensibilidad.

    La exportación de datos en formatos alternativos —**CSV** (con manejo de codificación UTF-8/BOM) y **Excel** (SheetJS/xlsx)— completa las capacidades de generación de documentos, permitiendo a los usuarios trabajar con los datos en las herramientas que prefieran.

    Finalmente, las buenas prácticas y los errores frecuentes recogidos al final de la unidad sintetizan la experiencia acumulada en proyectos reales y proporcionan al alumnado una guía práctica para evitar los tropiezos más comunes en la implementación de sistemas de generación de documentos.

## Recursos complementarios

### Documentación oficial

- **PDFMake - Documentación oficial**: https://pdfmake.github.io/docs/
- **PDFMake - Playground interactivo**: http://pdfmake.org/playground.html
- **jsPDF - Documentación oficial**: https://raw.githack.com/MrRio/jsPDF/master/docs/
- **jsPDF-AutoTable - Documentación**: https://github.com/simonbengtsson/jsPDF-AutoTable
- **PDF-LIB - Documentación oficial**: https://pdf-lib.js.org/
- **SheetJS (xlsx) - Documentación oficial**: https://docs.sheetjs.com/

### Tutoriales y cursos

- **Video: "Generación de PDFs con Angular y PDFMake"** (canal de YouTube "DominiCode")
- **Tutorial: "Export Data to CSV in Angular"** (blog "Angular University")
- **Curso: "Angular Material Data Table with Export"** (Angular University)

### Herramientas

- **Conversor de imágenes a base64**: https://www.base64-image.de/
- **Conversor de fuentes TTF a base64 para PDFMake vfs**: https://pdfmakeutils.herokuapp.com/
- **Visor PDF online para pruebas**: https://www.pdfescape.com/
- **Generador de plantillas PDFMake visual**: http://pdfmake.org/playground.html

### Ejemplos de código

- **Repositorio GitHub con ejemplos PDFMake + Angular**: buscar "angular pdfmake invoice example" en GitHub.
- **Stack Overflow**: Etiquetas `[pdfmake]`, `[jspdf]`, `[angular]` para consultas de la comunidad.

### Referencias legales (España)

- **Real Decreto 1619/2012, de 30 de noviembre**, por el que se aprueba el Reglamento por el que se regulan las obligaciones de facturación (BOE núm. 289, de 1 de diciembre de 2012).
- **Ley 25/2013, de 27 de diciembre**, de impulso de la factura electrónica y creación del registro contable de facturas en el Sector Público (BOE núm. 311, de 28 de diciembre de 2013).
- **Guía de factura electrónica de la Agencia Tributaria**: https://www.agenciatributaria.es/
