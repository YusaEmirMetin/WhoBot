import os
from groq import Groq
from dotenv import load_dotenv

# 1. Load Configuration and API Key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 2. Configure Groq Client
client = Groq(api_key=api_key)

def kim_bu(isim):
    """Get summary information about the given name from Groq."""
    prompt = f"You are a Twitter bot. Provide a brief, impressive summary of a maximum of 250 characters about the following person: {isim}"
    
    try:
        # Use Groq's chat completion API with available model
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# --- TEST IN VS CODE ---
if __name__ == "__main__":
    user_input = input("Enter the name of the person you want to know about: ")
    print("\n[WhoBot Researching...]\n")
    print(kim_bu(user_input))