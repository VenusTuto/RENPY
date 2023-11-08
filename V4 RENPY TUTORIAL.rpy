### TEXTBUTTON MENU PRINCIPAL RENPY ###
textbutton _("Comenzar") xpos 500 ypos 500 action Start()
textbutton _("Cargar") xpos 500 ypos 550 action ShowMenu("load")
textbutton _("Opciones") xpos 500 ypos 600 action ShowMenu("preferences")
textbutton _("Información") xpos 500 ypos 650 action ShowMenu("about")
textbutton _("Salir") xpos 500 ypos 700 action Quit(confirm=not main_menu)


### IMAGEBUTTON MENU PRINCIPAL RENPY###
imagebutton idle "jugar_idle.png" hover "jugar_hover.png" xpos 500 ypos 500 focus_mask True action Start()
imagebutton idle "cargar_idle.png" hover "cargar_hover.png" xpos 500 ypos 600 focus_mask True action ShowMenu("load")
imagebutton idle "opciones_idle.png" hover "opciones_hover.png" xpos 500 ypos 700 focus_mask True action ShowMenu("preferences")
imagebutton idle "salir_idle.png" hover "salir_hover.png" xpos 500 ypos 800 focus_mask True action Quit(confirm=not main_menu)


#### Suscríbete al canal para más contenido así ####
#### Venus Tuto en Youtube ####
#### Link: https://www.youtube.com/channel/UCwGTqFwJxa8B_8yfTjmx_1A ####