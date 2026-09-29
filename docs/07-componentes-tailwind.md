---
icon: lucide/component
---

# Implementación de Componentes con Tailwind CSS

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Implementar componentes de interfaz de usuario completos y reutilizables en Angular utilizando exclusivamente Tailwind CSS, comprendiendo la traducción directa entre propiedades CSS y clases utility y aplicando las convenciones de nomenclatura y organización del framework.
2. Construir sistemas completos de botones, tarjetas, formularios, tablas de datos, modales, barras de navegación y dashboards como componentes Angular autocontenidos, con todas sus variantes, tamaños y estados visuales correctamente implementados.
3. Desarrollar componentes de formulario con estados complejos (normal, hover, focus, error, disabled, read-only) utilizando validación reactiva de Angular y aplicando estilos condicionales mediante Tailwind para comunicar visualmente cada estado.
4. Implementar tablas de datos con características avanzadas como filas alternas (zebra), scroll horizontal en dispositivos móviles, indicadores visuales de ordenación, selección de filas y estados de celda, todo ello con clases de Tailwind sin CSS personalizado.
5. Construir modales accesibles con overlay semitransparente, animaciones de entrada y salida, y variantes de confirmación, aplicando las técnicas de gestión de foco y ARIA de Angular CDK en combinación con los estilos de Tailwind.
6. Diseñar barras de navegación adaptables (navbar horizontal y sidebar colapsable) y sistemas de pestañas como componentes Angular reutilizables, con animaciones de transición y comportamiento responsive.
7. Realizar una comparativa sistemática entre el enfoque de CSS tradicional y el enfoque de Tailwind para cada tipo de componente, evaluando objetivamente las ventajas e inconvenientes de cada enfoque en términos de líneas de código, legibilidad, mantenibilidad, curva de aprendizaje y consistencia del diseño, y extrayendo conclusiones aplicables a la toma de decisiones en proyectos reales.

## Resultado de aprendizaje asociado

Esta unidad contribuye, como RA principal, al **RA 3** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 3.** Crea componentes visuales valorando y empleando herramientas específicas.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE b) Se han creado componentes visuales.
- CE c) Se han definido sus métodos y propiedades con asignación de valores por defecto.
- CE d) Se han determinado los eventos a los que debe responder el componente y se les han asociado las acciones correspondientes.
- CE h) Se han programado aplicaciones cuyo interfaz gráfico utiliza los componentes creados.

Como RA secundario, se vincula al **RA 4** («Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad»):

- CE g) Se ha diseñado el aspecto de la interfaz de usuario (colores y fuentes entre otros) atendiendo a su legibilidad.

> Nota: los componentes que se implementan con Tailwind CSS (botones, formularios con validación reactiva, tablas de datos, modales y navegación) son los «componentes visuales» del RA 3, construidos con el enfoque utility-first.

!!! note "Conocimientos previos"

    Para abordar esta unidad con éxito, el alumnado debe poseer los siguientes conocimientos y destrezas:

    - Dominio de **Angular** y **TypeScript** para la creación de componentes, incluyendo el sistema de plantillas, el binding de propiedades, eventos y clases, los formularios reactivos, las señales (signals), la inyección de dependencias, y la comunicación entre componentes mediante `@Input`, `@Output` y servicios.
    - Conocimientos sólidos de **Tailwind CSS 4**, cubiertos en la Unidad 6, incluyendo la configuración con `@theme`, las clases utility de layout, espaciado, colores, tipografía, estados interactivos, modo oscuro y diseño responsive.
    - Comprensión del **modelo de estilos en Angular**: encapsulación de estilos (ViewEncapsulation.Emulated, None, ShadowDom), estilos globales vs. estilos de componente, y la interacción entre Tailwind (que genera CSS global) y el encapsulamiento de Angular.
    - Fundamentos de **accesibilidad web** (Unidad 2), necesarios para implementar componentes como modales, tablas y formularios que sean utilizables por todas las personas, incluyendo el uso de **roles ARIA**, gestión del foco con Angular CDK, y navegación por teclado.
    - Experiencia previa en la implementación de componentes con **CSS tradicional**, para poder apreciar y evaluar las diferencias con el enfoque de Tailwind en la sección comparativa final.

## Contenidos

1. **Componente 1**: Sistema completo de botones
2. **Componente 2**: Sistema de tarjetas (cards)
3. **Componente 3**: Sistema de formularios
4. **Componente 4**: Tablas de datos
5. **Componente 5**: Modales
6. **Componente 6**: Barras de navegación
7. **Componente 7**: Dashboard
8. **Comparativa sistemática**: CSS tradicional vs. Tailwind

## Desarrollo teórico

### Componente 1: Sistema Completo de Botones

El botón es el componente interactivo más ubicuo de cualquier aplicación. A pesar de su aparente simplicidad, un **sistema de botones** profesional debe cubrir un abanico considerable de variantes, tamaños y estados. Implementar este sistema con Tailwind en Angular demuestra cómo el **enfoque utility-first**, combinado con un componente reutilizable bien diseñado, produce un código más mantenible que el CSS tradicional.

El componente **Button** en Angular se define como un componente standalone que recibe mediante `@Input` sus propiedades de configuración: `variant` (que puede ser `'primary'`, `'secondary'`, `'outline'`, `'ghost'` o `'danger'`), `size` (que puede ser `'sm'`, `'md'` o `'lg'`), `disabled` (booleano), y `loading` (booleano que indica si debe mostrar un spinner y deshabilitar la interacción).

La estrategia de estilado con Tailwind se implementa mediante una **señal computada** o un método en el componente que devuelve la cadena de clases CSS correspondiente a la combinación de variante, tamaño y estado. Esta cadena se vincula a la clase del elemento `<button>` nativo mediante `[class]="buttonClasses()"`. Es fundamental usar un elemento `<button>` nativo de HTML, no un `<div>` o `<span>` con `(click)`, porque el botón nativo ya es accesible por teclado sin esfuerzo adicional.

Para la variante `primary`, las clases base incluyen el color de fondo del tema primario en su tono 500, texto blanco, bordes redondeados, y transiciones suaves para los cambios de estado: `bg-primary-500 text-white rounded-lg font-medium transition-colors duration-200`. Los estados se añaden mediante las **variantes de Tailwind**: `hover:bg-primary-600` para el hover, `active:bg-primary-700` para el clic activo, `focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:ring-offset-2 focus-visible:outline-none` para el foco visible solo con teclado, y `disabled:opacity-50 disabled:cursor-not-allowed` para el estado deshabilitado.

