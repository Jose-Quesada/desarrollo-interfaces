import sys
import os
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule

sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.Workbook()
wb.remove(wb.active)  # Remove default sheet

# -------------------------------------------------------------
# Color Palette & Visual System Tokens
# -------------------------------------------------------------
NAVY_HEADER = "0F172A"       # Slate 900
NAVY_SUBHEADER = "1E293B"    # Slate 800
BLUE_ACCENT = "1D4ED8"       # Blue 700
BLUE_LIGHT = "DBEAFE"        # Blue 100
BLUE_BORDER = "93C5FD"       # Blue 300
TEAL_HEADER = "0F766E"       # Teal 700
TEAL_LIGHT = "CCFBF1"        # Teal 100
GREEN_HEADER = "15803D"      # Green 700
GREEN_LIGHT = "DCFCE7"       # Green 100
PURPLE_HEADER = "6B21A8"     # Purple 700
PURPLE_LIGHT = "F3E8FF"      # Purple 100
ORANGE_HEADER = "C2410C"     # Orange 700
ORANGE_LIGHT = "FFEDD5"      # Orange 100
ZEBRA_FILL = "F8FAFC"        # Slate 50
TOTAL_FILL = "FEF3C7"        # Amber 100
HIGHLIGHT_ROW = "FEF9C3"     # Yellow 100

FILL_NAVY = PatternFill(start_color=NAVY_HEADER, end_color=NAVY_HEADER, fill_type="solid")
FILL_SUBHEADER = PatternFill(start_color=NAVY_SUBHEADER, end_color=NAVY_SUBHEADER, fill_type="solid")
FILL_BLUE_HEADER = PatternFill(start_color=BLUE_ACCENT, end_color=BLUE_ACCENT, fill_type="solid")
FILL_BLUE_LIGHT = PatternFill(start_color=BLUE_LIGHT, end_color=BLUE_LIGHT, fill_type="solid")
FILL_TEAL_HEADER = PatternFill(start_color=TEAL_HEADER, end_color=TEAL_HEADER, fill_type="solid")
FILL_TEAL_LIGHT = PatternFill(start_color=TEAL_LIGHT, end_color=TEAL_LIGHT, fill_type="solid")
FILL_GREEN_HEADER = PatternFill(start_color=GREEN_HEADER, end_color=GREEN_HEADER, fill_type="solid")
FILL_GREEN_LIGHT = PatternFill(start_color=GREEN_LIGHT, end_color=GREEN_LIGHT, fill_type="solid")
FILL_PURPLE_HEADER = PatternFill(start_color=PURPLE_HEADER, end_color=PURPLE_HEADER, fill_type="solid")
FILL_PURPLE_LIGHT = PatternFill(start_color=PURPLE_LIGHT, end_color=PURPLE_LIGHT, fill_type="solid")
FILL_ORANGE_HEADER = PatternFill(start_color=ORANGE_HEADER, end_color=ORANGE_HEADER, fill_type="solid")
FILL_ORANGE_LIGHT = PatternFill(start_color=ORANGE_LIGHT, end_color=ORANGE_LIGHT, fill_type="solid")
FILL_ZEBRA = PatternFill(start_color=ZEBRA_FILL, end_color=ZEBRA_FILL, fill_type="solid")
FILL_TOTAL = PatternFill(start_color=TOTAL_FILL, end_color=TOTAL_FILL, fill_type="solid")
FILL_HIGHLIGHT = PatternFill(start_color=HIGHLIGHT_ROW, end_color=HIGHLIGHT_ROW, fill_type="solid")

FONT_TITLE = Font(name="Segoe UI", size=14, bold=True, color="FFFFFF")
FONT_SUBTITLE = Font(name="Segoe UI", size=10, italic=True, color="E2E8F0")
FONT_HEADER = Font(name="Segoe UI", size=9, bold=True, color="FFFFFF")
FONT_HEADER_DARK = Font(name="Segoe UI", size=9, bold=True, color="0F172A")
FONT_BODY = Font(name="Segoe UI", size=9)
FONT_BODY_BOLD = Font(name="Segoe UI", size=9, bold=True)
FONT_KPI_VAL = Font(name="Segoe UI", size=16, bold=True, color="0F172A")
FONT_KPI_LBL = Font(name="Segoe UI", size=8, bold=True, color="64748B")

BORDER_THIN = Side(border_style="thin", color="CBD5E1")
BORDER_MEDIUM = Side(border_style="medium", color="64748B")
BORDER_DOUBLE = Side(border_style="double", color="0F172A")

CELL_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_THIN)
TOTAL_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_DOUBLE)
HEADER_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_MEDIUM)

ALIGN_CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
ALIGN_LEFT = Alignment(horizontal="left", vertical="center")
ALIGN_RIGHT = Alignment(horizontal="right", vertical="center")

# 15 Sample Students
STUDENTS = [
    ("Álvarez Gómez", "Laura"),
    ("Benítez Romero", "Carlos"),
    ("Castillo Morales", "Elena"),
    ("Delgado Santos", "Alejandro"),
    ("Fernández Navarro", "Lucía"),
    ("García Serrano", "David"),
    ("Herrera Cruz", "Marta"),
    ("Jiménez Ortiz", "Pablo"),
    ("López Molina", "Sara"),
    ("Martín Vega", "Javier"),
    ("Navarro Gil", "Ana"),
    ("Pérez Rubio", "Álvaro"),
    ("Ramírez Soto", "Carmen"),
    ("Sánchez Vidal", "Daniel"),
    ("Torres Lozano", "Irene")
]

# 40 Official CEs for Desarrollo de Interfaces (2º DAM)
# Task indices: 0:T01, 1:T02, 2:T03, 3:T04, 4:T05, 5:T06(ExT1), 6:T07(GitT1),
#               7:T08, 8:T09, 9:T10, 10:T11, 11:T12, 12:T13(GesFlow), 13:T14(ExT2), 14:T15(GitT2)
CRITERIA_DATA = [
    # RA1 (22%) - 6 CEs (3.67% each)
    ("RA1", 0.22, "CE1.a", "Se han identificado los elementos que componen la interfaz gráfica.", "UD00, UD01", [0, 5, 12]),
    ("RA1", 0.22, "CE1.b", "Se han analizado los principios de usabilidad y diseño centrado en el usuario (UX).", "UD01", [0, 5]),
    ("RA1", 0.22, "CE1.c", "Se han elaborado bocetos, wireframes y prototipos interactivos en alta fidelidad (Figma).", "UD04", [0, 5, 8, 12]),
    ("RA1", 0.22, "CE1.d", "Se han aplicado guías de estilo, tipografías, colores, espaciados y sistemas de diseño.", "UD07, UD13", [0, 2, 6, 8, 12]),
    ("RA1", 0.22, "CE1.e", "Se han diseñado layouts modernos y adaptables (CSS Grid, Flexbox, Tailwind CSS v4).", "UD05, UD06, UD08", [2, 5, 12]),
    ("RA1", 0.22, "CE1.f", "Se ha verificado la correcta interacción y flujo de navegación entre pantallas.", "UD04, UD15", [0, 5, 6, 8, 12]),

    # RA2 (16%) - 5 CEs (3.20% each)
    ("RA2", 0.16, "CE2.a", "Se han identificado conceptos, arquitecturas y hardware de interfaces naturales (NUI).", "UD03", [1, 5]),
    ("RA2", 0.16, "CE2.b", "Se han integrado librerías y APIs de reconocimiento y síntesis de voz (Web Speech API).", "UD03", [1, 5, 12]),
    ("RA2", 0.16, "CE2.c", "Se han implementado controles basados en visión artificial y tracking de gestos/manos.", "UD03", [1]),
    ("RA2", 0.16, "CE2.d", "Se han explorado patrones de realidad aumentada y experiencias inmersivas (WebXR/Three.js).", "UD03", [1]),
    ("RA2", 0.16, "CE2.e", "Se han evaluado ventajas y barreras de accesibilidad de interfaces conversacionales y gestuales.", "UD03", [1, 5]),

    # RA3 (20%) - 6 CEs (3.33% each)
    ("RA3", 0.20, "CE3.a", "Se ha seleccionado el framework y entorno de desarrollo (Angular 19+ Standalone).", "UD09, UD10", [4, 5, 12]),
    ("RA3", 0.20, "CE3.b", "Se han diseñado componentes reutilizables aplicando atomic design.", "UD11, UD13", [4, 5, 6, 8, 12]),
    ("RA3", 0.20, "CE3.c", "Se ha gestionado el estado reactivo y comunicación de componentes (Signals, RxJS).", "UD10, UD11", [4, 5, 7, 12, 13]),
    ("RA3", 0.20, "CE3.d", "Se han integrado directivas, pipes personalizados e inyección de dependencias.", "UD10, UD11", [4, 7, 12]),
    ("RA3", 0.20, "CE3.e", "Se ha documentado e interactuado con la librería de componentes mediante Storybook.", "UD14", [8, 12]),
    ("RA3", 0.20, "CE3.f", "Se han creado formularios reactivos con validaciones asíncronas y accesibles.", "UD12", [7, 12, 13]),

    # RA4 (11%) - 5 CEs (2.20% each)
    ("RA4", 0.11, "CE4.a", "Se han analizado las pautas WCAG 2.2 en niveles A, AA y AAA.", "UD02", [3, 5]),
    ("RA4", 0.11, "CE4.b", "Se han verificado atributos semánticos WAI-ARIA (roles, states, live regions).", "UD02, UD12", [3, 7, 12]),
    ("RA4", 0.11, "CE4.c", "Se ha asegurado navegación por teclado, focos visibles y ratios de contraste.", "UD02, UD08", [3, 5, 7, 12]),
    ("RA4", 0.11, "CE4.d", "Se han ejecutado auditorías automáticas de accesibilidad (Axe Core, Lighthouse).", "UD02", [3, 12]),
    ("RA4", 0.11, "CE4.e", "Se han realizado pruebas de compatibilidad con lectores de pantalla (NVDA, VoiceOver).", "UD02, UD12", [3, 7]),

    # RA5 (4%) - 4 CEs (1.00% each)
    ("RA5", 0.04, "CE5.a", "Se han seleccionado herramientas y librerías de generación de documentos (jsPDF, SheetJS).", "UD16", [9, 12, 13]),
    ("RA5", 0.04, "CE5.b", "Se han diseñado plantillas de informes estructurados con tablas y paginación.", "UD16", [9, 12]),
    ("RA5", 0.04, "CE5.c", "Se han creado cuadros de mando interactivos con visualización de datos (Chart.js).", "UD17", [9, 12]),
    ("RA5", 0.04, "CE5.d", "Se han implementado filtros dinámicos y exportación en formatos estándar (PDF, Excel, CSV).", "UD17", [9, 12]),

    # RA6 (7%) - 4 CEs (1.75% each)
    ("RA6", 0.07, "CE6.a", "Se han identificado destinatarios y requisitos de la documentación técnica y de usuario.", "UD18", [8, 12, 14]),
    ("RA6", 0.07, "CE6.b", "Se han generado esquemas, diagramas de flujo y arquitectura de la interfaz.", "UD18", [8, 12]),
    ("RA6", 0.07, "CE6.c", "Se ha automatizado la generación de documentación de componentes (Compodoc, Storybook).", "UD14, UD18", [8, 12]),
    ("RA6", 0.07, "CE6.d", "Se han redactado guías de estilo, manuales interactivos y ayuda en línea (Zensical/Markdown).", "UD18", [8, 12, 14]),

    # RA7 (10%) - 5 CEs (2.00% each)
    ("RA7", 0.10, "CE7.a", "Se han identificado entornos de ejecución y plataformas de destino (Windows, macOS, Linux).", "UD20", [11, 12]),
    ("RA7", 0.10, "CE7.b", "Se ha integrado la aplicación Angular en un contenedor de escritorio con Electron.", "UD20", [11, 12, 13]),
    ("RA7", 0.10, "CE7.c", "Se ha configurado la comunicación IPC segura (Preload Scripts, Context Isolation).", "UD20", [11, 12, 13]),
    ("RA7", 0.10, "CE7.d", "Se han generado paquetes e instaladores multiplataforma (Forge, Builder, MSIX, AppImage).", "UD21", [11, 12]),
    ("RA7", 0.10, "CE7.e", "Se han configurado actualizaciones automáticas y firmas de ejecutables.", "UD21", [11, 14]),

    # RA8 (10%) - 5 CEs (2.00% each)
    ("RA8", 0.10, "CE8.a", "Se ha planificado la estrategia de pruebas de la interfaz de usuario.", "UD19", [10, 12, 14]),
    ("RA8", 0.10, "CE8.b", "Se han implementado pruebas unitarias de componentes y servicios (Vitest).", "UD19", [10, 12, 13]),
    ("RA8", 0.10, "CE8.c", "Se han realizado pruebas de integración y simulación de eventos (Testing Library).", "UD19", [10, 12]),
    ("RA8", 0.10, "CE8.d", "Se han automatizado pruebas End-to-End (E2E) de flujos críticos (Playwright).", "UD19", [10, 12, 13]),
    ("RA8", 0.10, "CE8.e", "Se han medido métricas de rendimiento, tiempos de renderizado y Core Web Vitals.", "UD19", [10, 12])
]

