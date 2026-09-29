---
icon: lucide/hand
---

# Interfaces Naturales de Usuario (NUI)

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Definir el concepto de interfaz natural de usuario (NUI) y diferenciarla de las interfaces gráficas tradicionales (GUI), identificando sus modalidades: voz, gestos, movimiento corporal, táctil avanzado y realidad aumentada/virtual.
2. Reconocer las herramientas y APIs web disponibles para el desarrollo de interfaces naturales, valorando su madurez, accesibilidad y viabilidad técnica en proyectos reales.
3. Implementar una interfaz natural de usuario sencilla integrando al menos una modalidad (reconocimiento de voz o detección de movimiento) en una aplicación construida con las tecnologías del módulo.
4. Aplicar criterios de usabilidad y accesibilidad específicos de las interfaces naturales, anticipando los errores de reconocimiento y proporcionando alternativas siempre disponibles.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 2** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 2.** Genera interfaces naturales de usuario utilizando herramientas visuales.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE a) Se han identificado las herramientas disponibles para el aprendizaje automático relacionadas con las interfaces de usuario.
- CE b) Se ha creado una interfaz natural de usuario utilizando las herramientas disponibles.
- CE c) Se ha utilizado el reconocimiento de voz para implementar acciones en las interfaces naturales de usuario.
- CE d) Se ha incorporado la detección del movimiento del cuerpo para implementar acciones en las interfaces naturales de usuario.
- CE e) Se han integrado elementos de detección de partes del cuerpo para implementar acciones en las interfaces naturales de usuario.
- CE f) Se ha integrado la realidad aumentada en los interfaces de usuario.

!!! note "Conocimientos previos"

    Para abordar esta unidad con garantías, el alumnado debe dominar:

    - Fundamentos de JavaScript/TypeScript y de eventos en el navegador (`addEventListener`, promesas y `async/await`).
    - Conceptos básicos de la API Web Media (acceso a cámara y micrófono) y de permisos del navegador.
    - Nociones de las unidades anteriores sobre componentes Angular, servicios e inyección de dependencias, para encapsular la lógica de reconocimiento en servicios reutilizables.
    - Comprensión de los principios de usabilidad y accesibilidad (Unidades 1 y 2), que resultan críticos en interfaces naturales dada su tasa de error.

## Contenidos

**Bloque 1: Fundamentos de las interfaces naturales**
- De la GUI a la NUI: reducción de la distancia entre intención y acción.
- Modalidades: VUI (voz), gestual, corporal, háptica y realidad aumentada/virtual (RA/RV).
- Arquitectura típica: captura del sensor → preprocesado → modelo de reconocimiento → interpretación semántica → acción en la aplicación.
- Tasa de error, ambigüedad y el principio de «alternativa siempre disponible» (Shneiderman).

**Bloque 2: Reconocimiento de voz (VUI)**
- Web Speech API: `SpeechRecognition` / `SpeechRecognitionResult` y síntesis con `SpeechSynthesis`.
- Diferencia entre comandos discretos («guardar», «filtrar por fecha») y lenguaje natural.
- Manejo de eventos (`result`, `end`, `error`), idiomas y confianza del reconocimiento (`confidence`).
- Patrones de diseño de diálogos: confirmación, repetición y salida de la conversación.

**Bloque 3: Detección de movimiento corporal**
- Captura con `getUserMedia` y análisis de fotogramas.
- TensorFlow.js y MediaPipe (Pose Landmarker, Hand Landmarker): inferencia en el navegador sin backend.
- Representación de partes del cuerpo (landmarks) y definición de gestos a partir de su posición relativa.
- Umbrales, suavizado temporal y histeresis para evitar activaciones erróneas.

**Bloque 4: Realidad aumentada en la web**
- WebXR Device API: sesiones `immersive-ar` e `immersive-vr`.
- Three.js como motor de renderizado y su integración con el ciclo de vida de un componente Angular.
- Hit-test y anclaje de contenido sobre el mundo real; limitaciones por dispositivo.

**Bloque 5: Integración en la aplicación del módulo**
- Encapsulación de cada modalidad en un servicio Angular (`VoiceCommandService`, `GestureService`).
- Emisión de eventos/`Signal`s que los componentes suscriben para ejecutar acciones (equivalentes a pulsar un botón).
- Accesibilidad: transcripción visible, atajos por teclado equivalentes y aviso de estado del reconocimiento.

## Desarrollo teórico

### 1. ¿Por qué interfaces naturales?

Una **interfaz natural (NUI)** es aquella en la que el usuario interactúa con el sistema mediante capacidades humanas «instintivas» —hablar, señalar, moverse— en lugar de operar dispositivos intermedios como ratón o teclado. El objetivo es acortar al máximo la distancia entre la intención del usuario y la acción del sistema, una tendencia ya analizada en la introducción del módulo (evolución de las interfaces).

