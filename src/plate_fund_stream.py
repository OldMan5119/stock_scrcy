import stock_data as sdata
import pandas as pd


def process_data():
    """
    大盘资金流向
    :return:
    """
    klines_data = sdata.get_stock_plate_list_fund_stream()
    # 定义列名
    columns = [
        "f1", "f2", "今日涨跌幅", "f12", "f13",
        "名称", "主力净流入额", "今日超大单净流入额", "今日超大单净流入占比", "今日大单净流入额",
        "今日大单净流入占比", "今日中单净流入额", "今日中单净流入占比", "今日小单净流入额",
        "今日小单净流入占比", "f124", "主力净流入占比", "f204", "f205", "f206"
    ]

    df = pd.DataFrame([[line['f1'], line['f2']] for line in klines_data], columns=['f1', 'f2', 'f3'])
    print(df)
    # 将每行数据拆分成列表并创建 DataFrame
    df = pd.DataFrame(klines_data, columns=columns)
    # 删除 col12 列
    df = df.drop(columns=['f1', 'f2', 'f12', 'f13', 'f124', 'f204', 'f205'])
    #
    # # 将 col14 列转换为百分比格式
    # df['主力净流入占比'] = df['主力净流入占比'].astype(float).map(lambda x: f'{x * 1:.2f}%')
    # df['中单净流入占比'] = df['中单净流入占比'].astype(float).map(lambda x: f'{x * 1:.2f}%')
    # df['大单净流入占比'] = df['大单净流入占比'].astype(float).map(lambda x: f'{x * 1:.2f}%')
    # df['超大单净流入占比'] = df['超大单净流入占比'].astype(float).map(lambda x: f'{x * 1:.2f}%')
    # df['上证-涨跌幅'] = df['上证-涨跌幅'].astype(float).map(lambda x: f'{x * 1:.2f}%')
    # df['深证-涨跌幅'] = df['深证-涨跌幅'].astype(float).map(lambda x: f'{x * 1:.2f}%')
    # #
    #
    # # 将 col1 列以亿为单位展示
    # df['主力流入净额'] = (df['主力流入净额'].astype(float) / 100000000).map(lambda x: f'{x:.1f}亿')
    # df['中单流入净额'] = (df['中单流入净额'].astype(float) / 100000000).map(lambda x: f'{x:.1f}亿')
    # df['大单流入净额'] = (df['大单流入净额'].astype(float) / 100000000).map(lambda x: f'{x:.1f}亿')
    # df['超大单流入净额'] = (df['超大单流入净额'].astype(float) / 100000000).map(lambda x: f'{x:.1f}亿')

    # # 重新排列列的顺序
    # new_columns_order = ["日期", "上证-收盘价", "上证-涨跌幅", "深证-收盘价", "深证-涨跌幅",
    #                      "主力流入净额", "主力净流入占比", "超大单流入净额", "超大单净流入占比",
    #                      "大单流入净额", "大单净流入占比", "中单流入净额", "中单净流入占比"
    #                      ]
    # df = df.reindex(columns=new_columns_order)
    # df.to_csv("../output/" + sdata.day + "/大盘资金流向历史数据(沪深两市)", index=False)


if __name__ == '__main__':
    process_data()
