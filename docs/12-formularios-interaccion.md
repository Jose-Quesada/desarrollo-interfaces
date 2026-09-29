---
icon: lucide/text-cursor-input
---

# Formularios e Interacción

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:
- Diseñar e implementar formularios reactivos avanzados con Angular Reactive Forms, integrando feedback visual inmediato mediante Tailwind CSS.
- Crear validadores personalizados síncronos y asíncronos, incluyendo validación cross-field y validación contra APIs externas.
- Construir sistemas de mensajes de error contextualizados, internacionalizados y accesibles que mejoren la experiencia de usuario.
- Implementar patrones avanzados de UX en formularios: wizards multi-paso, formularios dinámicos con FormArray, auto-guardado de borradores y confirmación de salida.
- Gestionar el feedback visual en todos los estados de interacción: loading, éxito, error y transiciones entre estados.
- Aplicar técnicas de micro-interacciones (animaciones sutiles) para mejorar la percepción de respuesta y calidad de la interfaz.
- Integrar máscaras de entrada, autocompletado y sugerencias para reducir errores del usuario en la entrada de datos.

## Resultado de aprendizaje asociado

Esta unidad contribuye, como RA principal, al **RA 1** del módulo profesional 0488 *Desarrollo de interfaces* (CFGS en Desarrollo de Aplicaciones Multiplataforma, DAM — currículo andaluz, BOJA; actualizado por el RD 405/2023, BOE):

> **RA 1.** Genera interfaces gráficos de usuario mediante editores visuales utilizando las funcionalidades del editor y adaptando el código generado.

Criterios de evaluación oficiales que se trabajan en esta unidad:

- CE d) Se han modificado las propiedades de los componentes para adecuarlas a las necesidades de la aplicación.
- CE g) Se han asociado a los eventos las acciones correspondientes.
- CE h) Se ha desarrollado una aplicación que incluye el interfaz gráfico obtenido.

Como RA secundario, se vincula al **RA 3** («Crea componentes visuales valorando y empleando herramientas específicas»):

- CE b) Se han creado componentes visuales (componentes de formulario reutilizables).
- CE d) Se han determinado los eventos a los que debe responder el componente y se les han asociado las acciones correspondientes.

!!! note "Conocimientos previos"

    El alumnado debe poseer los siguientes conocimientos antes de abordar esta unidad:
    - **Angular Reactive Forms**: FormControl, FormGroup, FormBuilder, valueChanges, statusChanges.
    - **TypeScript**: tipos avanzados, funciones como parámetros y retorno, genéricos, utility types.
    - **Tailwind CSS 4**: clases utilitarias, animaciones, transiciones, personalización con @theme.
    - **RxJS básico**: Observables, operadores (debounceTime, distinctUntilChanged, filter, switchMap, catchError).
    - **Angular Signals**: signal, computed, effect, toObservable.
    - **HTML5**: validación nativa de formularios, atributos de accesibilidad web (aria-required, aria-invalid, aria-describedby).
    - **UX**: principios de diseño de formularios, ley de Fitts, carga cognitiva, jerarquía visual.

## Contenidos

1. Reactive Forms en profundidad orientado a interfaces
2. Validaciones síncronas y asíncronas
3. Mensajes de error y feedback visual
4. UX avanzada en formularios
5. Feedback visual y micro-interacciones

## Desarrollo teórico

### SECCIÓN A — REACTIVE FORMS EN PROFUNDIDAD ORIENTADO A INTERFACES

#### FormControl, FormGroup y FormArray con enfoque en UI

!!! info "Definición"

    **Angular Reactive Forms** proporciona un modelo de programación reactivo para gestionar formularios. A diferencia de **Template-Driven Forms**, donde la lógica reside en el template HTML, Reactive Forms sitúan el control y la validación en la clase del componente TypeScript, ofreciendo mayor control, testabilidad y previsibilidad. En el contexto del desarrollo de interfaces, esta separación es crucial porque permite que la lógica de validación y el estado del formulario estén disponibles programáticamente para generar feedback visual rico y contextual.

El `FormControl` es la unidad atómica de un formulario reactivo: representa un único campo de entrada y encapsula su valor, estado de validación, si ha sido tocado (touched), si está sucio (dirty) y si está pendiente de validación asíncrona (pending). Cada uno de estos estados se traduce en feedback visual para el usuario.

El `FormGroup` agrupa un conjunto de FormControls, representando una sección coherente de un formulario o el formulario completo. Proporciona acceso a los valores agregados, al estado de validación global y permite la validación **cross-field** (entre campos del grupo).

El `FormArray` gestiona una colección dinámica de FormControls, FormGroups o incluso otros FormArrays, permitiendo al usuario añadir y eliminar elementos repetibles como líneas de factura, direcciones o miembros de un equipo.

Ejemplo de estructura de formulario complejo usando **FormBuilder**:

```
this.invoiceForm = this.fb.group({
  header: this.fb.group({
    number: ['', [Validators.required, Validators.pattern(/^FAC-\d{4}-\d{4}$/)]],
    date: [new Date().toISOString().split('T')[0], Validators.required],
    dueDate: ['', Validators.required],
  }),
  client: this.fb.group({
    name: ['', Validators.required],
    cif: ['', [Validators.required, cifValidator()]],
    email: ['', [Validators.required, Validators.email]],
  }),
  lines: this.fb.array([this.createLine()]),
  totals: this.fb.group({
    subtotal: [{ value: 0, disabled: true }],
    tax: [{ value: 0, disabled: true }],
    total: [{ value: 0, disabled: true }],
  }),
});
```

#### Estados del control y su traducción a feedback visual

Cada `FormControl` y `FormGroup` expone propiedades que describen su estado actual y que son fundamentales para proporcionar **feedback visual** al usuario. La correcta interpretación de estos estados es lo que distingue un formulario profesional de uno amateur.

**touched / untouched:** Un control se considera `touched` cuando el usuario ha interactuado con él y luego ha salido (ha perdido el foco). La propiedad `untouched` es el estado inicial. Esta distinción es crucial para la UX: ==no debemos mostrar errores de validación en campos que el usuario ni siquiera ha visto aún==. Mostrar un formulario lleno de mensajes de error rojos antes de que el usuario haya escrito nada es una experiencia pésima.

**Regla de oro para mostrar errores:**
```
// Mal: mostrar error siempre
if (control.invalid) { ... }

// Bien: mostrar error solo después de tocar
if (control.invalid && control.touched) { ... }

// Bien: mostrar error si se intentó enviar
if (control.invalid && (control.touched || formSubmitted)) { ... }
```

**dirty / pristine:** Un control es `dirty` si el usuario ha modificado su valor desde que se cargó, y `pristine` si no lo ha hecho. Este estado es útil para detectar cambios sin guardar, activar avisos de "estas seguro de que quieres salir" y habilitar/deshabilitar botones de guardar.

```
isDirty = computed(() => this.form.dirty);
canSave = computed(() => this.form.valid && this.form.dirty);
```

**valid / invalid:** La propiedad `valid` indica que todos los validadores del control (sincronos y asincronos) han pasado satisfactoriamente. `invalid` indica que al menos un validador ha fallado. Desde Angular 12, estas propiedades solo se actualizan despues de que el estado `pending` se haya resuelto.

**pending:** Este estado indica que hay al menos un validador asincrono en curso. Es una senal para mostrar un indicador de carga (spinner) junto al campo, informando al usuario de que se esta verificando algo (por ejemplo, "Comprobando disponibilidad del email...").

#### Patron de clases CSS condicionales segun estado del control

