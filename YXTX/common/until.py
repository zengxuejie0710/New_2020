# encoding utf-8
import yaml
class Util:
    """
    读取yaml文件
    """
    def data(self,path):
        with open(path, encoding="utf-8")as f:
            testdata = yaml.safe_load(f)
            return testdata