from . import general_styles as gs
subtitle_style = {
    "font_size": gs.font_medium,
    "font_weight": "bold",
    "padding_bottom": "0.5em",
    "margin_bottom": "0.4em",
    "border_bottom": f"0.18em solid {gs.border_color}",
    "min_width": "80%",
}

section_style = {
    "max_width": "72rem",
    "margin": "0 auto",
    "padding": ["3rem 1rem", "3.5rem 1.5rem", "4rem 2rem"],
}

experience_card_style = {
    "margin_bottom": "2.5rem",
    "width": "100%",
}

company_style = {
    "color": gs.secondary_foreground_color,
    "line_height": "0.8",
}

period_style = {
    "color": gs.secondary_foreground_color,
}

bullet_item_style = {
    "display": "flex",
    "align_items": "flex-start",
    "gap": "0.75rem",
    "color": gs.secondary_foreground_color,
}

bullet_dot_style = {
    "width": "0.375rem",
    "height": "0.375rem",
    "border_radius": "9999px",
    "background_color": gs.primary_color,
    "margin_top": "0.55rem",
}