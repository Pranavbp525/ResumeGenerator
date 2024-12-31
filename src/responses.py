from pydantic import BaseModel
from typing import List, Optional

class ExperienceItem(BaseModel):
    company: str
    duration: str
    role: str
    location: str
    tools: List[str]
    responsibilities: List[str]

class ExperienceResponse(BaseModel):
    experiences: List[ExperienceItem]

class ProjectItem(BaseModel):
    title: str
    skills: List[str]
    descriptions: List[str]

class ProjectsResponse(BaseModel):
    projects: List[ProjectItem]

class SkillItem(BaseModel):
    category: str
    items: List[str]

class SkillsResponse(BaseModel):
    skills: List[SkillItem]

class EducationItem(BaseModel):
    university: str
    duration: str
    degree: str
    location: str
    gpa: str  
    relevant_coursework: List[str]

class EducationResponse(BaseModel):
    education: List[EducationItem]

class HeadingData(BaseModel):
    name: str
    phone: str
    email: str
    linkedin: str
    github: str

