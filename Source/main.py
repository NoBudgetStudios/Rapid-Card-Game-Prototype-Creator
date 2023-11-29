import Card
import DbManager
import JsonManager
import TextManager
import CardDesigner
import PrintDesigner
import random
import string

def main():

    cards_file_url = '.\\..\\data\\cards.txt'

    card_list_in = TextManager.read_cards(cards_file_url)
    # Create the cards table if it doesn't exist
    DbManager.create_db_if_not_exists()
    read_cards = True
    card_list = []
    if read_cards:
        for i in range(len(card_list_in)):
            new_card = generate_random_card(card_list_in[i], random_title = True, random_subtitle = True, random_stats = True)
            card_list.append(new_card)
            DbManager.insert_card(new_card)

            CardDesigner.design_card(new_card)
    else:
        for i in range(int(input('Card Number: '))):
            new_card = generate_random_card(random_title = True, random_subtitle = True, random_stats = True)
            card_list.append(new_card)
            DbManager.insert_card(new_card)

            CardDesigner.design_card(new_card)
        
    JsonManager.export_cards_to_json(card_list)

    if(input("Make it printable? ") == 'y'):
        PrintDesigner.DesignPrint()

def generate_random_title(syllable_count=2):
    syllables = [
        'dra', 'gon', 'pho', 'enix', 'cen', 'tau', 'rus', 'grif', 'fin', 'dor',
        'man', 'tic', 'cor', 'ger', 'gar', 'ath', 'eas', 'tor', 'loth', 'en', 'nix',
        'zel', 'dus', 'mi', 'tyr', 'ga', 'mag', 'ra', 'len', 'thor', 'ian', 'sil',
        'mon', 'cer', 'tar', 'ix', 'vor', 'vol', 'gol', 'tar', 'kron', 'gorn', 'nath'
    ]
    
    title = ''.join(random.choices(syllables, k=syllable_count)).capitalize()
    return title

def generate_random_subtitle():
    subtitles = [
        'Treants', 'Werewolves', 'Arachnids', 'Warturtles', 'Gorliths', 'Reptions',
        'Lacerons', 'Tentacloids', 'Zephyrions', 'Aetherwings', 'Dragons', 'Lionids',
        'Chiropts', 'Chlamyphs', 'Selachs'
    ]
    
    subtitle = ''.join(random.choices(subtitles)).capitalize()
    return subtitle

def generate_random_card(card = None, random_title = False, random_subtitle = False, random_stats = False):
    # Generating random values for attributes
    if not random_title or card == None:
        title = generate_random_title(syllable_count=random.randint(2, 3))
    else:
        title = card.get_title()
        
    if random_subtitle or card == None:
        subtitle = generate_random_subtitle()
    else:
        subtitle = card.get_subtitle()

    subtitle = ''

    if card == None:    
        text = ''
    else:
        text = card.get_text()
        
    if random_stats or card == None:
        attack_value = random.randint(1, 6)
        range_value = random.randint(1, 6)
        defense_value = random.randint(1, 6)
        speed_value = random.randint(1, 6)
        value = round((attack_value + range_value + defense_value + speed_value) / 4)
    else:
        attack_value = -1
        range_value = -1
        defense_value = -1
        speed_value = -1
        value = -1

    if card == None:
        layout_url = ''
        artwork_url = ''
    else:
        layout_url = card.get_layout_url()
        artwork_url = card.get_artwork_url()

    # Creating and returning a Card object with the generated values
    return Card.Card(title, subtitle, text, value, attack_value, range_value, defense_value, speed_value, layout_url, artwork_url)

  
if __name__ == "__main__":
    main()
