import unittest
from unittest.mock import MagicMock, patch

from src.utils import data_transactions


class TestGetTransactions(unittest.TestCase):

    @patch("builtins.open")
    def test_get_transactions_valid_file(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = '[{"transaction_id": 1, "amount": 100}]'
        transactions = data_transactions("test_file.json")
        self.assertEqual(transactions, [{"transaction_id": 1, "amount": 100}])

    @patch("builtins.open")
    def test_get_transactions_empty_file(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = ""
        transactions = data_transactions("test_file.json")
        self.assertEqual(transactions, [])

    def test_get_transactions_file_not_found(self) -> None:
        transactions = data_transactions("nonexistent_file.json")
        self.assertEqual(transactions, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_transactions_file_not_found_with_patch(self, mock_open: MagicMock) -> None:
        transactions = data_transactions("test_file.json")
        self.assertEqual(transactions, [])
