import json
import sys

def load_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: Файл {file_path} содержит некорректный JSON")
        sys.exit(1)

def create_values_dict(values_data):
    values_dict = {}
    for item in values_data.get('values', []):
        values_dict[item['id']] = item['value']
    return values_dict

def fill_values(tests_structure, values_dict):
    if isinstance(tests_structure, dict):
        if 'id' in tests_structure and tests_structure['id'] in values_dict:
            tests_structure['value'] = values_dict[tests_structure['id']]

        for key, value in tests_structure.items():
            if isinstance(value, (dict, list)):
                fill_values(value, values_dict)
    
    elif isinstance(tests_structure, list):
        for item in tests_structure:
            fill_values(item, values_dict)
    
    return tests_structure

def main():
    if len(sys.argv) != 4:
        print("Использование: python script.py <tests.json> <values.json> <report.json>")
        sys.exit(1)

    tests_path = sys.argv[1]
    values_path = sys.argv[2]
    report_path = sys.argv[3]

    tests_data = load_json_file(tests_path)
    values_data = load_json_file(values_path)

    values_dict = create_values_dict(values_data)

    report_data = fill_values(tests_data, values_dict)

    try:
        with open(report_path, 'w', encoding='utf-8') as file:
            json.dump(report_data, file, indent=2, ensure_ascii=False)
        print(f"Отчет успешно сохранен в {report_path}")
    except IOError as e:
        print(f"Ошибка при записи в файл {report_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