# Task metadata: (TaskCode, ShortTitle, FullName, UDs, Trimestre)
TASKS_INFO = [
    # Trimestre 1 (Cols H to N in Matriz, Cols D to J in Registro)
    ("T01", "Figma & UX", "Act. 1: Prototipado Figma y Diseño UX", "UD01, UD04", "T1"),
    ("T02", "NUI & Voz", "Act. 2: Interfaces NUI y Web Speech API", "UD03", "T1"),
    ("T03", "Tailwind & Grid", "Act. 3: Layouts CSS Grid y Tailwind CSS v4", "UD05-07", "T1"),
    ("T04", "Accesibilidad", "Act. 4: Accesibilidad Universal WCAG y Responsive", "UD02, UD08", "T1"),
    ("T05", "Angular Signals", "Act. 5: Componentes Angular Standalone y Signals", "UD09-11", "T1"),
    ("T06", "Examen Práctico T1", "Examen Práctico 1er Trimestre (Desarrollo UI)", "UD01-11", "T1"),
    ("T07", "Git & Actitud T1", "Control de Versiones Git, Buenas Prácticas y DUA T1", "Transversal", "T1"),

    # Trimestre 2 (Cols O to V in Matriz, Cols K to R in Registro)
    ("T08", "Forms & A11y", "Act. 6: Formularios Reactivos y Accesibilidad", "UD12", "T2"),
    ("T09", "Storybook & Design", "Act. 7: Storybook, Design Systems y Tokens", "UD13-15", "T2"),
    ("T10", "Informes & Dashboards", "Act. 8: Informes PDF (jsPDF) y Dashboards Chart.js", "UD16-17", "T2"),
    ("T11", "Pruebas Vitest", "Act. 9: Pruebas Unitarias y E2E (Vitest / Playwright)", "UD19", "T2"),
    ("T12", "Electron Desktop", "Act. 10: Escritorio Electron y Comunicación IPC", "UD20-21", "T2"),
    ("T13", "Proyecto GesFlow", "Proyecto Final Integrador: Sistema GesFlow Desktop", "UD22", "T2"),
    ("T14", "Examen Práctico T2", "Examen Práctico 2º Trimestre (Prueba Global)", "UD12-21", "T2"),
    ("T15", "Git & Despliegue T2", "Calidad de Código, Git Flow y Despliegue T2", "Transversal", "T2")
]

# Realistic grades for the 15 students across the 15 tasks
STUDENT_TASK_GRADES = [
    [8.5, 9.0, 8.0, 8.5, 9.0, 8.5, 9.0,   8.5, 9.0, 8.5, 9.0, 8.5, 9.0, 8.5, 9.5],
    [6.0, 5.5, 6.5, 7.0, 6.0, 6.0, 7.0,   6.5, 6.0, 7.0, 6.5, 6.0, 6.5, 6.0, 7.0],
    [9.5, 9.0, 10.0, 9.5, 10.0, 9.5, 10.0, 10.0, 9.5, 9.5, 10.0, 9.5, 10.0, 10.0, 10.0],
    [4.0, 5.0, 4.5, 5.5, 4.0, 4.5, 6.0,   5.0, 4.5, 5.0, 4.5, 5.0, 4.5, 4.0, 5.0],
    [7.5, 8.0, 7.0, 7.5, 8.0, 7.5, 8.5,   7.5, 8.0, 8.0, 7.5, 8.0, 7.5, 8.0, 8.5],
    [8.0, 7.5, 8.5, 8.0, 8.5, 8.0, 8.5,   8.0, 8.5, 8.0, 8.5, 8.0, 8.5, 8.0, 8.5],
    [9.0, 8.5, 9.5, 9.0, 9.0, 9.0, 9.5,   9.0, 9.5, 9.0, 9.5, 9.0, 9.5, 9.0, 9.5],
    [5.0, 6.0, 5.5, 5.0, 6.0, 5.5, 6.5,   5.5, 6.0, 5.5, 6.0, 5.5, 6.0, 5.5, 6.5],
    [10.0, 9.5, 9.5, 10.0, 9.5, 10.0, 10.0, 10.0, 9.5, 10.0, 10.0, 9.5, 10.0, 10.0, 10.0],
    [3.5, 4.0, 4.0, 4.5, 4.0, 3.5, 5.0,   4.0, 4.5, 4.0, 4.0, 4.5, 4.0, 4.0, 4.5],
    [8.0, 8.5, 8.0, 8.5, 8.0, 8.5, 9.0,   8.5, 8.0, 8.5, 8.5, 8.0, 8.5, 8.5, 9.0],
    [7.0, 6.5, 7.5, 7.0, 7.0, 7.0, 7.5,   7.5, 7.0, 7.5, 7.0, 7.5, 7.0, 7.5, 7.5],
    [6.5, 7.0, 6.0, 6.5, 7.0, 6.5, 7.0,   7.0, 6.5, 7.0, 6.5, 7.0, 6.5, 7.0, 7.0],
    [8.5, 9.0, 8.5, 9.0, 8.5, 9.0, 9.5,   9.0, 8.5, 9.0, 9.0, 8.5, 9.0, 9.0, 9.5],
    [9.0, 9.5, 9.0, 9.5, 9.0, 9.5, 9.5,   9.5, 9.0, 9.5, 10.0, 9.5, 9.5, 9.5, 10.0]
]


# =============================================================
# SHEET 1: MATRIZ DE CRITERIOS (SELECTOR AVANZADO DE TAREAS)
# =============================================================
ws_mat = wb.create_sheet(title="Matriz Criterios")
ws_mat.views.sheetView[0].showGridLines = True

# Title
ws_mat.merge_cells("A1:W1")
ws_mat["A1"] = "MATRIZ DE SELECCIÓN DE CRITERIOS DE EVALUACIÓN POR TAREA — DESARROLLO DE INTERFACES (2º DAM)"
ws_mat["A1"].font = FONT_TITLE
ws_mat["A1"].fill = FILL_NAVY
ws_mat["A1"].alignment = ALIGN_CENTER
ws_mat.row_dimensions[1].height = 36

ws_mat.merge_cells("A2:W2")
ws_mat["A2"] = "Marca con una 'X' en la casilla correspondiente para activar los criterios evaluados en cada tarea. Los porcentajes de las líneas 47 y 48 se calculan automáticamente."
ws_mat["A2"].font = FONT_SUBTITLE
ws_mat["A2"].fill = FILL_SUBHEADER
ws_mat["A2"].alignment = ALIGN_CENTER
ws_mat.row_dimensions[2].height = 20

# Header groups (Row 4)
ws_mat.merge_cells("A4:G4")
ws_mat["A4"] = "CRITERIOS OFICIALES DE EVALUACIÓN (DECRETO 104/2024 & RD 405/2023)"
ws_mat["A4"].font = FONT_HEADER
ws_mat["A4"].alignment = ALIGN_CENTER
ws_mat["A4"].fill = FILL_NAVY

