import reflex as rx
from ..styles import general_styles as gs

from ..styles import proyects_style

projects_data = [
    {
        "title": "Sistema de Automatización",
        "description": "Herramienta interna de automatización con Google Apps Script y JavaScript para optimizar flujos de trabajo y reducir procesos manuales en Alimentos Cárnicos.",
        "tech": ["JavaScript", "Google Apps Script", "Google Sheets"],
        "year": "2025",
        "role": "Desarrollador Principal",
        "preview": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&h=400&fit=crop",
        "github": "https://github.com/",
        "youtube": "https://youtube.com/",
    },
    {
        "title": "Sistema de Asistencia",
        "description": "Sistema web para gestión de asistencia y excusas desarrollado para el SENA, con diseño responsivo para múltiples dispositivos.",
        "tech": ["HTML", "CSS", "JavaScript"],
        "year": "2020",
        "role": "Desarrollador Front-End",
        "preview": "https://images.unsplash.com/photo-1547082299-de196ea013d6?w=800&h=400&fit=crop",
        "github": "https://github.com/",
        "youtube": "https://youtube.com/",
    },
    {
        "title": "API REST – Django",
        "description": "API RESTful construida con Django y PostgreSQL, implementando autenticación, operaciones CRUD y patrones de arquitectura limpia.",
        "tech": ["Python", "Django", "PostgreSQL", "REST"],
        "year": "2024",
        "role": "Desarrollador Backend",
        "preview": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&h=400&fit=crop",
        "github": "https://github.com/",
        "youtube": "https://youtube.com/",
    },
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
                        style=proyects_style.preview_image_style,
                    ),
                    style=proyects_style.preview_image_container_style,
                    position="relative",
                ),
                rx.text(
                    ProjectsState.current_year,
                    style=proyects_style.year_badge_style,
                ),
                # Content section
                rx.box(
                    rx.text(
                        ProjectsState.current_role,
                        style=proyects_style.role_label_style,
                    ),
                    rx.heading(
                        ProjectsState.current_title,
                        style=proyects_style.title_style,
                        as_="h3",
                    ),
                    rx.text(
                        ProjectsState.current_description,
                        style=proyects_style.description_style,
                    ),
                    rx.box(
                        rx.foreach(
                            ProjectsState.current_tech,
                            lambda tech: rx.text(tech, style=proyects_style.tech_tag_style),
                        ),
                        style=proyects_style.tech_tags_container_style,
                    ),
                    rx.box(
                        rx.link(
                            rx.icon("github", size=15),
                            " GitHub",
                            href=ProjectsState.current_github,
                            is_external=True,
                            style=proyects_style.github_button_style,
                        ),
                        rx.link(
                            rx.icon("youtube", size=15),
                            " YouTube",
                            href=ProjectsState.current_youtube,
                            is_external=True,
                            style=proyects_style.youtube_button_style,
                        ),
                        style=proyects_style.links_row_style,
                    ),
                    style=proyects_style.content_wrapper_style,
                ),
                style=proyects_style.card_style,
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
                                proyects_style.active_dot_style,
                                proyects_style.inactive_dot_style,
                            ),
                        )
                        for i in range(len(projects_data))
                    ],
                    style=proyects_style.dots_container_style,
                ),
                rx.box(
                    rx.button(
                        rx.icon("chevron-left", size=18),
                        on_click=ProjectsState.prev_project,
                        style=proyects_style.arrow_button_style,
                    ),
                    rx.text(
                        ProjectsState.current_position,
                        style=proyects_style.counter_style,
                    ),
                    rx.button(
                        rx.icon("chevron-right", size=18),
                        on_click=ProjectsState.next_project,
                        style=proyects_style.arrow_button_style,
                    ),
                    style=proyects_style.arrows_container_style,
                ),
                style=proyects_style.navigation_container_style,
                margin_top="1.5rem",
                width="100%",
            ),
            width="100%",
            style=gs.container_style,
        ),
    )
