import unittest
import requests
from calls import get_data
from mock import patch, Mock


class TestCalls(unittest.TestCase):

    def test_get_data(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            assert get_data() == 200


if __name__ == '__main__':
    unittest.main()
