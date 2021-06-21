from pathlib import Path

import pytest


def test_upload_file(test_app_with_db):
    print(path := Path(__file__).parent)
    with open(path / "data" / "test-5mb.bin", "rb") as f:
        files = {"file": f}
        response = test_app_with_db.post("/upload/file", files=files)
        assert response.status_code == 201
        response_dict = response.json()
        assert isinstance(response_dict, dict)
        assert isinstance(response_dict["id"], int)
        assert response_dict["filename"] == "test-5mb.bin"
        assert response_dict["created_at"]


@pytest.mark.skip
def test_multiple_files_upload(test_app_with_db):
    path = Path(__file__).parent
    headers = {"Content-Type": "multipart/form-data"}
    files = [
        ("file_list", ("test-10mb.bin", open(path / "data" / "test-10mb.bin", "rb"))),
        ("file_list", ("test-5mb.bin", open(path / "data" / "test-5mb.bin", "rb")))]
    response = test_app_with_db.post(
        "/upload/files", data=files, headers=headers
    )
    print(response.text)
    assert response.status_code == 201
    response_list = response.json()
    assert isinstance(response_list, list)
