import streamlit as st

'# 🔍: 일반 텍스트'
st.write('# 마크다운 H1 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('') # 빈 줄 추가

st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.write('') 

st.markdown('## 마크다운 : st.markdown()')
st.markdown(
    '''
    # 마크다운 헤더1
    - 마크다운 목록1. **굵게** 표시
    - 마크다운 목록. *기울임* 표시
        - 마크다운 목록2-1
        - 마크다운 목록 2-2
        
    ## 마크다운 헤더2
    - [네이버](https://naver.com)
    - [구글](https://google.com)
    
    ### 마크다운 헤더3
    일반 텍스트
    '''
)

st.divider() # 구분선

'# 🔍: 형식이 있는 텍스트'
st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')
st.write('') 

st.write('##### 코드 블록: st.code()')
st.code('print("Hello, World!")', language='python')
st.code('print("Hello, World!")', language='R')
st.code('print("Hello, World!")', language='python', line_numbers=True)

st.write('##### 코드 블록: Markdown')
st.write(
    '''
    ```python
    print("Hello, World!")
    ```
    '''
) 
st.write('') 


st.write('##### 코드+결과 : st.echo()')
with st.echo():
    # 이 블록의 코드와 결과를 출력
    name = 'Chunghun Ha'
    st.write("Hello, Streamlit!", name)
st.write('') 
    
st.write('##### Latex 수식 작성 : st.latex()')
st.latex('\int_a^b f(x)dx')

st.write('##### Latex 수식 작성 : Markdown')
st.write('$$\int_a^b f(x)dx$$')
st.divider()


'# 🔍: Streamlit Magic'
'''### Magic 적용
1. orderd item
    - 강조: **unordered item**
    - 기울임: *unordered item*
2. ordered item
3. ordered item
'''
st.divider()


'# 🔍: 색상이 있는 텍스트'
'''#### 텍스트 색상 변경
- :red[빨간색 텍스트]
- :blue[파란색 텍스트]
- :green[초록색 텍스트]
- :orange[주황색 텍스트]
- :gray[회색 텍스트]
'''
st.divider()


'# 🔍: 이미지, 오디오, 비디오'
'#### :orange[이미지: st.image()]'
st.image('./data/image.jpg', caption='바탕화면', width=500)

'#### :orange[오디오: st.audio()]'
st.audio('./data/바흐_첼로.mp3', format='audio/mpeg', loop=True)

'#### :orange[이미지: st.video()]'
video_file = open('./data/gizmo.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.divider()


'# 🔍: 콜아웃'
'#### :orange[정보: st.info()]'
st.info('This is a purely informational message', icon='ℹ️')

'#### :orange[경고: st.warning()]'
st.warning('This is a warning message', icon='⚠️')

'#### :orange[에러: st.error()]'
st.error('This is an error message', icon='🚫')

'#### :orange[성공: st.success()]'
st.success('This is success message', icon='✅')
st.divider()


'# 🔍: 데이터 테이블'
'#### :orange[Pandas 데이터프레임]'
import pandas as pd
df = pd.DataFrame(
    {'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [24, 34, 45]
    }
)

df

'#### :orange[지표(Metric)]'
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
st.divider()

'# :blue[Streamlit 그래프]'
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

'#### :orange[st.area_chart()]'
st.area_chart(chart_data)

'#### :orange[st.line_chart()]'
st.line_chart(chart_data)

'#### :orange[st.bar_chart()]'
st.bar_chart(chart_data)

'#### :orange[st.scatter_chart()]'
st.scatter_chart(chart_data)

'#### :orange[st.map()]'
df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
    columns=['lat', 'lon']
)

st.map(df)
st.divider()


'# :blue[시각화 라이브러리]'
'#### :orange[Matplotlib: st.pyplot()]'
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig) # 차트 출력

'#### :orange[Altair: st.altair_chart()]'
import altair as alt

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(
        x='a', y='b',
        size='c',
        color='c',
        tooltip=['a', 'b', 'c']
    )
)

st.altair_chart(c, use_container_width = True)

'#### :orange[Plotly: st.plotly_chart()]'
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length')

st.plotly_chart(fig, key='iris', on_select='rerun')