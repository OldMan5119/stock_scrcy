from datetime import datetime
import subprocess
import execjs
from functools import partial  # 作用.用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

# day = datetime.now().date().strftime('%Y-%m-%d')
day = "2024-10-28"


def readJsFile(file_name):
    file_path = "../data/" + day + "/" + file_name
    text = open(file_path, mode="r", encoding="UTF-8").read()
    text = text[text.rfind("(") + 1:text.rfind(")")]
    return execjs.eval(text)


def get_stock_plate_list():
    """
        获取股票板块列表
    """
    js_data = readJsFile("板块对象1.js")
    # {'f12': 'BK1031', 'f13': 90, 'f14': '光伏设备', 'f62': 9347129856}
    stock_plate_list = js_data['data']['diff']
    return stock_plate_list


def get_stock_plate_list_fund_stream():
    """
        获取股票板块资金变动情况
    """
    stock_plate_list = []
    page1_js_data = readJsFile("板块对象1资金情况.js")
    page2_js_data = readJsFile("板块对象2资金情况.js")
    stock_plate_list += page1_js_data['data']['diff']
    stock_plate_list += page2_js_data['data']['diff']

    return stock_plate_list


def get_stock_bigbang_fund_stream():
    """
        获取股票大盘块资金变动情况
    """
    page1_js_data = readJsFile("大盘资金流向(沪深).js")
    return page1_js_data['data']['klines']


if __name__ == '__main__':
    plate_list = get_stock_bigbang_fund_stream()
    for i in range(len(plate_list)):
        print(plate_list[i])
