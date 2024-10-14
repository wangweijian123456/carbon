import json
import os

# 配置文件路径
CONFIG_FILE = 'config.json'

# 加载配置文件
def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"配置文件 {CONFIG_FILE} 不存在，请检查路径。")
        return None
    
    with open(CONFIG_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

# 保存配置文件
def save_config(config):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=4, ensure_ascii=False)
    print(f"配置已成功保存到 {CONFIG_FILE}")

# 显示当前配置
def display_config(config):
    print("\n当前配置：")
    print("------能源-------")
    for i, energy in enumerate(config['energy']):
        print(f"{i}) {energy['name']} - {energy['size']} kg CO₂e/{energy['unit']}")
    
    print("------材料-------")
    for i, material in enumerate(config['materials']):
        print(f"{i}) {material['name']} - {material['size']} kg CO₂e/{material['unit']}")

# 修改配置项
def modify_config_item(config, item_type, index):
    if item_type == 'energy':
        items = config['energy']
    else:
        items = config['materials']
    
    if index >= len(items):
        print(f"无效的索引：{index}")
        return

    item = items[index]
    print(f"\n正在修改 {item_type}：{item['name']}")
    new_name = input(f"请输入新的名称（当前：{item['name']}，留空则不修改）：")
    new_size = input(f"请输入新的碳排放系数（kg CO₂e/{item['unit']}），当前：{item['size']}：")
    new_unit = input(f"请输入新的单位（当前：{item['unit']}，留空则不修改）：")
    
    if new_name:
        item['name'] = new_name
    if new_size:
        try:
            item['size'] = float(new_size)
        except ValueError:
            print("输入的碳排放系数无效，将保持原值。")
    if new_unit:
        item['unit'] = new_unit

    print(f"\n已更新 {item_type}：{item}")

# 修改配置主逻辑
def modify_config():
    config = load_config()
    if config is None:
        return
    
    display_config(config)
    
    while True:
        print("\n选择需要修改的类型：")
        print("1) 修改能源")
        print("2) 修改材料")
        print("3) 保存并退出")
        print("4) 退出不保存")
        
        choice = input("请输入选择：")
        
        if choice == '1':
            index = input("请输入要修改的能源编号：")
            if index.isdigit():
                modify_config_item(config, 'energy', int(index))
            else:
                print("输入无效，请输入有效的编号。")
        
        elif choice == '2':
            index = input("请输入要修改的材料编号：")
            if index.isdigit():
                modify_config_item(config, 'materials', int(index))
            else:
                print("输入无效，请输入有效的编号。")
        
        elif choice == '3':
            save_config(config)
            break
        
        elif choice == '4':
            print("已取消修改。")
            break
        
        else:
            print("无效的选项，请重新选择。")

if __name__ == '__main__':
    modify_config()
