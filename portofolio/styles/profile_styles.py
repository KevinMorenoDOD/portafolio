from . import general_styles as gs

img_style={
    "width": "20em",
    "border_radius": "100%",
    "margin": "0.8em",
}

hstack_style={
    "max_height": "20em",
    "min_height": "3em",
    "align_items": "center",
    "gap": "1.5em",
    "margin": "1em 0",
}


buttons_style={
    "bg_color": gs.color_primary,
    "font_size": gs.font_small,
    "color": "white",
    "padding": gs.padding_standard,
    "border_radius": "10em",
    "cursor": "pointer",
    "min_width": "9em",

    "_hover": {
        "background_color": gs.border_color,
        "box_shadow": f"0 0 15px {gs.border_color}80",
    }
}