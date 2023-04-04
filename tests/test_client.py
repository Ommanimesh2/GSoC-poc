import unittest
from src.demoapi.api import DemoAPi

class TestDummyJsonClient(unittest.TestCase):
    def setUp(self):
        self.client = DemoAPi()

    def test_get_products(self):
        products = self.client.products.get()
        self.assertIsInstance(products, list)

    def test_get_product(self):
        product = self.client.products.get(id=1)
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 1)

    def test_get_todos(self):
        todos = self.client.todo.get()
        self.assertIsInstance(todos, dict)
        self.assertEqual(todos, list)

    def test_get_product(self):
        todo = self.client.products.get(id=1)
        self.assertIsInstance(todo, dict)
        self.assertEqual(todo['id'], 1)