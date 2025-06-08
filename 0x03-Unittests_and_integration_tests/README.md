# GithubOrgClient Test Suite

This project contains unit and integration tests for the `GithubOrgClient` class and utility functions used for accessing GitHub organization data.

## Files

- `client.py`: Contains the `GithubOrgClient` class.
- `utils.py`: Contains helper functions (`get_json`, `memoize`, `access_nested_map`).
- `fixtures.py`: Provides example payloads for integration tests.
- `test_utils.py`: Unit tests for functions in `utils.py`.
- `test_client.py`: Contains both unit and integration tests for `GithubOrgClient`.

## Running Tests

To run all tests:

```bash
python3 -m unittest discover
