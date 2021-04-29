import unittest
import utils.encryption as encryption

class EncryptionTestCase(unittest.TestCase):
    
    # Implement method for instantiating objects
    def setUp(self):
        pass
    
    # Follow this format for writing our future test cases
    def test_encrypt(self):
        pswd = "hello"
        data = '{"nonce": "wfOGp8lJMqc3aGkk", "salt": "AM1s8HRS4QZSMP/97b/XemBwHNl/bO4z7dIcrbuIaU4=", "ct": "xXOe+/vYmgKe681/Vy+KCDcG/B26SMTxhJgJX21QCGW3mppZ1vTkHwHhel7KI4RerfgVxhiSL/ZI8GqK", "tag": "xOvkp5xKAVhKxHmJ46dKJQ=="}'
        payload = bytes(data, "utf-8")

        result = encryption.encrypt(payload, pswd)
        print("result is about to be: ")
        print(result)
        