ws_mat.merge_cells("H4:N4")
ws_mat["H4"] = "1er TRIMESTRE (T1) — TAREAS Y PRUEBAS"
ws_mat["H4"].font = FONT_HEADER
ws_mat["H4"].alignment = ALIGN_CENTER
ws_mat["H4"].fill = FILL_BLUE_HEADER

ws_mat.merge_cells("O4:V4")
ws_mat["O4"] = "2º TRIMESTRE (T2) — TAREAS, PRUEBAS Y PROYECTO"
ws_mat["O4"].font = FONT_HEADER
ws_mat["O4"].alignment = ALIGN_CENTER
ws_mat["O4"].fill = FILL_TEAL_HEADER

ws_mat.merge_cells("W4:W5")
ws_mat["W4"] = "Pond. CE\nGlobal"
ws_mat["W4"].font = FONT_HEADER
ws_mat["W4"].alignment = ALIGN_CENTER
ws_mat["W4"].fill = FILL_PURPLE_HEADER

# Column subheaders (Row 5)
col_defs_mat = [
    ("RA", 8),
    ("Peso RA", 9),
    ("Código CE", 10),
    ("Descripción Oficial del Criterio de Evaluación", 44),
    ("UDs", 14),
    ("Total\nTareas", 8),
    ("Estado Cobertura", 14)
]

for col_idx, (name, width) in enumerate(col_defs_mat, start=1):
    col_let = get_column_letter(col_idx)
    ws_mat.column_dimensions[col_let].width = width
    cell = ws_mat.cell(row=5, column=col_idx, value=name)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.fill = FILL_SUBHEADER
    cell.border = HEADER_BORDER

# Task headers (Cols H to V, idx 8 to 22)
for t_idx, t_info in enumerate(TASKS_INFO, start=8):
    col_let = get_column_letter(t_idx)
    ws_mat.column_dimensions[col_let].width = 12
    cell = ws_mat.cell(row=5, column=t_idx, value=f"{t_info[0]}\n{t_info[1]}")
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.fill = FILL_BLUE_HEADER if t_idx <= 14 else FILL_TEAL_HEADER
    cell.border = HEADER_BORDER

ws_mat.column_dimensions["W"].width = 12
ws_mat.row_dimensions[5].height = 36

