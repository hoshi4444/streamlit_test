import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


"""
# 基本
## 文字列を表示 
"""
st.title('Streamlit 超入門')
st.write('DataFrame')

"""
## データフレーム(テーブル)を表示 
"""
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4,],
    '2列目': [1, 2, 3, 4,],
})
st.dataframe(df.style.highlight_max(axis=0))

"""
## markdownを反映できる

# 章
## 節
### 項 

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


"""
# 折れ線・塗り線・棒グラフ 
"""
rnd = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(rnd)
st.area_chart(rnd)
st.bar_chart(rnd)

"""
# 地図にマーカー表示 
"""
rnd2 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(rnd2)

# 画像を表示
# img = Image.open('sample.png')
# st.image(img, caption='ねこ ', use_column_width=True)

"""
# インタラクティブ
## チェック・セレクト・テキストボックス・スライダー 
"""
if st.checkbox('show message'):
    st.write('fuga')

option = st.selectbox(
    'chose num',
    list(range(1,11))
)
'your chose', option

text = st.text_input('what you are hobby?')
'your hobby:', text

condition = st.slider('how do you?, 0, 100, 150')
'your condition:',condition


"""
## サイドバー
"""
st.sidebar.write('Interactive Widgets')
text = st.sidebar.text_input('what you are hobby?')
condition = st.sidebar.slider('how do you?, 0, 100, 150')


"""
## 2カラムレイアウト 
"""
left_column, right_column = st.beta_columns(2)
button = left_column.button('put to right column')
if button:
    right_column.write('this right column')


"""
## expander
"""
expander = se.beta_expander('Q.1')
expander.write('A.1')
expander = se.beta_expander('Q.2')
expander.write('A.2')
expander = se.beta_expander('Q.3')
expander.write('A.3')

"""
## プログレスバー 
"""
st.write('put progres bar')
'Start'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!'
