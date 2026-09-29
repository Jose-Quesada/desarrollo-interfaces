---
icon: lucide/blocks
---

# Componentes Reutilizables

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:
- Diseñar e implementar componentes de interfaz de usuario verdaderamente reutilizables siguiendo principios **SOLID**.
- Construir un catálogo completo de componentes UI con **Angular Standalone**, TypeScript estricto y Tailwind CSS 4.
- Aplicar proyección de contenido con **ng-content** para crear componentes compuestos y flexibles.
- Implementar accesibilidad (**ARIA**, teclado, foco) como parte integral del diseño de cada componente.
- Gestionar estados de interfaz (loading, empty, error, data) de forma consistente en todos los componentes.
- Documentar la API pública de componentes (inputs, outputs, modelos) con tipado completo.
- Evaluar la reutilización de un componente en diferentes contextos y refactorizarlo para aumentar su genericidad.

## Resultado de aprendizaje asociado

Esta unidad contribuye al **RA 3** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 3.** Crea componentes visuales valorando y empleando herramientas específicas.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- **CE a)** Se han identificado las herramientas para diseño y prueba de componentes.
- **CE b)** Se han creado componentes visuales.
- **CE c)** Se han definido sus métodos y propiedades con asignación de valores por defecto.
- **CE d)** Se han determinado los eventos a los que debe responder el componente y se les han asociado las acciones correspondientes.
- **CE e)** Se han realizado pruebas unitarias sobre los componentes desarrollados.
- **CE f)** Se han documentado los componentes creados.
- **CE h)** Se han programado aplicaciones cuyo interfaz gráfico utiliza los componentes creados.

!!! note "Conocimientos previos"

    - **TypeScript avanzado**: interfaces, tipos genéricos, tipos condicionales, utility types.
    - **Angular**: Standalone Components, Signals, inputs/outputs, ciclo de vida.
    - **Tailwind CSS 4**: clases utilitarias, variantes, personalización con @theme.
    - **Accesibilidad web**: roles ARIA, atributos aria-*, navegación por teclado.
    - **Principios SOLID** aplicados al desarrollo de software.

## Contenidos

1. Principios de reutilización en componentes de interfaz
2. Catálogo completo de componentes reutilizables
3. Proyección de contenido con ng-content
4. Estados de interfaz: loading, empty, error, data
5. Accesibilidad en componentes reutilizables

## Desarrollo teórico

### Qué hace que un componente sea reutilizable

!!! info "Definición"

    Un componente de interfaz verdaderamente reutilizable posee cuatro características fundamentales: genericidad, configurabilidad, ausencia de acoplamiento y documentación exhaustiva. Analicemos cada una en profundidad.

La **genericidad** implica que el componente no contiene referencias a conceptos específicos del dominio de la aplicación. Un componente `Button` no debe saber qué significa "guardar cambios" o "eliminar producto"; solo debe saber que es un botón que muestra un texto, un icono opcional y emite un evento al ser pulsado. La separación entre el comportamiento genérico del componente y el significado de negocio es responsabilidad del código que consume el componente.

La **configurabilidad** se logra mediante una API pública rica y bien diseñada de inputs. Un componente reutilizable debe exponer todas las dimensiones de variación que sus consumidores puedan necesitar: variantes visuales (primary, secondary, outline, ghost, danger), tamaños (sm, md, lg), estados (disabled, loading, active), y opciones de comportamiento (closeOnBackdrop para un modal, multiple para un select). Sin embargo, la configurabilidad debe equilibrarse con la simplicidad: demasiados inputs pueden hacer que el componente sea difícil de entender y mantener. La regla práctica es exponer inputs para las variaciones que realmente se utilizan en el diseño y añadir nuevas opciones según surjan necesidades reales, no anticipadas.

La **ausencia de acoplamiento** significa que el componente no depende de servicios globales (excepto aquellos estrictamente necesarios para su funcionamiento interno), no conoce las rutas de la aplicación, no importa modelos de dominio específicos y no asume nada sobre el contexto en el que será utilizado. Un `DataTable` debe funcionar igual en la página de productos, en la de usuarios y en la de pedidos, porque opera sobre datos genéricos tipados con `<T>`.

La **documentación exhaustiva** es el cuarto pilar de la reutilización. Sin documentación, un componente por muy bien diseñado que esté no será utilizado correctamente. La documentación debe incluir: la lista de inputs con sus tipos y valores por defecto, la lista de outputs con los tipos de datos emitidos, ejemplos de uso para cada variante, consideraciones de accesibilidad y notas sobre comportamientos especiales. En un entorno profesional, esta documentación se materializa en Storybook, que trataremos en profundidad en la Unidad 14.

### Principios SOLID aplicados a componentes UI

Los principios **SOLID**, formulados por Robert C. Martin, se aplican de manera natural al diseño de componentes de interfaz de usuario:

**Single Responsibility Principle (SRP):** ==Un componente debe tener una única razón para cambiar.== En el contexto de componentes UI, esto significa que un componente debe hacer una sola cosa: mostrar un botón, renderizar una tabla, presentar un modal. Si un componente `DataTable` además gestiona la obtención de datos desde una API, está violando SRP. La solución es separar: un **Smart Component** (`ProductListPage`) obtiene los datos, y un **Presentational Component** (`DataTable`) los muestra.

**Open/Closed Principle (OCP):** Un componente debe estar abierto a la extensión pero cerrado a la modificación. En la práctica, esto significa que añadir una nueva variante de botón (por ejemplo, "ghost") no debería requerir modificar la lógica interna del componente `Button`, sino simplemente añadir una nueva opción al input `variant` y las clases de Tailwind correspondientes. Las proyecciones de contenido (`<ng-content>`) son el mecanismo principal para cumplir OCP: un `Card` puede aceptar cualquier contenido en su header, body y footer sin necesidad de modificar su implementación.

**Liskov Substitution Principle (LSP):** Los componentes que implementan una misma interfaz deben ser intercambiables sin alterar el comportamiento esperado. Si definimos una interfaz `SelectControl<T>`, cualquier componente que la implemente (`Dropdown`, `RadioGroup`, `Autocomplete`) debe comportarse de manera coherente. En Angular, esto se puede lograr mediante directivas o tokens de inyección.

**Interface Segregation Principle (ISP):** Los consumidores de un componente no deberían depender de inputs que no utilizan. Un componente `Modal` no debería tener inputs relacionados con tablas solo porque a veces se muestra una tabla dentro de un modal. En su lugar, el contenido de la tabla se pasa por proyección de contenido, manteniendo la interfaz del Modal limpia y enfocada.

**Dependency Inversion Principle (DIP):** Los componentes de alto nivel no deberían depender de los de bajo nivel; ambos deberían depender de abstracciones. En Angular, esto se traduce en que un Smart Component no debería acoplarse a implementaciones concretas de servicios, sino a interfaces o tokens de inyección. En componentes presentacionales, la dependencia se invierte mediante inputs: el componente no busca los datos, se los proporcionan.

### CATÁLOGO DE COMPONENTES

A continuación se presenta un catálogo exhaustivo de componentes de interfaz de usuario reutilizables. Para cada componente se especifica su interfaz TypeScript completa, su implementación con Angular y Tailwind, sus variantes y consideraciones de accesibilidad.

---

### 1. BUTTON

El componente **Button** es el más fundamental de cualquier sistema de diseño. A pesar de su aparente simplicidad, un botón profesional debe manejar múltiples variantes visuales, tamaños, estados (incluyendo loading y disabled), iconos en diferentes posiciones y cumplir con requisitos estrictos de accesibilidad.

**Interfaz TypeScript:**

```
export type ButtonVariant = 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
export type ButtonSize = 'sm' | 'md' | 'lg';
export type IconPosition = 'left' | 'right';

export const BUTTON_VARIANTS: ButtonVariant[] = ['primary', 'secondary', 'outline', 'ghost', 'danger'];
export const BUTTON_SIZES: ButtonSize[] = ['sm', 'md', 'lg'];
```

**Implementación del componente:**

