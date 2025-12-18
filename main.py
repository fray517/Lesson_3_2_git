"""Модуль для работы с температурными преобразованиями."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Преобразует температуру из градусов Цельсия в градусы Фаренгейта.

    Формула: F = C * 9/5 + 32

    Args:
        celsius: Температура в градусах Цельсия.

    Returns:
        Температура в градусах Фаренгейта.
    """
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    # Пример использования
    temp_c = 25.0
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f'{temp_c}°C = {temp_f}°F')

