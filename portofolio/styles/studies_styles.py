from . import general_styles as gs

title_style = {
    "font_size": gs.font_large,
    "font_weight": "bold",
    "padding_bottom": "0.5em",
    "border_bottom": f"0.2em solid {gs.border_color}",
    "margin_bottom": "0.5em",
    "min_width": "100%",
    "text_align": "center",
}

cards_wrap_style = {
    "display": "grid",
    "grid_template_columns": ["1fr", "repeat(2, minmax(0, 1fr))", "repeat(2, minmax(0, 1fr))"],
    "gap": "1.5rem",
    "margin_top": "1rem",
}

card_style = {
    "background_color": gs.card_color,
    "border": f"1px solid {gs.secondary_color}",
    "border_radius": "0.75rem",
    "padding": "1.5rem",
    "transition": "all 300ms ease",
    "width": "100%",
    "min_width": 0,
}

icon_shell_style = {
    "width": "2.5rem",
    "height": "2.5rem",
    "border_radius": "9999px",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "margin_top": "0.25rem",
    "background_color": "rgba(58,168,159,0.12)",
    "border": "1px solid rgba(58,168,159,0.3)",
}

year_style = {
    "font_size": "0.75rem",
    "font_weight": "700",
    "text_transform": "uppercase",
    "letter_spacing": "0.12em",
    "color": gs.primary_color,
}

degree_style = {
    "font_size": gs.font_medium,
    "font_weight": "700",
    "margin_top": "0.25rem",
    "margin_bottom": "0.125rem",
    "color": gs.foreground_color,
}

institution_style = {
    "font_size": "0.95rem",
    "font_weight": "600",
    "color": gs.secondary_foreground_color,
}

detail_style = {
    "font_size": "0.95rem",
    "color": "#666666",
    "margin_top": "0.25rem",
}