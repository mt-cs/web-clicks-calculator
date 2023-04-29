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

## Dependencies

## Output

* When run, this program outputs the following to the console:
```
A sorted array of JSON objects containing the long URL as the key and the click count as the value. 
The array is sorted descending by click count.

The form is as follows: [{"LONG_URL": count}, {"LONG_URL": count}]

Example: [{"https://google.com": 3}, {"https://www.twitter.com" : 2}]
```


## Language and Framework

Feel free to choose any language and framework you are comfortable with. The language that we primarily use at Bitly on the backend is Go, however, you should not feel pressured to use Go if you are not currently comfortable with it. We want you to be able to focus more on your solution than the tools and language.

If you are advanced to the next stage of interviews, the live coding will involve making minor improvements/additions to your coding challenge solution which is why we emphasize using a language that you can navigate comfortably. 

## Run 
Run the script with encodes.csv and decodes.json file paths:
```
python script.py -e path/your/encodes.csv -d path/your/decodes.json
```
The argparse module is used to parse command line arguments. The encoded_data_file and decoded_data_file variables are set to default values, but can be overwritten by command line arguments.

# Test

This solution includes unit tests for each function. To test the program, run this script on command line:
```
python -m unittest test_click_counter.py
```

## Notes

* Bitly Glossary:
  * Bitlink: the short link created by the Bitly platform
  * Encode: the act of shortening a long link into a bitlink on the Bitly platform
  * Decode (or click): a metric collected each time a bitlink is accessed and performs the redirect
* The encodes.csv file contains users identified by `user_id` who created a redirect from https://`domain`/`hash` to `long_url`.
