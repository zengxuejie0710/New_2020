#encoding utf-8


import pytest
import yaml


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')


@pytest.fixture(scope="module")
def param_a(request):
    print("参数a:",request.param[0])
    return request.param[0]

@pytest.fixture(scope="module")
def param_b(request):
    print('参数b:',request.param[1])
    return request.param[1]




def pytest_addoption(parser):
    mygroup = parser.getgroup("zengxuejie")     #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",    #注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv= request.config.getoption("--env",default='test')

    if myenv == 'test':
        datapath = 'datas/test/data.yml'
    if myenv == 'dev':
        datapath = 'datas/dev/data.yml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv,datas



def pytest_generate_tests(metafunc: "Metafunc") -> None:
    """ generate (multiple) parametrized calls to a test function."""
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.datas,
                             ids=metafunc.module.ids,
                             scope='function'
                             )