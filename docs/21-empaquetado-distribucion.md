---
icon: lucide/package
---

# Empaquetado y Distribución de Aplicaciones

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Comprender el ciclo completo de vida de una aplicación de escritorio, desde el desarrollo hasta la distribución final al usuario, incluyendo las fases de build (compilación), empaquetado (generación de instaladores), distribución (despliegue en servidores/tiendas) y actualización (mecanismos de entrega continua de nuevas versiones).
2. Dominar la herramienta electron-builder para empaquetar aplicaciones Electron + Angular en instaladores nativos para los 3 sistemas operativos principales (Windows, macOS, Linux), configurando todos los parámetros necesarios: appId, productName, iconos, formatos de salida, ficheros a incluir/excluir, metadatos del instalador y configuración de auto-actualización.
3. Configurar y ejecutar builds multiplataforma para generar los siguientes formatos de salida: Windows (instalador NSIS `.exe`, versión portable `.exe`, AppX para Microsoft Store), macOS (imagen DMG, paquete `.pkg`, Mac App Store MAS), Linux (AppImage, `.deb` para Debian/Ubuntu, `.rpm` para Fedora/RHEL, `.snap` para Snap Store, `.tar.gz` genérico).
4. Implementar un pipeline de CI/CD con GitHub Actions para automatizar la construcción, prueba y publicación de aplicaciones Electron en las 3 plataformas simultáneamente, incluyendo la generación de releases en GitHub con los instaladores adjuntos.
5. Comprender el sistema de firma de código (Code Signing) y su importancia para la confianza del usuario: certificados Authenticode en Windows (para evitar advertencias de SmartScreen), Apple Developer ID y notarización en macOS (obligatoria a partir de macOS Catalina para aplicaciones distribuidas fuera de la Mac App Store), y firma GPG en Linux.
6. Implementar un sistema de actualizaciones automáticas mediante `electron-updater`, configurando el servidor de actualizaciones (GitHub Releases, AWS S3, Bintray o servidor personalizado), el flujo de comprobación-descarga-instalación, y la experiencia de usuario durante el proceso de actualización.
7. Comprender el proceso de publicación en tiendas de aplicaciones: Microsoft Store (requisitos, proceso de empaquetado como AppX/MSIX, validación, publicación), Mac App Store (requisitos de sandbox, entitlements, provisioning profiles, TestFlight para beta testing), Snap Store en Linux (snapcraft.yaml, confinement, revisión automática y manual).
8. Diseñar una estrategia de distribución dual: la misma base de código Angular se despliega como aplicación web SPA (en servidores web tradicionales o plataformas cloud como Vercel/Netlify) y como aplicación de escritorio (empaquetada con Electron para las 3 plataformas), utilizando variables de entorno de Angular (`environment.electron` vs `environment.web`) para condicionar el comportamiento.
9. Configurar los aspectos visuales y de marca del instalador: iconos de la aplicación en los formatos requeridos por cada plataforma, imágenes de fondo del instalador NSIS en Windows, personalización del diálogo de instalación, inclusión de acuerdos de licencia (EULA), y configuración de la experiencia de desinstalación.
10. Identificar y resolver los problemas más comunes en el empaquetado y la distribución de aplicaciones Electron: errores de firma de código, incompatibilidades de dependencias nativas entre plataformas, diferencias en el sistema de archivos (paths, permisos), gestión de dependencias nativas de Node.js, y problemas de rendimiento en CI/CD.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 7** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 7.** Prepara aplicaciones para su distribución evaluando y utilizando herramientas específicas.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE a) Se han empaquetado los componentes que requiere la aplicación.
- CE b) Se ha personalizado el asistente de instalación.
- CE c) Se han generado paquetes de instalación utilizando el entorno de desarrollo.
- CE d) Se han generado paquetes de instalación utilizando herramientas externas (electron-builder).
- CE e) Se han firmado digitalmente las aplicaciones para su distribución.
- CE f) Se han generado paquetes instalables en modo desatendido.
- CE g) Se ha preparado el paquete de instalación para que la aplicación pueda ser correctamente desinstalada.
- CE h) Se ha preparado la aplicación para ser distribuida a través de diferentes canales de distribución.

> Nota: la automatización del proceso mediante integración continua (CI/CD) y las actualizaciones automáticas son buenas prácticas complementarias a estos criterios oficiales.

!!! note "Conocimientos previos"

    - **Electron**: comprensión de la arquitectura de procesos (Main Process, Renderer Process), configuración de `BrowserWindow`, scripts de precarga (preload.js), IPC (Inter-Process Communication), y manejo de APIs nativas (estudiados en la unidad 20).
    - **Angular**: conocimiento profundo del proceso de build (`ng build --configuration production`), comprensión de los archivos generados en `dist/`, configuración de environments (`environment.ts`, `environment.prod.ts`) para variables de entorno, y manejo del archivo `angular.json`.
    - **Node.js y npm**: dominio del archivo `package.json` (scripts, dependencias, configuración de campos como `main`, `build`, `author`, `license`), comprensión de las dependencias nativas de Node.js (`node-gyp`, módulos compilados en C++ como `sharp`, `sqlite3`, `bcrypt`), y conocimiento del sistema de módulos (CommonJS vs ES Modules).
    - **Control de versiones con Git**: manejo avanzado (tags para versiones, releases en GitHub, branches), configuración de `.gitignore` para excluir binarios compilados, instaladores y directorios de build, y comprensión del flujo de trabajo Git Flow.
    - **CI/CD (Integración y Despliegue Continuo)**: conceptos básicos de pipelines de CI/CD, conocimiento de GitHub Actions (workflows, jobs, steps, actions del marketplace, secrets, matrices de estrategia para builds multiplataforma), y comprensión de los runners de GitHub Actions (ubuntu-latest, macos-latest, windows-latest).
    - **Sistemas operativos**: conocimiento de las diferencias entre Windows, macOS y Linux en cuanto a instalación de aplicaciones (rutas estándar como `C:\Program Files`, `/Applications`, `/opt`), permisos de usuario, formatos de instaladores, y requisitos de firma de código de cada plataforma.
    - **Conceptos de seguridad informática**: firma digital, certificados de código (Code Signing Certificates), autoridades de certificación (CA), notarización en macOS, SmartScreen en Windows, y modelo de permisos en macOS (sandbox, entitlements, hardened runtime).

## Contenidos

1. **El ciclo completo de vida de una aplicación de escritorio**
   - 1.1. **Fases del ciclo**: desarrollo (escribir código, probar localmente) → build (compilar Angular, agrupar con Electron) → empaquetado (generar instaladores para cada plataforma) → distribución (publicar en servidor/tienda) → instalación (el usuario descarga e instala) → actualización (mecanismo de entrega de nuevas versiones).
   - 1.2. **Diferencias fundamentales con el desarrollo web**: en la web, "desplegar" significa subir archivos a un servidor y los usuarios acceden instantáneamente a la nueva versión. En escritorio, "distribuir" significa generar un instalador de decenas de megabytes que el usuario debe descargar, ejecutar e instalar. Esta diferencia tiene implicaciones profundas en la experiencia de usuario y en la estrategia de actualizaciones.
   - 1.3. **Importancia del empaquetado correcto**: un instalador mal configurado puede generar errores de permisos, antivirus que bloquean la aplicación, certificados de seguridad que generan miedo en el usuario, o simplemente una aplicación que no arranca. ==La calidad del empaquetado afecta directamente a la tasa de adopción y retención de usuarios==.

