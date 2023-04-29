import json
import csv
from collections import Counter

class ClickCounter:
    def __init__(self, encoded_data_file, decoded_data_file):
        self.encoded_data_file = encoded_data_file
        self.decoded_data_file = decoded_data_file
        self.clicks = {}

    def get_bitlink_url(self):
        """
        Parse a JSON file and return the bitlink URL.

        Returns:
            str: The bitlink URL from the JSON data in the decodes data file.

        Raises:
            FileNotFoundError: If the decodes data file does not exist.
            KeyError: If the 'bitlink' key is not present in the JSON data.
        """
        try:

            with open(self.encoded_data_file) as f:
                input_json_data = json.load(f)

            encoded_data = []
            for data in input_json_data:
                encoded_data.append(data['bitlink'])

            return encoded_data

        except FileNotFoundError:
            raise FileNotFoundError(f"Encoded data file not found: {self.encoded_data_file}")

        except KeyError:
            raise KeyError("JSON data does not contain a 'bitlink' key")

    def count_clicks(self):
        encoded_url = self.get_bitlink_url()
        self.clicks = dict(Counter(encoded_url))


        # for record in self.encoded_data:
        #     if record in self.click_count_encoded:
        #         self.click_count_encoded[record] += 1
        #     else:
        #         self.click_count_encoded[record] = 1
        #
        # for record in self.raw_data:
        #     if record in self.click_count_raw:
        #         self.click_count_raw[record] += 1
        #     else:
        #         self.click_count_raw[record] = 1

    def parse_encoded_data(self):
        with open(self.encoded_data_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the first row (header)
            next(reader)
            raw_data = [row for row in reader]
        return raw_data

def main():
    encoded_data_file = 'decodes.json'
    decoded_data_file = 'encodes.csv'

    counter = ClickCounter(encoded_data_file, decoded_data_file)
    # bitlink_url = counter.get_bitlink_url()

    # print(f"The bitlink URL is: {bitlink_url}")


    # raw_data = counter.parse_encoded_data()
    # print(raw_data)

    counter.count_clicks()
    print(counter.clicks)


if __name__ == '__main__':
    main()
