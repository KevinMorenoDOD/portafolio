import reflex as rx
from ..styles import experience_styles as es
from ..styles import general_styles as gs


experiences = [
    {
        "title": "Auxiliar de servicio tecnico",
        "company": "Corporación Universitaria Minuto de Dios - UNIMINUTO",
        "location": "Bogotá",
        "period": "Octubre 2025 - Diciembre 2025",
        "bullets": [
            "Brindé soporte técnico a estudiantes, docentes y personal administrativo en hardware, software y plataformas institucionales.",
            "Desarrollé scripts en Python para automatizar procesos internos y optimizar tareas operativas.",
            "Utilicé Selenium para pruebas y validación de plataformas web institucionales.",
            "Coordiné con distintas áreas para garantizar atención oportuna y continuidad en actividades académicas y administrativas."
        ],
    },
    {
        "title": "Técnico de Mantenimiento y Desarrollador",
        "company": "Alimentos Cárnicos",
        "location": "Bogotá",
        "period": "Septiembre 2024 – Septiembre 2025",
        "bullets": [
            "Realicé mantenimiento en sitio y soporte técnico para impresoras, equipos de cómputo y cableado estructurado.",
            "Diagnostiqué y resolví fallas de cableado estructurado y problemas de conectividad.",
            "Desarrollé y lideré proyectos internos usando JavaScript y Google Apps Script para automatizar procesos y optimizar el tiempo de trabajo.",
        ],
    },
    {
        "title": "Desarrollador Front-End",
        "company": "SENA – Institución Gustavo Campos Guevara",
        "location": "Bogotá",
        "period": "Junio 2018 – Noviembre 2020",
        "bullets": [
            "Diseñé e implementé un sistema de gestión de asistencia y excusas usando HTML y CSS.",
            "Desarrollé interfaces intuitivas y responsivas para múltiples dispositivos.",
            "Mejoré el seguimiento y registro de asistencia escolar, incrementando la eficiencia administrativa.",
        ],
    },  
]


def _render_experience_item(exp) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("briefcase", color=gs.primary_color, size=15),
                rx.text(exp["title"], style=gs.subtitle_style, color=gs.primary_foreground_color),
                align="center",
                align_items="center",
                gap="0.5rem",
            ),
            rx.box(style=gs.group_divider_style),
            rx.text(f"{exp['company']} — {exp['location']}", style=es.company_style),
            rx.text(exp["period"], style=es.period_style, margin_bottom="0.75rem"),
            rx.vstack(
                *[
                    rx.hstack(
                        rx.box(style=es.bullet_dot_style),
                        rx.text(b, style=es.bullet_item_style),
                        align_items="flex-start",
                        gap="0.5rem",
                    )
                    for b in exp["bullets"]
                ],
                spacing="2",
            ),
            spacing="3",
            style=es.experience_card_style,
        ),
        width="100%",
        padding_left="1.5rem",
        border_left=f"4px solid {gs.primary_color}",
        margin_top="1rem",
    )


def experience() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("Experiencia", style=gs.title_style, width="100%"),
            rx.box(style=gs.group_divider_title_style),
            rx.vstack(*[_render_experience_item(e) for e in experiences], spacing="4", margin_top="0.75rem"),
            style=es.section_style,
        )
    )