La variante `secondary` utiliza un fondo gris claro con texto oscuro: `bg-gray-100 text-gray-900 hover:bg-gray-200 active:bg-gray-300`. La variante `outline` no tiene fondo, solo borde y texto del color primario: `border-2 border-primary-500 text-primary-500 bg-transparent hover:bg-primary-50 active:bg-primary-100`. La variante `ghost` es la más minimalista: sin fondo ni borde, solo texto con color primario y un sutil fondo al pasar el cursor: `text-primary-500 hover:bg-primary-50 active:bg-primary-100`. La variante `danger` usa el color de peligro: `bg-red-600 text-white hover:bg-red-700 active:bg-red-800`, con su correspondiente anillo de foco en rojo.

Los tamaños se implementan ajustando el padding y el tamaño de texto mediante clases condicionales. El tamaño `sm` usa `px-3 py-1.5 text-sm`, `md` usa `px-4 py-2 text-sm` (tamaño por defecto), y `lg` usa `px-6 py-3 text-base`. El radio del borde se mantiene consistente para todos los tamaños de una misma variante.

El estado `loading` se implementa añadiendo un **spinner SVG animado** antes del texto del botón y deshabilitando la interacción. En Angular, se usa un `@if` en la plantilla para mostrar condicionalmente el spinner: `@if (loading()) { <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-current"> ... </svg> }`. El botón se deshabilita automáticamente cuando `loading` es verdadero, pero además se vincula explícitamente `[disabled]="loading() || disabled()"` y `[attr.aria-disabled]="loading() || disabled()"`.

Cuando el botón incluye un icono, se distinguen dos casos: botón con icono y texto (icono a la izquierda o a la derecha del texto), y botón de solo icono. Para el botón de solo icono, se aplica padding simétrico (`p-2` en tamaño md) y se añade `aria-label` para accesibilidad: `<button aria-label="Eliminar elemento"><svg>...</svg></button>`. El `aria-label` debe describir la acción, no el icono: "Eliminar elemento", no "Icono de papelera".

!!! tip "Ventajas frente al CSS tradicional"

    La implementación completa en Angular produce un componente de aproximadamente 60 líneas de TypeScript y 30 líneas de plantilla HTML. ==No hay una sola línea de CSS personalizado==: todos los estilos son clases de Tailwind aplicadas condicionalmente. Las ventajas frente al **CSS tradicional** son evidentes: todas las decisiones de diseño son visibles en el código del componente, no hay que navegar a un archivo CSS separado, y la consistencia está garantizada porque todas las variantes usan los mismos **tokens de diseño** del `@theme`.

### Componente 2: Sistema de Tarjetas (Cards)

Las **tarjetas** son contenedores de información visualmente delimitados que agrupan contenido relacionado. En aplicaciones de gestión, aparecen en dashboards (widgets de estadísticas), listados (cards de entidades como clientes o productos), páginas de detalle (secciones de información), y feeds de actividad. Un sistema de tarjetas modela estas variaciones como un **componente reutilizable** con proyección de contenido (ng-content) para máxima flexibilidad.

La **card básica** es un contenedor rectangular con fondo blanco, borde redondeado, sombra sutil y padding interior: `bg-white rounded-xl shadow-sm border border-gray-200 p-6`. Esta card básica acepta cualquier contenido mediante `<ng-content>`. La card con header, body y footer utiliza tres slots de proyección de contenido nombrados (select atributo en Angular 17+) para inyectar contenido estructurado. El header típicamente lleva un fondo ligeramente diferenciado (`bg-gray-50`) y un borde inferior (`border-b border-gray-200`), con padding reducido en los laterales. El body es el área de contenido principal, con padding generoso. El footer, al igual que el header, tiene fondo diferenciado y borde superior, y suele contener acciones (botones).

La **card horizontal** es una variante donde el contenido se distribuye en fila en lugar de columna: `flex flex-col md:flex-row`. En móvil, se apila verticalmente; en desktop, se distribuye horizontalmente. Es ideal para listados de elementos donde cada card ocupa poco alto, con una imagen o icono a la izquierda y la información textual a la derecha.

La **card de estadística**, omnipresente en dashboards, muestra un valor numérico grande, un título descriptivo pequeño, y opcionalmente un indicador de tendencia y un icono. El layout interno usa `flex flex-col gap-2`. El valor se muestra con `text-3xl font-bold text-gray-900`, el título con `text-sm text-gray-500`, la tendencia con `inline-flex items-center gap-1 text-sm font-medium` y color condicional (verde para subida, rojo para bajada). Un icono decorativo (svg de un gráfico, un usuario, un carrito) se posiciona en la esquina superior derecha de la card con `absolute top-4 right-4`.

La **card con imagen**, común en aplicaciones de catálogo o gestión de productos, incluye una imagen de cabecera que ocupa todo el ancho de la card. La imagen usa `w-full h-48 object-cover rounded-t-xl` para mantener la proporción y recortar si es necesario. El contenido textual se sitúa debajo con el padding estándar. Se puede añadir un badge de estado (disponible, agotado) posicionado absolutamente sobre la imagen.

### Componente 3: Sistema de Formularios

Los **formularios** son probablemente los componentes más complejos de una aplicación de gestión en términos de estados visuales. Un campo de formulario profesional debe comunicar visualmente al menos **cinco estados**: normal (sin interacción), hover (cursor sobre el campo), focus (campo activo para escribir), error (validación fallida), disabled (no editable), y read-only (visible pero no editable). Tailwind permite implementar todos estos estados con clases condicionales, sin CSS personalizado.

El **input con label flotante** es un patrón popularizado por **Material Design** donde la etiqueta se muestra dentro del campo como placeholder cuando está vacío y se desplaza hacia arriba cuando el campo tiene foco o contenido. La implementación en Angular con Tailwind utiliza un contenedor `relative` y un `<label>` posicionado absolutamente que transiciona suavemente entre el estado de placeholder (dentro del campo, `top-1/2 -translate-y-1/2 text-gray-400`) y el estado de etiqueta flotante (arriba, `top-0 -translate-y-full text-xs text-primary-500`). La transición se controla con `transition-all duration-200` en el label. La activación del estado flotante se gestiona con una variable en el componente que se activa cuando el input recibe foco o cuando su valor no está vacío, y se vincula a las clases del label mediante `[class]`.

