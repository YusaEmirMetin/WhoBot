from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def get_person_info(name):
    """Get summary information about a person from Groq."""
    prompt = f"You are a Twitter bot. Provide a brief, impressive summary of a maximum of 250 characters about the following person: {name}"
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "WhoBot API is running!"})

@app.route("/api/search", methods=["POST"])
def search():
    """API endpoint to search for person information."""
    try:
        data = request.json
        person_name = data.get("name", "").strip()
        
        if not person_name:
            return jsonify({"error": "Please provide a person's name"}), 400
        
        result = get_person_info(person_name)
        
        return jsonify({
            "name": person_name,
            "info": result,
            "success": True
        }), 200
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        }), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