La integracion de los estados del FormControl con las clases de Tailwind produce formularios visualmente ricos que guian al usuario de forma intuitiva:

```
@Component({
  template: `
    <input
      [formControl]="emailControl"
      class="block w-full rounded-lg border px-3 py-2 text-sm transition-colors duration-200"
      [ngClass]="emailClasses()"
      placeholder="correo@ejemplo.com" />
    @if (showEmailError()) {
      <p class="mt-1 text-xs text-red-500 animate-fadeIn">{{ emailErrorMessage() }}</p>
    }
    @if (emailControl.pending) {
      <p class="mt-1 text-xs text-gray-400 flex items-center gap-1">
        <span class="animate-spin">&#8635;</span> Verificando email...
      </p>
    }
  `,
})
export class LoginFormComponent {
  emailControl = new FormControl('', {
    validators: [Validators.required, Validators.email],
    asyncValidators: [this.emailExistsValidator()],
    updateOn: 'blur',
  });

  emailClasses = computed(() => {
    const c = this.emailControl;
    return {
      'border-gray-300 focus:ring-blue-500 focus:border-blue-500': c.pristine,
      'border-green-400 focus:ring-green-500 focus:border-green-500': c.valid && c.touched,
      'border-red-400 focus:ring-red-500 focus:border-red-500': c.invalid && c.touched,
      'border-yellow-400 bg-yellow-50': c.pending,
    };
  });

  showEmailError = computed(() =>
    this.emailControl.invalid && this.emailControl.touched
  );
}
```

==La clave del patron es el mapeo de estados==:
- **Pristine**: borde gris neutro, sin indicacion de correccion o error.
- **Valid + touched**: borde verde, senal silenciosa de "esto esta bien".
- **Invalid + touched**: borde rojo, mensaje de error descriptivo.
- **Pending**: borde amarillo y spinner, comunicando "estoy trabajando en ello".

---

### SECCION B — VALIDACIONES

#### Validadores integrados y su aplicacion practica

Angular proporciona un conjunto de **validadores sincronos** en la clase `Validators` que cubren los casos mas comunes:

```
import { Validators } from '@angular/forms';

const nameControl = new FormControl('', [
  Validators.required,
  Validators.minLength(2),
  Validators.maxLength(50),
]);

const emailControl = new FormControl('', [
  Validators.required,
  Validators.email,
]);

const ageControl = new FormControl(null, [
  Validators.min(0),
  Validators.max(150),
]);
```

Cada validador devuelve un **objeto de error especifico** cuando falla. Por ejemplo, `Validators.required` devuelve `{ required: true }`, `Validators.minLength(3)` devuelve `{ minlength: { requiredLength: 3, actualLength: 1 } }`. Estos objetos de error son la base para construir mensajes de error personalizados y contextualizados.

#### Validadores personalizados (ValidatorFn)

Cuando los validadores integrados no son suficientes, Angular permite crear **validadores personalizados** mediante funciones que implementan la interfaz `ValidatorFn`. Un validador personalizado recibe un `AbstractControl` y devuelve `null` si el valor es valido, o un objeto de error si no lo es.

**Validador de DNI espanol:**

```
export function dniValidator(): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const value = control.value;
    if (!value) return null;

    const dniRegex = /^(\d{8})([A-Z])$/;
    const match = value.toUpperCase().match(dniRegex);

    if (!match) {
      return { dni: { message: 'El formato del DNI no es valido (8 digitos + letra)' } };
    }

    const number = parseInt(match[1], 10);
    const letter = match[2];
    const validLetters = 'TRWAGMYFPDXBNJZSQVHLCKE';
    const calculatedLetter = validLetters[number % 23];

    if (letter !== calculatedLetter) {
      return { dni: { message: 'La letra del DNI no coincide con el numero' } };
    }

    return null;
  };
}
```

**Validador de IBAN espanol:**

```
export function ibanValidator(): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const value = control.value?.replace(/\s/g, '').toUpperCase();
    if (!value) return null;

    if (!/^ES\d{22}$/.test(value)) {
      return { iban: { message: 'Formato IBAN invalido. Debe ser ES seguido de 22 digitos' } };
    }

    const rearranged = value.substring(4) + value.substring(0, 4);
    const numeric = rearranged.replace(/[A-Z]/g, (char: string) =>
      (char.charCodeAt(0) - 55).toString()
    );

    const remainder = BigInt(numeric) % 97n;
    if (remainder !== 1n) {
      return { iban: { message: 'El IBAN no es valido (digito de control incorrecto)' } };
    }

    return null;
  };
}
```

**Validador de codigo postal espanol:**

```
export function postalCodeValidator(): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const value = control.value;
    if (!value) return null;

    if (!/^(0[1-9]|[1-4]\d|5[0-2])\d{3}$/.test(value)) {
      return { postalCode: { message: 'Codigo postal no valido. Debe ser un CP espanol valido (5 digitos)' } };
    }

    return null;
  };
}
```

#### Validacion cross-field

La **validacion cross-field** verifica la coherencia entre dos o mas campos del formulario. El caso mas comun es la confirmacion de contrasena. Los validadores cross-field se aplican al `FormGroup` que contiene los campos a comparar, no a los FormControls individuales:

```
export function passwordMatchValidator(
  passwordKey: string,
  confirmKey: string
): ValidatorFn {
  return (group: AbstractControl): ValidationErrors | null => {
    const password = group.get(passwordKey);
    const confirm = group.get(confirmKey);

    if (!password || !confirm) return null;

    if (password.value !== confirm.value) {
      const error = { passwordMismatch: true };
      confirm.setErrors({ ...confirm.errors, ...error });
      return error;
    }

    if (confirm.hasError('passwordMismatch')) {
      const { passwordMismatch, ...otherErrors } = confirm.errors || {};
      confirm.setErrors(Object.keys(otherErrors).length ? otherErrors : null);
    }

    return null;
  };
}
```

Otro ejemplo comun es la verificacion de rangos de fecha:

```
export function dateRangeValidator(startKey: string, endKey: string): ValidatorFn {
  return (group: AbstractControl): ValidationErrors | null => {
    const start = group.get(startKey)?.value;
    const end = group.get(endKey)?.value;

    if (!start || !end) return null;

    if (new Date(end) <= new Date(start)) {
      return { dateRange: { message: 'La fecha de fin debe ser posterior a la de inicio' } };
    }

    return null;
  };
}
```

#### Validacion asincrona (AsyncValidator)

La **validacion asincrona** es necesaria cuando la validez de un campo depende de una comprobacion externa, tipicamente una llamada a una API. El caso de uso mas frecuente es verificar la unicidad de un nombre de usuario o correo electronico contra la base de datos:

```
private emailExistsValidator(): AsyncValidatorFn {
  return (control: AbstractControl): Observable<ValidationErrors | null> => {
    if (!control.value) return of(null);

    return this.userService.checkEmailExists(control.value).pipe(
      debounceTime(500),
      distinctUntilChanged(),
      map(exists => exists ? { emailExists: true } : null),
      catchError(() => of(null)),
      first(),
    );
  };
}

// Uso
this.emailControl = new FormControl('', {
  validators: [Validators.required, Validators.email],
  asyncValidators: [this.emailExistsValidator()],
  updateOn: 'blur',
});
```

El uso de `debounceTime(500)` es esencial para no saturar el servidor con una petición por cada pulsación de tecla. `distinctUntilChanged()` evita peticiones duplicadas para el mismo valor. El estado `pending` del control se activa automaticamente mientras el validador asincrono esta en curso, permitiendo mostrar feedback visual.

#### Opcion updateOn: cuando validar

