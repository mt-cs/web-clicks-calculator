import json
import csv
from collections import Counter


class ClickCounter:
    def __init__(self, encoded_data_file, decoded_data_file):
        self.encoded_data_file = encoded_data_file
        self.decoded_data_file = decoded_data_file
        self.encoding_map = {}
        self.clicks = {}
        self.result = {}

    def get_encoded_data(self):
        with open(self.encoded_data_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the first row (header)
            next(reader)
            raw_data = [row for row in reader]
        return raw_data

    def create_encoding_map(self):
        raw_data = self.get_encoded_data()
        for record in raw_data:
            key = ('http://' + record[1] + '/' + record[2])
            value = record[0]
            self.encoding_map.update({key: value})

        # print(self.encoding_map)

    def get_bitlink_url(self):
        """
        Parse a JSON file and return the bitlink URL.

        Returns:
            str: The bitlink URL from the JSON data in the decodes data file.

        Raises:
            FileNotFoundError: If the decodes data file does not exist.
            KeyError: If the 'bitlink' key is not present in the JSON data.
        """
        # print(self.encoding_map)
        # if 'https://bit.ly/31Tt55y' in self.encoding_map:
        #     print('https://bit.ly/31Tt55y')

        try:
            with open(self.decoded_data_file) as f:
                input_json_data = json.load(f)

            decoded_data = []
            for data in input_json_data:
                decoded_data.append(data['bitlink'])

            return decoded_data

        except FileNotFoundError:
            raise FileNotFoundError(f"Decoded data file not found: {self.decoded_data_file}")

        except KeyError:
            raise KeyError("JSON data does not contain a 'bitlink' key")

    def count_clicks(self):
        decoded_url = self.get_bitlink_url()
        self.clicks = dict(Counter(decoded_url))
        print(self.clicks)

    def get_long_url_count(self):
        for key in self.clicks.copy().keys():
            if key not in self.encoding_map:
                del self.clicks[key]
        print()
        print(self.clicks)

def main():
    encoded_data_file = 'encodes.csv'
    decoded_data_file = 'decodes.json'

    counter = ClickCounter(encoded_data_file, decoded_data_file)

    # Create a map of bitlink url as key and long url as value
    counter.create_encoding_map()

    # Get all records from the json file and count the number of clicks
    counter.count_clicks()

    # Get result by checking if the counted url is in encoding map
    counter.get_long_url_count()


if __name__ == '__main__':
    main()
