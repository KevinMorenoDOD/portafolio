from . import general_styles as gs

section_style = {
    "max_width": "72rem",
    "margin": "0 auto",
    "padding": ["4.5rem 1rem", "5rem 1.5rem", "5.5rem 2rem"],
}

card_style = {
    "width": ["100%", "44rem", "52rem"],
    "max_width": ["100%", "44rem", "52rem"],
    "box_sizing": "border-box",
    "margin_left": "auto",
    "margin_right": "auto",
    "background_color": gs.card_color,
    "border": f"1px solid {gs.border_color}",
    "border_radius": "0.75rem",
    "overflow": "hidden",
    "box_shadow": "0 4px 32px rgba(0, 0, 0, 0.4)",
    "transition": "all 500ms ease",
}

preview_image_container_style = {
    "position": "relative",
    "width": "100%",
    "height": ["13rem", "14rem", "13rem"],
    "overflow": "hidden",
}

preview_image_style = {
    "width": "100%",
    "height": "100%",
    "object_fit": "cover",
    "filter": "brightness(0.75) saturate(0.7)",
}

year_badge_style = {
    "position": "absolute",
    "top": "1rem",
    "right": "1rem",
    "font_size": "0.75rem",
    "font_weight": "700",
    "padding": "0.25rem 0.75rem",
    "border_radius": "9999px",
    "background_color": "rgba(58, 168, 159, 0.85)",
    "color": "#fff",
    "letter_spacing": "0.08em",
    "text_transform": "uppercase",
}

content_wrapper_style = {
    "padding": ["1.75rem", "1.75rem", "1.75rem"],
}

role_label_style = {
    "font_size": "0.75rem",
    "font_weight": "600",
    "letter_spacing": "0.08em",
    "text_transform": "uppercase",
    "color": gs.primary_color,
}

title_style = {
    "font_size": ["1.5rem", "1.75rem", "1.5rem"],
    "font_weight": "700",
    "margin_top": "0.5rem",
    "margin_bottom": "0.75rem",
    "line_height": "1.2",
    "color": gs.foreground_color,
}

description_style = {
    "font_size": "0.95rem",
    "line_height": "1.6",
    "margin_bottom": "1.25rem",
    "color": gs.secondary_foreground_color,
}

tech_tags_container_style = {
    "display": "flex",
    "flex_wrap": "wrap",
    "gap": "0.5rem",
    "margin_bottom": "1.5rem",
}

tech_tag_style = {
    "font_size": "0.8rem",
    "padding": "0.25rem 0.5rem",
    "border_radius": "9999px",
    "background_color": f"rgba(58, 168, 159, 0.12)",
    "color": gs.primary_color,
    "border": f"1px solid rgba(58, 168, 159, 0.25)",
    "font_weight": "500",
}

links_row_style = {
    "display": "flex",
    "align_items": "center",
    "gap": "1rem",
}

button_style = {
    "display": "inline-flex",
    "align_items": "center",
    "gap": "0.5rem",
    "font_size": "0.9rem",
    "font_weight": "600",
    "padding": "0.5rem 1rem",
    "border_radius": "0.5rem",
    "transition": "all 200ms ease",
    "border": "1.5px solid var_border_color",
}

github_button_style = {
    **button_style,
    "border": f"1.5px solid {gs.primary_color}",
    "color": gs.primary_color,
    "background_color": "transparent",
    "_hover": {
        "background_color": gs.primary_color,
        "color": gs.background_color,
    },
}

youtube_button_style = {
    **button_style,
    "border": "1.5px solid #e53e3e",
    "color": "#e53e3e",
    "background_color": "transparent",
    "_hover": {
        "background_color": "#e53e3e",
        "color": "#fff",
    },
}

navigation_container_style = {
    "display": "flex",
    "align_items": "center",
    "justify_content": "space-between",
    "margin_top": "1.5rem",
}

dots_container_style = {
    "display": "flex",
    "align_items": "center",
    "gap": "0.5rem",
}

dot_style = {
    "width": "0.5rem",
    "height": "0.5rem",
    "border_radius": "9999px",
    "background_color": gs.border_color,
    "cursor": "pointer",
    "transition": "all 300ms ease",
}

active_dot_style = {
    **dot_style,
    "width": "1.75rem",
    "background_color": gs.primary_color,
}

inactive_dot_style = {
    **dot_style,
    "width": "0.5rem",
}

arrows_container_style = {
    "display": "flex",
    "align_items": "center",
    "gap": "0.75rem",
}

arrow_button_style = {
    "width": "2.5rem",
    "height": "2.5rem",
    "border_radius": "9999px",
    "border": f"1.5px solid {gs.border_color}",
    "background_color": "transparent",
    "color": gs.secondary_foreground_color,
    "cursor": "pointer",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "transition": "all 200ms ease",
    "_hover": {
        "border_color": gs.primary_color,
        "color": gs.primary_color,
    },
}

counter_style = {
    "font_size": "0.8rem",
    "color": gs.secondary_foreground_color,
}
