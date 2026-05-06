import reflex as rx
from ..styles import general_styles as gs

def studies() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Studies",
                style=gs.title_style,
            ),
            rx.text("Systems Engineering – Universidad Minuto de Dios 7th semester in progress – Bogotá, Colombia"),
            rx.text("Software Development Technician – SENA Bogotá,Colombia"),
            
            width="90%",
            style = gs.container_style    
        ),
        width="100%",
        style = gs.container_style    
    )