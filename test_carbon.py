import unittest
from io import StringIO
from unittest.mock import patch

import carbon

class TestCarbonCalculator(unittest.TestCase):
    
    # 测试get_item_quantity函数
    @patch('builtins.input', side_effect=['10.5'])  # 模拟用户输入10.5
    def test_get_item_quantity_valid(self, mock_input):
        item = {'name': '电力', 'unit': 'kWh'}
        result = carbon.get_item_quantity(item)
        self.assertEqual(result, 10.5)

    @patch('builtins.input', side_effect=['-5', '0', '20'])  # 模拟无效输入，再输入有效值
    def test_get_item_quantity_invalid(self, mock_input):
        item = {'name': '天然气', 'unit': 'm³'}
        result = carbon.get_item_quantity(item)
        self.assertEqual(result, 20)

    # 测试calculate函数
    def test_calculate_carbon(self):
        necessities = [
            {'name': '电力', 'size': 0.5, 'unit': 'kWh', 'num': 100},
            {'name': '天然气', 'size': 2.75, 'unit': 'm³', 'num': 50}
        ]
        result, total_emissions = carbon.calculate(necessities)
        self.assertIn('电力', result)
        self.assertIn('天然气', result)
        self.assertAlmostEqual(total_emissions, 187.5)  # 50 + 137.5 = 187.5

if __name__ == '__main__':
    unittest.main()
