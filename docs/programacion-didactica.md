# Programación Didáctica: Desarrollo de Interfaces (2º DAM)
**Curso Académico: 2025/2026**  
**Ciclo Formativo:** Grado Superior en Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Módulo Profesional:** Desarrollo de Interfaces (Código: 0488)  
**Comunidad Autónoma:** Andalucía  

---

## 1. Introducción y Justificación del Módulo

El módulo profesional de **Desarrollo de Interfaces** (Código 0488) es una materia fundamental en el 2º curso del Ciclo Formativo de Grado Superior de **Desarrollo de Aplicaciones Multiplataforma (DAM)**. Su objetivo principal es dotar al alumnado de las competencias necesarias para concebir, diseñar, implementar, documentar, probar y distribuir interfaces de usuario modernas, intuitivas, accesibles y multidispositivo (escritorio con Electron/Angular, web apps y entornos interactivos basados en interfaces naturales NUI/voz/gestos).

El enfoque pedagógico sitúa al usuario en el centro del diseño (**User-Centered Design & UX**), combinando herramientas de prototipado y diseño en alta fidelidad (**Figma**), frameworks de diseño atómico y utilidades (**Tailwind CSS v4**), arquitecturas avanzadas de componentes desacoplados (**Angular 19+** con Standalone Components, Signals y Storybook), librerías de generación y exportación de informes (**jsPDF, SheetJS, Chart.js**), automatización de pruebas (**Vitest, Playwright/Cypress**) y empaquetado nativo multiplataforma (**Electron, Electron Forge/Builder, MSIX/AppImage**).

---

## 2. Marco Normativo de Referencia

La presente programación didáctica se fundamenta y adecúa estrictamente a la normativa estatal y autonómica vigente:

### 2.1. Normativa Estatal
1. **Ley Orgánica 3/2022, de 31 de marzo**, de ordenación e integración de la Formación Profesional.
2. **Real Decreto 659/2023, de 18 de julio**, por el que se desarrolla la ordenación del Sistema de Formación Profesional.
3. **Real Decreto 405/2023, de 29 de mayo**, por el que se actualizan los títulos de la formación profesional del sistema educativo (entre ellos DAM) y se fijan sus enseñanzas mínimas.
4. **Real Decreto 500/2024, de 21 de mayo**, por el que se modifican determinados reales decretos de títulos de Formación Profesional para adaptar currículos y marcos de competencias.
5. **Real Decreto 1112/2018, de 7 de septiembre**, sobre accesibilidad de los sitios web y aplicaciones para dispositivos móviles.
6. **Ley 11/2023, de 8 de mayo**, de trasposición de Directivas de la Unión Europea en materia de accesibilidad de determinados productos y servicios (Directiva Europea de Accesibilidad).
7. **Ley Orgánica 3/2018 (LOPDGDD)** y **Reglamento (UE) 2016/679 (RGPD)** sobre protección de datos y privacidad en interfaces y formularios.

### 2.2. Normativa Autonómica de Andalucía
1. **Decreto 104/2024, de 28 de mayo**, por el que se establece la ordenación del Sistema de Formación Profesional en la Comunidad Autónoma de Andalucía (deroga el Decreto 436/2008).
2. **Orden de 16 de junio de 2011**, por la que se desarrolla el currículo correspondiente al título de Técnico Superior en Desarrollo de Aplicaciones Multiplataforma en Andalucía.
3. **Orden de 18 de septiembre de 2025**, por la que se regula la evaluación y acreditación del aprendizaje del alumnado de Formación Profesional en Andalucía.
4. **Orden de 26 de septiembre de 2025**, por la que se regulan los periodos de formación en empresas y la modalidad Dual en Andalucía.

---

## 3. Carga Horaria, Calendario y Modalidad Dual

De acuerdo con el Decreto 104/2024 y la ordenación de 2º curso de Grado Superior en Andalucía:

- **Carga horaria total del módulo:** 210 horas.
- **Distribución lectiva semanal:** 6 horas/semana.
- **Periodo en Centro Educativo (Trimestres 1 y 2):** ~124 horas lectivas (septiembre a marzo).
- **Fase de Formación Dual en Empresa (Trimestre 3):** ~86 horas del módulo integradas en la estancia en empresa (que completa las 400 horas duales de 2º curso de marzo a junio).

