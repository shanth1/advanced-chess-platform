from PIL import Image

# Based on fen in readme
def get_piece_type_from_row(index):
	return ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn', 'empty'][index]

# Based on fen in readme
def get_piece_color_from_col(index):
	return 'white' if index >= 2 else 'black'

# Based on fen in readme
def get_cell_color_from_coordinates(col, row):
	return 'bgWhite' if (col + row) % 2 == 0 else 'bgBlack'

def resize_image_to_resolution(image, target_width, target_height):
    width, height = image.size

    # Calculate scaling ratios for width and height
    width_ratio = target_width / width
    height_ratio = target_height / height

    # Use the minimum ratio to ensure the image fits within the given target resolution
    new_size_ratio = min(width_ratio, height_ratio)

    # Calculate new dimensions
    new_width = int(width * new_size_ratio)
    new_height = int(height * new_size_ratio)

    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    # Create a new image with the desired target resolution (optional, but keeps the image centered)
    new_image = Image.new('RGB', (target_width, target_height))
    new_image.paste(resized_image, ((target_width - new_width) // 2, (target_height - new_height) // 2))

    return new_image