El **input con validación** es la variante más común en formularios de negocio. El campo muestra un borde gris en estado normal (`border-gray-300`), que cambia a azul primario en foco (`focus:border-primary-500 focus:ring-2 focus:ring-primary-200`) y a rojo en error (`border-red-500 focus:border-red-500 focus:ring-red-200`). Bajo el campo, el mensaje de error se muestra en texto rojo pequeño con un icono de advertencia, asociado al campo mediante `aria-describedby`. En Angular, la validación reactiva proporciona los estados del campo (`touched`, `dirty`, `invalid`, `valid`), que se traducen a clases condicionales en la plantilla.

El **select personalizado** reemplaza el `<select>` nativo (cuyo estilado es limitado en algunos navegadores) por un componente que renderiza un `<button>` con la apariencia de un input y un dropdown posicionado absolutamente. Las opciones se navegan con teclado utilizando `FocusKeyManager` de **Angular CDK**. Visualmente, el select cerrado es idéntico a un input; al abrirse, muestra una lista desplegable con cada opción estilada como `px-4 py-2 hover:bg-gray-100 cursor-pointer`, y la opción seleccionada con `bg-primary-50 text-primary-700 font-medium`.

El **checkbox** y el **radio button** personalizados ocultan el input nativo mediante `sr-only` (visible para lectores de pantalla, invisible visualmente) y renderizan un elemento visual que refleja el estado. Para el checkbox, un `<span>` con borde redondeado pequeño (`w-5 h-5 rounded border-2 border-gray-300`) muestra un checkmark SVG cuando está marcado, y cambia a `bg-primary-500 border-primary-500` con el checkmark en blanco. El estado `disabled` atenúa los colores (`opacity-50`). La interacción del input nativo oculto se vincula al elemento visual mediante un `<label>` que envuelve ambos, haciendo que el clic en cualquier parte active el checkbox.

El **toggle switch** es un checkbox estilizado como un interruptor de encendido/apagado. Consiste en un contenedor redondeado (`w-11 h-6 rounded-full`) que cambia de color de fondo según el estado (gris para apagado, color primario para encendido) y contiene un círculo blanco que se desplaza horizontalmente con `transition-transform duration-200` y `translate-x-5` cuando está activo. La implementación es completamente visual: el `<input type="checkbox">` está oculto con `sr-only` y el elemento visual reacciona al estado mediante el binding de Angular.

El **formulario de login** completo integra todos estos componentes en una composición real. Un contenedor centrado vertical y horizontalmente (`min-h-screen flex items-center justify-center bg-gray-100`), una tarjeta blanca con sombra (`bg-white rounded-2xl shadow-xl p-8 w-full max-w-md`), dos campos de input (email y contraseña) con sus etiquetas, estados de validación, un checkbox de "Recordarme", un enlace de "Olvidé mi contraseña", un botón de envío con estado loading, y un enlace a registro. Todo el formulario está gestionado por un `FormGroup` de Angular con validadores síncronos (required, email, minLength) y asíncronos (verificación de credenciales simulada con delay). El botón de envío se deshabilita mientras el formulario es inválido o está enviando. Tras el envío exitoso, un toast verde confirma el acceso y se redirige al dashboard.

### Componente 4: Tablas de Datos

Las **tablas de datos** son el componente central de la mayoría de aplicaciones de gestión empresarial. Una buena tabla debe ser legible, escaneable, accesible y adaptable a diferentes tamaños de pantalla. Tailwind proporciona clases específicas que simplifican la implementación de todas estas características.

La tabla básica utiliza los elementos HTML semánticos `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>` y `<td>` con las clases de Tailwind para el estilado. El `<table>` completo lleva `w-full text-sm text-left`. Las celdas de encabezado (`<th>`) llevan `px-4 py-3 font-medium text-gray-500 uppercase tracking-wider text-xs bg-gray-50 border-b border-gray-200`. Las celdas de datos (`<td>`) llevan `px-4 py-3 text-gray-700 border-b border-gray-100`. Los bordes inferiores (`border-b`) crean líneas divisorias entre filas, más sutiles en las celdas de datos.

La tabla con **filas alternas (zebra)** es una mejora de legibilidad que alterna colores de fondo entre filas. Tailwind proporciona las variantes `odd:` y `even:` para esto. Añadiendo `even:bg-gray-50` al `<tr>` se consigue el efecto zebra sin modificar las celdas individuales. En tablas grandes, el zebra reduce errores de lectura al ayudar a la vista a seguir una misma fila horizontalmente.

La **tabla responsive** es probablemente la característica más importante en aplicaciones modernas. En pantallas pequeñas, una tabla con muchas columnas desborda horizontalmente o comprime el texto hasta la ilegibilidad. La solución con Tailwind es envolver la tabla en un contenedor con `overflow-x-auto` y `rounded-lg border border-gray-200`, y dar a la tabla un ancho mínimo con `min-w-full` o `min-w-[800px]`. Esto permite hacer scroll horizontal en móvil mientras se mantiene la legibilidad de las celdas. Opcionalmente, se puede implementar una tabla con columnas que se ocultan progresivamente en breakpoints menores usando `hidden md:table-cell` en las celdas de las columnas menos importantes, mostrando solo las columnas esenciales en móvil.

La **tabla con ordenación visual** añade indicadores de dirección de ordenación en las cabeceras. Los `<th>` se convierten en botones con `cursor-pointer select-none` y un icono de flecha que cambia según el estado: sin ordenación muestra una flecha doble en gris claro (`text-gray-300`), ordenado ascendente muestra flecha hacia arriba en color primario (`text-primary-500`), ordenado descendente muestra flecha hacia abajo en color primario. La lógica de ordenación se implementa en el componente Angular con una señal que almacena la columna ordenada y la dirección, y un pipe o método que ordena los datos reactivamente.

La **tabla con selección de filas** añade una columna de checkbox al inicio de cada fila y un checkbox maestro en la cabecera para seleccionar/deseleccionar todas. La fila seleccionada recibe un fondo azul muy claro (`bg-primary-50`). La implementación en Angular utiliza un `Set<number>` o `Set<string>` con los IDs de las filas seleccionadas, actualizado mediante eventos de los checkboxes. Una barra de acciones masivas aparece condicionalmente sobre la tabla cuando hay filas seleccionadas, mostrando el número de elementos seleccionados y las acciones disponibles (eliminar, exportar, cambiar estado).

