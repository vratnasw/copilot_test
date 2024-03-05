import streamlit as st
from pathlib import Path

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

with open("mechanical.pdf",'rb') as pdf_file:
    mechanical_file =  pdf_file.read()
with open("structural.pdf",'rb') as pdf_file:
    structural_file =  pdf_file.read()
with open("plumbing.pdf",'rb') as pdf_file:
    plumbing_file =  pdf_file.read()
with open("zoning.pdf",'rb') as pdf_file:
    zoning_file =  pdf_file.read()
with open("parcel.pdf",'rb') as pdf_file:
    parcel_file =  pdf_file.read()
with open("electrical.pdf",'rb') as pdf_file:
    electrical_file =  pdf_file.read()
with open("complete.pdf",'rb') as pdf_file:
    complete_file =  pdf_file.read()


st.set_page_config(layout='wide')
col1_n,col2_n = st.columns(2)
with col1_n:
    st.image('igland.svg',width=125)

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    
    st.image("atlanta_logo.jpg",width=300)
    st.write(' ')
    st.title(":green[Let's get started]")

with col3:
    st.write(' ')
row1 = st.columns(3)
#row2 = st.columns(3)

buttons = ['Parcel Subdivision', 'Check Zoning Parameters', 'Analyze Plumbing','Analyze Electrical','Analyze Mechanical','Analyze Structural']
col11, col21, col31 = st.columns(3)
with col11:
    if st.button('Parcel Subdivision', key=1, use_container_width=True):
                st.markdown(' Zoning classification - [R5](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH7TMIREDIRE) ')
                st.markdown(' Structure Type - **Two Family Dwelling** ')
                st.markdown(' Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH7TMIREDIRE)')
                st.markdown(' Minimum frontage - 70 ft')
                st.markdown(' Lot frontage - 74 ft')
                st.markdown(' Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH7TMIREDIRE_S16-07.007MILORE)')
                st.markdown(' Minimum lot size- 9000 sqft')
                st.markdown(' Lot size - 9500 sqft')
                st.markdown(' Lot size - 9500 sqft')
                st.markdown(' Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH7TMIREDIRE_S16-07.008MIYARE)')
                st.download_button(label="Export Parcel Report",
                               data =  parcel_file,
                               file_name="parcel_report.pdf",
                               mime = 'application/octet-stream')
           
    
    if st.button('Analyze Electrical', key=2, use_container_width=True):
        test =  True
        if test: 
            st.markdown('''**Electrical System Compliance Check:** ''')
            st.markdown('''>1.**Electrical Service and Distribution:** ''')
            st.markdown('>> * Compliance with service size and capacity requirements for the building demands : [Compliant](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>> * Adequacy of electrical panel location and access:[Adequate](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>>* Pass/Fail:  [Pass/Fail](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>2.**Branch Circuits, Feeders, and Conductors**')
            st.markdown('>>* Compliance with requirements for branch circuits, feeders, and conductor sizing and protection : [**Compliant**](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* Use of appropriate conductor materials and types: [Used](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>3.**Grounding and Bonding**')
            st.markdown('>>* Adequacy of grounding and bonding of electrical systems and equipment:  [Adequate](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>>* Compliance with NEC grounding requirements: [Compliant](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>4.**Lighting Design and Controls**')
            st.markdown('>>* Compliance with IBC/IECC lighting efficiency and control requirements: [Compliant](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>>* Provision of emergency and egress lighting as required: [Not Provided](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>5.**Overcurrent Protection**')
            st.markdown('>>* Proper sizing and installation of overcurrent protection devices: [Properly Sized](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* Coordination with electrical design and loads: [Coordinated](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)   ')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>6.**Electrical Outlets and Receptacles**')
            st.markdown('>>* Adequacy and accessibility of outlets in accordance with IBC/ADA: [Adequate](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* Compliance with spacing and placement requirements: [Compliant](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)   ')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>7.**Electrical Safety Measures**')
            st.markdown('>>* Installation of GFCI protection where required: [Installed](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* Arc-fault circuit interrupter (AFCI) protection in residential dwellings: [Provided](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>8.**Renewable Energy Systems (If Applicable)**')
            st.markdown('>>* Integration of renewable energy systems (solar, wind, etc.) within electrical design:[Integrated](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>>* Compliance with IBC and NEC for renewable energy installations: [Compliant](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>9.**Emergency and Standby Power Systems**')
            st.markdown('>>* Provision and design of emergency and standby power systems as required: [Provided](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* Compliance with IBC/NEC for emergency systems: [Compliant](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>10.**Testing and Verification**')
            st.markdown('>>* Performance of required electrical system testing: [Performed](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')
            st.markdown('>>* Documentation and verification of testing results: [Documented](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical)')

            st.markdown(' **Summary**:')
            st.markdown('>>* **Overall Electrical Compliance**: [Pass](https://codes.iccsafe.org/content/IBC2018P6/chapter-27-electrical) ')
            st.markdown('>>* **Details/Comments** : Provision of emergency and egress lighting as required. ')
            st.download_button(label="Export Electrical Report",
                               data =  electrical_file,
                               file_name="electrical_report.pdf",
                               mime = 'application/octet-stream')
           



