import json

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

def job_description_analyzer_prompt(job_description: str):
    """Generates a prompt for analyzing job descriptions with HR expertise."""
    
    schema_instruction = """
    {
        "core_requirements": {
            "hard_skills": [{"skill": "Python", "variants": ["PyTorch", "Python 3"]}],
            "certifications": [],
            "tools": []
        },
        "scoring_rubric": {
            "primary_keywords": [],
            "secondary_keywords": [],
            "dealbreaker_terms": []  
        }
    }
    """
    
    prompt = f"""
    You are a veteran HR director with 20+ years experience at FAANG companies. Analyze this job description with surgical precision:

    Job Description:
    {job_description}

    Extract and analyze:
    1. Non-negotiable requirements (Must appear in resume)
    2. Priority order of technical skills (Top 10 only)
    3. Hidden cultural signals (Startup vs enterprise language)
    4. ATS keyword patterns (Including synonyms and acronyms)

    Output your analysis in JSON format adhering to the following schema:

    {schema_instruction}

    Guidelines:
    - For hard_skills: Include all variants and synonyms
    - For certifications: List exact names and common abbreviations
    - For tools: Include specific versions if mentioned
    - For keywords: Categorize by importance and match probability
    - For dealbreakers: Include absolute requirements and red flags

    Ensure the output is valid JSON adhering to the specified schema.
    """
    return prompt

def relevance_scorer_prompt(experience_data: list[dict], projects_data: list[dict], job_analysis: dict):
    """Generates a prompt for scoring resume relevance against job requirements."""
    prompt = f"""
    # ROLE: Senior ATS Compliance Analyst
    # TASK: Score resume components while preserving optimization potential

    ## INPUT DATA:
    {{
    "experience": {json.dumps(experience_data, indent=2)},
    "projects": {json.dumps(projects_data, indent=2)},
    "job_requirements": {json.dumps(job_analysis, indent=2)}
    }}

    ## SCORING MATRIX:
    1. **Core Requirements** (40% weight):
    - Direct keyword matches (Primary × 3, Secondary × 1)
    - Required certification/tool presence
    - Minimum experience duration met

    2. **Quality Indicators** (30% weight):
    - Metric density (Numbers/$ amounts per bullet)
    - Career progression (Title seniority growth)
    - Technical complexity (Tools/scale mentioned)

    3. **Potential Signals** (20% weight):
    - Adjacent skill proximity
    - Progressive responsibility
    - Conceptual project alignment

    4. **Risk Factors** (10% weight):
    - Employment gaps
    - Title/requirement mismatch
    - Over-qualification flags

    ## OUTPUT REQUIREMENTS:
    {{
    "scoring_breakdown": {{
        "experience": [
        {{
            "id": "exp1",
            "score": 92,
            "breakdown": {{
            "core": 36,
            "quality": 28,
            "potential": 18,
            "risk": 10
            }},
            "issues": {{
            "hard_requirements": ["Missing AWS certification"],
            "recommendations": ["Add EC2 deployment metrics"]
            }},
            "survival_status": "keep|borderline|reject"
        }}
        ],
        "projects": [
        {{
            "id": "proj1",
            "score": 85,
            "technical_depth": {{
            "tools": 20,
            "architecture": 15,
            "integration": 10
            }},
            "business_impact": {{
            "scale": 15,
            "metrics": 25
            }}
        }}
        ]
    }},
    "system_flags": {{
        "critical_issues": ["No Kubernetes experience"],
        "optimization_opportunities": ["Add Terraform keywords to Project X"],
        "borderline_cases": ["exp2: Partial Python match"]
    }}
    }}

    ## CRITICAL GUIDELINES:
    1. NEVER automatically reject items - only flag issues
    2. Score ALL entries regardless of dealbreakers
    3. Separate hard requirements vs fixable issues
    4. Identify salvage potential for low-scoring items
    5. Prioritize progressive experience over raw duration
    6. Flag implicit skills from project context
    7. Use ATS psychology: 7±2 keywords per section ideal

    ## EXAMPLE OUTPUT:
    For experience missing required certification but showing adjacent skills:
    {{
    "id": "exp3",
    "score": 68,
    "breakdown": {{
        "core": 25, 
        "quality": 20,
        "potential": 15,
        "risk": 8
    }},
    "issues": {{
        "hard_requirements": ["Missing CKA certification"],
        "recommendations": ["Emphasize Docker cluster experience"]
    }},
    "survival_status": "borderline"
    }}
    """

    return prompt


