---
icon: lucide/file-text
---

# Documentación de Aplicaciones

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Identificar los distintos tipos de documentación de una aplicación (ayuda general y sensible al contexto, manual de usuario, guía de referencia, manuales de instalación/configuración/administración y tutoriales) y su destinatario.
2. Seleccionar herramientas específicas para generar cada tipo de documentación, valorando formatos habituales (HTML, PDF, Markdown) y sistemas de generación de ayudas.
3. Documentar la estructura de la información persistente de una aplicación (modelo de datos, esquemas y contratos de API).
4. Producir el conjunto documental mínimo de una aplicación del módulo (Angular + Tailwind + Electron), integrando la documentación en el flujo de desarrollo y en la propia aplicación.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 6** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 6.** Documenta aplicaciones seleccionando y utilizando herramientas específicas.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE a) Se han identificado sistemas de generación de ayudas.
- CE b) Se han generado ayudas en los formatos habituales.
- CE c) Se han generado ayudas sensibles al contexto.
- CE d) Se ha documentado la estructura de la información persistente.
- CE e) Se ha confeccionado el manual de usuario y la guía de referencia.
- CE f) Se han confeccionado los manuales de instalación, configuración y administración.
- CE g) Se han confeccionado tutoriales.

!!! note "Conocimientos previos"

    Para abordar esta unidad con garantías, el alumnado debe:

    - Dominar Markdown y su uso en README, guías y documentación técnica.
    - Conocer la aplicación del módulo (Angular + Tailwind + Electron) para poder describir su instalación, configuración y uso.
    - Tener nociones de la información persistente que utiliza la aplicación (base de datos o API), para documentar su estructura.
    - Haber trabajado Storybook (Unidad 14), cuya documentación de componentes es un caso concreto de documentación técnica reutilizable.

## Contenidos

**Bloque 1: Tipos de documentación y destinatarios**
- Ayuda general vs. ayuda sensible al contexto (context-sensitive help).
- Manual de usuario, guía de referencia rápida, guías rápidas (*quick start*).
- Manuales de instalación, configuración y administración.
- Tutoriales orientados a tareas.
- Matriz documento → destinatario (usuario final, administrador, desarrollador).

**Bloque 2: Sistemas y herramientas de generación de ayudas**
- Generadores de documentación estática: Docusaurus, VitePress, MkDocs, Sphinx.
- Documentación in-app: tooltips, paneles de ayuda contextuales, `title`/`aria-describedby`, atajos de teclado documentados.
- Formatos de exportación: HTML, PDF (con las herramientas vistas en la unidad de informes), Markdown.
- Integración en el repositorio y en el pipeline (CI que publica la documentación).

**Bloque 3: Documentación de la información persistente**
- Diagramas del modelo de datos (entidad-relación) y esquemas.
- Contratos de API: OpenAPI/Swagger como fuente única de verdad.
- Diccionario de datos: campos, tipos, restricciones y valores permitidos.

**Bloque 4: Documentación de código y componentes**
- Comentar el «por qué», no el «qué». Convenciones (TSDoc/JSDoc).
- Storybook como documentación viva de componentes (Unidad 14).
- Changelogs, `CONTRIBUTING.md` y política de versiones.

## Desarrollo teórico

### 1. El documento correcto para la persona correcta

Documentar no es escribir más: es poner la información adecuada ante el usuario adecuado en el momento adecuado. Un administrador necesita el manual de configuración; un usuario nuevo necesita una guía rápida; un desarrollador que integra la API necesita el contrato OpenAPI. La primera decisión, por tanto, es definir **matriz documento → destinatario → formato**.

| Documento | Destinatario | Formato habitual |
|-----------|--------------|------------------|
| Guía rápida / tutorial | Usuario nuevo | HTML/PDF, pasos orientados a tareas |
| Manual de usuario | Usuario | HTML/PDF |
| Guía de referencia | Usuario avanzado | HTML (búsqueda) |
| Ayuda sensible al contexto | Usuario, in situ | In-app (tooltips, paneles) |
| Manual de instalación/configuración/administración | Administrador/DevOps | Markdown/HTML en repositorio |
| Contrato de API / diccionario de datos | Desarrollador | OpenAPI, diagramas E/R |

### 2. Ayuda sensible al contexto

La **ayuda contextual** aparece «donde el usuario la necesita»: un icono de ayuda junto a cada campo que despliega una explicación específica, o un panel lateral que cambia según la vista activa. En Angular se implementa con directivas/componentes reutilizables:

```typescript
// help.directive.ts (esquemático)
@Directive({ selector: '[appHelp]' })
export class HelpDirective {
  @Input() appHelp = ''; // texto de ayuda específico del elemento
  @HostListener('mouseenter') show() { /* muestra tooltip con this.appHelp */ }
  @HostListener('mouseleave') hide() { /* oculta */ }
}
```

Buenas prácticas: textos cortos y accionables, activación predecible (hover/focus), accesibles por teclado (`role="tooltip"`, `aria-describedby`) y coherentes en tono con la guía de referencia.

