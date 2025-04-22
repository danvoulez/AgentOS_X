import os
import google.generativeai as gemini

class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        gemini.configure(api_key=self.api_key)

    def generate_text(self, prompt):
        response = gemini.generate_text(prompt=prompt)
        return response['text']