def content_optimizer_prompt(original_content: dict, job_analysis: dict, relevance_report: dict) -> str:
    """
    Generates optimization prompt with full contextual inputs and examples
    """
    
    # Extract key elements for example generation
    primary_keywords = job_analysis['scoring_rubric']['primary_keywords'][:3]
    missing_skills = relevance_report['system_flags']['critical_issues']
    borderline_case = next((item for item in relevance_report['scoring_breakdown']['experience'] 
                          if item['survival_status'] == 'borderline'), None)
    
    # Create dynamic examples based on actual inputs
    examples = {
        "ats_keyword_example": {
            "original": "Managed servers",
            "optimized": f"Automated {primary_keywords[0]} deployments using {job_analysis['core_requirements']['tools'][0]} (50% faster deployments)"
        },
        "star_example": {
            "situation": "High cloud costs",
            "action": f"Implemented {primary_keywords[1]} optimization",
            "result": "Saved $1.2M annually"
        },
        "padding_example": f"Exposure to {missing_skills[0]} through {borderline_case['recommendations'][0]}" 
                           if missing_skills and borderline_case else ""
    }

    prompt = f"""
    # ROLE: ATS Optimization Expert
    # INPUT DATA
    ## Job Requirements
    {json.dumps(job_analysis, indent=2)}

    ## Resume Analysis
    {json.dumps(relevance_report, indent=2)}

    ## Content to Optimize
    {json.dumps(original_content, indent=2)}

    # OPTIMIZATION RULES (+ EXAMPLES)
    1. **ATS Keyword Injection**
    Formula: [Action Verb] + [Number] + [JD Keyword] + [Business Impact]
    Example: "{examples['ats_keyword_example']['optimized']}"

    2. **STAR Format**
    Template: "Achieved X (Situation) by Y (Action) leading to Z (Result)"
    Example: "{examples['star_example']['situation']} by {examples['star_example']['action']} {examples['star_example']['result']}"

    3. **Skill Bridging**
    Template: "Gained [MISSING_SKILL] exposure through [RELATED_ACTIVITY]"
    Example: "{examples['padding_example']}"

    # OUTPUT REQUIREMENTS
    For EACH bullet point, provide:
    - 2 ATS-optimized versions
    - 1 STAR-formatted version 
    - 1 skill-bridged version (if needed)

    Format:
    {{
    "original": "Managed AWS infrastructure",
    "optimized": [
        {{
        "type": "ATS",
        "version": "Orchestrated 50+ AWS EC2 deployments with 99.9% uptime",
        "keywords": ["AWS", "EC2"],
        "metrics": ["50+", "99.9%"]
        }},
        {{
        "type": "STAR", 
        "version": "Reduced cloud costs 40% (Situation) via auto-scaling (Action) saving $1.2M (Result)",
        "components": {{
            "situation": "High cloud spend",
            "action": "Implemented AWS auto-scaling",
            "result": "$1.2M annual savings"
        }}
        }}
    ]
    }}

    # CRITICAL CONTEXT
    - Missing Requirements: {missing_skills}
    - Must Include: {primary_keywords}
    - Avoid: {relevance_report['system_flags'].get('red_flags', [])}
    - Target Metric Density: {job_analysis['scoring_rubric'].get('metric_density_target', '2+ per bullet')}
    """

    return prompt