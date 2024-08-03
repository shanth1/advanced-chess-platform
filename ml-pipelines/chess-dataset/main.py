import os
from PIL import Image

# Устанавливаем пути
ASSETS_FOLDER = 'assets'
OUTPUT_FOLDER = 'output'
OUTPUT_SIZE = 32

# Based on fen in readme
def get_piece_type_from_row(index):
	return ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn', 'empty'][index]

# Based on fen in readme
def get_piece_color_from_col(index):
	return 'white' if index >= 2 else 'black'

# Based on fen in readme
def get_cell_color_from_coordinates(col, row):
	return 'bgWhite' if (col + row) % 2 == 0 else 'bgBlack'

def resize_image_to_max_resolution(image, max_width, max_height):
    # Получаем текущие размеры изображения
    width, height = image.size

    # Если изображение уже меньше или равно допустимому размеру, ничего не делаем
    if width <= max_width and height <= max_height:
        return image

    # Расчитываем соотношение масштабирования для ширины и высоты
    width_ratio = max_width / width
    height_ratio = max_height / height

    # Используем минимальное соотношение, чтобы не выйти за пределы максимальных размеров
    new_size_ratio = min(width_ratio, height_ratio)

    # Рассчитываем новые размеры
    new_width = int(width * new_size_ratio)
    new_height = int(height * new_size_ratio)

    # Изменяем размер изображения
    return image.resize((new_width, new_height), Image.ADAPTIVE)



# Убедимся, что выходная папка существует
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Проходим по всем папкам в assets
for idx, piece_folder in enumerate(os.listdir(ASSETS_FOLDER), 1):
    print(idx, "/", len(os.listdir(ASSETS_FOLDER)))
    piece_path = os.path.join(ASSETS_FOLDER, piece_folder)

    # Проверяем, что это папка
    if os.path.isdir(piece_path):
        # Проходим по всем файлам в папке
        for board_file in os.listdir(piece_path):
            board_path = os.path.join(piece_path, board_file)
            board_name = board_file.split('.')[0]

            # Проверяем, что это файл PNG
            if os.path.isfile(board_path) and board_file.endswith('.png'):
                with Image.open(board_path) as im:
                    width, height = im.size
                    cell_width = width // 8
                    cell_height = height // 8

                    # Извлекаем клетки
                    for row in range(7):
                        for col in range(4):
                            left = col * cell_width
                            upper = row * cell_height
                            right = (col + 1) * cell_width
                            lower = (row + 1) * cell_height

                            cell = im.crop((left, upper, right, lower))

                            piece_type = get_piece_type_from_row(row)
                            piece_color = get_piece_color_from_col(col)
                            cell_color = get_cell_color_from_coordinates(col, row)

                            # Имя файла для клетки
                            cell_filename = f"{piece_folder}_{board_name}_{piece_type}_{piece_color}_{cell_color}.png"

                            cell_path = os.path.join(OUTPUT_FOLDER, cell_filename)

                            resized_cell = resize_image_to_max_resolution(cell, OUTPUT_SIZE, OUTPUT_SIZE)

                            # Сохраняем клетку
                            resized_cell.save(cell_path)

print("All cells have been extracted and saved.")
