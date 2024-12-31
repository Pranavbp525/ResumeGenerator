import subprocess
import os
import sys
import yaml
from typing import List
from jinja2 import Template
from src.responses import EducationResponse, SkillsResponse, HeadingData, ProjectsResponse, ExperienceResponse

import subprocess
import os

import subprocess
import os

def convert_tex_to_pdf(input_path, output_path):
    """
    Convert a LaTeX source file to a PDF.

    Parameters:
    input_path (str): The path to the LaTeX source file.
    output_path (str): The path where the output PDF should be saved.
    """
    try:
        

        # Run pdflatex to convert the .tex file to .pdf
        subprocess.run(["latexmk", "-pdf", input_path], check=True)
        subprocess.run(["latexmk", "-c"])
        subprocess.run(["mv", "resume.pdf", output_path+"/resume.pdf"])
        subprocess.run(["rm", "resume.aux", "resume.fdb_latexmk", "resume.fls", "resume.log", "resume.out", output_path+"/custom-commands.aux"], check=True)
        print(f"PDF successfully generated at {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating the PDF: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def write_experience_to_latex(experience_response: ExperienceResponse, file_path: str = "experience.tex"):
    """
    Writes the experience data to a LaTeX file.

    Parameters:
    experience_response (ExperienceResponse): The response object containing experience data.
    file_path (str): The path to the LaTeX file to write.
    """
    experiences = experience_response.experiences

    # LaTeX template for experience
    latex_template = r"""
\section{Experience}
\resumeSubHeadingListStart
{% for exp in experiences %}
\resumeSubheading
    { {{ exp.company }} }{ {{ exp.duration }} }
    { {{ exp.role }} | \emph{ {% for tool in exp.tools %}{{ tool }}{% if not loop.last %}, {% endif %}{% endfor %} } }{ {{ exp.location }} }
    \resumeItemListStart
    {% for responsibility in exp.responsibilities %}
        \resumeItem{ {{ responsibility }} }
    {% endfor %}
    \resumeItemListEnd
{% endfor %}
\resumeSubHeadingListEnd
"""
    # Render the template using Jinja2
    template = Template(latex_template)
    rendered_content = template.render(experiences=experiences)

    # Write the rendered LaTeX content to the file
    with open(file_path, "w") as file:
        file.write(rendered_content)

    print(f"Experience section successfully written to {file_path}")

def write_projects_to_latex(projects_response: ProjectsResponse, file_path: str = "projects.tex"):
    """
    Writes the project data to a LaTeX file.

    Parameters:
    projects_response (ProjectsResponse): The response object containing project data.
    file_path (str): The path to the LaTeX file to write.
    """
    projects = projects_response.projects

    # LaTeX template for projects
    latex_template = r"""
\section{Projects}
\resumeSubHeadingListStart
{% for project in projects %}
\resumeProjectHeading
    {\textbf{ {{ project.title }} } $|$ \emph{ {% for skill in project.skills %}{{ skill }}{% if not loop.last %}, {% endif %}{% endfor %} }}    {}
\resumeItemListStart
    {% for description in project.descriptions %}
        \resumeItem{ {{ description }} }
    {% endfor %}
\resumeItemListEnd
{% endfor %}
\resumeSubHeadingListEnd
"""
    # Render the template using Jinja2
    template = Template(latex_template)
    rendered_content = template.render(projects=projects)

    # Write the rendered LaTeX content to the file
    with open(file_path, "w") as file:
        file.write(rendered_content)

    print(f"Projects section successfully written to {file_path}")


def write_skills_to_latex(skills_data: SkillsResponse, file_path: str = "skills.tex"):
    """
    Writes the skills data to a LaTeX file.

    Parameters:
    skills_data (SkillsResponse): The skills data to write.
    file_path (str): The path to the LaTeX file to write.
    """
    # LaTeX template for skills
    latex_template = r"""
%-----------PROGRAMMING SKILLS-----------%
\section{Technical Skills}
    \begin{itemize}[leftmargin=0.15in, label={}]
    \small{
    \item{
    {% for skill in skills %}
        \textbf{ {{ skill.category }} }:{: {{ skill.items|join(', ') }} } \\
    {% endfor %}
    }}
    \end{itemize}
"""

    # Render the template using Jinja2
    template = Template(latex_template)
    rendered_content = template.render(skills=skills_data.skills)

    # Write the rendered LaTeX content to the file
    with open(file_path, "w") as file:
        file.write(rendered_content)

    print(f"Skills section successfully written to {file_path}")



def write_education_to_latex(education_data: EducationResponse, file_path: str = "education.tex"):
    """
    Writes the education data to a LaTeX file.

    Parameters:
    education_data (EducationResponse): The education data to write.
    file_path (str): The path to the LaTeX file to write.
    """
    # LaTeX template for education
    latex_template = r"""
%-----------EDUCATION-----------%
\section{Education}
\resumeSubHeadingListStart
{% for edu in education %}
\resumeSubheading
    { {{ edu.university }} }{ {{ edu.duration }} }
    { {{ edu.degree }} {% if edu.gpa %}(GPA: {{ edu.gpa }}){% endif %} }{ {{ edu.location }} }
    {% if edu.relevant_coursework %}
    \resumeItemListStart
        \resumeItem{\textbf{Relevant Coursework:} {{ edu.relevant_coursework|join(', ') }} }
    \resumeItemListEnd
    {% endif %}
{% endfor %}
\resumeSubHeadingListEnd
"""

    # Render the template using Jinja2
    template = Template(latex_template)
    rendered_content = template.render(education=education_data.education)

    # Write the rendered LaTeX content to the file
    with open(file_path, "w") as file:
        file.write(rendered_content)

    print(f"Education section successfully written to {file_path}")


def write_heading_to_latex(heading_data: HeadingData, file_path: str = "heading.tex"):
    """
    Writes the heading data to a LaTeX file.

    Parameters:
    heading_data (HeadingData): The heading data to write.
    file_path (str): The path to the LaTeX file to write.
    """
    # LaTeX template for heading
    latex_template = r"""
%----------HEADING----------%
\begin{center}
    \textbf{\Large \scshape {{ heading_data.name }} } \\ \vspace{1pt}

    \href{tel:{{ heading_data.phone }}}{\seticon{faPhone}
    \underline{ {{ heading_data.phone }} }} \quad
    \href{mailto:{{ heading_data.email }}}{\seticon{faEnvelope} \underline{ {{ heading_data.email }} }} \quad
    \href{https://www.linkedin.com/in/{{ heading_data.linkedin }}}{\seticon{faLinkedin} \underline{in/{{ heading_data.linkedin }}}} \quad
    \href{https://github.com/{{ heading_data.github }}}{\seticon{faGithub} \underline{ {{ heading_data.github }} }}

\end{center}
    """

    # Render the template using Jinja2
    template = Template(latex_template)
    rendered_content = template.render(heading_data=heading_data)

    # Write the rendered LaTeX content to the file
    with open(file_path, "w") as file:
        file.write(rendered_content)

    print(f"Heading section successfully written to {file_path}")



def load_resume_data(yaml_file_path="resume.yaml"):
    """Loads and parses the resume.yaml file."""
    with open(yaml_file_path, "r") as f:
        try:
            resume_data = yaml.safe_load(f)
            return resume_data
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            return None

def extract_heading_section(resume_data):
    """Extracts the heading section from resume data."""
    personal_info = resume_data.get("personal_information", {})
    heading_data = {
        "name": f"{personal_info.get('name', '')} {personal_info.get('surname', '')}",
        "phone": f"{personal_info.get('phone_prefix', '')}{personal_info.get('phone', '')}",
        "email": personal_info.get("email", ""),
        "linkedin": personal_info.get("linkedin", "").split("/")[-1],
        "github": personal_info.get("github", "").split("/")[-1],
    }
    return heading_data

def extract_education_section(resume_data):
    """Extracts the education section from resume data."""
    education_list = resume_data.get("education_details", [])
    education_data = []
    for edu in education_list:
        education_data.append({
            "university": edu.get("university", ""),
            "duration": edu.get("graduation_year", ""),
            "degree": f"{edu.get('degree', '')}s in {edu.get('field_of_study', '')}",
            "location": "",  # You don't have location in your education details
            "gpa": edu.get("gpa", ""),
            "relevant_coursework": edu.get("courses", [])
        })
    return education_data

def extract_experience_section(resume_data):
    """Extracts the experience section from resume data."""
    experience_list = resume_data.get("experience_details", [])
    experience_data = []
    for exp in experience_list:
        experience_data.append({
            "company": exp.get("company", ""),
            "duration": exp.get("employment_period", ""),
            "role": exp.get("position", ""),
            "location": exp.get("location", ""),
            "tools": exp.get("skills_acquired", []),
            "responsibilities": exp.get("key_responsibilities", [])
        })
    return experience_data

def extract_projects_section(resume_data):
    """Extracts the projects section from resume data."""
    project_list = resume_data.get("projects", [])
    project_data = []
    for proj in project_list:
        project_data.append({
            "title": proj.get("name", ""),
            "skills": [],  # You don't have specific skills listed per project, you could extract from description
            "descriptions": [proj.get("description", "")] # Assuming description is a single string, adjust if it's a list
        })
    return project_data

def extract_skills_section(resume_data):
    """Extracts the skills section from resume data."""
    skills_data = resume_data.get("skills", {})
    formatted_skills = []
    for category, skills in skills_data.items():
        formatted_skills.append({
            "category": category.replace("_", " ").title(),
            "items": skills
        })
    return formatted_skills



def write_resume_dot_tex(path):
    """
    Writes the main LaTeX resume file with dynamically generated paths for included files.

    Parameters:
    path (str): The base directory where the LaTeX file and its included files are stored.
    """
    # Define the content of the LaTeX file with dynamic paths
    latex_content = rf"""
\documentclass[letterpaper,10pt]{{article}}

\usepackage{{fontawesome5}}
\usepackage{{latexsym}}
\usepackage[empty]{{fullpage}}
\usepackage{{titlesec}}
\usepackage{{marvosym}}
\usepackage[usenames,dvipsnames]{{color}}
\usepackage{{verbatim}}
\usepackage{{enumitem}}
\usepackage[hidelinks]{{hyperref}}
\usepackage{{fancyhdr}}
\usepackage[english]{{babel}}
\usepackage{{tabularx}}
\input{{glyphtounicode}}

% Custom font
\usepackage[default]{{lato}}

\pagestyle{{fancy}}
\fancyhf{{}} % clear all header and footer fields
\fancyfoot{{}}
\renewcommand{{\headrulewidth}}{{0pt}}
\renewcommand{{\footrulewidth}}{{0pt}}

% Adjust margins
\addtolength{{\oddsidemargin}}{{-0.5in}}
\addtolength{{\evensidemargin}}{{-0.7in}}
\addtolength{{\textwidth}}{{1in}}
\addtolength{{\topmargin}}{{-0.5in}}
\addtolength{{\textheight}}{{1.0in}}

\urlstyle{{same}}

\raggedbottom
\raggedright
\setlength{{\tabcolsep}}{{0in}}

% Sections formatting
\titleformat{{\section}}{{
\vspace{{-4pt}}\scshape\raggedright\large
}}{{}}{{0em}}{{}}[\color{{black}}\titlerule\vspace{{-5pt}}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------%
% Custom commands
\begin{{document}}
\include{{{path}/custom-commands}}

%-------------------------------------------%
%%%%%%  RESUME STARTS HERE  %%%%%

%----------HEADING----------%
\input{{{path}/src/heading}}

%-----------EDUCATION-----------%
\input{{{path}/src/education.tex}}

%-----------SKILLS-----------%
\input{{{path}/src/skills.tex}}

%-----------EXPERIENCE-----------%
\input{{{path}/src/experience}}

%-----------PROJECTS-----------%
\input{{{path}/src/projects}}

%-------------------------------------------%
\end{{document}}
"""

    # Specify the file path
    file_path = f"{path}/resume.tex"

    # Write the content to the file
    try:
        with open(file_path, "w") as file:
            file.write(latex_content)
        print(f"LaTeX file successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_custom_commands_dot_tex(path):
    # Define the content of the custom-commands.tex file
    custom_commands_content = r"""
    %-------------------------%
    % Custom commands
    \newcommand{\resumeItem}[1]{
    \item\small{
        {#1 \vspace{-2pt}}
    }
    }

    \newcommand{\resumeSubheading}[4]{
    \vspace{-2pt}\item
        \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1} & #2 \\
        \textit{\small#3} & \textit{\small #4} \\
        \end{tabular*}\vspace{-7pt}
    }

    \newcommand{\resumeSubSubheading}[2]{
        \item
        \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
        \textit{\small#1} & \textit{\small #2} \\
        \end{tabular*}\vspace{-7pt}
    }

    \newcommand{\resumeProjectHeading}[2]{
        \item
        \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
        \small#1 & #2 \\
        \end{tabular*}\vspace{-7pt}
    }

    \newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

    \renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

    \newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
    \newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
    \newcommand{\resumeItemListStart}{\begin{itemize}}
    \newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

    \definecolor{Black}{RGB}{0, 0, 0}
    \newcommand{\seticon}[1]{\textcolor{Black}{\csname #1\endcsname}}
    """

    # Specify the file path
    file_path = f"{path}/custom-commands.tex"

    # Write the content to the file
    try:
        with open(file_path, "w") as file:
            file.write(custom_commands_content)
        print(f"LaTeX file successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")