### Componente 5: Modales

!!! info "Definición"

    El **modal** es un componente que presenta contenido en una capa superpuesta al contenido principal, exigiendo la atención de la persona usuaria para completar una tarea o tomar una decisión antes de continuar. Un modal profesional debe cumplir requisitos de accesibilidad, animación y usabilidad.

El **modal con overlay** se compone de dos capas. La capa de overlay es un `<div>` fijo que cubre toda la ventana (`fixed inset-0 z-50`) con un fondo negro semitransparente (`bg-black/50`) y una transición de opacidad (`transition-opacity duration-300`). Hacer clic en el overlay cierra el modal (comportamiento configurable mediante `@Input closeOnOverlayClick`). La capa de contenido es un `<div>` centrado en la pantalla (`fixed inset-0 z-50 flex items-center justify-center p-4`) que contiene la tarjeta del modal. La tarjeta tiene fondo blanco, bordes redondeados, sombra pronunciada, ancho máximo y padding: `bg-white rounded-2xl shadow-2xl w-full max-w-lg p-6`. Un botón de cierre (X) en la esquina superior derecha permite cerrar explícitamente.

!!! info "Accesibilidad del modal"

    La accesibilidad del modal se implementa con **Angular CDK**. El contenedor del modal recibe `cdkTrapFocus` para capturar el foco del teclado dentro del modal mientras está abierto. El atributo `role="dialog"` identifica el modal para los lectores de pantalla. `aria-modal="true"` indica que es una ventana modal. `aria-labelledby` referencia al título del modal. La tecla Escape cierra el modal mediante un `@HostListener('document:keydown.escape', ['$event'])`. Al cerrarse, el foco retorna al elemento que abrió el modal.

El **modal con animación** añade transiciones de entrada y salida. Angular proporciona el sistema de animaciones (`@angular/animations`) que permite definir transiciones declarativas. La animación típica de un modal es: el overlay aparece con un fade-in de opacidad, y el contenido del modal aparece con una combinación de fade-in y un sutil desplazamiento hacia arriba o escalado. En la entrada, el modal pasa de `opacity: 0; transform: scale(0.95)` a `opacity: 1; transform: scale(1)` en 200ms con una curva de easing. En la salida, la animación inversa dura 150ms.

El **modal de confirmación** es una variante especializada para acciones destructivas. Sustituye el contenido libre por una estructura fija: un icono de advertencia (triángulo con exclamación en naranja o rojo), un título que describe la acción, un texto explicativo de las consecuencias, y dos botones: "Cancelar" (secundario) y "Confirmar" (danger). Esta estructura consistente evita que cada desarrollador implemente la confirmación de forma diferente.

### Componente 6: Barras de Navegación

La **navegación** es la columna vertebral de la experiencia de usuario en cualquier aplicación. Un **sistema de navegación** bien diseñado permite a la persona usuaria orientarse, desplazarse y encontrar lo que busca sin esfuerzo.

El **navbar horizontal responsive** es una barra superior fija (`fixed top-0 inset-x-0 z-40`) con altura definida (`h-16`), fondo blanco y borde inferior sutil (`bg-white border-b border-gray-200`). En su interior, un contenedor `flex items-center justify-between` distribuye los tres bloques típicos: logo/nombre de la app a la izquierda, navegación principal en el centro (visible solo en desktop: `hidden md:flex items-center gap-1`), y acciones de usuario a la derecha (notificaciones, avatar, menú desplegable). El espaciado horizontal se gestiona con `px-4` o `px-6`. Cada item del menú es un enlace o botón con `px-3 py-2 rounded-lg text-sm font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-colors`. El item activo se destaca con `bg-primary-50 text-primary-700`.

En móvil, la navegación principal se oculta y se reemplaza por un **botón de hamburguesa** (tres líneas horizontales) que abre un menú desplegable o un drawer lateral con overlay. El botón hamburguesa se oculta en desktop (`md:hidden`). El menú móvil usa `absolute top-full left-0 right-0 bg-white border-b border-gray-200 shadow-lg` y muestra los items en columna (`flex flex-col p-4 gap-1`). Una transición de altura (`transition-all duration-300`) anima la apertura y cierre del menú.

La **sidebar colapsable** es el patrón de navegación más común en aplicaciones de gestión de escritorio. Consiste en un panel lateral fijo a la izquierda (`fixed left-0 top-16 bottom-0`) con dos estados: expandida (ancho de 256px, `w-64`) y colapsada (ancho de 64px, `w-16`). La transición entre estados se anima con `transition-all duration-300`. En estado expandido, cada item muestra icono y texto (`flex items-center gap-3 px-4 py-2`); en estado colapsado, solo muestra el icono centrado (`flex items-center justify-center p-2`), y un tooltip aparece al pasar el cursor para revelar el texto. En móvil, la sidebar se oculta completamente y se convierte en un drawer que se abre con overlay al pulsar el botón hamburguesa.

Las **tabs (pestañas)** permiten alternar entre diferentes vistas o secciones dentro de una misma página. Se implementan como una barra horizontal de botones con borde inferior. El tab activo se indica con el color primario en el texto y un borde inferior de 2px del mismo color: `text-primary-600 border-b-2 border-primary-600`. Los tabs inactivos tienen texto gris sin borde: `text-gray-500 border-b-2 border-transparent hover:text-gray-700 hover:border-gray-300`. El contenido asociado a cada tab se muestra condicionalmente mediante `@if` en Angular, basado en una señal que almacena el índice del tab activo. La navegación entre tabs con teclado (flechas izquierda/derecha) se implementa con `FocusKeyManager` de Angular CDK.

### Componente 7: Dashboard

El **dashboard** es la pantalla principal de muchas aplicaciones de gestión. Agrega información de múltiples fuentes en una vista panorámica que permite a la persona usuaria evaluar el estado general del sistema de un vistazo. Construir un layout de dashboard con Tailwind demuestra la potencia de las clases de grid responsive.

