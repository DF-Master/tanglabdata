import settings as set
import Serialcontrol as sc
import requests, json
import streamlit as st


def search_by_id(
    id,
    host=set.host_url,
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


def print_id(com, id12, name, date, manager, location, note, bps=115200):
    printer = sc.Communication(
        com=com,
        bps=bps,
    )
    oneDID12 = id12.encode("utf-8")
    printer.Send_data(set.defaultStartCode + set.defaultOneDCode + oneDID12 +
                      set.end_code + set.printWord("ID: " + id12, y=96) +
                      set.printWord("Name: " + name, y=126) +
                      set.printWord("date: " + date, y=156) +
                      set.printWord("Manager: " + manager, y=186) +
                      set.printWord("Location: " + location, y=216) +
                      set.printWord("Note: " + note, y=246) +
                      set.defaultEndCode)


if __name__ == '__main__':
    # print(search_by_id("500"))

    st.title("Tanglab-Digital-Printer-WebUI")
    st.caption('made by [Yida](https://github.com/DF-Master) --230330 update!',
               unsafe_allow_html=True)

    with st.container():
        # 可以在这里写一些标题之类的东西
        st.header("ID Search & Printer")
        st.subheader("Search by ID")
        cola1, cola2 = st.columns(2)
        step_set = cola1.text_input('Short ID', value='45c47d')
        host_set = cola2.text_input('Host Set', value='')

        st.subheader("Print by ID12")

        colb1, colb2 = st.columns(2)
        com_set = colb1.text_input('COM Set',
                                   value='/dev/ttyACM0',
                                   key="com_set")
        uuid = colb2.text_input('UUID', "", key="uuid")

        colc1, colc2, colc3 = st.columns(3)
        id12 = colc1.text_input('ID12', "", key="id12")
        name = colc2.text_input('Name', "", key="name")
        date = colc3.text_input('Date', "", key="date")

        colc4, colc5, colc6 = st.columns(3)
        manager = colc4.text_input('Manager', "", key="manager")
        location = colc5.text_input('Location', "", key="location")
        note = colc6.text_input('Note', "", key="note")

        def search_botton():
            try:
                if host_set == '':
                    results_list = search_by_id(step_set)
                else:
                    results_list = search_by_id(step_set, host=host_set)
                st.session_state.uuid = results_list[0]["id"]
                st.session_state.id12 = results_list[0]["id"].split('-')[-1]
                st.session_state.name = results_list[0]["reagent"]
                st.session_state.date = results_list[0]["register_date"]
                st.session_state.manager = results_list[0]["principal"]
                st.session_state.location = results_list[0]["location"]
                st.session_state.note = str(results_list[0]["note"])
                st.write(results_list)
            except:
                st.write("Search Failed")

        def print_botton():
            try:
                print_id(st.session_state.com_set, st.session_state.id12,
                         st.session_state.name, st.session_state.date,
                         st.session_state.manager, st.session_state.location,
                         st.session_state.note)
            except:
                st.write("Print Failed")

        cold1, cold2 = st.columns(2)
        search_here = cold1.button('Search', on_click=search_botton)
        print_here = cold2.button('Print', on_click=print_botton)
# sudo usermod -a -G dialout $USER