!!! tip "Opcion updateOn"

    La opcion `updateOn` controla en que momento se ejecutan los validadores y se actualizan los valores del control:
    - `'change'` (por defecto): en cada pulsacion de tecla o cambio.
    - `'blur'`: cuando el control pierde el foco.
    - `'submit'`: solo cuando el formulario se envia.

    La eleccion tiene un impacto directo en la **UX**. `'change'` proporciona el feedback mas inmediato pero puede generar demasiadas peticiones en validaciones asincronas. `'blur'` retrasa la validacion hasta que el usuario termina con el campo y pasa al siguiente, siendo mas respetuoso con el usuario y mas eficiente. `'submit'` concentra toda la validacion en el momento del envio; puede ser frustrante para formularios largos pero apropiado para formularios cortos. La opcion recomendada para la mayoria de formularios es `'blur'`.

---

### SECCIÓN C — MENSAJES DE ERROR

#### Sistema de mensajes de error personalizados

Un sistema profesional de **mensajes de error** debe ser capaz de mostrar el mensaje adecuado para cada tipo de error de validacion, en el idioma del usuario, y en el momento oportuno. La implementacion tipica consiste en una funcion que mapea los errores de validacion a mensajes de texto:

```
getErrorMessage(control: AbstractControl, fieldName: string): string | null {
  if (!control.errors || (!control.touched && !this.formSubmitted)) return null;

  const errors = control.errors;

  if (errors['required']) return `El campo "${fieldName}" es obligatorio`;
  if (errors['email']) return 'Introduce una direccion de correo electronico valida';
  if (errors['minlength']) return `${fieldName} debe tener al menos ${errors['minlength'].requiredLength} caracteres`;
  if (errors['maxlength']) return `${fieldName} no puede superar los ${errors['maxlength'].requiredLength} caracteres`;
  if (errors['min']) return `El valor minimo es ${errors['min'].min}`;
  if (errors['max']) return `El valor maximo es ${errors['max'].max}`;
  if (errors['pattern']) return `El formato de "${fieldName}" no es valido`;
  if (errors['emailExists']) return 'Este email ya esta registrado';
  if (errors['dni']) return errors['dni'].message;
  if (errors['iban']) return errors['iban'].message;
  if (errors['dateRange']) return errors['dateRange'].message;
  if (errors['passwordMismatch']) return 'Las contrasenas no coinciden';

  return 'Campo invalido';
}
```

**Componente FormErrorComponent reutilizable:**

Este componente encapsula toda la logica de presentacion de errores, recibiendo el control y el nombre del campo como inputs:

