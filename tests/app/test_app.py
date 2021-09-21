from unittest import mock
import project.app


@mock.patch(project.app)
def test_app_is_called(mock_app):
    assert mock_app.called

