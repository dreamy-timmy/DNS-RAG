import os
import json

def merge_json_files(input_dir, output_file):
    """
    Объединяет все JSON файлы из указанной директории в один большой JSON файл.

    :param input_dir: Директория с JSON файлами для объединения.
    :param output_file: Имя выходного JSON файла.
    """
    merged_data = []  # Список для хранения объединенных данных

    # Перебираем все файлы в директории
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):  # Фильтруем только JSON файлы
            file_path = os.path.join(input_dir, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    # Добавляем содержимое файла в общий список
                    if isinstance(data, list):  # Если файл содержит список
                        merged_data.extend(data)
                    else:  # Если файл содержит словарь
                        merged_data.append(data)
            except Exception as e:
                print(f"Ошибка при обработке файла {filename}: {e}")

    # Сохраняем объединенные данные в выходной файл
    try:
        with open(output_file, 'w', encoding='utf-8') as output:
            json.dump(merged_data, output, ensure_ascii=False, indent=4)
        print(f"Данные успешно сохранены в {output_file}")
    except Exception as e:
        print(f"Ошибка при сохранении в файл {output_file}: {e}")


input_directory = "parser/laptop_specifications"  # Директория с JSON файлами
output_json = "parser/merged_data.json"  # Имя выходного файла

merge_json_files(input_directory, output_json)
