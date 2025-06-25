import os
import json

def generar_json_productos(ruta_carpeta, nombre_json, nombre_generico, descripcion_generica):
    productos = []
    for archivo in os.listdir(ruta_carpeta):
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
            codigo = os.path.splitext(archivo)[0]
            producto = {
                "nombre": nombre_generico,
                "codigo": codigo,
                "imagen": f"{ruta_carpeta}/{archivo}",
                "descripcion": descripcion_generica
            }
            productos.append(producto)
    with open(nombre_json, 'w', encoding='utf-8') as f:
        json.dump(productos, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    carpetas = [
        ("joyas", "joyas.json", "Joya", "Joya exclusiva, diseño moderno y elegante."),
        ("carteras", "carteras.json", "Cartera", "Cartera de moda, práctica y elegante."),
        ("perfumes", "perfumes.json", "Perfume", "Fragancia original, aroma duradero."),
        ("ropa de caballero", "ropa_caballero.json", "Prenda Caballero", "Ropa de caballero de calidad y estilo."),
        ("ropa de dama", "ropa_dama.json", "Prenda Dama", "Ropa de dama moderna y cómoda."),
        ("ropa de niños", "ropa_ninos.json", "Prenda Niño", "Ropa para niños divertida y resistente."),
        ("ropa interior femenina", "ropa_interior_femenina.json", "Ropa Interior Femenina", "Comodidad y estilo para ella."),
        ("ropa interior masculina", "ropa_interior_masculina.json", "Ropa Interior Masculina", "Comodidad y estilo para él.")
    ]
    for carpeta, json_file, nombre, descripcion in carpetas:
        if os.path.exists(carpeta):
            generar_json_productos(carpeta, json_file, nombre, descripcion)
            print(f"Archivo {json_file} generado correctamente.")
        else:
            print(f"Carpeta {carpeta} no encontrada, se omite.")