2. **Electron Builder: la herramienta principal de empaquetado**
   - 2.1. Instalación y configuración básica:
     ```bash
     npm install --save-dev electron-builder
     ```
   - 2.2. Configuración en `package.json` (campo `"build"`): electron-builder lee la configuración desde el campo `"build"` del `package.json` o desde un archivo separado `electron-builder.yml`. Se recomienda usar `package.json` para mantener la configuración centralizada.

   - 2.3. **Opciones de configuración principales**:
     ```json
     {
       "build": {
         "appId": "com.miempresa.miapp",
         "productName": "Mi Aplicación",
         "copyright": "Copyright © 2024 Mi Empresa S.L.",
         "directories": {
           "output": "release",
           "buildResources": "build"
         },
         "files": [
           "dist/**/*",
           "main.js",
           "preload.js",
           "node_modules/**/*",
           "!node_modules/.cache/**/*",
           "!node_modules/electron/**/*"
         ],
         "win": {
           "target": [
             { "target": "nsis", "arch": ["x64", "ia32"] },
             { "target": "portable", "arch": ["x64"] }
           ],
           "icon": "build/icon.ico",
           "publisherName": "Mi Empresa S.L.",
           "certificateFile": "build/cert.pfx",
           "certificatePassword": "${CSC_KEY_PASSWORD}"
         },
         "mac": {
           "target": [
             { "target": "dmg", "arch": ["x64", "arm64"] },
             { "target": "zip", "arch": ["x64", "arm64"] }
           ],
           "icon": "build/icon.icns",
           "category": "public.app-category.productivity",
           "hardenedRuntime": true,
           "gatekeeperAssess": false,
           "entitlements": "build/entitlements.mac.plist",
           "entitlementsInherit": "build/entitlements.mac.plist"
         },
         "linux": {
           "target": [
             "AppImage",
             "deb",
             "rpm",
             "snap"
           ],
           "icon": "build/icons",
           "category": "Office",
           "maintainer": "soporte@miempresa.com",
           "synopsis": "Gestor empresarial multiplataforma",
           "description": "Aplicación completa de gestión empresarial con dashboard, facturación y clientes."
         },
         "nsis": {
           "oneClick": false,
           "perMachine": true,
           "allowToChangeInstallationDirectory": true,
           "installerIcon": "build/icon.ico",
           "uninstallerIcon": "build/icon.ico",
           "installerHeaderIcon": "build/icon.ico",
           "createDesktopShortcut": true,
           "createStartMenuShortcut": true,
           "shortcutName": "Mi Aplicación",
           "license": "LICENSE.txt",
           "installerLanguages": ["es_ES", "en_US"]
         },
         "dmg": {
           "title": "Mi Aplicación ${version}",
           "icon": "build/icon.icns",
           "background": "build/dmg-background.png",
           "iconSize": 80,
           "contents": [
             { "x": 130, "y": 220 },
             { "x": 410, "y": 220, "type": "link", "path": "/Applications" }
           ],
           "window": { "width": 540, "height": 380 }
         },
         "publish": [
           {
             "provider": "github",
             "owner": "miempresa",
             "repo": "miapp",
             "releaseType": "draft"
           }
         ]
       }
     }
     ```

   - 2.4. **Explicación de los campos clave**:
     - **appId**: Identificador único de la aplicación en formato reverse-domain (`com.empresa.app`). Debe ser único globalmente. Se usa para identificar la aplicación en el sistema operativo, para las actualizaciones y para la firma de código.
     - **productName**: Nombre visible de la aplicación que aparece en el instalador, en el menú de inicio, en la carpeta de aplicaciones y en la barra de título.
     - **directories.output**: Carpeta donde se generarán los instaladores (por defecto `dist`). Se recomienda usar `release` para evitar conflictos con la salida de Angular.
     - **directories.buildResources**: Carpeta donde se almacenan los recursos de build (iconos, fondos, certificados, archivos de entitlements). Por defecto `build`.
     - **files**: Array de patrones glob que especifica qué archivos se incluyen en el paquete. Por defecto incluye todo excepto lo especificado en `.gitignore`. Es crucial excluir dependencias de desarrollo y archivos fuente.
     - **win.target, mac.target, linux.target**: Especifican los formatos de salida y las arquitecturas de CPU para cada plataforma.

3. **Formatos de salida por plataforma**

   - 3.1. **Windows**:
     - **NSIS (Nullsoft Scriptable Install System)**: Formato recomendado para instaladores tradicionales. Genera un archivo `.exe` que guía al usuario a través de un asistente de instalación. Ventajas: ampliamente compatible (Windows 7+), permite personalizar el diálogo de instalación, soporta instalación por usuario o por máquina, permite elegir directorio de instalación, crea accesos directos en el escritorio y menú de inicio, incluye desinstalador. Es la opción por defecto de electron-builder para Windows.
     - **Portable**: Archivo `.exe` autocontenido que no requiere instalación. El usuario lo descarga y lo ejecuta directamente. Ideal para entornos corporativos donde los usuarios no tienen permisos de instalación, o para herramientas que se usan ocasionalmente. Desventajas: no se integra en el menú de inicio, no se asocia con extensiones de archivo, las actualizaciones deben gestionarse manualmente.
     - **AppX / MSIX**: Formato de paquete de aplicación para la Microsoft Store (Windows 10/11). Requiere una cuenta de desarrollador de Microsoft ($19 USD único para particulares). Ventajas: distribución a través de la tienda oficial de Microsoft, actualizaciones automáticas gestionadas por la tienda, instalación y desinstalación limpias sin dejar residuos en el registro.

   - 3.2. **macOS**:
     - **DMG (Disk Image)**: Formato más común para distribuir aplicaciones macOS fuera de la App Store. Es una imagen de disco que se "monta" como un volumen virtual. El usuario arrastra el icono de la aplicación a la carpeta `/Applications`. electron-builder permite personalizar el fondo, el tamaño de los iconos y la disposición de los elementos dentro de la ventana del DMG.
     - **PKG**: Instalador de paquetes de macOS, similar a un instalador MSI en Windows. Más adecuado para aplicaciones que necesitan instalar componentes en ubicaciones del sistema.
     - **MAS (Mac App Store)**: Formato para publicación en la Mac App Store. Requiere un Apple Developer Program membership ($99/año), cumplir con las directrices de revisión de Apple (sandbox obligatorio, uso de APIs permitidas, interfaz de usuario de calidad), y pasar la revisión manual de Apple.
     - **ZIP**: Archivo comprimido simple. Menos profesional que un DMG, pero útil para distribución interna o CI/CD.

   - 3.3. **Linux**:
     - **AppImage**: Formato de aplicación portable autocontenida. No requiere instalación: se descarga, se da permiso de ejecución (`chmod +x`) y se ejecuta. Funciona en prácticamente cualquier distribución Linux. Es la opción más fácil para los desarrolladores, pero no se integra con el gestor de paquetes del sistema.
     - **DEB**: Paquete para Debian, Ubuntu, Linux Mint, elementary OS y derivadas. Se instala mediante `dpkg -i` o `apt install ./paquete.deb`. Se integra con el gestor de paquetes del sistema.
     - **RPM**: Paquete para Fedora, Red Hat Enterprise Linux, CentOS, openSUSE y derivadas. Se instala mediante `rpm -i` o `dnf install ./paquete.rpm`.
     - **Snap**: Paquete universal para Linux distribuido a través de la Snap Store de Canonical. Ventajas: actualizaciones automáticas, aislamiento (sandbox), funciona en 40+ distribuciones Linux.
     - **tar.gz**: Archivo comprimido genérico. Similar a AppImage pero sin el formato estándar. Menos recomendado.

