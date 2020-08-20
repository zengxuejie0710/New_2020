# Author xuejie zeng
# encoding utf-8
from selenium.webdriver.common.by import By

def handle_black(func):

    # def wrapper(*args, **kwargs):
    #     _black_list = [
    #         (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    #
    #     _max_err_num = 3
    #     _error_num = 0
    #
    #     try:
    #         # 如果元素找到，就清空 error 计数
    #         element = func(*args, **kwargs)
    #         _error_num = 0
    #         return element
    #
    #     except Exception as e:
    #         instance = args[0]
    #         instance.set_implicitly_wait(2)
    #         # 如果没找到，就进行黑名单处理
    #         if instance._error_num > instance._max_err_num:
    #             # 如果 erro 次数大于指定指，清空 error 次数并报异常
    #             instance._error_num = 0
    #             raise e
    #         instance._error_num += 1
    #         for ele in instance._black_list:
    #             # 对黑名单进行点击
    #             eles = instance.finds(ele)
    #             if len(eles) > 0:
    #                 eles[0].click()
    #                 return wrapper(*args, **kwargs)
    #         raise ValueError("元素不在黑名单中")
    #
    # return wrapper

    def wrapper(*args, **kwargs):
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
        ]
        _max_err_num = 3
        _error_num = 0
        try:
            #logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)
            #instance.set_implicitly_wait(3)
            return element
        except Exception as e:
            instance = args[0]
            # instance.screenshot("tmp.png")
            # with open("tmp.png", "rb") as f:
            #     content = f.read()
            # allure.attach(content, attachment_type=allure.attachment_type.PNG)
            # logging.error("element not found, handle black list")
            instance.set_implicitly_wait(1)
            # 如果没找到，就进行黑名单处理
            if instance._error_num > instance._max_err_num:
                # 如果 erro 次数大于指定指，清空 error 次数并报异常
                instance._error_num = 0
                raise e
            instance._error_num += 1
            for ele in instance._black_list:
                # 对黑名单进行点击
                eles = instance.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return wrapper(*args, **kwargs)
            raise ValueError("元素不在黑名单中")

    return wrapper




