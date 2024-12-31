import streamlit as st
import uuid
import os
import base64
import logging
from generate import generate_resume

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def display_pdf(pdf_path: str):
    """
    Display a PDF file in the Streamlit app.

    Parameters:
    pdf_path (str): The path to the PDF file.
    """
    # Verify that the PDF file exists
    if not os.path.exists(pdf_path):
        logging.error(f"PDF file not found at: {pdf_path}")
        st.error("The generated PDF file could not be found.")
        return

    # Display the PDF in the app using an iframe
    with open(pdf_path, "rb") as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    st.title("Resume Generator")
    st.write("Enter the job description below and click 'Generate Resume' to create your resume.")

    # Textbox for job description
    job_description = st.text_area("Job Description", placeholder="Enter the job description here...")

    # Initialize session state for resume generation
    if "pdf_path" not in st.session_state:
        st.session_state.pdf_path = None

    # Placeholder for PDF display
    pdf_placeholder = st.empty()

    # Generate Resume button
    if st.button("Generate Resume"):
        if not job_description.strip():
            st.error("Please enter a job description.")
        else:
            # Generate a unique UUID for the application ID
            application_id = str(uuid.uuid4())
            logging.info(f"Generated application ID: {application_id}")

            # Generate the resume
            with st.spinner("Generating your resume..."):
                st.session_state.pdf_path = generate_resume(job_description, application_id)
                logging.info(f"Resume generated and saved at: {st.session_state.pdf_path}")

            st.success("Resume generated successfully!")

    # Display the resume if it has been generated
    if st.session_state.pdf_path:
        logging.info(f"Attempting to display PDF from: {st.session_state.pdf_path}")
        # Verify that the PDF file exists
        if os.path.exists(st.session_state.pdf_path):
            logging.info("PDF file exists. Displaying...")
            st.write("### Your Resume")
            with open(st.session_state.pdf_path, "rb") as pdf_file:
                st.download_button(
                    label="Download Resume",
                    data=pdf_file,
                    file_name="resume.pdf",
                    mime="application/pdf"
                )

            # Display the PDF in the app using an iframe
            st.write("### Preview")
            pdf_placeholder.empty()  # Clear the previous PDF display
            display_pdf(st.session_state.pdf_path)
        else:
            logging.error(f"PDF file not found at: {st.session_state.pdf_path}")
            st.error("The generated PDF file could not be found.")

        # Regenerate Resume button
        if st.button("Regenerate Resume"):
            if not job_description.strip():
                st.error("Please enter a job description.")
            else:
                # Generate a new UUID for the application ID
                application_id = str(uuid.uuid4())
                logging.info(f"Regenerating resume with new application ID: {application_id}")

                # Regenerate the resume
                with st.spinner("Regenerating your resume..."):
                    st.session_state.pdf_path = generate_resume(job_description, application_id)
                    logging.info(f"Resume regenerated and saved at: {st.session_state.pdf_path}")

                st.success("Resume regenerated successfully!")

                # Update the PDF display
                if os.path.exists(st.session_state.pdf_path):
                    pdf_placeholder.empty()  # Clear the previous PDF display
                    display_pdf(st.session_state.pdf_path)

if __name__ == "__main__":
    main()