```
@Component({
  selector: 'ui-form-error',
  standalone: true,
  imports: [NgClass],
  template: `
    @if (errorMessage()) {
      <p class="mt-1.5 text-xs text-red-600 animate-slideIn flex items-start gap-1" role="alert">
        <svg class="h-3.5 w-3.5 mt-0.5 shrink-0" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
        <span>{{ errorMessage() }}</span>
      </p>
    }
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FormErrorComponent implements OnInit, OnDestroy {
  control = input.required<AbstractControl>();
  fieldName = input('Este campo');
  showOnSubmit = input(false);

  errorMessage = signal<string | null>(null);
  private statusSub?: Subscription;

  ngOnInit(): void {
    this.statusSub = this.control().statusChanges.subscribe(() => {
      this.updateErrorMessage();
    });
  }

  private updateErrorMessage(): void {
    const ctrl = this.control();
    if (!ctrl.errors || (!ctrl.touched && !this.showOnSubmit())) {
      this.errorMessage.set(null);
      return;
    }
    this.errorMessage.set(this.resolveMessage(ctrl.errors, this.fieldName()));
  }

  private resolveMessage(errors: ValidationErrors, field: string): string {
    if (errors['required']) return `"${field}" es obligatorio`;
    if (errors['email']) return 'Introduce un email valido';
    if (errors['minlength']) return `Minimo ${errors['minlength'].requiredLength} caracteres`;
    if (errors['maxlength']) return `Maximo ${errors['maxlength'].requiredLength} caracteres`;
    if (errors['passwordMismatch']) return 'Las contrasenas no coinciden';
    return 'Valor invalido';
  }

  ngOnDestroy(): void {
    this.statusSub?.unsubscribe();
  }
}
```

#### UX de validacion: reglas de oro

!!! tip "Reglas de oro"

    1. **No mostrar errores antes de la interaccion.** Un formulario recien cargado debe verse limpio, sin campos en rojo ni mensajes de error. Los errores solo deben aparecer despues de que el usuario haya tocado el campo (touched && invalid) o tras un intento de envio.

    2. **Validar en el momento adecuado.** Para campos con restricciones de formato (email, telefono, DNI), validar en `blur` es generalmente la mejor opcion.

    3. **Limpieza de errores al corregir.** Tan pronto como el usuario corrige un campo y este se vuelve valido, el mensaje de error debe desaparecer y el borde del campo debe cambiar a un color neutro o de confirmacion (verde).

    4. **Resumen de errores en el envio.** Si el usuario intenta enviar un formulario con multiples campos invalidos, es buena practica mostrar un resumen en la parte superior, marcar todos los campos invalidos como `touched` y hacer scroll automatico al primer error:

    ```
    submitForm(): void {
      this.formSubmitted = true;

      if (this.form.invalid) {
        this.markFormGroupTouched(this.form);

        setTimeout(() => {
          const firstError = document.querySelector('.ng-invalid');
          firstError?.scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
        return;
      }

      this.processForm();
    }

    private markFormGroupTouched(formGroup: FormGroup): void {
      Object.values(formGroup.controls).forEach(control => {
        control.markAsTouched();
        if (control instanceof FormGroup) {
          this.markFormGroupTouched(control);
        }
      });
    }
    ```

---

### SECCIÓN D — UX EN FORMULARIOS: TEMAS AVANZADOS

#### Formularios multi-paso (Wizard/Stepper)

Los **formularios multi-paso** dividen un formulario largo en pasos secuenciales, reduciendo la carga cognitiva y la tasa de abandono. Cada paso es un `FormGroup` independiente, y un `FormGroup` principal los agrupa a todos.

La implementacion con Signals para el paso actual proporciona una experiencia fluida. El componente Wizard incluye: barra de progreso visual con pasos numerados, lineas conectoras entre pasos que cambian de color al completarse, contenido del paso actual renderizado con `@switch`, y botones de navegacion "Anterior" y "Siguiente" (el ultimo paso muestra "Completar").

```
@Component({
  standalone: true,
  template: `
    <nav class="mb-8" aria-label="Progreso">
      <ol class="flex items-center">
        @for (step of steps; track step.id; let i = $index) {
          <li class="flex items-center" [class.flex-1]="i < steps.length - 1">
            <button type="button" class="flex items-center gap-2"
                    [disabled]="!canGoToStep(i)" (click)="goToStep(i)">
              <span class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full text-sm font-medium"
                    [ngClass]="isStepComplete(i) ? 'bg-blue-600 text-white' : 'border-2 border-gray-300 text-gray-500'">
                @if (isStepComplete(i)) { &#10003; } @else { {{ i + 1 }} }
              </span>
              <span class="hidden sm:block text-sm font-medium">{{ step.label }}</span>
            </button>
            @if (i < steps.length - 1) {
              <div class="mx-2 h-0.5 flex-1 rounded"
                   [ngClass]="isStepComplete(i) ? 'bg-blue-500' : 'bg-gray-200'"></div>
            }
          </li>
        }
      </ol>
    </nav>

    <form [formGroup]="form">
      @switch (currentStep()) {
        @case (0) { <ng-container [formGroup]="personalInfo"> ... </ng-container> }
        @case (1) { <ng-container [formGroup]="accountInfo"> ... </ng-container> }
        @case (2) { <ng-container [formGroup]="review"> ... </ng-container> }
      }
    </form>

    <div class="mt-8 flex justify-between">
      @if (currentStep() > 0) {
        <ui-button variant="secondary" (clicked)="previousStep()">Anterior</ui-button>
      } @else { <div></div> }
      @if (currentStep() < steps.length - 1) {
        <ui-button variant="primary" (clicked)="nextStep()">Siguiente</ui-button>
      } @else {
        <ui-button variant="primary" (clicked)="submit()" [loading]="submitting()">Completar</ui-button>
      }
    </div>
  `,
})
export class WizardFormComponent {
  currentStep = signal(0);
  completedSteps = signal<Set<number>>(new Set());

  steps = [
    { id: 'personal', label: 'Datos personales', group: 'personalInfo' },
    { id: 'account', label: 'Cuenta', group: 'accountInfo' },
    { id: 'review', label: 'Revision', group: 'review' },
  ];

  form = this.fb.group({
    personalInfo: this.fb.group({
      firstName: ['', Validators.required],
      lastName: ['', Validators.required],
      dni: ['', [Validators.required, dniValidator()]],
    }),
    accountInfo: this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      passwords: this.fb.group({
        password: ['', [Validators.required, Validators.minLength(8)]],
        confirm: ['', Validators.required],
      }, { validators: passwordMatchValidator('password', 'confirm') }),
    }),
    review: this.fb.group({
      acceptTerms: [false, Validators.requiredTrue],
    }),
  });

  currentGroup = computed(() =>
    this.form.get(this.steps[this.currentStep()].group) as FormGroup
  );

  nextStep(): void {
    if (this.currentGroup().invalid) {
      this.markGroupTouched(this.currentGroup());
      return;
    }
    this.completedSteps.update(s => new Set(s).add(this.currentStep()));
    this.currentStep.update(s => Math.min(s + 1, this.steps.length - 1));
  }

  previousStep(): void {
    this.currentStep.update(s => Math.max(s - 1, 0));
  }
}
```

#### Formularios dinamicos con FormArray

Los `FormArray` permiten crear formularios donde el usuario puede anadir y eliminar dinamicamente grupos de campos. Este patron es esencial para interfaces como facturas (anadir/quitar lineas), formularios de direcciones (multiples direcciones de envio), o gestion de equipos (anadir/quitar miembros).

La implementacion con **Signals** para calcular totales derivados en tiempo real hace que el formulario sea reactivo y eficiente:

```
@Component({
  standalone: true,
  template: `
    <div formArrayName="lines">
      <div class="space-y-4">
        @for (line of lines.controls; track line; let i = $index) {
          <div [formGroupName]="i"
               class="rounded-lg border border-gray-200 p-4 transition-all duration-300">
            <div class="grid grid-cols-12 gap-3">
              <div class="col-span-5">
                <ui-form-field label="Descripcion" [control]="getControl(line, 'description')" />
              </div>
              <div class="col-span-2">
                <ui-form-field label="Cantidad" type="number" [control]="getControl(line, 'quantity')" />
              </div>
              <div class="col-span-2">
                <ui-form-field label="Precio" type="number" [control]="getControl(line, 'unitPrice')" />
              </div>
              <div class="col-span-2">
                <label class="block text-sm font-medium text-gray-700">Total</label>
                <p class="mt-2 text-sm font-semibold text-gray-900">
                  {{ lineTotals()[i] | currency:'EUR' }}
                </p>
              </div>
              <div class="col-span-1 flex items-end justify-center pb-2">
                <button type="button"
                        class="rounded-lg p-2 text-gray-400 hover:bg-red-50 hover:text-red-600"
                        [disabled]="lines.length === 1"
                        (click)="removeLine(i)"
                        aria-label="Eliminar linea {{ i + 1 }}">&#10005;</button>
              </div>
            </div>
          </div>
        }
      </div>
    </div>

    <button type="button"
            class="mt-4 flex items-center gap-2 text-sm font-medium text-blue-600 hover:text-blue-700"
            (click)="addLine()">
      + Anadir linea
    </button>

    <div class="mt-6 border-t border-gray-200 pt-4">
      <div class="flex justify-end">
        <dl class="w-64 space-y-2 text-sm">
          <div class="flex justify-between">
            <dt class="text-gray-500">Subtotal</dt>
            <dd class="font-medium">{{ subtotal() | currency:'EUR' }}</dd>
          </div>
          <div class="flex justify-between">
            <dt class="text-gray-500">IVA (21%)</dt>
            <dd class="font-medium">{{ tax() | currency:'EUR' }}</dd>
          </div>
          <div class="flex justify-between border-t pt-2 text-base">
            <dt class="font-semibold">Total</dt>
            <dd class="font-bold">{{ total() | currency:'EUR' }}</dd>
          </div>
        </dl>
      </div>
    </div>
  `,
})
export class InvoiceFormComponent {
  private fb = inject(FormBuilder);
  invoiceForm = this.fb.group({ lines: this.fb.array([this.createLine()]) });

  get lines(): FormArray { return this.invoiceForm.get('lines') as FormArray; }

  lineTotals = computed(() =>
    this.lines.controls.map((_, i) => {
      const line = this.lines.at(i);
      return (line.get('quantity')?.value || 0) * (line.get('unitPrice')?.value || 0);
    })
  );

  subtotal = computed(() => this.lineTotals().reduce((s, t) => s + t, 0));
  tax = computed(() => this.subtotal() * 0.21);
  total = computed(() => this.subtotal() + this.tax());

  createLine(): FormGroup {
    return this.fb.group({
      description: ['', Validators.required],
      quantity: [1, [Validators.required, Validators.min(1)]],
      unitPrice: [0, [Validators.required, Validators.min(0)]],
    });
  }

