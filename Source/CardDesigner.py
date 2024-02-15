from PIL import Image, ImageDraw, ImageFont
import os
import random
import datetime

layout_url = '.\\..\\Images\\Layout\\'
artwork_url = '.\\..\\Images\\Artwork\\'
font_url = '.\\..\\Fonts\\Manrope.ttf'
output_url = '.\\..\\Images\\Output\\'

random_images = False

def create_bg():
    # Dimensions in inches and DPI
    width_inches = 2.5
    height_inches = 3.5
    dpi = 300

    # Convert inches to pixels based on DPI
    width_pixels = int(width_inches * dpi)
    height_pixels = int(height_inches * dpi)

    # Create a black image
    bg_image = Image.new("RGB", (width_pixels, height_pixels), color="white")

    return bg_image

def show_image(image):
    image.show()

def overlay_images(back_image, front_image):
    back_image.paste(front_image, (0, 0), front_image)
    return back_image

def resize_image(image, new_width, new_height):
    # Resize the image
    resized_image = image.resize((new_width, new_height))

    return resized_image

def import_image(image_path):
    try:
        img = Image.open(image_path)
        return img
    except FileNotFoundError:
        print("Image file not found: " + image_path)
        return None

def export_image(image_name, image):
    export_path = image_name

    image.save(export_path, "PNG")
    return export_path

def LoadFont(fontUrl, size):
    return ImageFont.truetype(fontUrl, size)

def SetText( image, xy, text, text_fill=None, text_font=None, text_anchor=None, text_spacing=0, text_align='left'):#img, position, text, font_url, font_size, font_color):
    draw = ImageDraw.Draw(image)
    draw.multiline_text(xy, text, fill=text_fill, font=text_font, anchor=text_anchor, spacing=text_spacing, align=text_align)
    return image

def MakeCardTextPrintFriendly(string, max_characters_per_line):
    words = string.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line + word) + 1 <= max_characters_per_line:
            current_line += " " + word
        else:
            lines.append(current_line.strip())
            current_line = word

    if current_line:
        lines.append(current_line.strip())

    printFriendlyText = "\n".join(lines)
    return printFriendlyText.replace('CHLN','\n\n')

def get_random_file(path):
    if not os.path.isdir(path):
        return "Invalid path or path doesn't exist"

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if not files:
        return "No files found in the directory"

    random_file = random.choice(files)
    return random_file

def design_card(card):
    global layout_url
    
    bg_image = create_bg()
    
    #artwork_image = import_image( '.\\..\\Images\\Artwork\\t.png' )
    print("Image Exported: " + card.get_title())
    #artwork_image = artwork_url + import_image(get_random_file(artwork_url))
    if random_images == True and len(card.get_artwork_url()) > 0:
        artwork_image = import_image( artwork_url + get_random_file(artwork_url) )
    else:
        #print(card.get_artwork_url())
        artwork_image = import_image( card.get_artwork_url() )
        
    artwork_image = resize_image(artwork_image, bg_image.size[0], bg_image.size[1])
    artwork_ready_image = overlay_images(bg_image, artwork_image)

    if len(card.get_layout_url()) > 0:
        layout_image = import_image(card.get_layout_url())
    else:
        layout_image = import_image( layout_url + 'default_layout.png' )
        
    layout_image = resize_image(layout_image, artwork_ready_image.size[0], artwork_ready_image.size[1])
    layout_ready_image = overlay_images(artwork_ready_image, layout_image)
    #show_image(layout_ready_image)

    size = layout_ready_image.size
    #xy, text, fill=None, font=None, anchor=None, spacing=0, align=”left”)
    
    #text
    texted_img = SetText( layout_ready_image, (size[0]/25, size[1]/1.35), MakeCardTextPrintFriendly(card.get_text(), 50), text_fill='white', text_font=LoadFont(font_url, 30))
    #title
    if len(card.get_title()) > 0:
        texted_img = SetText( texted_img, (size[0]/25, size[1]/75), card.get_title(), text_fill='white', text_font=LoadFont(font_url, 50))
    #subtitle
    if len(card.get_subtitle()) > 0:
        texted_img = SetText( texted_img, (size[0]/25, size[1]/13), card.get_subtitle(), text_fill='white', text_font=LoadFont(font_url, 30))
    #value
    if card.get_value() >= 0:
        texted_img = SetText( texted_img, (size[0]/1.25, 0), card.get_value(), text_fill='white', text_font=LoadFont(font_url, 100))
    #stats
    if card.get_attack_value() >= 0:
        texted_img = SetText( texted_img, (size[0]/2 - 300, size[1]/1.15), 'Atk: ' + str(card.get_attack_value()), text_fill='white', text_font=LoadFont(font_url, 35))
    if card.get_range_value() >= 0:
        texted_img = SetText( texted_img, (size[0]/2 - 150, size[1]/1.15), 'Rng: ' + str(card.get_range_value()), text_fill='white', text_font=LoadFont(font_url, 35))
    if card.get_defense_value() >= 0:
        texted_img = SetText( texted_img, (size[0]/2 + 50, size[1]/1.15), 'Def: ' + str(card.get_defense_value()), text_fill='white', text_font=LoadFont(font_url, 35))
    if card.get_speed_value() >= 0:
        texted_img = SetText( texted_img, (size[0]/2 + 200, size[1]/1.15), 'Spe: ' + str(card.get_speed_value()), text_fill='white', text_font=LoadFont(font_url, 35))
    
    #old
    '''
    #stats
    statsText = 'Atk: {0}\nRng: {0}\nDfs: {1}\nSpd: {2}'.format(
        card.get_attack_value(),
        card.get_range_value(),
        card.get_defense_value(),
        card.get_speed_value())
    statsText = 'Atk: {0}        Rng: {0}        Dfs: {1}        Spd: {2}'.format(
        card.get_attack_value(),
        card.get_range_value(),
        card.get_defense_value(),
        card.get_speed_value())
    #texted_img = SetText( texted_img, (size[0]/1.25, size[1]/1.35), statsText, font_url, 40, (255, 255, 255))
    texted_img = SetText( texted_img, (size[0]/8, size[1]/1.15), statsText, font_url, 35, (255, 255, 255))

    '''
    #cardId
    #texted_img = SetText( texted_img, (size[0]/25, size[1]/1.075), '\nID: ' + str(card.get_card_id()), font_url, 20, (255, 255, 255))
    texted_img = SetText( texted_img, (size[0]/25, size[1]/1.075), '\nID: ' + str(card.get_card_id()), text_fill='white', text_font=LoadFont(font_url, 20))
    final_image = texted_img
    #print(str(card.get_card_id()))
    if len(card.get_subtitle()) > 0:
        export_url = output_url + str(card.get_card_id()) + '_' + card.get_subtitle() + '-' + card.get_title() + '.png'
    else:
        export_url = output_url + str(card.get_card_id()) + '_' + card.get_title()+ '.png'
    export_image(export_url, final_image)

    #show_image(texted_img)