# Fill 40 Criterios (Rows 6 to 45)
for c_idx, crit in enumerate(CRITERIA_DATA, start=6):
    ws_mat.row_dimensions[c_idx].height = 24
    ra_code, ra_weight, ce_code, ce_desc, uds, tasks_x = crit
    is_zebra = (c_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Col A: RA
    cA = ws_mat.cell(row=c_idx, column=1, value=ra_code)
    cA.font = FONT_BODY_BOLD
    cA.alignment = ALIGN_CENTER
    cA.fill = row_fill
    cA.border = CELL_BORDER
    
    # Col B: Peso RA
    cB = ws_mat.cell(row=c_idx, column=2, value=ra_weight)
    cB.font = FONT_BODY
    cB.alignment = ALIGN_CENTER
    cB.fill = row_fill
    cB.border = CELL_BORDER
    cB.number_format = "0.0%"
    
    # Col C: Codigo CE
    cC = ws_mat.cell(row=c_idx, column=3, value=ce_code)
    cC.font = FONT_BODY_BOLD
    cC.alignment = ALIGN_CENTER
    cC.fill = row_fill
    cC.border = CELL_BORDER
    
    # Col D: Descripcion
    cD = ws_mat.cell(row=c_idx, column=4, value=ce_desc)
    cD.font = FONT_BODY
    cD.alignment = ALIGN_LEFT
    cD.fill = row_fill
    cD.border = CELL_BORDER
    
    # Col E: UDs
    cE = ws_mat.cell(row=c_idx, column=5, value=uds)
    cE.font = FONT_BODY
    cE.alignment = ALIGN_CENTER
    cE.fill = row_fill
    cE.border = CELL_BORDER
    
    # Col F: Total Tareas que evaluan este criterio =COUNTIF(H{c_idx}:V{c_idx}, "X")
    cF = ws_mat.cell(row=c_idx, column=6)
    cF.value = f'=COUNTIF(H{c_idx}:V{c_idx}, "X")'
    cF.font = FONT_BODY_BOLD
    cF.alignment = ALIGN_CENTER
    cF.fill = FILL_TOTAL
    cF.border = CELL_BORDER
    
    # Col G: Estado Cobertura =IF(F{c_idx}>0, "EVALUADO", "SIN EVALUAR")
    cG = ws_mat.cell(row=c_idx, column=7)
    cG.value = f'=IF(F{c_idx}>0, "EVALUADO", "SIN EVALUAR")'
    cG.font = FONT_BODY_BOLD
    cG.alignment = ALIGN_CENTER
    cG.fill = row_fill
    cG.border = CELL_BORDER
    
    # Cols H to V: Tasks selection "X"
    for t_i in range(15):
        col_target = 8 + t_i
        cell_x = ws_mat.cell(row=c_idx, column=col_target)
        if t_i in tasks_x:
            cell_x.value = "X"
            cell_x.font = Font(name="Segoe UI", size=10, bold=True, color="1E3A8A")
            cell_x.fill = FILL_BLUE_LIGHT if col_target <= 14 else FILL_TEAL_LIGHT
        else:
            cell_x.value = ""
            cell_x.font = FONT_BODY
            cell_x.fill = row_fill
        cell_x.alignment = ALIGN_CENTER
        cell_x.border = CELL_BORDER
        
    # Col W: Ponderacion Global de este CE = B{c_idx} / COUNTIF(A$6:A$45, A{c_idx})
    cW = ws_mat.cell(row=c_idx, column=23)
    cW.value = f"=B{c_idx} / COUNTIF(A$6:A$45, A{c_idx})"
    cW.font = FONT_BODY
    cW.alignment = ALIGN_CENTER
    cW.fill = row_fill
    cW.border = CELL_BORDER
    cW.number_format = "0.00%"

# Row 46: Total criterios evaluados por tarea
row_crit_count = 46
ws_mat.row_dimensions[row_crit_count].height = 24
ws_mat.merge_cells(f"A{row_crit_count}:G{row_crit_count}")
ws_mat[f"A{row_crit_count}"] = "TOTAL CRITERIOS EVALUADOS POR ESTA TAREA"
ws_mat[f"A{row_crit_count}"].font = FONT_HEADER_DARK
ws_mat[f"A{row_crit_count}"].alignment = ALIGN_RIGHT
ws_mat[f"A{row_crit_count}"].fill = FILL_TOTAL
ws_mat[f"A{row_crit_count}"].border = TOTAL_BORDER

for t_i in range(15):
    col_t = 8 + t_i
    col_let = get_column_letter(col_t)
    c_tot = ws_mat.cell(row=row_crit_count, column=col_t)
    c_tot.value = f'=COUNTIF({col_let}$6:{col_let}$45, "X")'
    c_tot.font = FONT_BODY_BOLD
    c_tot.alignment = ALIGN_CENTER
    c_tot.fill = FILL_TOTAL
    c_tot.border = TOTAL_BORDER

c_tot_w = ws_mat.cell(row=row_crit_count, column=23, value="100.0%")
c_tot_w.font = FONT_BODY_BOLD
c_tot_w.alignment = ALIGN_CENTER
c_tot_w.fill = FILL_GREEN_LIGHT
c_tot_w.border = TOTAL_BORDER

# Row 47: SUMA DE PESOS DE CRITERIOS EVALUADOS EN LA TAREA (Dinámico según las 'X')
row_weight = 47
ws_mat.row_dimensions[row_weight].height = 26
ws_mat.merge_cells(f"A{row_weight}:G{row_weight}")
ws_mat[f"A{row_weight}"] = "SUMA DE CRITERIOS EVALUADOS EN ESTA TAREA (Suma Directa con 'X')"
ws_mat[f"A{row_weight}"].font = FONT_HEADER_DARK
ws_mat[f"A{row_weight}"].alignment = ALIGN_RIGHT
ws_mat[f"A{row_weight}"].fill = FILL_HIGHLIGHT
ws_mat[f"A{row_weight}"].border = TOTAL_BORDER

for t_i in range(15):
    col_t = 8 + t_i
    col_let = get_column_letter(col_t)
    c_w = ws_mat.cell(row=row_weight, column=col_t)
    # SUMIF: Sum the CE global weights from col W where that task has an "X"
    c_w.value = f'=SUMIF({col_let}$6:{col_let}$45, "X", $W$6:$W$45)'
    c_w.font = Font(name="Segoe UI", size=9, bold=True, color="1E3A8A")
    c_w.alignment = ALIGN_CENTER
    c_w.fill = FILL_HIGHLIGHT
    c_w.border = TOTAL_BORDER
    c_w.number_format = "0.00%"

c_w_sum = ws_mat.cell(row=row_weight, column=23)
c_w_sum.value = f"=SUM(H{row_weight}:V{row_weight})"
c_w_sum.font = FONT_BODY_BOLD
c_w_sum.alignment = ALIGN_CENTER
c_w_sum.fill = FILL_HIGHLIGHT
c_w_sum.border = TOTAL_BORDER
c_w_sum.number_format = "0.00%"

# Row 48: % PONDERACIÓN EN EL TRIMESTRE (Normalizado a 100% de T1 / T2)
row_norm = 48
ws_mat.row_dimensions[row_norm].height = 26
ws_mat.merge_cells(f"A{row_norm}:G{row_norm}")
ws_mat[f"A{row_norm}"] = "% PONDERACIÓN EN EL TRIMESTRE (Normalizado a 100% para boletín de notas)"
ws_mat[f"A{row_norm}"].font = FONT_HEADER_DARK
ws_mat[f"A{row_norm}"].alignment = ALIGN_RIGHT
ws_mat[f"A{row_norm}"].fill = FILL_GREEN_LIGHT
ws_mat[f"A{row_norm}"].border = TOTAL_BORDER

for t_i in range(15):
    col_t = 8 + t_i
    col_let = get_column_letter(col_t)
    c_norm = ws_mat.cell(row=row_norm, column=col_t)
    if t_i < 7:  # T1: T01 to T07 (Cols H to N)
        c_norm.value = f'=IF(SUM($H${row_weight}:$N${row_weight})=0, 0, {col_let}${row_weight} / SUM($H${row_weight}:$N${row_weight}))'
    else:        # T2: T08 to T15 (Cols O to V)
        c_norm.value = f'=IF(SUM($O${row_weight}:$V${row_weight})=0, 0, {col_let}${row_weight} / SUM($O${row_weight}:$V${row_weight}))'
    c_norm.font = Font(name="Segoe UI", size=9, bold=True, color="15803D")
    c_norm.alignment = ALIGN_CENTER
    c_norm.fill = FILL_GREEN_LIGHT
    c_norm.border = TOTAL_BORDER
    c_norm.number_format = "0.00%"

c_norm_sum = ws_mat.cell(row=row_norm, column=23)
c_norm_sum.value = "100% T1 / 100% T2"
c_norm_sum.font = Font(name="Segoe UI", size=8, bold=True, color="15803D")
c_norm_sum.alignment = ALIGN_CENTER
c_norm_sum.fill = FILL_GREEN_LIGHT
c_norm_sum.border = TOTAL_BORDER

# Conditional Formatting on Matrix
ws_mat.conditional_formatting.add("G6:G45", CellIsRule(operator="equal", formula=['"EVALUADO"'], stopIfTrue=True, fill=FILL_GREEN_LIGHT, font=Font(color="15803D", bold=True)))
ws_mat.conditional_formatting.add("G6:G45", CellIsRule(operator="equal", formula=['"SIN EVALUAR"'], stopIfTrue=True, fill=PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid"), font=Font(color="DC2626", bold=True)))
ws_mat.conditional_formatting.add("H6:V45", CellIsRule(operator="equal", formula=['"X"'], stopIfTrue=True, fill=FILL_BLUE_LIGHT, font=Font(color="1D4ED8", bold=True)))


# =============================================================
# SHEET 2: REGISTRO DE NOTAS (CALIFICADOR POR TAREAS)
# =============================================================
ws_reg = wb.create_sheet(title="Registro Notas")
ws_reg.views.sheetView[0].showGridLines = True

# Title
ws_reg.merge_cells("A1:T1")
ws_reg["A1"] = "REGISTRO DE CALIFICACIONES POR TAREA — DESARROLLO DE INTERFACES (2º DAM)"
ws_reg["A1"].font = FONT_TITLE
ws_reg["A1"].fill = FILL_NAVY
ws_reg["A1"].alignment = ALIGN_CENTER
ws_reg.row_dimensions[1].height = 36

ws_reg.merge_cells("A2:T2")
ws_reg["A2"] = "Introduce las notas obtenidas (0 a 10). Las cabeceras muestran el % dinámico calculado a partir de los criterios seleccionados en 'Matriz Criterios'."
ws_reg["A2"].font = FONT_SUBTITLE
ws_reg["A2"].fill = FILL_SUBHEADER
ws_reg["A2"].alignment = ALIGN_CENTER
ws_reg.row_dimensions[2].height = 20

# Subgroups headers (Row 4)
ws_reg.merge_cells("A4:C4")
ws_reg["A4"] = "DATOS DEL ALUMNADO"
ws_reg["A4"].font = FONT_HEADER
ws_reg["A4"].alignment = ALIGN_CENTER
ws_reg["A4"].fill = FILL_NAVY

ws_reg.merge_cells("D4:J4")
ws_reg["D4"] = "TAREAS 1er TRIMESTRE (T1) — PESOS DERIVADOS DE CRITERIOS"
ws_reg["D4"].font = FONT_HEADER
ws_reg["D4"].alignment = ALIGN_CENTER
ws_reg["D4"].fill = FILL_BLUE_HEADER

ws_reg.merge_cells("K4:R4")
ws_reg["K4"] = "TAREAS 2º TRIMESTRE (T2) — PESOS DERIVADOS DE CRITERIOS"
ws_reg["K4"].font = FONT_HEADER
ws_reg["K4"].alignment = ALIGN_CENTER
ws_reg["K4"].fill = FILL_TEAL_HEADER

ws_reg.merge_cells("S4:T4")
ws_reg["S4"] = "CALIFICACIONES TRIMESTRALES"
ws_reg["S4"].font = FONT_HEADER
ws_reg["S4"].alignment = ALIGN_CENTER
ws_reg["S4"].fill = FILL_PURPLE_HEADER

# Row 5: Column headers
reg_cols = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("Grupo", 8),
    # T01 to T07 (T1)
    ("T01\nFigma & UX", 12),
    ("T02\nNUI & Voz", 12),
    ("T03\nTailwind", 12),
    ("T04\nAccesib.", 12),
    ("T05\nAngular", 12),
    ("T06\nExamen T1", 12),
    ("T07\nGit T1", 11),
    # T08 to T15 (T2)
    ("T08\nForms A11y", 12),
    ("T09\nStorybook", 12),
    ("T10\nInformes", 12),
    ("T11\nVitest/E2E", 12),
    ("T12\nElectron", 12),
    ("T13\nGesFlow", 13),
    ("T14\nExamen T2", 12),
    ("T15\nGit T2", 11),
    # Trimester totals
    ("1º TRIMESTRE\n(100% Criterios)", 15),
    ("2º TRIMESTRE\n(100% Criterios)", 15)
]

ws_reg.row_dimensions[5].height = 36
for col_idx, (col_name, width) in enumerate(reg_cols, start=1):
    col_let = get_column_letter(col_idx)
    ws_reg.column_dimensions[col_let].width = width
    cell = ws_reg.cell(row=5, column=col_idx, value=col_name)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 3:
        cell.fill = FILL_NAVY
    elif col_idx <= 10:
        cell.fill = FILL_BLUE_HEADER
    elif col_idx <= 18:
        cell.fill = FILL_TEAL_HEADER
    else:
        cell.fill = FILL_PURPLE_HEADER

# Student rows (Rows 6 to 20)
for r_idx, (apell, nom) in enumerate(STUDENTS, start=6):
    ws_reg.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº
    c1 = ws_reg.cell(row=r_idx, column=1, value=r_idx-5)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    # Nombre
    c2 = ws_reg.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # Grupo
    c3 = ws_reg.cell(row=r_idx, column=3, value="2º DAM")
    c3.alignment = ALIGN_CENTER
    c3.border = CELL_BORDER
    c3.fill = row_fill
    c3.font = FONT_BODY
    
    # Grades for 15 tasks (Cols D to R, index 4 to 18)
    grades = STUDENT_TASK_GRADES[r_idx-6]
    for g_i, grade_val in enumerate(grades):
        c_task = ws_reg.cell(row=r_idx, column=4 + g_i, value=grade_val)
        c_task.alignment = ALIGN_CENTER
        c_task.border = CELL_BORDER
        c_task.fill = row_fill
        c_task.font = FONT_BODY
        c_task.number_format = "0.00"
        
    # Col S: NOTA 1º TRIMESTRE (T1) -> dynamically uses weights from 'Matriz Criterios'!H$48:N$48
    c_t1 = ws_reg.cell(row=r_idx, column=19)
    c_t1.value = f"=D{r_idx}*'Matriz Criterios'!H$48 + E{r_idx}*'Matriz Criterios'!I$48 + F{r_idx}*'Matriz Criterios'!J$48 + G{r_idx}*'Matriz Criterios'!K$48 + H{r_idx}*'Matriz Criterios'!L$48 + I{r_idx}*'Matriz Criterios'!M$48 + J{r_idx}*'Matriz Criterios'!N$48"
    c_t1.alignment = ALIGN_CENTER
    c_t1.border = CELL_BORDER
    c_t1.fill = FILL_BLUE_LIGHT
    c_t1.font = FONT_BODY_BOLD
    c_t1.number_format = "0.00"
    
    # Col T: NOTA 2º TRIMESTRE (T2) -> dynamically uses weights from 'Matriz Criterios'!O$48:V$48
    c_t2 = ws_reg.cell(row=r_idx, column=20)
    c_t2.value = f"=K{r_idx}*'Matriz Criterios'!O$48 + L{r_idx}*'Matriz Criterios'!P$48 + M{r_idx}*'Matriz Criterios'!Q$48 + N{r_idx}*'Matriz Criterios'!R$48 + O{r_idx}*'Matriz Criterios'!S$48 + P{r_idx}*'Matriz Criterios'!T$48 + Q{r_idx}*'Matriz Criterios'!U$48 + R{r_idx}*'Matriz Criterios'!V$48"
    c_t2.alignment = ALIGN_CENTER
    c_t2.border = CELL_BORDER
    c_t2.fill = FILL_TEAL_LIGHT
    c_t2.font = FONT_BODY_BOLD
    c_t2.number_format = "0.00"

# Average row for Tasks (Row 21)
row_reg_avg = 21
ws_reg.row_dimensions[row_reg_avg].height = 24
ws_reg.merge_cells(f"A{row_reg_avg}:C{row_reg_avg}")
c_avg_lbl = ws_reg.cell(row=row_reg_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl.font = FONT_HEADER_DARK
c_avg_lbl.alignment = ALIGN_CENTER
c_avg_lbl.fill = FILL_TOTAL
c_avg_lbl.border = TOTAL_BORDER
ws_reg.cell(row=row_reg_avg, column=2).border = TOTAL_BORDER
ws_reg.cell(row=row_reg_avg, column=3).border = TOTAL_BORDER

for col_idx in range(4, 21):
    col_let = get_column_letter(col_idx)
    c_avg = ws_reg.cell(row=row_reg_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}6:{col_let}20)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

# Conditional formatting on Trimester notes
green_fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
green_font = Font(color="15803D", bold=True)
red_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
red_font = Font(color="DC2626", bold=True)

ws_reg.conditional_formatting.add("S6:T20", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_reg.conditional_formatting.add("S6:T20", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 3: CÁLCULO POR CRITERIOS (CEs) — AUTOMATIZACIÓN TOTAL
# =============================================================
ws_ces = wb.create_sheet(title="Calculo CEs")
ws_ces.views.sheetView[0].showGridLines = True

# Title
ws_ces.merge_cells("A1:AR1")
ws_ces["A1"] = "CALIFICACIÓN DETALLADA POR CRITERIOS DE EVALUACIÓN (CE1.a a CE8.e) — DESARROLLO DE INTERFACES"
ws_ces["A1"].font = FONT_TITLE
ws_ces["A1"].fill = FILL_NAVY
ws_ces["A1"].alignment = ALIGN_CENTER
ws_ces.row_dimensions[1].height = 36

ws_ces.merge_cells("A2:AR2")
ws_ces["A2"] = "Cálculo matemático automático: cada criterio se calcula promediando exclusivamente las tareas donde tiene marcada una 'X' en la 'Matriz Criterios'."
ws_ces["A2"].font = FONT_SUBTITLE
ws_ces["A2"].fill = FILL_SUBHEADER
ws_ces["A2"].alignment = ALIGN_CENTER
ws_ces.row_dimensions[2].height = 20

# Header groups (Row 4)
ws_ces.merge_cells("A4:B4")
ws_ces["A4"] = "ALUMNADO"
ws_ces["A4"].font = FONT_HEADER
ws_ces["A4"].alignment = ALIGN_CENTER
ws_ces["A4"].fill = FILL_NAVY

ws_ces.merge_cells("C4:H4")
ws_ces["C4"] = "RA1 (22%) — Interfaces Gráficas, UX, Figma y Layouts"
ws_ces["C4"].font = FONT_HEADER
ws_ces["C4"].alignment = ALIGN_CENTER
ws_ces["C4"].fill = FILL_BLUE_HEADER

ws_ces.merge_cells("I4:M4")
ws_ces["I4"] = "RA2 (16%) — Interfaces Naturales (NUI, Voz, Gestos)"
ws_ces["I4"].font = FONT_HEADER
ws_ces["I4"].alignment = ALIGN_CENTER
ws_ces["I4"].fill = FILL_TEAL_HEADER

ws_ces.merge_cells("N4:S4")
ws_ces["N4"] = "RA3 (20%) — Componentes Angular Standalone y Forms"
ws_ces["N4"].font = FONT_HEADER
ws_ces["N4"].alignment = ALIGN_CENTER
ws_ces["N4"].fill = FILL_PURPLE_HEADER

ws_ces.merge_cells("T4:X4")
ws_ces["T4"] = "RA4 (11%) — Accesibilidad Universal y WCAG 2.2"
ws_ces["T4"].font = FONT_HEADER
ws_ces["T4"].alignment = ALIGN_CENTER
ws_ces["T4"].fill = FILL_GREEN_HEADER

ws_ces.merge_cells("Y4:AB4")
ws_ces["Y4"] = "RA5 (4%) — Informes y Cuadros Mando"
ws_ces["Y4"].font = FONT_HEADER
ws_ces["Y4"].alignment = ALIGN_CENTER
ws_ces["Y4"].fill = FILL_ORANGE_HEADER

ws_ces.merge_cells("AC4:AF4")
ws_ces["AC4"] = "RA6 (7%) — Documentación Técnica y Storybook"
ws_ces["AC4"].font = FONT_HEADER
ws_ces["AC4"].alignment = ALIGN_CENTER
ws_ces["AC4"].fill = FILL_SUBHEADER

ws_ces.merge_cells("AG4:AK4")
ws_ces["AG4"] = "RA7 (10%) — Escritorio Electron y Empaquetado"
ws_ces["AG4"].font = FONT_HEADER
ws_ces["AG4"].alignment = ALIGN_CENTER
ws_ces["AG4"].fill = FILL_BLUE_HEADER

ws_ces.merge_cells("AL4:AP4")
ws_ces["AL4"] = "RA8 (10%) — Pruebas Vitest y Playwright E2E"
ws_ces["AL4"].font = FONT_HEADER
ws_ces["AL4"].alignment = ALIGN_CENTER
ws_ces["AL4"].fill = FILL_TEAL_HEADER

ws_ces.merge_cells("AQ4:AR4")
ws_ces["AQ4"] = "RESUMEN DE CRITERIOS"
ws_ces["AQ4"].font = FONT_HEADER
ws_ces["AQ4"].alignment = ALIGN_CENTER
ws_ces["AQ4"].fill = FILL_NAVY

# Row 5: Column headers with CE codes
ws_ces.column_dimensions["A"].width = 5
ws_ces.cell(row=5, column=1, value="Nº").font = FONT_HEADER
ws_ces.cell(row=5, column=1).alignment = ALIGN_CENTER
ws_ces.cell(row=5, column=1).fill = FILL_NAVY
ws_ces.cell(row=5, column=1).border = HEADER_BORDER

ws_ces.column_dimensions["B"].width = 24
ws_ces.cell(row=5, column=2, value="Apellidos, Nombre").font = FONT_HEADER
ws_ces.cell(row=5, column=2).alignment = ALIGN_LEFT
ws_ces.cell(row=5, column=2).fill = FILL_NAVY
ws_ces.cell(row=5, column=2).border = HEADER_BORDER

ws_ces.row_dimensions[5].height = 30
for c_i, crit in enumerate(CRITERIA_DATA, start=3):
    col_let = get_column_letter(c_i)
    ws_ces.column_dimensions[col_let].width = 9
    cell = ws_ces.cell(row=5, column=c_i, value=crit[2])
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    ra_code = crit[0]
    if ra_code == "RA1":
        cell.fill = FILL_BLUE_HEADER
    elif ra_code == "RA2":
        cell.fill = FILL_TEAL_HEADER
    elif ra_code == "RA3":
        cell.fill = FILL_PURPLE_HEADER
    elif ra_code == "RA4":
        cell.fill = FILL_GREEN_HEADER
    elif ra_code == "RA5":
        cell.fill = FILL_ORANGE_HEADER
    elif ra_code == "RA6":
        cell.fill = FILL_SUBHEADER
    elif ra_code == "RA7":
        cell.fill = FILL_BLUE_HEADER
    else:
        cell.fill = FILL_TEAL_HEADER

ws_ces.column_dimensions["AQ"].width = 12
ws_ces.cell(row=5, column=43, value="Media CEs\nSuperados").font = FONT_HEADER
ws_ces.cell(row=5, column=43).alignment = ALIGN_CENTER
ws_ces.cell(row=5, column=43).fill = FILL_NAVY
ws_ces.cell(row=5, column=43).border = HEADER_BORDER

ws_ces.column_dimensions["AR"].width = 12
ws_ces.cell(row=5, column=44, value="Nº CEs >= 5\n(de 40)").font = FONT_HEADER
ws_ces.cell(row=5, column=44).alignment = ALIGN_CENTER
ws_ces.cell(row=5, column=44).fill = FILL_NAVY
ws_ces.cell(row=5, column=44).border = HEADER_BORDER

# Student rows (Rows 6 to 20 in Calculo CEs)
for r_idx, (apell, nom) in enumerate(STUDENTS, start=6):
    ws_ces.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº & Nombre
    c1 = ws_ces.cell(row=r_idx, column=1, value=r_idx-5)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_ces.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    for c_i in range(40):
        target_col = 3 + c_i
        mat_row = 6 + c_i
        cell_ce = ws_ces.cell(row=r_idx, column=target_col)
        
        # Dynamic formula averaging tasks where 'Matriz Criterios' has "X"
        formula = f'=IF(SUMPRODUCT((\'Matriz Criterios\'!$H${mat_row}:$V${mat_row}="X")*ISNUMBER(\'Registro Notas\'!$D{r_idx}:$R{r_idx}))=0, "-", SUMPRODUCT((\'Matriz Criterios\'!$H${mat_row}:$V${mat_row}="X")*ISNUMBER(\'Registro Notas\'!$D{r_idx}:$R{r_idx})*\'Registro Notas\'!$D{r_idx}:$R{r_idx})/SUMPRODUCT((\'Matriz Criterios\'!$H${mat_row}:$V${mat_row}="X")*ISNUMBER(\'Registro Notas\'!$D{r_idx}:$R{r_idx})))'
        cell_ce.value = formula
        cell_ce.alignment = ALIGN_CENTER
        cell_ce.border = CELL_BORDER
        cell_ce.fill = row_fill
        cell_ce.font = FONT_BODY
        cell_ce.number_format = "0.00"
        
    # Col AQ: Media CEs Superados
    cAQ = ws_ces.cell(row=r_idx, column=43)
    cAQ.value = f"=AVERAGE(C{r_idx}:AP{r_idx})"
    cAQ.alignment = ALIGN_CENTER
    cAQ.border = CELL_BORDER
    cAQ.fill = FILL_TOTAL
    cAQ.font = FONT_BODY_BOLD
    cAQ.number_format = "0.00"
    
    # Col AR: Nº CEs >= 5
    cAR = ws_ces.cell(row=r_idx, column=44)
    cAR.value = f'=COUNTIF(C{r_idx}:AP{r_idx}, ">=5")'
    cAR.alignment = ALIGN_CENTER
    cAR.border = CELL_BORDER
    cAR.fill = FILL_GREEN_LIGHT
    cAR.font = FONT_BODY_BOLD

# Group Average Row
row_ce_avg = 21
ws_ces.row_dimensions[row_ce_avg].height = 24
ws_ces.merge_cells(f"A{row_ce_avg}:B{row_ce_avg}")
c_avg_lbl_ce = ws_ces.cell(row=row_ce_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl_ce.font = FONT_HEADER_DARK
c_avg_lbl_ce.alignment = ALIGN_CENTER
c_avg_lbl_ce.fill = FILL_TOTAL
c_avg_lbl_ce.border = TOTAL_BORDER
ws_ces.cell(row=row_ce_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 45):
    col_let = get_column_letter(col_idx)
    c_avg = ws_ces.cell(row=row_ce_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}6:{col_let}20)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_ces.conditional_formatting.add("C6:AP20", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_ces.conditional_formatting.add("C6:AP20", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 4: CÁLCULO POR RESULTADOS DE APRENDIZAJE (RAs)
# =============================================================
ws_ras = wb.create_sheet(title="Calculo RAs")
ws_ras.views.sheetView[0].showGridLines = True

ws_ras.merge_cells("A1:K1")
ws_ras["A1"] = "CALIFICACIÓN POR RESULTADOS DE APRENDIZAJE (RA1 a RA8) — PONDERACIÓN OFICIAL"
ws_ras["A1"].font = FONT_TITLE
ws_ras["A1"].fill = FILL_NAVY
ws_ras["A1"].alignment = ALIGN_CENTER
ws_ras.row_dimensions[1].height = 36

ws_ras.merge_cells("A2:K2")
ws_ras["A2"] = "Cada Resultado de Aprendizaje se obtiene promediando sus Criterios de Evaluación evaluados. La Nota Final aplica los pesos oficiales del título en Andalucía."
ws_ras["A2"].font = FONT_SUBTITLE
ws_ras["A2"].fill = FILL_SUBHEADER
ws_ras["A2"].alignment = ALIGN_CENTER
ws_ras.row_dimensions[2].height = 20

headers_ras = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("RA1 (22%)\nInterfaces Gráficas\nUX & Layouts", 16),
    ("RA2 (16%)\nInterfaces NUI\nVoz & Gestos", 16),
    ("RA3 (20%)\nComponentes\nAngular Standalone", 16),
    ("RA4 (11%)\nAccesibilidad\nUniversal WCAG", 16),
    ("RA5 (4%)\nInformes PDF\ny Dashboards", 15),
    ("RA6 (7%)\nDocumentación\ny Storybook", 15),
    ("RA7 (10%)\nEscritorio Electron\ny Empaquetado", 16),
    ("RA8 (10%)\nPruebas Vitest\ny Playwright E2E", 16),
    ("CALIFICACIÓN FINAL\nORDINARIA (100%)", 18)
]

ws_ras.row_dimensions[4].height = 42
for col_idx, (h_text, width) in enumerate(headers_ras, start=1):
    col_let = get_column_letter(col_idx)
    ws_ras.column_dimensions[col_let].width = width
    cell = ws_ras.cell(row=4, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 2:
        cell.fill = FILL_NAVY
    elif col_idx <= 10:
        cell.fill = FILL_BLUE_HEADER
    else:
        cell.fill = FILL_GREEN_HEADER

# Fill Student Rows for RAs
for r_idx, (apell, nom) in enumerate(STUDENTS, start=6):
    ws_ras.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº & Nombre
    c1 = ws_ras.cell(row=r_idx, column=1, value=r_idx-5)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_ras.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # RA1 (22%): CE1.a to CE1.f -> 'Calculo CEs'!C{r_idx}:H{r_idx}
    c_ra1 = ws_ras.cell(row=r_idx, column=3)
    c_ra1.value = f"=AVERAGE('Calculo CEs'!C{r_idx}:H{r_idx})"
    c_ra1.alignment = ALIGN_CENTER
    c_ra1.border = CELL_BORDER
    c_ra1.fill = row_fill
    c_ra1.font = FONT_BODY
    c_ra1.number_format = "0.00"
    
    # RA2 (16%): CE2.a to CE2.e -> 'Calculo CEs'!I{r_idx}:M{r_idx}
    c_ra2 = ws_ras.cell(row=r_idx, column=4)
    c_ra2.value = f"=AVERAGE('Calculo CEs'!I{r_idx}:M{r_idx})"
    c_ra2.alignment = ALIGN_CENTER
    c_ra2.border = CELL_BORDER
    c_ra2.fill = row_fill
    c_ra2.font = FONT_BODY
    c_ra2.number_format = "0.00"
    
    # RA3 (20%): CE3.a to CE3.f -> 'Calculo CEs'!N{r_idx}:S{r_idx}
    c_ra3 = ws_ras.cell(row=r_idx, column=5)
    c_ra3.value = f"=AVERAGE('Calculo CEs'!N{r_idx}:S{r_idx})"
    c_ra3.alignment = ALIGN_CENTER
    c_ra3.border = CELL_BORDER
    c_ra3.fill = row_fill
    c_ra3.font = FONT_BODY
    c_ra3.number_format = "0.00"
    
    # RA4 (11%): CE4.a to CE4.e -> 'Calculo CEs'!T{r_idx}:X{r_idx}
    c_ra4 = ws_ras.cell(row=r_idx, column=6)
    c_ra4.value = f"=AVERAGE('Calculo CEs'!T{r_idx}:X{r_idx})"
    c_ra4.alignment = ALIGN_CENTER
    c_ra4.border = CELL_BORDER
    c_ra4.fill = row_fill
    c_ra4.font = FONT_BODY
    c_ra4.number_format = "0.00"
    
    # RA5 (4%): CE5.a to CE5.d -> 'Calculo CEs'!Y{r_idx}:AB{r_idx}
    c_ra5 = ws_ras.cell(row=r_idx, column=7)
    c_ra5.value = f"=AVERAGE('Calculo CEs'!Y{r_idx}:AB{r_idx})"
    c_ra5.alignment = ALIGN_CENTER
    c_ra5.border = CELL_BORDER
    c_ra5.fill = row_fill
    c_ra5.font = FONT_BODY
    c_ra5.number_format = "0.00"
    
    # RA6 (7%): CE6.a to CE6.d -> 'Calculo CEs'!AC{r_idx}:AF{r_idx}
    c_ra6 = ws_ras.cell(row=r_idx, column=8)
    c_ra6.value = f"=AVERAGE('Calculo CEs'!AC{r_idx}:AF{r_idx})"
    c_ra6.alignment = ALIGN_CENTER
    c_ra6.border = CELL_BORDER
    c_ra6.fill = row_fill
    c_ra6.font = FONT_BODY
    c_ra6.number_format = "0.00"
    
    # RA7 (10%): CE7.a to CE7.e -> 'Calculo CEs'!AG{r_idx}:AK{r_idx}
    c_ra7 = ws_ras.cell(row=r_idx, column=9)
    c_ra7.value = f"=AVERAGE('Calculo CEs'!AG{r_idx}:AK{r_idx})"
    c_ra7.alignment = ALIGN_CENTER
    c_ra7.border = CELL_BORDER
    c_ra7.fill = row_fill
    c_ra7.font = FONT_BODY
    c_ra7.number_format = "0.00"
    
    # RA8 (10%): CE8.a to CE8.e -> 'Calculo CEs'!AL{r_idx}:AP{r_idx}
    c_ra8 = ws_ras.cell(row=r_idx, column=10)
    c_ra8.value = f"=AVERAGE('Calculo CEs'!AL{r_idx}:AP{r_idx})"
    c_ra8.alignment = ALIGN_CENTER
    c_ra8.border = CELL_BORDER
    c_ra8.fill = row_fill
    c_ra8.font = FONT_BODY
    c_ra8.number_format = "0.00"
    
    # Calificacion Final Ordinaria Oficial
    c_tot = ws_ras.cell(row=r_idx, column=11)
    c_tot.value = f"=C{r_idx}*0.22 + D{r_idx}*0.16 + E{r_idx}*0.20 + F{r_idx}*0.11 + G{r_idx}*0.04 + H{r_idx}*0.07 + I{r_idx}*0.10 + J{r_idx}*0.10"
    c_tot.alignment = ALIGN_CENTER
    c_tot.border = CELL_BORDER
    c_tot.fill = FILL_TOTAL
    c_tot.font = Font(name="Segoe UI", size=10, bold=True, color="0F172A")
    c_tot.number_format = "0.00"

# Average Row
row_ras_avg = 21
ws_ras.row_dimensions[row_ras_avg].height = 24
ws_ras.merge_cells(f"A{row_ras_avg}:B{row_ras_avg}")
c_avg_lbl_ras = ws_ras.cell(row=row_ras_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl_ras.font = FONT_HEADER_DARK
c_avg_lbl_ras.alignment = ALIGN_CENTER
c_avg_lbl_ras.fill = FILL_TOTAL
c_avg_lbl_ras.border = TOTAL_BORDER
ws_ras.cell(row=row_ras_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 12):
    col_let = get_column_letter(col_idx)
    c_avg = ws_ras.cell(row=row_ras_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}6:{col_let}20)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_ras.conditional_formatting.add("K6:K20", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_ras.conditional_formatting.add("K6:K20", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 5: PANEL DE CONTROL Y RESUMEN EJECUTIVO
# =============================================================
ws_dash = wb.create_sheet(title="Panel de Control")
ws_dash.views.sheetView[0].showGridLines = True

# Title Header
ws_dash.merge_cells("A1:P1")
ws_dash["A1"] = "PANEL DE CONTROL GENERAL — DESARROLLO DE INTERFACES (2º DAM)"
ws_dash["A1"].font = FONT_TITLE
ws_dash["A1"].fill = FILL_NAVY
ws_dash["A1"].alignment = ALIGN_CENTER
ws_dash.row_dimensions[1].height = 36

ws_dash.merge_cells("A2:P2")
ws_dash["A2"] = "Síntesis Integral: Trimestres, Resultados de Aprendizaje Oficiales, Calificación Ordinaria y Acceso a Formación en Empresa (Dual)"
ws_dash["A2"].font = FONT_SUBTITLE
ws_dash["A2"].fill = FILL_SUBHEADER
ws_dash["A2"].alignment = ALIGN_CENTER
ws_dash.row_dimensions[2].height = 20

# Top KPI Cards (Rows 4 to 6)
ws_dash.merge_cells("B4:C4")
ws_dash["B4"] = "ALUMNADO MATRICULADO"
ws_dash["B4"].font = FONT_KPI_LBL
ws_dash["B4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("B5:C6")
ws_dash["B5"] = '=COUNTA(A9:A23)'
ws_dash["B5"].font = FONT_KPI_VAL
ws_dash["B5"].alignment = ALIGN_CENTER
ws_dash["B5"].fill = FILL_BLUE_LIGHT

ws_dash.merge_cells("E4:F4")
ws_dash["E4"] = "APROBADOS EVAL. ORDINARIA"
ws_dash["E4"].font = FONT_KPI_LBL
ws_dash["E4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("E5:F6")
ws_dash["E5"] = '=COUNTIF(N9:N23, ">=5")'
ws_dash["E5"].font = Font(name="Segoe UI", size=16, bold=True, color="15803D")
ws_dash["E5"].alignment = ALIGN_CENTER
ws_dash["E5"].fill = FILL_GREEN_LIGHT

ws_dash.merge_cells("H4:I4")
ws_dash["H4"] = "SUSPENSOS EVAL. ORDINARIA"
ws_dash["H4"].font = FONT_KPI_LBL
ws_dash["H4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("H5:I6")
ws_dash["H5"] = '=COUNTIF(N9:N23, "<5")'
ws_dash["H5"].font = Font(name="Segoe UI", size=16, bold=True, color="DC2626")
ws_dash["H5"].alignment = ALIGN_CENTER
ws_dash["H5"].fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")

ws_dash.merge_cells("K4:L4")
ws_dash["K4"] = "NOTA MEDIA DEL GRUPO"
ws_dash["K4"].font = FONT_KPI_LBL
ws_dash["K4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("K5:L6")
ws_dash["K5"] = '=AVERAGE(N9:N23)'
ws_dash["K5"].font = FONT_KPI_VAL
ws_dash["K5"].alignment = ALIGN_CENTER
ws_dash["K5"].fill = FILL_TOTAL
ws_dash["K5"].number_format = "0.00"

ws_dash.merge_cells("N4:O4")
ws_dash["N4"] = "TASA DE ÉXITO ACADÉMICO"
ws_dash["N4"].font = FONT_KPI_LBL
ws_dash["N4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("N5:O6")
ws_dash["N5"] = '=E5/B5'
ws_dash["N5"].font = Font(name="Segoe UI", size=16, bold=True, color="1E3A8A")
ws_dash["N5"].alignment = ALIGN_CENTER
ws_dash["N5"].fill = FILL_PURPLE_LIGHT
ws_dash["N5"].number_format = "0.0%"

# Table Headers (Row 8)
headers_dash = [
    ("Nº", 5),
    ("Apellidos, Nombre", 24),
    ("1º Trim\n(T1)", 10),
    ("2º Trim\n(T2)", 10),
    ("RA1\n(22%)", 8),
    ("RA2\n(16%)", 8),
    ("RA3\n(20%)", 8),
    ("RA4\n(11%)", 8),
    ("RA5\n(4%)", 8),
    ("RA6\n(7%)", 8),
    ("RA7\n(10%)", 8),
    ("RA8\n(10%)", 8),
    ("Media\nT1-T2", 9),
    ("Nota Final\nOrdinaria (Marzo)", 16),
    ("Calificación Cualitativa", 18),
    ("Acceso a Dual en Empresa", 22)
]

ws_dash.row_dimensions[8].height = 40
for col_idx, (h_text, width) in enumerate(headers_dash, start=1):
    col_let = get_column_letter(col_idx)
    ws_dash.column_dimensions[col_let].width = width
    cell = ws_dash.cell(row=8, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 2:
        cell.fill = FILL_NAVY
    elif col_idx <= 4:
        cell.fill = FILL_TEAL_HEADER
    elif col_idx <= 12:
        cell.fill = FILL_BLUE_HEADER
    elif col_idx <= 14:
        cell.fill = FILL_GREEN_HEADER
    else:
        cell.fill = FILL_PURPLE_HEADER

# Student rows (Rows 9 to 23 in Panel de Control)
for r_idx, (apell, nom) in enumerate(STUDENTS, start=9):
    ws_dash.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    src_row = r_idx - 3  # Maps row 9 to row 6 in other sheets
    
    # Nº & Nombre
    c1 = ws_dash.cell(row=r_idx, column=1, value=r_idx-8)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_dash.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # 1º Trimestre (from 'Registro Notas'!S{src_row})
    c3 = ws_dash.cell(row=r_idx, column=3)
    c3.value = f"='Registro Notas'!S{src_row}"
    c3.alignment = ALIGN_CENTER
    c3.border = CELL_BORDER
    c3.fill = FILL_BLUE_LIGHT if is_zebra else PatternFill(start_color="EFF6FF", end_color="EFF6FF", fill_type="solid")
    c3.font = FONT_BODY_BOLD
    c3.number_format = "0.00"
    
    # 2º Trimestre (from 'Registro Notas'!T{src_row})
    c4 = ws_dash.cell(row=r_idx, column=4)
    c4.value = f"='Registro Notas'!T{src_row}"
    c4.alignment = ALIGN_CENTER
    c4.border = CELL_BORDER
    c4.fill = FILL_TEAL_LIGHT if is_zebra else PatternFill(start_color="F0FDFA", end_color="F0FDFA", fill_type="solid")
    c4.font = FONT_BODY_BOLD
    c4.number_format = "0.00"
    
    # RA1 to RA8 (from 'Calculo RAs'!C{src_row}:J{src_row})
    for ra_i in range(8):
        c_target = 5 + ra_i
        ra_col_let = get_column_letter(3 + ra_i)
        c_ra = ws_dash.cell(row=r_idx, column=c_target)
        c_ra.value = f"='Calculo RAs'!{ra_col_let}{src_row}"
        c_ra.alignment = ALIGN_CENTER
        c_ra.border = CELL_BORDER
        c_ra.fill = row_fill
        c_ra.font = FONT_BODY
        c_ra.number_format = "0.00"
        
    # Media T1-T2 (Col M, 13)
    c_med = ws_dash.cell(row=r_idx, column=13)
    c_med.value = f"=AVERAGE(C{r_idx}, D{r_idx})"
    c_med.alignment = ALIGN_CENTER
    c_med.border = CELL_BORDER
    c_med.fill = row_fill
    c_med.font = FONT_BODY
    c_med.number_format = "0.00"
    
    # Nota Final Ordinaria (from 'Calculo RAs'!K{src_row})
    c_fin = ws_dash.cell(row=r_idx, column=14)
    c_fin.value = f"='Calculo RAs'!K{src_row}"
    c_fin.alignment = ALIGN_CENTER
    c_fin.border = CELL_BORDER
    c_fin.fill = FILL_TOTAL
    c_fin.font = Font(name="Segoe UI", size=10, bold=True, color="0F172A")
    c_fin.number_format = "0.00"
    
    # Calificacion Cualitativa (Col O, 15)
    c_cual = ws_dash.cell(row=r_idx, column=15)
    c_cual.value = f'=IF(N{r_idx}>=9, "SOBRESALIENTE", IF(N{r_idx}>=7, "NOTABLE", IF(N{r_idx}>=6, "BIEN", IF(N{r_idx}>=5, "SUFICIENTE", "INSUFICIENTE"))))'
    c_cual.alignment = ALIGN_CENTER
    c_cual.border = CELL_BORDER
    c_cual.fill = row_fill
    c_cual.font = FONT_BODY_BOLD
    
    # Acceso a Dual (Col P, 16)
    c_dual = ws_dash.cell(row=r_idx, column=16)
    c_dual.value = f'=IF(N{r_idx}>=5, "AUTORIZADO (DUAL)", "PENDIENTE RECUP.")'
    c_dual.alignment = ALIGN_CENTER
    c_dual.border = CELL_BORDER
    c_dual.fill = row_fill
    c_dual.font = FONT_BODY_BOLD

# Group Average Row
row_dash_avg = 24
ws_dash.row_dimensions[row_dash_avg].height = 24
ws_dash.merge_cells(f"A{row_dash_avg}:B{row_dash_avg}")
c_avg_lbl_d = ws_dash.cell(row=row_dash_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl_d.font = FONT_HEADER_DARK
c_avg_lbl_d.alignment = ALIGN_CENTER
c_avg_lbl_d.fill = FILL_TOTAL
c_avg_lbl_d.border = TOTAL_BORDER
ws_dash.cell(row=row_dash_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 15):
    col_let = get_column_letter(col_idx)
    c_avg = ws_dash.cell(row=row_dash_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}9:{col_let}23)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_dash.cell(row=row_dash_avg, column=15, value="").fill = FILL_TOTAL
ws_dash.cell(row=row_dash_avg, column=15).border = TOTAL_BORDER
ws_dash.cell(row=row_dash_avg, column=16, value="").fill = FILL_TOTAL
ws_dash.cell(row=row_dash_avg, column=16).border = TOTAL_BORDER

ws_dash.conditional_formatting.add("N9:N23", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_dash.conditional_formatting.add("N9:N23", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))
ws_dash.conditional_formatting.add("P9:P23", CellIsRule(operator="equal", formula=['"AUTORIZADO (DUAL)"'], stopIfTrue=True, fill=green_fill, font=green_font))
ws_dash.conditional_formatting.add("P9:P23", CellIsRule(operator="equal", formula=['"PENDIENTE RECUP."'], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 6: SEGUIMIENTO DUAL Y EXTRAORDINARIA
# =============================================================
ws_dual = wb.create_sheet(title="Seguimiento Dual y Extraord")
ws_dual.views.sheetView[0].showGridLines = True

ws_dual.merge_cells("A1:J1")
ws_dual["A1"] = "FASE DE FORMACIÓN DUAL EN EMPRESA (T3 - 86 h) Y CONVOCATORIA EXTRAORDINARIA"
ws_dual["A1"].font = FONT_TITLE
ws_dual["A1"].fill = FILL_NAVY
ws_dual["A1"].alignment = ALIGN_CENTER
ws_dual.row_dimensions[1].height = 36

ws_dual.merge_cells("A2:J2")
ws_dual["A2"] = "Orden de 26 de septiembre de 2025 (Dual Andalucía) | Periodo en Empresa: Marzo a Junio 2026"
ws_dual["A2"].font = FONT_SUBTITLE
ws_dual["A2"].fill = FILL_SUBHEADER
ws_dual["A2"].alignment = ALIGN_CENTER
ws_dual.row_dimensions[2].height = 20

headers_dual = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("Nota Ordinaria\n(Marzo)", 15),
    ("Empresa Asignada", 22),
    ("Tutor/a Laboral", 20),
    ("Horas Dual\n(Módulo 86 h)", 14),
    ("Valoración Empresa\n(Apto / No Apto)", 18),
    ("RAs Pendientes\n(Extraordinaria)", 18),
    ("Nota Convocatoria\nExtraordinaria (Junio)", 20),
    ("Calificación Definitiva\nCurso Académico", 20)
]

ws_dual.row_dimensions[4].height = 38
for col_idx, (h_text, width) in enumerate(headers_dual, start=1):
    col_let = get_column_letter(col_idx)
    ws_dual.column_dimensions[col_let].width = width
    cell = ws_dual.cell(row=4, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 2:
        cell.fill = FILL_NAVY
    elif col_idx <= 7:
        cell.fill = FILL_TEAL_HEADER
    else:
        cell.fill = FILL_PURPLE_HEADER

for r_idx, (apell, nom) in enumerate(STUDENTS, start=5):
    ws_dual.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    dash_row = r_idx + 4  # Maps row 5 to row 9 in Dashboard
    
    # Nº & Nombre
    c1 = ws_dual.cell(row=r_idx, column=1, value=r_idx-4)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_dual.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # Nota Ordinaria (Pulled from Dashboard)
    c3 = ws_dual.cell(row=r_idx, column=3)
    c3.value = f"='Panel de Control'!N{dash_row}"
    c3.alignment = ALIGN_CENTER
    c3.border = CELL_BORDER
    c3.fill = FILL_TOTAL
    c3.font = FONT_BODY_BOLD
    c3.number_format = "0.00"
    
    # Empresa
    c4 = ws_dual.cell(row=r_idx, column=4, value="Innovatech Solutions S.L." if r_idx % 2 == 0 else "SoftAndalucía Dev Group")
    c4.alignment = ALIGN_LEFT
    c4.border = CELL_BORDER
    c4.fill = row_fill
    c4.font = FONT_BODY
    
    # Tutor
    c5 = ws_dual.cell(row=r_idx, column=5, value="Ing. Manuel Rivas" if r_idx % 2 == 0 else "Dra. Beatriz Cano")
    c5.alignment = ALIGN_LEFT
    c5.border = CELL_BORDER
    c5.fill = row_fill
    c5.font = FONT_BODY
    
    # Horas Dual
    c6 = ws_dual.cell(row=r_idx, column=6, value=86)
    c6.alignment = ALIGN_CENTER
    c6.border = CELL_BORDER
    c6.fill = row_fill
    c6.font = FONT_BODY
    
    # Valoración
    c7 = ws_dual.cell(row=r_idx, column=7)
    c7.value = f'=IF(C{r_idx}>=5, "APTO", "PENDIENTE")'
    c7.alignment = ALIGN_CENTER
    c7.border = CELL_BORDER
    c7.fill = row_fill
    c7.font = FONT_BODY_BOLD
    
    # RAs Pendientes
    c8 = ws_dual.cell(row=r_idx, column=8, value=f'=IF(C{r_idx}<5, "RA1, RA3", "Ninguno")')
    c8.alignment = ALIGN_CENTER
    c8.border = CELL_BORDER
    c8.fill = row_fill
    c8.font = FONT_BODY
    
    # Nota Extraordinaria
    c9 = ws_dual.cell(row=r_idx, column=9, value="")
    c9.alignment = ALIGN_CENTER
    c9.border = CELL_BORDER
    c9.fill = row_fill
    c9.font = FONT_BODY
    c9.number_format = "0.00"
    
    # Calificación Definitiva
    c10 = ws_dual.cell(row=r_idx, column=10)
    c10.value = f'=IF(ISBLANK(I{r_idx}), C{r_idx}, MAX(C{r_idx}, I{r_idx}))'
    c10.alignment = ALIGN_CENTER
    c10.border = CELL_BORDER
    c10.fill = FILL_GREEN_LIGHT
    c10.font = FONT_BODY_BOLD
    c10.number_format = "0.00"

ws_dual.conditional_formatting.add("J5:J19", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_dual.conditional_formatting.add("J5:J19", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 7: GUÍA DE FUNCIONAMIENTO INTERACTIVA
# =============================================================
ws_guide = wb.create_sheet(title="Guía de Funcionamiento")
ws_guide.views.sheetView[0].showGridLines = True

ws_guide.merge_cells("A1:G1")
ws_guide["A1"] = "GUÍA DE USO Y ARQUITECTURA DEL SISTEMA DE EVALUACIÓN"
ws_guide["A1"].font = FONT_TITLE
ws_guide["A1"].fill = FILL_NAVY
ws_guide["A1"].alignment = ALIGN_CENTER
ws_guide.row_dimensions[1].height = 36

guide_sections = [
    ("1. Filosofía y Funcionamiento Dinámico",
     "Esta hoja de cálculo implementa un motor de evaluación competencial bidireccional completamente automatizado:\n"
     "• La 'Matriz Criterios' contiene los 40 Criterios de Evaluación oficiales agrupados en los 8 Resultados de Aprendizaje.\n"
     "• En cualquier momento del curso puedes marcar o desmarcar con una 'X' qué criterios evalúa cada tarea o examen.\n"
     "• En la FILA 47 se calcula automáticamente la SUMA EXACTA DE LOS PESOS de los criterios marcados con 'X' para esa tarea.\n"
     "• En la FILA 48 se calcula el % DE PONDERACIÓN EN EL TRIMESTRE, normalizado a 100% (para que el boletín de notas trimestral sume 100%).\n"
     "• El motor recalcula en tiempo real las notas individuales de cada criterio, el avance de cada RA y las notas trimestrales y finales."),
    
    ("2. Flujo de Trabajo para el Docente",
     "PASO 1: Configurar la Matriz Criterios\n"
     "Revisa las columnas H a V (tareas T01 a T15). Coloca una 'X' en la fila del criterio que evalúe dicha tarea.\n"
     "La fila 46 te indica cuántos criterios evalúa cada tarea.\n"
     "La fila 47 calcula dinámicamente la suma directa de los pesos de dichos criterios sobre el total del módulo.\n"
     "La fila 48 rebalancea automáticamente los porcentajes dentro de cada trimestre sumando exactamente el 100%.\n\n"
     "PASO 2: Introducir Calificaciones en 'Registro Notas'\n"
     "Introduce las notas (0.00 a 10.00) obtenidas por los alumnos en cada tarea (columnas D a R).\n"
     "Las notas de 1º y 2º Trimestre se calculan automáticamente en las columnas S y T a partir de los pesos derivados de los criterios.\n\n"
     "PASO 3: Supervisar el 'Panel de Control'\n"
     "Observa las tarjetas de KPIs (Alumnos, Aprobados, Suspensos, Nota Media, Tasa de Éxito) y la tabla consolidada\n"
     "con la calificación oficial en marzo y la autorización automática para la estancia Dual en empresa."),
    
    ("3. Robustez Matemática (Sin Ceros Prematuros)",
     "La fórmula implementada en cada criterio utiliza la función ISNUMBER combinada con SUMPRODUCT:\n"
     "Solo se promedian aquellas tareas que tienen una 'X' Y QUE ADEMÁS TIENEN NOTA INTRODUCIDA.\n"
     "Esto evita que un alumno aparezca con una nota suspensa en un criterio a principio de curso simplemente\n"
     "porque las tareas del segundo trimestre todavía no se han impartido o calificado."),
    
    ("4. Marco Normativo Integrado",
     "• Ley Orgánica 3/2022 y Real Decreto 659/2023 (Ordenación del Sistema de Formación Profesional).\n"
     "• Real Decreto 405/2023 y Real Decreto 500/2024 (Currículo oficial y competencias de DAM).\n"
     "• Decreto 104/2024 (Ordenación de FP en Andalucía, derogando el Decreto 436/2008).\n"
     "• Orden de 18 de septiembre de 2025 (Evaluación y acreditación del alumnado de FP en Andalucía).\n"
     "• Orden de 26 de septiembre de 2025 (Regulación de la formación dual y estancias en empresa en Andalucía).")
]

ws_guide.column_dimensions["A"].width = 6
ws_guide.column_dimensions["B"].width = 85
for c in ["C", "D", "E", "F", "G"]:
    ws_guide.column_dimensions[c].width = 12

curr_row = 3
for title, text in guide_sections:
    ws_guide.row_dimensions[curr_row].height = 26
    ws_guide.merge_cells(f"B{curr_row}:G{curr_row}")
    cell_sec = ws_guide[f"B{curr_row}"]
    cell_sec.value = title
    cell_sec.font = Font(name="Segoe UI", size=11, bold=True, color="1E3A8A")
    cell_sec.fill = FILL_BLUE_LIGHT
    cell_sec.alignment = ALIGN_LEFT
    cell_sec.border = HEADER_BORDER
    curr_row += 1
    
    num_lines = text.count("\n") + 1
    ws_guide.row_dimensions[curr_row].height = max(50, num_lines * 18)
    ws_guide.merge_cells(f"B{curr_row}:G{curr_row}")
    cell_body = ws_guide[f"B{curr_row}"]
    cell_body.value = text
    cell_body.font = FONT_BODY
    cell_body.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    cell_body.fill = FILL_ZEBRA
    cell_body.border = CELL_BORDER
    curr_row += 2


# -------------------------------------------------------------
# Save Workbook
# -------------------------------------------------------------
output_dir = r"e:\00. Clases\Apuntes\Desarrollo_Interfaces\programación"
os.makedirs(output_dir, exist_ok=True)

excel_path = os.path.join(output_dir, "Hoja_Evaluacion_Avanzada_DI_2DAM_2025_2026.xlsx")
excel_path_v2 = os.path.join(output_dir, "Hoja_Evaluacion_Avanzada_DI_2DAM_2025_2026_v2.xlsx")

try:
    wb.save(excel_path)
    print(f"Hoja de evaluación avanzada actualizada con éxito en:\n{excel_path}")
except PermissionError:
    wb.save(excel_path_v2)
    print(f"AVISO: El archivo principal está abierto en Excel. Se ha guardado la nueva versión actualizada en:\n{excel_path_v2}")
