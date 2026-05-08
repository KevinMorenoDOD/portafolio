import reflex as rx
from ..styles import general_styles as gs
from ..styles import studies_styles as ss


studies_data = [
    {
        "degree": "Ingeniería de Sistemas",
        "institution": "Universidad Minuto de Dios",
        "detail": "7mo semestre en curso",
        "location": "Bogotá, Colombia",
        "year": "2021 – Presente",
    },
    {
        "degree": "Técnico en Desarrollo de Software",
        "institution": "SENA",
        "detail": "Certificado Técnico",
        "location": "Bogotá, Colombia",
        "year": "2018 – 2020",
    },
    
]


def _study_card(study: dict[str, str]) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.icon("graduation-cap", size=17, color=gs.primary_color),
                style=ss.icon_shell_style,
            ),
            rx.vstack(
                rx.text(study["year"], style=ss.year_style),
                rx.text(study["degree"], style=ss.degree_style),
                rx.text(study["institution"], style=ss.institution_style),
                rx.text(f"{study['detail']} · {study['location']}", style=ss.detail_style),
                spacing="1",
                align_items="start",
            ),
            align_items="start",
            gap="1rem",
        ),
        style=ss.card_style,
    )

def studies() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("Estudios", style=gs.title_style),
            rx.box(style=gs.group_divider_title_style),
            rx.flex(
                *[_study_card(study) for study in studies_data],
                style=ss.cards_wrap_style,
            ),
            width="100%",
            style=gs.container_style,
        ),
    )