El layout completo de dashboard consta de **cuatro zonas**. El navbar superior (ya visto en el componente 6), fijo, ocupa todo el ancho y tiene altura `h-16`. La sidebar (componente 6), fija a la izquierda, ocupa el alto restante (`top-16 bottom-0`). El contenido principal (`<main>`) se desplaza para dejar espacio a la sidebar: `ml-64` cuando la sidebar está expandida, `ml-16` cuando está colapsada. El padding del contenido principal es generoso: `p-6 md:p-8`. En móvil, la sidebar se oculta y el contenido ocupa todo el ancho (`ml-0`).

Dentro del contenido principal, los **widgets de estadísticas** se organizan en una cuadrícula responsive: `grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6`. Cada widget es una instancia del componente Card de Estadística (componente 2), mostrando un valor, un título y una tendencia.

El **gráfico placeholder** demuestra cómo incluso elementos visualmente complejos pueden construirse con Tailwind sin CSS personalizado. Un gráfico de barras se construye con un contenedor `flex items-end gap-2 h-48` que contiene múltiples barras (divs con altura variable mediante clases como `h-[60%]`, `h-[85%]`). Las barras tienen `w-8 bg-primary-200 rounded-t hover:bg-primary-500 transition-colors cursor-pointer`. Los ejes se simulan con líneas horizontales (`border-t border-gray-200 absolute inset-x-0` en posiciones absolutas). Un gráfico de líneas se construye con SVG inline, utilizando `stroke="currentColor"` para heredar el color de Tailwind. Esto evita cargar librerías de gráficos completas cuando el dashboard solo necesita gráficos estáticos o placeholder.

La **lista de actividad reciente**, otro componente típico de dashboard, muestra eventos en orden cronológico inverso con una línea de tiempo visual. Cada item es una fila con un punto (círculo de 8px con `w-2 h-2 rounded-full`) conectado a los demás por una línea vertical (`border-l-2 border-gray-200`), la hora del evento (`text-xs text-gray-400`), y la descripción (`text-sm text-gray-700`). Los items se estilizan con `relative pl-6 pb-4 last:pb-0`. El punto se posiciona absolutamente a la izquierda: `absolute left-[-5px] top-1.5`. Esta línea de tiempo, implementada enteramente con Tailwind, crea una visualización clara y profesional.

### Sección Final: Comparativa Sistemática CSS Tradicional vs. Tailwind

Esta sección constituye la reflexión culminante de la unidad. Para cada uno de los siete tipos de componentes implementados, se compara el enfoque de **CSS tradicional** con el enfoque de **Tailwind** en múltiples dimensiones, extrayendo conclusiones basadas en evidencia, no en preferencias personales.

La comparativa se estructura en una tabla para cada componente, con las siguientes dimensiones:

**Código CSS.** Para el botón primario, el CSS tradicional requiere aproximadamente 20 líneas de CSS en un archivo separado: definir la clase `.btn-primary`, sus estados `:hover`, `:active`, `:focus-visible`, `:disabled`, más las variantes de tamaño y las combinaciones con iconos. Con Tailwind, el CSS generado es cero líneas en archivos de estilo; las clases se aplican directamente en el HTML (aproximadamente 12 clases por botón). La ventaja de Tailwind es la eliminación del CSS no utilizado: en un proyecto grande con centenares de botones pero solo unas pocas variantes, el CSS tradicional mantiene todas las reglas incluso para variantes no usadas, mientras que Tailwind genera solo las clases realmente utilizadas.

**Número de líneas de CSS.** En una aplicación con 7 variantes de botón, 3 tamaños, y estados para cada combinación, el CSS tradicional puede sumar 200 líneas. Tailwind: 0 líneas en archivos CSS. Este diferencial es engañoso, sin embargo: las líneas no desaparecen, se trasladan al HTML, donde cada botón suma entre 8 y 15 clases. La diferencia real es de ubicación, no de cantidad.

**Legibilidad del HTML.** Esta es la crítica más común a Tailwind: un botón con `class="inline-flex items-center justify-center px-4 py-2 bg-primary-500 text-white text-sm font-medium rounded-lg hover:bg-primary-600 active:bg-primary-700 focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:ring-offset-2 focus-visible:outline-none disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200"` es verbalmente ruidoso comparado con `class="btn btn-primary"`. Sin embargo, esta crítica presupone que la alternativa es que el HTML ya es limpio en CSS tradicional. La realidad en proyectos CSS es que el HTML contiene igualmente clases (a menudo múltiples) y el desarrollador debe alternar entre HTML y CSS para entender qué aspecto tiene un elemento. La diferencia no es entre "limpio y ruidoso", sino entre "una clase semántica que oculta información" y "clases explícitas que revelan información". Para equipos que dominan Tailwind, la legibilidad explícita supera a la opacidad semántica.

!!! warning "Debilidad de Tailwind puro"

    **Mantenibilidad.** Con CSS tradicional, los cambios de diseño se realizan editando el archivo CSS centralizado. Un cambio en el color primario se propaga a todos los botones automáticamente. Con Tailwind puro (sin `@apply`), el mismo cambio requeriría buscar y reemplazar `bg-blue-500` por `bg-primary-500` en toda la aplicación. Esta es una debilidad real de Tailwind puro que se mitiga mediante dos estrategias: usar los tokens de `@theme` (cambiando `--color-primary-500` en un solo lugar se actualizan todas las clases `bg-primary-500`), y usar componentes Angular (el botón está encapsulado en un componente; cambiar sus clases en la plantilla del componente actualiza todos los botones de la aplicación). Con estas dos estrategias, Tailwind alcanza una mantenibilidad comparable o superior al CSS tradicional.

**Curva de aprendizaje.** CSS tradicional tiene una curva de aprendizaje menor para quien ya conoce CSS: escribir `.btn { ... }` en un archivo `.css` es inmediato. Tailwind requiere memorizar decenas de nombres de clases y su correspondencia con propiedades CSS. Esta curva, sin embargo, se aplana en pocas semanas de uso intensivo ayudado por IntelliSense. A largo plazo, los desarrolladores que dominan Tailwind reportan mayor velocidad de desarrollo que con CSS tradicional.

**Consistencia del diseño.** Aquí Tailwind tiene una ventaja estructural. En CSS tradicional, la consistencia depende de la disciplina del equipo: nadie impide que una persona use `padding: 15px` y otra `padding: 16px`. Tailwind fuerza la consistencia limitando las opciones a su escala predefinida. Un equipo con Tailwind no discute sobre espaciados porque todos usan `p-4` (16px) o `p-5` (20px). Esta consistencia forzada es una ventaja objetiva para proyectos con múltiples desarrolladores.