Las NUI no sustituyen a la GUI: la complementan. Un mando por voz es útil para tareas con las manos ocupadas o para usuarios con movilidad reducida, pero nunca debe ser el único canal. Por ello el principio rector es ofrecer **siempre una alternativa** (teclado/ratón) y tratar el reconocimiento como un acelerador, no como una dependencia crítica.

### 2. Reconocimiento de voz con la Web Speech API

La **Web Speech API** expone dos capacidades: síntesis (`SpeechSynthesis`) y reconocimiento (`SpeechRecognition`, aún con prefijo en algunos navegadores). El patrón mínimo para escuchar un comando y actuar es el siguiente:

```typescript
// voice-command.service.ts (Angular)
import { Injectable, EventEmitter } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class VoiceCommandService {
  private recognition: any;
  readonly command = new EventEmitter<string>();

  constructor() {
    const SR = window.SpeechRecognition || (window as any).webkitSpeechRecognition;
    if (!SR) return; // el navegador no lo soporta: la alternativa por teclado sigue disponible
    this.recognition = new SR();
    this.recognition.lang = 'es-ES';
    this.recognition.onresult = (e: any) => {
      const texto: string = e.results[0][0].transcript.trim().toLowerCase();
      if (e.results[0][0].confidence > 0.6) this.command.emit(texto);
    };
    this.recognition.onend = () => this.recognition.start(); // escucha continua
  }

  start() { this.recognition?.start(); }
  stop() { this.recognition?.stop(); }
}
```

En el componente se suscribe al evento y se mapea el texto a acciones:

```typescript
export class DashboardComponent implements OnInit {
  constructor(private voice: VoiceCommandService) {}
  ngOnInit() {
    this.voice.command.subscribe((cmd) => {
      if (cmd.includes('filtro')) this.aplicarFiltro();
      if (cmd.includes('guardar')) this.guardar();
    });
    this.voice.start();
  }
}
```

Buenas prácticas de VUI: usar comandos cortos y consistentes, confirmar acciones destructivas por voz («¿confirmas borrar?»), mostrar siempre la transcripción en pantalla y degradar con elegancia cuando `confidence` es baja.

### 3. Detección de movimiento corporal con TensorFlow.js / MediaPipe

Para gestos y postura, la combinación más práctica en el navegador es **MediaPipe** (modelos ligeros de landmarks) ejecutado con **TensorFlow.js**. El flujo es: activar la cámara, enviar cada fotograma al modelo y obtener coordenadas normalizadas de las articulaciones o dedos. A partir de esas coordenadas se definen reglas simples («codo por encima de la rodilla» = sentarse; «palma abierta hacia la cámara» = pausa).

```typescript
// gesture.service.ts (esquemático)
import { Injectable, EventEmitter } from '@angular/core';
import { PoseLandmarker } from '@mediapipe/tasks-vision';

@Injectable({ providedIn: 'root' })
export class GestureService {
  readonly pose = new EventEmitter<{ codoY: number; rodillaY: number }>();
  private landmarker?: PoseLandmarker;

  async onFrame(video: HTMLVideoElement) {
    if (!this.landmarker) return;
    const res = this.landmarker.detectForVideo(video, performance.now());
    if (res.poseLandmarks?.length) {
      const codo = res.poseLandmarks[10], rodilla = res.poseLandmarks[23];
      this.pose.emit({ codoY: codo.y, rodillaY: rodilla.y });
    }
  }

  // En el componente: si codoY < rodillaY durante N frames => «de pie»
}
```

Claves de robustez: aplicar **suavizado temporal** (media móvil de posiciones), usar **histeresis** (umbrales distintos para activar y desactivar un gesto) y exigir que el gesto se mantenga varios fotogramas antes de disparar la acción.

### 4. Realidad aumentada con WebXR + Three.js

**WebXR** permite solicitar una sesión inmersiva (`navigator.xr.requestSession('immersive-ar')`) y renderizar contenido 3D anclado al mundo mediante hit-test. En Angular, el canvas de Three.js se gestiona en `ngAfterViewInit` y se destruye en `ngOnDestroy`. La RA es la modalidad con más limitaciones de dispositivo (requiere cámara compatible y soporte WebXR), por lo que debe plantearse como ampliación, no como requisito central.

### 5. Accesibilidad de las interfaces naturales

Una NUI mal diseñada excluye a usuarios con discapacidad del habla, auditiva o motriz. Criterios mínimos: transcripción en texto de todo lo dicho/escuchado, paridad funcional con el teclado, control explícito para activar/desactivar cada modalidad y avisos claros del estado («escuchando…», «no te he entendido, repítelo»).

