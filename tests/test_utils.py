import pytest
from utils import read_csv_files

def test_read_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        read_csv_files(["nonexistent.csv"])