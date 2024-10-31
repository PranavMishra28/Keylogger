import unittest
from unittest.mock import patch, MagicMock
import threading
import sys

# Import the Keylogger class from your keylogger module
from keylogger import Keylogger

class TestKeylogger(unittest.TestCase):
    def setUp(self):
        self.args = MagicMock()
        self.args.outfile = 'test_keys.log'
        self.args.interval = 1
        self.kl = Keylogger(self.args)

    def test_callback(self):
        event = MagicMock()
        event.name = 'a'
        self.kl.callback(event)
        self.assertEqual(self.kl.log, 'a')

        event.name = 'space'
        self.kl.callback(event)
        self.assertEqual(self.kl.log, 'a ')

        event.name = 'enter'
        self.kl.callback(event)
        self.assertEqual(self.kl.log, 'a \n')

        event.name = 'decimal'
        self.kl.callback(event)
        self.assertEqual(self.kl.log, 'a \n.')

        event.name = 'shift'
        self.kl.callback(event)
        self.assertEqual(self.kl.log, 'a \n.[SHIFT]')

    def test_write_log_to_file(self):
        self.kl.log = 'test log'
        self.kl.write_log_to_file()
        with open(self.args.outfile, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'test log')

    def test_send_log(self):
        with patch.object(self.kl, 'write_log_to_file') as mock_write_log_to_file:
            self.kl.log = 'test log'
            self.kl.send_log()
            mock_write_log_to_file.assert_called_once()
            self.assertEqual(self.kl.log, '')

    def test_loop_send_log(self):
        with patch.object(self.kl, 'send_log') as mock_send_log:
            self.kl.loop_send_log()
            mock_send_log.assert_called_once()

    def test_start(self):
        with patch('keyboard.on_release') as mock_on_release, patch('keyboard.wait') as mock_wait:
            self.kl.start()
            mock_on_release.assert_called_once()
            mock_wait.assert_called_once()

    def test_keyboard_interrupt(self):
        with patch('keyboard.on_release'), patch('keyboard.wait', side_effect=KeyboardInterrupt), patch.object(self.kl, 'send_log') as mock_send_log:
            with self.assertRaises(SystemExit):
                self.kl.start()
            mock_send_log.assert_called_once()

if __name__ == '__main__':
    unittest.main()