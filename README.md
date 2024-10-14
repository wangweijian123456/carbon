# 碳足迹计算工具

## 项目简介

该工具用于计算公司在生产过程中消耗的能源和原材料的碳足迹。用户可以通过输入消耗的能源和原材料的类型及数量，工具会根据配置文件中提供的碳排放系数，计算并输出每种能源和材料的碳排放量以及总碳排放量。

## 功能

- 支持输入多种能源类型及其消耗量（如电力、天然气等）。
- 支持输入多种原材料及其消耗量（如铝、钢、塑料等）。
- 根据输入的数据，计算各个能源和原材料的碳排放量。
- 累加所有能源和原材料的碳排放量，计算总碳排放量。
- 提供简单的命令行界面，方便用户操作。

## 安装与运行

### 环境要求

- Python 3.12 或更高版本

### 安装步骤

1. 克隆本项目到本地：

```bash
git clone https://github.com/wangweijian123456/carbon.git
cd carbon
```

2. 准备配置文件 config.json，确保文件包含能源和原材料的碳排放系数，例如：
```json
{
  "energy": [
    {"name": "电力", "size": 0.5, "unit": "kWh"},
    {"name": "天然气", "size": 2.75, "unit": "m³"}
  ],
  "materials": [
    {"name": "铝", "size": 8.0, "unit": "kg"},
    {"name": "钢", "size": 1.9, "unit": "kg"},
    {"name": "塑料", "size": 2.5, "unit": "kg"}
  ]
}
```

3. 运行程序:
```bash
python carbon.py
```
4. 运行示例:
```plaintext
------ 能源 -------
0) 电力
1) 天然气
2) 煤碳
请输入需要消耗的能源编号(或直接回车完成): 0
请输入电力的消耗量(kwh): 100
请输入需要消耗的能源编号(或直接回车完成): 2
请输入煤碳的消耗量(kg): 100
请输入需要消耗的能源编号(或直接回车完成): 
------ 材料 -------
1) 钢
2) 塑料
请输入需要消耗的材料编号(或直接回车完成): 0
请输入铝的消耗量(kg): 100
请输入需要消耗的材料编号(或直接回车完成): 2
请输入塑料的消耗量(kg): 50
请输入需要消耗的材料编号(或直接回车完成): 1
请输入钢的消耗量(kg): 100
请输入需要消耗的材料编号(或直接回车完成):
计算结果:
电力：100.0 kwh × 0.5 kg CO₂e/kwh = 50.0 kg CO₂e
铝：100.0 kg × 8.0 kg CO₂e/kg = 800.0 kg CO₂e
塑料：50.0 kg × 2.5 kg CO₂e/kg = 125.0 kg CO₂e
钢：100.0 kg × 1.9 kg CO₂e/kg = 190.0 kg CO₂e
总碳排放量：50.0 + 242.0 + 800.0 + 125.0 + 190.0 = 1407.0 kg CO₂e
```
### 修改配置
1. 运行程序:
```bash
python modify_config.py
```
2. 运行示例：
```plaintext
当前配置：
------能源-------
0) 电力 - 0.5 kg CO₂e/kwh
1) 天然气 - 2.75 kg CO₂e/m³
2) 煤碳 - 2.42 kg CO₂e/kg
------材料-------
0) 铝 - 8.0 kg CO₂e/kg
1) 钢 - 1.9 kg CO₂e/kg
2) 塑料 - 2.5 kg CO₂e/kg

选择需要修改的类型：
1) 修改能源
2) 修改材料
3) 保存并退出
4) 退出不保存
请输入选择：1
请输入要修改的能源编号：1

正在修改 energy：天然气
请输入新的名称（当前：天然气，留空则不修改）：
请输入新的碳排放系数（kg CO₂e/m³），当前：2.75：2
请输入新的单位（当前：m³，留空则不修改）：

已更新 energy：{'name': '天然气', 'unit': 'm³', 'size': 2.0}

选择需要修改的类型：
1) 修改能源
2) 修改材料
3) 保存并退出
4) 退出不保存
请输入选择：3
配置已成功保存到 config.json
```

## 单元测试
```bash
 python -m unittest test_carbon.py
```
## 项目结构
```plaintext
.
├── carbon.py               # 主程序文件
├── test_carbon.py          # 单元测试文件
├── modify_config.py        # 允许用户修改能源和材料配置的脚本
├── config.json             # 碳排放系数配置文件
└── README.md               # 项目说明文件
```