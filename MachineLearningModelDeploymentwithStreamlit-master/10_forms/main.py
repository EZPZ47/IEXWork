import streamlit as st

with st.form("form_key"):
    st.write('What would you like to order?')
    appetizers = st.selectbox('Appetizers',options=['choice1','choice2','choice3'])
    main = st.selectbox('Main Course',options=['choice1','choice2','choice3'])
    desert = st.selectbox('Dessert',options = ['choice1','choice2','choice3'])
    wine = st.checkbox('Are you bringing wine?')
    date =  st.date_input('When are you coming?')
    time=st.time_input('What time are you coming?')
    allergy=st.text_area('Any allergies?',placeholder='Leave us a note for allergies')
    st.form_submit_button()

st.write(f"""Your Order Summary:
     Appetizer:{appetizers}

        Main Course:{main}

        Dessert:{desert}

        Are you bringing your own wine:{'yes' if wine else 'no'}

        Date of Visit:{date}

        Time of Visit{time}

        Allergies:{allergy}""")