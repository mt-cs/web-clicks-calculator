import unittest
import os
import json
import csv

from click_counter import ClickCounter


class TestClickCounter(unittest.TestCase):
    def setUp(self):
        # create test CSV file
        self.encoded_file = 'test_encodes.csv'

        # write test data to CSV file
        self.encoded_data = [
            ['https://google.com/', 'bit.ly', 'test1'],
            ['http://github.com/', 'bit.ly', 'test2'],
            ['http://twitter.com/', 'bit.ly', 'test3']
            ]

        with open(self.encoded_file, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['long_url', 'domain', 'hash'])
            for row in self.encoded_data:
                writer.writerow(row)

        # create ClickCounter instance for testing
        self.counter = ClickCounter(self.encoded_file, 'test_data.json')

        # create test json file
        self.decoded_file = 'test_decodes.json'
        # write test data to JSON file
        self.decoded_data = [
            {'bitlink': 'http://bit.ly/test1', 'user_agent': 'breathe', 'timestamp': '2020-09-10T00:00:00Z'},
            {'bitlink': 'http://bit.ly/test1', 'user_agent': 'breathe', 'timestamp': '2021-09-10T00:00:00Z'},
            {'bitlink': 'http://bit.ly/test2', 'user_agent': 'breathe', 'timestamp': '2021-09-10T00:00:00Z'},
            {'bitlink': 'http://bit.ly/test3', 'user_agent': 'breathe', 'timestamp': '2021-09-10T00:00:00Z'},
            {'bitlink': 'http://bit.ly/test2', 'user_agent': 'listen', 'timestamp': '2020-09-10T00:00:00Z'},
            {'bitlink': 'http://bit.ly/test3', 'user_agent': 'listen', 'timestamp': '2020-09-10T00:00:00Z'},
            {'bitlink': 'http://bit.ly/test2', 'user_agent': 'listen', 'timestamp': '2021-09-10T00:00:00Z'},
            {'bitlink': 'http://bit.ly/test3', 'user_agent': 'listen', 'timestamp': '2021-09-10T00:00:00Z'},
            {'bitlink': 'http://bit.ly/test3', 'user_agent': 'smile', 'timestamp': '2021-09-10T00:00:00Z'}
        ]
        with open(self.decoded_file, 'w') as f:
            json.dump(self.decoded_data, f)

        # create ClickCounter instance for testing
        self.counter = ClickCounter(self.encoded_file, self.decoded_file)
        self.counter.create_encoding_map()

    def tearDown(self):
        # remove temporary files
        os.remove(self.encoded_file)
        os.remove(self.decoded_file)

    def test_get_encoded_data(self):
        expected_data = self.encoded_data
        actual_data = self.counter.get_encoded_data()
        self.assertEqual(expected_data, actual_data)

    def test_create_encoding_map(self):
        expected_map = {
            'http://bit.ly/test1': 'https://google.com',
            'http://bit.ly/test2': 'http://github.com',
            'http://bit.ly/test3': 'http://twitter.com'
        }
        self.counter.create_encoding_map()
        actual_map = self.counter.encoding_map
        self.assertEqual(expected_map, actual_map)

    def test_get_decoded_url(self):
        expected_data = [
            'https://google.com',
            'http://github.com',
            'http://twitter.com',
            'http://github.com',
            'http://twitter.com',
            'http://twitter.com']
        actual_data = self.counter.get_decoded_url()
        self.assertEqual(expected_data, actual_data)

    def test_count_clicks(self):
        expected_clicks = [{'https://google.com': 1}, {'http://github.com': 2}, {'http://twitter.com': 3}]
        self.counter.count_clicks()
        actual_clicks = self.counter.clicks
        self.assertEqual(expected_clicks, actual_clicks)

    def test_get_sorted_result(self):
        expected_result = [{'http://twitter.com': 3}, {'http://github.com': 2}, {'https://google.com': 1}]
        self.counter.count_clicks()
        actual_result = self.counter.get_sorted_result()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()