La conclusión razonada de esta comparativa es que ==no hay un ganador absoluto==. Para aplicaciones empresariales con un **Design System** definido y un equipo de al menos dos desarrolladores, Tailwind acelera el desarrollo, fuerza la consistencia y elimina categorías enteras de problemas (CSS muerto, guerras de naming, especificidad descontrolada). Para proyectos pequeños con CSS altamente personalizado (animaciones complejas, layouts artísticos, microinteracciones muy específicas), CSS puro puede ser más directo. Para el perfil profesional del alumnado de DAM, que previsiblemente trabajará en equipos desarrollando aplicaciones de gestión empresarial, Tailwind es la herramienta más alineada con el mercado laboral actual.

## Actividades guiadas

### Actividad Guiada 1: Sistema Completo de Botones como Componente Angular

El alumnado implementará el **componente Button** descrito en el desarrollo teórico como un componente Angular standalone con todas las variantes, tamaños y estados. El componente debe aceptar `@Input` para variant (primary, secondary, outline, ghost, danger), size (sm, md, lg), disabled, loading, icon (opcional, string con el nombre del icono), iconPosition (left, right), y type (button, submit, reset). El componente debe renderizar un `<button>` nativo y aplicar las clases de Tailwind condicionalmente mediante una señal computada. El alumnado escribirá tests unitarios que verifiquen: que el botón renderiza con las clases correctas para cada variante, que se deshabilita correctamente, que muestra el spinner en estado loading, y que los eventos click se emiten correctamente. El componente se integrará en una página de demostración que muestre una matriz con todas las combinaciones de variantes, tamaños y estados.

### Actividad Guiada 2: Formulario de Registro Completo

El alumnado construirá un formulario de registro de persona usuaria completo con **validación reactiva** en Angular y estilado con Tailwind. El formulario incluirá campos para: nombre de usuario, email, contraseña (con requisitos de complejidad: mínimo 8 caracteres, una mayúscula, un número, un carácter especial), confirmación de contraseña, y checkbox de aceptación de términos. Cada campo se implementará como un componente de formulario reutilizable (InputField) que recibe el `FormControl`, la etiqueta, el tipo, y los mensajes de error personalizados. Los mensajes de error se mostrarán junto al campo en tiempo real al perder el foco o al intentar enviar. Una barra de progreso indicará la fortaleza de la contraseña. El botón de envío mostrará estado loading durante 2 segundos simulados. Tras el envío exitoso, se mostrará un toast de confirmación.

### Actividad Guiada 3: Dashboard con Widgets y Gráficos Placeholder

El alumnado construirá un dashboard completo con layout de sidebar + contenido principal, cuatro **widgets de estadísticas** en grid responsive, una tabla de últimos registros, y dos gráficos placeholder. El dashboard debe ser responsive (1 columna en móvil, 2 en tablet, 4 en desktop) y utilizar los componentes de card y tabla implementados previamente. Los gráficos placeholder (barras y líneas) se construirán con divs y SVG estilados con Tailwind. La actividad incluirá la implementación de la sidebar colapsable con animación de transición y la barra de navegación superior fija.

## Actividades propuestas

### Actividad Propuesta 1: Sistema de Tabla de Datos Avanzada

Implementa un componente de **tabla de datos** como componente Angular standalone con las siguientes características: columnas configurables mediante `@Input`, filas alternas (zebra con `even:bg-gray-50`), ordenación por columna con indicadores visuales, filtrado por texto con debounce de 300ms, paginación con controles de página anterior/siguiente, selección de filas con checkbox maestro, altura máxima con scroll vertical interno (`max-h-96 overflow-y-auto`), cabeceras sticky que no se desplacen al hacer scroll (`sticky top-0 z-10`), y columnas responsive que se ocultan en pantallas pequeñas. La tabla debe procesar un array genérico de datos (`T[]`) y una definición de columnas. Todos los estilos deben ser clases de Tailwind. Escribe tests unitarios para la ordenación, filtrado y selección.

### Actividad Propuesta 2: Modal Genérico Reutilizable

Implementa un componente **Modal genérico** como componente Angular standalone que acepte: título, contenido (proyectado con ng-content), botones de acción configurables mediante `@Input`, tamaño (sm, md, lg, xl, fullscreen), y opciones de comportamiento (closeOnOverlayClick, closeOnEscape, showCloseButton). El modal debe implementar accesibilidad completa con Angular CDK (cdkTrapFocus, LiveAnnouncer), animaciones de entrada/salida con `@angular/animations`, y gestión del foco (retorno al elemento que abrió el modal al cerrar). Escribe tests de accesibilidad con axe-core que verifiquen el modal. Crea tres variantes de uso: modal de confirmación, modal de formulario, y modal de información con video.

### Actividad Propuesta 3: Componentes de Formulario con Tailwind

Crea una librería de **8 componentes de formulario** reutilizables: InputText, InputNumber, InputEmail, InputPassword (con toggle de visibilidad), TextArea (con contador de caracteres), Select (con búsqueda integrada), DatePicker (input de fecha con calendario), y FileUpload (con zona de arrastre y vista previa de imagen). Cada componente debe implementar: integración con Angular Reactive Forms (aceptando FormControl), todos los estados visuales (normal, hover, focus, filled, error, disabled), mensajes de error posicionados bajo el campo con animación de entrada, y tests unitarios. Todos los estilos con Tailwind. Publica la librería en un repositorio con documentación Storybook.

### Actividad Propuesta 4: Comparativa Práctica CSS vs Tailwind

Selecciona tres de los componentes implementados en esta unidad y desarrolla cada uno en dos versiones: una completamente con **CSS tradicional** en archivos `.css` separados (usando **metodología BEM** para los nombres de clases), y otra completamente con Tailwind en la plantilla HTML (sin `@apply`, sin archivos CSS adicionales). Para cada componente y cada versión, mide: líneas totales de código, tiempo de implementación, tamaño del CSS generado, curva de aprendizaje (documenta tus dificultades), y mantenibilidad simulada (cambia el color primario y mide el esfuerzo). Presenta los resultados en un informe comparativo con tablas, gráficos y conclusiones argumentadas sobre cuándo recomendarías cada enfoque.

### Actividad Propuesta 5: Sidebar con Navegación Jerárquica