with col21:
    if st.button('Check Zoning Parameters', key=3, use_container_width=True):
        test = 1
        if test: 
                st.markdown('Zoning classification - [**R4**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE)')
                st.markdown('Structure Type - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE)')
                st.markdown('Pass/Fail - **Pass** \n ')
                st.markdown('Accessory Structure Type - **N/A** ')
                st.markdown('Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE_S16-06.001SCPR) ')
                st.markdown('Minimum lot size- 9000 sqft')
                st.markdown(' Lot size - 9500 sqft ')
                st.markdown('Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE_S16-06.007MILORE) ')
                st.markdown('Minimum frontage - 70 ft  ')
                st.markdown('Lot frontage - 74 ft')
                st.markdown('Pass/Fail -[**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE_S16-06.007MILORE)')
                st.markdown('Min front setback - 35 ft')
                st.markdown(' Front Setback - 40ft')
                st.markdown('Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE_S16-06.007MILORE) ')
                st.markdown('Min rear setback allowed - 15ft')
                st.markdown(' Rear Setback - 25ft')
                st.markdown('Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE_S16-06.007MILORE)')
                st.markdown('Min side setback - 7ft')
                st.markdown('Side Setback - 6 ft')
                st.markdown('Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE_S16-06.007MILORE)')
                st.markdown('Maximum Height - 35 ft')
                st.markdown('Height - 25 ft')
                st.markdown('Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE_S16-06.009MAHE)')
                st.markdown('Minimum off street parking - 1')
                st.markdown('Off street parking - 2')
                st.markdown('Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE_S16-06.010MIOREPARE)')
                st.markdown('Maximum Floor to Area ratio - 40%')
                st.markdown('Floor to Area Ratio - 35%')
                st.markdown('Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE_S16-06.006TRUSSTRE)')
                st.markdown('Max Lot coverage - 35%')
                st.markdown('Lot Coverage - 30%')
                st.markdown('Pass/Fail - [**Pass**](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIIICOORANDECO_PT16ZO_CH6SIMIREDIRE_S16-06.007MILORE)')
                st.download_button(label="Export Zoning Report",
                               data =  zoning_file,
                               file_name="zoning_report.pdf",
                               mime = 'application/octet-stream')
           

    if st.button('Analyze Mechanical', key=4, use_container_width=True):
        test =  True
        mechanical_markdown = read_markdown_file("mechanical.md")
        if test: 
            st.markdown(mechanical_markdown, unsafe_allow_html=True) 
            st.download_button(label="Export Mechanical Report",
                               data =  mechanical_file,
                               file_name="mechanical_report.pdf",
                               mime = 'application/octet-stream')
    if st.button('Complete Report', use_container_width=True):
        test =  True
        if test: 
            st.markdown('**You can export the complete report below**')
            st.download_button(label="Export Complete Report",
                               data =  complete_file,
                               file_name="total_report.pdf",
                               mime = 'application/octet-stream')
           

