
# AI-Powered Code Reviewer

## Description
This project is an AI-powered code reviewer that provides feedback on code snippets using OpenAI's GPT model. It’s designed to be easy to use and highly customizable.

## Features
- Interactive command-line interface for code input
- AI-powered code review and feedback
- Uses OpenAI's GPT model for code analysis

## Installation

To get started, you need to install the required Python packages. Create a virtual environment and install the dependencies listed in `requirements.txt`:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

API Key

This project requires an API key from OpenAI. To get an API key:

	1.	Go to OpenAI’s website and sign up for an account if you don’t already have one.
	2.	Navigate to the API keys page and create a new key.

Configure Your Key:

	•	Replace 'your-openai-api-key-here' in code_reviewer.py with the API key you obtained.

Usage

	1.	Set Up API Key: Replace 'your-openai-api-key-here' in code_reviewer.py with your API key.
	2.	Run the Script:

python code_reviewer.py


	3.	Enter Your Code: Follow the prompts to input your code snippet. End your input with END.
	4.	Review: The script will output the AI-generated review of your code. If improvements are suggested, it will also provide an improved version.

Example

Welcome to the AI-powered Code Reviewer!
Please enter your code snippet below. End your input with a single line containing only 'END':

def add_numbers(a, b):
    return a + b
END

Reviewing your code...

Code Review:
The function `add_numbers` is simple and works correctly. Consider adding type hints to improve readability.

The AI has suggested improvements to your code.
Requesting improved code...

Improved Code:
def add_numbers(a: int, b: int) -> int:
    return a + b

Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Contributions are welcome!

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

	•	OpenAI for providing the GPT model
	•	Various Python libraries and tools used in this project
