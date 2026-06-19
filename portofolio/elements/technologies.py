import reflex as rx
from ..styles import general_styles as gs
from ..styles import technologies_styles

principal_groups = [
    {
        "title": "Python",
        "items": [
            {"name": "Python", "icon": "/python.png"},
            {"name": "Django", "icon": "/django.png"},
            {"name": "FastAPI", "icon": "/fastapi.png"},
        ],
    },
    {
        "title": "Java",
        "items": [
            {"name": "Java", "icon": "/java.png"},
            {"name": "Spring", "icon": "/springg.png"},
        ],
    },
    {
        "title": "SQL",
        "items": [
            {"name": "SQL", "icon": "/sql-server.png"},
            {"name": "PostgreSQL", "icon": "/database(1).png"},
        ],
    },
    {
        "title": "NoSQL",
        "items": [
            {"name": "NoSQL", "icon": "/unstructured-data.png"},
            {"name": "MongoDB", "icon": "/mongo.png"},
        ],
    },
]

secondary_tecnologies = [
    {
        "name": "HTML",
        "icon": "/html-5.png"
    },
    {
        "name": "CSS",
        "icon": "/css-3.png"
    },
    {
        "name": "JavaScript",
        "icon": "/java-script.png"
    },
    {
        "name": "Reflex",
        "icon": "/reflex.png"
    },
    {
        "name": "MySQL",
        "icon": "/database.png"
    },
    {
        "name": "SQLite",
        "icon": "/sql-server.png"  
    },
    {
        "name": "Git",
        "icon": "/git.png"
    },
    {
        "name": "Docker",
        "icon": "/docker.png"
    },
    {
        "name": "VBA",
        "icon": "/vba.png"
    },
]

def tag(text: str, icon_name: str) -> rx.Component:
    return rx.hstack(
        rx.image(
            src=icon_name,
            style=technologies_styles.badge_icon_style,
        ),
        rx.text(text),
        style=technologies_styles.badge_style,
    )

def tech_group(title: str, items: list[dict]) -> rx.Component:
    return rx.box(
        rx.text(title, style=technologies_styles.group_title_style),
        rx.box(
            *[tag(tech["name"], tech["icon"]) for tech in items],
            style=technologies_styles.badges_row_style,
        ),
        style=technologies_styles.group_wrapper_style,
    )


def tecnologies() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Tecnologías",
                style=gs.title_style,                
            ),
            rx.box(style=gs.group_divider_title_style),
            rx.text(
                "Principal",
                style=gs.subtitle_style,
            ),
            rx.box(style=gs.group_divider_style),
            rx.flex(
                *[
                    tech_group(group["title"], group["items"])
                    for group in principal_groups
                ],
                wrap="wrap",
                justify_content="flex-start",
                gap="2rem",
                width="100%",
            ),
            rx.text(
                "Secundarias",
                style=gs.subtitle_style,
            ),
            rx.box(style=gs.group_divider_style),

            tech_group("Herramientas extras", secondary_tecnologies),
            width="100%",
            align_items="start",
            style=gs.container_style,
        ), 
    )