
# Writen by Evert Ramos

# Import print functions
from utils.print import sucesso, aviso, padrao, erro, pergunta

from google.download_ips import baixar_arquivos_googlebots
from google.convert_to_cvs import converter_json_para_csv

# Escrever suas funções aqui
def main():
    sucesso('Sua função principal')

# Menu da aplicação
while True:
    print()
    padrao('Menu Principal:')
    padrao('1. Download files')
    padrao('2. Convert to CSV')
    padrao('0. Sair')
    print()
    padrao('00. Para sair em qualquer tela!')
    print()

    try:
        escolha = int(pergunta('Escolha uma opção: '))
        print('<fim [Menu]')
        print() 
    except ValueError:
        erro('Entrada inválida, por favor insira um número.')
        continue

    if escolha == 0:
        break
    elif escolha == 1:
        print('Você escolheu a Opção 1: Download files.')
        baixar_arquivos_googlebots()
    elif escolha == 2:
        print('Você escolheu a Opção 2: Convert to CSV.')
        converter_json_para_csv()
    else:
        print('Opção inválida, tente novamente.')

print('Programa encerrado.')