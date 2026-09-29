---
icon: lucide/bug
---

# Pruebas de Software

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Establecer una estrategia de pruebas para una aplicación del módulo, seleccionando tipos de prueba y herramientas adecuados a cada nivel (unidad, integración, end-to-end).
2. Ejecutar pruebas de integración, regresión, volumen y estrés, así como pruebas básicas de seguridad y de uso de recursos.
3. Aplicar técnicas de prueba específicas de interfaces: pruebas de componentes, pruebas E2E del flujo completo y verificación en distintos navegadores y dispositivos.
4. Documentar la estrategia de pruebas y los resultados obtenidos, produciendo informes accionables para el equipo.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 8** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 8.** Evalúa el funcionamiento de aplicaciones diseñando y ejecutando pruebas.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE a) Se ha establecido una estrategia de pruebas.
- CE b) Se han realizado pruebas de integración de los distintos elementos.
- CE c) Se han realizado pruebas de regresión.
- CE d) Se han realizado pruebas de volumen y estrés.
- CE e) Se han realizado pruebas de seguridad.
- CE f) Se han realizado pruebas de uso de recursos por parte de la aplicación.
- CE g) Se ha documentado la estrategia de pruebas y los resultados obtenidos.

!!! note "Conocimientos previos"

    Para abordar esta unidad con garantías, el alumnado debe:

    - Dominar las unidades anteriores de componentes Angular (Unidades 10–15), para saber qué y cómo probar.
    - Conocer Jest y Testing Library (o Karma) como frameworks de prueba unitaria en Angular.
    - Tener nociones de control de versiones (Git) para entender el concepto de regresión entre versiones.
    - Conocer el flujo completo de la aplicación (formularios, navegación, informes) para diseñar pruebas end-to-end.

## Contenidos

**Bloque 1: Estrategia de pruebas**
- Objetivos, alcance y limitaciones del proceso de prueba; pirámide de pruebas (unidad → integración → E2E).
- Selección de herramientas por nivel: Jest + Testing Library (unidad), pruebas de servicios/integración, Playwright/Cypress (E2E).
- Criterios de entrada/salida y definición de «prueba aceptable».

**Bloque 2: Pruebas de componentes y servicios**
- Pruebas unitarias de componentes Angular (renderizado, `inputs`, eventos `outputs`).
- Pruebas de servicios con inyección de dependencias y mocks (HttpClient, servicios del módulo).
- Cobertura de código e interpretación de umbrales.

**Bloque 3: Pruebas de integración y end-to-end**
- Integración de componentes entre sí y con el enrutador.
- Flujos completos E2E: registro, creación de un elemento, generación de un informe, exportación.
- Ejecución en distintos navegadores y tamaños de pantalla (responsive).

**Bloque 4: Regresión, volumen, estrés, seguridad y recursos**
- Pruebas de regresión: reejecutar la suite tras cada cambio; detección de roturas.
- Volumen y estrés: comportamiento con grandes volúmenes de datos y carga sostenida.
- Seguridad básica: validación de entradas, inyección, gestión de errores que no filtren información sensible.
- Uso de recursos: memoria (fugas), rendimiento (Core Web Vitals) y consumo en la versión de escritorio (Electron).

**Bloque 5: Documentación de resultados**
- Informes de pruebas: casos, entorno, resultados, defectos y severidad.
- Trazabilidad requisito → caso de prueba → resultado.
- Integración en el pipeline (CI que ejecuta la suite y publica el informe).

## Desarrollo teórico

### 1. La pirámide de pruebas

La estrategia se organiza como una pirámide: muchas pruebas unitarias baratas y rápidas en la base, menos de integración en el medio y pocas end-to-end caras y lentas arriba. Invertirla (muchas E2E) hace la suite frágil y lenta. En el contexto del módulo:

- **Unidad:** componentes y servicios con Jest + Testing Library.
- **Integración:** composición de componentes, enrutador y servicios reales o mockeados.
- **E2E:** flujos completos con Playwright/Cypress en un navegador real.

```typescript
// button.spec.ts (Jest + Testing Library)
import { render, screen } from '@testing-library/angular';
import { ButtonComponent } from './button.component';

describe('ButtonComponent', () => {
  it('emite el evento click al pulsarse', async () => {
    const clicks: number[] = [];
    await render(ButtonComponent, {
      declarations: [],
      componentProperties: { (click: any) => void }: undefined as any,
    });
    // ...
    expect(screen.getByRole('button')).toBeTruthy();
  });
});
```

### 2. Pruebas de integración y E2E

Las pruebas de integración verifican que los elementos funcionan **juntos** (CE b): un formulario (Unidad 12) que valida, guarda mediante el servicio y actualiza la vista. Las pruebas E2E recorren el flujo completo en un navegador real:

```typescript
// e2e/nota.spec.ts (Playwright)
test('crea una nota y la exporta', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Nueva nota' }).click();
  await page.getByLabel('Título').fill('Prueba');
  await page.getByRole('button', { name: 'Guardar' }).click();
  await expect(page.getByText('Prueba')).toBeVisible();
});
```

