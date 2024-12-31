# Resume Generator

This is a resume generator that creates a resume based on a given job description.

## Installation and Setup

1. **Install or activate the environment using pipenv:**

    ```sh
    pipenv install
    pipenv shell
    ```

2. **Create a `.env` file:**

    In the root directory of the project, create a file named `.env` and add the following line to it:

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

    Replace `your_openai_api_key_here` with your actual OpenAI API key.

3. **Fill in the `assets/resume.yaml` details:**

    Open the `assets/resume.yaml` file and replace the example information with your own details.

4. **Run the app:**

    ```sh
    streamlit run app.py
    ```

## Usage

1. Open the Streamlit app in your browser.
2. Enter the job description in the provided field.
3. Click the "Generate Resume" button to create your resume.
