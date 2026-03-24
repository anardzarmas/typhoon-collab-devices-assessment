import streamlit as st
from fpdf import FPDF
import datetime
import os

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Cisco Collaboration Assessment", layout="wide")

# --- CABECERAS Y TÍTULOS EN LA UI ---
st.title("Formulario de Evaluación de Cisco Collaboration & Workspaces")
st.subheader("Partner de Cisco: Typhoon Technology")
st.write("Complete este cuestionario detallado para descubrir la arquitectura de dispositivos y colaboración recomendada para sus espacios de trabajo.")
st.markdown("---")

# --- 1. INFORMACIÓN GENERAL DEL PROYECTO ---
st.header("1. Información General del Cliente")
col1, col2 = st.columns(2)

with col1:
    empresa = st.text_input("Empresa:")
    correo = st.text_input("Correo electrónico:")
    contacto = st.text_input("Contacto principal:")
    puesto = st.text_input("Puesto:")

with col2:
    am_cisco = st.text_input("AM de Cisco:")
    responsable_best = st.text_input("Responsable de Best:")
    fecha = st.date_input("Fecha de evaluación:", datetime.date.today())
    verticales = ["Finanzas", "Salud", "Educación", "Retail", "Manufactura", "Gobierno", "Servicios", "Otro"]
    vertical = st.selectbox("Vertical de negocio:", verticales)

st.markdown("---")

# --- 2. DOMINIOS DE EVALUACIÓN ---
st.header("2. Dominios de Evaluación")
st.write("Seleccione las opciones que mejor describan su entorno y utilice los campos de texto para información adicional.")

# I. Requerimientos y Necesidades del Negocio
st.subheader("I. Requerimientos y Necesidades del Negocio")
q_expectativas = st.text_area("¿Cuál es la visión de éxito y las expectativas de experiencia (ej. simplicidad de conexión, paridad entre remotos y presenciales, o innovación tecnológica) que sus colaboradores demandan para que el regreso a la oficina sea percibido como un valor agregado?")
q_prioridad = st.selectbox("2. ¿Están priorizando la inversión en agregar nuevas salas de reuniones o en actualizar las existentes?", 
                           ["Seleccione", "Agregar nuevas salas", "Actualizar las existentes", "Ambas por igual"])
q_sostenibilidad = st.selectbox("3. ¿Tienen iniciativas de sostenibilidad corporativa en las que la infraestructura tecnológica deba contribuir?", 
                                ["Seleccione", "Sí, es de alta prioridad (ej. reducción de consumo, materiales reciclados)", "Sí, pero es secundario", "No actualmente"])

# II. Entorno Actual y Desafíos Operativos
st.subheader("II. Entorno Actual y Desafíos Operativos")
q_salas_antiguas = st.text_input("4. ¿Cuántas salas de reuniones antiguas tienen actualmente que requieran una actualización tecnológica?")
q_visibilidad = st.selectbox("5. ¿Qué nivel de visibilidad y métricas tienen sobre qué tan utilizadas son realmente sus salas de reuniones?", 
                             ["Seleccione", "Nulo/Bajo", "Básico (algunas métricas manuales)", "Avanzado (monitoreo en tiempo real)"])
q_plataformas = st.selectbox("6. ¿Cuántas plataformas de reuniones soportan en la organización?", 
                             ["Seleccione", "1 plataforma (Exclusivo)", "2 plataformas", "3 o más plataformas"])
q_teams = st.selectbox("7. ¿Son ustedes un entorno exclusivo de Microsoft Teams?", 
                       ["Seleccione", "Sí, exclusivo de MS Teams", "No, utilizamos múltiples plataformas"])
q_retos = st.text_area("8. ¿Cuáles son los principales retos operativos al gestionar sus sistemas de conferencias? ¿Tienen soluciones aisladas?")

