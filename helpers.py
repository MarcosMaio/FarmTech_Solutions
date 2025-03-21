import os
import csv
from datetime import datetime
import uuid
import csv
import os
import uuid
from datetime import datetime
from typing import Any, Dict, List, Callable

SHAPES_MAPPING = {
    "1": "Triângulo",
    "2": "Retângulo"
}

def get_valid_input(prompt: str, cast):
    """
    Prompts the user for input and attempts to cast it to the desired type.
    Repeats until a valid input is received.
    
    Args:
        prompt (str): The prompt to display to the user.
        cast: The type to which the input should be cast.
        
    Returns:
        The casted value.
    """
    while True:
        try:
            return cast(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, tente novamente.")

def show_menu() -> None:
    """
    Exibe o menu de opções para o usuário.
    """
    menu = (
        "\n"
        "Menu de Opções:\n"
        "========================\n"
        "Escolha uma opção:\n"
        "1 - Inserir Dados\n"
        "2 - Exibir Dados\n"
        "3 - Atualizar Dados\n"
        "4 - Deletar Dados\n"
        "5 - Calcular Área\n"
        "6 - Calcular Insumo\n"
        "7 - Exportar Dados para CSV\n"
        "8 - Sair\n"
        "\n"
    )
    print(menu)

def exist_culture_data(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that checks if the 'cultures' argument is non-empty before
    executing the decorated function. If 'cultures' is empty, it prints a
    series of messages and returns early without calling the function.
    
    Args:
        func: The function to be decorated.
        
    Returns:
        A wrapper function that includes the culture data check.
    """
    def wrapper(cultures: List[Any], *args, **kwargs) -> Any:
        if not cultures:
            print(
                "\n"
                "Nenhuma cultura cadastrada.\n"
                "Por favor, cadastre uma cultura antes de continuar.\n"
                "Retornando ao menu principal... \n"
            )
            return
        return func(cultures, *args, **kwargs)
    return wrapper

def gather_culture_input() -> dict:
    """
    Gathers input from the user to create a culture record.
    
    Returns:
        dict: A dictionary representing the culture record.
    """
    name = input("Digite o nome da cultura: ")

    print("Escolha a forma geométrica:")
    for key, shape in SHAPES_MAPPING.items():
        print(f"{key}: {shape}")

    while True:
        shape_choice = input("Digite o número correspondente à forma geométrica desejada: ")
        if shape_choice in SHAPES_MAPPING:
            chosen_shape = SHAPES_MAPPING[shape_choice]
            break
        else:
            print("Opção inválida. Tente novamente.")

    base = get_valid_input("Digite a base: ", float)
    altura = get_valid_input("Digite a altura: ", float)
    product = input("Digite o nome do insumo: ")
    rate = get_valid_input("Digite a taxa de aplicação (mL/metro): ", float)
    streets = get_valid_input("Digite o número de ruas da lavoura: ", int)
    length = get_valid_input("Digite o comprimento de cada rua: ", float)

    return {
        "name": name,
        "shape": chosen_shape,
        "dimensions": {
            "base": base,
            "altura": altura
        },
        "inputs": {
            "product": product,
            "rate": rate,
            "streets": streets,
            "length": length
        }
    }

def insert_data(cultures: list) -> None:
    """
    Prompts the user to input culture data by gathering inputs, builds a culture record,
    and appends it to the provided list.
    
    Parameters:
        cultures (list): List to store culture records.
    """
    culture = gather_culture_input()
    cultures.append(culture)

@exist_culture_data
def show_data(cultures: list[dict]) -> None:
    """
    Print detailed information for each culture in the provided list.

    Args:
        cultures (list[dict]): List of culture dictionaries with keys 'name', 'shape',
                                'dimensions', and 'inputs'.
    """
    for i, culture in enumerate(cultures, start=1):
        print(f"Cultura {i}:")
        print(f"Nome: {culture['name']}")
        print(f"Forma: {culture['shape']}")
        dimensions = culture["dimensions"]
        print(f"Dimensões: Base - {dimensions['base']}, Altura - {dimensions['altura']}")
        inputs = culture["inputs"]
        print(f"Insumo: Produto - {inputs['product']}, Taxa - {inputs['rate']}, Ruas - {inputs['streets']}, Comprimento - {inputs['length']}")
        print()

@exist_culture_data
def update_data(cultures: list) -> None:
    """
    Updates the data of a selected culture from the list of cultures.
    
    The function displays current culture data, prompts the user for the index 
    of the culture to update, and then requests new inputs to update the culture's:
      - name
      - geometric shape (validated with a mapping)
      - dimensions: base and altura
      - inputs: product, rate, streets, and length

    If the provided index is invalid, an error message is printed.
    """
    show_data(cultures)
    
    indice: int = get_valid_input("Digite o índice da cultura que deseja atualizar: ", int) - 1

    if 0 <= indice < len(cultures):
        culture = cultures[indice]
        print(f"Atualizando dados da cultura: {culture['name']}")
    
        try:
            culture["name"] = get_valid_input("Digite o novo nome da cultura: ", str)
            
            print("Escolha a nova forma geométrica:")
            for key, shape in SHAPES_MAPPING.items():
                print(f"{key}: {shape}")
            
            while True:
                shape_choice: str = input("Digite o número correspondente à forma geométrica desejada: ")
                if shape_choice in SHAPES_MAPPING:
                    culture["shape"] = SHAPES_MAPPING[shape_choice]
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            
            culture["dimensions"]["base"] = get_valid_input("Digite a nova base: ", float)
            culture["dimensions"]["altura"] = get_valid_input("Digite a nova altura: ", float)
            
            culture["inputs"]["product"] = get_valid_input("Digite o novo nome do insumo: ", str)
            culture["inputs"]["rate"] = get_valid_input("Digite a nova taxa de aplicação (mL/metro): ", float)
            culture["inputs"]["streets"] = get_valid_input("Digite o novo número de ruas da lavoura: ", int)
            culture["inputs"]["length"] = get_valid_input("Digite o novo comprimento de cada rua: ", float)
        except KeyError as e:
            print(f"Erro de chave: {e}")
    else:
        print("Índice inválido.")

def confirm_and_delete(cultures: list, index: int) -> None:
    """
    Asks the user for confirmation and deletes the culture at the given index if confirmed.

    Args:
        cultures (list): List of culture entries.
        index (int): The index of the culture to delete.
    """
    confirm = get_valid_input(
        "Tem certeza que deseja deletar esta cultura? (s/n): ",
        lambda x: x.strip().lower() if x.strip().lower() in ['s', 'n'] else (_ for _ in ()).throw(ValueError())
    )
    if confirm == 's':
        cultures.pop(index)
        print("Cultura deletada com sucesso.")
    else:
        print("Operação cancelada.")

@exist_culture_data
def delete_data(cultures: list) -> None:
    """
    Displays cultures, prompts the user to delete a selected culture,
    confirms the deletion, and removes it if confirmed.

    Args:
        cultures (list): List of culture entries.
    """
    show_data(cultures)
    indice = get_valid_input("Digite o índice da cultura que deseja deletar: ", int) - 1

    if 0 <= indice < len(cultures):
        confirm_and_delete(cultures, indice)
    else:
        print("Índice inválido.")

@exist_culture_data
def calculate_area(cultures: List[Dict[str, Any]]) -> None:
    """
    Calculates and prints the area of a selected culture based on its geometrical shape.

    Args:
        cultures (list): A list of dictionaries, each containing 'name', 'shape', and
        'dimensions' keys. The 'dimensions' dictionary should have
        'base' and 'altura' values.
    """
    show_data(cultures)
    
    user_index = get_valid_input("Digite o índice da cultura para calcular a área: ", int)
    indice = user_index - 1

    if not (0 <= indice < len(cultures)):
        print("Índice inválido.")
        return

    culture = cultures[indice]
    if "shape" not in culture or "dimensions" not in culture:
        print("Dados incompletos para calcular a área.")
        return

    shape = culture["shape"].lower()
    dimensions = culture["dimensions"]
    if "base" not in dimensions or "altura" not in dimensions:
        print("Dimensões incompletas para calcular a área.")
        return

    base = dimensions["base"]
    altura = dimensions["altura"]

    area_calculators = {
        "retângulo": lambda base, altura: base * altura,
        "triângulo": lambda base, altura: (base * altura) / 2,
    }

    if shape in area_calculators:
        area = area_calculators[shape](base, altura)
        print(f"A área da cultura {culture['name']} é: {area} m²")
    else:
        print("Forma geométrica não suportada.")

@exist_culture_data
def calculate_inputs(cultures: list[dict]) -> None:
    """
    Displays culture data, prompts for a culture index, calculates the required input amount,
    and prints the result for the selected culture.
    
    Args:
        cultures (list[dict]): A list of culture dictionaries, each containing a 'name' and an 'inputs' 
        dictionary with keys 'rate', 'streets', and 'length'.
    """
    
    show_data(cultures)
    
    while True:
        indice = get_valid_input("Digite o índice da cultura para calcular o insumo: ", int)
        if 1 <= indice <= len(cultures):
            break
        print("Índice inválido. Por favor, tente novamente.")
    
    culture = cultures[indice - 1]
    if "inputs" in culture and all(k in culture["inputs"] for k in ["rate", "streets", "length"]):
        inputs = culture["inputs"]
        total_insumo = (inputs["rate"] * inputs["streets"] * inputs["length"]) / 1000
        print(f"A quantidade total de insumo necessária para a cultura {culture['name']} é: {total_insumo:.2f} L")
    else:
        print("Dados insuficientes para calcular o insumo da cultura selecionada.")

@exist_culture_data
def export_data_to_csv(cultures: list[dict], filename: str = None) -> None:
    """
    Exports the culture data to a CSV file with a dynamic filename if none is provided.
    
    If filename is not provided, a new file is created with a name based on the current 
    timestamp and a short UUID to ensure uniqueness.
    
    Args:
        cultures (list[dict]): A list of culture dictionaries.
        filename (str, optional): The CSV filename. Defaults to None.
    """
    if not cultures:
        print("Nenhuma cultura para exportar.")
        return

    directory = "cultures"
    os.makedirs(directory, exist_ok=True)

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = uuid.uuid4().hex[:6]
        filename = f"cultures_{timestamp}_{unique_id}.csv"
    filepath = os.path.join(directory, filename)

    FIELDNAMES = ['name', 'shape', 'base', 'altura', 'product', 'rate', 'streets', 'length']
    rows = []
    for culture in cultures:
        try:
            row = {
                'name': culture['name'],
                'shape': culture['shape'],
                'base': culture['dimensions']['base'],
                'altura': culture['dimensions']['altura'],
                'product': culture['inputs']['product'],
                'rate': culture['inputs']['rate'],
                'streets': culture['inputs']['streets'],
                'length': culture['inputs']['length']
            }
        except KeyError as e:
            print(f"Chave ausente em dados de cultura: {e}")
            continue
        rows.append(row)

    try:
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)
    except Exception as e:
        print(f"Erro ao exportar dados: {e}")
        return

    print(f"Dados exportados com sucesso para {filepath}")
