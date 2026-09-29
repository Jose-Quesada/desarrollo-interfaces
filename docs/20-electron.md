---
icon: lucide/app-window
---

# Aplicaciones de Escritorio con Electron

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Comprender qué es Electron, cómo funciona internamente combinando Chromium y Node.js, y por qué esta arquitectura ha revolucionado el desarrollo de aplicaciones de escritorio, permitiendo usar tecnologías web (HTML, CSS, JavaScript/TypeScript) para construir aplicaciones nativas multiplataforma.
2. Analizar en profundidad la arquitectura de procesos de Electron: el **proceso principal (Main Process)** con acceso completo a Node.js y APIs del sistema operativo, el **proceso renderizador (Renderer Process)** que ejecuta la interfaz web en Chromium de forma aislada, el script de precarga (Preload Script) como puente seguro entre ambos mundos, y el sistema de comunicación entre procesos (IPC: Inter-Process Communication) mediante `ipcMain` e `ipcRenderer`.
3. Estudiar casos reales de aplicaciones construidas con Electron, analizando su arquitectura, decisiones técnicas y lecciones aprendidas: Visual Studio Code (el caso canónico de excelente rendimiento en una aplicación enorme), Discord (chat en tiempo real con WebRTC), Slack (mensajería empresarial), Figma Desktop (renderizado GPU con WebGL), Postman (cliente HTTP), Obsidian (editor de notas con ecosistema de plugins), WhatsApp Desktop y Spotify Desktop.
4. Integrar Angular con Electron siguiendo un enfoque profesional: proyecto Angular standalone que se ejecuta tanto en navegador web como en ventana nativa de Electron, configuración del proceso principal (main.js), script de precarga (preload.js) con `contextBridge` para exponer APIs seguras, scripts de desarrollo y producción en package.json, y uso de librerías facilitadoras como electron-builder y ngx-electron.
5. Dominar las APIs nativas clave de Electron que diferencian una aplicación de escritorio de una aplicación web: sistema de archivos (`fs`), diálogos nativos (`dialog.showOpenDialog`, `showSaveDialog`, `showMessageBox`), notificaciones nativas del sistema operativo (`Notification`), menú nativo (`Menu`, `MenuItem`), bandeja del sistema (`Tray`), atajos de teclado globales (`globalShortcut`), gestión de ventanas (`BrowserWindow` con opciones como fullscreen, alwaysOnTop, transparent, frame), y sistema de auto-actualización (`autoUpdater`).
6. Implementar un servicio Angular tipado (`ElectronService`) que detecte el entorno de ejecución (Electron vs navegador web) y proporcione una API unificada para funcionalidades nativas, permitiendo que la misma aplicación funcione en ambos entornos con degradación gracefully (funcionalidades nativas disponibles en escritorio, alternativas web en navegador).
7. Aplicar las mejores prácticas de seguridad en aplicaciones Electron: `nodeIntegration: false` y `contextIsolation: true` como configuración obligatoria, uso estricto de `contextBridge` en el script de precarga para exponer solo los métodos necesarios, implementación de Content Security Policy (CSP), sanitización de contenido externo, validación de datos en el lado del proceso principal y gestión adecuada de permisos del sistema operativo.
8. Desarrollar una aplicación de ejemplo completa —"Gestor de Notas"— que integre Angular + Electron con funcionalidades nativas reales: leer y guardar archivos de texto en el sistema de archivos local, usar diálogos nativos para abrir y guardar archivos, implementar un menú nativo completo (Archivo, Edición, Ver, Ayuda) con atajos de teclado (Ctrl+N, Ctrl+O, Ctrl+S, Ctrl+Q), y añadir un icono en la bandeja del sistema con menú contextual.
9. Comprender las diferencias fundamentales entre desarrollar para la web y desarrollar para el escritorio con Electron: modelo de seguridad diferente, acceso a recursos del sistema operativo, instalación y actualización de la aplicación (vs carga instantánea de una web), distribución a través de instaladores (vs deploy en un servidor web), y consideraciones de rendimiento específicas de aplicaciones de escritorio (consumo de memoria RAM, uso de CPU, arranque en frío).
10. Identificar y evitar los errores de seguridad más graves en aplicaciones Electron, que pueden comprometer todo el sistema del usuario al tener acceso a Node.js en un entorno de escritorio, y aplicar las recomendaciones de seguridad del equipo oficial de Electron y del Electron Security Working Group.

## Resultado de aprendizaje asociado

!!! info "Normativa"

    Esta unidad contribuye, como RA principal, al **RA 1** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 1.** Genera interfaces gráficos de usuario mediante editores visuales utilizando las funcionalidades del editor y adaptando el código generado.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE b) Se ha creado un interfaz gráfico utilizando las herramientas de un editor visual (la interfaz Angular se ejecuta en el contenedor Electron).
- CE h) Se ha desarrollado una aplicación que incluye el interfaz gráfico obtenido (aplicación de escritorio multiplataforma).

Como RA secundario, esta unidad prepara el **RA 7** («Prepara aplicaciones para su distribución evaluando y utilizando herramientas específicas»), en particular:

- CE a) Se han empaquetado los componentes que requiere la aplicación.
- CE h) Se ha preparado la aplicación para ser distribuida a través de diferentes canales de distribución.

> Nota: la arquitectura de procesos (Main Process y Renderer Process), el IPC, la integración de APIs nativas del sistema operativo y las medidas de seguridad específicas de escritorio son los mecanismos técnicos con los que se genera y prepara esta aplicación multiplataforma.

!!! note "Conocimientos previos"

    - **Angular avanzado**: dominio de componentes standalone, servicios con `inject()`, Signals, HttpClient, Reactive Forms, routing con lazy loading, y comprensión profunda del sistema de inyección de dependencias y el ciclo de vida de los componentes.
    - **Node.js y npm**: comprensión del ecosistema Node.js, gestión de paquetes con npm, scripts de package.json, conocimiento de las APIs básicas de Node.js (`fs`, `path`, `os`, `process`), y comprensión del sistema de módulos CommonJS y ES Modules.
    - **TypeScript avanzado**: interfaces, tipos genéricos, tipos de unión, aserciones de tipo, manejo de promesas y programación asíncrona con async/await, comprensión de los tipos de Node.js (`@types/node`).
    - **JavaScript moderno (ES6+)**: arrow functions, destructuring, spread/rest operators, template literals, módulos ES6, y comprensión del event loop de JavaScript (fundamental para entender la arquitectura de procesos de Electron).
    - **HTML y CSS avanzado**: maquetación responsive, Flexbox, Grid, animaciones CSS, variables CSS (custom properties), y comprensión del modelo de caja y el posicionamiento.
    - **Principios básicos de sistemas operativos**: comprensión de la estructura de archivos y directorios, diferencia entre aplicaciones nativas y aplicaciones web, concepto de permisos de usuario, y familiaridad con los 3 sistemas operativos principales (Windows, macOS, Linux) a nivel de usuario avanzado.
    - **Protocolo HTTP y arquitectura cliente-servidor**: aunque Electron no es cliente-servidor en sentido tradicional, la comunicación entre Main Process y Renderer Process sigue patrones similares.
    - **Control de versiones con Git**: manejo de .gitignore para excluir binarios de Electron, node_modules y directorios de build.

## Contenidos

