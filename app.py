import streamlit as st

st.title('Power Calculator')
st.write('Enter a number to calculate its square, cube and fifth power')

n=st.number_input('enter the number',value=1,step=1)

square=n**2
cube=n**3
fifth=n**5

st.write(f'square of the number {n} is: ',square)
st.write(f'cube of the number {n} is: ',cube)
st.write(f'fifth power of the number {n} is: ',fifth)