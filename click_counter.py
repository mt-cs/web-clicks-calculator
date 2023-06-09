import argparse
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
            value = record[0].rstrip("/")
            self.encoding_map.update({key: value})

    def get_decoded_url(self):
        """
        Parse a JSON file, checks if the bitlink url is in encoding map,
        and clicks happened in 2021,
        then return a list of decoded long URL.

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
                timestamp = data['timestamp']
                # Only store the url that passed the given specification
                # keep urls if they are in encoding map, and clicks occur 2021
                if url in self.encoding_map and timestamp.startswith('2021'):
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
        # The built-in counter class makes the code more readable and concise
        counts = Counter(decoded_url)
        self.clicks = [{url: count} for url, count in counts.items()]

    def get_sorted_result(self):
        """
        Sort the results of click counts in descending order
        and return them as a list of dictionary.
        """
        # uses the sorted function to sort the results of the click counts
        # It's more efficient for large datasets, as it uses an algorithm called Timsort
        # that has a worst-case time complexity of O(n log n)
        # compared to a traditional sorting algorithm implemented in a for loop that has a time complexity of O(n^2).
        return sorted(self.clicks, key=lambda x: next(iter(x.values())), reverse=True)

    def run_click_counter(self):
        """
        Runs the click counter.

        Creates a map of Bitlink url as key and long url as value,
        and counts the number of clicks for each long URL.

        Returns:
            list: The sorted URL and click count result.

        Raises:
            FileNotFoundError: If the encoded or decoded data file does not exist.
            KeyError: If the 'bitlink' key is not present in the JSON data.
        """
        # Create a map of Bitlink url as key and long url as value
        self.create_encoding_map()

        # Get desired records from the json file and count the number of clicks
        self.count_clicks()

        # Get sorted result based on clicks in descending order
        return self.get_sorted_result()


if __name__ == '__main__':
    encoded_data_file = 'encodes.csv'
    decoded_data_file = 'decodes.json'

    # Allow other developers to pass their own data file paths
    # using command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encoded_data_file', type=str, default=encoded_data_file,
                        help='Path to the CSV file containing the encoded long URL data')
    parser.add_argument('-d', '--decoded_data_file', type=str, default=decoded_data_file,
                        help='Path to the JSON file containing the decoded Bitlink URL data')
    args = parser.parse_args()

    # Create instance, run ClickCounter class, and print result
    counter = ClickCounter(args.encoded_data_file, args.decoded_data_file)
    result = counter.run_click_counter()
    print(result)