| Fase | Periodo | Horas Módulo | Actividades Principales |
| :--- | :--- | :---: | :--- |
| **Fase Centro (T1 y T2)** | Septiembre - Marzo | 124 h | Clases teórico-prácticas, retos y desarrollo del proyecto GesFlow. |
| **Fase Dual Empresa (T3)** | Marzo - Junio | 86 h | Prácticas profesionales en empresas de desarrollo de software multiplataforma. |
| **Total Módulo** | Curso 2025/2026 | **210 h** | Adquisición plena de las competencias profesionales del módulo. |

---

## 4. Resultados de Aprendizaje (RA) y Criterios de Evaluación (CE)

El módulo consta de **8 Resultados de Aprendizaje** oficiales, con las ponderaciones asignadas en función de su impacto competencial:

### RA1: Confecciona interfaces de usuario gráficas identificando y aplicando la metodología del diseño de interfaces (22%)
- **CE1.a:** Se han identificado los elementos que componen la interfaz gráfica.
- **CE1.b:** Se han analizado los principios de usabilidad y diseño centrado en el usuario (UX).
- **CE1.c:** Se han elaborado bocetos, wireframes y prototipos interactivos en alta fidelidad (Figma).
- **CE1.d:** Se han aplicado guías de estilo, tipografías, colores, espaciados y sistemas de diseño (Design Tokens).
- **CE1.e:** Se han diseñado layouts modernos y adaptables a diferentes resoluciones y dispositivos (CSS Grid, Flexbox, Tailwind CSS v4).
- **CE1.f:** Se ha verificado la correcta interacción y flujo de navegación entre pantallas.

### RA2: Confecciona interfaces de usuario utilizando interfaces naturales (NUI, voz, gestos, visión) y tecnologías emergentes (16%)
- **CE2.a:** Se han identificado los conceptos, arquitecturas y hardware de interfaces naturales (NUI).
- **CE2.b:** Se han integrado librerías y APIs de reconocimiento de voz y síntesis de voz (Web Speech API / SpeechRecognition).
- **CE2.c:** Se han implementado controles basados en visión artificial y tracking de gestos/manos (MediaPipe, Handpose).
- **CE2.d:** Se han explorado y aplicado patrones de realidad aumentada y experiencias inmersivas básicas (WebXR, Three.js).
- **CE2.e:** Se han evaluado las ventajas y barreras de accesibilidad de las interfaces conversacionales y gestuales.

### RA3: Crea componentes visuales estándar y personalizados reutilizables integrándolos en librerías y aplicaciones (20%)
- **CE3.a:** Se ha seleccionado el framework y entorno de desarrollo de componentes (Angular 19+ Standalone).
- **CE3.b:** Se han diseñado componentes reutilizables aplicando atomic design (átomos, moléculas, organismos).
- **CE3.c:** Se ha gestionado el estado reactivo y la comunicación entre componentes (Input/Output signals, RxJS/State).
- **CE3.d:** Se han integrado directivas, pipes personalizados y servicios de inyección de dependencias.
- **CE3.e:** Se ha documentado e interactuado con la librería de componentes mediante catálogos interactivos (Storybook).
- **CE3.f:** Se han creado formularios reactivos con validaciones asíncronas y accesibles.

### RA4: Diseña interfaces amigables y accesibles verificando el cumplimiento de estándares y normativas (11%)
- **CE4.a:** Se han analizado las pautas WCAG 2.2 en niveles A, AA y AAA.
- **CE4.b:** Se han verificado atributos semánticos WAI-ARIA (roles, states, properties, live regions).
- **CE4.c:** Se ha asegurado la navegación completa por teclado, focos visibles y ratios de contraste de color.
- **CE4.d:** Se han ejecutado auditorías automáticas de accesibilidad con herramientas especializadas (Axe Core, Lighthouse).
- **CE4.e:** Se han realizado pruebas de compatibilidad con lectores de pantalla (NVDA, VoiceOver).

