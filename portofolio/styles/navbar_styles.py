from . import general_styles as gs

navbar_shell_style = {
    "position": "sticky",
    "width": "100%",
    "top": "0",
    "z_index": "50",
    "background_color": gs.background_color,
    "border_bottom": f"1px solid {gs.border_color}",
    "backdrop_filter": "blur(10px)",
    "box_shadow": "0 8px 24px rgba(0, 0, 0, 0.12)",
}

navbar_inner_style = {
    "width": "100%",
    "max_width": "72rem",
    "margin": "0 auto",
    "padding": ["0.85rem 1rem", "0.9rem 1.5rem", "1rem 2rem"],
    "display": "flex",
    "align_items": "center",
    "justify_content": "space-between",
    "gap": "1rem",
    "flex_wrap": "wrap",
}

navbar_brand_style = {
    "font_size": gs.font_small,
    "font_weight": "700",
    "letter_spacing": "0.18em",
    "text_transform": "uppercase",
    "color": gs.primary_color,
    "white_space": "nowrap",
}

navbar_links_style = {
    "display": "flex",
    "align_items": "center",
    "justify_content": "flex-end",
    "flex_wrap": "wrap",
    "gap": "0.6rem",
}

navbar_button_style = {
    "border": f"1px solid {gs.primary_color}",
    "border_radius": "9999px",
    "background_color": "transparent",
    "color": "white",
    "cursor": "pointer",
    "padding": "0.55rem 1rem",
    "font_size": gs.font_small,
    "transition": "all 0.2s ease",
    "white_space": "nowrap",
    "_hover": {
        "background_color": gs.border_color,
        "box_shadow": f"0 0 15px {gs.border_color}80",
        "transform": "translateY(-1px)",
    },
}
