import json
import unittest
from app import app
from Models import Customer


class TestAPI(unittest.TestCase):
    CUSTOMERS_URL = "http://127.0.0.1:5000/customers"

    customer_id = "/4"
    new_customer = Customer(4,"Test", "Test", "test@gmail.com", "2022-04-07")

    expected_customer = {'customer': {"birthdate": "2022-04-07",
                                      "email": "test@gmail.com",
                                      "id": 4,
                                      "name": "Test",
                                      "surname": "Test"}}

    update_customer = Customer(4,
        "Update", "Update", "test@gmail.com", "2022-04-07")

    def test_1_get_all_customers(self):
        resp = app.test_client().get(self.CUSTOMERS_URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEquals(len(json.loads(resp.data)), 2)
        print("Test 1 completed")

    def test_2_add_new_cutomer(self):
        resp = app.test_client().post(self.CUSTOMERS_URL,
                           json=self.new_customer.serialize())
        self.assertEqual(resp.status_code, 200)
        print("Test 2 completed")

    def test_3_get_single_customer(self):
        resp = app.test_client().get(self.CUSTOMERS_URL + self.customer_id)
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(json.loads(resp.data), self.expected_customer)
        print("Test 3 completed")

    def test_4_update_customer(self):
        resp = app.test_client().put(
            self.CUSTOMERS_URL + self.customer_id, json=self.update_customer.serialize())
        self.assertEqual(resp.status_code, 200)
        print("Test 4 completed")

    def test_5_delete_customer(self):
        resp = app.test_client().delete(self.CUSTOMERS_URL + self.customer_id)
        self.assertEqual(resp.status_code, 200)
        print("Test 5 completed")


if __name__ == "__main__":
    unittest.main()