1. **¿Qué es Electron y cómo funciona?**
   - 1.1. Definición y propósito: **framework open source** (GitHub, 2013) para construir aplicaciones de escritorio multiplataforma utilizando tecnologías web estándar (HTML, CSS, JavaScript/TypeScript).
   - 1.2. ¿Cómo funciona internamente?: Electron combina dos componentes principales en un único ejecutable:
     - **Chromium**: el motor de renderizado de código abierto que impulsa Google Chrome. Se encarga de mostrar la interfaz de usuario (HTML + CSS) y ejecutar el JavaScript del lado del cliente.
     - **Node.js**: el entorno de ejecución de JavaScript en el servidor. Se encarga de interactuar con el sistema operativo: leer/escribir archivos, acceder a la red, ejecutar procesos hijos, interactuar con hardware, etc.
   - 1.3. La "magia" de Electron: en lugar de ejecutarse en un servidor remoto y mostrarse en un navegador, la aplicación web se ejecuta localmente dentro de una **ventana nativa** (sin barra de direcciones ni botones de navegador), y tiene acceso directo a las capacidades del sistema operativo a través de Node.js.
   - 1.4. Ventajas de Electron frente al desarrollo nativo tradicional (C++, C#, JavaFX, Qt): un solo código base para 3 plataformas (Windows, macOS, Linux), uso de tecnologías web que todo desarrollador frontend ya conoce, **ecosistema npm** con cientos de miles de paquetes, desarrollo más rápido, iteración más ágil, hot reload en desarrollo.
   - 1.5. Desventajas y críticas a Electron: **consumo de memoria RAM elevado** (cada aplicación Electron incluye su propia instancia de Chromium, lo que significa al menos 50-100 MB de RAM base incluso para una app "Hola Mundo"), tamaño del instalador grande (mínimo 50-80 MB comprimido), rendimiento inferior al nativo en operaciones intensivas de CPU, no es adecuado para aplicaciones que requieren acceso a hardware de muy bajo nivel o latencia mínima (audio profesional, videojuegos AAA).

2. **Arquitectura de procesos en Electron**
   - 2.1. **Proceso Principal (Main Process)**:
     - Es el punto de entrada de la aplicación (el script definido en `"main"` de package.json).
     - Solo hay UN proceso principal por aplicación. Se crea cuando la aplicación arranca y se destruye cuando la aplicación se cierra.
     - Tiene acceso completo a Node.js y a todas sus APIs (`fs`, `path`, `os`, `child_process`, `net`, `http`, `crypto`, etc.).
     - Es el responsable de gestionar el ciclo de vida de la aplicación: crear ventanas (`BrowserWindow`), gestionar menús nativos (`Menu`), registrar atajos de teclado globales, mostrar diálogos nativos, gestionar la bandeja del sistema (`Tray`), manejar eventos de la aplicación (`app.on('ready')`, `app.on('window-all-closed')`, `app.on('activate')`), y gestionar actualizaciones automáticas.
     - No tiene acceso directo al DOM ni a las APIs del navegador (`window`, `document`, `localStorage`), ya que no hay ventana renderizada en este proceso.
     - Se comunica con los procesos renderizadores mediante **IPC** (Inter-Process Communication).
   - 2.2. **Proceso Renderizador (Renderer Process)**:
     - Cada ventana (`BrowserWindow`) que se abre tiene su propio proceso renderizador independiente.
     - Ejecuta la interfaz de usuario: HTML, CSS y JavaScript (Angular en nuestro caso).
     - Por defecto, por seguridad, NO tiene acceso a Node.js (`nodeIntegration: false`). Solo tiene acceso a las APIs estándar del navegador (DOM, Fetch API, localStorage, etc.) y a las APIs que el Preload Script expone explícitamente.
     - Se comunica con el proceso principal mediante IPC para solicitar operaciones que requieran acceso al sistema operativo.
   - 2.3. **Preload Script**:
     - Es un script JavaScript que se ejecuta en el contexto del proceso renderizador, pero ANTES de que se cargue la página web.
     - Tiene acceso a Node.js y a las APIs del DOM (es un entorno privilegiado).
     - Su función es ser un puente seguro: utiliza `contextBridge.exposeInMainWorld()` para exponer un objeto con métodos específicos en el `window` del renderizador, de forma que el código Angular pueda llamar a funcionalidades nativas sin tener acceso directo a Node.js.
     - Esto implementa el principio de mínimo privilegio: el renderizador solo puede hacer lo que el preload script le permite explícitamente.
   - 2.4. **IPC (Inter-Process Communication)**:
     - Es el mecanismo de comunicación entre el proceso principal y los procesos renderizadores.
     - En el proceso principal: `ipcMain.on('channel', callback)` para escuchar mensajes, `ipcMain.handle('channel', handler)` para manejar solicitudes con respuesta (modelo invoke/handle).
     - En el preload script: `ipcRenderer.invoke('channel', args)` para enviar solicitudes y esperar respuesta asíncrona, `ipcRenderer.on('channel', callback)` para escuchar mensajes enviados desde el proceso principal.
     - En el renderizador (a través del preload): `window.electronAPI.invoke('channel', args)`.

3. **Casos reales de aplicaciones Electron**
   - 3.1. **Visual Studio Code (Microsoft)**: El ejemplo canónico y el que demuestra que Electron puede escalar a aplicaciones enormes con excelente rendimiento. VS Code tiene cientos de miles de líneas de código TypeScript, cientos de extensiones ejecutándose simultáneamente, y un editor de texto que debe responder en milisegundos a cada pulsación de tecla. Claves de su arquitectura: uso intensivo de Web Workers para tareas pesadas (análisis sintáctico, linting, indexación), renderizado parcial y virtualizado del editor, lazy loading de extensiones, y un equipo de ingeniería dedicado a tiempo completo a optimizar el rendimiento. VS Code demuestra que Electron no es intrínsecamente lento: el rendimiento depende de la calidad de la ingeniería de software.
   - 3.2. **Discord**: Aplicación de chat en tiempo real con voz y vídeo. Utiliza Electron para la capa de UI y WebRTC para la comunicación de voz/vídeo. La integración con el sistema operativo es clave: notificaciones nativas, superposición (overlay) en juegos, detección de qué juego se está ejecutando (Rich Presence), atajos de teclado globales para push-to-talk, y minimización a la bandeja del sistema.
   - 3.3. **Slack**: Aplicación empresarial de mensajería. Aprovecha Electron para ofrecer una experiencia nativa (notificaciones, bandeja del sistema, apertura de enlaces en el navegador por defecto del SO) sobre una base de código web. Slack ha invertido significativamente en optimizar el consumo de memoria de su aplicación Electron.
   - 3.4. **Figma Desktop**: Herramienta de diseño de interfaces. El caso de Figma es particularmente interesante porque, a diferencia de la mayoría de aplicaciones Electron que usan el renderizado DOM tradicional de Chromium, Figma utiliza WebGL para renderizar su lienzo de diseño directamente en la GPU, logrando un rendimiento comparable al nativo incluso con documentos complejos con miles de capas.
   - 3.5. **Postman**: Cliente HTTP para probar APIs. Electron permite a Postman acceder al sistema de archivos (para guardar colecciones de requests), al portapapeles del sistema, y sortear las restricciones CORS que un navegador normal impondría (las peticiones HTTP desde Node.js no están sujetas a CORS).
   - 3.6. **Obsidian**: Editor de notas basado en Markdown con ecosistema de plugins. Electron permite a Obsidian acceder al sistema de archivos para trabajar con bóvedas (vaults) locales de archivos `.md`, algo imposible en una aplicación puramente web.
   - 3.7. **WhatsApp Desktop**: La versión de escritorio de WhatsApp, utilizada por cientos de millones de personas.
   - 3.8. **Spotify Desktop**: Aunque Spotify utiliza su propio framework (Chromium Embedded Framework, CEF), la arquitectura es conceptualmente idéntica a Electron: una capa web (HTML/CSS/JS) ejecutándose en un shell nativo con acceso a APIs del sistema operativo.

   **Análisis de lecciones comunes**: Todas estas aplicaciones comparten patrones: separación clara entre UI (web) y lógica nativa (Node.js), actualizaciones automáticas silenciosas, instalación nativa (no "abrir en navegador"), acceso a funcionalidades del sistema operativo que las diferencian de sus versiones web, y un enfoque "offline-first" (la app funciona incluso sin conexión a internet).

4. **Integración de Angular con Electron**

   - 4.1. **Dos enfoques principales**:
     - **Enfoque A (recomendado)**: El proyecto Angular existe de forma independiente. Electron se añade como una capa que "envuelve" la aplicación Angular ya compilada. La app Angular se ejecuta en el proceso renderizador dentro de una `BrowserWindow`. Durante el desarrollo, la ventana de Electron carga `http://localhost:4200` (el servidor de desarrollo de Angular). En producción, carga el `index.html` compilado desde el sistema de archivos local.
     - **Enfoque B**: Usar soluciones integradas como `electron-builder` con configuraciones específicas para Angular, o frameworks como Electron Forge con plantillas Angular preconfiguradas.

   - 4.2. **Configuración paso a paso**:

     **Paso 1: Proyecto Angular existente**
     Asegurarse de que el proyecto Angular funciona correctamente: `ng serve` arranca sin errores, `ng build --configuration production` genera los archivos en `dist/`.

     **Paso 2: Instalar Electron**
     ```bash
     npm install --save-dev electron
     ```

     La versión de Electron se instala como **dependencia de desarrollo**. Electron es un binario de ~60 MB que contiene Chromium + Node.js para la plataforma actual.

     **Paso 3: Crear el punto de entrada del proceso principal (`main.js`)**

     Se crea en la raíz del proyecto (o en una carpeta `electron/`):

     ```javascript
     const { app, BrowserWindow, Menu, dialog, ipcMain } = require('electron');
     const path = require('path');

     let mainWindow = null;

     function createWindow() {
       mainWindow = new BrowserWindow({
         width: 1200,
         height: 800,
         minWidth: 800,
         minHeight: 600,
         title: 'Mi App Angular + Electron',
         icon: path.join(__dirname, 'assets/icon.png'),
         webPreferences: {
           nodeIntegration: false,
           contextIsolation: true,
           preload: path.join(__dirname, 'preload.js'),
           sandbox: false
         }
       });

       // En desarrollo: cargar desde el servidor de Angular
       if (process.env.NODE_ENV === 'development') {
         mainWindow.loadURL('http://localhost:4200');
         mainWindow.webContents.openDevTools();
       } else {
         // En producción: cargar desde el sistema de archivos
         mainWindow.loadFile(path.join(__dirname, 'dist', 'index.html'));
       }

       mainWindow.on('closed', () => {
         mainWindow = null;
       });
     }

     app.whenReady().then(createWindow);

     app.on('window-all-closed', () => {
       if (process.platform !== 'darwin') {
         app.quit();
       }
     });

     app.on('activate', () => {
       if (BrowserWindow.getAllWindows().length === 0) {
         createWindow();
       }
     });
     ```

     **Paso 4: Crear el script de precarga (`preload.js`)**

     ```javascript
     const { contextBridge, ipcRenderer } = require('electron');

     contextBridge.exposeInMainWorld('electronAPI', {
       // Diálogos nativos
       openFileDialog: (options) => ipcRenderer.invoke('dialog:openFile', options),
       saveFileDialog: (options) => ipcRenderer.invoke('dialog:saveFile', options),
       showMessageBox: (options) => ipcRenderer.invoke('dialog:messageBox', options),

       // Sistema de archivos
       readFile: (filePath) => ipcRenderer.invoke('fs:readFile', filePath),
       writeFile: (filePath, data) => ipcRenderer.invoke('fs:writeFile', filePath, data),
       getAppDataPath: () => ipcRenderer.invoke('app:getDataPath'),

       // Información de la app
       getAppVersion: () => ipcRenderer.invoke('app:getVersion'),
       getPlatform: () => ipcRenderer.invoke('app:getPlatform'),

       // Eventos del proceso principal al renderizador
       onFileSaved: (callback) => ipcRenderer.on('file:saved', (event, data) => callback(data)),
       onUpdateAvailable: (callback) => ipcRenderer.on('update:available', callback),

       // Eliminar listeners
       removeAllListeners: (channel) => ipcRenderer.removeAllListeners(channel)
     });
     ```

     **Paso 5: Configurar los manejadores IPC en el proceso principal**

     En `main.js`, añadir los manejadores antes de `createWindow()`:

     ```javascript
     const fs = require('fs');

     // Diálogo de apertura de archivo
     ipcMain.handle('dialog:openFile', async (event, options) => {
       const result = await dialog.showOpenDialog(mainWindow, {
         title: 'Abrir archivo',
         filters: [{ name: 'Documentos', extensions: ['txt', 'md', 'json', 'html', 'css', 'js'] }],
         properties: ['openFile'],
         ...options
       });
       return result;
     });

     // Diálogo de guardar archivo
     ipcMain.handle('dialog:saveFile', async (event, options) => {
       const result = await dialog.showSaveDialog(mainWindow, {
         title: 'Guardar archivo',
         filters: [{ name: 'Documentos', extensions: ['txt', 'md'] }],
         ...options
       });
       return result;
     });

     // Lectura de archivo
     ipcMain.handle('fs:readFile', async (event, filePath) => {
       try {
         const data = fs.readFileSync(filePath, 'utf-8');
         return { success: true, data };
       } catch (error) {
         return { success: false, error: error.message };
       }
     });

     // Escritura de archivo
     ipcMain.handle('fs:writeFile', async (event, filePath, data) => {
       try {
         fs.writeFileSync(filePath, data, 'utf-8');
         mainWindow.webContents.send('file:saved', { filePath });
         return { success: true };
       } catch (error) {
         return { success: false, error: error.message };
       }
     });

     // Ruta de datos de la aplicación
     ipcMain.handle('app:getDataPath', () => app.getPath('userData'));

     // Versión de la aplicación
     ipcMain.handle('app:getVersion', () => app.getVersion());

     // Plataforma del SO
     ipcMain.handle('app:getPlatform', () => process.platform);
     ```

     **Paso 6: Configurar scripts en package.json**

     ```json
     {
       "name": "mi-app-angular-electron",
       "version": "1.0.0",
       "main": "main.js",
       "scripts": {
         "ng": "ng",
         "start": "ng serve",
         "build": "ng build --configuration production",
         "electron:dev": "cross-env NODE_ENV=development concurrently \"ng serve\" \"wait-on http://localhost:4200 && electron .\"",
         "electron:build": "ng build --configuration production && electron-builder",
         "electron:start": "electron ."
       },
       "devDependencies": {
         "concurrently": "^8.2.0",
         "cross-env": "^7.0.3",
         "electron": "^31.0.0",
         "electron-builder": "^24.0.0",
         "wait-on": "^7.0.0"
       }
     }
     ```

   - 4.3. **Servicio ElectronService en Angular**:

     ```typescript
     import { Injectable, inject, signal } from '@angular/core';

     export interface ElectronAPI {
       openFileDialog: (options?: any) => Promise<any>;
       saveFileDialog: (options?: any) => Promise<any>;
       showMessageBox: (options?: any) => Promise<any>;
       readFile: (filePath: string) => Promise<{ success: boolean; data?: string; error?: string }>;
       writeFile: (filePath: string, data: string) => Promise<{ success: boolean; error?: string }>;
       getAppDataPath: () => Promise<string>;
       getAppVersion: () => Promise<string>;
       getPlatform: () => Promise<NodeJS.Platform>;
       onFileSaved: (callback: (data: any) => void) => void;
       onUpdateAvailable: (callback: () => void) => void;
       removeAllListeners: (channel: string) => void;
     }

     @Injectable({ providedIn: 'root' })
     export class ElectronService {
       isElectron = signal(false);
       platform = signal<string>('browser');

       private electronAPI: ElectronAPI | undefined;

       constructor() {
         this.detectElectron();
       }

       private detectElectron(): void {
         if (typeof window !== 'undefined' && (window as any).electronAPI) {
           this.electronAPI = (window as any).electronAPI as ElectronAPI;
           this.isElectron.set(true);
           this.electronAPI.getPlatform().then(p => this.platform.set(p));
         }
       }

       async openFile(): Promise<{ filePath: string; content: string } | null> {
         if (!this.electronAPI) return null;

         const result = await this.electronAPI.openFileDialog();
         if (result.canceled || result.filePaths.length === 0) return null;

         const filePath = result.filePaths[0];
         const readResult = await this.electronAPI.readFile(filePath);
         if (!readResult.success) return null;

         return { filePath, content: readResult.data! };
       }

       async saveFile(content: string, suggestedPath?: string): Promise<string | null> {
         if (!this.electronAPI) return null;

         const result = await this.electronAPI.saveFileDialog(
           suggestedPath ? { defaultPath: suggestedPath } : {}
         );
         if (result.canceled || !result.filePath) return null;

         const writeResult = await this.electronAPI.writeFile(result.filePath, content);
         return writeResult.success ? result.filePath : null;
       }

       async saveExistingFile(filePath: string, content: string): Promise<boolean> {
         if (!this.electronAPI) return false;
         const result = await this.electronAPI.writeFile(filePath, content);
         return result.success;
       }

       async getAppDataPath(): Promise<string | null> {
         if (!this.electronAPI) return null;
         return this.electronAPI.getAppDataPath();
       }

       async showMessage(title: string, message: string): Promise<void> {
         if (!this.electronAPI) {
           alert(`${title}\n${message}`);
           return;
         }
         await this.electronAPI.showMessageBox({
           type: 'info',
           title,
           message,
           buttons: ['Aceptar']
         });
       }
     }
     ```

5. **APIs nativas clave de Electron**

   - 5.1. **Sistema de archivos (fs)**: A diferencia del **File API del navegador** (limitado, basado en selección de archivo por el usuario y sandbox), en Electron se tiene acceso completo al sistema de archivos del usuario mediante el módulo `fs` de Node.js. Esto permite leer y escribir archivos en cualquier ubicación del disco (con los permisos del usuario), crear directorios, listar archivos, vigilar cambios en archivos (`fs.watch`), y trabajar con streams para archivos grandes.

   - 5.2. **Diálogos nativos (dialog)**: `dialog.showOpenDialog(win, options)` muestra el diálogo nativo de apertura de archivos del sistema operativo (no un componente HTML simulado). `dialog.showSaveDialog(win, options)` muestra el diálogo de guardar. `dialog.showMessageBox(win, options)` muestra un cuadro de diálogo con mensaje y botones personalizables. `dialog.showErrorBox(title, content)` muestra un cuadro de error simple.

   - 5.3. **Menús nativos (Menu)**: `Menu.buildFromTemplate(template)` construye un menú a partir de una definición declarativa. `Menu.setApplicationMenu(menu)` establece el menú de la aplicación (macOS: menú superior de la pantalla; Windows/Linux: menú de la ventana). Cada `MenuItem` puede tener `label`, `accelerator` (atajo de teclado), `click` (función callback), `type` (normal, separator, submenu, checkbox, radio), `enabled`, `visible`, `checked`.

   - 5.4. **Bandeja del sistema (Tray)**: `new Tray(iconPath)` crea un icono en la bandeja del sistema (área de notificación en Windows, barra de menú en macOS). Se puede asociar un menú contextual y un tooltip. El evento `click` permite restaurar la ventana principal cuando el usuario hace clic en el icono.

   - 5.5. **Notificaciones nativas (Notification)**: `new Notification({ title, body, icon, silent })` muestra una notificación del sistema. En Windows 10/11, aparecen en el Centro de actividades. En macOS, en el Centro de notificaciones. En Linux, dependen del entorno de escritorio (soporte nativo en GNOME, KDE). El evento `click` permite enfocar la ventana de la aplicación cuando el usuario hace clic en la notificación.

   - 5.6. **Atajos de teclado globales (globalShortcut)**: A diferencia de los atajos de teclado locales (que solo funcionan cuando la app tiene el foco), los **atajos globales** funcionan incluso cuando la aplicación está en segundo plano. `globalShortcut.register('CommandOrControl+Shift+Space', callback)`. Usar con moderación y siempre permitir al usuario configurarlos o desactivarlos.

   - 5.7. **Ventanas (BrowserWindow)**: Las opciones de configuración de `BrowserWindow` son muy extensas:
     - `width`, `height`, `minWidth`, `minHeight`, `maxWidth`, `maxHeight`: dimensiones.
     - `x`, `y`: posición inicial en pantalla.
     - `fullscreen: true`: pantalla completa.
     - `alwaysOnTop: true`: ventana siempre encima de las demás.
     - `transparent: true`: fondo transparente (permite ventanas con formas no rectangulares).
     - `frame: false`: ventana sin bordes (para aplicaciones con diseño personalizado de barra de título, como Spotify o VS Code con título personalizado).
     - `titleBarStyle: 'hiddenInset'`: barra de título oculta con tráfico de luces integrado (solo macOS).
     - `vibrancy: 'ultra-dark'`: efecto de desenfoque del fondo (solo macOS).
     - `backgroundColor`: color de fondo mientras se carga la página.
     - `show: false`: crear la ventana oculta y mostrarla cuando esté lista (evita el flash blanco).
     - `kiosk: true`: modo quiosco (pantalla completa sin posibilidad de salir).

   - 5.8. **Auto-actualización (autoUpdater)**: `autoUpdater` permite que la aplicación se actualice automáticamente descargando nuevas versiones desde un servidor. Se integra con `electron-updater` (npm) para soportar GitHub Releases, S3, Bintray y servidores personalizados. El flujo típico es: comprobar actualizaciones al iniciar (`autoUpdater.checkForUpdatesAndNotify()`), descargar en segundo plano, notificar al usuario cuando esté lista, instalar al reiniciar.

   - 5.9. **Portapapeles (clipboard)**: `clipboard.writeText(text)`, `clipboard.readText()`, `clipboard.writeImage(image)`, `clipboard.readImage()`.
   - 5.10. **Shell**: `shell.openExternal(url)` abre una URL en el navegador por defecto del sistema. `shell.openPath(path)` abre un archivo con la aplicación predeterminada. `shell.showItemInFolder(path)` revela un archivo en el explorador de archivos del sistema.

6. **Seguridad en Electron**

   ==La seguridad es el aspecto más crítico del desarrollo con Electron.== Una aplicación Electron mal configurada puede permitir que código malicioso ejecutado en el proceso renderizador (por ejemplo, a través de un **ataque XSS**) obtenga acceso completo al sistema operativo del usuario a través de Node.js. Esto es órdenes de magnitud más grave que un XSS en una aplicación web tradicional.

   **Reglas de seguridad obligatorias (checklist del equipo oficial de Electron)**:

   1. **`nodeIntegration: false` (SIEMPRE)**: Esta es la regla más importante. Nunca, bajo ninguna circunstancia, habilites `nodeIntegration` en una `BrowserWindow` que cargue contenido remoto o contenido que pueda incluir scripts de terceros. Con `nodeIntegration: true`, cualquier script que se ejecute en el renderizador tiene acceso completo a `require()` y a todas las APIs de Node.js, lo que significa acceso total al sistema de archivos, red, procesos del sistema, etc.

   2. **`contextIsolation: true` (SIEMPRE)**: Esta configuración (activada por defecto desde Electron 12) aísla los contextos de JavaScript del preload script y del renderizador. Sin ella, el código del renderizador podría acceder a las APIs de Node.js expuestas en el preload script. Con `contextIsolation: true`, la única forma de comunicación es a través de `contextBridge.exposeInMainWorld()`.

   3. **Usar `contextBridge` en el preload script**: No exponer APIs de Node.js directamente. Exponer solo funciones específicas y validadas. El objeto expuesto a través de `contextBridge` no puede ser modificado por el código del renderizador.

   4. **Content Security Policy (CSP)**: Configurar una política CSP restrictiva para prevenir ataques XSS. La CSP se puede configurar mediante el meta tag HTTP o mediante la cabecera `Content-Security-Policy`:

       ```html
       <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; connect-src 'self' https:;">
       ```

   5. **Validar y sanitizar todas las entradas del renderizador en el proceso principal**: El proceso principal nunca debe confiar en los datos que recibe del renderizador. Antes de ejecutar cualquier operación con datos recibidos por IPC, validar tipos, rangos, longitudes y formato.

   6. **No confiar en contenido externo sin sanitizar**: Si la aplicación carga contenido de internet (páginas web, HTML de terceros), utilizar `webview` con `sandbox` en lugar de `BrowserWindow`, o implementar sanitización rigurosa con DOMPurify.

   7. **Deshabilitar o limitar la creación de nuevas ventanas**: `mainWindow.webContents.setWindowOpenHandler()` permite controlar qué ventanas se pueden abrir desde el renderizador, previniendo que contenido malicioso abra ventanas no autorizadas.

   8. **Usar `sandbox: true`**: Activar el sandbox de Chromium para el proceso renderizador añade una capa adicional de seguridad, aunque puede limitar algunas funcionalidades (acceso a `require` desde el preload, que ya no debería ser necesario con `contextIsolation`).

7. **Aplicación de ejemplo: "Gestor de Notas" con Angular + Electron**

   Esta aplicación completa demuestra la integración de todas las tecnologías y conceptos de la unidad.

   **Requisitos funcionales**:
   - Crear, abrir, editar y guardar notas de texto.
   - Las notas se almacenan como archivos `.md` (Markdown) en el sistema de archivos local.
   - **Menú nativo**: Archivo (Nuevo Ctrl+N, Abrir Ctrl+O, Guardar Ctrl+S, Guardar como... Ctrl+Shift+S, Salir Ctrl+Q), Edición (Deshacer Ctrl+Z, Rehacer Ctrl+Y, Cortar Ctrl+X, Copiar Ctrl+C, Pegar Ctrl+V), Ver (Modo oscuro, Pantalla completa F11), Ayuda (Acerca de, Documentación).
   - **Bandeja del sistema**: icono con menú contextual para restaurar la ventana o salir.
   - Atajos de teclado para todas las operaciones comunes.
   - **Indicador de cambios no guardados** (punto en la barra de título, diálogo de confirmación al cerrar).
   - Título de la ventana actualizado con el nombre del archivo actual.

   **Estructura de archivos del proyecto**:
   ```
   gestor-notas/
   ├── electron/
   │   ├── main.js          # Proceso principal
   │   ├── preload.js       # Script de precarga
   │   └── menu-template.js # Plantilla del menú nativo
   ├── src/
   │   ├── app/
   │   │   ├── core/
   │   │   │   └── services/
   │   │   │       ├── electron.service.ts
   │   │   │       └── file.service.ts
   │   │   ├── features/
   │   │   │   └── editor/
   │   │   │       ├── editor.component.ts
   │   │   │       └── editor.component.html
   │   │   └── app.component.ts
   │   ├── assets/
   │   │   └── icons/
   │   └── environments/
   ├── package.json
   ├── angular.json
   └── main.js
   ```

   **Código del proceso principal completo** (electron/main.js):
   Incluye creación de ventana, menú nativo con atajos, bandeja del sistema, manejadores IPC para archivos y diálogos, gestión de cambios no guardados, y configuración de seguridad.

   **Código del componente editor Angular**:
   ```typescript
   @Component({
     selector: 'app-editor',
     standalone: true,
     template: `
       <div class="h-screen flex flex-col">
         <!-- Barra de herramientas -->
         <div class="flex items-center gap-2 px-4 py-2 bg-gray-100 border-b">
           <button (click)="newFile()" title="Nuevo (Ctrl+N)" class="p-2 hover:bg-gray-200 rounded">📄</button>
           <button (click)="openFile()" title="Abrir (Ctrl+O)" class="p-2 hover:bg-gray-200 rounded">📂</button>
           <button (click)="saveFile()" title="Guardar (Ctrl+S)" class="p-2 hover:bg-gray-200 rounded">💾</button>
           <span class="flex-1 text-sm text-gray-500 truncate">{{ currentFilePath() || 'Sin título' }}</span>
           @if (isModified()) { <span class="text-xs text-orange-500">● Modificado</span> }
         </div>

         <!-- Área de edición -->
         <textarea
           #editorTextarea
           [(ngModel)]="content"
           (input)="onContentChange()"
           class="flex-1 p-6 resize-none focus:outline-none font-mono text-gray-800"
           placeholder="Escribe tu nota aquí...">
         </textarea>

         <!-- Barra de estado -->
         <div class="flex items-center px-4 py-1 bg-gray-50 border-t text-xs text-gray-400">
           <span>{{ wordCount() }} palabras | {{ charCount() }} caracteres</span>
           <span class="ml-auto">{{ platform() }}</span>
         </div>
       </div>
     `
   })
   export class EditorComponent implements OnInit, OnDestroy {
     private electronService = inject(ElectronService);

     content = '';
     currentFilePath = signal<string | null>(null);
     isModified = signal(false);
     platform = this.electronService.platform;

     wordCount = computed(() => this.content.trim() ? this.content.trim().split(/\s+/).length : 0);
     charCount = computed(() => this.content.length);

     ngOnInit(): void {
       this.electronService.onFileSaved((data) => {
         console.log('Archivo guardado:', data.filePath);
       });
     }

     async openFile(): Promise<void> {
       const result = await this.electronService.openFile();
       if (result) {
         this.content = result.content;
         this.currentFilePath.set(result.filePath);
         this.isModified.set(false);
         document.title = `Gestor de Notas - ${result.filePath.split('/').pop()}`;
       }
     }

     async saveFile(): Promise<void> {
       if (this.currentFilePath()) {
         const success = await this.electronService.saveExistingFile(this.currentFilePath()!, this.content);
         if (success) this.isModified.set(false);
       } else {
         const savedPath = await this.electronService.saveFile(this.content);
         if (savedPath) {
           this.currentFilePath.set(savedPath);
           this.isModified.set(false);
         }
       }
     }

     newFile(): void {
       if (this.isModified()) {
         if (!confirm('Tienes cambios sin guardar. ¿Deseas continuar?')) return;
       }
       this.content = '';
       this.currentFilePath.set(null);
       this.isModified.set(false);
     }

     onContentChange(): void {
       this.isModified.set(true);
     }

     ngOnDestroy(): void {
       this.electronService.removeListeners();
     }
   }
   ```

## Ejemplos guiados

### Ejemplo 1: Configurar Angular + Electron desde cero

**Objetivo**: Crear un proyecto Angular standalone y configurar Electron para ejecutar la aplicación en una ventana nativa de escritorio.

**Instrucciones paso a paso**:

1. Crea un nuevo proyecto Angular standalone:
   ```bash
   ng new gestor-notas --standalone --routing --style=css
   cd gestor-notas
   ```

2. Instala Electron como dependencia de desarrollo:
   ```bash
   npm install --save-dev electron
   ```

3. Crea el archivo `main.js` en la raíz del proyecto con el contenido del proceso principal descrito en la sección 4.2 del desarrollo teórico.

4. Crea el archivo `preload.js` en la raíz del proyecto con el contenido del script de precarga descrito en la sección 4.2.

5. Instala las dependencias adicionales necesarias:
   ```bash
   npm install --save-dev concurrently wait-on cross-env
   ```

6. Modifica `package.json`:
   - Añade `"main": "main.js"` en la raíz.
   - Añade los scripts `electron:dev` y `electron:build` como se describió anteriormente.

7. Crea/modifica `src/app/app.component.ts` para que muestre un mensaje indicando si se está ejecutando en Electron o en navegador, utilizando el `ElectronService` descrito en la sección 4.3.

8. Ejecuta la aplicación en modo desarrollo:
   ```bash
   npm run electron:dev
   ```

9. Verifica que se abre una ventana nativa (sin barra de direcciones del navegador) mostrando la aplicación Angular. La ventana debe tener el título configurado, los botones de minimizar/maximizar/cerrar nativos del sistema operativo, y las DevTools abiertas (para depuración).

### Ejemplo 2: Implementar diálogo de "Abrir archivo" nativo desde un componente Angular

**Objetivo**: Añadir a la aplicación un botón que abra el diálogo nativo de selección de archivo, lea el contenido del archivo seleccionado y lo muestre en un textarea.

**Implementación**:

1. Asegúrate de que `ElectronService`, `main.js` y `preload.js` están configurados como se describió anteriormente, con los manejadores IPC para `dialog:openFile` y `fs:readFile`.

2. En el componente Angular, inyecta `ElectronService` y utiliza el método `openFile()`:

```typescript
@Component({
  selector: 'app-open-file-demo',
  standalone: true,
  template: `
    <div class="p-6">
      <button (click)="openFile()" class="px-4 py-2 bg-blue-600 text-white rounded-lg mb-4">
        Abrir archivo
      </button>
      @if (fileContent()) {
        <pre class="p-4 bg-gray-100 rounded">{{ fileContent() }}</pre>
      }
    </div>
  `
})
export class OpenFileDemoComponent {
  private electronService = inject(ElectronService);
  fileContent = signal('');

  async openFile(): Promise<void> {
    const result = await this.electronService.openFile();
    if (result) {
      this.fileContent.set(result.content);
    }
  }
}
```

3. Prueba la funcionalidad: ejecuta `npm run electron:dev`, pulsa el botón, selecciona un archivo `.txt` o `.md` del sistema, y verifica que el contenido se muestra en pantalla.

4. Para manejar el caso de que la aplicación se ejecute en un navegador web (sin Electron), el `ElectronService.openFile()` devolverá `null`, por lo que se podría implementar un fallback usando la API estándar del navegador (`<input type="file">`).

### Ejemplo 3: Menú nativo completo con atajos de teclado

**Objetivo**: Crear un menú nativo completo (Archivo, Edición, Ver, Ayuda) con atajos de teclado que se comuniquen con el proceso renderizador mediante IPC.

**Implementación del menú en el proceso principal** (electron/main.js):

```javascript
const { Menu, shell } = require('electron');

function createMenu(mainWindow) {
  const isMac = process.platform === 'darwin';

  const template = [
    // En macOS, la primera entrada es el menú de la aplicación
    ...(isMac ? [{
      label: app.name,
      submenu: [
        { role: 'about', label: 'Acerca de Gestor de Notas' },
        { type: 'separator' },
        { role: 'services', label: 'Servicios' },
        { type: 'separator' },
        { role: 'hide', label: 'Ocultar' },
        { role: 'hideOthers', label: 'Ocultar otros' },
        { role: 'unhide', label: 'Mostrar todo' },
        { type: 'separator' },
        { role: 'quit', label: 'Salir' }
      ]
    }] : []),

    {
      label: 'Archivo',
      submenu: [
        {
          label: 'Nuevo',
          accelerator: 'CmdOrCtrl+N',
          click: () => mainWindow.webContents.send('menu:new')
        },
        {
          label: 'Abrir...',
          accelerator: 'CmdOrCtrl+O',
          click: () => mainWindow.webContents.send('menu:open')
        },
        { type: 'separator' },
        {
          label: 'Guardar',
          accelerator: 'CmdOrCtrl+S',
          click: () => mainWindow.webContents.send('menu:save')
        },
        {
          label: 'Guardar como...',
          accelerator: 'CmdOrCtrl+Shift+S',
          click: () => mainWindow.webContents.send('menu:saveAs')
        },
        { type: 'separator' },
        ...(isMac ? [] : [{ role: 'quit', label: 'Salir', accelerator: 'Alt+F4' }])
      ]
    },

    {
      label: 'Edición',
      submenu: [
        { role: 'undo', label: 'Deshacer' },
        { role: 'redo', label: 'Rehacer' },
        { type: 'separator' },
        { role: 'cut', label: 'Cortar' },
        { role: 'copy', label: 'Copiar' },
        { role: 'paste', label: 'Pegar' },
        { role: 'selectAll', label: 'Seleccionar todo' }
      ]
    },

    {
      label: 'Ver',
      submenu: [
        {
          label: 'Modo oscuro',
          type: 'checkbox',
          checked: false,
          accelerator: 'CmdOrCtrl+D',
          click: (menuItem) => mainWindow.webContents.send('menu:toggleDarkMode', menuItem.checked)
        },
        { type: 'separator' },
        { role: 'togglefullscreen', label: 'Pantalla completa' },
        { role: 'reload', label: 'Recargar' },
        { role: 'toggleDevTools', label: 'Herramientas de desarrollo' }
      ]
    },

    {
      label: 'Ayuda',
      submenu: [
        {
          label: 'Acerca de Gestor de Notas',
          click: () => {
            dialog.showMessageBox(mainWindow, {
              type: 'info',
              title: 'Acerca de',
              message: 'Gestor de Notas v1.0.0',
              detail: 'Aplicación de ejemplo para el módulo Desarrollo de Interfaces.\nConstruida con Angular + Electron.'
            });
          }
        },
        {
          label: 'Documentación',
          click: () => shell.openExternal('https://electronjs.org/docs')
        }
      ]
    }
  ];

  const menu = Menu.buildFromTemplate(template);
  Menu.setApplicationMenu(menu);
}
```

**Escuchar los eventos del menú en el componente Angular**:

En el preload script, exponer un método para escuchar eventos del menú:

```javascript
contextBridge.exposeInMainWorld('electronAPI', {
  // ...
  onMenuEvent: (channel, callback) => {
    const validChannels = ['menu:new', 'menu:open', 'menu:save', 'menu:saveAs', 'menu:toggleDarkMode'];
    if (validChannels.includes(channel)) {
      ipcRenderer.on(channel, (event, ...args) => callback(...args));
    }
  }
});
```

En el servicio `ElectronService` y en el componente, suscribirse a estos eventos para ejecutar las acciones correspondientes (nuevo archivo, abrir, guardar, etc.).

## Actividades guiadas

### Actividad guiada 1: Tu primera aplicación Angular + Electron

**Duración**: 90 minutos  
**Nivel**: Medio  
**Agrupamiento**: Parejas

**Objetivo**: Configurar un proyecto Angular con Electron desde cero y ejecutar la aplicación en una ventana nativa.

**Instrucciones**:

1. Crea un nuevo proyecto Angular standalone (`ng new demo-electron --standalone`).
2. Instala Electron y las dependencias auxiliares (`concurrently`, `wait-on`, `cross-env`).
3. Crea el archivo `main.js` con la configuración del proceso principal: creación de `BrowserWindow`, carga del `index.html` de Angular, configuración de `webPreferences` con `nodeIntegration: false`, `contextIsolation: true` y `preload`.
4. Crea el archivo `preload.js` con `contextBridge.exposeInMainWorld` exponiendo al menos dos métodos: uno para obtener la plataforma del sistema y otro para mostrar un cuadro de diálogo.
5. Implementa los manejadores IPC en `main.js` para los métodos expuestos.
6. Crea un `ElectronService` en Angular que detecte si se está ejecutando en Electron y exponga los métodos.
7. Modifica `AppComponent` para que muestre: "Ejecutándose en [Windows|macOS|Linux] con Electron" o "Ejecutándose en navegador web".
8. Configura los scripts en `package.json` (`electron:dev`, `electron:start`).
9. Ejecuta `npm run electron:dev` y verifica que la aplicación se abre en una ventana nativa.
10. Toma una captura de pantalla de la aplicación funcionando.

**Criterios de evaluación**:
- La aplicación se ejecuta correctamente tanto en navegador (`ng serve`) como en Electron (`npm run electron:dev`).
- El `ElectronService` detecta correctamente el entorno de ejecución.
- La configuración de seguridad es correcta (`nodeIntegration: false`, `contextIsolation: true`).
- El código está correctamente tipado con TypeScript.

### Actividad guiada 2: Diálogos nativos y sistema de archivos

**Duración**: 60 minutos  
**Nivel**: Medio  
**Agrupamiento**: Individual

**Objetivo**: Implementar las funcionalidades de abrir, leer y guardar archivos utilizando los diálogos nativos y el módulo `fs` de Node.js a través de IPC.

**Instrucciones**:

1. Amplía el `preload.js` del ejercicio anterior para exponer métodos: `openFileDialog`, `saveFileDialog`, `readFile`, `writeFile`.
2. Amplía `main.js` para implementar los manejadores IPC correspondientes usando `dialog.showOpenDialog`, `dialog.showSaveDialog`, `fs.readFileSync` y `fs.writeFileSync`.
3. Añade al `ElectronService` los métodos `openFile()` y `saveFile()` que devuelvan promesas con el contenido del archivo.
4. Crea un componente `TextEditorComponent` con:
   - Un `textarea` vinculado con `[(ngModel)]`.
   - Botones "Abrir" y "Guardar".
   - Un indicador de si hay cambios sin guardar.
5. Implementa la lógica:
   - Al pulsar "Abrir": muestra el diálogo nativo, lee el archivo, carga el contenido en el textarea.
   - Al pulsar "Guardar": si hay una ruta actual, guarda directamente; si no, muestra el diálogo "Guardar como".
6. Prueba la funcionalidad completa: abre un archivo `.txt`, modifícalo, guárdalo y verifica que los cambios persisten en el disco.

**Criterios de evaluación**:
- Los diálogos nativos se muestran correctamente (son los del sistema operativo, no HTML simulado).
- La lectura y escritura de archivos funciona correctamente con diferentes codificaciones (UTF-8, con tildes y eñes).
- El manejo de errores es robusto (archivo no encontrado, permisos denegados).

### Actividad guiada 3: Menú nativo y bandeja del sistema

**Duración**: 75 minutos  
**Nivel**: Medio-Alto  
**Agrupamiento**: Parejas

**Objetivo**: Implementar un menú nativo completo y un icono en la bandeja del sistema para la aplicación "Gestor de Notas".

**Instrucciones**:

1. Crea una plantilla de menú completa en `main.js` con las secciones: Archivo (Nuevo, Abrir, Guardar, Guardar como, Salir), Edición (Deshacer, Rehacer, Cortar, Copiar, Pegar), Ver (Modo oscuro, Pantalla completa, DevTools), Ayuda (Acerca de).
2. Asigna atajos de teclado a cada acción: `CmdOrCtrl+N`, `CmdOrCtrl+O`, `CmdOrCtrl+S`, etc.
3. Configura la comunicación del menú con el renderizador mediante IPC: usa `mainWindow.webContents.send('menu:action', actionName)` en los callbacks `click` del menú.
4. En el preload script, expón un método `onMenuAction(callback)` para escuchar los eventos del menú.
5. En el componente Angular principal, suscríbete a los eventos del menú y ejecuta las acciones correspondientes.
6. Añade un icono en la bandeja del sistema usando `Tray`:
   - Carga un icono PNG (crea uno simple de 16x16 o 22x22 píxeles).
   - Asocia un menú contextual con opciones: "Mostrar ventana", "Salir".
   - Configura el evento `click` en el icono para restaurar/mostrar la ventana principal.
   - Al cerrar la ventana, minimiza a la bandeja en lugar de salir (excepto si se selecciona "Salir" explícitamente).
7. Prueba todas las funcionalidades: atajos de teclado, acciones del menú, bandeja del sistema.

**Criterios de evaluación**:
- El menú nativo funciona correctamente en el sistema operativo del alumno.
- Los atajos de teclado ejecutan las acciones esperadas.
- El icono en la bandeja del sistema aparece y responde a clics.

## Actividades propuestas

### Actividad propuesta 1: Reproductor de música con Electron (Dificultad: Alta)

Desarrolla un reproductor de música de escritorio utilizando Angular + Electron:

1. La aplicación debe poder reproducir archivos de audio locales (MP3, WAV, OGG) utilizando la API `Audio` de HTML5.
2. Implementa una biblioteca musical que lea los metadatos de los archivos (título, artista, álbum, carátula) usando una librería como `music-metadata-browser`.
3. Añade soporte para arrastrar y soltar (drag & drop) archivos y carpetas desde el explorador del sistema a la aplicación.
4. Implementa una lista de reproducción con añadir, eliminar, reordenar y guardar/cargar playlists como archivos JSON.
5. Añade controles de reproducción: play/pause, anterior, siguiente, barra de progreso, control de volumen.
6. Muestra notificaciones nativas del sistema operativo al cambiar de canción.
7. Añade un icono en la bandeja del sistema con controles de reproducción (play/pause, siguiente).
8. Implementa atajos de teclado globales para play/pause, siguiente y anterior (que funcionen incluso cuando la app no tiene el foco).

### Actividad propuesta 2: Visor de Markdown con vista previa en tiempo real (Dificultad: Media)

Crea una aplicación de escritorio para editar archivos Markdown con vista previa en tiempo real:

1. La interfaz debe tener dos paneles: editor (izquierda, textarea o editor como Monaco/CodeMirror) y vista previa (derecha, HTML renderizado a partir del Markdown).
2. Utiliza una librería como `marked` o `markdown-it` para convertir Markdown a HTML.
3. Aplica estilos CSS a la vista previa para que se vea como un documento formateado (tipografía, espaciado, código con resaltado de sintaxis).
4. Implementa autoguardado: cada 30 segundos, o al perder el foco, guarda automáticamente el archivo (si ya tiene ruta asociada).
5. Añade un explorador de archivos lateral (sidebar) que muestre los archivos `.md` de la carpeta actual y permita navegar entre ellos.
6. Implementa exportación a HTML y PDF.
7. Añade soporte para modo oscuro que afecte tanto al editor como a la vista previa.

### Actividad propuesta 3: Cliente de API REST con Electron (Dificultad: Media-Alta)

Desarrolla una aplicación similar a Postman pero simplificada, utilizando Angular + Electron:

1. Interfaz con: selector de método HTTP (GET, POST, PUT, DELETE, PATCH), campo de URL, área de headers (clave-valor dinámicos), área de body (JSON), y área de respuesta (cuerpo, cabeceras, código de estado, tiempo de respuesta).
2. Las peticiones HTTP se realizan desde el proceso principal (Node.js) usando `fetch` de Node.js o `axios`. Esto permite sortear las restricciones CORS que tendría un navegador normal.
3. Implementa un historial de peticiones (últimas 50) almacenado en el sistema de archivos local (`userData`).
4. Permite guardar colecciones de requests como archivos JSON.
5. Añade variables de entorno (base URL, tokens) que se puedan usar en las peticiones con sintaxis `{{variable}}`.
6. Implementa generación automática de código (cURL, JavaScript fetch, Python requests) a partir de la request configurada.
7. Añade un visor de respuestas con resaltado de sintaxis JSON.

### Actividad propuesta 4: Gestor de tareas con notificaciones del sistema (Dificultad: Media)

Crea una aplicación de lista de tareas (To-Do) con las siguientes características de escritorio:

1. CRUD de tareas con título, descripción, fecha de vencimiento, prioridad (alta/media/baja), etiquetas y estado (pendiente/en progreso/completada).
2. Persistencia en el sistema de archivos local (archivo JSON en `userData`).
3. Notificaciones nativas del sistema operativo cuando se acerca la fecha de vencimiento de una tarea (1 día antes, 1 hora antes).
4. La aplicación debe iniciarse con el sistema operativo (configurable en ajustes) y ejecutarse en segundo plano en la bandeja del sistema, verificando periódicamente las fechas de vencimiento.
5. Implementa un sistema de productividad estilo Pomodoro integrado: temporizador de 25 minutos de trabajo + 5 de descanso, con notificaciones nativas al finalizar cada ciclo.
6. Añade estadísticas de productividad: tareas completadas por día/semana/mes, tiempo total en modo Pomodoro.

### Actividad propuesta 5: Conversor de imágenes con procesamiento nativo (Dificultad: Alta)

Desarrolla una aplicación de escritorio para conversión y procesamiento de imágenes:

1. Soporta arrastrar y soltar imágenes desde el explorador de archivos.
2. Permite redimensionar, recortar, rotar, cambiar formato (JPEG, PNG, WebP, AVIF) y ajustar calidad de compresión.
3. Implementa procesamiento por lotes (batch): seleccionar múltiples imágenes y aplicar las mismas transformaciones a todas.
4. Utiliza `sharp` (librería Node.js de procesamiento de imágenes) en el proceso principal para las operaciones de transformación, comunicando el progreso al renderizador mediante IPC.
5. Muestra una vista previa de la imagen antes y después en el renderizador.
6. Añade una barra de progreso para procesamiento por lotes.
7. Guarda la configuración de la última sesión (formato, calidad, dimensiones) en `userData`.

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Integración con hardware del sistema (Dificultad: Alta)

    Investiga y utiliza las APIs de Electron para interactuar con hardware específico del sistema:

    1. Utiliza `powerMonitor` para detectar cambios en el estado de energía del sistema (conexión/desconexión de corriente, suspensión, reanudación) y adaptar el comportamiento de la aplicación (por ejemplo, pausar el autoguardado cuando el equipo entra en suspensión).
    2. Utiliza `screen` para detectar las pantallas conectadas y sus dimensiones, y adaptar el tamaño y posición de las ventanas (por ejemplo, abrir la app en la pantalla secundaria si está disponible).
    3. Utiliza `desktopCapturer` para capturar la pantalla o ventanas específicas (útil para herramientas de screenshot o grabación).
    4. Documenta los permisos del sistema operativo necesarios para cada API (macOS requiere permisos explícitos de accesibilidad y grabación de pantalla).

    ### Actividad de ampliación 2: Comunicación entre múltiples ventanas (Dificultad: Media-Alta)

    Diseña una aplicación Electron que gestione múltiples ventanas comunicándose entre sí:

    1. Una ventana principal y múltiples ventanas secundarias (por ejemplo, ventanas de detalle que se abren al hacer clic en un elemento de la lista).
    2. Implementa un sistema de mensajería entre ventanas utilizando `ipcMain` como broker central.
    3. Las ventanas secundarias deben poder enviar datos de vuelta a la ventana principal (por ejemplo, editar un elemento en una ventana secundaria y que la lista en la ventana principal se actualice automáticamente).
    4. Sincroniza el tema (oscuro/claro) entre todas las ventanas.
    5. Asegura que al cerrar la ventana principal se cierren todas las ventanas secundarias.

    ### Actividad de ampliación 3: Migración de PWA a Electron (Dificultad: Alta)

    Partiendo de una aplicación Angular que funcione como PWA (Progressive Web Application con Service Worker, funcionamiento offline, instalable), migra la aplicación a Electron preservando las capacidades offline y añadiendo funcionalidades nativas:

    1. Analiza qué funcionalidades de la PWA pueden ser reemplazadas o mejoradas con APIs nativas de Electron (cache offline con Service Worker vs almacenamiento en sistema de archivos, notificaciones push vs notificaciones nativas, instalación como PWA vs instalador nativo).
    2. Implementa la funcionalidad dual: la misma aplicación debe funcionar como PWA en navegador y como app nativa en Electron, detectando el entorno y utilizando las APIs apropiadas en cada caso.
    3. Sincroniza datos entre la versión Electron y la versión web utilizando un backend común (por ejemplo, Firebase Firestore).
    4. Añade funcionalidades exclusivas de la versión de escritorio: acceso al sistema de archivos, menú nativo, bandeja del sistema.

!!! tip "Buenas prácticas"

    1. **Seguridad primero**: `nodeIntegration: false`, `contextIsolation: true`, usar siempre `contextBridge` en el preload. Estas tres configuraciones no son negociables en un entorno de producción. Revisa periódicamente el Security Checklist oficial de Electron: https://www.electronjs.org/docs/latest/tutorial/security

    2. **Mantén el proceso principal ligero**: El proceso principal debe ser un orquestador, no un procesador pesado. Las tareas intensivas de CPU deben delegarse a Web Workers (en el renderizador) o a procesos hijo (`child_process.fork()`). Un proceso principal bloqueado impide que la aplicación responda a eventos del sistema.

    3. **Valida todos los datos que llegan por IPC**: El proceso principal nunca debe confiar en los datos que recibe del renderizador. Implementa validación de tipos, rangos y formatos antes de ejecutar cualquier operación con esos datos (especialmente rutas de archivo, comandos del sistema y consultas a bases de datos).

    4. **Diseña para funcionamiento offline**: Una de las grandes ventajas de Electron es que la aplicación puede funcionar sin conexión a internet. Aprovecha esto: almacena datos localmente (`userData`), cachea recursos, y sincroniza cuando haya conexión.

    5. **Gestiona correctamente el ciclo de vida de las ventanas**: En macOS, las aplicaciones no se cierran cuando se cierran todas las ventanas (permanecen en el Dock). En Windows y Linux, sí. Respeta las convenciones de cada plataforma.

    6. **Usa los menús nativos de cada plataforma**: macOS y Windows tienen convenciones de menú diferentes (en macOS, el menú "Acerca de" va en el menú de la aplicación, no en "Ayuda"; en Windows, "Salir" va en "Archivo"). Usa `process.platform` para adaptar los menús.

    7. **No abuses de las notificaciones**: Las notificaciones nativas son intrusivas. Úsalas solo para información que realmente requiere atención inmediata. Permite al usuario configurar qué notificaciones quiere recibir.

    8. **Implementa auto-actualización desde el primer día**: Las aplicaciones de escritorio no se actualizan automáticamente como las webs. Implementar `electron-updater` desde el principio evita tener que pedir a los usuarios que descarguen nuevas versiones manualmente.

    9. **Optimiza el tamaño del instalador**: Revisa qué archivos se incluyen en el empaquetado. Excluye archivos fuente, tests, dependencias de desarrollo, y archivos no utilizados. Cada megabyte extra en el instalador aumenta la tasa de abandono en la descarga.

    10. **Prueba en las 3 plataformas**: Un mismo código Electron puede comportarse de forma diferente en Windows, macOS y Linux. Comportamiento de diálogos, atajos de teclado (Cmd vs Ctrl), renderizado de fuentes, rutas de archivo (backslash vs forward slash), APIs disponibles (algunas APIs son específicas de plataforma). Si no puedes probar en las 3, usa CI con GitHub Actions (runners de Windows, macOS y Linux).

!!! warning "Errores frecuentes"

    1. **Habilitar `nodeIntegration: true`**: Es el error de seguridad más grave en Electron. Permite que cualquier script en el renderizador (incluyendo scripts de terceros, anuncios, o código XSS inyectado) ejecute código Node.js arbitrario con los privilegios del usuario. **Nunca hagas esto en producción.**

    2. **No usar `contextIsolation: true`**: Sin aislamiento de contexto, el código del renderizador puede acceder a las variables del preload script, incluyendo `require` y los módulos de Node.js. Esto anula cualquier protección que pudiera ofrecer `nodeIntegration: false`.

    3. **Exponer `ipcRenderer` directamente en lugar de usar `contextBridge`**: Exponer `ipcRenderer` da al renderizador acceso a todos los canales IPC, incluyendo los del sistema. En su lugar, exponer solo funciones específicas que envuelvan las llamadas IPC necesarias.

    4. **Cargar contenido remoto sin CSP**: Si la aplicación carga URLs remotas (incluso de confianza), una CSP laxa puede permitir ataques XSS que comprometan toda la aplicación y el sistema del usuario. Configura siempre una CSP restrictiva.

    5. **No manejar el evento `window-all-closed` correctamente en macOS**: En macOS, `app.quit()` no debe llamarse automáticamente al cerrar todas las ventanas, porque las aplicaciones macOS permanecen activas sin ventanas (el usuario espera que la app siga abierta en el Dock).

    6. **Usar `fs.readFileSync` en el proceso principal para archivos grandes**: Las funciones síncronas bloquean el proceso principal, congelando toda la aplicación hasta que la operación termina. Usa las versiones asíncronas (`fs.readFile`, `fs.promises.readFile`) para archivos de más de unos pocos kilobytes.

    7. **No gestionar la destrucción de listeners IPC**: Cada vez que se recarga una página en el renderizador (por ejemplo, en desarrollo con hot reload), se crean nuevos listeners IPC sin eliminar los anteriores. Esto causa fugas de memoria y comportamientos impredecibles (callbacks ejecutándose múltiples veces). Limpia los listeners con `ipcRenderer.removeAllListeners(channel)`.

    8. **Ignorar las diferencias de rutas de archivo entre plataformas**: Windows usa `\` como separador, macOS y Linux usan `/`. Node.js maneja esto bien internamente, pero al construir rutas manualmente con concatenación de strings pueden surgir problemas. Usa `path.join()` para construir rutas.

    9. **No configurar el icono de la aplicación**: Electron usa un icono por defecto (genérico) si no se configura uno. Esto da una apariencia poco profesional. Configura íconos en formato `.ico` (Windows), `.icns` (macOS) y `.png` (Linux).

    10. **Usar `alert()` y `confirm()` en Electron**: En producción, estas funciones muestran cuadros de diálogo con el aspecto del navegador (no nativos). Usa `dialog.showMessageBox()` para cuadros de diálogo con aspecto nativo.

!!! abstract "Resumen"

    Electron representa un **cambio de paradigma** en el desarrollo de aplicaciones de escritorio, permitiendo a desarrolladores web construir aplicaciones nativas multiplataforma utilizando las mismas tecnologías (HTML, CSS, JavaScript/TypeScript) que ya dominan. Esta unidad ha proporcionado una formación completa y profunda en el desarrollo de aplicaciones de escritorio con Electron integrado en el ecosistema Angular.

    La unidad comenzó explicando los fundamentos de Electron: su arquitectura basada en **Chromium + Node.js**, la separación en procesos (Main Process con acceso al sistema operativo, Renderer Process con la interfaz web aislada por seguridad) y la comunicación entre ellos mediante IPC. Comprender esta arquitectura es esencial para desarrollar aplicaciones seguras y eficientes.

    El análisis de casos reales —VS Code, Discord, Slack, Figma, Postman, Obsidian, WhatsApp y Spotify— ha proporcionado al alumnado referentes concretos de cómo las grandes empresas utilizan Electron en producción, las lecciones aprendidas y los patrones arquitectónicos que funcionan a escala.

    La integración de Angular con Electron se ha detallado paso a paso: configuración del proceso principal (`main.js`), script de precarga (`preload.js`), implementación de manejadores IPC en ambos lados, scripts de desarrollo y producción, y creación de un `ElectronService` en Angular que abstrae la detección del entorno y proporciona una API unificada para funcionalidades nativas.

    Las APIs nativas clave de Electron —sistema de archivos, diálogos nativos, menús, bandeja del sistema, notificaciones, atajos globales, portapapeles, shell— se han presentado con ejemplos prácticos, demostrando cómo estas capacidades diferencian una aplicación de escritorio de una aplicación web y aportan valor real al usuario.

    ==La seguridad ha ocupado un lugar central en la unidad.== Se ha hecho hincapié en las **reglas no negociables** (`nodeIntegration: false`, `contextIsolation: true`, uso de `contextBridge`, CSP restrictiva) y se ha explicado el porqué de cada una, contextualizando las graves consecuencias de una configuración insegura.

    La aplicación de ejemplo "Gestor de Notas" ha servido como hilo conductor práctico para integrar todos los conceptos: desde la configuración inicial hasta un menú nativo completo con atajos de teclado, pasando por la lectura/escritura de archivos, los diálogos nativos y la bandeja del sistema.

    Finalmente, las buenas prácticas y los errores frecuentes recogen la experiencia de la comunidad Electron, proporcionando al alumnado una guía para evitar los tropiezos más comunes y costosos en el desarrollo de aplicaciones de escritorio.

## Recursos complementarios

**Documentación oficial**:
- Electron - Documentación oficial: https://www.electronjs.org/docs/latest/
- Electron - Guía de seguridad: https://www.electronjs.org/docs/latest/tutorial/security
- Electron - Checklist de seguridad: https://www.electronjs.org/docs/latest/tutorial/security#checklist-security-recommendations
- Electron Builder - Documentación: https://www.electron.build/
- Context Bridge: https://www.electronjs.org/docs/latest/api/context-bridge
- IPC: https://www.electronjs.org/docs/latest/tutorial/ipc

**Ejemplos y tutoriales**:
- Repositorio oficial de ejemplos de Electron: https://github.com/electron/electron/tree/main/docs/fiddles
- Electron API Demos (aplicación descargable que demuestra todas las APIs): https://github.com/electron/electron-api-demos
- Tutorial: "Building an Electron App with Angular" (blog "Angular University")
- Video: "Electron + Angular Crash Course" (canal de YouTube "Fireship")

**Referencias de aplicaciones reales**:
- VS Code - Repositorio de código fuente: https://github.com/microsoft/vscode
- Obsidian - Documentación para desarrolladores de plugins: https://docs.obsidian.md/

**Herramientas**:
- Electron Fiddle - Entorno de pruebas rápido para Electron: https://www.electronjs.org/fiddle
- Spectron - Testing de aplicaciones Electron (obsoleto, usar Playwright para Electron en su lugar)
- Playwright con soporte Electron: https://playwright.dev/docs/api/class-electron

**Comunidad**:
- Electron en Stack Overflow: etiqueta `[electron]`
- Discord de la comunidad Electron: https://discord.gg/electronjs
- Awesome Electron - Lista curada de recursos: https://github.com/sindresorhus/awesome-electron
