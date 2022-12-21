from unittest.mock import patch

from django.core.management import call_command
from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    def test_wait_for_db_ready(self, mock_check):
        """Test waiting for DB if it is ready"""

        # Arrange
        mock_check.return_value = True

        # Act
        call_command('wait_for_db')

        # Assert
        mock_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, mock_sleep, mock_check):
        """Test waiting for DB when getting OperationalError"""

        # Arrange
        # DB raises a PsyCopg2Error when it isn't ready to accept connections and OperationalError
        # when it is ready but is hasn't set up the testing DB that we want to use
        mock_check.side_effect = [Psycopg2OpError] * 2 + [OperationalError] * 3 + [True]

        # Act
        call_command('wait_for_db')

        # Assert
        self.assertEqual(mock_check.call_count, 6)

        mock_check.assert_called_with(databases=['default'])
