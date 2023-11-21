import sqlite3

def create_db_if_not_exists():
    # Connect to SQLite database (creates if not exists)
    conn = sqlite3.connect('cards.db')
    cursor = conn.cursor()

    # Create a table for cards if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            card_id INTEGER PRIMARY KEY,
            title TEXT,
            subtitle TEXT,
            text TEXT,
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

def insert_card(card):
    conn = sqlite3.connect('cards.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO cards (title, subtitle, text, value, attack_value, range_value, defense_value, speed_value, layout_url, artwork_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (card.get_title(), card.get_subtitle(), card.get_text(), card.get_value(), card.get_attack_value(), card.get_range_value(), card.get_defense_value(), card.get_speed_value(), card.get_layout_url(), card.get_artwork_url()))

    conn.commit()
    conn.close()

def get_card_by_id(card_id):
    conn = sqlite3.connect('cards.db')
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

def update_card(card):
    conn = sqlite3.connect('cards.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE cards SET title=?, subtitle=?, text=?, value=?, attack_value=?, range_value=?, defense_value=?, speed_value=?, layout_url=?, artwork_url=?
        WHERE card_id=?
    ''', (card.get_title(), card.get_subtitle(), card.get_text(), card.get_value(), card.get_attack_value(), card.get_range_value(), card.get_defense_value(), card.get_speed_value(), card.get_layout_url(), card.get_artwork_url(), card.get_card_id()))

    conn.commit()
    conn.close()

def delete_card(card_id):
    conn = sqlite3.connect('cards.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM cards WHERE card_id=?
    ''', (card_id,))

    conn.commit()
    conn.close()
