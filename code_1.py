import pandas as pd

def func_1():
    df1 = pd.read_excel('附件1.xlsx')
    df2 = pd.read_excel('附件2.xlsx')

    group_by = df2.groupby('单品编码')['销量(千克)'].agg('mean')
    # print(group_by)
    # group_by.to_excel('结果.xlsx')

    merge_res = pd.merge(df1, group_by, on='单品编码')
    # merge_res.to_excel('结果.xlsx')

    total_res = merge_res.pivot_table(index='单品名称',columns='分类名称', values='销量(千克)')
    print(total_res)

if __name__ == '__main__':
    func_1()