Implementa una **sidebar de navegación jerárquica** con múltiples niveles de profundidad. El primer nivel muestra secciones principales (Dashboard, Usuarios, Productos, Pedidos, Configuración) con iconos y texto. Algunas secciones tienen subsecciones (Productos > Categorías, Inventario, Precios) que se despliegan con una animación de altura al hacer clic. La sidebar debe ser colapsable a iconos, mostrar indicador de sección activa con un punto o barra lateral coloreada, y ser completamente navegable por teclado (flechas para expandir/colapsar, Enter para navegar, Tab para moverse entre items). En móvil, debe convertirse en un drawer con overlay. Implementa con Tailwind y Angular CDK.

??? "Actividades de ampliación"

    ### Actividad de Ampliación 1: Editor Visual de Componentes con Tailwind

    Desarrolla una pequeña aplicación Angular que funcione como "playground" o **editor visual de componentes** Tailwind. La aplicación debe permitir seleccionar un tipo de componente (botón, card, input) y modificar sus propiedades (variante, tamaño, color, texto) mediante controles de formulario, viendo el resultado en tiempo real junto con el código HTML+Tailwind que lo genera, listo para copiar y pegar. La aplicación debe tener una interfaz dividida (panel de controles a la izquierda, previsualización a la derecha, código generado abajo) y ser responsive. Implementa al menos 5 tipos de componentes editables.

    ### Actividad de Ampliación 2: Sistema de Notificaciones Toast

    Implementa un sistema completo de **notificaciones toast** para Angular con Tailwind. El sistema debe incluir: un servicio ToastService inyectable que expone métodos `success()`, `error()`, `warning()` e `info()`, un componente ToastContainer que se renderiza una vez en el layout raíz y muestra los toasts activos, animaciones de entrada (slide desde la derecha) y salida (fade out), auto-dismiss configurable (por defecto 5 segundos, pausa al hacer hover), barra de progreso que indica el tiempo restante, botón de cierre manual, y posiciones configurables (top-right, top-left, bottom-right, bottom-left). Los toasts deben ser accesibles con `aria-live="polite"` y `role="alert"` para variantes de error. Implementa tests unitarios para el servicio y tests de integración para el componente.

    ### Actividad de Ampliación 3: Tema Multi-tenant con Tailwind

    Implementa un sistema de **temas multi-tenant** en Angular con Tailwind, donde diferentes "inquilinos" (empresas clientes de una aplicación SaaS) tienen diferentes esquemas de color. El sistema debe permitir: definir un tema base con variables CSS (colores primario, secundario, éxito, peligro, fuentes, bordes redondeados), cambiar de tema en tiempo de ejecución sin recargar la página, persistir la selección de tema, y aplicar el tema a todos los componentes de la aplicación. Investiga cómo Tailwind 4 con su sistema `@theme` basado en CSS puede adaptarse para soportar múltiples temas mediante custom properties CSS que cambian dinámicamente. Implementa al menos 3 temas demostración (tema corporativo azul, tema verde naturaleza, tema púrpura moderno) y un selector de tema en la interfaz.

!!! tip "Buenas prácticas"

    1. Utiliza siempre **elementos HTML nativos** como base de tus componentes. Un `<button>` nativo estilado con Tailwind es intrínsecamente más accesible, más ligero y más mantenible que un `<div>` con `role="button"` y manejadores de teclado manuales. Tailwind no limita el uso de elementos nativos; al contrario, al eliminar la fricción del estilado, facilita usarlos.

    2. Encapsula las decisiones de diseño en **componentes Angular**, no en clases de `@apply`. Si necesitas que todos los botones de la aplicación se vean igual, crea un componente `<app-button>` y aplica las clases de Tailwind en su plantilla. Si necesitas modificar el aspecto de los botones, cambia las clases en un solo lugar (la plantilla del componente), no en cientos de lugares de la aplicación.

    3. Utiliza **señales computadas** para generar cadenas de clases condicionales. En lugar de concatenar manualmente clases con ternarios en la plantilla (`[class]="variant() === 'primary' ? 'bg-blue-500 text-white' : 'bg-gray-100'"`), define una señal computada que devuelva la cadena completa de clases en función de todas las propiedades. Esto es más legible, más testeable y más eficiente.

    4. Aprovecha las **variantes de estado de Tailwind** en lugar de añadir lógica condicional en TypeScript. Un tooltip que se muestra en hover no necesita un `@HostListener('mouseenter')` que modifique una señal. Usa `group-hover:opacity-100 opacity-0` en el tooltip y `group` en el contenedor padre. Menos lógica en TypeScript significa menos bugs.

    5. Mantén los **componentes pequeños y enfocados**. Un componente de formulario no debería contener también la tabla de resultados y el modal de confirmación. Cada componente debe tener una responsabilidad única y clara, y componerse con otros componentes mediante proyección de contenido o inputs/outputs.

    6. Escribe **tests unitarios** que verifiquen las clases CSS aplicadas. No basta con probar que el componente renderiza; verifica que ante determinadas entradas, se aplican las clases de Tailwind correctas. Por ejemplo, que un botón con `variant="danger"` tiene la clase `bg-red-600` y no `bg-primary-500`.

    7. Documenta las propiedades de entrada de cada componente con **JSDoc** y ejemplos de uso en Storybook. Esto permite a otros desarrolladores del equipo entender cómo usar el componente sin leer su código fuente.

    8. Verifica la **accesibilidad** de cada componente antes de darlo por terminado. Navega por el componente solo con teclado, pásale axe DevTools, comprueba el contraste de colores, y verifica que los atributos ARIA necesarios están presentes.

    9. Diseña los componentes para ser **responsive** desde el primer momento, no como una mejora posterior. Incluye las variantes responsive de Tailwind (`sm:`, `md:`, `lg:`, `xl:`) en las clases del componente desde su primera implementación.

    10. Mantén una **guía de estilo viva** (style guide page) dentro de la aplicación Angular que muestre todos los componentes en todas sus variantes, estados y breakpoints. Actualízala cada vez que se añada una variante nueva. Esta guía sirve como documentación, como herramienta de diseño y como prueba visual de regresión.

