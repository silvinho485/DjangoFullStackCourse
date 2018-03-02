import random

def devolve_palavra():
    palavras=["cachaça", "garrafa", "caneta", "caneca", "cadeira", "tecnica",
              "biologia", "maconha", "maconheiro", "comunista", "aguinha", "gasinho",
              "quebrado", "pregunton", "genitais", "queimadura", "coqueteleira",
              "cavalaria", "monitoramente", "firewall", "sapeco", "perplecto",
              "chimarrão", "batalha", "linkpradiaria", "agile", "desenhista",
              "amigo", "arroto", "perereca", "android", "esquerdista", "arrombado",
              "cafe", "chiclete", "allegro", "altis", "montserrat", "papacu",
              "hombrecabron", "movistar", "flatulencia", "casinha", "detergente",
              "atrasado", "barbudo", "paralelepipedo", "xinforinfola",
              "aquifaroseselamo", "ironmaidennão", "bibiana", "jorgeversilo",]
    return random.choice(palavras)
