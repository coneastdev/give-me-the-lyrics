import unittest
from unittest.mock import patch
import sys
import os
import customtkinter as ctk

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from appUI import App  # Updated to import the App class

class TestAppUI(unittest.TestCase):

    def setUp(self):
        # Create the CustomTkinter root and the app instance
        self.root = App()  # Instantiate the App class

    def tearDown(self):
        # Destroy the CustomTkinter root after each test
        self.root.destroy()

    @patch('appUI.getLyrics')  # Mock any external dependencies
    def test_button_click(self, mock_getLyrics):
        # Simulate entering a valid song query
        self.root.userInputEntry.insert(0, "livin thing")

        # Ensure the button is enabled
        self.root.checkEntry()

        # Simulate a button click
        self.root.userSearchButton.invoke()

        # Assert that the mocked function was called with the correct arguments
        mock_getLyrics.assert_called_once_with("livin%20thing", "genius")

    def test_input_field(self):
        # Simulate entering text into an input field
        self.root.userInputEntry.insert(0, "Test Input")

        # Assert that the input field contains the expected text
        self.assertEqual(self.root.userInputEntry.get(), "Test Input")

    def test_save_button(self):
        # Simulate displaying lyrics
        self.root.setOutput("Sample Lyrics")

        # Assert that the save button is enabled
        self.assertEqual(self.root.saveButton.cget("state"), "normal")

    def test_output_textbox(self):
        # Simulate setting output text
        self.root.setOutput("Sample Lyrics")

        # Assert that the output textbox contains the correct text
        self.assertEqual(self.root.outputTextbox.get("1.0", "end-1c"), "Sample Lyrics")

    def test_option_menu(self):
        # Change the value of the option menu
        self.root.sourceVar.set("LyricAdvisor")

        # Assert that the sourceVar value is updated
        self.assertEqual(self.root.sourceVar.get(), "LyricAdvisor")

    @patch('customtkinter.set_appearance_mode')
    def test_appearance_mode(self, mock_set_appearance_mode):
        # Simulate setting the appearance mode
        ctk.set_appearance_mode("light")

        # Assert that the appearance mode was set correctly
        mock_set_appearance_mode.assert_called_once_with("light")

if __name__ == '__main__':
    unittest.main()