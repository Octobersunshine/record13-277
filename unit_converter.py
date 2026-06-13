from typing import Dict, List, Tuple


LENGTH_UNITS = {
    'm': {'name': '米', 'to_base': 1.0},
    'km': {'name': '公里', 'to_base': 1000.0},
    'mile': {'name': '英里', 'to_base': 1609.344},
}

WEIGHT_UNITS = {
    'kg': {'name': '千克', 'to_base': 1.0},
    'lb': {'name': '磅', 'to_base': 0.45359237},
}

CATEGORY_NAMES = {
    'length': '长度',
    'weight': '重量',
    'temperature': '温度',
}


def celsius_to_fahrenheit(c: float) -> float:
    return round(c * 9 / 5 + 32, 2)


def fahrenheit_to_celsius(f: float) -> float:
    return round((f - 32) * 5 / 9, 2)


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in LENGTH_UNITS or to_unit not in LENGTH_UNITS:
        raise ValueError(f"不支持的长度单位: {from_unit} -> {to_unit}")
    base_value = value * LENGTH_UNITS[from_unit]['to_base']
    return round(base_value / LENGTH_UNITS[to_unit]['to_base'], 2)


def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in WEIGHT_UNITS or to_unit not in WEIGHT_UNITS:
        raise ValueError(f"不支持的重量单位: {from_unit} -> {to_unit}")
    base_value = value * WEIGHT_UNITS[from_unit]['to_base']
    return round(base_value / WEIGHT_UNITS[to_unit]['to_base'], 2)


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    from_u = from_unit.lower()
    to_u = to_unit.lower()
    valid = {'c', 'f'}
    if from_u not in valid or to_u not in valid:
        raise ValueError(f"不支持的温度单位: {from_unit} -> {to_unit}")
    if from_u == to_u:
        return value
    if from_u == 'c':
        return celsius_to_fahrenheit(value)
    return fahrenheit_to_celsius(value)


def convert(value: float, category: str, from_unit: str, to_unit: str) -> float:
    cat = category.lower()
    if cat == 'length':
        return convert_length(value, from_unit, to_unit)
    if cat == 'weight':
        return convert_weight(value, from_unit, to_unit)
    if cat == 'temperature':
        return convert_temperature(value, from_unit, to_unit)
    raise ValueError(f"不支持的类别: {category}")


def get_supported_units() -> Dict[str, List[Tuple[str, str]]]:
    return {
        'length': [(k, v['name']) for k, v in LENGTH_UNITS.items()],
        'weight': [(k, v['name']) for k, v in WEIGHT_UNITS.items()],
        'temperature': [('c', '摄氏'), ('f', '华氏')],
    }


def print_menu():
    print("\n===== 单位换算服务 =====")
    print("1. 长度换算 (米/公里/英里)")
    print("2. 重量换算 (千克/磅)")
    print("3. 温度换算 (摄氏/华氏)")
    print("4. 查看支持的单位")
    print("0. 退出")
    print("========================")


def handle_length():
    units = get_supported_units()['length']
    print(f"\n支持的长度单位: {', '.join(f'{k}({v})' for k, v in units)}")
    try:
        value = float(input("请输入数值: "))
        from_unit = input("源单位 (m/km/mile): ").strip().lower()
        to_unit = input("目标单位 (m/km/mile): ").strip().lower()
        result = convert_length(value, from_unit, to_unit)
        print(f"结果: {value} {LENGTH_UNITS[from_unit]['name']} = {result:.2f} {LENGTH_UNITS[to_unit]['name']}")
    except ValueError as e:
        print(f"错误: {e}")


def handle_weight():
    units = get_supported_units()['weight']
    print(f"\n支持的重量单位: {', '.join(f'{k}({v})' for k, v in units)}")
    try:
        value = float(input("请输入数值: "))
        from_unit = input("源单位 (kg/lb): ").strip().lower()
        to_unit = input("目标单位 (kg/lb): ").strip().lower()
        result = convert_weight(value, from_unit, to_unit)
        print(f"结果: {value} {WEIGHT_UNITS[from_unit]['name']} = {result:.2f} {WEIGHT_UNITS[to_unit]['name']}")
    except ValueError as e:
        print(f"错误: {e}")


def handle_temperature():
    print("\n支持的温度单位: c(摄氏), f(华氏)")
    try:
        value = float(input("请输入数值: "))
        from_unit = input("源单位 (c/f): ").strip().lower()
        to_unit = input("目标单位 (c/f): ").strip().lower()
        result = convert_temperature(value, from_unit, to_unit)
        from_name = '摄氏' if from_unit == 'c' else '华氏'
        to_name = '摄氏' if to_unit == 'c' else '华氏'
        print(f"结果: {value} {from_name} = {result:.2f} {to_name}")
    except ValueError as e:
        print(f"错误: {e}")


def handle_list_units():
    info = get_supported_units()
    print("\n支持的单位列表:")
    for cat, units in info.items():
        print(f"  [{CATEGORY_NAMES[cat]}]: {', '.join(f'{k}({v})' for k, v in units)}")


def main():
    while True:
        print_menu()
        choice = input("请选择操作 (0-4): ").strip()
        if choice == '0':
            print("再见！")
            break
        elif choice == '1':
            handle_length()
        elif choice == '2':
            handle_weight()
        elif choice == '3':
            handle_temperature()
        elif choice == '4':
            handle_list_units()
        else:
            print("无效选择，请重试。")


if __name__ == '__main__':
    main()
