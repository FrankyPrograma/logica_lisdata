def calculate_points(card_list):
    total_points = 0
    
    for card in card_list:
        match_count = len(set(card['winning']) & set(card['yours']))
        if match_count > 0:
            total_points += 2 ** (match_count - 1)
    
    return total_points


def load_cards(file_path):
    card_list = []
    try:
        with open(file_path, "r") as input_file:
            for line in input_file:
                winning_part, your_part = line.strip().split("|")
                winning_nums = list(map(int, winning_part.split(":")[1].strip().split()))
                your_nums   = list(map(int, your_part.strip().split()))
                card_list.append({
                    "winning": winning_nums,
                    "yours":   your_nums
                })
        return card_list
    except Exception as error:
        print(f"No se pudo acceder al archivo: {error}")
        return []


if __name__ == "__main__":
    card_list = load_cards('cards_input.txt')
    if card_list:
        total_points = calculate_points(card_list)
        print(total_points)
    else:
        print("No se pudieron calcular los puntos porque no se cargaron las tarjetas")
