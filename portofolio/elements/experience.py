import reflex as rx
from ..styles import experience_styles
from ..styles import general_styles as gs


def elements(title:str, site:str, date:str, description:list[str]) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon("cog"),
            rx.text(title, style=gs.subtitle_style,
            width="100%"),
            align="center",
            align_items="center",
        ),
        rx.text(site),
        rx.text(date),
        rx.list.unordered(
            *[rx.list_item(desc) for desc in description],  
        ),
        width="100%"
    )

def experience() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Experience",
                style=gs.title_style,
                width="100%"
            ),
            elements(
                "Maintenance Technician and Developer",
                "Alimentos Cárnicos – Bogotá",
                "September 2024 – September 2025",
                [
                    "Performed on-site maintenance and technical support for printers, computer equipment, and structured cabling. ",
                    "Diagnosed and resolved structured cabling failures and connectivity issues. ",            
                    "Developed and led internal projects using JavaScript and Google Apps Script to automate processes and optimize work time. "                
                ]                
            ),
            elements(
                "Front-End Developer",
                "SENA – Gustavo Campos Guevara Institution",
                "June 2018 – November 2020",
                [
                    "Designed and implemented an attendance and excuse management system using HTML and CSS.",
                    "Developed intuitive and responsive interfaces for multiple devices.",
                    "Improved school attendance tracking and registration, increasing administrative efficiency.",
                ]
            ),
            align="center",
            align_items="center",
            width="90%",
            style=gs.container_style
        ),
        style=gs.container_style,
        display="flex",
        justify_content="center",
        width="100%",
    )