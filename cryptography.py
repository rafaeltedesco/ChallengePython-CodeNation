import json
import string
import hashlib


class Crypto:
    """Cesar Decryptography"""

    def __init__(self):
        """"
        json is the content of a json file
        alphabet contains a list with the all letters of the alphabet in lowercase
        key is the key to decrypt
        message is the message to decrypt
        decrypt is the message decrypted
        brief_decrypt is a sha1 hash
        """
        self.json = ''
        self.alphabet = list(string.ascii_lowercase)
        self.key = ''
        self.message = ''
        self.decrypt = ''
        self.brief_decrypt = ''
        self.token = ''

    def set_json(self, f_json):
        self.json = f_json
        self.read_json()

    def read_json(self):
        j = json.loads(self.json)
        self.key = j['numero_casas']
        self.message = j['cifrado']
        self.token = j['token']
        self.decrypt_message()

    def save_json(self):
        info_js = {"numero_casas": self.key, "token": self.token, "cifrado": self.message,
                   "decifrado": self.decrypt, "resumo_criptografico": self.brief_decrypt}
        with open('answer.json', 'w') as f_json:
            json.dump(info_js, f_json)

    def decrypt_message(self):
        msg = self.message
        new_msg = ''
        for letter in msg.lower():
            if (letter.isdigit()) or (letter == '.') or (letter == ' '):
                new_msg += letter
            else:
                new_msg += self.alphabet[self.alphabet.index(letter) - self.key]
        self.decrypt = new_msg
        self.to_hash_sha1()

    def to_hash_sha1(self):
        self.brief_decrypt = hashlib.sha1(self.decrypt.encode('utf-8')).hexdigest()
        self.save_json()