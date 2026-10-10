# -*- coding: utf-8 -*-
"""
Script generador de la Programación Didáctica actualizada y completa
del módulo profesional 'Desarrollo de Interfaces' (Código 0488) - 2º DAM
Comunidad Autónoma de Andalucía.

Genera:
1. programación/Desarrollo_de_interfaces_2DAM_2025-2026.docx (Actualización directa)
2. programación/Programacion_Didactica_DI_2DAM_Andalucia.docx (Copia formal)
3. programación/Programacion_Didactica_DI_2DAM.md (Versión Markdown en programación)
4. docs/programacion-didactica.md (Integración en portal de apuntes web)
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def build_di_dam_programacion():
    doc = docx.Document()
    
    # Page setup - Margins (Normal 2.5 cm = ~0.98 inches)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.9)
        section.bottom_margin = Inches(0.9)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
        
    # Styles config
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
    
    # Helper functions
    def set_cell_background(cell, fill_hex):
        tcPr = cell._element.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
        tcPr = cell._element.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, color="D1D5DB", sz="4", val="single"):
        tblPr = table._element.xpath('w:tblPr')
        if tblPr:
            borders = parse_xml(
                f'<w:tblBorders {nsdecls("w")}>'
                f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:left w:val="none"/>'
                f'<w:right w:val="none"/>'
                f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:insideV w:val="none"/>'
                f'</w:tblBorders>'
            )
            tblPr[0].append(borders)

    def add_callout(text_list, title="MARCO DESTACADO", bg_hex="F0FDF4", border_hex="16A34A", text_color=(0x16, 0x65, 0x34)):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        table.columns[0].width = Inches(6.7)
        
        cell = table.cell(0, 0)
        set_cell_background(cell, bg_hex)
        set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
        
        tcPr = cell._element.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:top w:val="none"/>'
            f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/>'
            f'<w:bottom w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        run_title = p.add_run(f"📌 {title}\n")
        run_title.bold = True
        run_title.font.name = "Calibri"
        run_title.font.size = Pt(10)
        run_title.font.color.rgb = RGBColor(*text_color)
        
        for idx, line in enumerate(text_list):
            if idx > 0:
                p = cell.add_paragraph()
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.line_spacing = 1.15
            r = p.add_run(line)
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(2)
        p_after.paragraph_format.space_after = Pt(4)

    def heading_1(text):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(14.5)
        r.bold = True
        r.font.color.rgb = RGBColor(0x0F, 0x4C, 0x81) # Deep Indigo
        return p

    def heading_2(text):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(12)
        r.bold = True
        r.font.color.rgb = RGBColor(0x0D, 0x94, 0x88) # Teal / Cyan
        return p

    def heading_3(text):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10.5)
        r.bold = True
        r.font.color.rgb = RGBColor(0x37, 0x41, 0x51) # Slate
        return p

    def body_p(text, bold_prefix=None, space_after=4):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = "Calibri"
            r_pre.font.size = Pt(10)
            r_pre.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        return p

    def bullet_p(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = "Calibri"
            r_pre.font.size = Pt(10)
            r_pre.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        return p

    def styled_table(headers, data, col_widths=None, header_bg="0F4C81", header_fg=(0xFF, 0xFF, 0xFF)):
        table = doc.add_table(rows=len(data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        
        # Header
        hdr_cells = table.rows[0].cells
        for i, title in enumerate(headers):
            hdr_cells[i].text = title
            set_cell_background(hdr_cells[i], header_bg)
            set_cell_margins(hdr_cells[i], top=120, bottom=120, left=140, right=140)
            p = hdr_cells[i].paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            for run in p.runs:
                run.font.name = "Calibri"
                run.font.size = Pt(9.5)
                run.font.bold = True
                run.font.color.rgb = RGBColor(*header_fg)
                
        # Data rows
        for row_idx, row_data in enumerate(data):
            row_cells = table.rows[row_idx + 1].cells
            bg_color = "F9FAFB" if row_idx % 2 == 1 else "FFFFFF"
            for col_idx, cell_value in enumerate(row_data):
                row_cells[col_idx].text = str(cell_value)
                set_cell_background(row_cells[col_idx], bg_color)
                set_cell_margins(row_cells[col_idx], top=100, bottom=100, left=140, right=140)
                p = row_cells[col_idx].paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.1
                for run in p.runs:
                    run.font.name = "Calibri"
                    run.font.size = Pt(9)
                    run.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
                    
        # Column widths
        if col_widths:
            for i, col in enumerate(table.columns):
                w = Inches(col_widths[i])
                for cell in col.cells:
                    cell.width = w
                    
        set_table_borders(table)
        
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(2)
        p_after.paragraph_format.space_after = Pt(4)
        return table

    # -------------------------------------------------------------
    # PORTADA Y ENCABEZADO
    # -------------------------------------------------------------
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(24)
    p_title.paragraph_format.space_after = Pt(4)
    p_title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_title.add_run("PROGRAMACIÓN DIDÁCTICA")
    r.bold = True
    r.font.size = Pt(22)
    r.font.color.rgb = RGBColor(0x0F, 0x4C, 0x81)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(8)
    p_sub.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Módulo Profesional: Desarrollo de Interfaces (Código 0488)")
    r_sub.bold = True
    r_sub.font.size = Pt(13)
    r_sub.font.color.rgb = RGBColor(0x0D, 0x94, 0x88)

    p_cycles = doc.add_paragraph()
    p_cycles.paragraph_format.space_before = Pt(0)
    p_cycles.paragraph_format.space_after = Pt(16)
    p_cycles.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_c = p_cycles.add_run("Ciclo Formativo de Grado Superior: Desarrollo de Aplicaciones Multiplataforma (DAM)\nSegundo Curso · Familia Profesional: Informática y Comunicaciones\nComunidad Autónoma de Andalucía · Curso Académico 2025 / 2026")
    r_c.font.size = Pt(11)
    r_c.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    # Tabla Ficha Técnica del Módulo
    info_headers = ["Elemento", "Especificación y Datos del Módulo"]
    info_data = [
        ["Denominación oficial", "Desarrollo de Interfaces"],
        ["Código oficial del módulo", "0488 (Real Decreto 450/2010, Real Decreto 686/2010 y Orden de 16 de junio de 2011)"],
        ["Ciclo formativo y curso", "2º curso de Técnico Superior en Desarrollo de Aplicaciones Multiplataforma (DAM)"],
        ["Carga horaria total", "210 horas totales (6 horas semanales en periodo lectivo en centro + fase dual en empresa)"],
        ["Equivalencia crediticia", "10 créditos ECTS (Grado Superior)"],
        ["Régimen de impartición", "Formación Profesional Grado D - Régimen Dual General (400 h totales de empresa en 2º curso, con 86 h vinculadas a DI)"],
        ["Departamento didáctico", "Departamento de Informática y Comunicaciones"],
        ["Repositorio y Materiales de aula", "Carpeta digital del módulo: 23 unidades temáticas de apuntes y proyecto integral GesFlow en docs/"]
    ]
    styled_table(info_headers, info_data, col_widths=[2.3, 4.4], header_bg="0F4C81")

    # -------------------------------------------------------------
    # 1. INTRODUCCIÓN Y JUSTIFICACIÓN PEDAGÓGICA
    # -------------------------------------------------------------
    heading_1("1. INTRODUCCIÓN Y JUSTIFICACIÓN PEDAGÓGICA DEL MÓDULO")
    body_p("El módulo profesional de Desarrollo de Interfaces (Código 0488) se imparte en el segundo curso del Ciclo Formativo de Grado Superior de Desarrollo de Aplicaciones Multiplataforma (DAM), con una carga lectiva de 210 horas totales (a razón de 6 horas semanales durante el periodo lectivo en el centro educativo complementado con la fase de formación en empresa).")
    body_p("En la ingeniería de software multiplataforma moderna, el desarrollo de interfaces abarca desde la concepción UX y diseño en Figma, pasando por la creación de componentes visuales reactivos y accesibles, la integración de Interfaces Naturales de Usuario (NUI: voz, visión por computador, gestos y realidad aumentada), hasta la generación de informes empresariales, la construcción de paneles de control (dashboards), el testing automatizado, la documentación técnica y el empaquetado/distribución de aplicaciones de escritorio multiplataforma (Electron/Angular).")

    add_callout([
        "El módulo capacita al futuro Técnico Superior en DAM para:",
        "1. Diseñar interfaces y sistemas de diseño profesionales en Figma con Auto Layout y Design Tokens sincronizados con el código.",
        "2. Maquetar con HTML5 semántico, CSS moderno avanzado, Flexbox, Grid y frameworks utility-first (Tailwind CSS 4).",
        "3. Desarrollar componentes visuales reutilizables y reactivos mediante Angular Standalone, Signals, Reactive Forms y documentarlos en Storybook.",
        "4. Implementar Interfaces Naturales de Usuario (NUI) con reconocimiento de voz (Web Speech API), visión/gestos (MediaPipe/TensorFlow.js) y realidad aumentada (WebXR/Three.js).",
        "5. Garantizar la accesibilidad universal (WCAG 2.2 / WAI-ARIA / RD 1112/2018) y usabilidad (Heurísticas de Nielsen, ISO 9241-210 y SUS).",
        "6. Generar informes empresariales dinámicos (PDFMake, jsPDF, exportación Excel/CSV) y cuadros de mando interactivos (Chart.js, ApexCharts).",
        "7. Crear aplicaciones de escritorio multiplataforma con Electron + Angular, ejecutando planes de pruebas (Playwright/Jest) y empaquetando instaladores nativos (NSIS, deb, DMG) con CI/CD."
    ], title="Propósito Formativo y Competencial de Desarrollo de Interfaces")

    body_p("La programación didáctica está compaginada al 100% con los materiales preparados en la carpeta docs/ (23 unidades de apuntes teóricos, código fuente y proyecto final integrador GesFlow).")

    # -------------------------------------------------------------
    # 2. MARCO NORMATIVO VIGENTE
    # -------------------------------------------------------------
    heading_1("2. MARCO NORMATIVO VIGENTE")
    body_p("La programación didáctica se fundamenta y ajusta rigurosamente a la siguiente jerarquía normativa estatal, autonómica andaluza y sectorial:")

    heading_2("2.1 Normativa General del Sistema Educativo y Formación Profesional")
    bullet_p("Garantiza el derecho a la educación y el libre desarrollo de la personalidad.", "Constitución Española de 1978 (Artículo 27): ")
    bullet_p("Marco regulador de las enseñanzas no universitarias, con las modificaciones de la Ley Orgánica 3/2020 (LOMLOE) en inclusión, digitalización y diseño universal.", "Ley Orgánica 2/2006, de 3 de mayo, de Educación (LOE / LOMLOE): ")
    bullet_p("Establece el marco legal unificado del Sistema de FP y el carácter dual de las ofertas formativas de Grado D.", "Ley Orgánica 3/2022, de 31 de marzo, de ordenación e integración de la FP: ")
    bullet_p("Desarrolla la ordenación del Sistema de FP (estructura de Grados D, régimen dual y resultados de aprendizaje).", "Real Decreto 659/2023, de 18 de julio: ")
    bullet_p("Establece el título de Técnico Superior en Desarrollo de Aplicaciones Multiplataforma y fija sus enseñanzas mínimas.", "Real Decreto 450/2010 / Real Decreto 686/2010: ")
    bullet_p("Actualiza el título de Técnico Superior en DAM, modernizando los Resultados de Aprendizaje de Desarrollo de Interfaces (incorporando formalmente las NUI con IA, reconocimiento de voz y movimiento, y frameworks modernos).", "Real Decreto 405/2023, de 29 de mayo (BOE-A-2023-13221): ")
    bullet_p("Actualiza los títulos de FP de grado superior, adaptando la ordenación modular, IPE II e integrando la formación en empresa dual.", "Real Decreto 500/2024, de 21 de mayo (BOE-A-2024-10684): ")

    heading_2("2.2 Normativa Autonómica de la Comunidad Autónoma de Andalucía")
    bullet_p("Garantizan el derecho a la educación permanente y la vinculación de la FP con el tejido socioproductivo andaluz.", "Estatuto de Autonomía para Andalucía (Ley Orgánica 2/2007) - Artículos 21 y 52: ")
    bullet_p("Marco legal educativo propio de Andalucía.", "Ley 17/2007, de 10 de diciembre, de Educación de Andalucía (LEA): ")
    bullet_p("Regula la ordenación del Sistema de Formación Profesional en Andalucía, estableciendo el régimen dual y la autonomía pedagógica de los centros docentes (deroga el Decreto 436/2008).", "Decreto 104/2024, de 28 de mayo: ")
    bullet_p("Regula con carácter preceptivo la evaluación criterial, continua, formativa y colegiada en Grados D y E en Andalucía (deroga la Orden de 29 de septiembre de 2010).", "Orden de 18 de septiembre de 2025: ")
    bullet_p("Regula la organización y desarrollo de la fase de formación en empresa u organismo equiparado en los centros docentes andaluces.", "Orden de 26 de septiembre de 2025: ")
    bullet_p("Desarrolla el currículo del título de Técnico Superior en DAM en la Comunidad Autónoma de Andalucía.", "Orden de 16 de junio de 2011: ")
    bullet_p("Reglamento Orgánico de los IES y normas de organización y funcionamiento de centros docentes en Andalucía.", "Decreto 327/2010, de 13 de julio, y Orden de 20 de agosto de 2010: ")

    heading_2("2.3 Normativa Específica de Accesibilidad, Propiedad Intelectual y Protección de Datos")
    bullet_p("Regula la accesibilidad obligatoria de sitios web y aplicaciones para dispositivos móviles y servicios de interés general (trasposición de la Directiva UE 2016/2102).", "Real Decreto 1112/2018, de 7 de septiembre (Accesibilidad Web y Apps): ")
    bullet_p("Trasposición de directivas europeas en materia de accesibilidad de productos y servicios (Acta Europea de Accesibilidad).", "Ley 11/2023, de 8 de mayo: ")
    bullet_p("Regula los derechos de autor, explotación de software, componentes y licencias de distribución (Creative Commons, GPL, MIT, Apache).", "Real Decreto Legislativo 1/1996 (Ley de Propiedad Intelectual - TRLPI): ")
    bullet_p("Regulan la privacidad por diseño, el tratamiento lícito de datos y la garantía de derechos digitales en interfaces y aplicaciones de gestión.", "Reglamento (UE) 2016/679 (RGPD) y Ley Orgánica 3/2018 (LOPDGDD): ")

    # -------------------------------------------------------------
    # 3. CONTEXTO DEL GRUPO DE ALUMNADO
    # -------------------------------------------------------------
    heading_1("3. CONTEXTO DEL GRUPO DE ALUMNADO (2º DAM)")
    body_p("El grupo de 2º curso de Desarrollo de Aplicaciones Multiplataforma está integrado por 11 alumnos/as procedentes de diversos municipios de las provincias de Jaén y Córdoba (Martos, Torredonjimeno, Torredelcampo, Escañuela, Jaén y Priego de Córdoba):")
    bullet_p("Edades comprendidas entre 20 y 30 años, con perfiles orientados al desarrollo de aplicaciones empresariales, móviles y multiplataforma.", "Distribución etaria: ")
    bullet_p("10 alumnos proceden de la promoción directa de 1º DAM en el mismo centro educativo, contando con una base homogénea en programación orientada a objetos (Java), bases de datos y lenguajes de marcas. 1 alumno proviene de matrícula directa con estudios anteriores de DAM.", "Trayectoria académica: ")
    bullet_p("El grupo demuestra buen clima de convivencia y colaboración. Existen perfiles de liderazgo técnico que dinamizan el avance colectivo en las actividades cooperativas y de laboratorio.", "Dinámica de aula: ")
    bullet_p("No se registran dictámenes formales de NEAE en el expediente de orientación. Se aplican estrategias basadas en el Diseño Universal para el Aprendizaje (DUA) para atender la diversidad de ritmos de aprendizaje.", "Atención a la diversidad: ")

    # -------------------------------------------------------------
    # 4. OBJETIVOS GENERALES Y COMPETENCIAS
    # -------------------------------------------------------------
    heading_1("4. OBJETIVOS GENERALES Y COMPETENCIAS DEL TÍTULO")
    body_p("De conformidad con la Orden de 16 de junio de 2011 y el Real Decreto 450/2010 / RD 405/2023, el módulo de Desarrollo de Interfaces contribuye a los siguientes objetivos generales y competencias:")

    heading_2("4.1 Objetivos Generales del Ciclo Vinculados al Módulo")
    bullet_p("Seleccionar y emplear lenguajes, herramientas y librerías para desarrollar interfaces multiplataforma con acceso a bases de datos (e).", "Desarrollo con acceso a datos: ")
    bullet_p("Planificar e implementar sistemas de formularios e informes para desarrollar aplicaciones de gestión (f).", "Formularios e informes: ")
    bullet_p("Manipular e integrar contenidos gráficos y componentes multimedia siguiendo manuales de estilo (g).", "Multimedia y estilos: ")
    bullet_p("Emplear herramientas visuales y componentes interactivos verificando usabilidad y accesibilidad (h).", "Interfaces gráficas y usabilidad: ")
    bullet_p("Crear ayudas generales, sensibles al contexto, tutoriales y manuales de usuario (k, l).", "Documentación y ayuda: ")
    bullet_p("Seleccionar técnicas y herramientas para empaquetar, desplegar y distribuir aplicaciones (m, s).", "Empaquetado y distribución: ")
    bullet_p("Verificar los componentes software desarrollados completando un plan de pruebas (r).", "Plan de pruebas: ")
    bullet_p("Identificar cambios tecnológicos para mantener el espíritu de innovación continua (w).", "Innovación y actualización: ")

    heading_2("4.2 Competencias Profesionales, Personales y Sociales")
    bullet_p("Gestionar entornos de desarrollo, frameworks y herramientas de frontend/escritorio (d).", "Entornos y herramientas: ")
    bullet_p("Desarrollar interfaces gráficas de usuario interactivas, accesibles y amigables implementando componentes visuales estándar o personalizados (h).", "Desarrollo de UI interactiva: ")
    bullet_p("Implementar sistemas completos de formularios, informes incrustados y cuadros de mando para gestión integral de información (f).", "Gestión de información y dashboards: ")
    bullet_p("Crear ayudas interactivas, documentación de APIs y manuales técnicos y de usuario (k, l).", "Documentación técnica: ")
    bullet_p("Empaquetar aplicaciones multiplataforma con asistentes autoinstalables, firmas y actualización continua (m, s).", "Distribución y empaquetado: ")
    bullet_p("Diseñar y ejecutar planes rigurosos de pruebas unitarias, de integración, rendimiento y seguridad (r).", "Testing y calidad: ")

    # -------------------------------------------------------------
    # 5. RESULTADOS DE APRENDIZAJE Y CRITERIOS DE EVALUACIÓN
    # -------------------------------------------------------------
    heading_1("5. RESULTADOS DE APRENDIZAJE Y CRITERIOS DE EVALUACIÓN (RD 405/2023)")
    body_p("A continuación se detallan los 8 Resultados de Aprendizaje oficiales fijados por el Real Decreto 405/2023 y la Orden de 16 de junio de 2011 para el módulo de Desarrollo de Interfaces, junto con sus Criterios de Evaluación y el peso porcentual asignado a cada uno:")

    ra_headers = ["RA", "Resultado de Aprendizaje Oficial", "Criterios de Evaluación Oficiales (CE)", "Pond. Total"]
    ra_data = [
        [
            "RA1",
            "Genera interfaces gráficos de usuario mediante editores visuales utilizando las funcionalidades del editor y adaptando el código generado.",
            "a) Se han analizado herramientas y librerías disponibles (2%).\nb) Se ha creado un interfaz gráfico con editor visual (2%).\nc) Se han ubicado componentes con funciones del editor (2%).\nd) Se han modificado propiedades de componentes (2%).\ne) Se ha analizado el código generado (3%).\nf) Se ha modificado el código generado (3%).\ng) Se han asociado acciones a eventos (4%).\nh) Se ha desarrollado una aplicación con interfaz gráfico (4%).",
            "22 %\n(Pond. diferenciada)"
        ],
        [
            "RA2",
            "Genera interfaces naturales de usuario utilizando herramientas visuales.",
            "a) Se han identificado herramientas de aprendizaje automático para UI (2%).\nb) Se ha creado una interfaz natural de usuario (2%).\nc) Se ha utilizado reconocimiento de voz para acciones (2%).\nd) Se ha incorporado detección del movimiento del cuerpo (2%).\ne) Se han integrado elementos de detección de partes del cuerpo (4%).\nf) Se ha integrado realidad aumentada en interfaces (4%).",
            "16 %\n(Pond. diferenciada)"
        ],
        [
            "RA3",
            "Crea componentes visuales valorando y empleando herramientas específicas.",
            "a) Se han identificado herramientas de diseño y prueba (2%).\nb) Se han creado componentes visuales (2%).\nc) Se han definido métodos y propiedades por defecto (2%).\nd) Se han asociado eventos y acciones (2%).\ne) Se han realizado pruebas unitarias sobre componentes (2%).\nf) Se han documentado los componentes creados (2%).\ng) Se han empaquetado componentes (4%).\nh) Se han programado aplicaciones con los componentes (4%).",
            "20 %\n(Pond. diferenciada)"
        ],
        [
            "RA4",
            "Diseña interfaces gráficas identificando y aplicando criterios de usabilidad y accesibilidad.",
            "a) Se han identificado estándares de usabilidad y accesibilidad (1%).\nb) Se ha valorado la importancia de los estándares (1%).\nc) Se han creado menús siguiendo estándares (1%).\nd) Se han distribuido acciones en menús y toolbars (1%).\ne) Se han distribuido controles en la interfaz (1%).\nf) Se ha utilizado el control más apropiado (1%).\ng) Se ha diseñado el aspecto atendiendo a legibilidad (1%).\nh) Se han verificado mensajes en claridad y extensión (2%).\ni) Se han evaluado usabilidad y accesibilidad con pruebas (2%).",
            "11 %\n(Pond. diferenciada)"
        ],
        [
            "RA5",
            "Crea informes evaluando y utilizando herramientas gráficas.",
            "a) Se ha establecido la estructura del informe (0,5%).\nb) Se han generado informes básicos con asistentes (0,5%).\nc) Se han establecido filtros sobre valores (0,5%).\nd) Se han incluido valores calculados y totales (0,5%).\ne) Se han incluido gráficos generados a partir de datos (0,5%).\nf) Se han utilizado herramientas para generar código (0,5%).\ng) Se ha modificado el código de informes (0,5%).\nh) Se ha desarrollado una aplicación con informes incrustados (0,5%).",
            "4 %\n(0,5% / CE)"
        ],
        [
            "RA6",
            "Documenta aplicaciones seleccionando y utilizando herramientas específicas.",
            "a) Se han identificado sistemas de generación de ayudas (1%).\nb) Se han generado ayudas en formatos habituales (1%).\nc) Se han generado ayudas sensibles al contexto (1%).\nd) Se ha documentado la información persistente (1%).\ne) Se ha confeccionado el manual de usuario y referencia (1%).\nf) Se han confeccionado manuales de instalación y admin (1%).\ng) Se han confeccionado tutoriales (1%).",
            "7 %\n(1% / CE)"
        ],
        [
            "RA7",
            "Prepara aplicaciones para su distribución evaluando y utilizando herramientas específicas.",
            "a) Se han empaquetado componentes requeridos (1%).\nb) Se ha personalizado el asistente de instalación (1%).\nc) Se han generado paquetes con el entorno de desarrollo (1%).\nd) Se han generado paquetes con herramientas externas (1%).\ne) Se han firmado digitalmente las aplicaciones (1%).\nf) Se han generado paquetes en modo desatendido (1%).\ng) Se ha preparado la desinstalación correcta (2%).\nh) Se ha preparado la distribución por diversos canales (2%).",
            "10 %\n(Pond. diferenciada)"
        ],
        [
            "RA8",
            "Evalúa el funcionamiento de aplicaciones diseñando y ejecutando pruebas.",
            "a) Se ha establecido una estrategia de pruebas (1%).\nb) Se han realizado pruebas de integración (1%).\nc) Se han realizado pruebas de regresión (1%).\nd) Se han realizado pruebas de volumen y estrés (1%).\ne) Se han realizado pruebas de seguridad (2%).\nf) Se han realizado pruebas de uso de recursos (2%).\ng) Se ha documentado la estrategia y resultados (2%).",
            "10 %\n(Pond. diferenciada)"
        ]
    ]
    styled_table(ra_headers, ra_data, col_widths=[0.6, 2.2, 3.2, 0.7], header_bg="0F4C81")

    # -------------------------------------------------------------
    # 6. ORGANIZACIÓN Y SECUENCIACIÓN DE UNIDADES DIDÁCTICAS
    # (COMPAGINADAS CON LOS MATERIALES DE DOCS/)
    # -------------------------------------------------------------
    heading_1("6. SECUENCIACIÓN DIDÁCTICA Y COMPAGINACIÓN CON LOS APUNTES DEL MÓDULO")
    body_p("El módulo se estructura pedagógicamente en 23 Unidades Didácticas (UD) organizadas en dos trimestres lectivos en centro educativo (124 horas lectivas presenciales) que culminan en el Proyecto Final Integrador «GesFlow» y se complementan con las 86 horas de formación dual en empresa (210 h totales):")

    heading_2("6.1 TRIMESTRE 1 (68 horas lectivas en centro)")
    bullet_p("Tipologías de interfaz (GUI, CLI, VUI, NUI, TUI), evolución histórica, UX vs UI, multiplataforma (PWA, Electron, nativo), ecosistema Angular y UCD (ISO 9241-210). Material: docs/index.md. RAs: RA1, RA4.", "UD 01. Introducción al desarrollo de interfaces (6 h): ")
    bullet_p("Diseño Centrado en el Usuario (UCD), las 10 heurísticas de Nielsen, arquitectura de información, flujos de usuario, principios visuales Gestalt y UX writing. Material: docs/01-ux.md. RAs: RA4.", "UD 02. Principios de UX para desarrolladores (10 h): ")
    bullet_p("Fundamentos de accesibilidad, WCAG 2.1/2.2 (A/AA/AAA), principios POUR, WAI-ARIA, accesibilidad en Angular CDK y herramientas de test (axe, Lighthouse, WAVE). Material: docs/02-accesibilidad.md. RAs: RA4.", "UD 03. Accesibilidad web (WCAG) (10 h): ")
    bullet_p("Modalidades NUI: reconocimiento de voz con Web Speech API, detección de gestos/movimiento corporal con MediaPipe/TensorFlow.js y Realidad Aumentada con WebXR y Three.js. Material: docs/03-interfaces-naturales.md. RAs: RA2.", "UD 04. Interfaces naturales de usuario (NUI) (8 h): ")
    bullet_p("Espacio de trabajo, frames, Auto Layout avanzado, variables de diseño, componentes y variantes, design tokens, plugins y Dev Mode para handoff. Material: docs/04-figma.md. RAs: RA1, RA3.", "UD 05. Diseño de interfaces con Figma (14 h): ")
    bullet_p("Flexbox y CSS Grid con clases utility de Tailwind, equivalencias con layouts clásicos de escritorio (VBox, HBox, GridPane, BorderPane) y container queries. Material: docs/05-layouts-modernos.md. RAs: RA1, RA4.", "UD 06. Layouts modernos para interfaces web (8 h): ")
    bullet_p("Filosofía utility-first, configuración de Tailwind 4 con @theme en Angular/Vite, clases utility clave, dark mode y motor JIT. Material: docs/06-tailwindcss4.md. RAs: RA1, RA4.", "UD 07. Tailwind CSS 4 en el desarrollo de interfaces (12 h): ")

    heading_2("6.2 TRIMESTRE 2 (56 horas lectivas en centro + Proyecto GesFlow)")
    bullet_p("Sistema completo de botones, tarjetas, tablas de datos, modales accesibles con Angular CDK y barras de navegación adaptables. Material: docs/07-componentes-tailwind.md. RAs: RA1, RA3.", "UD 08. Implementación de componentes con Tailwind CSS (12 h): ")
    bullet_p("Mobile First en escritorio/web, breakpoints Tailwind, BreakpointObserver (Angular CDK) con signals y responsive en Electron. Material: docs/08-responsive-design.md. RAs: RA1, RA4.", "UD 09. Responsive design en aplicaciones Angular (8 h): ")
    bullet_p("Node.js, npm, Angular Standalone, TypeScript estricto, Angular Signals, Storybook, Electron y tooling profesional. Material: docs/09-ecosistema-frontend.md. RAs: RA1, RA3.", "UD 10. Ecosistema profesional del desarrollo frontend (6 h): ")
    bullet_p("Componentes Standalone, organización por features, patrón Smart vs Presentational, comunicación inputs/outputs/signals y manipulación del DOM reactivo. Material: docs/10-arquitectura-angular.md. RAs: RA1, RA3.", "UD 11. Arquitectura de interfaces con Angular (12 h): ")
    bullet_p("Principios SOLID de UI, catálogo de componentes con Tailwind, proyección ng-content, estados de interfaz (loading, empty, error, data) y accesibilidad. Material: docs/11-componentes-reutilizables.md. RAs: RA3.", "UD 12. Componentes reutilizables (10 h): ")
    bullet_p("Reactive Forms avanzados, validadores síncronos/asíncronos, mensajes contextuales, wizards multipaso y FormArray. Material: docs/12-formularios-interaccion.md. RAs: RA1, RA3, RA4.", "UD 13. Formularios e interacción (10 h): ")
    bullet_p("Atomic Design en Angular, design tokens sincronizados Figma-código y ThemeProvider con signals (claro, oscuro, alto contraste). Material: docs/13-design-systems.md. RAs: RA1, RA3, RA4.", "UD 14. Design systems (8 h): ")
    bullet_p("Configuración en Angular, stories CSF3, addons (Controls, Actions, A11y, Interactions), MDX y Chromatic. Material: docs/14-storybook.md. RAs: RA3, RA6.", "UD 15. Documentación de componentes con Storybook (6 h): ")
    bullet_p("Handoff desde Figma Dev Mode, extracción de tokens a @theme, Atomic Design en Angular y checklist de calidad. Material: docs/15-diseno-a-implementacion.md. RAs: RA1, RA3.", "UD 16. Del diseño a la implementación (10 h): ")
    bullet_p("Generación cliente/servidor con PDFMake, jsPDF y SheetJS (facturas, informes de ventas con gráficos, certificados y CSV/Excel). Material: docs/16-generacion-informes.md. RAs: RA5.", "UD 17. Generación de informes y documentos (8 h): ")
    bullet_p("Principios data-ink ratio, integración de Chart.js y ApexCharts con signals en Angular, tarjetas KPI y exportación. Material: docs/17-dashboards-exportacion-datos.md. RAs: RA5.", "UD 18. Dashboards y visualización de datos (8 h): ")
    bullet_p("Ayudas sensibles al contexto, manuales de usuario/instalación/administración, generadores estáticos (Docusaurus/MkDocs) y TSDoc. Material: docs/18-documentacion-aplicaciones.md. RAs: RA6.", "UD 19. Documentación de aplicaciones (6 h): ")
    bullet_p("Pirámide de pruebas: unitarias en componentes/servicios Angular con mocks, pruebas E2E con Playwright/Cypress y pruebas de carga/seguridad. Material: docs/19-pruebas-de-software.md. RAs: RA8.", "UD 20. Pruebas de software (6 h): ")
    bullet_p("Arquitectura de procesos Main/Renderer, scripts preload, IPC seguro con contextBridge, APIs nativas del SO y Angular+Electron. Material: docs/20-electron.md. RAs: RA1, RA7.", "UD 21. Aplicaciones de escritorio con Electron (8 h): ")
    bullet_p("Configuración de electron-builder, instaladores NSIS/AppImage/deb/DMG, firma de código, autoactualizaciones con electron-updater y CI/CD en GitHub Actions. Material: docs/21-empaquetado-distribucion.md. RAs: RA7.", "UD 22. Empaquetado y distribución de aplicaciones (8 h): ")
    bullet_p("Desarrollo en 9 fases de una aplicación empresarial completa multiplataforma (Angular + Tailwind + Electron + NUI + Informes + Pruebas + Storybook + Distribución) con defensa individual. Material: docs/22-proyecto-final.md. RAs: RA1 a RA8.", "UD 23. Proyecto final integrador «GesFlow» (16 h): ")

    # -------------------------------------------------------------
    # 7. METODOLOGÍA DIDÁCTICA
    # -------------------------------------------------------------
    heading_1("7. METODOLOGÍA DIDÁCTICA Y PRINCIPIOS PEDAGÓGICOS")
    body_p("La metodología de enseñanza se basa en el Aprendizaje Basado en Proyectos (ABP), el enfoque constructivista y el desarrollo iterativo ágil de software multiplataforma:")
    bullet_p("Todo el módulo converge en la construcción progresiva de componentes y módulos que culminan en la aplicación empresarial GesFlow.", "Aprendizaje Basado en Proyectos (ABP): ")
    bullet_p("Sesiones interactivas donde la teoría se traduce en código y componentes ejecutables en tiempo real (Visual Studio Code, Angular CLI, Figma, Electron, Storybook).", "Enfoque Learning by Doing: ")
    bullet_p("Uso estricto de control de versiones con Git/GitHub, linters de accesibilidad (axe/ESLint), tipado estricto en TypeScript y metodologías de diseño atómico.", "Buenas Prácticas Profesionales: ")

    # -------------------------------------------------------------
    # 8. EVALUACIÓN Y CALIFICACIÓN
    # -------------------------------------------------------------
    heading_1("8. EVALUACIÓN, INSTRUMENTOS Y CRITERIOS DE CALIFICACIÓN")
    body_p("Conforme al Decreto 104/2024 y a la Orden de 18 de septiembre de 2025 de la Junta de Andalucía, la evaluación es continua, formativa, criterial e integradora.")

    heading_2("8.1 Instrumentos y Procedimientos de Evaluación")
    bullet_p("Ejercicios de aula, prácticas de diseño en Figma, componentes de Tailwind, integración de NUI y pruebas unitarias (40% de la calificación).", "1. Prácticas y Tareas de Laboratorio por Unidad (40%): ")
    bullet_p("Desarrollo de la aplicación multiplataforma GesFlow (Angular + Tailwind + Electron + Informes + Pruebas) con defensa oral individual (40% de la calificación).", "2. Proyecto Final Integrador «GesFlow» y Defensa Oral (40%): ")
    bullet_p("Pruebas escritas y supuestos prácticos de desarrollo para verificar la asimilación autónoma de los criterios de evaluación (20% de la calificación).", "3. Pruebas Objetivas y Supuestos Prácticos (20%): ")

    heading_2("8.2 Criterios de Calificación y Superación")
    bullet_p("Para superar el módulo profesional, es preceptivo que la media ponderada de los Criterios de Evaluación asociados a cada uno de los 8 Resultados de Aprendizaje (RA1 a RA8) alcance una calificación igual o superior a 5,0 puntos sobre 10.", "Superación Criterial Obligatoria: ")
    bullet_p("La calificación final del módulo será la media aritmética ponderada de todos los criterios evaluados, redondeada a un número entero entre 1 y 10.", "Calificación Final: ")
    bullet_p("Planes de refuerzo continuo para proyectos no superados y convocatoria extraordinaria en junio centrada exclusivamente en los RA suspensos.", "Recuperación y Convocatoria Extraordinaria: ")

    # -------------------------------------------------------------
    # 9. FORMACIÓN EN EMPRESA U ORGANISMO EQUIPARADO (RÉGIMEN DUAL EN 2º DAM)
    # -------------------------------------------------------------
    heading_1("9. FORMACIÓN EN EMPRESA U ORGANISMO EQUIPARADO (RÉGIMEN DUAL EN 2º DAM)")
    body_p("En cumplimiento de la Ley Orgánica 3/2022, el Real Decreto 659/2023, el Decreto 104/2024 y la Orden de 26 de septiembre de 2025 de la Junta de Andalucía, el ciclo de DAM se imparte en modalidad dual general (400 horas totales en empresas en 2º curso):")

    dual_headers = ["Módulo Profesional (2º DAM)", "Horas Totales", "Horas en Centro", "Horas en Empresa (Dual)"]
    dual_data = [
        ["Programación de Servicios y Procesos (PSP)", "105 h", "62 h", "43 h"],
        ["Desarrollo de Interfaces (DI)", "210 h", "124 h", "86 h"],
        ["Programación Multimedia y Dispositivos Móviles (PMDM)", "105 h", "62 h", "43 h"],
        ["Acceso a Datos (AD)", "140 h", "83 h", "57 h"],
        ["Sistemas de Gestión Empresarial (SGE)", "140 h", "83 h", "57 h"],
        ["Módulo Optativo", "105 h", "62 h", "43 h"],
        ["Inglés Profesional", "70 h", "41 h", "29 h"],
        ["Itinerario Personal para la Empleabilidad II (IPE II)", "105 h", "62 h", "43 h"],
        ["TOTAL HORAS 2º CURSO (+70h Proyecto)", "1.050 h", "579 h", "400 h (50 jornadas)"]
    ]
    styled_table(dual_headers, dual_data, col_widths=[2.8, 1.2, 1.3, 1.4], header_bg="0F4C81")

    heading_2("9.1 Resultados de Aprendizaje y Criterios Desarrollados en Empresa")
    body_p("Durante la estancia dual en la empresa colaboradora (86 horas de DI), se desarrollarán y consolidarán especialmente:")
    bullet_p("a) Herramientas de componentes; b) Creación de componentes visuales; d) Eventos y acciones; e) Pruebas unitarias; f) Documentación técnica; h) Programación de interfaces en aplicaciones de producción.", "RA3 (Componentes visuales reutilizables): ")
    bullet_p("c) Menús y navegación estándar; d) Barras de herramientas y acciones; e) Distribución de controles en la UI; f) Uso de controles apropiados; g) Diseño visual legible; h) Claridad de mensajes y feedback.", "RA4 (Usabilidad y accesibilidad en producción): ")
    bullet_p("Empaquetado de aplicaciones multiplataforma, generación de informes de gestión y ejecución de planes de pruebas reales.", "RA5, RA7 y RA8 (Informes, empaquetado y testing): ")

    # -------------------------------------------------------------
    # 10. ATENCIÓN A LA DIVERSIDAD (DUA)
    # -------------------------------------------------------------
    heading_1("10. ATENCIÓN A LA DIVERSIDAD Y DISEÑO UNIVERSAL PARA EL APRENDIZAJE (DUA)")
    body_p("Se aplican los principios del Diseño Universal para el Aprendizaje (DUA):")
    bullet_p("Apuntes modulares completos (`docs/`), código fuente funcional en repositorios, grabaciones y diagramas de flujo interactivos.", "Múltiples formas de representación: ")
    bullet_p("Posibilidad de desarrollar extensiones personalizadas en el proyecto GesFlow, elección de módulos y retos de ampliación multinivel.", "Múltiples formas de acción y expresión: ")
    bullet_p("Conexión con casos de uso empresariales reales y fomento del trabajo cooperativo.", "Múltiples formas de implicación: ")
    bullet_p("Apoyo tutorial guiado para ritmos lentos, retos avanzados (NUI compleja con MediaPipe, Signals reactivos avanzados, micro-frontends en Electron) para alumnado aventajado y seguimiento telemático en plataforma virtual para alumnado con compatibilidad laboral.", "Medidas específicas: ")

    # -------------------------------------------------------------
    # 11. ELEMENTOS TRANSVERSALES Y PROYECTO LINGÜÍSTICO DE CENTRO
    # -------------------------------------------------------------
    heading_1("11. ELEMENTOS TRANSVERSALES Y PROYECTO LINGÜÍSTICO DE CENTRO")
    body_p("En cumplimiento de los artículos 39 y 40 de la Ley 17/2007 (LEA) y del Real Decreto 659/2023:")
    bullet_p("El módulo sitúa la Accesibilidad Universal y el Diseño para Todos como pilar ético y legal indispensable del desarrollo de software.", "Inclusión y Accesibilidad Universal: ")
    bullet_p("Visibilización de referentes femeninos en ingeniería de software y diseño de interacción.", "Igualdad de Género: ")
    bullet_p("Respeto riguroso a la propiedad intelectual (TRLPI), licencias de código abierto y privacidad de datos (RGPD/LOPDGDD).", "Propiedad Intelectual y Privacidad: ")
    bullet_p("Optimización de memoria y CPU en aplicaciones Electron y Angular para minimizar el consumo energético.", "Sostenibilidad y Green Software: ")
    bullet_p("Lectura y análisis de documentación técnica oficial en inglés (Angular.dev, Electronjs.org, MDN). Corrección ortográfica y sintáctica en informes y memorias (descuento de 0,2 por falta hasta un máximo de 2 puntos).", "Proyecto Lingüístico de Centro (PLC): ")

    # -------------------------------------------------------------
    # 12. ACTIVIDADES COMPLEMENTARIAS Y EXTRAESCOLARES
    # -------------------------------------------------------------
    heading_1("12. ACTIVIDADES COMPLEMENTARIAS Y EXTRAESCOLARES")
    bullet_p("Visitas a empresas de desarrollo de software multiplataforma y centros tecnológicos andaluces (Geolit, PTA, Cartuja).", "Visitas a Empresas Tecnológicas: ")
    bullet_p("Participación en hackathons, eventos de desarrollo frontend/desktop y webinars técnicos.", "Jornadas Técnicas y Encuentros: ")
    bullet_p("Encuentros con antiguos alumnos/as de DAM dedicados profesionalmente al desarrollo de software multiplataforma.", "Mesa Redonda con Egresados: ")

    # -------------------------------------------------------------
    # 13. RECURSOS DIDÁCTICOS, BIBLIOGRAFÍA Y MATERIALES DEL MÓDULO
    # -------------------------------------------------------------
    heading_1("13. RECURSOS DIDÁCTICOS, BIBLIOGRAFÍA Y MATERIALES DEL MÓDULO")
    body_p("El módulo cuenta con un conjunto integral de 23 documentos de apuntes y proyectos estructurados en docs/:")

    docs_headers = ["Unidad", "Título del Recurso en docs/", "Contenido y Enfoque Profesional"]
    docs_data = [
        ["00 (index.md)", "00. Introducción al Desarrollo de Interfaces", "Tipologías (GUI, CLI, VUI, NUI), evolución, UX vs UI, multiplataforma y UCD."],
        ["01", "01-ux.md", "Principios de UX, heurísticas de Nielsen, flujos de usuario, arquitectura de información y UX writing."],
        ["02", "02-accesibilidad.md", "Accesibilidad web WCAG 2.2 (A/AA/AAA), principios POUR, WAI-ARIA y herramientas de auditoría."],
        ["03", "03-interfaces-naturales.md", "Interfaces Naturales (NUI): Web Speech API (voz), MediaPipe (gestos/cuerpo) y WebXR (Realidad Aumentada)."],
        ["04", "04-figma.md", "Figma avanzado: Auto Layout, variables, componentes, variantes, tokens y Dev Mode."],
        ["05", "05-layouts-modernos.md", "Layouts con Flexbox y CSS Grid, equivalencias con escritorio clásico y container queries."],
        ["06", "06-tailwindcss4.md", "Tailwind CSS 4: Enfoque utility-first, configuración en Vite/Angular con @theme y dark mode."],
        ["07", "07-componentes-tailwind.md", "Componentes de interfaz: botones, cards, tablas de datos, modales CDK y navbars."],
        ["08", "08-responsive-design.md", "Responsive design Mobile-First en Angular, BreakpointObserver con signals y Electron."],
        ["09", "09-ecosistema-frontend.md", "Node.js, npm, Angular Standalone, TypeScript estricto, Angular Signals, Storybook y Electron."],
        ["10", "10-arquitectura-angular.md", "Arquitectura por componentes Standalone, patrón Smart vs Presentational y signals."],
        ["11", "11-componentes-reutilizables.md", "Componentes reutilizables SOLID, proyección ng-content y estados de UI."],
        ["12", "12-formularios-interaccion.md", "Reactive Forms avanzados, validadores personalizados, mensajes contextuales y wizards."],
        ["13", "13-design-systems.md", "Design systems, Atomic Design, tokens fuente de verdad y ThemeProvider con signals."],
        ["14", "14-storybook.md", "Documentación de componentes con Storybook, formato CSF3, addons y pruebas de interacción."],
        ["15", "15-diseno-a-implementacion.md", "Handoff Figma Dev Mode a código Angular+Tailwind, Atomic Design y testing."],
        ["16", "16-generacion-informes.md", "Generación de informes con PDFMake, jsPDF y exportación Excel/CSV con SheetJS."],
        ["17", "17-dashboards-exportacion-datos.md", "Dashboards interactivos con Chart.js, ApexCharts, widgets KPI y exportación."],
        ["18", "18-documentacion-aplicaciones.md", "Documentación de apps, ayudas contextuales, MkDocs/Docusaurus y TSDoc."],
        ["19", "19-pruebas-de-software.md", "Pirámide de pruebas: unitarias con mocks, integración y E2E con Playwright."],
        ["20", "20-electron.md", "Aplicaciones de escritorio con Electron: procesos Main/Renderer, IPC tipado y APIs nativas."],
        ["21", "21-empaquetado-distribucion.md", "electron-builder, instaladores NSIS/AppImage/deb/DMG, autoactualizaciones y CI/CD."],
        ["22", "22-proyecto-final.md", "Proyecto integrador empresarial completo «GesFlow» en 9 fases con rúbrica de evaluación."]
    ]
    styled_table(docs_headers, docs_data, col_widths=[1.1, 2.4, 3.2], header_bg="0F4C81")

    # Guardar archivos docx
    out_docx_1 = r"e:\00. Clases\Apuntes\Desarrollo_Interfaces\programación\Desarrollo_de_interfaces_2DAM_2025-2026.docx"
    out_docx_2 = r"e:\00. Clases\Apuntes\Desarrollo_Interfaces\programación\Programacion_Didactica_DI_2DAM_Andalucia.docx"
    
    doc.save(out_docx_1)
    doc.save(out_docx_2)
    print(f"Documentos Word DI DAM guardados con éxito:\n1. {out_docx_1}\n2. {out_docx_2}")

if __name__ == "__main__":
    build_di_dam_programacion()