  addLine(): void {
    this.lines.push(this.createLine());
    setTimeout(() => {
      const last = document.querySelector('[formarrayname="lines"] > div:last-child');
      last?.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }

  removeLine(index: number): void { this.lines.removeAt(index); }
}
```

#### Auto-guardado de formularios (draft)

El **auto-guardado de borradores** mejora drasticamente la experiencia de usuario en formularios largos. Consiste en guardar automaticamente el estado del formulario en localStorage a medida que el usuario rellena los campos:

```
@Injectable({ providedIn: 'root' })
export class FormDraftService {
  private readonly PREFIX = 'form_draft_';

  save(formId: string, data: any): void {
    localStorage.setItem(this.PREFIX + formId, JSON.stringify({ data, timestamp: Date.now() }));
  }

  load(formId: string): any | null {
    const stored = localStorage.getItem(this.PREFIX + formId);
    if (!stored) return null;
    const draft = JSON.parse(stored);
    if (Date.now() - draft.timestamp > 24 * 60 * 60 * 1000) {
      this.clear(formId);
      return null;
    }
    return draft.data;
  }

  clear(formId: string): void { localStorage.removeItem(this.PREFIX + formId); }
  hasDraft(formId: string): boolean { return !!localStorage.getItem(this.PREFIX + formId); }

  getDraftAge(formId: string): string | null {
    const stored = localStorage.getItem(this.PREFIX + formId);
    if (!stored) return null;
    const minutes = Math.floor((Date.now() - JSON.parse(stored).timestamp) / 60000);
    if (minutes < 1) return 'hace unos segundos';
    if (minutes < 60) return `hace ${minutes} minutos`;
    return `hace ${Math.floor(minutes / 60)} horas`;
  }
}

// Uso en el componente
@Component({ ... })
export class ProductFormComponent implements OnInit, OnDestroy {
  private draftService = inject(FormDraftService);
  private readonly FORM_ID = 'product_create';
  productForm = this.fb.group({ ... });
  private draftSub?: Subscription;

  ngOnInit(): void {
    const draft = this.draftService.load(this.FORM_ID);
    if (draft && confirm('Tienes un borrador. ¿Recuperarlo?')) {
      this.productForm.patchValue(draft);
    }
    this.draftSub = this.productForm.valueChanges.pipe(
      debounceTime(2000),
      filter(() => this.productForm.dirty),
    ).subscribe(value => this.draftService.save(this.FORM_ID, value));
  }

  submitForm(): void {
    if (this.productForm.valid) {
      // enviar al servidor...
      this.draftService.clear(this.FORM_ID);
    }
  }

  ngOnDestroy(): void { this.draftSub?.unsubscribe(); }
}
```

#### Confirmacion al salir sin guardar (CanDeactivate)

El guard `CanDeactivate` de Angular Router protege al usuario de perder **cambios no guardados** al navegar a otra pagina:

```
export interface CanComponentDeactivate {
  canDeactivate: () => boolean | Observable<boolean> | Promise<boolean>;
}

@Injectable({ providedIn: 'root' })
export class PendingChangesGuard implements CanDeactivate<CanComponentDeactivate> {
  canDeactivate(component: CanComponentDeactivate): boolean | Observable<boolean> | Promise<boolean> {
    return component.canDeactivate ? component.canDeactivate() : true;
  }
}

// En el componente
@Component({ ... })
export class ProductEditComponent implements CanComponentDeactivate {
  productForm = this.fb.group({ ... });
  submitted = false;

  canDeactivate(): boolean {
    if (this.submitted || this.productForm.pristine) return true;
    return confirm('Tienes cambios sin guardar. ¿Estas seguro de que quieres salir?');
  }

  submitForm(): void {
    // guardar datos...
    this.submitted = true;
  }
}
```

#### Mascaras de input

Las **mascaras de entrada** guian al usuario en la introduccion de datos con formato especifico, reduciendo errores y mejorando la velocidad de entrada:

```
@Directive({
  selector: '[uiPhoneMask]',
  standalone: true,
  host: { '(input)': 'onInput($event)', '(keydown)': 'onKeydown($event)' },
})
export class PhoneMaskDirective implements ControlValueAccessor {
  private onChange: (value: string) => void = () => {};
  private onTouched: () => void = () => {};

  onInput(event: Event): void {
    const input = event.target as HTMLInputElement;
    let value = input.value.replace(/\D/g, '');
    if (value.startsWith('34')) value = value.substring(2);

    if (value.length > 3) value = value.substring(0, 3) + ' ' + value.substring(3);
    if (value.length > 7) value = value.substring(0, 7) + ' ' + value.substring(7);
    value = value.substring(0, 11);

    input.value = value;
    this.onChange(value.replace(/\s/g, ''));
  }

  onKeydown(event: KeyboardEvent): void {
    const allowed = ['Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'Tab'];
    if (allowed.includes(event.key)) return;
    if (!/^\d$/.test(event.key)) event.preventDefault();
  }

  writeValue(value: string): void { ... }
  registerOnChange(fn: any): void { this.onChange = fn; }
  registerOnTouched(fn: any): void { this.onTouched = fn; }
}
```

---

### SECCION E — FEEDBACK VISUAL Y MICRO-INTERACCIONES

#### Estados de boton y transiciones

Los botones deben comunicar claramente su estado en cada momento mediante representacion visual distinta y **transiciones suaves**:
- **Default:** Color de fondo correspondiente a la variante.
- **Hover:** Oscurecimiento ligero o cambio de elevacion.
- **Active/Pressed:** Oscurecimiento adicional o reduccion de escala (0.98).
- **Focus visible:** Anillo de foco (solo con navegacion por teclado).
- **Disabled:** Atenuacion (menor opacidad) y cursor `not-allowed`.
- **Loading:** Spinner animado, el texto se oculta visualmente pero permanece para lectores de pantalla. El boton mantiene el mismo tamano.

Estas transiciones se implementan con `transition-all duration-150` y las variantes `hover:`, `active:`, `focus-visible:`, `disabled:` de Tailwind.

#### Micro-interacciones

Las **micro-interacciones** son animaciones pequenas y sutiles que mejoran la percepcion de respuesta y calidad de la interfaz. Cada micro-interaccion debe tener un proposito funcional, no meramente decorativo.

**Shake en error:** Comunicacion instintiva de error mediante sacudida horizontal:

```
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  20% { transform: translateX(-4px); }
  40% { transform: translateX(4px); }
  60% { transform: translateX(-4px); }
  80% { transform: translateX(4px); }
}
.animate-shake { animation: shake 0.4s ease-in-out; }
```

Esta clase se aplica condicionalmente al intentar enviar un formulario con errores:
```
// Template
<input [class.animate-shake]="shouldShake()" ... />

// Componente
shouldShake = computed(() => this.formSubmitted && this.emailControl.invalid);
```

**Check de confirmacion:** Cuando un campo se vuelve valido despues de haber sido invalido, una breve animacion confirma al usuario que la correccion fue aceptada:

```
@keyframes checkmark {
  0% { transform: scale(0) rotate(-45deg); opacity: 0; }
  50% { transform: scale(1.3) rotate(0deg); }
  100% { transform: scale(1) rotate(0deg); opacity: 1; }
}
.animate-checkmark { animation: checkmark 0.3s ease-out; }
```

**Slide in para mensajes de error:** Los mensajes de error deben aparecer con una animacion suave, no abruptamente:

```
@keyframes slideIn {
  from { transform: translateY(-4px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}
.animate-slideIn { animation: slideIn 0.2s ease-out; }
```

**Pulse en campos requeridos vacios:** Si el usuario intenta enviar sin rellenar un campo requerido, una animacion de pulso sutil dirige la atencion:

```
@keyframes errorPulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.4); }
  50% { box-shadow: 0 0 0 4px rgba(239, 68, 68, 0); }
}
.animate-errorPulse { animation: errorPulse 1.5s ease-in-out; }
```

#### Skeleton loading para formularios que cargan datos

Cuando un formulario de edicion carga datos desde el servidor, mostrar campos vacios durante la carga causa desconcierto. En su lugar, se deben mostrar skeleton loaders:

```
@if (loading()) {
  <div class="space-y-4 animate-pulse">
    <div class="h-4 bg-gray-200 rounded w-1/4"></div>
    <div class="h-10 bg-gray-200 rounded w-full"></div>
    <div class="h-4 bg-gray-200 rounded w-1/4 mt-6"></div>
    <div class="h-10 bg-gray-200 rounded w-full"></div>
  </div>
} @else {
  <form [formGroup]="productForm"> ... </form>
}
```

#### Toast de confirmacion tras envio exitoso

Tras un envio exitoso, un **toast de confirmacion** es el cierre perfecto para la interaccion. Debe mostrarse en una ubicacion consistente (esquina superior derecha) y desaparecer automaticamente tras unos segundos. Utilizando el `ToastService` y `ToastComponent` definidos en la Unidad 11, el patron de uso es:

```
submitForm(): void {
  if (this.form.invalid) {
    this.markFormGroupTouched(this.form);
    return;
  }

  this.submitting.set(true);
  this.productService.create(this.form.value).subscribe({
    next: (result) => {
      this.toastService.success('Producto creado', 'El producto se ha guardado correctamente');
      this.router.navigate(['/products', result.id]);
    },
    error: (err) => {
      this.toastService.error('Error al guardar', 'No se pudo crear el producto. Intentalo de nuevo');
      this.submitting.set(false);
    },
  });
}
```

#### Transiciones suaves en cambios de estado

Cada cambio de estado en la interfaz debe estar acompanado de una transicion CSS suave. **Tailwind** proporciona las clases `transition-colors`, `transition-opacity`, `transition-all` con duraciones configurables:

```
// Input con transicion de borde y sombra
<input class="... transition-all duration-200" />

// Contenedor con transicion de altura (wizard steps)
<div class="transition-all duration-300 ease-in-out" ...>
```

---

## Ejemplos guiados

### Ejemplo guiado 1: Formulario de registro completo con todos los estados de validacion y UX

**Objetivo:** Construir un formulario de registro de usuario profesional que ilustre la gestion completa de estados de validacion y feedback visual.

**Paso 1 — Definir la estructura del formulario:**

```
@Component({
  selector: 'app-register-form',
  standalone: true,
  imports: [ReactiveFormsModule, NgClass, FormErrorComponent, ButtonComponent],
  template: `...`,
})
export class RegisterFormComponent {
  private fb = inject(FormBuilder);
  private userService = inject(UserService);
  private router = inject(Router);
  private toastService = inject(ToastService);