Se ejecutan en varios navegadores y tamaños de pantalla para cubrir el diseño responsive (Unidad 8).

### 3. Regresión, volumen, estrés, seguridad y recursos

- **Regresión (CE c):** tras cada cambio se reejecuta la suite completa; lo que antes funcionaba no debe romperse. Se automatiza en el CI para que corra en cada pull request.
- **Volumen y estrés (CE d):** se alimenta la aplicación con grandes volúmenes de datos (p. ej., miles de filas en una tabla) y carga sostenida para observar degradación, tiempos y estabilidad.
- **Seguridad (CE e):** validación robusta de entradas, ausencia de inyección por concatenar datos en HTML (`[innerHTML]` sin sanitizar), manejo de errores que no revele información sensible y control de acceso a recursos.
- **Uso de recursos (CE f):** detección de fugas de memoria (suscripciones de RxJS no dadas de baja, `ngOnDestroy`), medición de Core Web Vitals y, en la versión Electron, consumo de RAM frente a una aplicación nativa equivalente.

### 4. Documentar la estrategia y los resultados (CE g)

Se produce un informe que recoge: alcance, herramientas, casos de prueba, entorno, resultados (paso/fallo), defectos detectados con su severidad y trazabilidad hacia los requisitos. La suite y el informe se integran en el pipeline para que cada build genere evidencia reproducible.

## Ejemplos guiados

### Ejemplo 1: Suite unitaria de un componente
Escribimos pruebas para el componente de tabla de la unidad de componentes Tailwind: renderiza filas, emite selección al pulsar y muestra el estado vacío. Medimos cobertura y fijamos umbral.

### Ejemplo 2: Flujo E2E con Playwright
Automatizamos el flujo «crear informe → exportar a PDF» (Unidad 16) en Chromium y Firefox, verificando que el descarga se produce y que la interfaz queda en estado coherente.

!!! example "Casos reales"

    - **CI con calidad como puerta:** equipos que bloquean el merge si la suite de pruebas o los umbrales de cobertura fallan; la regresión se detecta antes de llegar a producción.
    - **Pruebas de rendimiento como métrica:** seguimiento de Core Web Vitals en cada versión para evitar regresiones de rendimiento imperceptibles hasta en producción.

## Actividades guiadas

1. Define la estrategia de pruebas (pirámide) de la aplicación del módulo y justifica las herramientas por nivel.
2. Escribe pruebas unitarias para tres componentes y un servicio, con mocks de dependencias.
3. Crea una prueba E2E que cubra el flujo principal completo y ejecútala en dos navegadores.

## Actividades propuestas

- Implementa una prueba de regresión automatizada en el CI que se ejecute en cada pull request.
- Realiza una prueba de estrés alimentando la tabla con 10.000 filas y documenta tiempos y consumo de memoria.
- Revisa la aplicación buscando al menos dos riesgos de seguridad básicos y propón su mitigación.

??? "Actividades de ampliación"

    - Mide Core Web Vitals antes y después de un cambio y documenta el impacto.
    - Detecta una fuga de memoria por suscripciones no dadas de baja y corrígela, verificando con el perfilador.
    - Genera un informe de pruebas automatizado desde el pipeline con cobertura y resultados.

!!! tip "Buenas prácticas"

    - Prioriza la pirámide: muchas pruebas unitarias, pocas E2E.
    - Prueba comportamientos observables (roles, texto), no detalles de implementación frágiles.
    - Automatiza la regresión en el CI; que corra en cada cambio.
    - Mide rendimiento y recursos como métricas, no solo «pasa/falla».
    - Documenta defectos con severidad y trazabilidad hacia requisitos.

!!! warning "Errores frecuentes"

    - Depender casi solo de pruebas E2E (suite lenta y frágil).
    - No dar de baja suscripciones en `ngOnDestroy`, provocando fugas de memoria.
    - Probar implementaciones internas en lugar del comportamiento, rompiendo pruebas con refactorizaciones inocuas.
    - Omitir pruebas de seguridad básicas (HTML no sanitizado, errores que filtran datos).
    - No documentar resultados ni trazabilidad, dejando la prueba sin valor accionable.

!!! abstract "Resumen"

    Evaluar el funcionamiento de una aplicación (RA 8) exige una estrategia estructurada en pirámide: pruebas unitarias (Jest + Testing Library), de integración y end-to-end (Playwright/Cypress). Se completan con pruebas de regresión, volumen y estrés, seguridad básica y uso de recursos (memoria, Core Web Vitals, consumo en Electron). Todo se automatiza en el pipeline y se documenta con trazabilidad requisito → caso → resultado, produciendo informes accionables.

## Recursos complementarios

- Jest y Testing Library — documentación oficial; guía de pruebas en Angular.
- Playwright y Cypress — frameworks end-to-end multi-navegador.
- Core Web Vitals (web.dev) — métricas de experiencia de usuario.
- OWASP Top 10 — riesgos de seguridad básicos a considerar en la interfaz.
