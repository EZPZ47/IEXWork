import streamlit as st
import pandas as pd
# Set page configuration
st.set_page_config(
    page_title='Homepage',
    page_icon='🏡',
    layout='centered',
    initial_sidebar_state='auto'
)



# Initialize a sample df and store it in the session state
df = pd.DataFrame({'col1':[1,2,3],'col2':[4,5,6]})

if 'df' not in st.session_state:
    st.session_state['df']=df
# Initialize state with the key "product" set to 0
if all(key not in st.session_state.keys() for key in ('product', 'x1', 'x2')):
    st.session_state['x1']=0
    st.session_state['x2'] = 0
    st.session_state['product'] = 0


# Define a function to multiply two numbers
def multiply(x1,x2):
    st.session_state['product'] = x1 + x2


if __name__ == "__main__":

    st.title("Homepage")

    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input("Pick a number", 0, 10, key="x1")
    with col2:
        x2 = st.number_input("Pick another number", 0, 10, key="x2")

    st.button("Multiply!", type="primary",on_click=multiply,args=(x1,x2))

st.write(st.session_state)
