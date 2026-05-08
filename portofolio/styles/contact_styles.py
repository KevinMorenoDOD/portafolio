from . import general_styles as gs

section_style = {
    "max_width": "72rem",
    "margin": "0 auto",
    "padding": ["3rem 1rem", "4rem 1.5rem", "5rem 2rem"],
    "border_top": f"1px solid {gs.secondary_color}",
}

divider_style = {
    "height": "3px",
    "width": "120px",
    "background": f"linear-gradient(90deg, {gs.primary_color}, transparent)",
    "border_radius": "2px",
    "margin_bottom": "2.5rem",
}

description_style = {
    "font_size": "1.15rem",
    "line_height": "1.7",
    "color": gs.secondary_foreground_color,
    "max_width": "40rem",
    "margin_bottom": "2rem",
}

form_container_style = {
    "max_width": "100%",
    "width": "100%",
}

input_style = {
    "width": "100%",
    "background_color": gs.card_color,
    "border": f"1.5px solid {gs.secondary_color}",
    "border_radius": "0.5rem",
    "color": gs.foreground_color,
    "font_size": "1.1rem",
    "min_height": "3.5rem",
    "&::placeholder": {
        "color": gs.secondary_foreground_color,

    },
    "_focus": {
        "border_color": gs.secondary_foreground_color,
        "box_shadow": f"0 0 0 2px {gs.primary_color}33",
        "outline": "none",
    },
}

placeholder_color = gs.secondary_foreground_color

submit_button_style = {
    "width": "100%",
    "padding": "1rem 1.5rem",
    "background_color": gs.primary_color,
    "color": gs.primary_foreground_color,
    "border": "none",
    "border_radius": "0.5rem",
    "font_weight": "700",
    "font_size": "1.1rem",
    "cursor": "pointer",
    "gap": "0.75rem",
    "min_height": "3.5rem",
}

success_message_style = {
    "text_align": "center",
    "padding": "4rem 1rem",
    "font_size": "1.125rem",
    "font_weight": "600",
    "color": gs.primary_color,
}

popup_overlay_style = {
    "position": "fixed",
    "inset": "0",
    "background_color": "rgba(0, 0, 0, 0.55)",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "z_index": "9999",
}

popup_card_style = {
    "background_color": gs.card_color,
    "border": f"1px solid {gs.secondary_color}",
    "border_radius": "0.75rem",
    "padding": "2rem 2.5rem",
    "max_width": "26rem",
    "width": "90%",
    "text_align": "center",
    "box_shadow": "0 12px 30px rgba(0, 0, 0, 0.4)",
    "position": "relative",
}

popup_close_button_style = {
    "position": "absolute",
    "top": "0.75rem",
    "right": "0.75rem",
    "background_color": "transparent",
    "border": "none",
    "color": gs.secondary_foreground_color,
    "font_size": "1.2rem",
    "cursor": "pointer",
}
