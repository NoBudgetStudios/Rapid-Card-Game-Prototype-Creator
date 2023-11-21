import Card

def read_cards(file_name):
    card_list = []

    with open(file_name, 'r', encoding='utf8') as file:
        lines = file.readlines()
        # Skip the first line (header)
        for line in lines[1:]:
            card_data = line.strip().split('|')
            # Convert numerical attributes to integers
            card = Card.Card(card_data[1], card_data[2], card_data[3],
                             card_data[4], card_data[5], card_data[6], card_data[7], card_data[8],
                             card_data[9],  card_data[10])
            card_list.append(card)

    return card_list
