# ---------------- #
# MADE BY SHIV-UWU #
# ---------------- #

# This is a simple script that uses the OpenAI API to generate text based on a prompt.
import openai
openai.api_key = "API_KEY_HERE"  # Replace API_KEY_HERE with your API key.

while True:
    # Replace text-davinci-003 with the engine you want to use.
    model_engine = "text-davinci-003"
    prompt = input('Enter new prompt: ')  # Enter the prompt you want to use.

    # If the prompt contains exit or quit, exit the program.
    if 'exit' in prompt or 'quit' in prompt:
        break

    completion = openai.Completion.create(  # Create the completion.
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the response from the completion.
    response = completion.choices[0].text

    print(response)  # Print the response.
