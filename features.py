from feature_files.dadjoke import dadjoke
from feature_files.web_search import googleSearch
from feature_files.text_summarizer import summary
from feature_files.open_app import OpenApp
from feature_files.dictionary import GiveAntonym, GiveSynonym, GiveMeaning
from feature_files.random_facts import RandomFacts
from feature_files.Weather import Weather
from feature_files.contact import create_new_contact, del_contact, show_all_the_contacts, show_one_contact
from fuzzywuzzy import fuzz
import json


class Assistant():
    def __init__(self, name):
        self.name = name

    def whoAmI(self):
        return "Hello, I am {}, your virtual assistant. Say 'What can you do?' to learn more about commands".format(self.name)

    def dadjoke(self, reqs_confirm=False):
        return dadjoke()

    def google_search(self, query='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Please enter what you wish to search for: "})
        return googleSearch(query)

    def summarize_text(self, text='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Please enter a paragraph you want to summarize. It should have more than 5 sentences. "})
        return summary(text)

    def random_facts(self, reqs_confirm=False):
        return RandomFacts()

    def open_app(self, text='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Which app do you want to open? "})
        OpenApp(text)
        return "App opened"

    def GiveMeaning(self, query='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Which word's meaning should I show? "})
        return GiveMeaning(query)

    def GiveSynonym(self, query='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Which word's synonyms should I show? "})
        return GiveSynonym(query)

    def GiveAntonym(self, query='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Which word's antonyms should I tell you? "})
        return GiveAntonym(query)

    def weather(self, reqs_confirm=False):
        Weather()
        return "Showing weather"

    def create_contact(self, firstname='', lastname='', phone_nums=None, emails=None, reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Adding a contact. Please tell me the first name of the contact. "})
        create_new_contact(firstname, lastname, phone_nums, emails)
        return "Contact created."

    def delete_contact(self, firstname='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Deleting a contact. Please enter the first name of the contact.  "})
        del_contact(firstname)
        return "Contact deleted."

    def show_all_contacts(self):
        return show_all_the_contacts()

    def show_one_of_my_contacts(self, firstname='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Whose contact should I show?"})
        return show_one_contact(firstname)

        # ADD EDIT CONTACT FEATURE AFTER GUI COMPLETED

    def show_phones(self, firstname='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Whose phone numbers should I show? "})
        with open("feature_files/data/user_contacts.json", "r") as readfile:
            read = dict(json.load(readfile))
            readfile.close()
        max_ratio = 0
        for i in read.keys():
            x = fuzz.ratio(i, firstname)
            if x >= max_ratio:
                max_ratio = x
                firstname = i
        if max_ratio == 0:
            return "That contact doesn't exist."
        return "Phone numbers of {} {}: {}".format(firstname, read.get(firstname).get("lastname"), ', '.join(list(read.get(firstname).get("phone"))))

    def show_emails(self, firstname='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Whose email addresses should I show?"})
        with open("feature_files/data/user_contacts.json", "r") as readfile:
            read = dict(json.load(readfile))
            readfile.close()
        max_ratio = 0
        for i in read.keys():
            x = fuzz.ratio(i, firstname)
            if x >= max_ratio:
                max_ratio = x
                firstname = i
        if max_ratio == 0:
            return "That contact doesn't exist."
        return "Emails of {} {}: {}".format(firstname, read.get(firstname).get("lastname"), ', '.join(list(read.get(firstname).get("email"))))


