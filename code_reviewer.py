import os
import sys
from colorama import Fore, Style, init
import openai

# Initialize colorama
init(autoreset=True)

# Set up API key for OpenAI
openai_api_key = 'your-openai-api-key-here'

def review_code_openai(code_snippet):
    openai.api_key = openai_api_key

    # Request a code review from OpenAI GPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please review the following code and provide feedback:\n\n{code_snippet}\n\nFeedback:",
        max_tokens=150
    )
    
    return response.choices[0].text.strip()

def suggest_improvements_openai(code_snippet):
    openai.api_key = openai_api_key

    # Request code improvement suggestions from OpenAI GPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Improve the following code based on best practices and provide the updated version:\n\n{code_snippet}\n\nImproved Code:",
        max_tokens=150
    )
    
    return response.choices[0].text.strip()

def main():
    print("Welcome to the AI-powered Code Reviewer!")
    print("Please enter your code snippet below. End your input with a single line containing only 'END':")
    
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        code_lines.append(line)
    
    code_snippet = "\n".join(code_lines)

    if openai_api_key and openai_api_key != 'your-openai-api-key-here':
        print("\nReviewing your code with OpenAI...")
        review = review_code_openai(code_snippet)
        suggest_improvements = suggest_improvements_openai
    else:
        print(Fore.RED + "No API Key Provided. Please check the GitHub for a tutorial on how to get it." + Style.RESET_ALL)
        sys.exit(1)
    
    print("\nCode Review:")
    print(review)

    if "improve" in review.lower() or "consider" in review.lower() or "should" in review.lower():
        print("\nThe AI has suggested improvements to your code.")
        print("Requesting improved code...")
        improved_code = suggest_improvements(code_snippet)
        print("\nImproved Code:")
        print(improved_code)
    else:
        print("\nNo significant improvements suggested.")

if __name__ == "__main__":
    main()
