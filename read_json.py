import sys
import json

{'nome': 'Alice', 'idade': 16, 'localiza¸c~ao': 'Pa´ıs das Maravilhas'}

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f'2 {json.dumps(data, indent=4)}')
            print('Processo concluído!')
    except FileNotFoundError:
        print("Ocorreu um erro! ")
        print('Processo concluído!')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso correto: python script.py <caminho_do_arquivo>")
    else:
        read_json(sys.argv[1])