import os
import json

def generar_json_productos(ruta_carpeta, nombre_json):
    productos = []
    for archivo in os.listdir(ruta_carpeta):
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
            codigo = os.path.splitext(archivo)[0]
            producto = {
                "nombre": "Joya",  # Puedes personalizar esto según el tipo
                "codigo": codigo,
                "imagen": f"{ruta_carpeta}/{archivo}",
                "descripcion": "Joya exclusiva, diseño moderno y elegante."
            }
            productos.append(producto)
    with open(nombre_json, 'w', encoding='utf-8') as f:
        json.dump(productos, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    # Ajusta la ruta si ejecutas desde otro directorio
    generar_json_productos('joyas', 'joyas.json')
    print("Archivo joyas.json generado correctamente.")
