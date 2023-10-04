import openai

# Set your API key here
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Define a prompt for question-answering or text generation
prompt = "tell me a joke "

# Generate text using GPT-3.5-turbo
response = openai.Completion.create(
    engine="text-davinci-002",  # Use "text-davinci-002" for GPT-3.5-turbo
    prompt=prompt,
    max_tokens=50  # Adjust as needed
)

# Get the generated text
generated_text = response.choices[0].text

# Print the generated text
print("Generated Text:")
print(generated_text)

