import pytest
from i18ntools.parse_i18n_file import parse_i18n_file


def test_parse_file():
    parsed_data = parse_i18n_file("tests/resources/example.properties")
    assert len(parsed_data.keys()) == 6
    assert (
        parsed_data["instructorService.removeSession.success"] == "{0} session removed."
    )
    assert parsed_data["default.invalid.min.message"] == (
        "Property [{0}] of class [{1}] with value "
        "[{2}] is less than minimum value [{3}]"
    )

    assert parsed_data[
        "instructor.submitWithCustomTime.customSubmitTS.missing.error"
    ] == (
        "The customSubmitTS parameter is missing. \\"
        "\n    It must be present and of type Date."
    )

    assert parsed_data["TheBeths.YourSide.lyrics"] == (
        "I want to see you knocking at the door. \\"
        "\n    I wanna leave you out there waiting in the downpour. \\"
        "\n    Singing that you’re sorry, dripping on the hall floor."
    )


def test_parse_file_and_remove_slashes():
    parsed_data = parse_i18n_file(
        "tests/resources/example.properties", remove_back_slashes=True
    )
    assert len(parsed_data.keys()) == 6
    assert (
        parsed_data["instructorService.removeSession.success"] == "{0} session removed."
    )
    assert parsed_data["default.invalid.min.message"] == (
        "Property [{0}] of class [{1}] with value "
        "[{2}] is less than minimum value [{3}]"
    )

    assert parsed_data[
        "instructor.submitWithCustomTime.customSubmitTS.missing.error"
    ] == (
        "The customSubmitTS parameter is missing. "
        "\n    It must be present and of type Date."
    )

    assert parsed_data["TheBeths.YourSide.lyrics"] == (
        "I want to see you knocking at the door. "
        "\n    I wanna leave you out there waiting in the downpour. "
        "\n    Singing that you’re sorry, dripping on the hall floor."
    )
    # TODO Note: the way removing backslashes is implemented in parse_i18n_file
    # does not work well in practice.
    # Since we are removing the backslashes but preserving newlines,
    # as shown in the test above, then the translations also have
    # newlines in them and no backslashes.
    # Which means they are not valid properties files and therefore cannot
    # be used by software and they cannot be automatically formatted by
    # prettier prettier-plugin-properties .
    # I guess we could try manually removing all newlines from the
    # translations returned by Azure...


def test_parse_file_with_duplicate_keys():
    """SyntaxWarning is raised for files with duplicate keys"""
    with pytest.raises(SyntaxWarning):
        parse_i18n_file("tests/resources/duplicate.properties")
