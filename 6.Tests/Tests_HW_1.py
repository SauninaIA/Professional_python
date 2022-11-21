import unittest
from func_testing import show_all_docs_info, add_new_doc, delete_doc, documents
from unittest.mock import patch


class TestFunction(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp ===> START TEST')

    def tearDown(self) -> None:
        print('tearDown ===> STOP TEST')


    # @patch('builtins.input')
    # def test_add_new_doc(self, mocked_input):
    #     mocked_input.side_effect = ['1234 567809', 'passport', 'Tom', '1']
    #     result = add_new_doc()
    #     self.assertEqual(result, '1')

    # def test_show_all_docs_info(self):
    #     result = show_all_docs_info()
    #     reference = ['"passport" "2207 876234" "Василий Гупкин"', '"invoice" "11-2" "Геннадий Покемонов"', '"insurance" "10006" "Аристарх Павлов"']
    #     self.assertEqual(result, reference)

    @patch('builtins.input')
    def test_delete_doc(self, mocked_input):
        mocked_input.return_value = '2207 876234'
        result = delete_doc()
        reference = '2207 876234', True
        self.assertEqual(result, reference)