### RA5: Crea informes y cuadros de mando interactivos integrando fuentes de datos y elementos gráficos (4%)
- **CE5.a:** Se han seleccionado herramientas y librerías de generación de documentos e informes (jsPDF, SheetJS/XLSX).
- **CE5.b:** Se han diseñado plantillas de informes estructurados con encabezados, tablas y paginación.
- **CE5.c:** Se han creado cuadros de mando (Dashboards) interactivos con visualización de datos (Chart.js / ng2-charts).
- **CE5.d:** Se han implementado funciones de filtrado dinámico y exportación masiva en formatos estándar (PDF, Excel, CSV, JSON).

### RA6: Elabora la documentación técnica y de usuario de la interfaz facilitando su mantenimiento y uso (7%)
- **CE6.a:** Se han identificado los destinatarios y requisitos de la documentación técnica y manuales de usuario.
- **CE6.b:** Se han generado esquemas, diagramas de flujo y arquitectura de la interfaz.
- **CE6.c:** Se ha automatizado la generación de documentación de código y componentes (Compodoc, Typedoc).
- **CE6.d:** Se han redactado guías de estilo, manuales de usuario interactivos y sistemas de ayuda en línea (Zensical / Markdown).

### RA7: Prepara aplicaciones para su distribución empaquetando componentes, instaladores y dependencias multiplataforma (10%)
- **CE7.a:** Se han identificado los entornos de ejecución y plataformas de destino (Windows, macOS, Linux).
- **CE7.b:** Se ha integrado la aplicación Angular en un contenedor de escritorio mediante Electron.
- **CE7.c:** Se ha configurado la comunicación segura entre procesos (IPC Main y IPC Renderer con Preload Scripts y Context Isolation).
- **CE7.d:** Se han generado paquetes e instaladores distribuidos (Electron Forge / Builder, MSIX, NSIS, AppImage).
- **CE7.e:** Se han configurado actualizaciones automáticas y firmas digitales de ejecutables.

### RA8: Realiza pruebas unitarias, de integración y extremo a extremo en interfaces evaluando su rendimiento y robustez (10%)
- **CE8.a:** Se ha planificado la estrategia de pruebas de la interfaz de usuario.
- **CE8.b:** Se han implementado pruebas unitarias de componentes y servicios (Vitest / Jasmine).
- **CE8.c:** Se han realizado pruebas de integración y simulación de eventos de usuario (Testing Library).
- **CE8.d:** Se han automatizado pruebas End-to-End (E2E) de flujos críticos (Playwright / Cypress).
- **CE8.e:** Se han medido métricas de rendimiento, tiempos de renderizado y Core Web Vitals.

---

## 5. Organización de Unidades Didácticas y Materiales

Los contenidos se articulan en **23 Unidades Didácticas** organizadas en 4 bloques temáticos, vinculadas directamente a los materiales preparados en el repositorio:

```
docs/
├── 01-ux.md
├── 02-accesibilidad.md
├── 03-interfaces-naturales.md
├── 04-figma.md
├── 05-layouts-modernos.md
├── 06-tailwindcss4.md
├── 07-componentes-tailwind.md
├── 08-responsive-design.md
├── 09-ecosistema-frontend.md
├── 10-arquitectura-angular.md
├── 11-componentes-reutilizables.md
├── 12-formularios-interaccion.md
├── 13-design-systems.md
├── 14-storybook.md
├── 15-diseno-a-implementacion.md
├── 16-generacion-informes.md
├── 17-dashboards-exportacion-datos.md
├── 18-documentacion-aplicaciones.md
├── 19-pruebas-de-software.md
├── 20-electron.md
├── 21-empaquetado-distribucion.md
├── 22-proyecto-final.md
└── index.md
```

### Tabla de Unidades Didácticas, RAs y Temporalización