4. **Iconos y personalización visual del instalador**

   - 4.1. **Requisitos de iconos por plataforma**:
     - **Windows (`.ico`)**: Formato ICO con múltiples resoluciones: 16x16, 32x32, 48x48, 64x64, 128x128, 256x256 píxeles. Se pueden generar con herramientas como ImageMagick, GIMP, o generadores online.
     - **macOS (`.icns`)**: Formato ICNS con las mismas resoluciones que Windows. Se puede generar con `iconutil` (herramienta de línea de comandos de macOS) o con herramientas como `electron-icon-builder`.
     - **Linux (`.png`)**: Formato PNG, típicamente 256x256 o 512x512 píxeles. Electron-builder acepta un directorio con varios tamaños (`16x16.png`, `32x32.png`, ..., `512x512.png`).

   - 4.2. **Herramienta recomendada: `electron-icon-builder`**:
     ```bash
     npm install --save-dev electron-icon-builder
     ```
     Crea un script en `package.json`:
     ```json
     "scripts": {
       "generate-icons": "electron-icon-builder --input=./src/assets/icon.png --output=./build/"
     }
     ```
     La imagen de entrada debe ser un PNG de al menos 1024x1024 píxeles.

   - 4.3. **Personalización del instalador NSIS (Windows)**:
     - `oneClick: false`: Muestra el asistente de instalación completo (permite elegir directorio, ver licencia, etc.). Con `true`, la instalación es silenciosa en un solo clic.
     - `perMachine: true`: Instala para todos los usuarios de la máquina (requiere permisos de administrador). Con `false`, instala solo para el usuario actual.
     - `installerSidebar`: Imagen lateral en el instalador (164x314 píxeles).
     - `uninstallDisplayName`: Nombre que aparece en "Agregar o quitar programas" de Windows.

   - 4.4. **Personalización del DMG (macOS)**:
     - `background`: Imagen de fondo del DMG (formato PNG, 540x380 píxeles). Normalmente incluye una flecha indicando al usuario que arrastre el icono de la app a la carpeta Applications.
     - `iconSize`: Tamaño de los iconos en el DMG (por defecto 80 píxeles).
     - `contents`: Array de objetos definiendo la posición de cada elemento (icono de la app y enlace a /Applications).

5. **CI/CD para Electron con GitHub Actions**

   - 5.1. **Workflow de build multiplataforma**: GitHub Actions permite ejecutar builds en runners de Windows, macOS y Linux de forma paralela (matrix strategy). Cada runner genera el instalador para su plataforma nativa.

   - 5.2. **Archivo `.github/workflows/release.yml` completo**:
     ```yaml
     name: Build and Release

     on:
       push:
         tags:
           - 'v*.*.*'  # Se activa al pushear tags de versión (ej: v1.0.0)

     jobs:
       build:
         strategy:
           matrix:
             os: [ubuntu-latest, macos-latest, windows-latest]
             include:
               - os: ubuntu-latest
                 platform: linux
               - os: macos-latest
                 platform: darwin
               - os: windows-latest
                 platform: win32

         runs-on: ${{ matrix.os }}

         steps:
           - name: Checkout code
             uses: actions/checkout@v4

           - name: Setup Node.js
             uses: actions/setup-node@v4
             with:
               node-version: '20'
               cache: 'npm'

           - name: Install dependencies
             run: npm ci

           - name: Build Angular
             run: npm run build

           - name: Build Electron (Linux)
             if: matrix.platform == 'linux'
             run: npx electron-builder --linux --publish=never

           - name: Build Electron (macOS)
             if: matrix.platform == 'darwin'
             run: npx electron-builder --mac --publish=never
             env:
               APPLE_ID: ${{ secrets.APPLE_ID }}
               APPLE_APP_SPECIFIC_PASSWORD: ${{ secrets.APPLE_APP_SPECIFIC_PASSWORD }}
               APPLE_TEAM_ID: ${{ secrets.APPLE_TEAM_ID }}
               CSC_LINK: ${{ secrets.CSC_LINK }}
               CSC_KEY_PASSWORD: ${{ secrets.CSC_KEY_PASSWORD }}

           - name: Build Electron (Windows)
             if: matrix.platform == 'win32'
             run: npx electron-builder --win --publish=never
             env:
               CSC_LINK: ${{ secrets.CSC_LINK }}
               CSC_KEY_PASSWORD: ${{ secrets.CSC_KEY_PASSWORD }}

           - name: Upload artifacts
             uses: actions/upload-artifact@v4
             with:
               name: release-${{ matrix.platform }}
               path: release/*

       create-release:
         needs: build
         runs-on: ubuntu-latest
         steps:
           - name: Download all artifacts
             uses: actions/download-artifact@v4

           - name: Create GitHub Release
             uses: softprops/action-gh-release@v1
             with:
               files: |
                 release-linux/*
                 release-darwin/*
                 release-win32/*
               draft: true
               generateReleaseNotes: true
             env:
               GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
     ```

   - 5.3. **Explicación del workflow**: El workflow se activa al pushear un tag de versión (ej: `git tag v1.0.0 && git push origin v1.0.0`). El job `build` usa una **matrix** para ejecutarse en los 3 sistemas operativos en paralelo. Cada runner instala dependencias, compila Angular, genera el instalador con electron-builder para su plataforma correspondiente, y sube los artefactos (instaladores) como artifacts de GitHub Actions. El job `create-release` (que se ejecuta al finalizar todos los builds) descarga todos los artifacts y crea una release en GitHub con los instaladores adjuntos.

