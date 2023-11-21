import Card
import DbManager
import JsonManager
import TextManager
import CardDesigner
import random
import string

def main():

    cards_file_url = '.\\..\\data\\cards.txt'

    card_list_in = TextManager.read_cards(cards_file_url)
    # Create the cards table if it doesn't exist
    DbManager.create_db_if_not_exists()

    card_list = []
    
    for i in range(len(card_list_in)):
        new_card = generate_random_card(card_list_in[i])
        card_list.append(new_card)
        DbManager.insert_card(new_card)

        CardDesigner.design_card(new_card)
        
        

    JsonManager.export_cards_to_json(card_list)

def generate_random_card(card, generate_random_stats = False):
    # Generating random values for attributes
    title = card.get_title()
    subtitle = card.get_subtitle()
    text = card.get_text()
    if generate_random_stats:
        attack_value = random.randint(1, 6)
        range_value = random.randint(1, 6)
        defense_value = random.randint(1, 6)
        speed_value = random.randint(1, 6)
        value = (attack_value + range_value + defense_value + speed_value) // 4
    else:
        attack_value = -1
        range_value = -1
        defense_value = -1
        speed_value = -1
        value = -1

    layout_url = card.get_layout_url()
    artwork_url = card.get_artwork_url()

    # Creating and returning a Card object with the generated values
    return Card.Card(title, subtitle, text, value, attack_value, range_value, defense_value, speed_value, layout_url, artwork_url)

  
if __name__ == "__main__":
    main()
