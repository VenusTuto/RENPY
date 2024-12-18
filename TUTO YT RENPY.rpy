##### TEXTBUTTON RENPY #####
## Contenedor para los botones  
    vbox:  
        xalign 0.1  
        yalign 0.5  
        spacing 15  

## Espaciado entre botones  
        textbutton "Jugar" action Start()  
        textbutton "Cargar" action ShowMenu("load")  
        textbutton "Opciones" action ShowMenu("preferences")  
        textbutton "Acerca de" action ShowMenu("about")  
        textbutton "Ayuda" action ShowMenu("help")  
        textbutton "Salir" action Quit() 
