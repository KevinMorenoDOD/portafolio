import reflex as rx
from ..styles import general_styles as gs
from ..styles import tecnologies_styles

def tags(text: str, icon_name: str, border:bool = False) ->rx.Component:
    return rx.hstack(
        rx.image(
            src=icon_name,
            style=tecnologies_styles.img_style
            ),
        rx.text(text),
        style=tecnologies_styles.tag_style_bordered if border else tecnologies_styles.tag_style,
    ) 


def tecnologies() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Tecnologies",
                style=gs.title_style,                
            ),

            rx.text(
                "Principal",
                style=gs.subtitle_style,
            ),
            rx.flex(
                # Python ecosystem
                rx.vstack(
                    tags("Python", "/python.png",True),
                    tags("Django", "/django.png",True),
                    tags("FastAPI", "/fastapi.png",True),
                    style=tecnologies_styles.vstack_style
                ),
                # Java ecosystem
                rx.vstack(
                    tags("Java", "/java.png",True),
                    tags("Spring", "/springg.png",True),
                    style=tecnologies_styles.vstack_style
                ),
                # SQL ecosystem
                rx.vstack(
                    tags("SQL", "/sql-server.png",True),
                    tags("PostgeSQL", "/database(1).png",True),
                    style=tecnologies_styles.vstack_style
                ),
                # NoSQL ecosystem
                rx.vstack(
                    tags("NoSQL", "/unstructured-data.png",True),
                    tags("MongoDB", "/mongo.png",True),
                    style=tecnologies_styles.vstack_style
                ),
                wrap="wrap",
                justify="center",
                align="start",
                spacing="6",
                width="100%",
            ),
            
            # Secondary Section
            rx.text(
                "Secondary",
                style=gs.subtitle_style,
            ),
            rx.flex(
                tags("HTML", "/html-5.png"),
                tags("CSS", "/css-3.png"),
                tags("JS", "/java-script.png"), 
                tags("Reflex", "/reflex.png"),
                tags("MySql", "/database.png"),
                tags("SQLite", "/sql-server.png"),
                wrap="wrap",
                justify="center",
                spacing="2",
                width="100%",
            ),          
            width="90%",
            style = gs.container_style            
        ),      
        width="100%",
        style = gs.container_style
    )