def calculate_copies(card_list):
    total_cards = len(card_list)
    copy_counts = [1] * total_cards

    for card_index, card in enumerate(card_list):
        hit_count = len(set(card['winning']) & set(card['yours']))
        for offset in range(1, hit_count + 1):
            target_index = card_index + offset
            if target_index < total_cards:
                copy_counts[target_index] += copy_counts[card_index]

    return sum(copy_counts)


def load_cards(file_path):
    card_list = []
    try:
        with open(file_path, "r") as input_file:
            for line_str in input_file:
                winning_part, your_part = line_str.strip().split("|")
                
                winning_numbers = list(map(int, winning_part.split(":")[1].strip().split()))
                your_numbers   = list(map(int, your_part.strip().split()))
                
                card_list.append({
                    "winning": winning_numbers,
                    "yours":   your_numbers
                })
        return card_list
    except Exception as error:
        print(f"No se pudo acceder al archivo: {error}")
        return []


if __name__ == "__main__":
    cards = load_cards('cards_input.txt')
    if cards:
        total_copies = calculate_copies(cards)
        print(total_copies)
    else:
        print("No se pudieron calcular las copias porque no se cargaron las tarjetas")