### 3. Documentar la información persistente

Documentar «la estructura de la información persistente» (CE d) significa dejar constancia clara del modelo de datos: entidades, relaciones, campos, tipos, restricciones y valores permitidos. Las herramientas habituales son diagramas entidad-relación (DBML, Mermaid, Lucidchart) y, para APIs, un especificador **OpenAPI/Swagger** que actúa como contrato entre frontend y backend:

```yaml
# openapi.yaml (fragmento)
paths:
  /notas:
    get:
      summary: Lista las notas del usuario autenticado
      responses:
        '200':
          description: Colección de notas
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Nota' }
components:
  schemas:
    Nota:
      type: object
      required: [id, titulo]
      properties:
        id: { type: string, format: uuid }
        titulo: { type: string, maxLength: 120 }
        cuerpo: { type: string }
        creadaEl: { type: string, format: date-time }
```

### 4. Documentación viva con Storybook y generadores

La documentación de componentes en Storybook (Unidad 14) es documentación **ejecutable**: muestra cada variante, estado y prop del componente. Para la documentación de la aplicación completa se usan generadores estáticos (Docusaurus/VitePress) que versionan las guías y se publican desde el CI. La clave es tratar la documentación como código: vive en el repositorio, se revisa en pull request y se actualiza junto al cambio.

## Ejemplos guiados

### Ejemplo 1: Ayuda contextual accesible
Añadimos `HelpDirective` a los campos de un formulario (Unidad 12). Cada campo muestra un tooltip al hacer foco o hover, con `role="tooltip"` y `aria-describedby`, verificando la navegación por teclado.

### Ejemplo 2: Contrato OpenAPI de la aplicación
Generamos el especificador OpenAPI del servicio de notas que consume la aplicación Angular, lo validamos con una herramienta (Swagger Editor) y documentamos los códigos de error y ejemplos de petición/respuesta.

!!! example "Casos reales"

    - **Documentación in-app de productos SaaS:** las aplicaciones empresariales combinan guías rápidas interactivas (*onboarding*), base de conocimiento y ayuda contextual; la coherencia entre ellas reduce el soporte.
    - **OpenAPI como contrato:** equipos frontend/backend que comparten un único especificador evitan divergencias y permiten generar clientes y documentación automáticamente.

## Actividades guiadas

1. Elabora la matriz documento → destinatario para la aplicación del módulo y justifica el formato de cada documento.
2. Implementa ayuda sensible al contexto accesible en tres pantallas de la aplicación.
3. Documenta el modelo de datos con un diagrama entidad-relación y un diccionario de campos.

## Actividades propuestas

- Genera un manual de usuario (PDF) a partir de las capturas y flujos principales, usando las herramientas de la unidad de informes.
- Redacta el manual de instalación y configuración para la versión de escritorio (Electron), incluyendo requisitos y resolución de problemas frecuentes.
- Crea un tutorial orientado a una tarea concreta («crear y exportar mi primer informe»).

??? "Actividades de ampliación"

    - Publica la documentación con Docusaurus/VitePress desde el pipeline del proyecto (CI que genera y despliega el sitio).
    - Genera documentación de API automáticamente a partir del especificador OpenAPI.
    - Define una política de `CHANGELOG` y versionado semántico para la aplicación.

!!! tip "Buenas prácticas"

    - Trata la documentación como código: en el repositorio, revisada y actualizada con cada cambio.
    - Un documento, un destinatario, un formato; evita duplicar contenido que puede desincronizarse.
    - Documenta el «por qué» en el código y las decisiones de diseño (ADR).
    - Haz la ayuda contextual accesible por teclado y coherente con la guía de referencia.
    - Usa OpenAPI como fuente única de verdad para los contratos de API.

!!! warning "Errores frecuentes"

    - Documentar solo al final, cuando la aplicación ya cambió (desactualización inmediata).
    - Ayuda contextual que no es accesible por teclado ni está asociada con ARIA.
    - Duplicar información entre manual y ayuda in-app sin un único origen.
    - Omitir la documentación de instalación/configuración/administración, imprescindible para el despliegue (RA 7).
    - Comentar el «qué» en lugar del «por qué», aportando poco valor a quien mantiene el código.

!!! abstract "Resumen"

    Documentar una aplicación (RA 6) exige elegir el documento adecuado para cada destinatario: ayuda general y sensible al contexto, manual de usuario, guía de referencia, manuales de instalación/configuración/administración y tutoriales, en formatos habituales (HTML, PDF, Markdown). Se documenta también la información persistente (modelo de datos, diccionario y contratos OpenAPI) y el código (comentarios, Storybook, changelogs). La documentación se trata como código: vive en el repositorio, se revisa y se publica desde el pipeline.

## Recursos complementarios

- Docusaurus, VitePress, MkDocs — generadores de documentación estática.
- OpenAPI Initiative / Swagger Editor — especificación y herramientas de contratos de API.
- Mermaid y DBML — diagramas de modelo de datos en texto.
- W3C WCAG (criterios sobre información y comunicación) para ayuda contextual accesible.
