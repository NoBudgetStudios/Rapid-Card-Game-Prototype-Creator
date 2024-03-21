import sqlite3

def create_db_if_not_exists(path):
    # Connect to SQLite database (creates if not exists)
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    # Create a table for cards if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            card_id INTEGER PRIMARY KEY,
            card_type TEXT,
            title TEXT,
            subtitle TEXT,
            main_text TEXT,
            big_center_text TEXT,
            small_center_text TEXT,
            corner_text TEXT,
            value INTEGER,
            attack_value INTEGER,
            range_value TEXT,
            defense_value INTEGER,
            speed_value INTEGER,
            layout_url TEXT,
            artwork_url TEXT
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

def insert_card(path, card):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO cards (card_type, title, subtitle, main_text, big_center_text, small_center_text, corner_text, value, attack_value, range_value, defense_value, speed_value, layout_url, artwork_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (card.get_card_type(), card.get_title(), card.get_subtitle(), card.get_main_text(), card.get_big_center_text(), card.get_small_center_text(), card.get_corner_text(), card.get_value(), card.get_attack_value(), card.get_range_value(), card.get_defense_value(), card.get_speed_value(), card.get_layout_url(), card.get_artwork_url()))

    conn.commit()
    conn.close()

def get_card_by_id(path, card_id):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM cards WHERE card_id = ?
    ''', (card_id,))

    card_data = cursor.fetchone()
    conn.close()

    if card_data:
        # Create a Card object using retrieved data
        return Card(*card_data)
    return None

def update_card(path, card):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE cards SET card_type=?, title=?, subtitle=?, main_text=?, big_center_text=?, small_center_text=?, corner_text=?, value=?, attack_value=?, range_value=?, defense_value=?, speed_value=?, layout_url=?, artwork_url=?
        WHERE card_id=?
    ''', (card.get_card_type(), card.get_title(), card.get_subtitle(), card.get_main_text(), card.get_big_center_text(), card.get_small_center_text(), card.get_corner_text(), card.get_value(), card.get_attack_value(), card.get_range_value(), card.get_defense_value(), card.get_speed_value(), card.get_layout_url(), card.get_artwork_url(), card.get_card_id()))

    conn.commit()
    conn.close()

def delete_card(path, card_id):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM cards WHERE card_id=?
    ''', (card_id,))

    conn.commit()
    conn.close()
