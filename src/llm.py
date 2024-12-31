from openai import OpenAI
import logging
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def invoke_omni(system_prompt, prompt, response_format):
    """
    Invokes GPT-4o with a mandatory structured output.

    Args:
        system_prompt (str): The system-level instructions for the model.
        prompt (str): The user's input prompt.
        response_format (BaseModel): A Pydantic model class for enforcing structured output.

    Returns:
        BaseModel: Parsed structured response as per the response_format.
    """
    if not response_format or not issubclass(response_format, BaseModel):
        raise ValueError("A valid response_format inheriting from BaseModel must be provided.")

    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            response_format=response_format,
        )
        return completion.choices[0].message.parsed
    except Exception as e:
        logging.error(f"Error invoking OpenAI API: {e}")
        return None
    

def invoke_mini(system_prompt, prompt, response_format):
    """
    Invokes GPT-4o-mini with a mandatory structured output.

    Args:
        system_prompt (str): The system-level instructions for the model.
        prompt (str): The user's input prompt.
        response_format (BaseModel): A Pydantic model class for enforcing structured output.

    Returns:
        BaseModel: Parsed structured response as per the response_format.
    """
    if not response_format or not issubclass(response_format, BaseModel):
        raise ValueError("A valid response_format inheriting from BaseModel must be provided.")

    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            response_format=response_format,
        )
        return completion.choices[0].message.parsed
    except Exception as e:
        logging.error(f"Error invoking OpenAI API: {e}")
        return None

