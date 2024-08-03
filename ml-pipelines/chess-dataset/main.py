import os
from PIL import Image

from utils import *

# Config
ASSETS_FOLDER = 'assets'
OUTPUT_FOLDER = 'output'
OUTPUT_SIZE = 32

# Check for existence of output folder
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Navigate through folders in assets
for idx, piece_folder in enumerate(os.listdir(ASSETS_FOLDER), 1):
    print(idx, "/", len(os.listdir(ASSETS_FOLDER)))
    piece_path = os.path.join(ASSETS_FOLDER, piece_folder)

    # Checking for a folder
    if os.path.isdir(piece_path):
        # Loop through all files in a folder
        for board_file in os.listdir(piece_path):
            board_path = os.path.join(piece_path, board_file)
            board_name = board_file.split('.')[0]

            # Checking for PNG file
            if os.path.isfile(board_path) and board_file.endswith('.png'):
                with Image.open(board_path) as im:
                    width, height = im.size
                    cell_width = width // 8
                    cell_height = height // 8

                    # Extracting cells
                    for row in range(7):
                        for col in range(4):
                            left = col * cell_width
                            upper = row * cell_height
                            right = (col + 1) * cell_width
                            lower = (row + 1) * cell_height

                            cell = im.crop((left, upper, right, lower))

                            resized_cell = resize_image_to_resolution(cell, OUTPUT_SIZE, OUTPUT_SIZE)

                            effects = {
                                "original": resized_cell,
                            }

                            piece_type = get_piece_type_from_row(row)
                            piece_color = get_piece_color_from_col(col)
                            cell_color = get_cell_color_from_coordinates(col, row)

                            for effect_name, effect_img in effects.items():
                                cell_filename = f"{piece_folder}_{board_name}_{piece_type}_{piece_color}_{cell_color}_noFlip.png"
                                cell_path = os.path.join(OUTPUT_FOLDER, cell_filename)

                                flipped_img = effect_img.transpose(Image.FLIP_TOP_BOTTOM)
                                flipped_filename = f"{piece_folder}_{board_name}_{piece_type}_{piece_color}_{cell_color}_flip.png"
                                flipped_path = os.path.join(OUTPUT_FOLDER, flipped_filename)

                                # Save the cells
                                effect_img.save(cell_path)
                                flipped_img.save(flipped_path)




print("All cells have been extracted and saved.")
