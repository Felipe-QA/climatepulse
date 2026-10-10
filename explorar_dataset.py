import csv

with open("data/raw/StormEvents_details-ftp_v1.0_d2020_c20201216.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    num_linha = 0
    tipos_eventos = set()
    for l in leitor:
        eventos = l["EVENT_TYPE"]
        tipos_eventos.add(eventos)
        num_linha += 1
    print(leitor.fieldnames)
    print(len(tipos_eventos))
    print(sorted(tipos_eventos))
    print(num_linha)