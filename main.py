from datetime import date


# Данные одного обращения
client_name = "Иванов Иван Изачик"
device_type = "Ноутбук"
problem_description = "Не включается"
master_name = "Славик"
is_master_available = True
request_date = date(2026, 9, 15)


def get_request_status(is_master_available: bool) -> str:
    """Вернуть текстовый статус регистрации обращения."""
    if is_master_available:
        return "Обращение зарегистрировано, мастер доступен"
    return "Обращение принято в очередь, мастер занят"


print(f"Клиент: {client_name}")
print(f"Устройство: {device_type}")
print(f"Проблема: {problem_description}")
print(f"Мастер: {master_name}")
print(f"Дата обращения: {request_date}")
print(get_request_status(is_master_available))