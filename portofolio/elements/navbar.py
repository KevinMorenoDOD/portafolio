import reflex as rx
from ..styles import navbar_styles

navbar_items = [
    {"id": "tecnologies", "label": "Tecnologías"},
    {"id": "proyects", "label": "Proyectos"},
    {"id": "experience", "label": "Experiencia"},
    {"id": "studies", "label": "Estudios"},
    {"id": "contact", "label": "Contacto"},
]

def button(text: str, section_id: str, id: str) -> rx.Component:
    return rx.link(
        rx.button(text, id=id, style=navbar_styles.navbar_button_style),
        href=f"#{section_id}",
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link(
                rx.text("Portafolio", style=navbar_styles.navbar_brand_style),
                href="#profile",
            ),
            rx.box(
                *[button(item["label"], item["id"], item["id"]) for item in navbar_items],
                style=navbar_styles.navbar_links_style,
                width="wrap",
            ),
            style=navbar_styles.navbar_inner_style,
        ),
        style=navbar_styles.navbar_shell_style,
        width="100%",
    )



