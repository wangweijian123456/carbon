import json
import time

# 读取配置文件
def load_config():
    with open('config.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# 生成提示信息
def generate_prompt(items, header):
    item_tips = [f"{i}) {item['name']}" for i, item in enumerate(items)]
    return f"------ {header} -------\n" + "\n".join(item_tips)

# 获取用户输入的编号
def get_item_by_index(items, item_type):
    while True:
        index_txt = input(f'请输入需要消耗的{item_type}编号(或直接回车完成): ')
        if not index_txt:
            return None  # 用户按回车，完成输入
        if index_txt.isnumeric():
            index = int(index_txt)
            if 0 <= index < len(items):
                return items[index]  # 返回选中的项目
            else:
                print(f'没有找到对应的{item_type}，请重新输入')
        else:
            print('输入错误，请输入数字编号')
        time.sleep(1)

# 获取用户输入的消耗量
def get_item_quantity(item):
    while True:
        name, unit = item['name'], item['unit']
        num_txt = input(f'请输入{name}的消耗量({unit}): ')
        try:
            num = float(num_txt)
            if num > 0:
                return num  # 返回有效的消耗量
            else:
                print('消耗量必须大于0，请重新输入')
        except ValueError:
            print('输入的不是有效的数字，请重新输入')
        time.sleep(1)

# 获取所有用户输入的消耗数据
def get_user_input(items, item_type):
    necessities = []
    while True:
        item = get_item_by_index(items, item_type)
        if item is None:
            break  # 用户完成输入
        num = get_item_quantity(item)
        necessities.append(dict(name=item['name'], size=item['size'], unit=item['unit'], num=num))
    return necessities

# 计算碳排放结果
def calculate(necessities):
    results = []
    result_tips = ['计算结果:']
    for item in necessities:
        item_result = item['num'] * item['size']
        results.append(item_result)
        result_tips.append(f"{item['name']}：{item['num']} {item['unit']} × {item['size']} kg CO₂e/{item['unit']} = {item_result} kg CO₂e")
    total_emissions = sum(results)
    result_tips.append(f'总碳排放量：{" + ".join(str(r) for r in results)} = {total_emissions} kg CO₂e')
    return "\n".join(result_tips), total_emissions

def main():
    config = load_config()

    # 提示能源和材料的输入
    energy_prompt = generate_prompt(config['energy'], '能源')
    materials_prompt = generate_prompt(config['materials'], '材料')

    print(energy_prompt)
    energy_necessities = get_user_input(config['energy'], '能源')

    print(materials_prompt)
    material_necessities = get_user_input(config['materials'], '材料')

    # 合并能源和材料
    all_necessities = energy_necessities + material_necessities

    # 计算碳排放
    if all_necessities:
        result, total_emissions = calculate(all_necessities)
        print(result)
    else:
        print('没有输入任何能源或材料。')

if __name__ == '__main__':
    main()
