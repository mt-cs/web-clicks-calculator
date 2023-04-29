import json
import csv
from collections import Counter


class ClickCounter:
    """A class for counting the number of clicks for a list of URLs.

    Args:
        encoded_data_file (str): The path to the CSV file containing long url and shortened links or "encodes".
        decoded_data_file (str): The path to the JSON file containing raw data on Bitlink clicks.

    Attributes:
        encoded_data_file (str): The path to the CSV file containing the encoded URL data.
        decoded_data_file (str): The path to the JSON file containing the decoded URL data.
        encoding_map (dict): A dictionary containing the mapping of Bitlink URL to long URL.
        clicks (dict): A dictionary containing the counts of clicks for each long URL.
    """

    def __init__(self, encoded_data_file, decoded_data_file):
        self.encoded_data_file = encoded_data_file
        self.decoded_data_file = decoded_data_file
        self.encoding_map = {}
        self.clicks = {}
        self.result = {}

    def get_encoded_data(self):
        """Read the CSV file and return the data.

        Returns:
            list: The data from the encoded data file as a list of lists.

        Raises:
            FileNotFoundError: If the encodes.csv file does not exist.
        """
        try:
            with open(self.encoded_data_file, 'r') as csv_file:
                reader = csv.reader(csv_file)
                # Skip the first row (header)
                next(reader)
                raw_data = [row for row in reader]
            return raw_data

        except FileNotFoundError:
            raise FileNotFoundError(f"Encoded data file not found: {self.encoded_data_file}")

    def create_encoding_map(self):
        """Create a dictionary mapping the Bitlink URL to long URL from raw data."""
        raw_data = self.get_encoded_data()
        for record in raw_data:
            key = f'http://{record[1]}/{record[2]}'
            value = record[0]
            self.encoding_map.update({key: value})

    def get_decoded_url(self):
        """
        Parse a JSON file, checks if the bitlink url is in encoding map,
        and return a list of decoded long URL.

        Returns:
            str: The long URL list from the JSON data

        Raises:
            FileNotFoundError: If the decodes data file does not exist.
            KeyError: If the 'bitlink' key is not present in the JSON data.
        """

        try:
            with open(self.decoded_data_file) as f:
                input_json_data = json.load(f)

            decoded_data = []
            for data in input_json_data:
                url = data['bitlink']
                # keep desired bitlink urls if they are in encoding map
                if url in self.encoding_map:
                    decoded_data.append(self.encoding_map.get(url))

            return decoded_data

        except FileNotFoundError:
            raise FileNotFoundError(f"Decoded data file not found: {self.decoded_data_file}")

        except KeyError:
            raise KeyError("JSON data does not contain a 'bitlink' key")

    def count_clicks(self):
        """
        Count the number of clicks for each long URL
        and save the url and its click count in clicks map
        """
        decoded_url = self.get_decoded_url()
        self.clicks = dict(Counter(decoded_url))

    def get_sorted_result(self):
        """
        Sort the results of click counts in descending order
        and return them as a list of dictionary.
        """
        self.clicks = dict(sorted(self.clicks.items(), key=lambda item: item[1], reverse=True))
        return [self.clicks]


def main():
    encoded_data_file = 'encodes.csv'
    decoded_data_file = 'decodes.json'

    counter = ClickCounter(encoded_data_file, decoded_data_file)

    # Create a map of Bitlink url as key and long url as value
    counter.create_encoding_map()

    # Get desired records from the json file and count the number of clicks
    counter.count_clicks()

    # Get sorted result based on clicks in descending order
    result = counter.get_sorted_result()
    print(f"The sorted URL and click count result is: {result}")


if __name__ == '__main__':
    main()
