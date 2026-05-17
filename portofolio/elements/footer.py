import reflex as rx
from ..styles import footer_styles as fs


def footer() -> rx.Component:
	return rx.box(
		rx.flex(
			rx.hstack(
				rx.box(style=fs.status_dot_style),
				rx.text("Las variables y nuestro cerebro, contienen la informacion que compartiremos y usaremos en un futuro", style=fs.status_text_style),
				style=fs.status_wrap_style,
			),
			
			rx.hstack(
				rx.text("Bogota, Colombia", style=fs.time_text_style),
			),
			rx.hstack(
				rx.link(
					rx.hstack(
						rx.icon("github", size=13),
						rx.text("GitHub"),
						style=fs.social_link_style,
					),
					href="https://github.com/KevinMorenoDOD",
					is_external=True,
				),
				rx.link(
					rx.hstack(
						rx.icon("linkedin", size=13),
						rx.text("LinkedIn"),
						style=fs.social_link_style,
					),
					href="https://www.linkedin.com/in/kevin-felipe-moreno-ramirez-863b59144/",
					is_external=True,
				),
				rx.text("(c) 2026 Kevin F. Moreno", style=fs.copyright_style),
			spacing="5",
				wrap="wrap",
			),
			align_items="center",
			justify="between",
			direction="column",
			gap="3",
			style=fs.inner_style,
		),
		style=fs.section_style,
	)