## Ejemplos guiados

### Ejemplo 1: Filtro de un dashboard por voz
Partimos del dashboard de la unidad de dashboards. Añadimos `VoiceCommandService` y tres comandos: «mostrar ventas», «filtrar por mes» y «limpiar». Se muestra la transcripción en una barra inferior y cada comando dispara el mismo método que el botón equivalente, garantizando paridad.

### Ejemplo 2: Pausa de vídeo con un gesto
Con `GestureService` (MediaPipe Hand Landmarker) detectamos la palma abierta sostenida dos segundos para pausar/reanudar un reproductor. Se aplica suavizado y histeresis, y se muestra el gesto reconocido en pantalla como feedback.

!!! example "Casos reales"

    - **Asistentes integrados:** los asistentes de voz de navegadores y SO (Siri, Alexa, asistente de Windows) son VUI a gran escala; sus patrones (confirmación, repetición, salida) son la referencia de diseño.
    - **Control por gestos en sanitarios e industria:** sistemas que usan cámaras y visión por computador para operar interfaces sin contacto, un caso directo de NUI corporal con fines de higiene y seguridad.
    - **RA comercial:** aplicaciones de probador de muebles (superponer objetos 3D en la sala) y de mantenimiento industrial (instrucciones superpuestas sobre la máquina) demuestran el valor de anclar información al contexto físico.

## Actividades guiadas

1. Implementa `VoiceCommandService` en un proyecto Angular vacío y emite por consola cada comando reconocido, verificando el umbral de confianza.
2. Añade tres comandos a una lista de tareas (crear, completar, eliminar) y comprueba la paridad con los botones existentes.
3. Integra MediaPipe Pose Landmarker en un componente que muestre en tiempo real si el usuario está «de pie» o «sentado», usando suavizado temporal.

## Actividades propuestas

- Diseña y documenta un diálogo por voz para una acción destructiva (borrar un elemento) con confirmación y cancelación.
- Implementa un gesto de dos manos (por ejemplo, «pinchar» con pulgar e índice de cada mano) para acercar/alejar el contenido de un visor.
- Compara la tasa de error de tu VUI en comandos discretos frente a frases en lenguaje natural y propone mejoras.

??? "Actividades de ampliación"

    - Integra una sesión WebXR `immersive-ar` con Three.js que ancle un objeto 3D a la mesa mediante hit-test.
    - Combina voz + gesto: el gesto selecciona un elemento y la voz lo renombra.
    - Documenta las limitaciones por navegador (soporte de `SpeechRecognition`, WebXR) y define la estrategia de degradación.

!!! tip "Buenas prácticas"

    - Ofrece siempre una alternativa por teclado/ratón a cualquier acción disponible por voz o gesto.
    - Muestra feedback visible del estado del reconocimiento («escuchando», «no entendido»).
    - Usa comandos cortos, consistentes y confirmación para acciones destructivas.
    - Aplica suavizado temporal y histeresis en la detección de gestos.
    - Encapsula cada modalidad en un servicio Angular que emita eventos; los componentes solo reaccionan.

!!! warning "Errores frecuentes"

    - Hacer de la voz/gesto el **único** canal de interacción (excluye a usuarios con discapacidad).
    - No comprobar el soporte del navegador (`SpeechRecognition`, WebXR) antes de usarlo.
    - Disparar acciones con un solo fotograma o una sola palabra, sin suavizado ni umbral de confianza.
    - Olvidar `ngOnDestroy` para detener reconocimiento/cámara y liberar recursos.
    - Ignorar la transcripción visible, lo que impide depurar y hace la interfaz opaca.

!!! abstract "Resumen"

    Las interfaces naturales (RA 2) acercan la interacción a capacidades humanas instintivas: voz, gestos, movimiento corporal y realidad aumentada. En el navegador se implementan con la Web Speech API (voz), TensorFlow.js/MediaPipe (cuerpo) y WebXR + Three.js (RA). Se encapsulan en servicios Angular que emiten eventos, garantizando siempre una alternativa accesible por teclado y un feedback visible del estado. Son complementos potentes de la GUI, no sustitutos.

## Recursos complementarios

- Web Speech API — MDN: `SpeechRecognition` y `SpeechSynthesis`.
- TensorFlow.js y MediaPipe (Pose/Hand Landmarker) — documentación oficial y ejemplos en el navegador.
- WebXR Device API — MDN; Three.js — guía de integración con entornos inmersivos.
- Shneiderman, B. *Designing the User Interface* (capítulos sobre interacción natural y principios de usabilidad).