# III. Experiencia del Usuario Final y Casos de Uso
st.subheader("III. Experiencia del Usuario Final y Casos de Uso")
q_quejas = st.text_area("9. ¿Qué feedback o quejas reciben de los usuarios sobre su experiencia en las salas de reuniones?")
q_ruido = st.selectbox("10. ¿Cuentan con espacios de trabajo abiertos o salas con paredes de cristal donde las distracciones visuales/ruido sean un problema?", 
                       ["Seleccione", "Sí, es un problema frecuente", "Ocasionalmente", "No tenemos ese problema"])
q_inmersion = st.selectbox("11. En sus salas más grandes, ¿los participantes remotos logran sentirse integrados e inmersos de forma natural?", 
                           ["Seleccione", "No, es difícil integrarlos", "Parcialmente", "Sí, la experiencia es excelente"])

# IV. Gestión de TI y Seguridad
st.subheader("IV. Gestión de TI y Seguridad, y Observabilidad")
q_observabilidad = st.selectbox(
    "12. ¿Cuál es su capacidad actual para diagnosticar si una falla de conexión es atribuible al ISP, la red local o la plataforma de video?",
    ["Nula (Dependemos del reporte del usuario)", "Limitada (Solo red local)", "Total (Visibilidad hop-by-hop)"]
)

q_seguridad_financiera = st.radio(
    "13. Por políticas internas, ¿requieren que el procesamiento de datos biométricos (rostros/voz) se realice localmente en el dispositivo?",
    ["Sí, es obligatorio por cumplimiento", "Es deseable pero no mandatorio", "No es un requisito actual"]
)

q_gestion_central = st.selectbox(
    "14. ¿Qué importancia tiene automatizar la actualización de firmware y parches de seguridad desde un único panel cifrado?",
    ["Crítica (Prioridad absoluta)", "Media", "Baja"]
)

# V. Calificación de la oportunidad comercial
st.subheader("V. Calificación de la oportunidad comercial.")
col_strat1, col_strat2 = st.columns(2)

with col_strat1:
    q_reto = st.selectbox("¿Cuál es el reto principal?", 
                          ["Seleccione", "Refresco Tecnológico de Salas", "Habilitar Trabajo Híbrido", "Estandarización Corporativa", "Reducción de Costos", "Otro"])
    q_presupuesto = st.selectbox("Presupuesto", 
                                 ["Seleccione", "Presupuesto aprobado", "En evaluación (Depende de ROI)", "Fase exploratoria", "No definido"])

with col_strat2:
    q_tiempo = st.selectbox("Tiempo de implementación", 
                            ["Seleccione", "0 a 3 meses", "3 a 6 meses", "6 a 12 meses", "Más de 12 meses"])
    q_competencia = st.selectbox("Plataformas evaluadas (Competencia)", 
                                 ["Seleccione", "Poly / HP", "Logitech", "Yealink", "Neat", "Ninguna / No aplica", "Otra"])

q_detalles_estrategia = st.text_area("Detalles adicionales de la estrategia", 
                                     placeholder="Ej. El cliente busca implementar salas de Teams en Q3 y necesita actualizar sus equipos legacy para asegurar interoperabilidad...")

