from click.testing import CliRunner

from src.skillcorner import skillcorner_line_cleaner


class TestImportData:
    def test_import_data_success(self) -> None:
        runner = CliRunner()
        result = runner.invoke(skillcorner_line_cleaner, ["tests/data/data.log"])
        assert result.exit_code == 0

    def test_import_data_fail_file_not_found(self) -> None:
        runner = CliRunner()
        result = runner.invoke(skillcorner_line_cleaner, ["toto"])
        assert result.exit_code == 1
        assert "File not found" in result.output

    def test_import_data_fail_wrong_json_format(self) -> None:
        runner = CliRunner()
        result = runner.invoke(skillcorner_line_cleaner, ["tests/data/bad.log"])
        assert result.exit_code == 0
        assert "Line 0: Error " in result.output
