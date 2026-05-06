from . import general_styles as gs
navbar_buttons_style = {
    "padding": gs.padding_standard,
    
    "border": f"2px solid {gs.border_color}",
    "border_radius": "10em",
    
    "cursor": "pointer",
    
    "max_width": "7em",
    "min_width": "4em",

    "bg_color": gs.color_primary,
    "color": "white",   
    "font_size": gs.font_medium_min,
       
    "_hover": {
        "background_color": gs.border_color,
        "box_shadow": f"0 0 15px {gs.border_color}80",
    }
}


navbar_style_fixed = {

    "position":"fixed",
    "top":"0px",
    "z_index":"5",
    "width":"100%",
    "left":"0",
    "right":"0",
    "margin":"0",
    "padding":"1em 0",
    "background_color":gs.color_page,
    "display":"flex",
    "justify_content":"center",
    "align_items":"center",
    "box_shadow": "0 4px 12px rgba(42, 161, 145, 0.15)",

}
