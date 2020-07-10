import pytest


@pytest.fixture(scope="module")
def cal():
    print("开始计算")
    yield
    print("计算结束")


@pytest.fixture()
def login(request):
    print(request.param)
    if request.param[0] == "username":
        return True
    else:
        return False