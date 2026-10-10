import sys
import os
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule

sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.Workbook()
# Remove default sheet
wb.remove(wb.active)

# -------------------------------------------------------------
# Color Palette & Styles
# -------------------------------------------------------------
NAVY_HEADER = "1E293B"      # Dark Navy
NAVY_SUBHEADER = "334155"   # Slate Navy
BLUE_ACCENT = "2563EB"      # Bright Blue
TEAL_ACCENT = "0D9488"      # Teal
GREEN_HEADER = "15803D"     # Forest Green
PURPLE_HEADER = "6B21A8"    # Purple
ORANGE_HEADER = "C2410C"    # Dark Orange

FILL_NAVY = PatternFill(start_color=NAVY_HEADER, end_color=NAVY_HEADER, fill_type="solid")
FILL_SUBHEADER = PatternFill(start_color=NAVY_SUBHEADER, end_color=NAVY_SUBHEADER, fill_type="solid")
FILL_BLUE = PatternFill(start_color="DBEAFE", end_color="DBEAFE", fill_type="solid")
FILL_BLUE_HEADER = PatternFill(start_color="1D4ED8", end_color="1D4ED8", fill_type="solid")
FILL_TEAL_HEADER = PatternFill(start_color="0F766E", end_color="0F766E", fill_type="solid")
FILL_GREEN_LIGHT = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
FILL_GREEN_HEADER = PatternFill(start_color=GREEN_HEADER, end_color=GREEN_HEADER, fill_type="solid")
FILL_PURPLE_HEADER = PatternFill(start_color=PURPLE_HEADER, end_color=PURPLE_HEADER, fill_type="solid")
FILL_ORANGE_HEADER = PatternFill(start_color=ORANGE_HEADER, end_color=ORANGE_HEADER, fill_type="solid")
FILL_ZEBRA = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
FILL_TOTAL = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid") # Warm light yellow

FONT_TITLE = Font(name="Segoe UI", size=15, bold=True, color="FFFFFF")
FONT_SUBTITLE = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
FONT_HEADER = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
FONT_HEADER_DARK = Font(name="Segoe UI", size=10, bold=True, color="1E293B")
FONT_BODY = Font(name="Segoe UI", size=10)
FONT_BODY_BOLD = Font(name="Segoe UI", size=10, bold=True)
FONT_KPI_VAL = Font(name="Segoe UI", size=16, bold=True, color="1E293B")
FONT_KPI_LABEL = Font(name="Segoe UI", size=9, bold=True, color="64748B")

BORDER_THIN = Side(border_style="thin", color="CBD5E1")
BORDER_MEDIUM = Side(border_style="medium", color="64748B")
BORDER_DOUBLE = Side(border_style="double", color="1E293B")

CELL_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_THIN)
TOTAL_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_DOUBLE)
HEADER_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_MEDIUM)

ALIGN_CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
ALIGN_LEFT = Alignment(horizontal="left", vertical="center")
ALIGN_RIGHT = Alignment(horizontal="right", vertical="center")

# Sample Students
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

# Sample Grades generator for realistic initial demo data
SAMPLE_T1 = [
    [8.5, 9.0, 8.0, 8.5, 9.0, 8.5],
    [6.0, 5.5, 6.5, 7.0, 6.0, 6.0],
    [9.5, 9.0, 10.0, 9.5, 10.0, 9.5],
    [4.0, 5.0, 4.5, 5.5, 4.0, 4.5],
    [7.5, 8.0, 7.0, 7.5, 8.0, 7.5],
    [8.0, 7.5, 8.5, 8.0, 8.5, 8.0],
    [9.0, 8.5, 9.5, 9.0, 9.0, 9.0],
    [5.0, 6.0, 5.5, 5.0, 6.0, 5.5],
    [10.0, 9.5, 9.5, 10.0, 9.5, 10.0],
    [3.5, 4.0, 4.0, 4.5, 4.0, 3.5],
    [8.0, 8.5, 8.0, 8.5, 8.0, 8.5],
    [7.0, 6.5, 7.5, 7.0, 7.0, 7.0],
    [6.5, 7.0, 6.0, 6.5, 7.0, 6.5],
    [8.5, 9.0, 8.5, 9.0, 8.5, 9.0],
    [9.0, 9.5, 9.0, 9.5, 9.0, 9.5]
]

SAMPLE_T2 = [
    [8.5, 9.0, 8.5, 9.0, 8.5, 9.0, 8.5],
    [6.5, 6.0, 7.0, 6.5, 6.0, 6.5, 6.0],
    [10.0, 9.5, 9.5, 10.0, 9.5, 10.0, 10.0],
    [5.0, 4.5, 5.0, 4.5, 5.0, 4.5, 4.0],
    [7.5, 8.0, 8.0, 7.5, 8.0, 7.5, 8.0],
    [8.0, 8.5, 8.0, 8.5, 8.0, 8.5, 8.0],
    [9.0, 9.5, 9.0, 9.5, 9.0, 9.5, 9.0],
    [5.5, 6.0, 5.5, 6.0, 5.5, 6.0, 5.5],
    [10.0, 9.5, 10.0, 10.0, 9.5, 10.0, 10.0],
    [4.0, 4.5, 4.0, 4.0, 4.5, 4.0, 4.0],
    [8.5, 8.0, 8.5, 8.5, 8.0, 8.5, 8.5],
    [7.5, 7.0, 7.5, 7.0, 7.5, 7.0, 7.5],
    [7.0, 6.5, 7.0, 6.5, 7.0, 6.5, 7.0],
    [9.0, 8.5, 9.0, 9.0, 8.5, 9.0, 9.0],
    [9.5, 9.0, 9.5, 10.0, 9.5, 9.5, 9.5]
]

