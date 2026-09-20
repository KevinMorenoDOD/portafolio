import reflex as rx
from ..styles import contact_styles as cs
from ..styles import general_styles as gs
from ..email_service import send_contact_email


class ContactState(rx.State):
    name: str = ""
    email: str = ""
    message: str = ""
    show_success: bool = False
    show_error: bool = False
    error_message: str = ""
    is_sending: bool = False

    @rx.event
    def handle_name_change(self, value: str):
        self.name = value
        if self.show_success:
            self.show_success = False

    @rx.event
    def handle_email_change(self, value: str):
        self.email = value
        if self.show_success:
            self.show_success = False

    @rx.event
    def handle_message_change(self, value: str):
        self.message = value
        if self.show_success:
            self.show_success = False

    @rx.event
    def handle_submit(self):
        # Validate fields
        if not self.name.strip() or not self.email.strip() or not self.message.strip():
            self.error_message = "Por favor, completa todos los campos."
            self.show_error = True
            return

        self.is_sending = True
        self.show_error = False
        self.show_success = False

        result = send_contact_email(self.name, self.email, self.message)

        self.is_sending = False

        if result["success"]:
            self.show_success = True
            self.name = ""
            self.email = ""
            self.message = ""
        else:
            self.error_message = result.get("error", "Error al enviar el mensaje.")
            self.show_error = True

    @rx.event
    def hide_success(self):
        self.show_success = False

    @rx.event
    def hide_error(self):
        self.show_error = False


def contact() -> rx.Component:
    return rx.box(
        rx.vstack(
        rx.el.style(
                """
            #contact input::placeholder,
            #contact textarea::placeholder {
            color: #cbd5e1;
            opacity: 1;
            }
            """
        ),
            rx.text("Contacto", style=gs.title_style),
            rx.box(style=gs.group_divider_title_style),
            rx.text(
                "Abierto a nuevas oportunidades, colaboraciones y proyectos estratégicos. Construyamos algo genial juntos.",
                style=cs.description_style,
            ),
            rx.cond(
                ContactState.show_success,
                rx.box(
                    rx.box(
                        rx.button(
                            "X",
                            on_click=ContactState.hide_success,
                            style=cs.popup_close_button_style,
                        ),
                        rx.text("✓ Mensaje enviado. Te responderé pronto.", style=cs.success_message_style),
                        style=cs.popup_card_style,
                    ),
                    style=cs.popup_overlay_style,
                ),
                rx.fragment(),
            ),
            rx.cond(
                ContactState.show_error,
                rx.box(
                    rx.text(ContactState.error_message, style=cs.error_message_style),
                ),
                rx.fragment(),
            ),
            rx.vstack(
                rx.input(
                    placeholder="TU NOMBRE",
                    value=ContactState.name,
                    on_change=ContactState.handle_name_change,
                    style=cs.input_style,
                    css={"&::placeholder": {"color": cs.placeholder_color}},
                    class_name="placeholder:text-slate-300 placeholder:opacity-100",
                ),
                rx.input(
                    placeholder="TU CORREO",
                    type_="email",
                    value=ContactState.email,
                    on_change=ContactState.handle_email_change,
                    style=cs.input_style,
                    css={"&::placeholder": {"color": cs.placeholder_color}},
                    class_name="placeholder:text-slate-300 placeholder:opacity-100",
                ),
                rx.text_area(
                    placeholder="TU MENSAJE",
                    value=ContactState.message,
                    on_change=ContactState.handle_message_change,
                    style=cs.input_style,
                    css={"&::placeholder": {"color": cs.placeholder_color}},
                    class_name="placeholder:text-slate-300 placeholder:opacity-100",
                ),
                rx.cond(
                    ContactState.is_sending,
                    rx.button(
                        rx.spinner(size="3"),
                        "Enviando...",
                        style=cs.submit_button_style,
                        is_loading=True,
                    ),
                    rx.button(
                        rx.icon("send", size=15),
                        "Enviar Mensaje",
                        on_click=ContactState.handle_submit,
                        style=cs.submit_button_style,
                    ),
                ),
                spacing="8",
                style=cs.form_container_style,
            ),
            spacing="8",
            width="100%",
            style=cs.section_style,
        ),
        width="100%",
    )