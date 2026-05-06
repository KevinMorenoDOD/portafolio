from . import general_styles as gs

tecnologies_style = {
    "bg_color": gs.color_primary,
    "font_size": gs.font_medium,
    "color": "white",   
    "padding": gs.padding_standard,
    "border_radius": "10em",
    "cursor": "pointer",
    "width": "7em",
}

tag_style ={
    "max_height": "2.2em",
    "bg_color": gs.color_primary,
    "font_size": gs.font_small,
    "color": "white",
    "padding": gs.padding_standard,
    "border_radius": "10em",
    "width": "9em",
    "align_items":"center",
    "justify_content":"center",
    "margin": "0.4em",

    "_hover": {
        "transform": "translateY(-3px)",
    }
}
tag_style_bordered ={
    "max_height": "2.2em",
    "bg_color": gs.color_primary,
    "font_size": gs.font_small,
    "color": "white",
    "padding": gs.padding_standard,
    "border_radius": "10em",
    "width": "9em",
    "align_items":"center",
    "justify_content":"center",
    "border": f"0.2em solid {gs.border_color}",
    "margin": "0.4em",
    "_hover": {
        "transform": "translateY(-3px)",
    }
}
img_style ={
    "max_height": "1.8em",
}

vstack_style = {
    "align_items":"center",
    "spacing":"2",
}