from . import general_styles as gs

group_wrapper_style = {
    "margin_bottom": "2rem",
}

group_title_style = {
    "font_size": "1rem",
    "font_weight": "700",
    "color": gs.foreground_color,
    "margin_bottom": "0.5rem",
}


badges_row_style = {
    "display": "flex",
    "flex_wrap": "wrap",
    "gap": "0.75rem",
    "align_items": "center",
}

badge_style = {
    "display": "inline-flex",
    "align_items": "center",
    "gap": "0.45rem",
    "padding": "0.5rem 0.85rem",
    "border_radius": "9999px",
    "background_color": gs.color_primary,
    "border": f"1px solid {gs.border_color}",
    "color": gs.foreground_color,
    "font_size": "0.95rem",
    "transition": "all 0.2s ease",
    "white_space": "nowrap",
    "_hover": {
        "transform": "translateY(-2px)",
        "box_shadow": f"0 0 14px {gs.border_color}66",
    },
}

badge_icon_style = {
    "height": "1.1rem",
    "width": "1.1rem",
    "object_fit": "contain",
}