# --- LÓGICA DE RECOMENDACIÓN DE PRODUCTOS CISCO ---
def generar_recomendacion():
    recomendaciones = []
    
    # Lógica de Plataformas y MS Teams
    if "Sí, exclusivo" in q_teams:
        recomendaciones.append("- Cisco Devices for Microsoft Teams Rooms (MTR): Experiencia nativa de Teams con hardware premium de Cisco (ej. Cisco Room Bar Pro, Cisco Board Pro), garantizando una experiencia consistente.")
    elif "2" in q_plataformas or "3" in q_plataformas:
        recomendaciones.append("- Interoperabilidad Multiplataforma: Equipos Cisco con capacidad de unirse nativamente a Webex, MS Teams, Zoom y Google Meet sin fricción ni reinicios.")
    
    # Lógica de Inteligencia de Audio y Video (Cristales/Ruido/Inmersión)
    if "Sí" in q_ruido:
        recomendaciones.append("- Webex AI Audio & Video Intelligence: Funciones de 'Noise Removal' avanzado e 'Intelligent Framing / Speaker Track' ideales para mitigar distracciones en salas de cristal y espacios abiertos.")
    if "No" in q_inmersion or "Parcialmente" in q_inmersion:
        recomendaciones.append("- Cinematic Meetings & Multi-Cámara (Cisco Room Kit EQ/EQX): Inteligencia de video que cambia de toma automáticamente (Cross-View) para asegurar equidad en reuniones (Meeting Equity) en salas grandes o profundas.")
    
  
    # Lógica de Sostenibilidad
    if "Sí, es de alta prioridad" in q_sostenibilidad:
        recomendaciones.append("- Iniciativas de Sostenibilidad Cisco: Equipos diseñados con materiales reciclados y empaques sin plástico. Integración de funciones como 'Office Hours' para apagar pantallas automáticamente y reducir la huella de carbono.")
    
    # Recomendación base por defecto si hay actualización
    if "Actualizar" in q_prioridad or "Refresco" in q_reto:
        recomendaciones.append("- Programa de Migración de Hardware: Aprovechar el portafolio de nueva generación (Room Bar, Board Pro 55/75) para modernizar el legado y estandarizar la experiencia.")

    # Lógica Estratégica
    if "0 a 3 meses" in q_tiempo:
        recomendaciones.append("- Fast-Track Deployment: Por los tiempos requeridos, se sugiere priorizar equipos en stock e iniciar pruebas de concepto (PoC) de inmediato.")

    if not recomendaciones:
        recomendaciones.append("- Portafolio de Cisco Collaboration Devices y Webex Suite: Solución integral adaptada a sus necesidades específicas de trabajo híbrido.")

    # 1. Lógica de Observabilidad (ThousandEyes) - Pregunta 12
    if q_observabilidad in ["Nula (Dependemos del reporte del usuario)", "Limitada (Solo red local)"]:
        recomendaciones.append(
            "**Cisco ThousandEyes Integration:** Se detecta una brecha en la visibilidad de red. "
            "Se recomienda activar los agentes de ThousandEyes nativos en los dispositivos para obtener una "
            "ruta visual 'hop-by-hop'. Esto permitirá a IT identificar si las fallas ocurren en el ISP o en la "
            "nube, reduciendo drásticamente el tiempo de resolución (MTTR)."
        )
    
    # 2. Lógica de Seguridad Financiera (Local IA/NVIDIA) - Pregunta 13
    if q_seguridad_financiera in ["Sí, es obligatorio por cumplimiento", "Es deseable pero no mandatorio"]:
        recomendaciones.append(
            "**Privacidad y Seguridad de RoomOS:** Para cumplir con los estándares, "
            "la arquitectura se basa en el procesamiento local de IA mediante chips NVIDIA. "
            "Esto garantiza que el reconocimiento de rostros, supresión de ruido y encriptación ocurran "
            "dentro del hardware, evitando el envío de datos sensibles a nubes de terceros."
        )

    # 3. Lógica de Gestión Centralizada (Control Hub) - Pregunta 14
    if q_gestion_central in ["Crítica (Prioridad absoluta)", "Media"]:
        recomendaciones.append(
            "**Webex Control Hub (Single Pane of Glass):** Se recomienda la consolidación de la gestión en "
            "Control Hub para automatizar actualizaciones de firmware y parches de seguridad. "
            "Esto asegura que toda la base instalada esté siempre protegida y bajo cumplimiento "
            "sin intervención manual en sitio."
        )

    # 4. Lógica de Interoperabilidad (Basada en la pregunta de Teams/Plataformas)
    if "Sí, exclusivo" in q_teams:
        recomendaciones.append(
            "**Cisco Devices for Microsoft Teams Rooms (MTR):** Implementación de hardware certificado "
            "para correr Teams de forma nativa, manteniendo la telemetría avanzada de Cisco."
        )
    elif "No, multiplataforma" in q_teams:
        recomendaciones.append(
            "**Interoperabilidad Multiplataforma Nativa:** Uso de Webex Video Integration para MS Teams, "
            "permitiendo que las salas se unan a cualquier reunión (Zoom, Google, Teams) con un solo botón."
        )
    return recomendaciones

