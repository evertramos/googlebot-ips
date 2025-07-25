import json
import csv
import glob

def converter_json_para_csv(output='google_ip_ranges.csv'):
    arquivos = glob.glob("*.json")

    with open(output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(['source', 'type', 'prefix'])

        for nome_arquivo in arquivos:
            with open(nome_arquivo, 'r') as f:
                data = json.load(f)
                for prefixo in data.get('prefixes', []):
                    if 'ipv4Prefix' in prefixo:
                        # writer.writerow([nome_arquivo.replace('.json',''), 'ipv4', prefixo['ipv4Prefix']])
                        writer.writerow([prefixo['ipv4Prefix'], nome_arquivo.replace('.json','') +   '-ipv4', ])
                    if 'ipv6Prefix' in prefixo:
                        # writer.writerow([nome_arquivo.replace('.json',''), 'ipv6', prefixo['ipv6Prefix']])
                        writer.writerow([prefixo['ipv6Prefix'], nome_arquivo.replace('.json','') +   '-ipv6', ])

    print(f"Arquivo CSV gerado: {output}")