| Ud. | Título de la Unidad | Archivo de Materiales | RAs Asociados | Horas Centro | Trimestre |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **UD00** | Introducción a Interfaces Multiplataforma | `index.md` | RA1 | 4 h | T1 |
| **UD01** | Fundamentos de UX y Diseño Centrado en Usuario | `01-ux.md` | RA1 | 6 h | T1 |
| **UD02** | Accesibilidad Web y Universal (WCAG 2.2, WAI-ARIA) | `02-accesibilidad.md` | RA4 | 6 h | T1 |
| **UD03** | Interfaces Naturales de Usuario (NUI, Voz, Gestos) | `03-interfaces-naturales.md` | RA2 | 8 h | T1 |
| **UD04** | Prototipado y Wireframing en Alta Fidelidad con Figma | `04-figma.md` | RA1 | 8 h | T1 |
| **UD05** | Layouts Modernos: Flexbox, CSS Grid y Subgrid | `05-layouts-modernos.md` | RA1 | 6 h | T1 |
| **UD06** | Tailwind CSS v4: Arquitectura y Utilidades | `06-tailwindcss4.md` | RA1 | 6 h | T1 |
| **UD07** | Creación de Componentes Estilizados con Tailwind | `07-componentes-tailwind.md` | RA1, RA3 | 6 h | T1 |
| **UD08** | Diseño Adaptativo y Responsive Design | `08-responsive-design.md` | RA1, RA4 | 6 h | T1 |
| **UD09** | Ecosistema Frontend: Node, npm, Vite y TypeScript | `09-ecosistema-frontend.md` | RA3 | 4 h | T1 |
| **UD10** | Arquitectura Angular: Standalone, Signals y Control Flow | `10-arquitectura-angular.md` | RA3 | 8 h | T1 |
| **UD11** | Componentes Reutilizables en Angular | `11-componentes-reutilizables.md` | RA3 | 8 h | T1 |
| **UD12** | Formularios Reactivos y Manejo de Interacción | `12-formularios-interaccion.md` | RA3, RA4 | 8 h | T2 |
| **UD13** | Design Systems y Atomic Design | `13-design-systems.md` | RA1, RA3 | 6 h | T2 |
| **UD14** | Catálogo Interactivo y Aislamiento con Storybook | `14-storybook.md` | RA3, RA6 | 6 h | T2 |
| **UD15** | De Diseño a Implementación (Figma to Code) | `15-diseno-a-implementacion.md` | RA1, RA3 | 6 h | T2 |
| **UD16** | Generación de Informes y Documentos (jsPDF, PDFMake) | `16-generacion-informes.md` | RA5 | 5 h | T2 |
| **UD17** | Cuadros de Mando (Dashboards) y Exportación de Datos | `17-dashboards-exportacion-datos.md` | RA5 | 5 h | T2 |
| **UD18** | Documentación de Aplicaciones (Compodoc, MkDocs/Zensical) | `18-documentacion-aplicaciones.md` | RA6 | 6 h | T2 |
| **UD19** | Pruebas de Software en UI (Unitarias, E2E con Vitest y Playwright) | `19-pruebas-de-software.md` | RA8 | 10 h | T2 |
| **UD20** | Aplicaciones de Escritorio con Electron y Angular | `20-electron.md` | RA7 | 8 h | T2 |
| **UD21** | Empaquetado, Compilación y Distribución Multiplataforma | `21-empaquetado-distribucion.md` | RA7 | 6 h | T2 |
| **UD22** | Proyecto Final Integrador: Sistema Multiplataforma GesFlow | `22-proyecto-final.md` | RA1-RA8 | 10 h | T2 |
| **Dual** | Formación en Empresa (Empaquetado, UX, Pruebas y Despliegue) | Entorno profesional | RA1-RA8 | 86 h | T3 |

---

## 6. Metodología Didáctica

La metodología se fundamenta en principios activos, constructivistas y aplicados:

1. **Aprendizaje Basado en Proyectos (ABP):** El alumnado construye de forma transversal a lo largo del curso el proyecto integrador **GesFlow** (una aplicación completa de escritorio y panel de gestión con Electron, Angular, Tailwind CSS, generación de informes y suite de tests).
2. **Design Thinking y User Experience (UX):** Flujo de trabajo real de la industria: *Empatizar -> Definir -> Idear -> Prototipar (Figma) -> Testear -> Implementar*.
3. **Atomic Design & Modularidad:** Construcción de interfaces desde átomos (botones, inputs) hasta páginas y plantillas completas.
4. **Diseño Universal para el Aprendizaje (DUA):**
    - Múltiples formas de representación: explicaciones visuales, diagramas de arquitectura, código en vivo, tutoriales interactivos en Storybook y documentación Zensical.
    - Múltiples formas de acción y expresión: desarrollo de proyectos individuales, retos grupales, exposiciones técnicas y defensas de código.
    - Múltiples formas de implicación: retos progresivos, gamificación en revisiones de código y simulaciones de casos reales de clientes.

