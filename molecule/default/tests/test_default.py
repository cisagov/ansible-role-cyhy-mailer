"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "directory", [{"path": "/var/cyhy/cyhy-mailer", "mode": "0o755"}]
)
def test_packages(host, directory):
    """Test that the appropriate directories were created."""
    assert host.file(directory["path"]).exists
    assert host.file(directory["path"]).is_directory
    assert oct(host.file(directory["path"]).mode) == directory["mode"]


@pytest.mark.parametrize(
    "path,mode",
    [
        ("/var/cyhy/cyhy-mailer/docker-compose.bod.yml", "0o644"),
        ("/var/cyhy/cyhy-mailer/docker-compose.cyhy-notification.yml", "0o644"),
        ("/var/cyhy/cyhy-mailer/docker-compose.cyhy.yml", "0o644"),
        ("/var/cyhy/cyhy-mailer/docker-compose.yml", "0o644"),
    ],
)
def test_files(host, path, mode):
    """Test that the appropriate files were created."""
    file = host.file(path)
    assert file.exists
    assert file.is_file
    assert oct(file.mode) == mode
