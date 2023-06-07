# Tests

This folder contains unit and integration tests organized with **pytest**.

## Tests execution

All commands should be run from the root directory of the repository.

Execute local unit tests:

```
python -m pytest tests -m unittest
```

Execute integration tests:
```
python -m pytest tests -m integration
```

Execute all tests (unit tests will be run first):
```
python -m pytest tests
```

You need to be authorized in Google Cloud before executing integration tests.
Run the following commands in your terminal to be authorized:
```
gcloud auth login
gcloud config set project np-quotecenter
gcloud auth application-default login
```

## Tests configuration

### pytest.ini

File `pytest.ini` is used to configure tests globally. 
The file defines:
- `addopts`: command line parameters for pytest which configure pytest's output (short type of exceptions, lists all executing tests)
- `markers`: test types (unit tests, integration tests)
- `filterwarnings`: hide not relevant deprecation warnings

Tests can be separated between unit and integration tests by the Python decorator `@pytest.mark.<test type>`.

### conftest.py

File `conftest.py` is used to create fixtures globally. Pytest fixtures are used to prepare everything what tests need.
By default, fixtures in `conftest.py` use `scope='session'` parameters. 
It means that the code in fixtures runs only once during a test session.
