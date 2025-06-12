import streamlit as st
import pandas as pd
import numpy as np

st.title('간단한 Streamlit 앱')

# 슬라이더 위젯
x = st.slider('x 값을 선택하세요', 0.0, 10.0, 5.0)
st.write('선택된 x 값:', x)

# 데이터프레임 표시
df = pd.DataFrame({
    '컬럼 A': np.random.randn(10),
    '컬럼 B': np.random.randn(10)
})
st.dataframe(df)

# 차트 그리기
st.line_chart(df)