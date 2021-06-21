def test_ping(test_app_without_db):
    # Given
    # test_app

    # When
    response = test_app_without_db.get("/ping")

    # Then
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}
