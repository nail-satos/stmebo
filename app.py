# from cProfile import label
# from itertools import chain
# from pydoc import describe
# import numpy as np
# import pandas as pd 
import streamlit as st
# import matplotlib.pyplot as plt 
# import japanize_matplotlib
# import seaborn as sns 
import requests
import json

# meboAPIにユーザーが入力した文字列をpost
def post_mebo(message):
    url = "https://api-mebo.dev/api"
    headers = {
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
    }
    payload = {
        "api_key": "c0dbf4fb-daa8-4f39-b46d-67eb830aa66c1839d878c4219f",
        "agent_id": "199a5291-0406-49bf-bf73-e1755835153d1839ceb44d6357",
        "utterance": message,
        }
    r = requests.post(url,headers=headers,json=payload)
    content = r.text
    content = json.loads(content)
    best_responce = content['bestResponse']
    print(best_responce['utterance'])
    return best_responce['utterance']
if 'list' not in st.session_state:
    st.session_state.list = []

# タイトル
st.title('AIチャット')

# メッセージを入力するテキストエリア
you_message= st.text_area(label='メッセージの入力')

# ボタンを押したら、post_mebo関数が呼び出される
if st.button('送信'):
    ai_message = post_mebo(message=you_message)
    st.session_state.list.append(you_message)
    st.session_state.list.append(ai_message)

# AIとの会話ログ
for num in range(len(st.session_state.list)):
    if 0 == num % 2:
        st.write('あなた:' + st.session_state.list[num])
    else:
        st.write('AI:' + st.session_state.list[num])
