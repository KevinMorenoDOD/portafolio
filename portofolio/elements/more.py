import reflex as rx
from ..styles import general_styles as gs

def more() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "More",
                style=gs.title_style,
            ),
            width="90%",
            style = gs.container_style    
        ),
        width="100%",
        style = gs.container_style  
    )