import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any

# Initialize FastAPI app
app = FastAPI(title="Code Generator API", description="API to generate code based on description using OpenAI.", version="1.0")

# OpenAI API Key (replace with your actual key)
openai.api_key = ""

# Request Model
class CodeRequest(BaseModel):
    description: str  # Description of the code to generate
    language: str     # Programming language for the code (e.g., python, javascript)

# Response Model
class CodeResponse(BaseModel):
    generated_code: str

# API Endpoint
@app.post("/api/v1/generate-code", response_model=CodeResponse)
async def generate_code(request: CodeRequest):
    """
    Generate code based on the provided description and programming language using OpenAI.
    """
    try:
        # Preprompt for OpenAI to generate professional code
        preprompt = f"""
        You are a highly skilled software developer. Write clean, professional, and production-ready code in {request.language}.
        Include appropriate comments for clarity, and ensure it adheres to best practices.
        The following is the description of the code to generate:

        {request.description}

        Provide the code only, without explanations or extra text.
        """

        # Call OpenAI GPT API
        response = openai.Completion.create(
            model="text-davinci-003",  # GPT-3.5 model
            prompt=preprompt,
            max_tokens=1000,
            temperature=0.7
        )

        # Extract generated code
        generated_code = response.choices[0].text.strip()

        # Return the code as response
        return CodeResponse(generated_code=generated_code)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating code: {str(e)}")
