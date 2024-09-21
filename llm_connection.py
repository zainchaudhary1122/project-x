import os
import google.generativeai as genai
# from prompt import joined_prompt

def llm_processing(joined_prompt):
  genai.configure(api_key=os.environ["GEMINI_API_KEY"])

  generation_config = {
    "temperature": 0.4,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
  )

  response = model.generate_content(joined_prompt)
  return response.text

# input = "what are the main aims to become a programmer?"
# result = llm_processing(joined_prompt)
# print(result)