```
@Component({
  selector: 'ui-button',
  standalone: true,
  imports: [NgClass],
  template: `
    <button
      [type]="type()"
      [disabled]="isDisabled()"
      [attr.aria-disabled]="isDisabled()"
      [attr.aria-busy]="loading()"
      [ngClass]="buttonClasses()"
      (click)="handleClick($event)">
      @if (loading() && iconPosition() === 'left') {
        <span class="animate-spin" aria-hidden="true">
          <svg class="h-4 w-4" ...><!-- spinner SVG --></svg>
        </span>
      }
      @if (icon() && !loading() && iconPosition() === 'left') {
        <span class="shrink-0" [innerHTML]="icon()" aria-hidden="true"></span>
      }
      @if (label()) {
        <span [class.sr-only]="loading()">{{ label() }}</span>
      }
      @if (loading()) {
        <span class="sr-only">Cargando...</span>
      }
      @if (icon() && !loading() && iconPosition() === 'right') {
        <span class="shrink-0" [innerHTML]="icon()" aria-hidden="true"></span>
      }
      @if (loading() && iconPosition() === 'right') {
        <span class="animate-spin" aria-hidden="true">
          <svg class="h-4 w-4" ...><!-- spinner SVG --></svg>
        </span>
      }
    </button>
  `,
  styles: [`
    :host { display: inline-flex; }
  `],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ButtonComponent {
  // Inputs como signals para máxima reactividad
  variant = input<ButtonVariant>('primary');
  size = input<ButtonSize>('md');
  disabled = input(false);
  loading = input(false);
  icon = input<string | null>(null);
  iconPosition = input<IconPosition>('left');
  label = input<string | null>(null);
  type = input<'button' | 'submit' | 'reset'>('button');

  // Output
  clicked = output<void>();

  // Computed signals para clases dinámicas
  isDisabled = computed(() => this.disabled() || this.loading());

  buttonClasses = computed(() => {
    const base = 'inline-flex items-center justify-center gap-2 rounded-lg font-medium transition-all duration-150 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:cursor-not-allowed';

    const sizes: Record<ButtonSize, string> = {
      sm: 'px-3 py-1.5 text-sm',
      md: 'px-4 py-2 text-sm',
      lg: 'px-6 py-3 text-base',
    };

    const variants: Record<ButtonVariant, string> = {
      primary: 'bg-blue-600 text-white hover:bg-blue-700 focus-visible:ring-blue-500 disabled:bg-blue-300 shadow-sm',
      secondary: 'bg-gray-100 text-gray-700 hover:bg-gray-200 focus-visible:ring-gray-400 disabled:bg-gray-50 disabled:text-gray-400 border border-gray-200',
      outline: 'bg-transparent text-blue-600 hover:bg-blue-50 focus-visible:ring-blue-500 disabled:text-blue-300 border border-blue-300 disabled:border-blue-200',
      ghost: 'bg-transparent text-gray-600 hover:bg-gray-100 hover:text-gray-900 focus-visible:ring-gray-400 disabled:text-gray-300',
      danger: 'bg-red-600 text-white hover:bg-red-700 focus-visible:ring-red-500 disabled:bg-red-300 shadow-sm',
    };

    return `${base} ${sizes[this.size()]} ${variants[this.variant()]}`;
  });

  handleClick(event: MouseEvent): void {
    if (!this.isDisabled()) {
      this.clicked.emit();
    }
  }
}
```

**Variantes y cuándo usar cada una:**
- **Primary:** La acción principal de la página o sección. Solo debe haber un primary button por contexto visual.
- **Secondary:** Acciones secundarias o alternativas. Se usa junto a un primary button, ofreciendo una opción menos prominente.
- **Outline:** Acciones de importancia media, a menudo en tarjetas o junto a contenido. Útil cuando un primary button sería demasiado dominante.
- **Ghost:** Acciones de baja importancia, como acciones en filas de tabla, barras de herramientas o cabeceras. Mínimo impacto visual.
- **Danger:** Acciones destructivas como eliminar, cancelar suscripción o resetear datos. El color rojo actúa como señal de advertencia.

**Consideraciones de accesibilidad:**
- El atributo `type` por defecto debe ser `'button'` para evitar envíos accidentales de formulario.
- `aria-disabled` se usa en lugar de `disabled` nativo cuando se necesita mantener el foco en el elemento (útil para tooltips explicativos).
- `aria-busy` se establece a `true` durante el estado de carga, notificando a tecnologías asistivas.
- El texto "Cargando..." es visible solo para lectores de pantalla (`sr-only`).
- `focus-visible` en lugar de `focus` para evitar anillos de foco al hacer click con ratón.
- El contraste de color debe cumplir **WCAG AA** (ratio 4.5:1 para texto normal).

---

### 2. INPUT / FORM FIELD

El componente **Input** o **FormField** es el bloque constructor de todos los formularios. Un buen componente de entrada de datos debe manejar múltiples estados visuales y proporcionar feedback claro al usuario.

**Interfaz TypeScript:**

```
export type InputType = 'text' | 'email' | 'password' | 'number' | 'tel' | 'url' | 'search';
export type InputState = 'default' | 'focus' | 'filled' | 'error' | 'disabled';

export interface FormFieldConfig {
  label: string;
  type?: InputType;
  placeholder?: string;
  hint?: string;
  error?: string;
  icon?: string;
  disabled?: boolean;
  readonly?: boolean;
}
```

**Implementación del componente:**

