from helpers import (
    show_menu,
    insert_data,
    show_data,
    update_data,
    delete_data,
    calculate_area,
    calculate_inputs,
    get_valid_input,
    export_data_to_csv
)

cultures = []

def main() -> None:
    """
    Runs the console-based menu system.

    Maps user input to designated operations by calling predefined functions.
    Option "7" terminates the program.
    """
    cultures = []
    operations = {
        "1": lambda: insert_data(cultures),
        "2": lambda: show_data(cultures),
        "3": lambda: update_data(cultures),
        "4": lambda: delete_data(cultures),
        "5": lambda: calculate_area(cultures),
        "6": lambda: calculate_inputs(cultures),
        "7": lambda: export_data_to_csv(cultures)  
    }

    while True:
        show_menu()
        opcao: str = get_valid_input("Escolha uma opção: ", str).strip()
        print("\n")

        if opcao == "8":
            print("Encerrando o programa...")
            break
        elif opcao in operations:
            try:
                operations[opcao]()
            except Exception as e:
                print(f"Erro ao executar a operação: {e}")
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
