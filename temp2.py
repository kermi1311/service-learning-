import streamlit as st
from fpdf import FPDF

# Define the function to create a PDF
def create_pdf(fields):
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set background color for the entire page
    pdf.set_fill_color(224, 235, 255)  # A light blue color
    pdf.rect(0, 0, 210, 297, 'F')  # Fill the entire page

    # Set font for the title to bold
    pdf.set_font("Arial", 'B', 16)

    # Title and school details in bold with no borders and no background color
    title = "Vidhya Vikas Mandir Andgaon\nTA:Mulshi,District:Pune\nSchool Recognition No. : 5/48/(OH) Pune dt. 29.9.1961\nS.S.C. BOARD NO. 11.10.005\n\nSchool Leaving Certificate\n"
    pdf.multi_cell(0, 10, title, align='C', border=0)

    # Set font to bold for the field names
    pdf.set_font("Arial", 'B', 12)

    # Insert field names and data into PDF with borders
    for key, value in fields.items():
        # Write field name in bold with border
        field_name = f"{key}: "
        pdf.cell(pdf.get_string_width(field_name), 10, field_name, ln=0, border=1)
        # Change font to underline for user input
        pdf.set_font("Arial", 'U', 12)
        pdf.cell(0, 10, f"{value}", ln=1, border=1)
        # Revert font to bold for next field name
        pdf.set_font("Arial", 'B', 12)

    # Disclaimer, in bold and not underlined, with border
    pdf.cell(0, 10, "No changes can be made once submitted", ln=True, align='C', border=1)

    # Save the PDF to a variable
    pdf_output = pdf.output(dest='S').encode('latin1')
    return pdf_output

# Streamlit interface
st.title("School Leaving Certificate Generator")

# Initialize session state
if 'pdf' not in st.session_state:
    st.session_state.pdf = None
    st.session_state.generated = False

# Streamlit form
with st.form("input_form"):
    fields = {
        "Sr no": st.text_input("Sr no"),
        "General reg no": st.text_input("General reg no"),
        "Medium": st.text_input("Medium", value="Marathi"),
        "School no": st.text_input("School no"),
        "Board": st.text_input("Board", value="SSC Pune"),
        "Student id": st.text_input("Student id"),
        "Aadhar card no": st.text_input("Aadhar card no"),
        "Students Full Name": st.text_input("Students Full Name"),
        "Surname": st.text_input("Surname"),
        "Nationality": st.text_input("Nationality"),
        "Mother tongue": st.text_input("Mother tongue"),
        "Religion": st.text_input("Religion"),
        "Sub caste": st.text_input("Sub caste"),
        "Place of Birth": st.text_input("Place of Birth"),
        "Date of admission": st.date_input("Date of admission"),
        "Date of Leaving": st.date_input("Date of Leaving")
    }
    submitted = st.form_submit_button("Generate PDF")

    if submitted:
        st.session_state.pdf = create_pdf(fields)
        st.session_state.generated = True
        pdf_name = f"{fields['Students Full Name'].replace(' ', '_')}_LC.pdf" if fields['Students Full Name'] else "Unnamed_LC.pdf"
        st.session_state.pdf_name = pdf_name

# Place the download button outside the form
if st.session_state.generated:
    st.download_button(label="Download PDF",
                       data=st.session_state.pdf,
                       file_name=st.session_state.pdf_name,
                       mime='application/pdf')
