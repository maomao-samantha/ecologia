import random

def obtener_recomendacion():
    acciones = [
        "Evita conducir, usa la bicicleta o camina.",
        "Usa el transporte público para reducir emisiones.",
        "Planta un árbol o cuida plantas en tu hogar.",
        "Reduce el uso de plásticos, lleva tu propia bolsa.",
        "Desconecta los dispositivos electrónicos que no usas.",
        "Participa en actividades de limpieza comunitaria.",
        "Compra productos locales y de temporada.",
        "Ahorra agua mientras te duchas o lavas los platos.",
        "Recicla y separa tus residuos correctamente.",
        "Apoya empresas que utilizan prácticas sostenibles."
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
