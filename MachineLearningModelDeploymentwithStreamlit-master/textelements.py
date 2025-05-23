import streamlit as st

st.title('Your title')

st.header('Main header')

st.subheader('This is a subheader')

st.markdown('This is markdown **text**')
st.markdown('# Header1')
st.markdown('## Header 2')
st.markdown('### Header 3')

st.caption('This is a caption')

st.code("""import pandas as pd
        pd.read_csv(my_csv_file)
        """)

st.text('Some Text')

#LaTeX
st.latex('x = 2^2')

st.text('Text above divider')
st.divider()
st.text('Text below divider')


#st.write
st.write('Some Text')