import json

def card_to_dict(card):
    return {
        "card_id": card.get_card_id(),
        "title": card.get_title(),
        "subtitle": card.get_subtitle(),
        "text": card.get_text(),
        "value": card.get_value(),
        "attack_value": card.get_attack_value(),
        "range_value": card.get_range_value(),
        "defense_value": card.get_defense_value(),
        "speed_value": card.get_speed_value(),
        "layout_url": card.get_layout_url(),
        "artwork_url": card.get_artwork_url()
    }

def export_cards_to_json(path, card_list):
    # Convert the list of Card objects into a list of dictionaries
    card_dicts = [card_to_dict(card) for card in card_list]

    # Export the list of dictionaries to a JSON file
    with open(path, 'w') as json_file:
        json.dump(card_dicts, json_file, indent=4)
