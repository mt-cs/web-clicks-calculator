import json
import csv

class ClickCounter:
    def __init__(self, encoded_data_file, decoded_data_file):
        self.encoded_data_file = encoded_data_file
        self.decoded_data_file = decoded_data_file
        self.clicks = {}

    # def decode_data(self):
    #     with open(self.encoded_data_file, 'r') as f:
    #         encoded_data = json.load(f)
    #
    #     decoded_data = []
    #     for data in encoded_data:
    #         decoded_data.append({
    #             'bitlink': data['bitlink'],
    #             'timestamp': data['timestamp'],
    #             'user_agent': data['user_agent'],
    #             'referrer': data['referrer'],
    #             'remote_ip': data['remote_ip']
    #         })
    #
    #     with open(self.decoded_data_file, 'w') as f:
    #         json.dump(decoded_data, f)
    #
    #     return decoded_data
    #
    # def get_bitlink_url(self):
    #     decoded_data = self.decode_data()
    #
    #     # Extract the bitlink URL from the first record
    #     bitlink_url = decoded_data[0]['bitlink']
    #
    #     return bitlink_url

    def get_bitlink_url(self):
        """
        Parse a JSON file and return the bitlink URL.

        Returns:
            str: The bitlink URL from the JSON data in the decoded data file.

        Raises:
            FileNotFoundError: If the decoded data file does not exist.
            KeyError: If the 'bitlink' key is not present in the JSON data.
        """
        try:

            with open(self.decoded_data_file) as f:
                data = json.load(f)

            bitlink_url = data[0]['bitlink']

            return bitlink_url

        except FileNotFoundError:
            raise FileNotFoundError(f"Decoded data file not found: {self.decoded_data_file}")

        except KeyError:
            raise KeyError("JSON data does not contain a 'bitlink' key")

    # def count_clicks(self):
    #     for record in self.encoded_data:
    #         if record in self.click_count_encoded:
    #             self.click_count_encoded[record] += 1
    #         else:
    #             self.click_count_encoded[record] = 1
    #
    #     for record in self.raw_data:
    #         if record in self.click_count_raw:
    #             self.click_count_raw[record] += 1
    #         else:
    #             self.click_count_raw[record] = 1
    #
    # def print_click_counts(self):
    #     print("Encoded data click counts:")
    #     for record, count in self.click_count_encoded.items():
    #         print(f"{record}: {count}")
    #
    #     print("\nRaw data click counts:")
    #     for record, count in self.click_count_raw.items():
    #         print(f"{record}: {count}")

    def parse_encoded_data(self):
        with open(self.encoded_data_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the first row (header)
            next(reader)
            raw_data = [row for row in reader]
        return raw_data

def main():
    encoded_data_file = 'encodes.csv'
    decoded_data_file = 'decodes.json'

    counter = ClickCounter(encoded_data_file, decoded_data_file)
    bitlink_url = counter.get_bitlink_url()

    raw_data = counter.parse_encoded_data()
    print(raw_data)

    print(f"The bitlink URL is: {bitlink_url}")


if __name__ == '__main__':
    main()