!!! warning "Errores frecuentes"

    1. Crear **componentes div con rol** en lugar de usar el elemento HTML nativo correspondiente. Este es el error más común y más dañino. Un `<div role="button" tabindex="0" (click)="..." (keydown.enter)="..." (keydown.space)="...">` requiere 5 líneas para hacer lo que `<button (click)="...">` hace en 1, y de forma más robusta. Tailwind estila elementos nativos sin problemas.

    2. No gestionar el **estado loading** en componentes interactivos. Un botón que no muestra un spinner mientras se procesa lleva a dobles clics y transacciones duplicadas. Un formulario que no se deshabilita durante el envío permite modificaciones durante la operación. Cada componente interactivo debe contemplar explícitamente su estado de carga.

    3. Estilizar el componente para un **solo breakpoint**. Implementar toda la interfaz pensando solo en desktop y luego intentar adaptarla a móvil es mucho más costoso que diseñar mobile-first desde el inicio. Las clases responsive de Tailwind facilitan el diseño mobile-first si se usan correctamente (clases base para móvil, prefijos para breakpoints superiores).

    4. Mezclar **lógica de negocio con lógica de presentación** en el mismo componente. Un componente que obtiene datos de una API, los transforma, gestiona la paginación Y además renderiza la tabla tiene demasiadas responsabilidades. Separa la lógica de presentación (cómo se ve) de la lógica de negocio (qué datos y cómo se obtienen) en componentes distintos o en servicios.

    5. No definir **tipos TypeScript** para las variantes y tamaños. Usar `variant: string` en lugar de `variant: 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger'` impide que el compilador detecte valores inválidos. Define los tipos union adecuados para todas las propiedades del componente.

    6. Ignorar los **estados de error** en los componentes de formulario. Implementar solo el estado normal y el estado foco, y olvidar los estados de error, éxito, disabled y read-only. Cada campo de formulario debe tener estilos definidos para todos sus estados posibles.

    7. **Anidar componentes innecesariamente**. Crear un componente para cada pequeña variación visual cuando una propiedad de entrada bastaría. Un componente `ButtonPrimary` y un `ButtonSecondary` son peores que un componente `Button` con `variant="primary"` y `variant="secondary"`.

    8. No gestionar la **destrucción de suscripciones y listeners**. Los `@HostListener` y las suscripciones a servicios deben limpiarse cuando el componente se destruye (`ngOnDestroy` o usando `takeUntilDestroyed` en Angular 16+). Olvidar esto causa memory leaks y comportamientos impredecibles.

    9. Usar **ng-content sin select** cuando el componente espera una estructura específica. Si un componente Modal espera un título, un cuerpo y acciones, define slots nombrados con `<ng-content select="[modal-title]">`, no un único slot genérico que obligue a quien usa el componente a conocer su estructura interna.

    10. No testear la **accesibilidad de los componentes**. Implementar un modal visualmente correcto pero que no atrapa el foco, no se cierra con Escape y no tiene roles ARIA. Cada componente interactivo debe incluir tests de accesibilidad en su suite de pruebas.

!!! abstract "Resumen"

    Esta unidad ha recorrido la implementación práctica de los siete tipos de componentes más comunes en aplicaciones de gestión empresarial utilizando **Angular** como framework de desarrollo y **Tailwind CSS** como sistema de estilado. Se ha demostrado que componentes de apariencia profesional y comportamiento complejo pueden implementarse íntegramente con clases utility de Tailwind, sin escribir una sola línea de CSS personalizado, y que esta aproximación produce código más mantenible, más consistente y más rápido de iterar que el CSS tradicional cuando se combina con buenas prácticas de arquitectura de componentes.

    Los **botones**, como componente interactivo fundamental, han mostrado cómo las **variantes de Tailwind** (`hover:`, `focus:`, `active:`, `disabled:`) mapean directamente los estados de interacción, eliminando la necesidad de definir reglas CSS separadas para cada estado. Las tarjetas han demostrado la flexibilidad de Tailwind para crear contenedores visualmente atractivos con mínimas clases.

    Los **formularios** han sido el componente más complejo, requiriendo la coordinación de múltiples estados visuales con los estados de validación de Angular. Las **tablas de datos** han ilustrado las capacidades responsive de Tailwind y el uso de variantes como `even:bg-gray-50` para mejorar la legibilidad. Los modales han sido el vehículo para integrar Tailwind con Angular CDK en la implementación de accesibilidad. Las barras de navegación han ejercitado los patrones de layout responsive y las transiciones animadas entre estados.

    El **dashboard** ha servido como ejercicio de composición, mostrando cómo los componentes individuales se integran en una interfaz completa y coherente.

    La **sección comparativa final** ha proporcionado una evaluación objetiva de Tailwind frente al CSS tradicional, reconociendo las ventajas e inconvenientes de cada enfoque y capacitando al alumnado para tomar **decisiones informadas** en sus futuros proyectos profesionales, basadas en el contexto del proyecto y no en preferencias subjetivas.

## Recursos complementarios

### Documentación oficial
- Tailwind CSS - Component Examples: https://tailwindcss.com/docs/container
- Tailwind UI (componentes de pago de referencia profesional): https://tailwindui.com
- Angular CDK - Accessibility (a11y): https://material.angular.io/cdk/a11y/overview
- Angular - Template Syntax: https://angular.dev/guide/templates
- Angular - Reactive Forms: https://angular.dev/guide/forms/reactive-forms

### Componentes de referencia open source
- shadcn/ui (componentes Radix + Tailwind, adaptables a Angular): https://ui.shadcn.com
- Preline UI (componentes Tailwind puros): https://preline.co
- Flowbite (biblioteca de componentes con Tailwind): https://flowbite.com
- daisyUI (plugin de componentes para Tailwind): https://daisyui.com

### Tutoriales y ejemplos
- "Building a Design System with Tailwind CSS" (Tailwind Labs en YouTube)
- "Recreating Spotify's UI with Tailwind CSS" (Fireship en YouTube)
- "Angular + Tailwind Dashboard" (tutoriales de codedamn o freeCodeCamp)
- "Build a SaaS Dashboard with Angular and Tailwind" (serie de tutoriales)

### Herramientas
- Headwind: extensión VS Code para ordenar clases de Tailwind
- axe-core: librería de tests automatizados de accesibilidad (npm install -D axe-core)
- jasmine-marbles: testing de observables en Angular con RxJS marbles
- Angular DevTools: extensión de Chrome para depurar componentes Angular, estados y rendimiento
- Storybook: herramienta de documentación y desarrollo de componentes aislados (Unidad 14)
