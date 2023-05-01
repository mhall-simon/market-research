import pytest


@pytest.fixture(name="change_test_dir", autouse=True)
def change_test_dir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
