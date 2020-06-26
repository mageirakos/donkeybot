import os.path
import pickle
import re

# for absolute paths 
BOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = BOT_DIR + '.\data\\'

# for EmailParser
try:  
    with open(DATA_DIR+'conversation_dict.pickle', 'rb') as f:
        CONVERSATION_DICT = pickle.load(f)
except:
        CONVERSATION_DICT = {}

# removed for conversation creation when searching same subjects
REGEX_METACHARACTERS = '^$.|?*+(){}[]'

# reply emails quoting past emails
ON_HDR_REGEX = re.compile(r'On (.*?)wrote: ')
QUOTED_REGEX = re.compile(r'(>>+|> >+)')
HEADER_REGEX = re.compile(r'(([_-]{7,})(.*)From:(.*)Sent:(.*)To:(.*)Subject:)')
ORIGINAL_MSG_REGEX = re.compile(r'-----Original Message-----')

# url
URL_REGEX = re.compile(r'(https|http|www)[^ ]*')

# emails sent automatically : find what other patterns exist in those
# AUTOMATIC_MSG = re.compile(r'\\-- THIS IS AN AUTOMATICALLY GENERATED MESSAGE')

