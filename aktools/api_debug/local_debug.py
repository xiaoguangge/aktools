# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Date: 2021/12/9 19:09
Desc: HTTP 测试
"""
import requests
import pandas as pd


url = "http://127.0.0.1:8080/api/stock_financial_hk_analysis_indicator_em"
params = {
    "stock": "00700",
    "indicator": "年度"
}
r = requests.get(url, params=params)
temp_df = pd.DataFrame.from_dict(r.json())
print(temp_df)
