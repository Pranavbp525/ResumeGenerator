def generate_system_prompt():
    """Generates a system prompt for the LLM."""
    return """
    You are a helpful assistant designed to help users tailor their resumes to specific job descriptions. 
    You will be provided with a job description and a section of the user's resume data.
    Your task is to select the most relevant information from the user's resume data that matches the job description and output it in a structured JSON format.
    Follow the instructions carefully and adhere to the specified JSON format for each section.
    Ensure that your responses are accurate, concise, and directly relevant to the job description provided.
    """

def experience_prompt(job_description, user_experience, num_experiences=2):
    """Generates a prompt for the experience section."""
    
    schema_instruction = """
    {
        "company": "Name of the company",
        "duration": "Employment period",
        "role": "Your role at the company",
        "location": "Location of the company",
        "tools": ["List of tools used. Include atmost 5 tools."],
        "responsibilities": ["List of responsibilities"]
    }
    """
    
    prompt = f"""
    Job Description:
    {job_description}

    My work experience:
    {user_experience}

    Please select up to {num_experiences} work experiences from my resume that are most relevant to the job description.
    Output the selected experiences in JSON format adhering to the following schema:
    
    {schema_instruction}
    
    Ensure the output is a valid JSON array with each element representing an experience adhering to the specified schema.
    """
    return prompt

def projects_prompt(job_description, user_projects, num_projects=2):
    """Generates a prompt for the projects section."""
    
    schema_instruction = """
    {
        "title": "Project title",
        "skills": ["List of skills used in the project. Include atmost 5 skills."],
        "descriptions": ["Description of the project"]
    }
    """
    
    prompt = f"""
    Job Description:
    {job_description}

    My projects:
    {user_projects}

    Please select up to {num_projects} projects from my resume that are most relevant to the job description.
    Output the selected projects in JSON format adhering to the following schema:

    {schema_instruction}

    Ensure the output is a valid JSON array with each element representing a project adhering to the specified schema.
    """
    return prompt

def skills_prompt(job_description, user_skills):
    """Generates a prompt for the skills section."""
    
    schema_instruction = """
    {
        "category": "Skill category",
        "items": ["List of skills in this category. Include atleast 5 skills for each category."]
    }
    """
    
    prompt = f"""
    Job Description:
    {job_description}

    My skills:
    {user_skills}

    Please select the most relevant skills from each category in my resume that match the job description.
    Output the selected skills in JSON format adhering to the following schema:

    {schema_instruction}

    Ensure the output is a valid JSON array with each element representing a skill category adhering to the specified schema.
    """
    return prompt

def education_prompt(job_description, user_education):
    """Generates a prompt for the education section."""
    
    schema_instruction = """
    {
        "university": "Name of the university",
        "duration": "Years attended",
        "degree": "Degree earned",
        "location": "Location of the university",
        "gpa": "Grade point average",
        "relevant_coursework": ["List of relevant courses upto to 8"]
    }
    """
    
    prompt = f"""
    Job Description:
    {job_description}

    My education:
    {user_education}

    Please select up to 8 relevant courses for each of my education from my education history that match the job description.
    Output my education details in JSON format adhering to the following schema:

    {schema_instruction}

    Ensure the output is a valid JSON array with each element representing an education entry adhering to the specified schema.
    """
    return prompt