6. **Firma de código (Code Signing)**

   - 6.1. **¿Por qué es importante la firma de código?**: Cuando un usuario descarga un ejecutable de internet, el sistema operativo verifica si está firmado por un desarrollador de confianza. Si no está firmado:
     - **Windows**: SmartScreen muestra una advertencia de seguridad ("Windows protegió su equipo"), en azul para aplicaciones sin firma y en rojo para aplicaciones con mala reputación. Muchos usuarios abandonan la instalación al ver este mensaje. Para conseguir reputación, se necesita un certificado de firma de código (Code Signing Certificate), preferiblemente Extended Validation (EV), que cuesta entre 200-400 €/año.
     - **macOS**: Gatekeeper bloquea la aplicación mostrando un mensaje de que "no se puede abrir porque es de un desarrollador no identificado". Para sortear esto, el usuario debe ir a Preferencias del Sistema > Seguridad y privacidad y autorizar manualmente la aplicación. Con un Apple Developer ID Certificate ($99/año), la aplicación puede ser notarizada por Apple, eliminando esta fricción.
     - **Linux**: La firma GPG es opcional pero recomendable para paquetes distribuidos a través de repositorios oficiales.

   - 6.2. **Firma en Windows**: Se necesita un archivo `.pfx` (PKCS#12) con el certificado y la clave privada. Se configura con `CSC_LINK` (ruta al `.pfx` o cadena base64) y `CSC_KEY_PASSWORD` (contraseña del `.pfx`). En CI/CD, estos valores se almacenan como secrets de GitHub.

   - 6.3. **Firma y notarización en macOS**: Proceso más complejo:
     1. Obtener un Apple Developer ID Certificate desde developer.apple.com.
     2. Exportar el certificado como `.p12` con su contraseña (CSC_KEY_PASSWORD).
     3. Generar una App-Specific Password para la cuenta de Apple ID (se usa `APPLE_APP_SPECIFIC_PASSWORD`).
     4. Configurar `hardenedRuntime: true` y los entitlements necesarios.
     5. electron-builder se encarga automáticamente de firmar la app con `CSC_LINK` y de notarizarla ante Apple (`notarize: true` en la configuración de macOS).

   - 6.4. **Entitlements en macOS**: Los entitlements son permisos específicos que la aplicación necesita para funcionar (acceso a cámara, micrófono, red, USB, etc.). Se definen en archivos `.plist`:

     ```xml
     <?xml version="1.0" encoding="UTF-8"?>
     <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
     <plist version="1.0">
     <dict>
       <key>com.apple.security.cs.allow-jit</key>
       <true/>
       <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
       <true/>
       <key>com.apple.security.cs.allow-dyld-environment-variables</key>
       <true/>
       <key>com.apple.security.device.audio-input</key>
       <true/>
       <key>com.apple.security.device.camera</key>
       <true/>
       <key>com.apple.security.files.user-selected.read-write</key>
       <true/>
       <key>com.apple.security.network.client</key>
       <true/>
     </dict>
     </plist>
     ```

7. **Actualizaciones automáticas (electron-updater)**

   - 7.1. **Instalación**:
     ```bash
     npm install electron-updater
     ```

   - 7.2. **Principio de funcionamiento**: `electron-updater` compara la versión instalada (definida en `package.json`) con la última versión disponible en el servidor de actualizaciones (por ejemplo, la release más reciente en GitHub). Si hay una versión más reciente, descarga los archivos de actualización en segundo plano y los aplica cuando la aplicación se reinicia.

   - 7.3. **Configuración en el proceso principal (`main.js`)**:
     ```javascript
     const { autoUpdater } = require('electron-updater');

     // Configurar el proveedor de actualizaciones
     autoUpdater.autoDownload = false;  // No descargar automáticamente (mejor UX)
     autoUpdater.autoInstallOnAppQuit = true;  // Instalar al cerrar la app

     // Comprobar actualizaciones al iniciar
     app.whenReady().then(() => {
       createWindow();
       autoUpdater.checkForUpdatesAndNotify();
     });

     // Eventos del autoUpdater
     autoUpdater.on('checking-for-update', () => {
       mainWindow.webContents.send('update:checking');
     });

     autoUpdater.on('update-available', (info) => {
       mainWindow.webContents.send('update:available', info);
     });

     autoUpdater.on('update-not-available', (info) => {
       mainWindow.webContents.send('update:not-available', info);
     });

     autoUpdater.on('download-progress', (progressObj) => {
       mainWindow.webContents.send('update:download-progress', progressObj);
     });

     autoUpdater.on('update-downloaded', (info) => {
       mainWindow.webContents.send('update:downloaded', info);
     });

     autoUpdater.on('error', (err) => {
       mainWindow.webContents.send('update:error', err.message);
     });

     // Escuchar peticiones del renderizador
     ipcMain.handle('update:download', () => autoUpdater.downloadUpdate());
     ipcMain.handle('update:install', () => autoUpdater.quitAndInstall());
     ```

   - 7.4. **Experiencia de usuario recomendada**: Al detectar una actualización disponible, notificar al usuario con un diálogo no intrusivo (no forzar la actualización). Mostrar progreso de descarga. Cuando la descarga termine, preguntar si desea reiniciar ahora para aplicar la actualización o posponerlo. La actualización se aplica al reiniciar la aplicación.

8. **Tiendas de aplicaciones**

   - 8.1. **Microsoft Store**: Requiere una cuenta de desarrollador ($19 USD pago único para particulares). La aplicación se empaqueta como **AppX/MSIX**. Ventajas: distribución a millones de usuarios, actualizaciones automáticas gestionadas por la tienda, instalación/desinstalación limpias, los usuarios confían más en aplicaciones de la tienda oficial. Desventajas: proceso de revisión (menos estricto que Apple), limitaciones técnicas (no se puede usar `shell.openExternal` libremente, algunas APIs de Electron están restringidas), requiere Windows 10/11.

   - 8.2. **Mac App Store**: Requiere Apple Developer Program ($99/año). La aplicación debe cumplir estrictas directrices: sandbox obligatorio (la app se ejecuta en un entorno aislado y solo puede acceder a los recursos que declare explícitamente), uso exclusivo de APIs públicas de Apple, interfaz de usuario de calidad, privacidad del usuario (describir qué datos se recopilan y por qué). El proceso de revisión puede llevar de 1 a 7 días y las aplicaciones son rechazadas con frecuencia la primera vez. Ventajas: acceso al ecosistema de usuarios de Apple, confianza del usuario, actualizaciones automáticas, facturación integrada (para apps de pago).

   - 8.3. **Snap Store (Linux)**: Gestionada por Canonical. La aplicación se empaqueta como Snap usando `snapcraft`. Ventajas: funciona en más de 40 distribuciones Linux, actualizaciones automáticas, sandbox de seguridad, canales de distribución (stable, candidate, beta, edge). Requiere un archivo `snapcraft.yaml` con la configuración del paquete.

9. **Estrategia de distribución dual: web + escritorio**

   - 9.1. **Un código base, dos destinos**: La misma aplicación Angular puede desplegarse como SPA web en un servidor (Vercel, Netlify, servidor propio) y empaquetarse como aplicación de escritorio con Electron. Esto maximiza el alcance: usuarios que prefieren web pueden usar la SPA, usuarios que necesitan funcionalidades nativas pueden instalar la app de escritorio.

   - 9.2. **Configuración de environments en Angular**: Se crean dos environments:
     ```typescript
     // environment.web.ts
     export const environment = {
       production: true,
       platform: 'web'
     };

     // environment.electron.ts
     export const environment = {
       production: true,
       platform: 'electron'
     };
     ```

     Y en `angular.json` se configuran dos configuraciones de build:
     ```json
     "configurations": {
       "production": { /* build normal, usa environment.web.ts */ },
       "electron": { "fileReplacements": [{ "replace": "src/environments/environment.ts", "with": "src/environments/environment.electron.ts" }] }
     }
     ```

   - 9.3. **Comportamiento condicionado por plataforma**:
     ```typescript
     @Injectable({ providedIn: 'root' })
     export class PlatformService {
       private electronService = inject(ElectronService);
       private http = inject(HttpClient);

       async openFile(): Promise<any> {
         if (this.electronService.isElectron()) {
           // En escritorio: diálogo nativo
           return this.electronService.openFile();
         } else {
           // En web: subir archivo del navegador
           return this.openFileViaBrowser();
         }
       }

       async saveData(data: any): Promise<void> {
         if (this.electronService.isElectron()) {
           await this.electronService.saveFile(JSON.stringify(data));
         } else {
           // En web: enviar a servidor
           await firstValueFrom(this.http.post('/api/data', data));
         }
       }
     }
     ```

10. **Gestión de dependencias nativas y problemas de compatibilidad**

    - 10.1. **Módulos nativos de Node.js**: Algunas dependencias npm incluyen código compilado en C/C++ (**módulos nativos**) que requiere `node-gyp` y un entorno de compilación (Visual Studio Build Tools en Windows, Xcode Command Line Tools en macOS, build-essential en Linux). Ejemplos: `sharp` (procesamiento de imágenes), `sqlite3` (base de datos), `bcrypt` (hashing).

    - 10.2. **Estrategias para manejar módulos nativos**:
      - **Rebuild**: `electron-builder` soporta la opción `"npmRebuild": true` que recompila automáticamente los módulos nativos para la versión de Electron que se está usando. Esto requiere que el entorno de build tenga las herramientas de compilación instaladas.
      - **Prebuild**: Algunos módulos proporcionan binarios precompilados para diferentes plataformas y versiones de Electron (por ejemplo, `sharp` y `sqlite3`).
      - **Evitar módulos nativos**: Cuando sea posible, usar alternativas puras en JavaScript. Por ejemplo, `bcryptjs` (JavaScript puro, aunque más lento) en lugar de `bcrypt` (módulo nativo).

## Ejemplos guiados

### Ejemplo 1: Configurar electron-builder y generar instalador para Windows

**Objetivo**: Configurar **electron-builder** en un proyecto Angular + Electron y generar un instalador NSIS para Windows.

**Paso 1**: Asegurarse de que el proyecto tiene la estructura correcta:
- `main.js` en la raíz.
- `preload.js` en la raíz.
- `package.json` con `"main": "main.js"`.

**Paso 2**: Instalar electron-builder:
```bash
npm install --save-dev electron-builder
```

**Paso 3**: Añadir la configuración `"build"` en `package.json` como se describió en la sección 2.3 del desarrollo teórico.

**Paso 4**: Crear los directorios y archivos necesarios:
- `build/`: carpeta para recursos de build (iconos, fondos, certificados).
- `build/icon.ico`: icono de la aplicación en formato ICO (múltiples resoluciones).

**Paso 5**: Añadir scripts en `package.json`:
```json
"scripts": {
  "build:electron": "ng build --configuration production && electron-builder",
  "build:electron:win": "ng build --configuration production && electron-builder --win",
  "build:electron:mac": "ng build --configuration production && electron-builder --mac",
  "build:electron:linux": "ng build --configuration production && electron-builder --linux"
}
```

**Paso 6**: Ejecutar el build para Windows:
```bash
npm run build:electron:win
```

**Paso 7**: Verificar los archivos generados en `release/`:
- `Mi Aplicación Setup 1.0.0.exe` (instalador NSIS).
- `Mi Aplicación 1.0.0.exe` (versión portable, si se configuró).
- `builder-effective-config.yaml` (configuración efectiva aplicada).
- `latest.yml` (archivo de metadatos para auto-update).

**Paso 8**: Probar el instalador generado en una máquina Windows:
- Ejecutar el instalador (`Mi Aplicación Setup 1.0.0.exe`).
- Verificar que el asistente de instalación se muestra correctamente (en español, si se configuró).
- Completar la instalación.
- Verificar que la aplicación se abre correctamente desde el acceso directo del escritorio.
- Verificar que la aplicación aparece en "Agregar o quitar programas".
- Desinstalar la aplicación y verificar que no quedan residuos.

### Ejemplo 2: Configurar auto-update con electron-updater y GitHub Releases

**Objetivo**: Implementar un sistema de actualizaciones automáticas que descargue nuevas versiones desde **GitHub Releases**.

**Paso 1**: Instalar electron-updater:
```bash
npm install electron-updater
```

**Paso 2**: Configurar el proveedor de publicación en `package.json` (campo `"build"`):
```json
"build": {
  "publish": [
    {
      "provider": "github",
      "owner": "TU_USUARIO_GITHUB",
      "repo": "TU_REPOSITORIO",
      "releaseType": "release"
    }
  ]
}
```

**Paso 3**: Implementar la lógica de auto-update en `main.js` como se describió en la sección 7.3 del desarrollo teórico.

**Paso 4**: Exponer los eventos de actualización al renderizador en el `preload.js`:
```javascript
contextBridge.exposeInMainWorld('electronAPI', {
  onUpdateChecking: (callback) => ipcRenderer.on('update:checking', callback),
  onUpdateAvailable: (callback) => ipcRenderer.on('update:available', (e, info) => callback(info)),
  onUpdateProgress: (callback) => ipcRenderer.on('update:download-progress', (e, progress) => callback(progress)),
  onUpdateDownloaded: (callback) => ipcRenderer.on('update:downloaded', (e, info) => callback(info)),
  downloadUpdate: () => ipcRenderer.invoke('update:download'),
  installUpdate: () => ipcRenderer.invoke('update:install')
});
```

**Paso 5**: Crear un componente de notificación de actualización en Angular:
```typescript
@Component({
  selector: 'app-update-notification',
  standalone: true,
  template: `
    @if (updateAvailable()) {
      <div class="fixed bottom-4 right-4 bg-blue-600 text-white p-4 rounded-lg shadow-lg max-w-sm z-50">
        @if (!downloading() && !downloaded()) {
          <p class="font-semibold mb-2">¡Nueva versión disponible!</p>
          <p class="text-sm mb-3">Versión {{ updateVersion() }} está lista para descargar.</p>
          <button (click)="startDownload()" class="px-4 py-2 bg-white text-blue-600 rounded font-medium">
            Descargar ahora
          </button>
        }
        @if (downloading()) {
          <p class="font-semibold mb-2">Descargando actualización...</p>
          <div class="w-full bg-blue-800 rounded-full h-2 mb-2">
            <div class="bg-white rounded-full h-2" [style.width]="downloadProgress() + '%'"></div>
          </div>
          <p class="text-sm">{{ downloadProgress() }}%</p>
        }
        @if (downloaded()) {
          <p class="font-semibold mb-2">¡Actualización descargada!</p>
          <p class="text-sm mb-3">Se instalará al reiniciar la aplicación.</p>
          <button (click)="installNow()" class="px-4 py-2 bg-white text-blue-600 rounded font-medium">
            Reiniciar ahora
          </button>
        }
      </div>
    }
  `
})
export class UpdateNotificationComponent implements OnInit {
  private electronService = inject(ElectronService);

  updateAvailable = signal(false);
  updateVersion = signal('');
  downloading = signal(false);
  downloadProgress = signal(0);
  downloaded = signal(false);

  ngOnInit(): void {
    this.electronService.onUpdateAvailable((info) => {
      this.updateAvailable.set(true);
      this.updateVersion.set(info.version);
    });

    this.electronService.onUpdateProgress((progress) => {
      this.downloading.set(true);
      this.downloadProgress.set(Math.round(progress.percent));
    });

    this.electronService.onUpdateDownloaded(() => {
      this.downloading.set(false);
      this.downloaded.set(true);
    });
  }

  startDownload(): void {
    this.downloading.set(true);
    this.electronService.downloadUpdate();
  }

  installNow(): void {
    this.electronService.installUpdate();
  }
}
```

### Ejemplo 3: Workflow de GitHub Actions para build multiplataforma

**Objetivo**: Configurar un pipeline de CI/CD con **GitHub Actions** que compile la aplicación para las 3 plataformas simultáneamente y publique los instaladores en una GitHub Release.

**Paso 1**: Crear el archivo `.github/workflows/release.yml` con el contenido descrito en la sección 5.2 del desarrollo teórico.

**Paso 2**: Configurar los secrets necesarios en GitHub (Settings > Secrets and variables > Actions):
- `CSC_LINK`: Certificado de firma de código (base64 del archivo `.pfx` o `.p12`).
- `CSC_KEY_PASSWORD`: Contraseña del certificado.
- `APPLE_ID`: Apple ID del desarrollador (solo para macOS).
- `APPLE_APP_SPECIFIC_PASSWORD`: Contraseña específica de aplicación de Apple.
- `APPLE_TEAM_ID`: Team ID de Apple Developer.
- `GH_TOKEN` o `GITHUB_TOKEN`: Se configura automáticamente, no es necesario añadirlo.

**Paso 3**: Crear un tag de versión y pushearlo a GitHub:
```bash
git tag v1.0.0
git push origin v1.0.0
```

**Paso 4**: Verificar en GitHub Actions que los 3 jobs de build se ejecutan en paralelo y finalizan correctamente.

**Paso 5**: Verificar en GitHub Releases que se ha creado una nueva release (en estado "draft") con los 3 instaladores adjuntos.

**Paso 6**: Revisar la release, editar las notas de la versión si es necesario, y publicarla (cambiar de "draft" a "published").

## Actividades guiadas

### Actividad guiada 1: Empaquetado de la aplicación "Gestor de Notas"

**Duración**: 90 minutos  
**Nivel**: Medio  
**Agrupamiento**: Parejas

**Objetivo**: Empaquetar la aplicación "Gestor de Notas" desarrollada en la unidad anterior como instalador nativo para el sistema operativo del alumno.

**Instrucciones**:

1. Partiendo del proyecto "Gestor de Notas" (Angular + Electron) desarrollado en la unidad 20, instala electron-builder: `npm install --save-dev electron-builder`.
2. Crea un icono para la aplicación: diseña un icono simple de 1024x1024 píxeles (puedes usar Figma, GIMP o Inkscape) y genera los formatos necesarios:
   - Windows: `.ico` (con múltiples resoluciones).
   - macOS: `.icns`.
   - Linux: varios PNGs de diferentes tamaños en una carpeta `build/icons/`.
3. Configura el campo `"build"` en `package.json` con la configuración para tu plataforma (siguiendo los ejemplos de la sección 2.3).
4. Configura los scripts `build:electron` y `build:electron:TU_PLATAFORMA` en `package.json`.
5. Ejecuta el build: `npm run build:electron:TU_PLATAFORMA`.
6. Si estás en Windows: prueba el instalador `.exe`. Verifica que la aplicación se instala, se abre, y se desinstala correctamente.
   Si estás en macOS: prueba el `.dmg`. Verifica que la aplicación se puede arrastrar a `/Applications`.
   Si estás en Linux: prueba el `.AppImage`. Verifica que la aplicación se ejecuta.
7. Documenta los pasos seguidos y los problemas encontrados.

**Criterios de evaluación**:
- El instalador se genera sin errores.
- La aplicación instalada funciona correctamente (se abre, las funcionalidades de Electron —menú nativo, diálogos de archivo— operan correctamente).
- La desinstalación es limpia.

### Actividad guiada 2: Configuración de actualizaciones automáticas

**Duración**: 60 minutos  
**Nivel**: Medio-Alto  
**Agrupamiento**: Individual

**Objetivo**: Implementar un sistema de auto-actualización en la aplicación "Gestor de Notas" usando **electron-updater** y GitHub Releases.

**Instrucciones**:

1. Instala electron-updater: `npm install electron-updater`.
2. Configura el proveedor de GitHub en `package.json` (campo `"build"` > `"publish"`).
3. Implementa la lógica de auto-update en `main.js` (siguiendo el ejemplo de la sección 7.3 del desarrollo teórico).
4. Expón los eventos de actualización al renderizador en `preload.js`.
5. Crea el componente `UpdateNotificationComponent` en Angular (siguiendo el ejemplo 2).
6. Integra el componente en `AppComponent`.
7. Para probar en desarrollo: crea un tag de versión ficticio (`v0.0.1`), genera un build, súbelo a GitHub como release, luego cambia la versión a `v0.0.2` en `package.json` y ejecuta `npm run electron:dev`. El auto-updater debería detectar la "nueva versión" disponible (aunque en desarrollo apunta a localhost).

**Criterios de evaluación**:
- El sistema de auto-update se inicializa sin errores al arrancar la aplicación.
- Los eventos del auto-updater se comunican correctamente al renderizador.
- El componente de notificación muestra la información adecuadamente.

### Actividad guiada 3: Pipeline CI/CD con GitHub Actions

**Duración**: 90 minutos  
**Nivel**: Alto  
**Agrupamiento**: Individual

**Objetivo**: Configurar un flujo de trabajo de **GitHub Actions** que compile la aplicación y publique los instaladores como release de GitHub.

**Instrucciones**:

1. Asegúrate de que el proyecto "Gestor de Notas" está en un repositorio de GitHub.
2. Crea el archivo `.github/workflows/release.yml` con el contenido de la sección 5.2 del desarrollo teórico, adaptando los paths y comandos a tu proyecto.
3. Configura los secrets necesarios en GitHub (Settings > Secrets and variables > Actions):
   - `GH_TOKEN` (necesario para crear releases, usa un Personal Access Token con permisos de repo).
   - Para macOS, necesitarás los secrets de Apple si quieres firmar la aplicación.
   - Para Windows, necesitarás el certificado de firma si quieres firmar.
   (Para esta actividad de aprendizaje, puedes omitir la firma de código —añade `"verifyUpdateCodeSignature": false` en la configuración de Windows— y centrarte en el flujo de build.)
4. Crea un tag de versión de prueba: `git tag v1.0.0-beta.1 && git push origin v1.0.0-beta.1`.
5. Ve a la pestaña "Actions" del repositorio en GitHub y observa cómo se ejecutan los jobs en paralelo para las 3 plataformas.
6. Al finalizar, verifica que se ha creado una release (o draft release) con los archivos adjuntos.
7. Si algún job falla, analiza los logs, corrige los errores y vuelve a intentarlo.
8. Documenta el proceso completo, incluyendo los problemas encontrados y sus soluciones.

**Criterios de evaluación**:
- El workflow se ejecuta correctamente para al menos 1 plataforma (idealmente las 3).
- Los artefactos (instaladores) se generan y se adjuntan a la release.
- El alumno es capaz de explicar el flujo completo y depurar errores en los logs de GitHub Actions.

## Actividades propuestas

### Actividad propuesta 1: Personalización completa del instalador (Dificultad: Media)

Personaliza el instalador de tu aplicación al máximo nivel de detalle:

1. Diseña un icono de aplicación profesional con al menos 5 variantes (color, monocromo, pequeño, grande, con texto) usando Figma.
2. Genera los formatos de icono para las 3 plataformas.
3. Personaliza el instalador NSIS para Windows: texto de bienvenida, licencia (EULA) en español, imagen de fondo o sidebar, colores del instalador, textos personalizados en cada paso del asistente.
4. Personaliza el DMG para macOS: imagen de fondo con flecha indicativa, iconos con el tamaño y posición correctos.
5. Personaliza los metadatos de la aplicación para Linux: descripción completa en el formato `.desktop`, categoría correcta, capturas de pantalla para la tienda de software.
6. Prueba todos los instaladores personalizados.

### Actividad propuesta 2: Estrategia de distribución dual web + escritorio (Dificultad: Alta)

Implementa una estrategia completa de **distribución dual** para una aplicación de notas:

1. Configura los environments de Angular (`environment.web.ts` y `environment.electron.ts`).
2. Implementa un `PlatformService` que abstraiga las diferencias entre web y escritorio.
3. Despliega la versión web en Vercel o Netlify (gratuito).
4. Genera los instaladores de escritorio para las 3 plataformas.
5. Implementa un sistema de sincronización de datos entre la versión web y la de escritorio usando una API REST simple (json-server o Firebase).
6. Añade una landing page que detecte la plataforma del usuario y le ofrezca la opción más adecuada (descargar instalador para escritorio o usar la versión web).

### Actividad propuesta 3: Configuración de firma de código y notarización (Dificultad: Alta)

Investiga y documenta el proceso completo de **firma de código** y notarización (sin necesidad de adquirir certificados reales, que son de pago):

1. Investiga los requisitos y precios de los certificados de firma de código para cada plataforma (Authenticode para Windows, Apple Developer ID para macOS).
2. Describe el proceso paso a paso para obtener cada certificado.
3. Configura electron-builder para firmar la aplicación en Windows y macOS.
4. Configura la notarización de Apple (`notarize: true` y las variables de entorno necesarias).
5. Explica las diferencias entre un certificado OV (Organization Validation) y EV (Extended Validation) en Windows, y por qué el EV reduce las advertencias de SmartScreen más rápidamente.
6. Documenta el coste total anual de distribuir una aplicación Electron firmada en las 3 plataformas.

### Actividad propuesta 4: Empaquetado para tiendas de aplicaciones (Dificultad: Alta)

Prepara la aplicación para su publicación en las tiendas oficiales:

1. Configura el empaquetado para Microsoft Store (AppX/MSIX): crea el manifiesto, configura los permisos, genera el paquete.
2. Configura el empaquetado para Mac App Store: configura el sandbox, los entitlements, el `provisioning profile`, y prueba la app en modo sandbox para detectar APIs no permitidas.
3. Configura el empaquetado Snap para Linux: crea el archivo `snapcraft.yaml`, configura el confinement (`strict` vs `classic`), y los plugs de conexión al sistema.
4. Para cada tienda, documenta los requisitos, el proceso de revisión, y las principales razones de rechazo que debes evitar.

### Actividad propuesta 5: Automatización completa de versionado y release (Dificultad: Media-Alta)

Implementa un flujo de trabajo automatizado de **versionado semántico** y release:

1. Configura `standard-version` o `semantic-release` para automatizar el versionado basado en commits convencionales (feat, fix, BREAKING CHANGE).
2. Configura el workflow de GitHub Actions para que:
   - Al pushear a `main`, se ejecuten tests y lint.
   - Al crear un PR hacia `main`, se ejecute un build de prueba.
   - Al fusionar un PR con commits `feat:` o `fix:`, se genere automáticamente un tag de versión, se compile para las 3 plataformas, se cree una GitHub Release con notas generadas automáticamente, y se publique la actualización para los usuarios existentes mediante electron-updater.
3. Configura un canal "beta" para releases pre-release (versiones con sufijo `-beta.1`).
4. Documenta todo el flujo en un diagrama.

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Análisis de rendimiento y optimización del empaquetado

    Investiga y aplica técnicas avanzadas de optimización del empaquetado:

    1. Analiza el tamaño de tu instalador con herramientas como `du -sh` y `7z l` para identificar los archivos que más contribuyen al tamaño total.
    2. Aplica las opciones de compresión de electron-builder: `compression: 'maximum'` en NSIS, diferentes niveles de compresión.
    3. Implementa ASAR (Atom Shell Archive) para empaquetar los recursos de la aplicación en un archivo comprimido.
    4. Configura `extraResources` vs `files` para separar recursos que no necesitan estar en el ASAR.
    5. Analiza el impacto del tree shaking de Angular en el tamaño del build y configura `"optimization": true` en `angular.json`.
    6. Mide el tiempo de arranque en frío de la aplicación y propón mejoras (lazy loading de módulos, diferir inicializaciones no críticas).

    ### Actividad de ampliación 2: Soporte multi-idioma en el instalador

    Investiga y configura el soporte para múltiples idiomas en los instaladores:

    1. Configura NSIS para soportar español e inglés (y opcionalmente otros idiomas).
    2. Traduce todos los textos del instalador: títulos, mensajes, botones, licencia.
    3. Configura la detección automática del idioma del sistema operativo para seleccionar el idioma por defecto del instalador.
    4. Investiga cómo hacer lo mismo para el instalador PKG en macOS y DEB/RPM en Linux.

    ### Actividad de ampliación 3: Sistema de telemetría y analítica de instalaciones

    Diseña e implementa un sistema básico de analítica para tu aplicación:

    1. Implementa un sistema de telemetría anónimo y respetuoso con la privacidad (opt-in, GDPR compliant) que registre: número de instalaciones, versión de la app, sistema operativo, frecuencia de uso, funcionalidades más utilizadas.
    2. Utiliza un servicio gratuito como Google Analytics Measurement Protocol, Plausible, o PostHog.
    3. Implementa el envío de eventos desde el proceso principal de Electron.
    4. Añade una pantalla de configuración de privacidad donde el usuario pueda activar/desactivar la telemetría.
    5. Documenta qué datos se recopilan y por qué, en cumplimiento del RGPD (GDPR) europeo.

!!! tip "Buenas prácticas"

    1. **Versionado semántico (SemVer) estricto**: Usa versiones en formato `MAJOR.MINOR.PATCH` (ej: `2.1.4`). Incrementa MAJOR para cambios incompatibles (breaking changes), MINOR para nuevas funcionalidades compatibles, y PATCH para correcciones de bugs. Electron-builder y electron-updater dependen de este esquema para determinar si una actualización es compatible.

    2. **Prueba los instaladores antes de publicar**: ==Nunca publiques un instalador sin haberlo probado en una máquina limpia== (máquina virtual o equipo de pruebas). Los errores en el instalador son extremadamente costosos porque afectan a la primera impresión del usuario y pueden ser difíciles de corregir (el usuario ya tiene una versión rota instalada).

    3. **Firma de código desde el primer release público**: Aunque los certificados de firma de código tienen un coste, la pérdida de usuarios por advertencias de seguridad supera con creces ese coste. Prioriza la firma de código desde el primer release público.

    4. **Mantén los canales de auto-update separados**: No mezcles versiones beta/alpha con versiones estables en el mismo canal de actualización. Usa canales separados (`stable`, `beta`, `alpha`) para que los usuarios que optaron por la versión estable no reciban versiones inestables.

    5. **Gestiona los breaking changes con migraciones automáticas**: Si una nueva versión cambia el formato de los datos almacenados localmente, implementa una migración automática que se ejecute al arrancar la nueva versión, en lugar de romper la aplicación del usuario.

    6. **Documenta el proceso de build y release**: Crea un archivo `RELEASE.md` o `CONTRIBUTING.md` que documente los pasos exactos para generar un nuevo release. Esto es crucial cuando el proyecto crece y varias personas participan en los releases.

    7. **Usa `.gitignore` adecuadamente**: Añade al `.gitignore` las carpetas `release/`, `dist/` (a veces), y archivos grandes como binarios de Electron descargados. No incluyas instaladores ni binarios compilados en el repositorio Git (para eso están las GitHub Releases y el almacenamiento de artefactos).

    8. **Monitoriza el tamaño del instalador**: Un instalador de más de 200 MB será un obstáculo significativo para muchos usuarios (especialmente en países con conexiones lentas). Revisa periódicamente qué está contribuyendo al tamaño e intenta reducirlo (excluyendo dependencias innecesarias, comprimiendo assets, usando `asar`).

    9. **Proporciona múltiples opciones de descarga**: No obligues a todos los usuarios a usar el mismo formato de instalador. En Windows, ofrece tanto NSIS (para la mayoría) como portable (para entornos corporativos). En Linux, ofrece AppImage (para usuarios noveles) y DEB/RPM (para usuarios avanzados).

    10. **Notifica a los usuarios sobre las actualizaciones de forma respetuosa**: No fuerces las actualizaciones (a menos que sea un parche de seguridad crítico). Permite al usuario posponer la actualización, pero recuérdasela periódicamente. No descargues grandes cantidades de datos en segundo plano sin el consentimiento del usuario.

!!! warning "Errores frecuentes"

    1. **No configurar `appId` o configurarlo incorrectamente**: El `appId` debe ser único y seguir el formato reverse-domain (`com.empresa.app`). Si no se configura, electron-builder usará un valor por defecto. Si se cambia en una versión posterior, el sistema operativo tratará la nueva versión como una aplicación diferente, causando duplicados en el sistema y rompiendo las actualizaciones automáticas.

    2. **Olvidar excluir las dependencias de desarrollo del empaquetado**: Por defecto, electron-builder incluye todas las dependencias de `node_modules`. Si no se configuran correctamente los patrones `files` para excluir `devDependencies`, el instalador incluirá electron-builder, TypeScript, ESLint y todas las herramientas de desarrollo, inflando innecesariamente el tamaño del instalador a cientos de megabytes.

    3. **No recompilar módulos nativos para Electron**: Las dependencias nativas compiladas para Node.js no son compatibles con la versión de Node.js incluida en Electron (que puede ser diferente). Es necesario recompilarlas con `electron-rebuild` o configurar `"npmRebuild": true` en electron-builder. Si no se hace, la aplicación fallará al iniciar con errores como `Error: The module was compiled against a different Node.js version`.

    4. **Configurar incorrectamente las rutas de archivos en producción**: Durante el desarrollo, la aplicación Angular se ejecuta en `http://localhost:4200` y los assets se cargan desde el sistema de archivos del proyecto. En producción empaquetada, las rutas son diferentes. `__dirname` en el proceso principal apunta a la carpeta `resources/app/` dentro del ASAR. Las rutas a archivos (`preload.js`, `assets/`) deben construirse con `path.join(__dirname, ...)`.

    5. **No gestionar correctamente los permisos de macOS**: A partir de macOS Catalina, las aplicaciones deben solicitar permisos explícitos para acceder a ciertos recursos (cámara, micrófono, archivos, contactos, calendario). Estos permisos deben declararse en los entitlements y en el `Info.plist`. Si no se configuran, la funcionalidad simplemente fallará sin una explicación clara para el usuario.

    6. **Ignorar la validación de SmartScreen en Windows**: Los nuevos certificados de firma de código necesitan acumular "reputación" con SmartScreen. Durante las primeras semanas o meses, incluso una aplicación firmada puede mostrar advertencias de SmartScreen (aunque menos severas que sin firma). Los certificados EV (Extended Validation) aceleran este proceso.

    7. **No probar la aplicación en un entorno limpio**: "En mi máquina funciona" es la frase más peligrosa en el empaquetado. La aplicación puede funcionar en tu máquina de desarrollo porque tienes dependencias instaladas globalmente, permisos de administrador, o configuraciones específicas. Prueba siempre en una VM limpia o en una máquina de un compañero.

    8. **Configurar `publish` para apuntar a un repositorio que no existe o es privado**: electron-updater necesita acceso de lectura al repositorio de GitHub configurado. Si el repositorio es privado, se necesita configurar un `GH_TOKEN` con los permisos adecuados.

    9. **Olvidar incrementar la versión en `package.json`**: Si la versión en `package.json` no cambia, electron-updater no detectará una nueva actualización, electron-builder sobrescribirá los instaladores anteriores, y los usuarios no recibirán la actualización.

    10. **Usar `asar: false` sin entender las implicaciones**: Desempaquetar los archivos del ASAR (`asar: false`) expone todo el código fuente de la aplicación en texto plano en el sistema de archivos del usuario. Además de ser un problema de seguridad (cualquiera puede leer y modificar el código), puede causar problemas con rutas de archivo y rendimiento de carga.

!!! abstract "Resumen"

    El empaquetado y la distribución de aplicaciones es la fase que transforma el código fuente en un producto que los usuarios pueden instalar y utilizar. Esta unidad ha recorrido de forma completa y detallada todo el proceso, desde la configuración de electron-builder hasta la publicación en tiendas de aplicaciones, pasando por la automatización con CI/CD y las actualizaciones automáticas.

    La herramienta central ha sido **electron-builder**, cuya configuración en `package.json` se ha desglosado campo a campo, explicando el significado y las implicaciones de cada opción: `appId`, `productName`, `directories`, `files` (crucial para controlar qué se incluye en el paquete), y las secciones específicas por plataforma (`win`, `mac`, `linux`) con sus formatos de salida correspondientes (NSIS, portable, DMG, AppImage, DEB, RPM, Snap).

    Los formatos de salida se han detallado por plataforma, explicando cuándo usar cada uno: NSIS para instaladores tradicionales en Windows, portable para entornos corporativos, DMG para macOS fuera de la App Store, AppImage para máxima compatibilidad en Linux, DEB/RPM para integración con gestores de paquetes.

    La automatización del proceso de build y release mediante **GitHub Actions** se ha presentado como una solución práctica y gratuita para proyectos open source y pequeñas empresas. El workflow de ejemplo, con su estrategia de matrix para builds paralelos en las 3 plataformas, permite generar instaladores para Windows, macOS y Linux con un solo push de un tag de versión.

    La **firma de código** ha recibido la atención que merece como aspecto crítico para la confianza del usuario. Se han explicado los requisitos de cada plataforma (Authenticode en Windows, Apple Developer ID y notarización en macOS, GPG en Linux), los costes asociados y el impacto en la experiencia de instalación del usuario.

    El sistema de actualizaciones automáticas con **electron-updater** cierra el ciclo de vida de la aplicación, permitiendo que los usuarios reciban nuevas versiones sin esfuerzo. Se ha detallado la configuración en el proceso principal, la comunicación con el renderizador vía IPC, y la implementación de una interfaz de usuario respetuosa que notifica al usuario sin interrumpir su flujo de trabajo.

    La estrategia de **distribución dual** (web + escritorio) abre la posibilidad de maximizar el alcance de la aplicación, permitiendo que el mismo código Angular funcione en ambos entornos con comportamientos adaptados mediante environments y un `PlatformService`.

    Finalmente, las buenas prácticas y los errores frecuentes proporcionan al alumnado una guía basada en la experiencia real de la comunidad Electron, ayudándoles a evitar los errores más costosos y a adoptar las prácticas que han demostrado funcionar en proyectos reales.

## Recursos complementarios

**Documentación oficial**:
- electron-builder - Documentación: https://www.electron.build/
- electron-builder - Opciones de configuración: https://www.electron.build/configuration/configuration
- electron-updater - Documentación: https://www.electron.build/auto-update
- Electron - Guía de distribución de aplicaciones: https://www.electronjs.org/docs/latest/tutorial/application-distribution
- Electron - Empaquetado de aplicaciones: https://www.electronjs.org/docs/latest/tutorial/application-packaging

**Guías y tutoriales**:
- GitHub Actions - Documentación oficial: https://docs.github.com/en/actions
- Electron + GitHub Actions: buscar "electron github actions release" en Google
- Microsoft Store - Publicación de aplicaciones de escritorio: https://learn.microsoft.com/es-es/windows/msix/desktop/desktop-to-uwp-manual-conversion
- Apple - Notarización de aplicaciones macOS: https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution
- Snapcraft - Creación de snaps: https://snapcraft.io/docs/creating-a-snap

**Herramientas**:
- electron-icon-builder: https://github.com/safu9/electron-icon-builder
- standard-version: https://github.com/conventional-changelog/standard-version
- semantic-release: https://github.com/semantic-release/semantic-release

!!! info "Dato clave"

    **Referencias de costes (2024-2025)**:
    - Certificado de firma de código Windows (OV): ~200-300 €/año (proveedores: Sectigo, DigiCert, GlobalSign)
    - Certificado de firma de código Windows (EV): ~300-500 €/año
    - Apple Developer Program: 99 €/año
    - Cuenta de desarrollador Microsoft Store: 19 $ USD (pago único para particulares)
    - Snap Store: gratuito

**Comunidad**:
- Stack Overflow: etiquetas `[electron-builder]`, `[electron-updater]`, `[github-actions]`
- Awesome Electron - Lista curada de recursos: https://github.com/sindresorhus/awesome-electron
- Discord de la comunidad Electron: https://discord.gg/electronjs