with col31:
    if st.button('Analyze Plumbing', key=5, use_container_width=True):
        test =  True
        if test: 
            st.markdown('**Plumbing System Compliance Check:**')
            st.markdown('>1. **Water Supply System**')
            st.markdown('>>* Compliance with minimum pipe diameter: [3 in] vs. [2 in](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution) ')
            st.markdown('>>* Backflow prevention: [Required], Provided: [Yes](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution) ')
            st.markdown('>>* Pass/Fail: : [Pass](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution)')
            st.markdown('>2. **Drainage System**')
            st.markdown('>>* Compliance with minimum slope for horizontal drainage pipes:[0.25] vs. [0.2](https://codes.iccsafe.org/content/IPC2018P5/chapter-11-storm-drainage) ')
            st.markdown('>>* Proper venting of drainage systems: [Compliant](https://codes.iccsafe.org/content/IPC2018P5/chapter-11-storm-drainage)')
            st.markdown('>>* Pass/Fail:: [Pass](https://codes.iccsafe.org/content/IPC2018P5/chapter-11-storm-drainage)')
            st.markdown('>3. **Vent System**')
            st.markdown('>>* Vent pipe sizes and locations meet requirements: [32 mm] vs. [32 mm](https://codes.iccsafe.org/content/IPC2018P5/chapter-9-vents) ')
            st.markdown('>>* Venting for traps: [Properly Vented/Not Vented](https://codes.iccsafe.org/content/IPC2018P5/chapter-9-vents)')
            st.markdown('>>* Pass/Fail:: [Pass](https://codes.iccsafe.org/content/IPC2018P5/chapter-9-vents)')
            st.markdown('>4. **Traps and Interceptors**')
            st.markdown('>>* Presence and proper installation of traps at each fixture:  [Present](https://codes.iccsafe.org/content/IPC2018P5/chapter-10-traps-interceptors-and-separators)')
            st.markdown('>>* Grease interceptor requirements for applicable fixtures: [Compliant](https://codes.iccsafe.org/content/IPC2018P5/chapter-10-traps-interceptors-and-separators) ')
            st.markdown('>>* Pass/Fail:: [Pass](https://codes.iccsafe.org/content/IPC2018P5/chapter-10-traps-interceptors-and-separators)')
            st.markdown('>5. **Fixture Count and Types**')
            st.markdown('>>* Compliance with minimum required fixtures for the type of occupancy: [Required Number and Types] vs. [Provided Number and Types](https://codes.iccsafe.org/content/IPC2018P5/chapter-4-fixtures-faucets-and-fixture-fittings) ')
            st.markdown('>>* Accessibility of fixtures per ADA standards:[Compliant](https://codes.iccsafe.org/content/IPC2018P5/chapter-4-fixtures-faucets-and-fixture-fittings) ')
            st.markdown('>>* Pass/Fail:: [Pass](https://codes.iccsafe.org/content/IPC2018P5/chapter-4-fixtures-faucets-and-fixture-fittings)')
            st.markdown('>6. **Hot Water Supply**')
            st.markdown('>>* Adequacy of hot water supply in compliance with IBC: [Adequate](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution) ')
            st.markdown('>>* Temperature control mechanisms in place:  [Not Present](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution)')
            st.markdown('>>* Pass/Fail:: [Fail](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution)')
            st.markdown('>7. **Building Sewer System**')
            st.markdown('>>* Connection to public sewer or private disposal system: [Connected](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution#IPC2018P5_Ch06_Sec604) ')
            st.markdown('>>* Compliance with IBC for sewer size and slope: [Compliant](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution#IPC2018P5_Ch06_Sec604)')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution#IPC2018P5_Ch06_Sec604)')
            st.markdown('>8. **Water Heater Installation**')
            st.markdown('>>* Compliance with installation and venting requirements: [Compliant](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution#IPC2018P5_Ch06_Sec607) ')
            st.markdown('>>* Temperature and pressure relief valve installation:  [Installed](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution#IPC2018P5_Ch06_Sec607) ')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution#IPC2018P5_Ch06_Sec607)')
            st.markdown('>9. **Plumbing Materials and Joints**')
            st.markdown('>>* Use of approved materials for pipes and fittings:  [Approved](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution#IPC2018P5_Ch06_Sec605) ')
            st.markdown('>>* Compliance with joint standards (e.g., soldering, solvent cement): [Soldering](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution#IPC2018P5_Ch06_Sec605)')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IPC2018P5/chapter-6-water-supply-and-distribution#IPC2018P5_Ch06_Sec605)')
            st.markdown('>10. **Testing and System Integrity**')
            st.markdown('>>* Pressure test for water and drainage systems:  [Passed](https://codes.iccsafe.org/content/IPC2018P5/appendix-c-structural-safety) ')
            st.markdown('>>* Leakage or cross-connection issues: [Identified](https://codes.iccsafe.org/content/IPC2018P5/appendix-c-structural-safety)')
            st.markdown('>>* Pass/Fail: [Pass](https://codes.iccsafe.org/content/IPC2018P5/appendix-c-structural-safety)')
           
            
            st.markdown(' **Summary**:')
            st.markdown('>>* **Overall Plumbing Compliance**: **Pass**')
            st.markdown('>>* **Details/Comments** : Temperature control mechanisms should be in place. ')
            st.download_button(label="Export Plumbing Report",
                               data =  plumbing_file,
                               file_name="plumbing_report.pdf",
                               mime = 'application/octet-stream')
           
    if st.button('Analyze Structural', key=6, use_container_width=True):
        test =  True
        structural_markdown = read_markdown_file("structural.md")
        if test: 
            st.markdown(structural_markdown, unsafe_allow_html=True) 
            st.download_button(label="Export Structural Report",
                               data =  structural_file,
                               file_name="structural_report.pdf",
                               mime = 'application/octet-stream')
           



uploaded_file = True

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
prompt = st.chat_input("🧷 Enter address or parcel number")

if prompt:
        uploaded_file = st.file_uploader('🧷 Upload your plans', type="pdf", accept_multiple_files=True)
       # Display user message in chat message container
        #st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        #st.session_state.messages.append({"role": "user", "content": prompt})

      

col_submit,col_sp =  st.columns([2,0.5])
with col_submit:
    submit = st.button('💡')  

if submit:
        text = st.text_area('Enter Notes:', height=100) 
        st.download_button(label="Download data as a text", data=text, file_name='output.txt', mime = 'txt') 

        #with st.spinner(text="This may take a moment..."):

   