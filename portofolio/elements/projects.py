import reflex as rx
from ..styles import general_styles as gs

from ..styles import projects_style

projects_data = [
    {
        "title": "MailOffice",
        "description": "Sistema de gestión de entregas para mensajeros con app Android (Kotlin), API REST (.NET) y dashboard web de monitoreo en mapa.",
        "tech": ["JavaScript", "C#", "SQL Server", "Kotlin" ],
        "year": "2025",
        "role": "Desarrollador Principal",
        "preview": "/mailoffice.jpg",
        "github": "https://github.com/KevinMorenoDOD/mailoffice",
        "youtube": "https://youtu.be/jVivE-QcvVc",
    },
    {
        "title": "SoporteTech",
        "description": "Sistema de gestión de tickets IT con entrada vía WhatsApp + asistente AI (DeepSeek), backend Spring Boot, panel React y automatización n8n.",
        "tech": ["Java", "Spring Boot", "React", "PostgreSQL", "JavaScript", "Google Cloud"],
        "year": "2026",
        "role": "Desarrollador Full Stack",
        "preview": "/soportech.png",
        "github": "https://github.com/KevinMorenoDOD/Soportech",
        "youtube": "https://youtu.be/XNgxpWF93Uk"
    }
]


class ProjectsState(rx.State):
    """Estado para el carrusel de proyectos."""
    current_index: int = 0
    current_position: str = "1 / 3"
    current_title: str = projects_data[0]["title"]
    current_description: str = projects_data[0]["description"]
    current_role: str = projects_data[0]["role"]
    current_year: str = projects_data[0]["year"]
    current_preview: str = projects_data[0]["preview"]
    current_github: str = projects_data[0]["github"]
    current_youtube: str = projects_data[0]["youtube"]
    current_tech: list[str] = projects_data[0]["tech"]

    def _set_current_project(self, index: int):
        project = projects_data[index]
        self.current_index = index
        self.current_position = f"{index + 1} / {len(projects_data)}"
        self.current_title = project["title"]
        self.current_description = project["description"]
        self.current_role = project["role"]
        self.current_year = project["year"]
        self.current_preview = project["preview"]
        self.current_github = project["github"]
        self.current_youtube = project["youtube"]
        self.current_tech = project["tech"]

    def prev_project(self):
        self._set_current_project((self.current_index - 1 + len(projects_data)) % len(projects_data))

    def next_project(self):
        self._set_current_project((self.current_index + 1) % len(projects_data))

    def go_to_project(self, index: int):
        self._set_current_project(index)


def proyects() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Proyectos",
                style=gs.title_style,
                
            ),
            rx.box(style=gs.group_divider_title_style),
            # Current project card
            rx.box(
                rx.box(
                    rx.image(
                        src=ProjectsState.current_preview,
                        alt=ProjectsState.current_title,
                        style=projects_style.preview_image_style,
                    ),
                    style=projects_style.preview_image_container_style,
                    position="relative",
                ),
                rx.text(
                    ProjectsState.current_year,
                    style=projects_style.year_badge_style,
                ),
                # Content section
                rx.box(
                    rx.text(
                        ProjectsState.current_role,
                        style=projects_style.role_label_style,
                    ),
                    rx.heading(
                        ProjectsState.current_title,
                        style=projects_style.title_style,
                        as_="h3",
                    ),
                    rx.text(
                        ProjectsState.current_description,
                        style=projects_style.description_style,
                    ),
                    rx.box(
                        rx.foreach(
                            ProjectsState.current_tech,
                            lambda tech: rx.text(tech, style=projects_style.tech_tag_style),
                        ),
                        style=projects_style.tech_tags_container_style,
                    ),
                    rx.box(
                        rx.link(
                            rx.icon("github", size=15),
                            " GitHub",
                            href=ProjectsState.current_github,
                            is_external=True,
                            style=projects_style.github_button_style,
                        ),
                        rx.link(
                            rx.icon("youtube", size=15),
                            " YouTube",
                            href=ProjectsState.current_youtube,
                            is_external=True,
                            style=projects_style.youtube_button_style,
                        ),
                        style=projects_style.links_row_style,
                    ),
                    style=projects_style.content_wrapper_style,
                ),
                style=projects_style.card_style,
                margin_top="1rem",
            ),
            # Navigation
            rx.box(
                rx.box(
                    *[
                        rx.box(
                            on_click=lambda i=i: ProjectsState.go_to_project(i),
                            style=rx.cond(
                                ProjectsState.current_index == i,
                                projects_style.active_dot_style,
                                projects_style.inactive_dot_style,
                            ),
                        )
                        for i in range(len(projects_data))
                    ],
                    style=projects_style.dots_container_style,
                ),
                rx.box(
                    rx.button(
                        rx.icon("chevron-left", size=18),
                        on_click=ProjectsState.prev_project,
                        style=projects_style.arrow_button_style,
                    ),
                    rx.text(
                        ProjectsState.current_position,
                        style=projects_style.counter_style,
                    ),
                    rx.button(
                        rx.icon("chevron-right", size=18),
                        on_click=ProjectsState.next_project,
                        style=projects_style.arrow_button_style,
                    ),
                    style=projects_style.arrows_container_style,
                ),
                style=projects_style.navigation_container_style,
                margin_top="1.5rem",
                width="100%",
            ),
            width="100%",
            style=gs.container_style,
        ),
    )
