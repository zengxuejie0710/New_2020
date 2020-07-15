import pytest


@pytest.fixture(scope="module")
def param_a(request):
    print("参数a:",request.param[0])
    return request.param[0]
@pytest.fixture(scope="module")
def param_b(request):
    print('参数b:',request.param[1])
    return request.param[1]


@pytest.fixture()
def login(request):
    print(request.param)
    if request.param[0] == "username":
        return True
    else:
        return False

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
