import streamlit as st

st.markdown(':purple[Before giving the formula, please look into the symbols which are supported by Streamlit]')
st.markdown(":purple[Check out this [link](https://katex.org/docs/support_table.html)]")

# User input for the formula
user_input = st.text_input(':purple[Enter your formula here]')

# Button to display the formula
if st.button('Click here to display the formula'):
    # Render the LaTeX equation using markdown
    st.markdown(':blue[Mathematical notation of your formula:]')
    st.markdown(f'${user_input}$')