```
@Component({
  selector: 'ui-form-field',
  standalone: true,
  imports: [ReactiveFormsModule, NgClass],
  template: `
    <div class="space-y-1.5">
      @if (label()) {
        <label
          [for]="fieldId"
          class="block text-sm font-medium"
          [ngClass]="{
            'text-gray-700': !error(),
            'text-red-600': error()
          }">
          {{ label() }}
          @if (required()) {
            <span class="text-red-500 ml-0.5" aria-hidden="true">*</span>
            <span class="sr-only">(obligatorio)</span>
          }
        </label>
      }

      <div class="relative">
        @if (icon()) {
          <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3 text-gray-400"
               aria-hidden="true">
            <svg class="h-5 w-5" [innerHTML]="icon()"></svg>
          </div>
        }

        <input
          #inputElement
          [id]="fieldId"
          [type]="type()"
          [placeholder]="placeholder()"
          [disabled]="disabled()"
          [readonly]="readonly()"
          [value]="value()"
          (input)="onInput($event)"
          (blur)="onBlur()"
          (focus)="onFocus()"
          [attr.aria-invalid]="error() ? true : false"
          [attr.aria-describedby]="describedById"
          class="block w-full rounded-lg border bg-white px-3 py-2 text-sm transition-colors duration-150
                 placeholder:text-gray-400
                 focus:outline-none focus:ring-2 focus:ring-offset-0
                 disabled:cursor-not-allowed disabled:bg-gray-50 disabled:text-gray-500"
          [ngClass]="inputClasses()"
          [class.pl-10]="!!icon()"
        />

        @if (error()) {
          <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3 text-red-500">
            <svg class="h-5 w-5" aria-hidden="true" ...><!-- icono de error --></svg>
          </div>
        }
      </div>

      @if (hint() && !error()) {
        <p [id]="hintId" class="text-xs text-gray-500">{{ hint() }}</p>
      }

      @if (error()) {
        <p [id]="errorId" class="text-xs text-red-600 animate-slideIn" role="alert">
          <span class="font-medium">Error:</span> {{ error() }}
        </p>
      }
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FormFieldComponent {
  // Model input para two-way binding del valor
  value = model<string>('');

  // Inputs de configuración
  label = input<string>('');
  type = input<InputType>('text');
  placeholder = input<string>('');
  hint = input<string>('');
  error = input<string | null>(null);
  icon = input<string | null>(null);
  disabled = input(false);
  readonly = input(false);
  required = input(false);

  // Output de eventos
  valueChange = output<string>();
  blurEvent = output<void>();
  focusEvent = output<void>();

  // Elemento DOM
  private inputElementRef = viewChild<ElementRef<HTMLInputElement>>('inputElement');

  // Estado local
  focused = signal(false);

  // IDs para accesibilidad
  fieldId = 'field-' + Math.random().toString(36).substring(2, 9);
  hintId = `${this.fieldId}-hint`;
  errorId = `${this.fieldId}-error`;

  describedById = computed(() => {
    const ids: string[] = [];
    if (this.hint() && !this.error()) ids.push(this.hintId);
    if (this.error()) ids.push(this.errorId);
    return ids.join(' ') || undefined;
  });

  inputClasses = computed(() => ({
    'border-gray-300 focus:ring-blue-500': !this.focused() && !this.error(),
    'border-blue-500 ring-2 ring-blue-500 ring-offset-0': this.focused() && !this.error(),
    'border-red-400 focus:ring-red-400 text-red-900': !!this.error(),
    'border-gray-300': !this.error() && !this.focused(),
  }));

  onInput(event: Event): void {
    const input = event.target as HTMLInputElement;
    this.value.set(input.value);
    this.valueChange.emit(input.value);
  }

  onBlur(): void {
    this.focused.set(false);
    this.blurEvent.emit();
  }

  onFocus(): void {
    this.focused.set(true);
    this.focusEvent.emit();
  }

  focus(): void {
    this.inputElementRef()?.nativeElement.focus();
  }
}
```

**Estados visuales:**
- **Default:** Borde gris claro, sin interacción aparente.
- **Focus:** Borde azul con anillo de foco del mismo color (ring-2), transición suave.
- **Filled:** Si el campo tiene contenido, se podría añadir un indicador visual (opcional, mediante lógica adicional con Signal).
- **Error:** Borde rojo, icono de error a la derecha, texto de error debajo con animación de entrada, label en rojo.
- **Disabled:** Fondo gris claro, texto atenuado, cursor not-allowed, sin interacción.

**Consideraciones de accesibilidad:**
- La asociación label-input mediante el atributo `for` es obligatoria.
- `aria-invalid` se establece dinámicamente según la presencia de error.
- `aria-describedby` enlaza el input con los elementos de hint y/o error.
- El icono de error tiene `aria-hidden="true"` porque la información ya se transmite mediante `aria-invalid` y el texto de error.
- El mensaje de error usa `role="alert"` para anunciarse automáticamente en lectores de pantalla.

---

### 3. CARD

La tarjeta es un contenedor visual fundamental que agrupa contenido relacionado. Su fortaleza como componente reutilizable reside en la **proyección de contenido** mediante `ng-content`, que permite al consumidor decidir exactamente qué contenido mostrar en cada zona de la tarjeta.

**Implementación del componente:**

```
@Component({
  selector: 'ui-card',
  standalone: true,
  imports: [NgClass],
  template: `
    <div
      [ngClass]="cardClasses()"
      (click)="clickable() && cardClick.emit()"
      [attr.role]="clickable() ? 'button' : null"
      [attr.tabindex]="clickable() ? 0 : null"
      (keydown.enter)="clickable() && cardClick.emit()"
      (keydown.space)="clickable() && cardClick.emit(); $event.preventDefault()">

      @if (hasImage()) {
        <div class="overflow-hidden rounded-t-xl">
          <ng-content select="[card-image]" />
        </div>
      }

      @if (hasHeader()) {
        <div class="border-b border-gray-100 px-6 py-4">
          <ng-content select="[card-header]" />
        </div>
      }

      <div [ngClass]="bodyPadding()">
        <ng-content />
      </div>

      @if (hasFooter()) {
        <div class="border-t border-gray-100 bg-gray-50/50 px-6 py-3">
          <ng-content select="[card-footer]" />
        </div>
      }
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CardComponent {
  padding = input<'none' | 'sm' | 'md' | 'lg'>('md');
  variant = input<'default' | 'bordered' | 'elevated'>('default');
  clickable = input(false);

  cardClick = output<void>();

  // El decorador @ContentChild permite detectar si se ha proyectado contenido
  private headerContent = contentChild('card-header');
  private footerContent = contentChild('card-footer');
  private imageContent = contentChild('card-image');

  hasHeader = computed(() => !!this.headerContent());
  hasFooter = computed(() => !!this.footerContent());
  hasImage = computed(() => !!this.imageContent());

  bodyPadding = computed(() => {
    const paddings: Record<string, string> = {
      none: '',
      sm: 'px-4 py-3',
      md: 'px-6 py-5',
      lg: 'px-8 py-6',
    };
    return paddings[this.padding()];
  });

  cardClasses = computed(() => {
    const base = 'rounded-xl bg-white overflow-hidden transition-all duration-200';
    const variants: Record<string, string> = {
      default: 'shadow-sm border border-gray-200',
      bordered: 'border-2 border-gray-300',
      elevated: 'shadow-lg',
    };
    const hover = this.clickable() ? 'hover:shadow-md hover:-translate-y-0.5 cursor-pointer focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:outline-none' : '';
    return `${base} ${variants[this.variant()]} ${hover}`;
  });
}
```

**Uso con proyección de contenido:**

```
<ui-card variant="elevated" padding="md">
  <div card-image>
    <img src="producto.jpg" alt="Producto" class="h-48 w-full object-cover" />
  </div>
  <div card-header>
    <h3 class="text-lg font-semibold text-gray-900">Título de la tarjeta</h3>
  </div>
  <!-- Contenido por defecto (sin selector) va al body -->
  <p class="text-gray-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
  <div card-footer>
    <div class="flex justify-end gap-2">
      <ui-button variant="ghost" size="sm">Cancelar</ui-button>
      <ui-button variant="primary" size="sm">Aceptar</ui-button>
    </div>
  </div>
</ui-card>
```

---

### 4. MODAL / DIALOG

El componente **Modal** es uno de los más complejos de implementar correctamente debido a sus requisitos de accesibilidad (trampa de foco, tecla Escape, rol dialog), su comportamiento de overlay y sus animaciones de entrada y salida.

**Implementación del componente:**

```
@Component({
  selector: 'ui-modal',
  standalone: true,
  imports: [NgClass],
  template: `
    @if (open()) {
      <div class="fixed inset-0 z-50 overflow-y-auto" role="dialog" aria-modal="true" [attr.aria-labelledby]="titleId">
        <!-- Overlay con animación de fade -->
        <div
          class="fixed inset-0 bg-black/50 backdrop-blur-sm transition-opacity duration-300"
          [class.opacity-0]="!visible()"
          [class.opacity-100]="visible()"
          (click)="closeOnBackdrop() && close()">
        </div>

        <!-- Panel del modal centrado -->
        <div class="flex min-h-full items-center justify-center p-4">
          <div
            [ngClass]="panelClasses()"
            class="transform transition-all duration-300"
            [class.opacity-0 scale-95]="!visible()"
            [class.opacity-100 scale-100]="visible()"
            (click)="$event.stopPropagation()">

            <!-- Cabecera -->
            @if (title()) {
              <div class="flex items-start justify-between border-b border-gray-200 px-6 py-4">
                <h2 [id]="titleId" class="text-lg font-semibold text-gray-900">{{ title() }}</h2>
                <button
                  type="button"
                  class="rounded-lg p-1 text-gray-400 hover:bg-gray-100 hover:text-gray-600"
                  (click)="close()"
                  aria-label="Cerrar diálogo">
                  <svg class="h-5 w-5" ...><!-- icono X --></svg>
                </button>
              </div>
            }

            <!-- Cuerpo -->
            <div class="px-6 py-4">
              <ng-content />
            </div>

            <!-- Footer con acciones -->
            @if (hasFooter()) {
              <div class="flex justify-end gap-3 border-t border-gray-200 px-6 py-4">
                <ng-content select="[modal-footer]" />
              </div>
            }
          </div>
        </div>
      </div>
    }
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ModalComponent implements OnInit, OnDestroy {
  open = input(false);
  title = input<string>('');
  size = input<'sm' | 'md' | 'lg' | 'xl'>('md');
  closeOnBackdrop = input(true);

  closed = output<void>();

  visible = signal(false);
  titleId = 'modal-title-' + Math.random().toString(36).substring(2, 9);

  private footerContent = contentChild('modal-footer');
  hasFooter = computed(() => !!this.footerContent());

  private previousActiveElement: HTMLElement | null = null;

  ngOnInit(): void {
    if (this.open()) {
      this.show();
    }
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['open']) {
      if (this.open()) {
        this.show();
      } else {
        this.hide();
      }
    }
  }

  private show(): void {
    this.previousActiveElement = document.activeElement as HTMLElement;
    document.body.style.overflow = 'hidden';
    requestAnimationFrame(() => {
      this.visible.set(true);
      this.trapFocus();
    });
    document.addEventListener('keydown', this.handleKeydown);
  }

  private hide(): void {
    this.visible.set(false);
    document.body.style.overflow = '';
    document.removeEventListener('keydown', this.handleKeydown);
    setTimeout(() => {
      this.closed.emit();
      this.previousActiveElement?.focus();
    }, 300);
  }

  close(): void {
    this.hide();
  }

  private handleKeydown = (event: KeyboardEvent): void => {
    if (event.key === 'Escape') {
      this.close();
    }
    if (event.key === 'Tab') {
      // Implementación de trampa de foco
      // ... (código para mantener el foco dentro del modal)
    }
  };

  panelClasses = computed(() => ({
    'bg-white rounded-xl shadow-2xl w-full': true,
    'max-w-sm': this.size() === 'sm',
    'max-w-lg': this.size() === 'md',
    'max-w-2xl': this.size() === 'lg',
    'max-w-4xl': this.size() === 'xl',
  }));

  ngOnDestroy(): void {
    document.body.style.overflow = '';
    document.removeEventListener('keydown', this.handleKeydown);
  }
}
```

**Consideraciones de accesibilidad imprescindibles:**
- `role="dialog"` y `aria-modal="true"` identifican el elemento como un diálogo modal.
- La trampa de foco mantiene la navegación por teclado dentro del modal.
- Escape cierra el modal.
- Al cerrar el modal, el foco retorna al elemento que lo abrió.
- El scroll del body se bloquea mientras el modal está abierto.
- El overlay intercepta clicks fuera del panel.

---

### 5. DROPDOWN / MENU

**Interfaz TypeScript:**

```
export interface MenuItem {
  id: string;
  label: string;
  icon?: string;
  shortcut?: string;
  disabled?: boolean;
  danger?: boolean;
  children?: MenuItem[]; // submenú
  action?: () => void;
}

export type DropdownPlacement = 'bottom-start' | 'bottom-end' | 'top-start' | 'top-end';
```

**Implementación:**

```
@Component({
  selector: 'ui-dropdown',
  standalone: true,
  imports: [NgClass, CdkMenuModule],
  template: `
    <div class="relative inline-block" cdkOverlayOrigin #trigger="cdkOverlayOrigin">
      <ng-content select="[dropdown-trigger]" />
    </div>

    <ng-template
      cdkConnectedOverlay
      [cdkConnectedOverlayOrigin]="trigger"
      [cdkConnectedOverlayOpen]="isOpen()"
      (overlayOutsideClick)="close()"
      (detach)="close()">
      <div class="z-50 mt-1 min-w-[12rem] rounded-lg border border-gray-200 bg-white py-1 shadow-lg"
           role="menu" [attr.aria-label]="ariaLabel()">
        @for (item of items(); track item.id) {
          @if (item.label === '---') {
            <div class="my-1 border-t border-gray-100"></div>
          } @else {
            <button
              type="button"
              class="flex w-full items-center gap-3 px-3 py-2 text-sm transition-colors"
              [ngClass]="{
                'text-gray-700 hover:bg-gray-50 hover:text-gray-900': !item.danger && !item.disabled,
                'text-red-600 hover:bg-red-50': item.danger && !item.disabled,
                'text-gray-300 cursor-not-allowed': item.disabled
              }"
              [disabled]="item.disabled"
              role="menuitem"
              (click)="selectItem(item)">
              @if (item.icon) {
                <span class="shrink-0" [innerHTML]="item.icon" aria-hidden="true"></span>
              }
              <span class="flex-1 text-left">{{ item.label }}</span>
              @if (item.shortcut) {
                <kbd class="text-xs text-gray-400">{{ item.shortcut }}</kbd>
              }
            </button>
          }
        }
      </div>
    </ng-template>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DropdownComponent {
  items = input<MenuItem[]>([]);
  placement = input<DropdownPlacement>('bottom-start');
  ariaLabel = input('Menú de opciones');

  itemSelected = output<MenuItem>();

  isOpen = signal(false);

  toggle(): void {
    this.isOpen.update(v => !v);
  }

  open(): void {
    this.isOpen.set(true);
  }

  close(): void {
    this.isOpen.set(false);
  }

  selectItem(item: MenuItem): void {
    if (!item.disabled) {
      this.itemSelected.emit(item);
      item.action?.();
      this.close();
    }
  }
}
```

---

### 6. TABLE / DATA TABLE

La **tabla de datos** es uno de los componentes más complejos y solicitados en aplicaciones enterprise. Una implementación profesional debe manejar ordenación, paginación, selección, estados (loading, empty, error) y ser completamente genérica (tipada con `<T>`).

**Interfaz TypeScript:**

```
export interface Column<T = any> {
  key: string;
  label: string;
  sortable?: boolean;
  type?: 'text' | 'number' | 'currency' | 'date' | 'badge' | 'custom';
  width?: string;
  align?: 'left' | 'center' | 'right';
  cellClass?: (row: T) => string;
  cellTemplate?: TemplateRef<any>; // para renderizado personalizado
}

export interface SortEvent {
  column: string;
  direction: 'asc' | 'desc' | '';
}
```

**Implementación:**

```
@Component({
  selector: 'ui-data-table',
  standalone: true,
  imports: [NgClass, NgTemplateOutlet, CurrencyPipe, DatePipe],
  template: `
    <div class="overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm">
      @if (loading()) {
        <div class="p-8">
          <ui-skeleton-table [rows]="5" [columns]="columns().length" />
        </div>
      } @else if (error()) {
        <div class="flex flex-col items-center justify-center p-12 text-center">
          <svg class="h-12 w-12 text-red-400 mb-4" ...><!-- icono error --></svg>
          <h3 class="text-lg font-medium text-gray-900">Error al cargar los datos</h3>
          <p class="mt-1 text-sm text-gray-500">{{ error() }}</p>
          <ui-button variant="outline" size="sm" class="mt-4" (clicked)="retry.emit()">
            Reintentar
          </ui-button>
        </div>
      } @else if (data().length === 0) {
        <div class="flex flex-col items-center justify-center p-12 text-center">
          <svg class="h-12 w-12 text-gray-300 mb-4" ...><!-- icono vacío --></svg>
          <h3 class="text-lg font-medium text-gray-900">{{ emptyMessage() }}</h3>
          <p class="mt-1 text-sm text-gray-500">{{ emptyDescription() }}</p>
        </div>
      } @else {
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200" role="table">
            <thead class="bg-gray-50">
              <tr>
                @if (selectable()) {
                  <th class="w-10 px-4 py-3">
                    <input type="checkbox"
                           [checked]="allSelected()"
                           [indeterminate]="someSelected()"
                           (change)="toggleAll()"
                           class="rounded border-gray-300" />
                  </th>
                }
                @for (col of columns(); track col.key) {
                  <th
                    class="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wider text-gray-500"
                    [ngClass]="{
                      'cursor-pointer select-none hover:text-gray-700': col.sortable,
                      'text-center': col.align === 'center',
                      'text-right': col.align === 'right'
                    }"
                    [style.width]="col.width"
                    (click)="col.sortable && sortColumn(col)">
                    <div class="flex items-center gap-1">
                      {{ col.label }}
                      @if (col.sortable && currentSort()?.column === col.key) {
                        <span class="text-blue-500">
                          {{ currentSort()?.direction === 'asc' ? '↑' : '↓' }}
                        </span>
                      }
                    </div>
                  </th>
                }
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 bg-white">
              @for (row of data(); track row; let i = $index) {
                <tr
                  class="transition-colors hover:bg-gray-50"
                  [class.bg-blue-50]="selectedRows().has(i)"
                  (click)="rowClick.emit(row)">
                  @if (selectable()) {
                    <td class="px-4 py-3">
                      <input type="checkbox"
                             [checked]="selectedRows().has(i)"
                             (change)="toggleRow(i); $event.stopPropagation()"
                             class="rounded border-gray-300" />
                    </td>
                  }
                  @for (col of columns(); track col.key) {
                    <td class="px-4 py-3 text-sm text-gray-700"
                        [ngClass]="{
                          'text-center': col.align === 'center',
                          'text-right': col.align === 'right'
                        }">
                      <ng-container [ngSwitch]="col.type">
                        <span *ngSwitchCase="'currency'">{{ row[col.key] | currency:'EUR' }}</span>
                        <span *ngSwitchCase="'date'">{{ row[col.key] | date:'dd/MM/yyyy' }}</span>
                        <span *ngSwitchCase="'badge'">
                          <span class="rounded-full px-2 py-0.5 text-xs font-medium"
                                [ngClass]="row[col.key + 'Class'] || 'bg-gray-100 text-gray-700'">
                            {{ row[col.key] }}
                          </span>
                        </span>
                        <ng-container *ngSwitchCase="'custom'">
                          <ng-container
                            [ngTemplateOutlet]="col.cellTemplate!"
                            [ngTemplateOutletContext]="{ $implicit: row }">
                          </ng-container>
                        </ng-container>
                        <span *ngSwitchDefault>{{ row[col.key] }}</span>
                      </ng-container>
                    </td>
                  }
                </tr>
              }
            </tbody>
          </table>
        </div>

        <!-- Paginación -->
        @if (pagination()) {
          <div class="flex items-center justify-between border-t border-gray-200 bg-gray-50 px-4 py-3">
            <p class="text-sm text-gray-600">
              Mostrando {{ (currentPage() - 1) * pageSize() + 1 }} a
              {{ min(currentPage() * pageSize(), totalItems()) }} de {{ totalItems() }} resultados
            </p>
            <div class="flex items-center gap-2">
              <ui-button variant="ghost" size="sm"
                         [disabled]="currentPage() === 1"
                         (clicked)="goToPage(currentPage() - 1)">
                Anterior
              </ui-button>
              @for (page of visiblePages(); track page) {
                <button
                  type="button"
                  class="rounded-lg px-3 py-1 text-sm font-medium transition-colors"
                  [ngClass]="currentPage() === page ? 'bg-blue-600 text-white' : 'text-gray-600 hover:bg-gray-200'"
                  (click)="goToPage(page)">
                  {{ page }}
                </button>
              }
              <ui-button variant="ghost" size="sm"
                         [disabled]="currentPage() >= totalPages()"
                         (clicked)="goToPage(currentPage() + 1)">
                Siguiente
              </ui-button>
            </div>
          </div>
        }
      }
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DataTableComponent<T extends Record<string, any>> {
  // Inputs
  columns = input.required<Column<T>[]>();
  data = input<T[]>([]);
  loading = input(false);
  error = input<string | null>(null);
  emptyMessage = input('No se encontraron resultados');
  emptyDescription = input('Prueba a ajustar los filtros de búsqueda');
  selectable = input(false);
  pagination = input(false);
  pageSize = input(10);
  totalItems = input(0);

  // Outputs
  sortChange = output<SortEvent>();
  rowClick = output<T>();
  selectionChange = output<T[]>();
  pageChange = output<number>();
  retry = output<void>();

  // Estado
  currentSort = signal<SortEvent | null>(null);
  currentPage = signal(1);
  selectedRows = signal<Set<number>>(new Set());

  totalPages = computed(() => Math.ceil(this.totalItems() / this.pageSize()));

  visiblePages = computed(() => {
    const total = this.totalPages();
    const current = this.currentPage();
    const maxVisible = 5;
    let start = Math.max(1, current - Math.floor(maxVisible / 2));
    let end = Math.min(total, start + maxVisible - 1);
    if (end - start + 1 < maxVisible) {
      start = Math.max(1, end - maxVisible + 1);
    }
    return Array.from({ length: end - start + 1 }, (_, i) => start + i);
  });

  allSelected = computed(() => {
    const sel = this.selectedRows();
    return sel.size > 0 && sel.size === this.data().length;
  });

  someSelected = computed(() => {
    const sel = this.selectedRows();
    return sel.size > 0 && sel.size < this.data().length;
  });

  sortColumn(column: Column<T>): void {
    const current = this.currentSort();
    let direction: 'asc' | 'desc' | '' = 'asc';
    if (current?.column === column.key) {
      if (current.direction === 'asc') direction = 'desc';
      else if (current.direction === 'desc') direction = '';
    }
    this.currentSort.set(direction ? { column: column.key, direction } : null);
    this.sortChange.emit({ column: column.key, direction });
  }

  toggleAll(): void {
    if (this.allSelected()) {
      this.selectedRows.set(new Set());
    } else {
      this.selectedRows.set(new Set(this.data().map((_, i) => i)));
    }
    this.emitSelection();
  }

  toggleRow(index: number): void {
    const sel = new Set(this.selectedRows());
    if (sel.has(index)) {
      sel.delete(index);
    } else {
      sel.add(index);
    }
    this.selectedRows.set(sel);
    this.emitSelection();
  }

  goToPage(page: number): void {
    this.currentPage.set(page);
    this.pageChange.emit(page);
  }

  private emitSelection(): void {
    const indices = this.selectedRows();
    this.selectionChange.emit(this.data().filter((_, i) => indices.has(i)));
  }
}
```

---

### COMPONENTES ADICIONALES DEL CATÁLOGO

### 7. TABS

**Implementación del componente Tabs:**

```
@Component({
  selector: 'ui-tabs',
  standalone: true,
  template: `
    <div>
      <div class="border-b border-gray-200" role="tablist">
        <div class="flex -mb-px space-x-1">
          @for (tab of tabs(); track tab.id) {
            <button
              type="button"
              role="tab"
              [attr.aria-selected]="activeTab() === tab.id"
              [attr.aria-controls]="'tabpanel-' + tab.id"
              [id]="'tab-' + tab.id"
              class="px-4 py-2.5 text-sm font-medium border-b-2 transition-colors duration-150"
              [ngClass]="activeTab() === tab.id
                ? 'border-blue-500 text-blue-600'
                : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'"
              [disabled]="tab.disabled"
              (click)="selectTab(tab.id)"
              (keydown.arrowLeft)="focusTab('prev')"
              (keydown.arrowRight)="focusTab('next')">
              @if (tab.icon) {
                <span class="mr-2 inline-block" [innerHTML]="tab.icon" aria-hidden="true"></span>
              }
              {{ tab.label }}
              @if (tab.count !== undefined) {
                <span class="ml-2 rounded-full bg-gray-100 px-2 py-0.5 text-xs text-gray-600">
                  {{ tab.count }}
                </span>
              }
            </button>
          }
        </div>
      </div>

      <div class="pt-4">
        <ng-content />
      </div>
    </div>
  `,
})
export class TabsComponent {
  tabs = input.required<Tab[]>();
  activeTab = model<string>('');

  tabChange = output<string>();

  selectTab(tabId: string): void {
    this.activeTab.set(tabId);
    this.tabChange.emit(tabId);
  }

  focusTab(direction: 'prev' | 'next'): void {
    const tabList = this.tabs();
    const currentIdx = tabList.findIndex(t => t.id === this.activeTab());
    const nextIdx = direction === 'next'
      ? (currentIdx + 1) % tabList.length
      : (currentIdx - 1 + tabList.length) % tabList.length;
    const nextTab = tabList[nextIdx];
    if (nextTab && !nextTab.disabled) {
      this.selectTab(nextTab.id);
      document.getElementById('tab-' + nextTab.id)?.focus();
    }
  }
}
```

### 8. TOAST / NOTIFICATION

El sistema de notificaciones se compone de un servicio que gestiona el estado y un componente que renderiza la lista de toasts activos.

**Servicio de notificaciones:**

```
export interface Toast {
  id: string;
  type: 'success' | 'error' | 'warning' | 'info';
  title: string;
  message?: string;
  duration?: number;
  dismissed?: boolean;
}

@Injectable({ providedIn: 'root' })
export class ToastService {
  private toastsSignal = signal<Toast[]>([]);
  toasts = this.toastsSignal.asReadonly();

  private readonly defaultDuration = 5000;

  show(toast: Partial<Toast> & { title: string; type: Toast['type'] }): string {
    const id = toast.id ?? crypto.randomUUID();
    const newToast: Toast = {
      id,
      title: toast.title,
      type: toast.type,
      message: toast.message,
      duration: toast.duration ?? this.defaultDuration,
      dismissed: false,
    };

    this.toastsSignal.update(toasts => [...toasts, newToast]);

    setTimeout(() => this.dismiss(id), newToast.duration);

    return id;
  }

  success(title: string, message?: string): string {
    return this.show({ type: 'success', title, message });
  }

  error(title: string, message?: string): string {
    return this.show({ type: 'error', title, message, duration: 8000 });
  }

  warning(title: string, message?: string): string {
    return this.show({ type: 'warning', title, message });
  }

  info(title: string, message?: string): string {
    return this.show({ type: 'info', title, message });
  }

  dismiss(id: string): void {
    this.toastsSignal.update(toasts =>
      toasts.map(t => t.id === id ? { ...t, dismissed: true } : t)
    );
    setTimeout(() => {
      this.toastsSignal.update(toasts => toasts.filter(t => t.id !== id));
    }, 300);
  }

  clear(): void {
    this.toastsSignal.set([]);
  }
}
```

**Componente de toast individual:**

```
@Component({
  selector: 'ui-toast',
  standalone: true,
  imports: [NgClass],
  template: `
    <div
      class="pointer-events-auto flex items-start gap-3 rounded-lg border p-4 shadow-lg transition-all duration-300"
      [ngClass]="[typeClasses(), dismissed() ? 'opacity-0 translate-x-full' : 'opacity-100 translate-x-0']"
      role="alert">
      <span class="shrink-0" aria-hidden="true">
        @switch (type()) {
          @case ('success') { <svg class="h-5 w-5 text-green-500" ...><!-- check --></svg> }
          @case ('error') { <svg class="h-5 w-5 text-red-500" ...><!-- x --></svg> }
          @case ('warning') { <svg class="h-5 w-5 text-yellow-500" ...><!-- warning --></svg> }
          @case ('info') { <svg class="h-5 w-5 text-blue-500" ...><!-- info --></svg> }
        }
      </span>
      <div class="flex-1 min-w-0">
        <p class="text-sm font-medium text-gray-900">{{ title() }}</p>
        @if (message()) {
          <p class="mt-0.5 text-sm text-gray-500">{{ message() }}</p>
        }
      </div>
      <button
        type="button"
        class="shrink-0 rounded-lg p-1 text-gray-400 hover:bg-gray-100 hover:text-gray-600"
        (click)="dismiss.emit()"
        aria-label="Cerrar notificación">
        <svg class="h-4 w-4" ...><!-- x --></svg>
      </button>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ToastComponent {
  type = input.required<Toast['type']>();
  title = input.required<string>();
  message = input<string>();
  dismissed = input(false);

  dismiss = output<void>();

  typeClasses = computed(() => {
    const classes: Record<string, string> = {
      success: 'border-green-200 bg-green-50',
      error: 'border-red-200 bg-red-50',
      warning: 'border-yellow-200 bg-yellow-50',
      info: 'border-blue-200 bg-blue-50',
    };
    return classes[this.type()] || '';
  });
}
```

---

### 9. COMPONENTES COMPLEMENTARIOS

**BADGE:**

```
@Component({
  selector: 'ui-badge',
  standalone: true,
  template: `
    <span
      class="inline-flex items-center gap-1 rounded-full font-medium"
      [ngClass]="badgeClasses()">
      @if (removable()) {
        <button type="button"
                class="ml-0.5 rounded-full p-0.5 hover:bg-black/10"
                (click)="remove.emit()"
                aria-label="Eliminar {{ label() }}">
          <svg class="h-3 w-3" ...><!-- x --></svg>
        </button>
      }
      {{ label() }}
    </span>
  `,
})
export class BadgeComponent {
  label = input.required<string>();
  variant = input<'default' | 'primary' | 'success' | 'warning' | 'danger'>('default');
  size = input<'sm' | 'md'>('md');
  removable = input(false);
  remove = output<void>();

  badgeClasses = computed(() => {
    const variants = {
      default: 'bg-gray-100 text-gray-700',
      primary: 'bg-blue-100 text-blue-700',
      success: 'bg-green-100 text-green-700',
      warning: 'bg-yellow-100 text-yellow-700',
      danger: 'bg-red-100 text-red-700',
    };
    const sizes = {
      sm: 'px-2 py-0.5 text-xs',
      md: 'px-2.5 py-1 text-sm',
    };
    return `${variants[this.variant()]} ${sizes[this.size()]}`;
  });
}
```

**AVATAR:**

```
@Component({
  selector: 'ui-avatar',
  standalone: true,
  template: `
    @if (src()) {
      <img [src]="src()" [alt]="alt()"
           class="rounded-full object-cover"
           [ngClass]="sizeClasses()" />
    } @else {
      <div class="rounded-full bg-gray-200 flex items-center justify-center font-medium text-gray-600"
           [ngClass]="sizeClasses()">
        {{ initials() }}
      </div>
    }
  `,
})
export class AvatarComponent {
  src = input<string | null>(null);
  alt = input('');
  name = input('');
  size = input<'xs' | 'sm' | 'md' | 'lg' | 'xl'>('md');

  initials = computed(() => {
    const name = this.name();
    if (!name) return '';
    return name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
  });

  sizeClasses = computed(() => ({
    'h-6 w-6 text-xs': this.size() === 'xs',
    'h-8 w-8 text-sm': this.size() === 'sm',
    'h-10 w-10 text-base': this.size() === 'md',
    'h-12 w-12 text-lg': this.size() === 'lg',
    'h-16 w-16 text-xl': this.size() === 'xl',
  }));
}
```

**SKELETON LOADER:**

```
@Component({
  selector: 'ui-skeleton',
  standalone: true,
  template: `
    <div class="animate-pulse">
      @if (variant() === 'text') {
        <div class="h-4 bg-gray-200 rounded" [style.width]="width()"></div>
      } @else if (variant() === 'circle') {
        <div class="rounded-full bg-gray-200" [ngClass]="sizeClasses()"></div>
      } @else if (variant() === 'card') {
        <div class="rounded-xl border border-gray-200 p-4">
          <div class="h-4 bg-gray-200 rounded w-3/4 mb-3"></div>
          <div class="h-3 bg-gray-200 rounded w-full mb-2"></div>
          <div class="h-3 bg-gray-200 rounded w-5/6"></div>
        </div>
      } @else if (variant() === 'table-row') {
        <div class="flex gap-4 py-3">
          @for (col of columnsArray(); track $index) {
            <div class="h-4 bg-gray-200 rounded" [style.width]="col"></div>
          }
        </div>
      }
    </div>
  `,
})
export class SkeletonComponent {
  variant = input<'text' | 'circle' | 'rect' | 'card' | 'table-row'>('text');
  width = input('100%');
  height = input('1rem');
  columns = input(''); // para table-row: "100px 150px 200px 100px"
  size = input<'sm' | 'md' | 'lg'>('md');

  columnsArray = computed(() => this.columns().split(' '));

  sizeClasses = computed(() => ({
    'h-8 w-8': this.size() === 'sm',
    'h-12 w-12': this.size() === 'md',
    'h-16 w-16': this.size() === 'lg',
  }));
}
```

**PROGRESS BAR:**

```
@Component({
  selector: 'ui-progress',
  standalone: true,
  template: `
    <div
      class="w-full overflow-hidden rounded-full bg-gray-200"
      [ngClass]="heightClasses()"
      role="progressbar"
      [attr.aria-valuenow]="value()"
      [attr.aria-valuemin]="0"
      [attr.aria-valuemax]="max()"
      [attr.aria-label]="label()">
      <div
        class="h-full rounded-full transition-all duration-500 ease-in-out"
        [ngClass]="colorClasses()"
        [style.width.%]="percentage()">
      </div>
    </div>
    @if (showLabel()) {
      <p class="mt-1 text-xs text-gray-500">{{ percentage() | number:'1.0-0' }}%</p>
    }
  `,
})
export class ProgressBarComponent {
  value = input(0);
  max = input(100);
  color = input<'blue' | 'green' | 'red' | 'yellow'>('blue');
  size = input<'sm' | 'md' | 'lg'>('md');
  showLabel = input(false);
  label = input('Progreso');

  percentage = computed(() => (this.value() / this.max()) * 100);

  heightClasses = computed(() => ({
    'h-1': this.size() === 'sm',
    'h-2': this.size() === 'md',
    'h-4': this.size() === 'lg',
  }));

  colorClasses = computed(() => ({
    'bg-blue-500': this.color() === 'blue',
    'bg-green-500': this.color() === 'green',
    'bg-red-500': this.color() === 'red',
    'bg-yellow-500': this.color() === 'yellow',
  }));
}
```

**TOOLTIP:**

```
@Component({
  selector: 'ui-tooltip',
  standalone: true,
  template: `
    <div class="relative inline-block"
         (mouseenter)="show()"
         (mouseleave)="hide()"
         (focusin)="show()"
         (focusout)="hide()">
      <ng-content />
      @if (visible()) {
        <div
          class="absolute z-50 rounded-lg bg-gray-900 px-3 py-1.5 text-xs text-white shadow-lg pointer-events-none
                 transition-opacity duration-150"
          [ngClass]="[positionClasses(), visible() ? 'opacity-100' : 'opacity-0']"
          role="tooltip">
          {{ text() }}
          <div class="absolute h-2 w-2 rotate-45 bg-gray-900"
               [ngClass]="arrowClasses()"></div>
        </div>
      }
    </div>
  `,
})
export class TooltipComponent {
  text = input.required<string>();
  position = input<'top' | 'bottom' | 'left' | 'right'>('top');
  delay = input(300);

  visible = signal(false);
  private timeoutId?: ReturnType<typeof setTimeout>;

  positionClasses = computed(() => {
    const positions = {
      top: 'bottom-full left-1/2 -translate-x-1/2 mb-2',
      bottom: 'top-full left-1/2 -translate-x-1/2 mt-2',
      left: 'right-full top-1/2 -translate-y-1/2 mr-2',
      right: 'left-full top-1/2 -translate-y-1/2 ml-2',
    };
    return positions[this.position()];
  });

  arrowClasses = computed(() => {
    const positions = {
      top: 'bottom-0 left-1/2 -translate-x-1/2 translate-y-1/2',
      bottom: 'top-0 left-1/2 -translate-x-1/2 -translate-y-1/2',
      left: 'right-0 top-1/2 translate-x-1/2 -translate-y-1/2',
      right: 'left-0 top-1/2 -translate-x-1/2 -translate-y-1/2',
    };
    return positions[this.position()];
  });

  show(): void {
    this.timeoutId = setTimeout(() => this.visible.set(true), this.delay());
  }

  hide(): void {
    clearTimeout(this.timeoutId);
    this.visible.set(false);
  }
}
```

**EMPTY STATE:**

```
@Component({
  selector: 'ui-empty-state',
  standalone: true,
  template: `
    <div class="flex flex-col items-center justify-center py-16 text-center">
      <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-gray-100">
        <svg class="h-10 w-10 text-gray-400" ...><!-- icono personalizado --></svg>
      </div>
      <h3 class="text-lg font-semibold text-gray-900">{{ title() }}</h3>
      <p class="mt-2 max-w-sm text-sm text-gray-500">{{ description() }}</p>
      @if (actionLabel()) {
        <ui-button [variant]="actionVariant()" size="sm" class="mt-6" (clicked)="action.emit()">
          {{ actionLabel() }}
        </ui-button>
      }
    </div>
  `,
})
export class EmptyStateComponent {
  title = input('Sin elementos');
  description = input('');
  actionLabel = input<string | null>(null);
  actionVariant = input<'primary' | 'secondary'>('primary');
  action = output<void>();
}
```

---

## Ejemplos guiados

### Ejemplo guiado 1: Construir el componente Button desde cero

**Objetivo:** Construir el componente Button completo paso a paso, desde la definición de la interfaz TypeScript hasta la implementación de accesibilidad y tests.

**Paso 1 — Definir la interfaz y tipos:**
```
export type ButtonVariant = 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
export type ButtonSize = 'sm' | 'md' | 'lg';
```

**Paso 2 — Crear el componente con la estructura básica:**

Se crea el archivo `button.component.ts` con el decorador `@Component`, la configuración standalone, y el template inicial con un elemento `<button>` nativo. Se definen los inputs básicos: `variant`, `size`, `disabled`, `label`.

**Paso 3 — Implementar las clases dinámicas de Tailwind:**

Se crea un `computed` signal `buttonClasses` que devuelve las clases CSS basadas en los valores de `variant()` y `size()`. Se definen mapas de clases para cada variante y tamaño, asegurando que todas las combinaciones producen estilos coherentes.

**Paso 4 — Añadir soporte para iconos y estado loading:**

Se añaden los inputs `icon`, `iconPosition` y `loading`. En el template, se utiliza `@if` para renderizar condicionalmente el spinner de carga o el icono según el estado. El spinner es un SVG animado con la clase `animate-spin` de Tailwind. Cuando el botón está en loading, el texto se oculta visualmente pero permanece accesible para lectores de pantalla mediante `sr-only`.

**Paso 5 — Implementar accesibilidad:**

- `type="button"` por defecto para evitar envíos accidentales.
- `aria-disabled` en lugar de `disabled` nativo para mantener el foco.
- `aria-busy` durante la carga.
- `focus-visible` para estilos de foco solo con teclado.
- Texto "Cargando..." en `sr-only`.

**Paso 6 — Escribir tests unitarios:**

Probar cada variante, cada tamaño, el estado disabled, el estado loading, la emisión del evento `clicked`, y que no se emita cuando está disabled o loading.

### Ejemplo guiado 2: Construir Modal accesible

**Objetivo:** Implementar un modal completamente accesible con trampa de foco, tecla Escape, y retorno de foco al elemento que lo abrió.

**Pasos:**

1. Crear el componente con inputs `open`, `title`, `size`, `closeOnBackdrop`.
2. Implementar la animación de entrada/salida usando Signals para controlar la opacidad y escala.
3. Guardar el elemento activo antes de abrir el modal (`document.activeElement`).
4. Implementar la trampa de foco en el handler de `keydown.Tab`.
5. Bloquear el scroll del body (`document.body.style.overflow = 'hidden'`).
6. Cerrar con Escape y restaurar el foco al elemento original.
7. Añadir roles ARIA: `role="dialog"`, `aria-modal="true"`, `aria-labelledby`.
8. Probar con lectores de pantalla (NVDA en Windows, VoiceOver en macOS).

### Ejemplo guiado 3: Construir DataTable con estados loading/empty/error/data

**Objetivo:** Implementar una tabla de datos que maneje correctamente los cuatro estados fundamentales de interfaz.

**Pasos:**

1. Definir la interfaz `Column<T>` genérica.
2. Implementar el estado **loading**: mostrar `ui-skeleton` con el mismo número de columnas y 5 filas fantasma.
3. Implementar el estado **empty**: mostrar `ui-empty-state` con icono, título descriptivo y opcionalmente un botón de acción (ej: "Crear primer elemento").
4. Implementar el estado **error**: mostrar icono de error, mensaje y botón de "Reintentar" que emite el evento `retry`.
5. Implementar el estado **data**: renderizar la tabla con los datos reales, incluyendo ordenación por columna al hacer click en la cabecera.
6. Añadir paginación con navegación entre páginas y resumen de resultados mostrados.
7. Añadir selección de filas con checkboxes y soporte para "seleccionar todas".
8. Verificar la transición suave entre estados.

---

## Actividades guiadas

### Actividad guiada 1: Auditoría de reutilización de componentes existentes

**Duración:** 45 minutos.

**Objetivo:** Evaluar un conjunto de componentes existentes y determinar su grado de reutilización, identificando problemas de acoplamiento y proponiendo mejoras.

**Desarrollo:**
1. El docente proporciona 4 componentes de una aplicación Angular (ej: `ProductCard`, `UserForm`, `OrderTable`, `NotificationBanner`) que tienen problemas de reutilización.
2. El alumnado analiza cada componente respondiendo las siguientes preguntas:
   - ¿Contiene referencias a conceptos de dominio específico?
   - ¿Inyecta servicios que limitan su reutilización?
   - ¿Su API de inputs es suficientemente genérica y configurable?
   - ¿Cumple el principio de responsabilidad única?
3. Para cada componente, el alumnado redacta una propuesta de refactorización que lo convierta en un componente verdaderamente reutilizable (ej: `ProductCard` → `MediaCard` genérico).
4. Se ponen en común las propuestas y se debate cuál es la mejor aproximación.

**Entregable:** Documento de auditoría con el análisis de cada componente y las propuestas de refactorización.

### Actividad guiada 2: Implementar un componente Alert desde cero

**Duración:** 60 minutos.

**Objetivo:** Aplicar el proceso completo de diseño e implementación de un componente reutilizable.

**Desarrollo:**

1. El docente explica la especificación del componente `Alert`:
   - Cuatro variantes: info, success, warning, error.
   - Con o sin título.
   - Con o sin botón de cierre.
   - Con o sin icono.
   - Capacidad de auto-desaparecer tras un tiempo configurable.
2. El alumnado implementa el componente paso a paso siguiendo el método enseñado:
   - Definición de tipos e interfaz.
   - Template con Tailwind (color de fondo y borde según variante, icono correspondiente a cada tipo).
   - Implementación de auto-dismiss con `setTimeout` y limpieza en `ngOnDestroy`.
   - Accesibilidad: `role="alert"` para tipos warning/error, `role="status"` para info/success.
   - Output `dismissed` para notificar al padre.
3. Al finalizar, el alumnado prueba el componente en una página de demostración que muestre los cuatro tipos simultáneamente.

**Entregable:** Componente `AlertComponent` funcional.

### Actividad guiada 3: Construir un componente Dropdown con submenús

**Duración:** 90 minutos.

**Objetivo:** Implementar un componente Dropdown avanzado que soporte submenús anidados, accesos directos de teclado y posicionamiento inteligente.

**Desarrollo:**

1. El alumnado parte del componente Dropdown básico proporcionado y lo extiende con:
   - Soporte para `children` en `MenuItem` (submenús que se abren al hacer hover o click).
   - Navegación completa por teclado: flechas arriba/abajo para moverse entre items, Enter/Space para seleccionar, Escape para cerrar, flecha derecha para abrir submenú.
   - Separadores visuales (items con `label: '---'`).
   - Atajos de teclado mostrados en el lado derecho (ej: `⌘K`, `Ctrl+S`).
   - Items con estado danger (rojo) para acciones destructivas.
2. El alumnado implementa tests unitarios que verifiquen:
   - La navegación por teclado produce el foco correcto.
   - Enter en un item emite el evento `itemSelected`.
   - Escape cierra el dropdown.
   - Los items disabled no emiten eventos y no reciben foco.

**Entregable:** Componente `DropdownComponent` avanzado con tests.

---

## Actividades propuestas

### Actividad propuesta 1: Catálogo de componentes básicos

**Duración:** 180 minutos.

**Descripción:** El alumnado debe implementar desde cero los siguientes 5 componentes del catálogo, siguiendo las especificaciones detalladas en el desarrollo teórico: Button, Input (FormField), Card, Badge y Avatar. Cada componente debe incluir todas las variantes especificadas, manejo de estados, accesibilidad y estilos con Tailwind.

**Requisitos adicionales:**
- Cada componente debe tener al menos 3 variantes visuales documentadas.
- Todos los componentes deben usar `ChangeDetectionStrategy.OnPush`.
- Todos los inputs requeridos deben marcarse con `required: true`.
- Los componentes con interacción deben emitir eventos mediante `output()`.
- La accesibilidad debe verificarse con el panel de Lighthouse o axe DevTools.

**Entregable:** Los 5 componentes en sus respectivas carpetas dentro de `shared/components/`, cada uno con su archivo `.component.ts`.

### Actividad propuesta 2: Implementar un sistema de notificaciones Toast

**Duración:** 120 minutos.

**Descripción:** Implementar el sistema completo de notificaciones Toast basado en el servicio `ToastService` y los componentes `ToastContainer` y `Toast` descritos en el desarrollo teórico.

**Requisitos adicionales:**
- Las notificaciones deben apilarse verticalmente en la esquina superior derecha.
- Debe haber animación de entrada (deslizar desde la derecha + fade) y salida.
- El auto-dismiss debe ser configurable por notificación.
- Al hacer hover sobre una notificación, el temporizador de auto-dismiss debe pausarse.
- Debe existir una notificación de tipo "persistente" que no se auto-elimina (duración 0 o Infinity).
- Máximo 5 notificaciones visibles simultáneamente; las nuevas desplazan a las más antiguas.

**Entregable:** Servicio `ToastService`, componentes `ToastContainerComponent` y `ToastComponent`, y una página de demostración con botones para disparar los 4 tipos de notificación.

### Actividad propuesta 3: Construir un componente Tabs con contenido asociado

**Duración:** 90 minutos.

**Descripción:** Implementar un sistema de pestañas (Tabs) completo que permita definir pestañas programáticamente y proyectar contenido para cada panel.

**Requisitos:**
- Los tabs se definen mediante un array de objetos `Tab` pasado por input.
- El contenido de cada panel se proyecta con `ng-content` o se asocia mediante IDs.
- Navegación completa por teclado: flechas izquierda/derecha entre tabs, Home/End para ir al primer/último tab.
- Soporte para tabs con badge de conteo (ej: "Notificaciones (3)").
- Soporte para tabs deshabilitados.
- Variante de tabs con iconos y tabs "pill" (estilo redondeado).

**Entregable:** Componentes `TabsComponent` y `TabPanelComponent`, con al menos 3 ejemplos de uso diferentes.

### Actividad propuesta 4: Componente de búsqueda con autocompletado

**Duración:** 150 minutos.

**Descripción:** Diseñar e implementar un componente `SearchInput` que incluya un campo de búsqueda con autocompletado, historial de búsquedas recientes y sugerencias.

**Requisitos:**
- Input de búsqueda con icono de lupa y botón de limpiar.
- Debounce de 300ms antes de emitir el término de búsqueda.
- Panel de sugerencias que se muestra al escribir, con resultados categorizados.
- Historial de búsquedas recientes almacenado en `localStorage` y mostrado cuando el campo está vacío y recibe el foco.
- Navegación por teclado en las sugerencias (flechas, Enter, Escape).
- Estado de carga mientras se obtienen sugerencias del servidor.
- Mensaje "Sin resultados" cuando la búsqueda no produce coincidencias.

**Entregable:** Componente `SearchInputComponent` funcional, probado con datos mock.

### Actividad propuesta 5: Componente de carga de archivos con arrastrar y soltar

**Duración:** 150 minutos.

**Descripción:** Implementar un componente `FileUpload` que permita cargar archivos mediante arrastrar y soltar (drag and drop) o mediante el diálogo nativo de selección de archivos.

**Requisitos:**
- Zona de drop con borde punteado que se resalta al arrastrar archivos sobre ella.
- Soporte para múltiples archivos.
- Validación de tipos de archivo (extensiones permitidas).
- Validación de tamaño máximo por archivo.
- Previsualización de imágenes antes de subir.
- Barra de progreso simulada durante la carga.
- Lista de archivos seleccionados con botón para eliminar cada uno.
- Estados: default, drag-over, uploading, success, error.
- Accesibilidad: la zona de drop debe ser operable por teclado.

**Entregable:** Componente `FileUploadComponent` con todos los estados implementados.

---

??? "Actividades de ampliación"

    ### Actividad de ampliación 1: Crear un componente de gráfico (Chart) con entrada de datos genérica

    **Duración:** 180 minutos.

    **Descripción:** Diseñar un componente `ChartWidget` reutilizable que envuelva Chart.js y exponga una API genérica para diferentes tipos de gráficos.

    **Requisitos:**
    - Soportar al menos 4 tipos de gráfico: líneas, barras, circular (doughnut) y radar.
    - Input `series` genérico que acepte datos en un formato común.
    - Inputs para configuración: `title`, `height`, `showLegend`, `showTooltip`, `colors`.
    - Estado loading (skeleton del gráfico), empty (mensaje) y error.
    - Botón de exportación a PNG.
    - Responsive: el gráfico debe redimensionarse con su contenedor.
    - Dos temas de color: claro y oscuro (reaccionar a la clase `dark` en `<html>`).

    **Entregable:** Componente `ChartWidgetComponent` con demostración de los 4 tipos de gráfico.

    ### Actividad de ampliación 2: Implementar virtual scrolling en DataTable

    **Duración:** 150 minutos.

    **Descripción:** Extender el componente `DataTable` desarrollado en el catálogo para que soporte scroll virtual con 10.000+ filas mediante `@angular/cdk/scrolling`.

    **Requisitos:**
    - Utilizar `CdkVirtualScrollViewport` de Angular CDK.
    - Renderizar solo las filas visibles + un buffer configurable.
    - Mantener la funcionalidad de ordenación y selección.
    - Medir y comparar el rendimiento (FPS, tiempo de renderizado, memoria) entre la versión con scroll virtual y sin él para 1.000, 5.000 y 10.000 filas.
    - Presentar resultados en un breve informe.

    **Entregable:** `DataTableComponent` con scroll virtual + informe de rendimiento.

    ### Actividad de ampliación 3: Construir un componente Rich Text Editor reutilizable

    **Duración:** 240 minutos.

    **Descripción:** Integrar una librería de edición de texto enriquecido (Quill, Tiptap o Slate) en un componente Angular reutilizable con todas las funcionalidades esperables de un editor profesional.

    **Requisitos:**
    - Barra de herramientas configurable por input (ej: `['bold', 'italic', 'underline', 'link', 'image', 'list']`).
    - Two-way binding del contenido HTML mediante `model()`.
    - Placeholder personalizable.
    - Límite de caracteres opcional con contador visual.
    - Modo solo lectura.
    - Validación visual (borde rojo si hay error de validación).
    - Accesibilidad: toolbar operable por teclado, anuncio del modo de edición.

    **Entregable:** Componente `RichTextEditorComponent` completamente funcional.

---

!!! tip "Buenas prácticas"

    1. **API de inputs basada en signals.** Utilizar `input()`, `model()` y `output()` en lugar de los decoradores tradicionales `@Input` y `@Output` para aprovechar la reactividad de Signals y la mejor integración con la detección de cambios OnPush.

    2. **Un solo output por evento conceptual.** Evitar outputs genéricos como `action` con un discriminador de tipo. Es preferible tener outputs específicos: `save`, `delete`, `cancel`, cada uno con su tipo de dato correspondiente.

    3. **Proyección de contenido con selectores nombrados.** Utilizar `ng-content` con atributos `select` para zonas específicas (header, body, footer) en lugar de múltiples inputs para contenido, lo que proporciona mayor flexibilidad y mejor experiencia de desarrollo.

    4. **Estados de interfaz explícitos.** ==Todo componente que muestre datos asíncronos debe contemplar los estados loading, empty, error y data.== No hacerlo resulta en interfaces que "parpadean" o muestran información incorrecta durante las transiciones.

    5. **CSS solo con Tailwind.** Evitar mezclar CSS personalizado con Tailwind en componentes reutilizables. Si un estilo no se puede expresar con clases de Tailwind, es un buen momento para reconsiderar el diseño o extender la configuración de Tailwind con valores personalizados.

    6. **Documentar cada input con JSDoc.** Un comentario `/** Descripción del input */` antes de cada `input()` proporciona documentación que aparece en tooltips del editor y puede extraerse con herramientas de generación de documentación.

    7. **No filtrar ni transformar datos en el componente presentacional.** Las transformaciones de datos pertenecen al Smart Component o a un pipe. El componente presentacional debe mostrar exactamente lo que recibe.

    8. **Usar `ChangeDetectionStrategy.OnPush` siempre.** En componentes presentacionales, OnPush combinado con Signals produce una detección de cambios extremadamente eficiente, ya que solo se ejecuta cuando los inputs (signals) cambian.

    9. **Internacionalizar textos de componentes reutilizables.** Los textos mostrados por componentes del catálogo (como "Cargando...", "Sin resultados", "Reintentar") deben ser configurables mediante inputs para permitir internacionalización.

    10. **Testear la accesibilidad desde el principio.** Utilizar `@storybook/addon-a11y` o `axe-core` para verificar automáticamente que cada variante del componente cumple con los estándares de accesibilidad.

    11. **Evitar dependencias circulares.** Los componentes de `shared/` no deben importar nada de `features/`. Si un componente necesita conocer un tipo de dominio, ese tipo debe definirse en `core/models` y ser importado por ambos.

    12. **Usar `model()` para two-way binding en controles de formulario.** Para componentes como Input, Toggle, Select, Slider que representan un valor modificable, `model()` es la opción más limpia y idiomática.

---

!!! warning "Errores frecuentes"

    1. **Crear componentes demasiado específicos.** El error más común es crear `ProductCard` en lugar de `Card`, `UserAvatar` en lugar de `Avatar`, `OrderTable` en lugar de `DataTable`. Los nombres deben reflejar la función genérica del componente, no su uso particular.

    2. **No tipificar correctamente los genéricos.** Un `DataTable<any>` anula los beneficios de TypeScript. Debe ser `DataTable<T extends Record<string, any>>` y las columnas deben tipificarse con `Column<T>`.

    3. **Olvidar el estado loading.** Un componente que recibe datos asíncronos siempre debe contemplar un estado de carga. Mostrar una tabla vacía mientras los datos se están cargando confunde al usuario, que piensa que no hay resultados.

    4. **No limpiar timers en ngOnDestroy.** Los `setTimeout` y `setInterval` utilizados para auto-dismiss de toasts o tooltips deben limpiarse al destruir el componente para evitar fugas de memoria e intentos de actualizar estado de un componente destruido.

    5. **Usar `any` en los tipos de eventos emitidos.** Si un `EventEmitter` emite `any`, el componente padre no tiene información sobre la forma de los datos que recibe, eliminando la seguridad de tipos.

    6. **No bloquear el scroll del body en modales.** Un modal abierto sin `overflow: hidden` en el body permite al usuario hacer scroll del contenido detrás del modal, una experiencia de usuario deficiente.

    7. **Implementar mal la trampa de foco en modales.** Sin trampa de foco, un usuario navegando con Tab puede salir del modal y perderse en elementos del fondo que no deberían ser accesibles.

    8. **Iconos sin `aria-hidden`.** Los iconos decorativos deben tener `aria-hidden="true"` para que los lectores de pantalla no intenten leerlos. Si el icono transmite información, debe tener una etiqueta `aria-label`.

    9. **Usar clases CSS de Tailwind inline en lugar de `computed` signals.** Cuando un elemento tiene más de 3-4 clases condicionales, extraer la lógica a un `computed` que devuelva un string de clases mejora la legibilidad del template.

    10. **No proporcionar ejemplos de uso.** Un componente sin documentación de cómo usarlo, aunque esté perfectamente implementado, no será utilizado correctamente por otros desarrolladores. Storybook resuelve este problema.

    11. **Confundir `viewChild` con `contentChild`.** `viewChild` accede a elementos del template propio. `contentChild` accede a elementos proyectados por el padre. Confundirlos resulta en referencias `undefined`.

    12. **No respetar el tamaño del bundle.** Cada dependencia (librería de iconos, utilidades, animaciones) añadida a un componente reutilizable incrementa el tamaño del bundle final. Evaluar si la funcionalidad justifica el coste.

---

!!! abstract "Resumen"

    Esta unidad ha abordado en profundidad el diseño e implementación de componentes de interfaz de usuario reutilizables en Angular, cubriendo:

    - Las **cuatro características esenciales** de un componente reutilizable: genericidad, configurabilidad, ausencia de acoplamiento y documentación exhaustiva.

    - La **aplicación de los principios SOLID** al diseño de componentes UI, con énfasis en la Responsabilidad Única (un componente, un propósito) y el Principio Abierto/Cerrado (extensible sin modificar).

    - Un **catálogo completo de 14 componentes** con su interfaz TypeScript, implementación Angular + Tailwind, variantes y consideraciones de accesibilidad: Button, Input/FormField, Card, Modal, Dropdown, DataTable, Tabs, Toast, Badge, Avatar, Skeleton, Progress, Tooltip y Empty State.

    - El uso de **proyección de contenido** (`ng-content` con selectores) para crear componentes compuestos flexibles que permiten al consumidor personalizar cada zona (header, body, footer).

    - La gestión de los **cuatro estados fundamentales** de interfaz: loading (skeleton), empty (ilustración + mensaje), error (mensaje + reintentar) y data (contenido real).

    - La **accesibilidad como parte integral** del diseño, no como un añadido posterior: roles ARIA correctos, navegación por teclado, gestión del foco, textos para lectores de pantalla y contraste de color.

---

## Recursos complementarios

### Documentación oficial
- Angular — **Signal Inputs**: https://angular.dev/guide/signals/inputs
- Angular — **Model Inputs**: https://angular.dev/guide/signals/model
- Angular — **Content Projection**: https://angular.dev/guide/components/content-projection
- Tailwind CSS — **Hover, Focus, and Other States**: https://tailwindcss.com/docs/hover-focus-and-other-states
- **ARIA Authoring Practices Guide (WAI)**: https://www.w3.org/WAI/ARIA/apg/

### Bibliotecas de referencia
- **Angular CDK** (Component Dev Kit): https://material.angular.io/cdk
- **TanStack Table** (inspiración para DataTable): https://tanstack.com/table
- **Radix UI** (inspiración de accesibilidad): https://www.radix-ui.com

### Artículos y guías
- "Building Reusable Components in Angular" — Tim Deschryver
- "Compound Components Pattern in Angular" — Angular Addicts
- "The Guide to Accessible Components" — Sara Soueidan
- "A Complete Guide to Angular Signal Components" — This is Angular Blog
- "Tailwind CSS Component Patterns" — Tailwind CSS Blog

### Herramientas
- **axe DevTools**: extensión para auditoría de accesibilidad en el navegador.
- **Storybook**: desarrollo y documentación aislada de componentes (Unidad 14).
- **Chromatic**: testing visual y revisión de cambios en componentes UI.
- **Figma**: diseño visual de componentes y definición de variantes.

### Libros
- "Atomic Design" — Brad Frost (metodología de composición de componentes).
- "Refactoring UI" — Adam Wathan y Steve Schoger (diseño de componentes con Tailwind).
- "Inclusive Components" — Heydon Pickering (patrones de componentes accesibles).
- "Design Systems" — Alla Kholmatova (arquitectura de sistemas de diseño).
