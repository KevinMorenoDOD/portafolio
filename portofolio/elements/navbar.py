import reflex as rx
from ..styles import navbar_styles
from ..styles import general_styles as gs



def button(text:str, section_id:str) -> rx.Component:
    return rx.link(
        rx.button(
            text,
            style=navbar_styles.navbar_buttons_style
        ),
        href=f"#{section_id}"
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.center(
            rx.hstack(                
                button("Tecnologies", "tecnologies"),
                button("Proyects", "proyects"),          
                button("Experience", "experience"),          
                button("Studies", "studies"),          
                button("More", "more"),    
                button("Contact", "contact"),                    
            ),
        ),
        style=navbar_styles.navbar_style_fixed
    )

