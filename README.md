# Web Clicks Calculator
A Python program that calculate the number of clicks for each record that occured in 2021 using encoded and raw data sets. 
 
* Solution should be well documented 
* A README which should include:
  - A list of dependencies of your project, as well as how to install them (we may not be experts in your chosen language, framework, and tools)
  - Instructions for running your application/script (you may include a Dockerfile or a Makefile, but this is not a requirement)
  - A description of any design decisions 

## Description
This coding exercise is from Bitly Backend Engineer - Coding Challenge. This task is designed to be relevant to the kind of work an engineer does at Bitly. 

The data files can be found and downloaded here: https://bit.ly/BitlyBackendCodingChallengeFiles 

This unzipped directory contains the data that you will be using for this challenge:
* `encodes.csv` contains information on shortened links or "encodes" to represent existing data infrastructure.
* `decodes.json` contains raw data on bitlink clicks as a comma-separated list of JSON to represent a large data stream.

## Problem Statement

**Problem:** Calculate the number of clicks from 2021 for each record in the encode.csv data set.

## Environment Set Up
* Install Python 3, check the following link for more info https://realpython.com/installing-python/

* Create virtual environment
Run the following command to create a virtual environment named env:
```
python3 -m venv env
```
Once the virtual environment is created, activate it by running the following command:
```
source env/bin/activate
```
Note: If you're on Windows, use env\Scripts\activate instead.

* Clone this repository
```
git clone https://github.com/mt-cs/web-clicks-calculator.git

cd web-clicks-calculator/
```

## Dependencies
Navigate to the directory where the requirements.txt file is located.

Run the following command to install the dependencies listed in the file:
```
pip install -r requirements.txt
```

Here are the dependencies used in this program:
* argparse==1.4.0: A Python module to write user-friendly command-line interfaces.  The version specified here is 1.4.0.
* jsonschema==4.2.1: A Python library for validating JSON data against a JSON schema. The version specified here is 4.2.1.

## Run 
Run the script with encodes.csv and decodes.json file paths:
```
python script.py -e path/your/encodes.csv -d path/your/decodes.json
```
The argparse module is used to parse command line arguments. The encoded_data_file and decoded_data_file variables are set to default values, but can be overwritten by command line arguments.

## Test

This solution includes unit tests for each function. To test the program, run this script on command line:
```
python -m unittest test_click_counter.py
```

## Output

* When run, this program outputs the following to the console:
```
A sorted array of JSON objects containing the long URL as the key and the click count as the value. 
The array is sorted descending by click count.

The form is as follows: [{"LONG_URL": count}, {"LONG_URL": count}]

Example: [{"https://google.com": 3}, {"https://www.twitter.com" : 2}]
```

Here is the exact output for this program:
```
[{'https://youtube.com': 557}, {'https://twitter.com': 512}, {'https://reddit.com': 510}, {'https://github.com': 497}, {'https://linkedin.com': 496}, {'https://google.com': 492}]
```

## Notes

* Bitly Glossary:
  * Bitlink: the short link created by the Bitly platform
  * Encode: the act of shortening a long link into a bitlink on the Bitly platform
  * Decode (or click): a metric collected each time a bitlink is accessed and performs the redirect
* The encodes.csv file contains users identified by `user_id` who created a redirect from https://`domain`/`hash` to `long_url`.
