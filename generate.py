import logging
import os
import uuid
import json
from typing import Dict, Any
from src.llm import invoke_mini, invoke_omni
from src.prompts import (
    generate_system_prompt,
    experience_prompt,
    education_prompt,
    projects_prompt,
    skills_prompt
)
from src.responses import (
    ExperienceItem, ExperienceResponse,
    EducationResponse, EducationItem,
    SkillItem, SkillsResponse,
    HeadingData, ProjectItem, ProjectsResponse
)
from utils import (
    convert_tex_to_pdf,
    write_education_to_latex,
    write_experience_to_latex,
    write_heading_to_latex,
    write_projects_to_latex,
    write_skills_to_latex,
    write_resume_dot_tex,
    write_custom_commands_dot_tex,
    load_resume_data,
    extract_education_section,
    extract_experience_section,
    extract_heading_section,
    extract_projects_section,
    extract_skills_section
)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# Constants
RESUME_FILE_PATH = "assets/resume.yaml"
OUTPUT_BASE_PATH = "artifacts"

def load_and_extract_resume_data(file_path):
    """Load resume data and extract relevant sections."""
    resume_data = load_resume_data(file_path)
    return {
        'education': extract_education_section(resume_data),
        'experience': extract_experience_section(resume_data),
        'projects': extract_projects_section(resume_data),
        'skills': extract_skills_section(resume_data),
        'heading': extract_heading_section(resume_data)
    }

def invoke_llm_for_section(system_prompt, prompt_func, response_format, **kwargs):
    """Invoke the LLM for a specific section."""
    return invoke_omni(
        system_prompt=system_prompt,
        prompt=prompt_func(**kwargs),
        response_format=response_format
    )

def write_section_to_latex(write_func, data, file_path):
    """Write a section to a LaTeX file."""
    write_func(data, file_path)

def save_outputs_to_json(
    education_output: EducationResponse,
    experience_output: ExperienceResponse,
    projects_output: ProjectsResponse,
    skills_output: SkillsResponse,
    output_path: str
) -> None:
    """
    Save all LLM outputs to a JSON file.

    Parameters:
    education_output (EducationResponse): Output for the education section.
    experience_output (ExperienceResponse): Output for the experience section.
    projects_output (ProjectsResponse): Output for the projects section.
    skills_output (SkillsResponse): Output for the skills section.
    output_path (str): The path where the JSON file should be saved.
    """
    # Combine all outputs into a single dictionary
    combined_outputs: Dict[str, Any] = {
        "education": education_output.model_dump(),
        "experience": experience_output.model_dump(),
        "projects": projects_output.model_dump(),
        "skills": skills_output.model_dump(),
    }

    # Write the combined dictionary to a JSON file
    try:
        with open(output_path, "w") as json_file:
            json.dump(combined_outputs, json_file, indent=4)
        print(f"All outputs successfully saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while saving outputs to JSON: {e}")

def generate_resume(job_description, application_id):
    # Load and extract resume data
    job_description = job_description
    job_id = application_id
    logging.info(f"GENERATING RESUME for JOB_ID: {job_id}")
    resume_sections = load_and_extract_resume_data(RESUME_FILE_PATH)
    heading_output = HeadingData.model_validate(resume_sections['heading'])
    logging.info(f"HEADING SECTION: {heading_output}")
    # Get job description and ID from user
    
    
    # Prepare output paths
    output_path = f"{OUTPUT_BASE_PATH}/{job_id}/latex_src"
    src_path = f"{output_path}/src"

    logging.info(f"output_path: {output_path}")
    logging.info(f"src path: {src_path}")
    os.makedirs(src_path, exist_ok=True)
    logging.info(f"Directories created: {output_path}, {src_path}")
    # Invoke LLM for each section
    system_prompt = generate_system_prompt()
    education_output = invoke_llm_for_section(
        system_prompt, education_prompt, EducationResponse,
        job_description=job_description, user_education=resume_sections['education']
    )
    logging.info(f"EDUCATION: {education_output}")
    experience_output = invoke_llm_for_section(
        system_prompt, experience_prompt, ExperienceResponse,
        job_description=job_description, user_experience=resume_sections['experience'], num_experiences=2
    )
    logging.info(f"EXPERIENCE: {experience_output}")
    projects_output = invoke_llm_for_section(
        system_prompt, projects_prompt, ProjectsResponse,
        job_description=job_description, user_projects=resume_sections['projects'], num_projects=2
    )
    logging.info(f"PROJECTS: {projects_output}")
    skills_output = invoke_llm_for_section(
        system_prompt, skills_prompt, SkillsResponse,
        job_description=job_description, user_skills=resume_sections['skills']
    )
    logging.info(f"SKILLS: {skills_output}")

    json_path = f"{OUTPUT_BASE_PATH}/{job_id}/model_outputs.json"
    save_outputs_to_json(
        education_output, experience_output, projects_output, skills_output, json_path
    )

    
    # Write LaTeX files
    logging.info(f"WRITING resume.tex to path: {output_path}/resume.tex")
    write_resume_dot_tex(output_path)
    logging.info(f"WRITING custom-commands.tex to path: {output_path}/custom-commands.tex")
    write_custom_commands_dot_tex(output_path)
    write_section_to_latex(write_heading_to_latex, heading_output, f"{src_path}/heading.tex")
    write_section_to_latex(write_education_to_latex, education_output, f"{src_path}/education.tex")
    write_section_to_latex(write_skills_to_latex, skills_output, f"{src_path}/skills.tex")
    write_section_to_latex(write_experience_to_latex, experience_output, f"{src_path}/experience.tex")
    write_section_to_latex(write_projects_to_latex, projects_output, f"{src_path}/projects.tex")

    # Convert LaTeX to PDF
    convert_tex_to_pdf(input_path=f"{output_path}/resume.tex", output_path=f"{OUTPUT_BASE_PATH}/{job_id}")

    return f"artifacts/{job_id}/resume.pdf"
