import pytest

from qaseio.models import AccessLevel, ProjectCreate


@pytest.mark.parametrize(
    "_type, value",
    [
        (AccessLevel.ALL, "all"),
        (AccessLevel.GROUP, "group"),
        (AccessLevel.NONE, "none"),
    ],
)
def test_access_level_types(_type, value):
    assert _type.value == value


@pytest.mark.parametrize(
    "data",
    [
        ("", "TE"),
        ("a" * 65, "TESTED", "", AccessLevel.NONE),
        ("test", "TESTED", "a" * 65, AccessLevel.ALL),
        ("test", "TESTED", None, AccessLevel.GROUP, "123414"),
    ],
)
def test_valid_project_creation(data):
    ProjectCreate(*data)


@pytest.mark.parametrize(
    "data",
    [
        ("", "T"),
        ("", None),
        ("a" * 65, "TESTEDS", "", AccessLevel.NONE),
        ("test", "Tes.sd"),
        ("test", "Tes123"),
        ("test", "русский"),
        ("test", "TESTED", None, AccessLevel.GROUP),
    ],
)
def test_invalid_project_creation(data):
    with pytest.raises((ValueError, TypeError)):
        ProjectCreate(*data)