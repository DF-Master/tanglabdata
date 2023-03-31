import requests, json
import streamlit as st
import settings as set


def search_by_id(
    id,
    host=set.host_url + "data/",
):
    response = requests.get(host + id)
    if response.status_code == 200:
        content_type = response.headers.get('Content-Type')
        if 'charset' in content_type.lower():
            encoding = content_type.split('charset=')[-1]
            data = response.content.decode(encoding)
            # 对data进行处理
        else:
            data = response.content.decode()
            # 对data进行处理
        data_list = json.loads(data)
        return data_list["results"]
    else:
        print('Error:', response.status_code)
        return None


if __name__ == '__main__':
    st.title("Tanglab-Digital-Decoder-WebUI")
    st.caption('made by [Yida](https://github.com/DF-Master) --230330 update!',
               unsafe_allow_html=True)

    with st.container():
        status = st.radio('Choose Status: ',
                          ('Run Out', 'Never Used', 'Available', 'Occupied'),
                          key="status")
        url_dic = {
            'Run Out': 'update-runout/',
            'Never Used': 'update-neverused/',
            'Available': 'update-available/',
            'Occupied': 'update-occupied/'
        }

        def on_input():
            id_value = st.session_state.id
            if len(id_value) >= 6:
                try:
                    results_list = search_by_id(id_value)
                    st.write(results_list)
                    uuid = results_list[0]["id"]
                    st.session_state.id = ""
                    response = requests.get(set.host_url + url_dic[status] +
                                            uuid)
                except:
                    st.write("Search ID Failed")

        id = st.text_input('ID(>= 6 num)',
                           value='',
                           key="id",
                           on_change=on_input)
