### TEXTBUTTON MENU PRINCIPAL RENPY ###
## Contenedor para los botones  
    vbox:  
        xalign 0.5  
        yalign 0.5  
        spacing 15  

## Espaciado entre botones  
        textbutton "Comenzar" action Start()  
        textbutton "Cargar" action ShowMenu("load")  
        textbutton "Opciones" action ShowMenu("preferences")  
        textbutton "Acerca de" action ShowMenu("about")  
        textbutton "Ayuda" action ShowMenu("help")  
        textbutton "Salir" action Quit()    


### IMAGEBUTTON MENU PRINCIPAL RENPY###
imagebutton idle "jugar_idle.png" hover "jugar_hover.png" xpos 500 ypos 500 focus_mask True action Start()
imagebutton idle "cargar_idle.png" hover "cargar_hover.png" xpos 500 ypos 600 focus_mask True action ShowMenu("load")
imagebutton idle "opciones_idle.png" hover "opciones_hover.png" xpos 500 ypos 700 focus_mask True action ShowMenu("preferences")
imagebutton idle "salir_idle.png" hover "salir_hover.png" xpos 500 ypos 800 focus_mask True action Quit(confirm=not main_menu)



### IMAGEBUTTON QUICK MENU ###
imagebutton idle "images/SCREENS/Rollback_idle.png" hover "images/SCREENS/Rollback_hover.png" action Rollback()
imagebutton idle "images/SCREENS/Save_idle.png" hover "images/SCREENS/Save_hover.png" action ShowMenu('save')
imagebutton idle "images/SCREENS/History_idle.png" hover "images/SCREENS/History_hover.png" action ShowMenu('history')
imagebutton idle "images/SCREENS/Skip_idle.png" hover "images/SCREENS/Skip_hover.png" action Skip() alternate Skip(fast=True, confirm=True)
imagebutton idle "images/SCREENS/Auto_idle.png" hover "images/SCREENS/Auto_hover.png" action Preference("auto-forward", "toggle")
imagebutton idle "images/SCREENS/QuickSave_idle.png" hover "images/SCREENS/QuickSave_hover.png" action QuickSave()
imagebutton idle "images/SCREENS/QuickLoad_idle.png" hover "images/SCREENS/QuickLoad_hover.png" action QuickLoad()
imagebutton idle "images/SCREENS/Preferences_idle.png" hover "images/SCREENS/Preferences_hover.png" action ShowMenu('preferences')



#### Suscríbete al canal para más contenido así ####
#### Venus Tuto en Youtube ####
#### Link: https://www.youtube.com/channel/UCwGTqFwJxa8B_8yfTjmx_1A ####