  registerForm = this.fb.group({
    personalInfo: this.fb.group({
      fullName: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', {
        validators: [Validators.required, Validators.email],
        asyncValidators: [this.emailExistsValidator()],
        updateOn: 'blur',
      }],
      phone: ['', [Validators.required, Validators.pattern(/^\d{9}$/)]],
    }),
    passwords: this.fb.group({
      password: ['', [Validators.required, Validators.minLength(8), this.passwordStrengthValidator()]],
      confirm: ['', Validators.required],
    }, { validators: this.passwordMatchValidator() }),
    terms: [false, Validators.requiredTrue],
  });

  formSubmitted = signal(false);
  submitting = signal(false);
}
```

**Paso 2 — Implementar el template con feedback visual completo para cada campo:**

El template incluye: labels con indicador de obligatoriedad, inputs con bordes dinamicos segun estado (pristine, valid, invalid, pending), mensajes de error contextuales mediante `ui-form-error`, indicador de fortaleza de contrasena (barra de progreso con colores), y checkbox de aceptacion de terminos con estilo personalizado.

**Paso 3 — Implementar la logica de envio con feedback completo:**

```
submitForm(): void {
  this.formSubmitted.set(true);

  if (this.registerForm.invalid) {
    this.markFormGroupTouched(this.registerForm);
    setTimeout(() => {
      document.querySelector('.ng-invalid')?.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
    return;
  }

  this.submitting.set(true);
  const formData = {
    ...this.registerForm.value.personalInfo,
    password: this.registerForm.value.passwords?.password,
  };

  this.userService.register(formData).subscribe({
    next: () => {
      this.toastService.success('Registro exitoso', 'Tu cuenta ha sido creada. Ya puedes iniciar sesion.');
      this.router.navigate(['/login']);
    },
    error: () => {
      this.toastService.error('Error en el registro', 'No se pudo completar el registro. Intentalo de nuevo.');
      this.submitting.set(false);
    },
  });
}
```

### Ejemplo guiado 2: Formulario multi-paso (wizard) con Signals

**Objetivo:** Construir un wizard de 3 pasos usando la implementacion detallada en la Seccion D, integrando Signals para el paso actual, validacion por paso, barra de progreso visual y navegacion entre pasos.

**Desarrollo:** El alumnado parte del codigo base de `WizardFormComponent` mostrado anteriormente y lo extiende con: resumen de datos introducidos en el paso final, boton "Guardar borrador" que persiste el progreso en `localStorage`, y confirmacion al abandonar el wizard con pasos incompletos.

### Ejemplo guiado 3: Formulario de factura con FormArray dinamico

**Objetivo:** Construir un formulario de factura con lineas de producto dinamicas usando FormArray y Signals para calculos en tiempo real.

**Desarrollo:** Siguiendo la implementacion de `InvoiceFormComponent`, el alumnado anade: validacion de que al menos una linea tenga cantidad > 0 y precio > 0, calculo de IVA variable por linea (21%, 10% o 4% segun tipo de producto), y guardado automatico del borrador de factura en localStorage.

---

## Actividades guiadas

### Actividad guiada 1: Implementar validadores personalizados para un formulario de alta de cliente

**Duracion:** 60 minutos.

**Objetivo:** Crear validadores personalizados para CIF/NIF espanol e IBAN en un formulario de alta de cliente.

**Desarrollo:**
1. El docente explica el formato real del CIF espanol (letra + 7 digitos + digito de control) y del IBAN espanol.
2. El alumnado implementa `cifValidator()` y `ibanValidator()` como funciones que devuelven `ValidatorFn`.
3. Integrar los validadores en un `FormGroup` de cliente y crear el template con feedback visual usando Tailwind.
4. Testear los validadores con valores reales y erroneos.

**Entregable:** Validadores funcionales y componente de formulario de alta de cliente.

### Actividad guiada 2: Construir un sistema de mensajes de error internacionalizado

**Duracion:** 45 minutos.

**Objetivo:** Crear un mapa de mensajes de error que soporte multiples idiomas (espanol e ingles) y un componente `FormErrorComponent` que los utilice.

**Desarrollo:**
1. Implementar un `ErrorMessageService` que contenga un diccionario de mensajes por idioma.
2. Permitir cambiar el idioma dinamicamente mediante un Signal.
3. Integrar el servicio en `FormErrorComponent`.
4. Probar mostrando errores en espanol e ingles.

**Entregable:** `ErrorMessageService` y `FormErrorComponent` internacionalizados.

### Actividad guiada 3: Construir un formulario de busqueda con filtros avanzados y auto-guardado

**Duracion:** 90 minutos.

**Objetivo:** Crear un formulario de busqueda que recuerde los filtros aplicados entre sesiones.

**Desarrollo:**
1. Crear un formulario de busqueda con campos: termino, categoria (dropdown), rango de precio (min/max), ordenacion (select), y fecha (rango de fechas).
2. Implementar auto-guardado de filtros en `localStorage` usando `FormDraftService`.
3. Al cargar la pagina, recuperar los filtros guardados y aplicarlos.
4. Anadir un boton "Limpiar filtros" que resetea el formulario y elimina el borrador.
5. Mostrar un indicador visual de que hay filtros activos (badge en el boton de filtros).

**Entregable:** Componente de busqueda con auto-guardado de filtros.

---

## Actividades propuestas

### Actividad propuesta 1: Formulario de creacion de producto con validacion asincrona de SKU

**Duracion:** 120 minutos.

**Descripcion:** Construir un formulario completo de creacion de producto en una tienda online que incluya validacion asincrona para verificar que el SKU (codigo de producto) no esta duplicado en la base de datos.

**Requisitos:**
- Campos: nombre, SKU, descripcion, precio, categoria (dropdown cargado de API), imagen (URL con previsualizacion), y stock.
- Validacion asincrona del SKU con debounce de 500ms y estado pending visual (spinner + texto "Verificando codigo...").
- Todos los campos requeridos deben mostrar feedback visual segun estado (touched, valid, invalid).
- Boton de guardar deshabilitado hasta que el formulario sea valido y no este pending.
- Barra de progreso de completitud del formulario (porcentaje de campos rellenos).
- Al enviar exitosamente, toast de confirmacion y redireccion a la lista de productos.

**Entregable:** Componente `ProductCreateFormComponent` completo.

### Actividad propuesta 2: Wizard de configuracion de cuenta en 4 pasos

**Duracion:** 180 minutos.

**Descripcion:** Construir un wizard de configuracion de cuenta de usuario con 4 pasos secuenciales.

**Requisitos:**
- Paso 1 — Perfil: nombre, apellidos, fecha de nacimiento, genero.
- Paso 2 — Contacto: email, telefono, direccion, codigo postal.
- Paso 3 — Preferencias: idioma, zona horaria, notificaciones (checkboxes), tema (toggle claro/oscuro).
- Paso 4 — Confirmacion: resumen de todos los datos introducidos con posibilidad de editar cada paso.
- Barra de progreso con 4 pasos: completados (check verde), actual (azul), pendientes (gris).
- Validacion individual de cada paso; no se puede avanzar hasta que el paso actual sea valido.
- Boton "Guardar y continuar despues" que persiste el progreso en localStorage.
- Al completar el ultimo paso, se envia todo el formulario.

**Entregable:** Componente `AccountSetupWizardComponent` y sus subcomponentes.

### Actividad propuesta 3: Formulario dinamico de encuesta con FormArray

**Duracion:** 150 minutos.

**Descripcion:** Construir un formulario de creacion de encuestas donde el usuario pueda anadir y quitar preguntas dinamicamente, y cada pregunta pueda ser de distinto tipo.

**Requisitos:**
- El formulario tiene un titulo y una descripcion (campos fijos).
- Cada pregunta es un FormGroup dentro de un FormArray, con campos: enunciado, tipo (select: texto corto, texto largo, opcion multiple, escala numerica), requerido (checkbox).
- Si el tipo es "opcion multiple", se muestra un FormArray anidado para las opciones de respuesta.
- Animacion de entrada al anadir preguntas (slideIn + fade).
- Boton de eliminar pregunta con confirmacion.
- Calculo en tiempo real del numero total de preguntas y del tiempo estimado de respuesta (5 segundos por pregunta).
- Boton "Previsualizar" que muestra la encuesta tal como la veria el usuario final.

**Entregable:** Componente `SurveyFormComponent` completo.

### Actividad propuesta 4: Componente de busqueda avanzada con filtros y autocompletado

**Duracion:** 150 minutos.

**Descripcion:** Implementar un sistema de busqueda avanzada que combine el componente `Autocomplete` con filtros adicionales.

**Requisitos:**
- Campo de busqueda principal con autocompletado (sugerencias de la API).
- Panel de filtros avanzados que se despliega al hacer click en "Filtros avanzados".
- Filtros: rango de precio, categoria, valoracion minima (estrellas), en stock (toggle), ordenar por (select).
- Los filtros activos se muestran como chips/badges bajo la barra de busqueda, con boton X para eliminar cada uno.
- Debounce de 400ms en la busqueda principal y en los cambios de filtros.
- Contador de resultados visibles y totales.
- Estado de carga (skeleton de resultados) mientras se buscan datos.
- Estado vacio con ilustracion y sugerencias de busqueda alternativa.
- Persistencia de la ultima busqueda y filtros en la URL (query params).

**Entregable:** Componente `SearchInterfaceComponent` completo.

### Actividad propuesta 5: Formulario de checkout multi-paso para e-commerce

**Duracion:** 180 minutos.

**Descripcion:** Implementar el flujo de checkout de un comercio electronico con 3 pasos.

**Requisitos:**
- Paso 1 — Direccion de envio: formulario de direccion con validacion de codigo postal y posibilidad de usar la misma direccion para facturacion (checkbox que copia los datos).
- Paso 2 — Metodo de pago: seleccion de tarjeta (formulario con mascara para numero de tarjeta, fecha de caducidad y CVV) o PayPal.
- Paso 3 — Revision: resumen del pedido con productos, direccion, metodo de pago y total.
- Validacion por paso con imposibilidad de avanzar sin completar el paso actual.
- Temporizador de sesion de 15 minutos con aviso visual cuando quedan 2 minutos.
- Boton "Pagar" que muestra estado de carga durante el procesamiento y toast de exito/error al finalizar.
- Accesibilidad: todos los campos con labels asociados, navegacion por teclado, mensajes de error anunciados por lectores de pantalla.

**Entregable:** Componente `CheckoutWizardComponent` completo.

---

??? "Actividades de ampliacion"

    ### Actividad de ampliacion 1: Sistema de formularios generados por esquema JSON

    **Duracion:** 240 minutos.

    **Descripcion:** Disenar un sistema que genere formularios Angular dinamicamente a partir de un esquema JSON, similar a **JSON Schema Forms**.

    **Requisitos:**
    - Definir un formato de esquema JSON que describa: campos, tipos, validaciones, orden, dependencias entre campos.
    - Crear un componente `DynamicFormComponent` que reciba un esquema y renderice los campos correspondientes.
    - Soportar tipos: text, number, email, select, checkbox, radio, date, textarea, file.
    - Implementar logica de visibilidad condicional: un campo se muestra solo si otro campo tiene cierto valor.
    - Generar el `FormGroup` dinamicamente con todas las validaciones especificadas en el esquema.

    **Entregable:** Sistema de formularios dinamicos con al menos 3 esquemas de ejemplo.

    ### Actividad de ampliacion 2: Comparativa de librerias de formularios para Angular

    **Duracion:** 120 minutos.

    **Descripcion:** Investigar, probar y comparar tres librerias de formularios para Angular, documentando ventajas, desventajas y casos de uso.

    **Librerias a comparar:**
    - **Angular Reactive Forms** (nativo).
    - **Formly** (formularios dinamicos por configuracion JSON).
    - @rxweb/reactive-form-validators (validadores extendidos).

    **Entregable:** Informe comparativo (~1500 palabras) con tabla de caracteristicas, ejemplos de codigo equivalentes en cada libreria, curva de aprendizaje, tamano del bundle y recomendacion final.

    ### Actividad de ampliacion 3: Implementar un editor de formularios visual (drag and drop)

    **Duracion:** 300 minutos.

    **Descripcion:** Construir un editor visual de formularios donde el usuario pueda arrastrar campos desde una paleta a un lienzo, configurar sus propiedades y generar el formulario resultante.

    **Requisitos:**
    - Paleta de campos disponibles: texto, numero, email, select, checkbox, radio, fecha, area de texto, encabezado, parrafo informativo, separador.
    - Lienzo donde se sueltan los campos (drag and drop con **Angular CDK Drag and Drop**).
    - Panel de propiedades que se muestra al seleccionar un campo en el lienzo: label, placeholder, requerido, validaciones, opciones (para select/radio).
    - Los campos en el lienzo se pueden reordenar arrastrando y eliminar con un boton X.
    - Boton "Previsualizar" que renderiza el formulario como lo veria el usuario final.
    - Boton "Exportar JSON" que genera el esquema del formulario en formato compatible con el sistema de la Actividad de Ampliacion 1.

    **Entregable:** Editor visual de formularios completamente funcional.

---

!!! tip "Buenas practicas"

    1. **Usar FormBuilder para formularios complejos.** `FormBuilder` reduce significativamente el codigo repetitivo al crear FormControls y FormGroups, especialmente en formularios con multiples niveles de anidamiento.

    2. **Validar en `blur` por defecto para formularios con validacion asincrona.** La opcion `updateOn: 'blur'` ofrece el mejor equilibrio entre feedback inmediato y eficiencia, evitando peticiones excesivas al servidor.

    3. **No mostrar errores hasta que el campo haya sido tocado.** Mostrar errores en campos `untouched` es una mala practica de UX que abruma al usuario antes de que haya comenzado a interactuar. La formula `control.invalid && (control.touched || formSubmitted)` es la regla de oro.

    4. **Extraer los validadores personalizados a funciones reutilizables.** Un validador de DNI o IBAN debe ser una funcion exportable e independiente del componente, no un metodo privado, para facilitar su reutilizacion en multiples formularios.

    5. **Usar `computed` para derivar estado visual de formulario.** En lugar de comprobar `form.valid && form.dirty` repetidamente en el template, crear computed signals: `canSave = computed(() => this.form.valid && this.form.dirty)`.

    6. **Proporcionar mensajes de error utiles, no tecnicos.** El mensaje "Campo requerido" es mejor que "Error: required validator failed". Los mensajes deben guiar al usuario hacia la correccion, no simplemente anunciar que algo esta mal.

    7. **Implementar auto-guardado en formularios largos.** Para formularios que requieren mas de 2 minutos para completarse, el auto-guardado de borradores en localStorage es una funcionalidad que el usuario agradecera enormemente.

    8. **Hacer scroll al primer error en formularios largos tras el envio.** El usuario no deberia tener que buscar manualmente cual campo fallo la validacion. `scrollIntoView({ behavior: 'smooth' })` es la implementacion estandar.

    9. **Usar skeleton en lugar de spinner para carga inicial de formularios.** Un spinner giratorio no da informacion sobre la estructura del formulario; un skeleton que imita la disposicion de los campos reduce la ansiedad del usuario durante la carga.

    10. **Limpiar suscripciones y timers en `ngOnDestroy`.** Las suscripciones a `valueChanges`, `statusChanges` y los timers de auto-guardado deben cancelarse cuando el componente se destruye. Usar `takeUntilDestroyed()` o gestion manual con `Subscription.unsubscribe()`.

    11. **Testear validadores personalizados de forma aislada.** Un validador como `dniValidator()` debe tener tests unitarios independientes que verifiquen DNI validos, formatos incorrectos y letras erroneas, sin necesidad de montar un componente completo.

    12. **No abusar de la validacion asincrona.** La validacion asincrona introduce latencia y complejidad. Debe reservarse para casos donde sea estrictamente necesaria (unicidad en BD). Si una validacion se puede realizar en el frontend, debe hacerse en el frontend.

---

!!! warning "Errores frecuentes"

    1. **Mostrar errores en campos untouched.** Un formulario con todos los campos en rojo al cargar es uno de los errores de UX mas graves y comunes. Siempre proteger la visualizacion de errores con la comprobacion `touched || formSubmitted`.

    2. **Olvidar el estado `pending` en la UI.** Si un campo tiene validacion asincrona, su estado `pending` debe reflejarse visualmente (borde amarillo, spinner). Ignorarlo hace que el formulario parezca congelado mientras el validador espera respuesta del servidor.

    3. **No limpiar validadores asincronos obsoletos.** Si un usuario escribe "a", luego "ab", luego "abc" rapidamente, las tres peticiones asincronas se lanzaran. Sin `switchMap` o `debounceTime`, la respuesta de "a" podria llegar despues de la de "abc" y sobrescribir el estado correcto con un error obsoleto.

    4. **Usar `form.value` sin comprobar que es valido.** `form.value` contiene los valores de todos los controles incluso si el formulario es invalido. Siempre comprobar `form.valid` antes de procesar los datos.

    5. **Anidar FormArrays incorrectamente.** Al anadir controles a un FormArray, es facil olvidar que cada elemento debe ser un `FormControl` o `FormGroup`. Intentar anadir valores crudos directamente causa errores en tiempo de ejecucion.

    6. **No recalcular totals al eliminar lineas en FormArray.** Al usar `removeAt(index)` en un FormArray, los computed signals que dependen del array se actualizan automaticamente, pero cualquier logica imperativa que mantenga un estado separado debe actualizarse manualmente. Usar siempre `computed` para valores derivados.

    7. **Ignorar la accesibilidad en mensajes de error.** Los mensajes de error deben usar `role="alert"` para que los lectores de pantalla los anuncien inmediatamente. El input debe tener `aria-describedby` apuntando al ID del mensaje de error.

    8. **No deshabilitar el boton de envio durante el procesamiento.** Mientras se procesa un formulario (estado `submitting`), el boton de envio debe estar deshabilitado y mostrar un spinner para evitar dobles envios accidentales.

    9. **Escribir validadores cross-field que mutan los controles hijos directamente.** Un validador de FormGroup debe devolver un objeto de error, no modificar directamente los controles. Para anadir errores a controles especificos, usar `setErrors` en el control concreto.

    10. **Usar `setValue` en lugar de `patchValue` al restaurar borradores.** `setValue` requiere proporcionar valores para TODOS los controles del formulario, mientras que `patchValue` permite valores parciales. Para restaurar borradores, `patchValue` es casi siempre la opcion correcta.

---

!!! abstract "Resumen"

    Esta unidad ha abordado en profundidad los formularios y la interaccion de usuario en Angular, cubriendo:

    - El uso de **Reactive Forms** con un enfoque especifico en la interfaz de usuario: cada estado del control (touched, dirty, valid, pending) se traduce en feedback visual mediante clases de Tailwind condicionales, creando formularios que guian al usuario sin abrumarlo.

    - La implementacion de **validaciones completas**: validadores integrados, validadores personalizados para documentos espanoles (DNI, CIF, IBAN), validacion cross-field para confirmacion de contrasenas y rangos de fecha, y validacion asincrona contra APIs con gestion del estado `pending` en la interfaz.

    - La construccion de un **sistema profesional de mensajes de error** mediante el componente `FormErrorComponent`, que encapsula la logica de presentacion de errores y la mantiene consistente en toda la aplicacion.

    - Las **tecnicas avanzadas de UX en formularios**: wizards multi-paso con Signals, formularios dinamicos con FormArray y calculos reactivos, auto-guardado de borradores en localStorage, y proteccion contra perdida de datos con CanDeactivate.

    - El **feedback visual y las micro-interacciones**: animaciones de shake en error, check en validacion correcta, slide in para mensajes, skeleton para carga de formularios, y toasts de confirmacion.

---

## Recursos complementarios

### Documentacion oficial
- Angular — Reactive Forms: https://angular.dev/guide/forms/reactive-forms
- Angular — Form Validation: https://angular.dev/guide/forms/form-validation
- Angular — Signals: https://angular.dev/guide/signals
- RxJS — Operators: https://rxjs.dev/guide/operators
- Tailwind CSS — Transitions and Animation: https://tailwindcss.com/docs/transition-property

### Herramientas y librerias
- ngx-mask: libreria de mascaras de input para Angular.
- @ngneat/error-tailor: gestion avanzada de errores de validacion en Angular.
- Angular CDK — Stepper: componente accesible para wizards multi-paso.
- TanStack Query (antes React Query): alternativa para gestionar estado de servidor en Angular.

### Articulos y guias
- "Best Practices for Form Design" — NN/g (Nielsen Norman Group)
- "Angular Reactive Forms: The Complete Guide" — Angular University
- "Building Multi-Step Forms in Angular" — Tim Deschryver
- "Async Validation in Angular Forms" — Netanel Basal
- "Micro-interactions in Form UX" — Smashing Magazine

### Libros
- "Web Form Design: Filling in the Blanks" — Luke Wroblewski
- "Don't Make Me Think" — Steve Krug (capitulos sobre formularios)
- "Designing with Data" — Rochelle King y Elizabeth Churchill
