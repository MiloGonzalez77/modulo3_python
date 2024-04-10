from api_get import obtener_datos
from templates import template_html

#Obtener datos desde api_get
datos_aves = obtener_datos()

#Generar plantilla de templates
plantilla_str = template_html(datos_aves)

#Abrir HTML
with open('aves_de_chile.html', 'w') as f:
        f.write(plantilla_str)

print("Archivo HTML generado exitosamente: aves_de_chile.html")