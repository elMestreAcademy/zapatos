class Zapato:
    cantidad_de_instancias = 0

    def __init__(self, forma, material, color, nombre):
        Zapato.cantidad_de_instancias += 1
        self.megas = len(nombre)
        self.forma = forma
        self.material = material
        self.color = color
        self.nombre = nombre
        self.usos = 0
        self.dmg = "Ouch"
        self.suciedad = 0

    def usar(self):
        self.usos += 1

    def describete(self):
        return f"{self.forma} --- {self.usos}"

    def __str__(self):
        return f"{self.nombre}: {self.color}"

    def patada(self):
        print(f"El enemigo grito: {self.dmg} al gopear \
            con la {self.forma}. Viva los {self.nombre}")


class Bota(Zapato):
    def __init__(self, material, color, nombre):
        super().__init__("Bota", material, color, nombre)
        self.usos = 10

    def patada(self):
        self.dmg = "OOOUCH"
        super().patada()


zapatos = [
    Zapato("sandalia", "cuero", "azul", "carmenes"),
    Zapato("Tacones", "charol", "rojo", "lucios"),
    Bota("piel", "negra", "pacos"),
    Bota("Tela", "Amarilla", "lucias"),
    Bota("Plastico", "Violeta", "marianas"),
]

# lista_de_zapatos[0].patada()
# lista_de_zapatos[2].patada()

# print(lista_de_zapatos[2].cantidad_de_instancias)

for pieza_de_ropa_que_va_en_el_pie in zapatos:
    print(pieza_de_ropa_que_va_en_el_pie)
    pieza_de_ropa_que_va_en_el_pie.patada()
