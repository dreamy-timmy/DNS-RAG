import json

def append_to_json(file_path, data):
    # Читаем существующий JSON файл, если он существует
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Загружаем текущие данные в Python-структуру
            existing_data = json.load(file)
    except FileNotFoundError:
        # Если файл не существует, создаем пустой список
        existing_data = []

    # Дописываем новые данные в существующую структуру
    existing_data.append(data)

    # Сохраняем обновленные данные обратно в JSON файл
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)