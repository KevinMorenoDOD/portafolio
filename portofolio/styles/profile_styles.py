from . import general_styles as gs

hero_section_style = {
    "max_width": "72rem",
    "margin": "0 auto",
    "padding": ["5rem 1rem 2.5rem", "5.5rem 1.5rem 3rem", "6rem 2rem 3.5rem"],
}

hero_grid_style = {
    "display": "grid",
    "grid_template_columns": ["1fr", "1fr", "minmax(260px, 360px) 1fr"],
    "gap": ["2rem", "2.5rem", "4rem"],
    "align_items": "center",
}

avatar_container_style = {
    "display": "flex",
    "justify_content": ["center", "center", "flex-start"],
}

avatar_frame_style = {
    "position": "relative",
    "width": ["16rem", "17rem", "20rem"],
    "height": ["16rem", "17rem", "20rem"],
    "border_radius": "9999px",
    "overflow": "hidden",
    "border": f"3px solid {gs.primary_color}",
    "box_shadow": "0 0 40px rgba(58, 168, 159, 0.25)",
}

avatar_image_style = {
    "width": "100%",
    "height": "100%",
    "object_fit": "cover",
    "filter": "grayscale(100%)",
    "transition": "filter 700ms ease",
    "_hover": {
        "filter": "grayscale(0%)",
    },
}

headline_style = {
    "font_size": ["2.6rem", "3.2rem", "4.8rem"],
    "font_weight": "800",
    "line_height": "0.95",
    "letter_spacing": "-0.02em",
    "color": gs.foreground_color,
    "margin_bottom": "1rem",
}

location_row_style = {
    "display": "flex",
    "align_items": "center",
    "gap": "0.4rem",
    "color": gs.secondary_foreground_color,
    "margin_bottom": "1rem",
}

summary_style = {
    "font_size": "1rem",
    "line_height": "1.8",
    "max_width": "37rem",
    "color": gs.secondary_foreground_color,
    "margin_bottom": "1.6rem",
}

socials_row_style = {
    "display": "flex",
    "align_items": "center",
    "flex_wrap": "wrap",
    "gap": "1.1rem",
}

hstack_style = socials_row_style

social_link_style = {
    "display": "inline-flex",
    "align_items": "center",
    "gap": "0.45rem",
    "font_size": "0.95rem",
    "color": gs.foreground_color,
    "transition": "color 0.2s ease",
    "_hover": {
        "color": gs.primary_color,
    },
}

buttons_style = {
    "display": "inline-flex",
    "align_items": "center",
    "gap": "0.45rem",
    "border": f"1px solid {gs.primary_color}",
    "border_radius": "9999px",
    "background_color": gs.color_primary,
    "color": gs.foreground_color,
    "cursor": "pointer",
    "padding": "0.55rem 1rem",
    "font_size": gs.font_small,
    "white_space": "nowrap",
    "transition": "all 0.2s ease",
    "_hover": {
        "background_color": gs.border_color,
        "box_shadow": f"0 0 15px {gs.border_color}80",
    },
}

mail_button_style = {
    "display": "inline-flex",
    "align_items": "center",
    "gap": "0.45rem",
    "font_size": "0.95rem",
    "background": "transparent",
    "border": "none",
    "padding": "0",
    "cursor": "pointer",
    "color": gs.foreground_color,
    "transition": "color 0.2s ease",
    "_hover": {
        "color": gs.primary_color,
    },
}