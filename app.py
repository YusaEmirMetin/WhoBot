import os
from google.genai import Client
from dotenv import load_dotenv

# 1. Load Configuration and API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Configure Gemini Client
client = Client(api_key=api_key)

def kim_bu(isim):
    """Get summary information about the given name from Gemini."""
    prompt = f"You are a Twitter bot. Provide a brief, impressive summary of a maximum of 250 characters about the following person: {isim}"
    
    try:
        # Write model name directly without 'models/' prefix
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# --- TEST IN VS CODE ---
if __name__ == "__main__":
    user_input = input("Enter the name of the person you want to know about: ")
    print("\n[WhoBot Researching...]\n")
    print(kim_bu(user_input))