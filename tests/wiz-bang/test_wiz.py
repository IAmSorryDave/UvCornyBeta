import pytest
from pathlib import Path


@pytest.fixture
def wiz_module_label(project_name):
    return f"{project_name}.{Path(__file__).parent.name}.wiz"


@pytest.fixture
def wiz_fn(wiz_module_label):
    return pytest.importorskip(wiz_module_label)


def test_wiz(wiz_fn):
    assert wiz_fn() == "BANG"
