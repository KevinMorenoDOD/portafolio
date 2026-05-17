import reflex as rx
from ..styles import profile_styles
from ..styles import general_styles as gs

class MailState(rx.State):
    show_mail: bool = False

    @rx.event
    def toggle_mail(self):
        self.show_mail = not self.show_mail

def mail_toggle() -> rx.Component:
    return rx.button(
        rx.icon("mail", size=15),
        rx.cond(
            MailState.show_mail,
            rx.text("kevin.dev.dod@gmail.com", color=gs.primary_color, font_weight="600"),
            rx.text("Mostrar correo"),
        ),
        style=profile_styles.mail_button_style,
        on_click=MailState.toggle_mail,
    )

def button_with_icon(icon_name: str, text: str, link: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon_name, size=15),
            rx.text(text),
            spacing="2",
            align_items="center",
        ),
        href=link,
        is_external=True,
        style=profile_styles.social_link_style,
    )

def profile() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    rx.image(
                        src=rx.asset("profile_img.png"),
                        alt="Kevin Felipe Moreno Ramirez",
                        style=profile_styles.avatar_image_style,
                    ),
                    style=profile_styles.avatar_frame_style,
                ),
                style=profile_styles.avatar_container_style,
            ),
            rx.vstack(
                rx.heading(
                    "Kevin Felipe",
                    rx.text(" Moreno", as_="span", color=gs.primary_color),
                    " Ramirez",
                    style=profile_styles.headline_style,
                    as_="h1",
                ),
                rx.hstack(
                    rx.icon("locate", size=14),
                    rx.text("Bogotá, Colombia", font_size="0.9rem", letter_spacing="0.04em"),
                    style=profile_styles.location_row_style,
                ),
                rx.text(
                    "Desarrollador y Estudiante de Ingeniería de Sistemas orientado al desarrollo Backend y Machine Learning, con interés en la construcción de APIs, automatización y soluciones escalables. Cuento con una fuerte capacidad analítica, aprendizaje autodidacta y experiencia trabajando con tecnologías enfocadas en backend y procesamiento de datos. Busco aportar en proyectos tecnológicos donde pueda combinar lógica, desarrollo e innovación para crear soluciones de impacto.",
                    style=profile_styles.summary_style,
                ),
                rx.box(
                    button_with_icon("github", "Github", "https://github.com/KevinMorenoDOD"),
                    button_with_icon(
                        "linkedin",
                        "LinkedIn",
                        "https://www.linkedin.com/in/kevin-felipe-moreno-ramirez/",
                    ),
                    rx.link(
                        rx.hstack(
                            rx.icon("download", size=15),
                            rx.text("CV"),
                            spacing="2",
                            align_items="center",
                        ),
                        href=rx.asset("CV_simple_kevin_moreno_ES.pdf"),
                        is_external=True,
                        style=profile_styles.social_link_style,
                    ),
                    mail_toggle(),
                    style=profile_styles.socials_row_style,
                ),
                align_items="start",
            ),
            style=profile_styles.hero_grid_style,
        ),
        style=gs.container_style,
    )
    