import streamlit as st
import streamlit as st


st.set_page_config(layout='centered')

st.title(" City of Atlanta Copilot")
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("https://ourhousega.org/wp-content/uploads/2016/09/City-of-Atlanta-seal.png")

with col3:
    st.write(' ')

with st.chat_message("user"):
    st.write("Hello 👋, please upload your files to analyze")
    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
    if uploaded_file is not None:
        print('File successfully uploaded')
        st.write("Would you like to analyze the plans?")

    else:
        st.write("Please upload your files to analyze")
        
if uploaded_file is not None:
    st.write("You have the following options to analyze the file: \n 1) Check Zoning Parameters  \n 2) Analyze Electrical \n 3) Analyze Plumbing \n 4) Analyze Mechanical \n 5) Analyze Structural")
    animal_shelter = ['ZONING', 'ELECTRICAL', 'PLUMBING', 'MECHANICAL','STRUCTURAL', 'NONE']

    animal = st.text_input('Type an option (ZONING, ELECTRICAL, PLUMBING, MECHANICAL,STRUCTURAL, or NONE)')

    if st.button('Analyze'):
        have_it = animal in animal_shelter
        val =  animal
        if have_it and val == 'ZONING': 
            st.write('The plans have met the standards proposed by the City of Atlanta. \n')
            link = '[Source](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6BSIMIREDIRE)'
            st.markdown(link, unsafe_allow_html=True)
        if have_it and val == 'ELECTRICAL': 
            st.write('Not Available. \n')
            link = '[Source](https://codes.iccsafe.org/codes/georgia)'
            st.markdown(link, unsafe_allow_html=True)
        if have_it and val == 'MECHANICAL': 
            st.write('Not Available. \n')
            link = '[Source](https://codes.iccsafe.org/codes/georgia)'
            st.markdown(link, unsafe_allow_html=True)
        if have_it and val == 'PLUMBING': 
            st.write('Not Available. \n')
            link = '[Source](https://codes.iccsafe.org/codes/georgia)'
            st.markdown(link, unsafe_allow_html=True)
        if have_it and val == 'STRUCTURAL': 
            st.write('Not Available. \n')
            link = '[Source](https://codes.iccsafe.org/codes/georgia)'
            st.markdown(link, unsafe_allow_html=True)
        if  val == 'NONE': 
            st.write('Session Ended. \n')
           



        
        
        
        
        
        