---

## 7. Procedimiento y Criterios de Evaluación

Conforme a la **Orden de 18 de septiembre de 2025** (Andalucía):

- La evaluación será **continua, formativa e integradora**.
- Cada Criterio de Evaluación (CE) se evalúa mediante instrumentos objetivos y rúbricas públicas.
- La calificación del módulo se obtiene a partir de la media ponderada de los Resultados de Aprendizaje superados:

$$\text{Calificación Final} = \sum_{i=1}^{8} (\text{Nota } RA_i \times \text{Ponderación } RA_i)$$

### Instrumentos de Evaluación
1. **Pruebas Prácticas y Retos de Código (40%):** Pruebas de desarrollo individual en aula de informática (creación de componentes Angular, maquetación CSS/Tailwind, scripts Electron, tests unitarios).
2. **Proyectos Prácticos y Entregables (GesFlow / Storybook) (40%):** Calidad del código, arquitectura, cumplimiento de especificaciones UX/UI, accesibilidad WCAG y suite de pruebas automatizadas.
3. **Documentación Técnica, Presentaciones y Pruebas Teóricas (10%):** Claridad en la documentación, diagramas de arquitectura, manuales y exposición de proyectos.
4. **Actitud, Participación y Trabajo Colaborativo (10%):** Uso de control de versiones (Git), buenas prácticas de Clean Code, puntualidad y trabajo en equipo.

### Sistema de Recuperación
- **Recuperación continua:** Al finalizar cada bloque/trimestre se planificarán actividades de refuerzo y segundas oportunidades para los RAs no alcanzados.
- **Convocatoria ordinaria (marzo):** Prueba integradora para aquellos RAs pendientes antes del inicio de la fase dual en empresa.
- **Convocatoria extraordinaria (junio):** Para el alumnado que no haya superado el módulo en la fase ordinaria.

---

## 8. Atención a la Diversidad y Medidas de Inclusión (DUA)

1. **Adaptaciones de Acceso:** Uso de herramientas de apoyo, tipografías legibles (OpenDyslexic, JetBrains Mono), software con soporte de alto contraste y lectores de pantalla.
2. **Gradación de Actividades:** Tareas organizadas en tres niveles: *Básico* (adquisición del criterio esencial), *Intermedio* (consolidación y buenas prácticas) y *Avanzado* (retos de optimización, accesibilidad avanzada o animación compleja).
3. **Tutorización personalizada:** Seguimiento cercano de ritmos de aprendizaje y refuerzo en conceptos troncales de programación reactiva y arquitectura modular.

---

## 9. Recursos Materiales y Software

- **Equipamiento:** Aulas de informática con puestos individuales conectados a Internet.
- **Software Libre y de Desarrollo:**
    - Node.js (LTS), npm / pnpm.
    - Visual Studio Code con extensiones recomendadas (Angular Language Service, Tailwind CSS IntelliSense, Prettier, ESLint).
    - Figma (cuenta educativa) para diseño y prototipado.
    - Angular CLI, Storybook, Vitest, Playwright.
    - Electron & Electron Forge / Builder.
    - Git y GitHub / GitLab.
    - Generador de documentación: Zensical / Markdown / Compodoc.

---

## 10. Concreción y Seguimiento de la Fase Dual en Empresa

En coordinación con la empresa formadora:

- **Tutor laboral y tutor docente:** Plan de formación individualizado con seguimiento quincenal.
- **Actividades en empresa:** Integración de componentes UI en sistemas en producción, adaptación de interfaces a normativas de accesibilidad corporativas, automatización de suites de pruebas E2E y empaquetado de ejecutables multiplataforma.
- **Evaluación dual:** Coordinación entre el tutor laboral y el equipo docente para la valoración del logro de los RAs en el puesto de trabajo.