# =============================================================
# SHEET 1: DASHBOARD & RESUMEN FINAL
# =============================================================
ws_dash = wb.create_sheet(title="Resumen y Calificaciones")
ws_dash.views.sheetView[0].showGridLines = True

# Title Header
ws_dash.merge_cells("A1:N1")
cell_t = ws_dash["A1"]
cell_t.value = "DESARROLLO DE INTERFACES (2º DAM) — CUADRO DE CALIFICACIONES Y SEGUIMIENTO"
cell_t.font = FONT_TITLE
cell_t.fill = FILL_NAVY
cell_t.alignment = ALIGN_CENTER
ws_dash.row_dimensions[1].height = 40

ws_dash.merge_cells("A2:N2")
cell_sub = ws_dash["A2"]
cell_sub.value = "Curso 2025/2026 | IES / Centro Educativo | Módulo: 0488 (210 h - Dual) | Decreto 104/2024 & Orden 18/09/2025"
cell_sub.font = Font(name="Segoe UI", size=10, italic=True, color="CBD5E1")
cell_sub.fill = FILL_SUBHEADER
cell_sub.alignment = ALIGN_CENTER
ws_dash.row_dimensions[2].height = 22

# KPI Cards Block (Rows 4 to 6)
ws_dash.merge_cells("B4:C4")
ws_dash["B4"] = "ALUMNADO MATRICULADO"
ws_dash["B4"].font = FONT_KPI_LABEL
ws_dash["B4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("B5:C6")
ws_dash["B5"] = '=COUNTA(A9:A23)'
ws_dash["B5"].font = FONT_KPI_VAL
ws_dash["B5"].alignment = ALIGN_CENTER
ws_dash["B5"].fill = FILL_BLUE

ws_dash.merge_cells("E4:F4")
ws_dash["E4"] = "APROBADOS EVAL. ORDINARIA"
ws_dash["E4"].font = FONT_KPI_LABEL
ws_dash["E4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("E5:F6")
ws_dash["E5"] = '=COUNTIF(M9:M23, ">=5")'
ws_dash["E5"].font = Font(name="Segoe UI", size=16, bold=True, color="15803D")
ws_dash["E5"].alignment = ALIGN_CENTER
ws_dash["E5"].fill = FILL_GREEN_LIGHT

ws_dash.merge_cells("H4:I4")
ws_dash["H4"] = "SUSPENSOS EVAL. ORDINARIA"
ws_dash["H4"].font = FONT_KPI_LABEL
ws_dash["H4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("H5:I6")
ws_dash["H5"] = '=COUNTIF(M9:M23, "<5")'
ws_dash["H5"].font = Font(name="Segoe UI", size=16, bold=True, color="DC2626")
ws_dash["H5"].alignment = ALIGN_CENTER
ws_dash["H5"].fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")

ws_dash.merge_cells("K4:L4")
ws_dash["K4"] = "NOTA MEDIA DEL GRUPO"
ws_dash["K4"].font = FONT_KPI_LABEL
ws_dash["K4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("K5:L6")
ws_dash["K5"] = '=AVERAGE(M9:M23)'
ws_dash["K5"].font = FONT_KPI_VAL
ws_dash["K5"].alignment = ALIGN_CENTER
ws_dash["K5"].fill = FILL_TOTAL
ws_dash["K5"].number_format = "0.00"

# Main Table Headers
headers_dash = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("RA1\n(22%)\nUX/Figma", 9),
    ("RA2\n(16%)\nNUI/Voz", 9),
    ("RA3\n(20%)\nAngular", 9),
    ("RA4\n(11%)\nA11y", 9),
    ("RA5\n(4%)\nInformes", 9),
    ("RA6\n(7%)\nDocum.", 9),
    ("RA7\n(10%)\nElectron", 9),
    ("RA8\n(10%)\nPruebas", 9),
    ("1º Trim\n(T1)", 10),
    ("2º Trim\n(T2)", 10),
    ("Nota Final\nOrdinaria (Marzo)", 16),
    ("Estado / Calificación", 18)
]

ws_dash.row_dimensions[8].height = 42
for col_idx, (h_text, width) in enumerate(headers_dash, start=1):
    col_letter = get_column_letter(col_idx)
    ws_dash.column_dimensions[col_letter].width = width
    cell = ws_dash.cell(row=8, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 2:
        cell.fill = FILL_NAVY
    elif col_idx <= 10:
        cell.fill = FILL_BLUE_HEADER
    elif col_idx <= 12:
        cell.fill = FILL_TEAL_HEADER
    else:
        cell.fill = FILL_GREEN_HEADER

# Student rows in Dashboard
for r_idx, (apell, nom) in enumerate(STUDENTS, start=9):
    ws_dash.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº
    c1 = ws_dash.cell(row=r_idx, column=1, value=r_idx-8)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    # Nombre
    c2 = ws_dash.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # References to Sheet 'Calculo RAs'
    # RA1 to RA8 are columns C to J in ws_dash, pulling from 'Calculo RAs'!C to 'Calculo RAs'!J
    for ra_idx in range(3, 11):
        ra_col_letter = get_column_letter(ra_idx)
        c_ra = ws_dash.cell(row=r_idx, column=ra_idx)
        c_ra.value = f"='Calculo RAs'!{ra_col_letter}{r_idx}"
        c_ra.alignment = ALIGN_CENTER
        c_ra.border = CELL_BORDER
        c_ra.fill = row_fill
        c_ra.font = FONT_BODY
        c_ra.number_format = "0.00"
        
    # 1º Trimestre (pulled from '1er Trimestre'!J)
    c_t1 = ws_dash.cell(row=r_idx, column=11)
    c_t1.value = f"='1er Trimestre'!J{r_idx}"
    c_t1.alignment = ALIGN_CENTER
    c_t1.border = CELL_BORDER
    c_t1.fill = PatternFill(start_color="F0FDFA", end_color="F0FDFA", fill_type="solid") if is_zebra else PatternFill(start_color="CCFBF1", end_color="CCFBF1", fill_type="solid")
    c_t1.font = FONT_BODY_BOLD
    c_t1.number_format = "0.00"
    
    # 2º Trimestre (pulled from '2º Trimestre'!K)
    c_t2 = ws_dash.cell(row=r_idx, column=12)
    c_t2.value = f"='2º Trimestre'!K{r_idx}"
    c_t2.alignment = ALIGN_CENTER
    c_t2.border = CELL_BORDER
    c_t2.fill = PatternFill(start_color="F0FDFA", end_color="F0FDFA", fill_type="solid") if is_zebra else PatternFill(start_color="CCFBF1", end_color="CCFBF1", fill_type="solid")
    c_t2.font = FONT_BODY_BOLD
    c_t2.number_format = "0.00"
    
    # Nota Final Ordinaria (Ponderada Oficial RAs)
    # RA1*0.22 + RA2*0.16 + RA3*0.20 + RA4*0.11 + RA5*0.04 + RA6*0.07 + RA7*0.10 + RA8*0.10
    c_final = ws_dash.cell(row=r_idx, column=13)
    c_final.value = f"=C{r_idx}*0.22 + D{r_idx}*0.16 + E{r_idx}*0.20 + F{r_idx}*0.11 + G{r_idx}*0.04 + H{r_idx}*0.07 + I{r_idx}*0.10 + J{r_idx}*0.10"
    c_final.alignment = ALIGN_CENTER
    c_final.border = CELL_BORDER
    c_final.fill = FILL_TOTAL
    c_final.font = Font(name="Segoe UI", size=10, bold=True, color="1E293B")
    c_final.number_format = "0.00"
    
    # Estado
    c_est = ws_dash.cell(row=r_idx, column=14)
    c_est.value = f'=IF(M{r_idx}>=9, "SOBRESALIENTE", IF(M{r_idx}>=7, "NOTABLE", IF(M{r_idx}>=6, "BIEN", IF(M{r_idx}>=5, "SUFICIENTE", "INSUFICIENTE"))))'
    c_est.alignment = ALIGN_CENTER
    c_est.border = CELL_BORDER
    c_est.fill = row_fill
    c_est.font = FONT_BODY_BOLD

# Group Averages Row
row_avg = 24
ws_dash.row_dimensions[row_avg].height = 24
ws_dash.merge_cells(f"A{row_avg}:B{row_avg}")
c_avg_lbl = ws_dash.cell(row=row_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl.font = FONT_HEADER_DARK
c_avg_lbl.alignment = ALIGN_CENTER
c_avg_lbl.fill = FILL_TOTAL
c_avg_lbl.border = TOTAL_BORDER
ws_dash.cell(row=row_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 14):
    col_let = get_column_letter(col_idx)
    c_avg = ws_dash.cell(row=row_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}9:{col_let}23)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

c_avg_end = ws_dash.cell(row=row_avg, column=14, value="")
c_avg_end.fill = FILL_TOTAL
c_avg_end.border = TOTAL_BORDER

# Conditional Formatting on Dashboard
green_fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
green_font = Font(color="15803D", bold=True)
red_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
red_font = Font(color="DC2626", bold=True)

ws_dash.conditional_formatting.add("K9:M23", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_dash.conditional_formatting.add("K9:M23", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 2: 1ER TRIMESTRE (UD00 - UD11)
# =============================================================
ws_t1 = wb.create_sheet(title="1er Trimestre")
ws_t1.views.sheetView[0].showGridLines = True

# Title Header
ws_t1.merge_cells("A1:J1")
cell_t1 = ws_t1["A1"]
cell_t1.value = "1º TRIMESTRE — DESARROLLO DE INTERFACES (UD00 a UD11)"
cell_t1.font = FONT_TITLE
cell_t1.fill = FILL_NAVY
cell_t1.alignment = ALIGN_CENTER
ws_t1.row_dimensions[1].height = 36

ws_t1.merge_cells("A2:J2")
cell_sub1 = ws_t1["A2"]
cell_sub1.value = "Bloque I & II: Fundamentos UX, Figma, NUI/Voz, Tailwind CSS v4, Responsive y Arquitectura Angular Standalone"
cell_sub1.font = Font(name="Segoe UI", size=10, italic=True, color="CBD5E1")
cell_sub1.fill = FILL_SUBHEADER
cell_sub1.alignment = ALIGN_CENTER
ws_t1.row_dimensions[2].height = 20

# Subheaders specifying UD and associated CEs
ws_t1.row_dimensions[4].height = 26
ws_t1.row_dimensions[5].height = 22
ws_t1.row_dimensions[6].height = 30

# Activity headers with CEs and weights
t1_activities = [
    ("Nº", 5, "", ""),
    ("Apellidos, Nombre", 25, "", ""),
    ("Actividad 1 (15%)\nPrototipado Figma UX", 18, "UD01, UD04", "RA1 (CE1.a, CE1.b, CE1.c)"),
    ("Actividad 2 (15%)\nNUI & Web Speech API", 18, "UD03", "RA2 (CE2.a, CE2.b, CE2.e)"),
    ("Actividad 3 (15%)\nLayouts Grid & Tailwind", 18, "UD05, UD06, UD07", "RA1 (CE1.d, CE1.e, CE1.f)"),
    ("Actividad 4 (15%)\nAccesibilidad & Responsive", 18, "UD02, UD08", "RA4 (CE4.a, CE4.b, CE4.c)"),
    ("Actividad 5 (15%)\nComponentes Angular Signals", 18, "UD09, UD10, UD11", "RA3 (CE3.a, CE3.b, CE3.c)"),
    ("Examen Práctico T1 (25%)\nDesarrollo UI Completa", 18, "UD01 a UD11", "RA1, RA2, RA3, RA4"),
    ("Actitud y Git (10%)\nControl Versiones y DUA", 16, "Transversal", "Buenas prácticas"),
    ("CALIFICACIÓN\n1º TRIMESTRE", 16, "Ponderación 100%", "Nota T1")
]

for col_idx, (title, width, uds, ces) in enumerate(t1_activities, start=1):
    col_let = get_column_letter(col_idx)
    ws_t1.column_dimensions[col_let].width = width
    
    c4 = ws_t1.cell(row=4, column=col_idx, value=uds)
    c4.font = Font(name="Segoe UI", size=8, bold=True, color="64748B")
    c4.alignment = ALIGN_CENTER
    c4.border = HEADER_BORDER
    c4.fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    
    c5 = ws_t1.cell(row=5, column=col_idx, value=ces)
    c5.font = Font(name="Segoe UI", size=8, italic=True, color="475569")
    c5.alignment = ALIGN_CENTER
    c5.border = HEADER_BORDER
    c5.fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    
    c6 = ws_t1.cell(row=6, column=col_idx, value=title)
    c6.font = FONT_HEADER
    c6.alignment = ALIGN_CENTER
    c6.border = HEADER_BORDER
    if col_idx <= 2:
        c6.fill = FILL_NAVY
    elif col_idx <= 8:
        c6.fill = FILL_BLUE_HEADER
    elif col_idx == 9:
        c6.fill = FILL_PURPLE_HEADER
    else:
        c6.fill = FILL_TEAL_HEADER

# Fill Student Rows for T1
for r_idx, (apell, nom) in enumerate(STUDENTS, start=9):
    ws_t1.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº
    c1 = ws_t1.cell(row=r_idx, column=1, value=r_idx-8)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    # Nombre
    c2 = ws_t1.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # Grades C to I (Cols 3 to 9)
    sample_scores = SAMPLE_T1[r_idx-9]
    # sample_scores has 6 values + 1 for attitude
    scores_to_put = sample_scores + [8.5 if sample_scores[0] > 7 else (5.0 if sample_scores[0] < 5 else 7.0)]
    for c_i, score in enumerate(scores_to_put, start=3):
        c_val = ws_t1.cell(row=r_idx, column=c_i, value=score)
        c_val.alignment = ALIGN_CENTER
        c_val.border = CELL_BORDER
        c_val.fill = row_fill
        c_val.font = FONT_BODY
        c_val.number_format = "0.00"
        
    # Formula for T1 Note:
    # Act1*0.15 + Act2*0.15 + Act3*0.15 + Act4*0.15 + Act5*0.15 + Examen*0.25 + Actitud*0.10
    c_t1_tot = ws_t1.cell(row=r_idx, column=10)
    c_t1_tot.value = f"=C{r_idx}*0.15 + D{r_idx}*0.15 + E{r_idx}*0.15 + F{r_idx}*0.15 + G{r_idx}*0.15 + H{r_idx}*0.25 + I{r_idx}*0.10"
    c_t1_tot.alignment = ALIGN_CENTER
    c_t1_tot.border = CELL_BORDER
    c_t1_tot.fill = PatternFill(start_color="CCFBF1", end_color="CCFBF1", fill_type="solid")
    c_t1_tot.font = FONT_BODY_BOLD
    c_t1_tot.number_format = "0.00"

# T1 Average Row
ws_t1.row_dimensions[row_avg].height = 24
ws_t1.merge_cells(f"A{row_avg}:B{row_avg}")
c_avg_lbl1 = ws_t1.cell(row=row_avg, column=1, value="PROMEDIO DEL GRUPO (T1)")
c_avg_lbl1.font = FONT_HEADER_DARK
c_avg_lbl1.alignment = ALIGN_CENTER
c_avg_lbl1.fill = FILL_TOTAL
c_avg_lbl1.border = TOTAL_BORDER
ws_t1.cell(row=row_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 11):
    col_let = get_column_letter(col_idx)
    c_avg = ws_t1.cell(row=row_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}9:{col_let}23)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_t1.conditional_formatting.add("J9:J23", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_t1.conditional_formatting.add("J9:J23", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 3: 2º TRIMESTRE (UD12 - UD22)
# =============================================================
ws_t2 = wb.create_sheet(title="2º Trimestre")
ws_t2.views.sheetView[0].showGridLines = True

# Title Header
ws_t2.merge_cells("A1:K1")
cell_t2 = ws_t2["A1"]
cell_t2.value = "2º TRIMESTRE — DESARROLLO DE INTERFACES (UD12 a UD22)"
cell_t2.font = FONT_TITLE
cell_t2.fill = FILL_NAVY
cell_t2.alignment = ALIGN_CENTER
ws_t2.row_dimensions[1].height = 36

ws_t2.merge_cells("A2:K2")
cell_sub2 = ws_t2["A2"]
cell_sub2.value = "Bloque III & IV: Formularios, Storybook, Informes/Dashboards, Pruebas Vitest/Playwright, Electron y Proyecto GesFlow"
cell_sub2.font = Font(name="Segoe UI", size=10, italic=True, color="CBD5E1")
cell_sub2.fill = FILL_SUBHEADER
cell_sub2.alignment = ALIGN_CENTER
ws_t2.row_dimensions[2].height = 20

# Subheaders specifying UD and associated CEs
ws_t2.row_dimensions[4].height = 26
ws_t2.row_dimensions[5].height = 22
ws_t2.row_dimensions[6].height = 30

t2_activities = [
    ("Nº", 5, "", ""),
    ("Apellidos, Nombre", 25, "", ""),
    ("Actividad 6 (10%)\nFormularios & A11y", 18, "UD12", "RA3, RA4 (CE3.f, CE4.b)"),
    ("Actividad 7 (10%)\nStorybook & Tokens", 18, "UD13, UD14, UD15", "RA3, RA6 (CE3.e, CE6.c)"),
    ("Actividad 8 (10%)\nInformes PDF & Dashboards", 18, "UD16, UD17", "RA5 (CE5.a, CE5.b, CE5.c, CE5.d)"),
    ("Actividad 9 (10%)\nPruebas Vitest & Playwright", 18, "UD19", "RA8 (CE8.b, CE8.c, CE8.d)"),
    ("Actividad 10 (10%)\nEscritorio Electron & IPC", 18, "UD20, UD21", "RA7 (CE7.a, CE7.b, CE7.c, CE7.d)"),
    ("Proyecto Final (30%)\nGesFlow Integrador", 20, "UD22", "RA1 a RA8 Integrados"),
    ("Examen Práctico T2 (15%)\nPrueba Desarrollo Global", 18, "UD12 a UD21", "RA3, RA5, RA7, RA8"),
    ("Actitud y Git (5%)\nCalidad & Despliegue", 16, "Transversal", "Buenas prácticas"),
    ("CALIFICACIÓN\n2º TRIMESTRE", 16, "Ponderación 100%", "Nota T2")
]

for col_idx, (title, width, uds, ces) in enumerate(t2_activities, start=1):
    col_let = get_column_letter(col_idx)
    ws_t2.column_dimensions[col_let].width = width
    
    c4 = ws_t2.cell(row=4, column=col_idx, value=uds)
    c4.font = Font(name="Segoe UI", size=8, bold=True, color="64748B")
    c4.alignment = ALIGN_CENTER
    c4.border = HEADER_BORDER
    c4.fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    
    c5 = ws_t2.cell(row=5, column=col_idx, value=ces)
    c5.font = Font(name="Segoe UI", size=8, italic=True, color="475569")
    c5.alignment = ALIGN_CENTER
    c5.border = HEADER_BORDER
    c5.fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    
    c6 = ws_t2.cell(row=6, column=col_idx, value=title)
    c6.font = FONT_HEADER
    c6.alignment = ALIGN_CENTER
    c6.border = HEADER_BORDER
    if col_idx <= 2:
        c6.fill = FILL_NAVY
    elif col_idx <= 8:
        c6.fill = FILL_BLUE_HEADER
    elif col_idx == 9:
        c6.fill = FILL_ORANGE_HEADER
    elif col_idx == 10:
        c6.fill = FILL_PURPLE_HEADER
    else:
        c6.fill = FILL_TEAL_HEADER

# Fill Student Rows for T2
for r_idx, (apell, nom) in enumerate(STUDENTS, start=9):
    ws_t2.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº
    c1 = ws_t2.cell(row=r_idx, column=1, value=r_idx-8)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    # Nombre
    c2 = ws_t2.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # Scores C to J (Cols 3 to 10)
    sample_scores2 = SAMPLE_T2[r_idx-9]
    scores_to_put2 = sample_scores2 + [9.0 if sample_scores2[0] > 7 else (5.0 if sample_scores2[0] < 5 else 7.5)]
    for c_i, score in enumerate(scores_to_put2, start=3):
        c_val = ws_t2.cell(row=r_idx, column=c_i, value=score)
        c_val.alignment = ALIGN_CENTER
        c_val.border = CELL_BORDER
        c_val.fill = row_fill
        c_val.font = FONT_BODY
        c_val.number_format = "0.00"
        
    # Formula for T2 Note:
    # Act6*0.10 + Act7*0.10 + Act8*0.10 + Act9*0.10 + Act10*0.10 + GesFlow*0.30 + Examen*0.15 + Actitud*0.05
    c_t2_tot = ws_t2.cell(row=r_idx, column=11)
    c_t2_tot.value = f"=C{r_idx}*0.10 + D{r_idx}*0.10 + E{r_idx}*0.10 + F{r_idx}*0.10 + G{r_idx}*0.10 + H{r_idx}*0.30 + I{r_idx}*0.15 + J{r_idx}*0.05"
    c_t2_tot.alignment = ALIGN_CENTER
    c_t2_tot.border = CELL_BORDER
    c_t2_tot.fill = PatternFill(start_color="CCFBF1", end_color="CCFBF1", fill_type="solid")
    c_t2_tot.font = FONT_BODY_BOLD
    c_t2_tot.number_format = "0.00"

# T2 Average Row
ws_t2.row_dimensions[row_avg].height = 24
ws_t2.merge_cells(f"A{row_avg}:B{row_avg}")
c_avg_lbl2 = ws_t2.cell(row=row_avg, column=1, value="PROMEDIO DEL GRUPO (T2)")
c_avg_lbl2.font = FONT_HEADER_DARK
c_avg_lbl2.alignment = ALIGN_CENTER
c_avg_lbl2.fill = FILL_TOTAL
c_avg_lbl2.border = TOTAL_BORDER
ws_t2.cell(row=row_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 12):
    col_let = get_column_letter(col_idx)
    c_avg = ws_t2.cell(row=row_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}9:{col_let}23)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_t2.conditional_formatting.add("K9:K23", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_t2.conditional_formatting.add("K9:K23", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 4: CÁLCULO POR RESULTADOS DE APRENDIZAJE (RAs)
# =============================================================
ws_ras = wb.create_sheet(title="Calculo RAs")
ws_ras.views.sheetView[0].showGridLines = True

ws_ras.merge_cells("A1:K1")
cell_tras = ws_ras["A1"]
cell_tras.value = "DESGLOSE Y CÁLCULO POR RESULTADOS DE APRENDIZAJE (RA1 a RA8)"
cell_tras.font = FONT_TITLE
cell_tras.fill = FILL_NAVY
cell_tras.alignment = ALIGN_CENTER
ws_ras.row_dimensions[1].height = 36

ws_ras.merge_cells("A2:K2")
cell_subras = ws_ras["A2"]
cell_subras.value = "Fórmulas vinculadas a las tareas de T1 y T2 según Criterios de Evaluación evaluados en cada actividad"
cell_subras.font = Font(name="Segoe UI", size=10, italic=True, color="CBD5E1")
cell_subras.fill = FILL_SUBHEADER
cell_subras.alignment = ALIGN_CENTER
ws_ras.row_dimensions[2].height = 20

headers_ras = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("RA1 (22%)\nDiseño UI, Figma\nTailwind, Grid", 15),
    ("RA2 (16%)\nInterfaces NUI\nVoz & Gestos", 15),
    ("RA3 (20%)\nComponentes\nAngular Standalone", 15),
    ("RA4 (11%)\nAccesibilidad\nUniversal WCAG", 15),
    ("RA5 (4%)\nInformes PDF\ny Cuadros Mando", 15),
    ("RA6 (7%)\nDocumentación\ny Storybook", 15),
    ("RA7 (10%)\nElectron Desktop\ny Distribución", 15),
    ("RA8 (10%)\nPruebas Vitest\ny Playwright", 15),
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

# Formulas for each RA based on T1 and T2 activities
# RA1: Evaluated in T1 Act1 (Figma), T1 Act3 (Tailwind/Grid), T1 Examen, T2 GesFlow
# RA2: Evaluated in T1 Act2 (NUI), T1 Examen, T2 GesFlow
# RA3: Evaluated in T1 Act5 (Angular), T2 Act6 (Forms), T2 Act7 (Storybook), T2 GesFlow, T2 Examen
# RA4: Evaluated in T1 Act4 (A11y), T2 Act6 (A11y Forms), T2 GesFlow
# RA5: Evaluated in T2 Act8 (Informes), T2 GesFlow, T2 Examen
# RA6: Evaluated in T2 Act7 (Storybook Doc), T2 GesFlow
# RA7: Evaluated in T2 Act10 (Electron), T2 GesFlow, T2 Examen
# RA8: Evaluated in T2 Act9 (Pruebas), T2 GesFlow, T2 Examen

for r_idx, (apell, nom) in enumerate(STUDENTS, start=9):
    ws_ras.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº & Nombre
    c1 = ws_ras.cell(row=r_idx, column=1, value=r_idx-8)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_ras.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # RA1 (Col C)
    c_ra1 = ws_ras.cell(row=r_idx, column=3)
    c_ra1.value = f"=AVERAGE('1er Trimestre'!C{r_idx}, '1er Trimestre'!E{r_idx}, '1er Trimestre'!H{r_idx}, '2º Trimestre'!H{r_idx})"
    c_ra1.alignment = ALIGN_CENTER
    c_ra1.border = CELL_BORDER
    c_ra1.fill = row_fill
    c_ra1.font = FONT_BODY
    c_ra1.number_format = "0.00"
    
    # RA2 (Col D)
    c_ra2 = ws_ras.cell(row=r_idx, column=4)
    c_ra2.value = f"=AVERAGE('1er Trimestre'!D{r_idx}, '1er Trimestre'!H{r_idx}, '2º Trimestre'!H{r_idx})"
    c_ra2.alignment = ALIGN_CENTER
    c_ra2.border = CELL_BORDER
    c_ra2.fill = row_fill
    c_ra2.font = FONT_BODY
    c_ra2.number_format = "0.00"
    
    # RA3 (Col E)
    c_ra3 = ws_ras.cell(row=r_idx, column=5)
    c_ra3.value = f"=AVERAGE('1er Trimestre'!G{r_idx}, '2º Trimestre'!C{r_idx}, '2º Trimestre'!D{r_idx}, '2º Trimestre'!H{r_idx}, '2º Trimestre'!I{r_idx})"
    c_ra3.alignment = ALIGN_CENTER
    c_ra3.border = CELL_BORDER
    c_ra3.fill = row_fill
    c_ra3.font = FONT_BODY
    c_ra3.number_format = "0.00"
    
    # RA4 (Col F)
    c_ra4 = ws_ras.cell(row=r_idx, column=6)
    c_ra4.value = f"=AVERAGE('1er Trimestre'!F{r_idx}, '2º Trimestre'!C{r_idx}, '2º Trimestre'!H{r_idx})"
    c_ra4.alignment = ALIGN_CENTER
    c_ra4.border = CELL_BORDER
    c_ra4.fill = row_fill
    c_ra4.font = FONT_BODY
    c_ra4.number_format = "0.00"
    
    # RA5 (Col G)
    c_ra5 = ws_ras.cell(row=r_idx, column=7)
    c_ra5.value = f"=AVERAGE('2º Trimestre'!E{r_idx}, '2º Trimestre'!H{r_idx}, '2º Trimestre'!I{r_idx})"
    c_ra5.alignment = ALIGN_CENTER
    c_ra5.border = CELL_BORDER
    c_ra5.fill = row_fill
    c_ra5.font = FONT_BODY
    c_ra5.number_format = "0.00"
    
    # RA6 (Col H)
    c_ra6 = ws_ras.cell(row=r_idx, column=8)
    c_ra6.value = f"=AVERAGE('2º Trimestre'!D{r_idx}, '2º Trimestre'!H{r_idx})"
    c_ra6.alignment = ALIGN_CENTER
    c_ra6.border = CELL_BORDER
    c_ra6.fill = row_fill
    c_ra6.font = FONT_BODY
    c_ra6.number_format = "0.00"
    
    # RA7 (Col I)
    c_ra7 = ws_ras.cell(row=r_idx, column=9)
    c_ra7.value = f"=AVERAGE('2º Trimestre'!G{r_idx}, '2º Trimestre'!H{r_idx}, '2º Trimestre'!I{r_idx})"
    c_ra7.alignment = ALIGN_CENTER
    c_ra7.border = CELL_BORDER
    c_ra7.fill = row_fill
    c_ra7.font = FONT_BODY
    c_ra7.number_format = "0.00"
    
    # RA8 (Col J)
    c_ra8 = ws_ras.cell(row=r_idx, column=10)
    c_ra8.value = f"=AVERAGE('2º Trimestre'!F{r_idx}, '2º Trimestre'!H{r_idx}, '2º Trimestre'!I{r_idx})"
    c_ra8.alignment = ALIGN_CENTER
    c_ra8.border = CELL_BORDER
    c_ra8.fill = row_fill
    c_ra8.font = FONT_BODY
    c_ra8.number_format = "0.00"
    
    # Nota Final Ordinaria
    c_tot = ws_ras.cell(row=r_idx, column=11)
    c_tot.value = f"=C{r_idx}*0.22 + D{r_idx}*0.16 + E{r_idx}*0.20 + F{r_idx}*0.11 + G{r_idx}*0.04 + H{r_idx}*0.07 + I{r_idx}*0.10 + J{r_idx}*0.10"
    c_tot.alignment = ALIGN_CENTER
    c_tot.border = CELL_BORDER
    c_tot.fill = FILL_TOTAL
    c_tot.font = FONT_BODY_BOLD
    c_tot.number_format = "0.00"

# Average Row
ws_ras.row_dimensions[row_avg].height = 24
ws_ras.merge_cells(f"A{row_avg}:B{row_avg}")
c_avg_lblr = ws_ras.cell(row=row_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lblr.font = FONT_HEADER_DARK
c_avg_lblr.alignment = ALIGN_CENTER
c_avg_lblr.fill = FILL_TOTAL
c_avg_lblr.border = TOTAL_BORDER
ws_ras.cell(row=row_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 12):
    col_let = get_column_letter(col_idx)
    c_avg = ws_ras.cell(row=row_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}9:{col_let}23)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_ras.conditional_formatting.add("K9:K23", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_ras.conditional_formatting.add("K9:K23", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 5: ESTRUCTURA, MATRIZ Y PONDERACIONES
# =============================================================
ws_mat = wb.create_sheet(title="Estructura y Ponderaciones")
ws_mat.views.sheetView[0].showGridLines = True

ws_mat.merge_cells("A1:F1")
cell_tmat = ws_mat["A1"]
cell_tmat.value = "MATRIZ DE RESULTADOS DE APRENDIZAJE, CRITERIOS Y UNIDADES DIDÁCTICAS"
cell_tmat.font = FONT_TITLE
cell_tmat.fill = FILL_NAVY
cell_tmat.alignment = ALIGN_CENTER
ws_mat.row_dimensions[1].height = 36

headers_mat = [
    ("Resultado de Aprendizaje (RA)", 28),
    ("Pond. RA", 10),
    ("Criterios de Evaluación (CE)", 35),
    ("Unidades Didácticas (UD)", 22),
    ("Actividades e Instrumentos de Evaluación", 32),
    ("Trimestre", 12)
]

ws_mat.row_dimensions[3].height = 28
for col_idx, (h_text, width) in enumerate(headers_mat, start=1):
    col_let = get_column_letter(col_idx)
    ws_mat.column_dimensions[col_let].width = width
    cell = ws_mat.cell(row=3, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    cell.fill = FILL_BLUE_HEADER

matrix_data = [
    ("RA1: Confecciona interfaces gráficas aplicando metodologías de diseño y usabilidad.", "22%", "CE1.a a CE1.f:\nElementos UI, UX, Wireframes, Figma, Guías estilo, CSS Grid, Tailwind.", "UD00, UD01, UD04, UD05, UD06, UD07, UD08, UD13, UD15", "Actividad 1 (Figma), Actividad 3 (Tailwind/Grid), Examen T1, GesFlow", "T1 / T2"),
    ("RA2: Confecciona interfaces de usuario utilizando interfaces naturales (NUI, voz, gestos).", "16%", "CE2.a a CE2.e:\nConceptos NUI, Web Speech API, MediaPipe gestos, WebXR / 3D, barreras.", "UD03", "Actividad 2 (NUI & Speech), Examen T1, GesFlow", "T1"),
    ("RA3: Crea componentes visuales estándar y reutilizables en librerías.", "20%", "CE3.a a CE3.f:\nAngular Standalone, Atomic Design, Signals, Directivas, Storybook, Forms reactivos.", "UD07, UD09, UD10, UD11, UD12, UD13, UD14, UD15", "Actividad 5 (Angular), Actividad 6 (Forms), Actividad 7 (Storybook), GesFlow", "T1 / T2"),
    ("RA4: Diseña interfaces accesibles y amigables verificando normativas.", "11%", "CE4.a a CE4.e:\nWCAG 2.2 (A/AA/AAA), WAI-ARIA, navegación teclado, contraste, Axe Core, NVDA.", "UD02, UD08, UD12", "Actividad 4 (A11y), Actividad 6 (Forms A11y), Auditoría GesFlow", "T1 / T2"),
    ("RA5: Crea informes y cuadros de mando interactivos integrando datos y gráficos.", "4%", "CE5.a a CE5.d:\njsPDF, SheetJS (XLSX), Dashboards con Chart.js, filtros y exportación.", "UD16, UD17", "Actividad 8 (Informes & Dashboards), Módulo Informes GesFlow", "T2"),
    ("RA6: Elabora la documentación técnica y de usuario de la interfaz.", "7%", "CE6.a a CE6.d:\nManuales usuario, arquitectura, Compodoc/Typedoc, Zensical/Markdown.", "UD14, UD18", "Actividad 7 (Storybook Doc), Manual GesFlow, Documentación Zensical", "T2"),
    ("RA7: Prepara aplicaciones para su distribución empaquetando para escritorio.", "10%", "CE7.a a CE7.e:\nElectron, IPC seguro (Preload/Context Isolation), Forge/Builder, instaladores.", "UD20, UD21", "Actividad 10 (Electron), Empaquetado GesFlow Desktop", "T2"),
    ("RA8: Realiza pruebas unitarias, de integración y E2E evaluando robustez.", "10%", "CE8.a a CE8.e:\nEstrategia de tests, Vitest, Testing Library, Playwright E2E, Core Web Vitals.", "UD19", "Actividad 9 (Vitest/Playwright), Suite Pruebas GesFlow", "T2")
]

for r_idx, row_items in enumerate(matrix_data, start=4):
    ws_mat.row_dimensions[r_idx].height = 42
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    for c_idx, val in enumerate(row_items, start=1):
        cell = ws_mat.cell(row=r_idx, column=c_idx, value=val)
        cell.font = FONT_BODY
        cell.border = CELL_BORDER
        cell.fill = row_fill
        if c_idx == 1:
            cell.font = FONT_BODY_BOLD
            cell.alignment = ALIGN_LEFT
        elif c_idx == 2:
            cell.font = FONT_BODY_BOLD
            cell.alignment = ALIGN_CENTER
            cell.fill = FILL_TOTAL
        elif c_idx == 6:
            cell.alignment = ALIGN_CENTER
        else:
            cell.alignment = ALIGN_LEFT

# Total Weights Row
row_tot_mat = len(matrix_data) + 4
ws_mat.row_dimensions[row_tot_mat].height = 24
ws_mat.cell(row=row_tot_mat, column=1, value="TOTAL PONDERACIÓN DEL MÓDULO").font = FONT_HEADER_DARK
ws_mat.cell(row=row_tot_mat, column=1).alignment = ALIGN_RIGHT
ws_mat.cell(row=row_tot_mat, column=1).fill = FILL_TOTAL
ws_mat.cell(row=row_tot_mat, column=1).border = TOTAL_BORDER

c_sum_pond = ws_mat.cell(row=row_tot_mat, column=2, value="100%")
c_sum_pond.font = FONT_KPI_VAL
c_sum_pond.alignment = ALIGN_CENTER
c_sum_pond.fill = FILL_GREEN_LIGHT
c_sum_pond.border = TOTAL_BORDER

for c in range(3, 7):
    cc = ws_mat.cell(row=row_tot_mat, column=c, value="")
    cc.fill = FILL_TOTAL
    cc.border = TOTAL_BORDER


# =============================================================
# SHEET 6: SEGUIMIENTO DUAL Y EXTRAORDINARIA
# =============================================================
ws_dual = wb.create_sheet(title="Seguimiento Dual y Extraord")
ws_dual.views.sheetView[0].showGridLines = True

ws_dual.merge_cells("A1:J1")
cell_tdual = ws_dual["A1"]
cell_tdual.value = "FASE DE FORMACIÓN DUAL EN EMPRESA (T3 - 86 h) Y CONVOCATORIA EXTRAORDINARIA"
cell_tdual.font = FONT_TITLE
cell_tdual.fill = FILL_NAVY
cell_tdual.alignment = ALIGN_CENTER
ws_dual.row_dimensions[1].height = 36

ws_dual.merge_cells("A2:J2")
cell_subdual = ws_dual["A2"]
cell_subdual.value = "Orden de 26 de septiembre de 2025 (Dual Andalucía) | Periodo en Empresa: Marzo a Junio 2026"
cell_subdual.font = Font(name="Segoe UI", size=10, italic=True, color="CBD5E1")
cell_subdual.fill = FILL_SUBHEADER
cell_subdual.alignment = ALIGN_CENTER
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
    
    # Nº
    c1 = ws_dual.cell(row=r_idx, column=1, value=r_idx-4)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    # Nombre
    c2 = ws_dual.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # Nota Ordinaria (Pulled from Dashboard)
    c3 = ws_dual.cell(row=r_idx, column=3)
    c3.value = f"='Resumen y Calificaciones'!M{r_idx+4}"
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
    c7 = ws_dual.cell(row=r_idx, column=7, value=f'=IF(C{r_idx}>=5, "APTO", "PENDIENTE")')
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
    
    # Nota Extraordinaria (vacío por defecto si aprueba en ordinaria)
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


# -------------------------------------------------------------
# Save Workbook
# -------------------------------------------------------------
output_dir = r"e:\00. Clases\Apuntes\Desarrollo_Interfaces\programación"
os.makedirs(output_dir, exist_ok=True)

excel_path = os.path.join(output_dir, "Hoja_Evaluacion_Seguimiento_DI_2DAM_2025_2026.xlsx")
wb.save(excel_path)

print(f"Hoja de evaluación generada con éxito en:\n{excel_path}")
