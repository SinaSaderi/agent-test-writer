from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import openai

app = FastAPI(title="Code Generator API", version="1.0")

# Request Model
class CodeRequest(BaseModel):
    description: str  # Code description
    language: str     # Programming language


# API Endpoint
@app.post("/api/v1/generate-code")
async def generate_code(request: CodeRequest, openai_api_key: str = Query(..., description="OpenAI API key")):
    """
    Generate code based on the provided description, language, and OpenAI API key.
    """
    try:
        # Set OpenAI API key
        openai.api_key = openai_api_key

        # Construct professional prompt
        preprompt = f"""
        You are a highly skilled software developer. Write clean, professional, and production-ready code in {request.language}.
        Include appropriate comments for clarity, and ensure it adheres to best practices.
        The following is the description of the code to generate:

        {request.description}

        Provide the code only, without explanations or extra text.
        """

        # Call OpenAI GPT API
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=preprompt,
            max_tokens=1000,
            temperature=0.7
        )

        # Return generated code
        generated_code = response.choices[0].text.strip()
        return {"generated_code": generated_code}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating code: {str(e)}")
