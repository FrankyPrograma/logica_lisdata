from collections import defaultdict

def calculate_points(cards):
    resultado = 0
    cardsCoinciden = defaultdict(set)
    
    for i, card in enumerate(cards):
        for n in card["yours"]:
            if n in card["winning"]:
                cardsCoinciden[i].add(n)
                        
                    
    for coinciden in cardsCoinciden.values():
        n = len(coinciden)
        
        if n == 1: 
            resultado += n
        elif n > 1: 
            resultado += 2 ** (n - 1)
            
    return resultado


def load_cards(path):
    cards = []
    try:
        with open(path, "r") as file:
            for line in file:
                left, right = line.strip().split("|")

                winning_numbers = list(map(int, left.split(":")[1].strip().split()))
                your_numbers = list(map(int, right.strip().split()))
                
                cards.append({
                    "winning": winning_numbers,
                    "yours": your_numbers
                })
    
        return cards
    except Exception as e:
        print(f"No se pudo acceder al archivo: {e}")
        
cards = load_cards('cards_input.txt')

if cards: 
    result = calculate_points(cards=cards)
    print(result)
else:
    print("No se puedieron calcular los puntos porque no se cargaron las tarjetas")