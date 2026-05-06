import reflex as rx
from rxconfig import config

from .styles import general_styles as gs
from .styles import index_styles

from .elements.navbar import navbar
from .elements.profile import profile
from .elements.tecnologies import tecnologies
from .elements.experience import experience
from .elements.proyects import proyects
from .elements.studies import studies
from .elements.more import more
from .elements.contact import contact



class State(rx.State):
    """The app state."""

# Estilo para las secciones (margin para el navbar fijo)
section_style = {
    "scroll_margin_top": "100px",
    "width": "100%",

}


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),

        rx.vstack(
            rx.box(profile(), id="profile", style=section_style),
            rx.box(tecnologies(), id="tecnologies", style=section_style),
            rx.box(proyects(), id="proyects", style=section_style),
            rx.box(experience(), id="experience", style=section_style),
            rx.box(studies(), id="studies", style=section_style),
            rx.box(more(), id="more", style=section_style),
            rx.box(contact(), id="contact", style=section_style),        
            style=index_styles.background_style 
        ),

    ),

app = rx.App()
app.add_page(index)
