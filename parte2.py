cards = []

with open("cards_input.txt", "r") as file:
    for line in file:
        left, right = line.strip().split("|")

        winning_numbers = list(map(int, left.split(":")[1].strip().split()))
        your_numbers = list(map(int, right.strip().split()))
        
        cards.append({
            "winning": winning_numbers,
            "yours": your_numbers
        })