import pytest
from pathlib import Path


@pytest.fixture
def main_module_label(project_name):
    return f"{project_name}.{Path(__file__).parent.name}.main"


@pytest.fixture
def main_fn(main_module_label):
    return pytest.importorskip(main_module_label)


def test_main(main_fn):
    assert main_fn() is None
