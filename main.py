import random

def obtener_recomendacion():
    acciones = [
        "Evita conducir, usa la bicicleta o camina.",
            "Usa el transporte público para reducir emisiones de CO₂,CO, NOx entre otros .",
            "Planta un árbol o cuida plantas en tu hogar par aumentar la combercion de Dióxido de carbono (CO₂) a Oxígeno.",
            "Reduce el uso de plásticos, lleva tu propia bolsa.",
            "Desconecta los dispositivos electrónicos que no usas.",
            "Participa u organiza actividades de limpieza comunitaria.",
            "Ahorra agua mientras te duchas o lavas los platos.",
            "Evita quemar basura, hojas y otros objetos, así como hacer fogatas en bosques o en plena ciudad.",
            "Recicla y separa tus residuos correctamente para obtener mas informacion porfavor visualizar el siguiente video https://www.youtube.com/watch?v=IoWmF0fo2Wc.",
            "Apoya empresas que utilizan prácticas sostenibles como Grupo Bimbo que ha realizado inversiones significativas en energía eólica y solar, coca cola con iniciativa global para el reciclaje de envases. Bajo el lema “Un Mundo sin Residuos”, Coca-Cola Además, Coca-Cola se ha enfocado en la gestión sostenible del agua, Banco Santander Se ha posicionado como una entidad financiera líder en sostenibilidad, integrando prácticas responsables y ecológicas en su modelo de negocio entre otras ."
    ]
    
    return random.choice(acciones)

def main():
    print("¡Bienvenido a la app de recomendaciones ecológicas!")
    while True:
        input("Presiona Enter para recibir una recomendación.")
        recomendacion = obtener_recomendacion()
        print(f"\nRecomendación: {recomendacion}\n")
        continuar = input("¿Quieres otra recomendación? (s/n): ")
        if continuar.lower() != 's':
            break
    print("Gracias por contribuir al cuidado del medio ambiente.")

if __name__ == "__main__":
    main()

