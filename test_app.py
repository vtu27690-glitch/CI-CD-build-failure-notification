from app import check_build


def test_success_build():
    assert check_build("success") == "Build successful"
