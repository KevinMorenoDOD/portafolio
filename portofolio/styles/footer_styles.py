from . import general_styles as gs

section_style = {
    "background_color": gs.background_color,
    "border_top": f"1px solid {gs.secondary_color}",
    "padding": "1.5rem 1.5rem",
}

inner_style = {
    "max_width": "72rem",
    "margin": "0 auto",
    "width": "100%",
}

status_wrap_style = {
    "display": "flex",
    "align_items": "center",
    "gap": "0.5rem",
}

status_dot_style = {
    "width": "0.5rem",
    "height": "0.5rem",
    "border_radius": "9999px",
    "background_color": gs.primary_color,
}

status_text_style = {
    "font_size": "0.7rem",
    "text_transform": "uppercase",
    "letter_spacing": "0.18em",
    "color": gs.primary_color,
}

time_text_style = {
    "font_size": "0.8rem",
    "letter_spacing": "0.08em",
    "color": "#555555",
}

social_link_style = {
    "font_size": "0.8rem",
    "color": gs.secondary_foreground_color,
    "display": "flex",
    "align_items": "center",
    "gap": "0.35rem",
}

copyright_style = {
    "font_size": "0.8rem",
    "color": "#444444",
}
