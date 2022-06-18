import os

import pytest

from dagstd import env


# Note, a test class is used here to allow test setup to be performed
class TestEnv:
    @classmethod
    def setup_class(cls):
        os.environ['TEST_ENV_VAR'] = 'test_value'

    def test_or_none(self):
        assert env.or_none('TEST_ENV_VAR') == 'test_value'
        assert env.or_none('TEST_ENV_VAR_NOT_SET') is None

    def test_or_empty(self):
        assert env.or_empty('TEST_ENV_VAR') == 'test_value'
        assert env.or_empty('TEST_ENV_VAR_NOT_SET') == ''

    def test_or_default(self):
        assert env.or_default('TEST_ENV_VAR', 'default_value') == 'test_value'
        assert env.or_default(
            'TEST_ENV_VAR_NOT_SET',
            'default_value',
        ) == 'default_value'

    def test_or_raise(self):
        with pytest.raises(KeyError):
            env.or_raise('TEST_ENV_VAR_NOT_SET')
        assert env.or_raise('TEST_ENV_VAR') == 'test_value'