# --- GENERACIÓN DE PDF LOOK & FEEL ---
class PDF(FPDF):
    def header(self):
        if os.path.exists("logo_typhoon.jpg"):
            self.image("logo_typhoon.jpg", 10, 10, 35)
        if os.path.exists("logo_cisco.jpg"):
            self.image("logo_cisco.jpg", 165, 10, 35)
        
        self.set_y(32) 
        self.set_font("Arial", 'B', 13)
        self.cell(0, 6, sanitize("Acta de Evaluacion - Cisco Collaboration & Workspaces"), align='C', ln=True)
        self.set_font("Arial", '', 10)
        self.cell(0, 6, sanitize("Elaborado por: Best - Typhoon Technology"), align='C', ln=True)
        
        self.set_y(48)
        self.set_draw_color(200, 200, 200)
        self.line(10, 48, 200, 48)
        self.set_y(54)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", '', 9)
        self.cell(0, 10, f"Pagina {self.page_no()}", align='C')

def sanitize(text):
    if text is None: return ""
    # Reemplaza saltos de línea y sanitiza caracteres especiales
    return str(text).replace('\r', '').encode('latin-1', 'replace').decode('latin-1')

def crear_pdf():
    pdf = PDF()
    pdf.set_margins(left=10, top=10, right=10)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # --- SECCIÓN 1: Información General ---
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(190, 8, sanitize("1. Informacion General del Cliente"), ln=True)
    pdf.ln(2)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(20, 6, "Empresa: ")
    pdf.set_font("Arial", '', 10)
    pdf.cell(75, 6, sanitize(empresa))
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(18, 6, "Vertical: ")
    pdf.set_font("Arial", '', 10)
    pdf.cell(77, 6, sanitize(vertical), ln=True)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(20, 6, "Correo: ")
    pdf.set_font("Arial", '', 10)
    pdf.cell(75, 6, sanitize(correo))
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(15, 6, "Fecha: ")
    pdf.set_font("Arial", '', 10)
    pdf.cell(80, 6, sanitize(str(fecha)), ln=True)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(20, 6, "Contacto: ")
    pdf.set_font("Arial", '', 10)
    pdf.cell(75, 6, sanitize(contacto))
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(22, 6, "AM Cisco: ")
    pdf.set_font("Arial", '', 10)
    pdf.cell(73, 6, sanitize(am_cisco), ln=True)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(20, 6, "Puesto: ")
    pdf.set_font("Arial", '', 10)
    pdf.cell(75, 6, sanitize(puesto))
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(25, 6, "Resp. Best: ")
    pdf.set_font("Arial", '', 10)
    pdf.cell(70, 6, sanitize(responsable_best), ln=True)
    
    pdf.ln(8)

    # --- SECCIÓN 2: Cuestionario ---
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(190, 8, sanitize("2. Cuestionario de Evaluacion y Respuestas"), ln=True)
    pdf.ln(2)

    def print_bloque(titulo_dominio, qa_list):
        pdf.set_x(10)
        pdf.set_font("Arial", 'B', 10)
        pdf.set_fill_color(240, 240, 240)
        pdf.cell(190, 7, sanitize(titulo_dominio), ln=True, fill=True)
        pdf.ln(2)
        
        for q, a in qa_list:
            pdf.set_x(10)
            pdf.set_font("Arial", 'B', 9)
            pdf.multi_cell(190, 5, sanitize(f"P: {q}"))
            
            pdf.set_x(10)
            pdf.set_font("Arial", '', 9)
            respuesta_texto = a if a.strip() else "N/A"
            pdf.multi_cell(190, 5, sanitize(f"R: {respuesta_texto}"))
            pdf.ln(3)

    print_bloque("I. Requerimientos y Necesidades del Negocio", [
        ("Expectativas de regreso a la oficina y modelos híbridos", q_expectativas),
        ("Prioridad de inversión en salas", q_prioridad),
        ("Iniciativas de sostenibilidad corporativa", q_sostenibilidad)
    ])
                 
    print_bloque("II. Entorno Actual y Desafios Operativos", [
        ("Cantidad de salas antiguas a actualizar", q_salas_antiguas),
        ("Visibilidad y métricas de uso de salas", q_visibilidad),
        ("Cantidad de plataformas de reuniones soportadas", q_plataformas),
        ("Exclusividad con Microsoft Teams", q_teams),
        ("Retos operativos y soluciones aisladas", q_retos)
    ])
                 
    print_bloque("III. Experiencia del Usuario Final y Casos de Uso", [
        ("Feedback o quejas sobre la experiencia", q_quejas),
        ("Problemas de ruido/distracciones en espacios abiertos", q_ruido),
        ("Nivel de inmersión de participantes remotos en salas grandes", q_inmersion)
    ])
                 
    print_bloque("IV. Gestión de TI, Seguridad y Observabilidad", [
        ("Capacidad de diagnóstico de red (ISP, Local, Nube)", q_observabilidad),
        ("Requisito de procesamiento de IA local (Privacidad)", q_seguridad_financiera),
        ("Prioridad de gestión centralizada de parches y seguridad", q_gestion_central),
    ])

    print_bloque("V. Calificacion de la oportunidad comercial", [
        ("Reto principal", q_reto),
        ("Tiempo de implementacion", q_tiempo),
        ("Presupuesto", q_presupuesto),
        ("Plataformas evaluadas (Competencia)", q_competencia),
        ("Detalles adicionales de la estrategia", q_detalles_estrategia)
    ])

    # --- SECCIÓN 3: Recomendaciones ---
    pdf.ln(2)
    pdf.set_x(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(190, 8, sanitize("3. Arquitectura y Soluciones Cisco Recomendadas"), ln=True)
    pdf.ln(2)
    
    pdf.set_font("Arial", '', 10)
    recomendaciones = generar_recomendacion()
    for rec in recomendaciones:
        pdf.set_x(10)
        pdf.multi_cell(190, 6, sanitize(rec))
        pdf.ln(2)
        
    pdf.ln(3)
    pdf.set_x(10)
    pdf.set_font("Arial", 'B', 9)
    pdf.multi_cell(190, 5, sanitize("Nota importante: Esta informacion es una sugerencia preliminar generada a partir del assessment. Queda estrictamente sujeta a los comentarios, validacion tecnica y diseno formal por parte de un preventa certificado de Typhoon Technology."))

    # Guardar PDF
    empresa_limpia = empresa.replace(' ', '_') if empresa else "Plantilla"
    nombre_archivo = f"Collab_Assessment_Rooms_{empresa_limpia}.pdf"
    pdf.output(nombre_archivo)
    return nombre_archivo

# --- BOTÓN DE DESCARGA ---
st.markdown("---")
if st.button("Analizar Datos y Generar Documento PDF"):
    if not empresa:
        st.warning("Por favor, ingrese el 'Nombre de la empresa' en la sección superior para nombrar el archivo correctamente.")
    else:
        try:
            archivo_pdf = crear_pdf()
            with open(archivo_pdf, "rb") as pdf_file:
                st.success("¡Análisis completado! Archivo generado exitosamente.")
                st.download_button(
                    label="📥 Descargar PDF de Evaluación",
                    data=pdf_file,
                    file_name=archivo_pdf,
                    mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Ocurrió un error inesperado generando el PDF: {e}")
