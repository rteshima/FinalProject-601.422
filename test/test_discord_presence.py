import unittest
import utils.discord_presence as discord

class DiscordPresenceTestCase(unittest.TestCase):
    
    # Implement method for instantiating objects
    def setUp(self):
        pass
    
    # Follow this format for writing our future test cases
    def test_start_presence(self):
        self.assertEqual(True, discord.connected)
        discord.start_presence()
