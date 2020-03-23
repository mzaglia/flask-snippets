import pytest

if __name__ == '__main__':
    from app_tests.test_app import TestApp
    pytest.main(['--color=auto', '--no-cov', '-v'])
