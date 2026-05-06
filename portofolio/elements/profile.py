import reflex as rx
from ..styles import profile_styles
from ..styles import general_styles as gs

class MailState(rx.State):
    show_send : bool = False
    text: str = "Show Mail"
    color: str = gs.color_primary
    cursor: str = "pointer"

    @rx.event
    def change_to_mail(self):
        if self.text == "Show Mail":
            self.show_send = True
            self.text = "morenokevinfelipe@gmail.com"
            self.color = gs.border_color
            self.cursor = "default"
        else:
            self.text = "Show Mail"
            self.show_send = False
            self.color = gs.color_primary
            self.cursor = "pointer"

def mail_show() ->rx.Component:
    return rx.hstack(
        rx.button(
            rx.icon("mail"), 
            MailState.text,
            style=profile_styles.buttons_style,
            bg_color = MailState.color,
            cursor = MailState.cursor,
            on_click=MailState.change_to_mail(),
        ),
        rx.cond(
            MailState.show_send,
            rx.link(
                rx.button(
                    rx.icon("mail"), 
                    "Send a mail",
                    style=profile_styles.buttons_style,
                    ),
                href="mailto:kevin@example.com",
                is_external=True,                           
            ),
        ),    
    )

def button_with_icon(icon_name: str, text: str, link: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon_name), 
            text,
            style=profile_styles.buttons_style 
        ),
        href=link,
        is_external=True,
               
    )

def profile() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.image(
                    src=rx.asset("profile_img.png"), 
                    style=profile_styles.img_style,
                ),
                rx.vstack(
                    rx.text(
                        "Kevin Felipe Moreno Ramirez",
                        font_size=gs.font_large,
                        max_width="8em",                    
                    ),
                    rx.hstack(
                        rx.icon("locate"),
                        rx.text("Bogotá, Colombia"),
                    ),

                    rx.text(
                        "I am a systems engineering student passionate about continuous learning and seeking new challenges that allow me to grow as a developer. I have a strong interest in mathematics and physics, disciplines that inspire me to analyze problems from logic, abstraction, and precision.",
                        max_width="28em",
                        font_size=gs.font_small,
                    ),
                ),
                
                style=profile_styles.hstack_style,

            ),
            
            rx.hstack(
                button_with_icon("github","Github","https://github.com/DODOPPPLER"),                          
                button_with_icon("linkedin", "Linkedin","https://www.linkedin.com/in/kevin-felipe-moreno-ramirez-863b59144/"),
                rx.link(
                    rx.button(
                        rx.icon("download"), 
                        "CV",
                        style=profile_styles.buttons_style
                        ),
                    href=rx.asset("CV_Kevin_Moreno_ES.pdf"),
                    is_external=True,      
                ),
                mail_show(),                
                style=profile_styles.hstack_style,                 
            ),
            
            align="center",
            style=gs.container_style
        ),

        style=gs.container_style
    )
    