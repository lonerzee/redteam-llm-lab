from llama_cpp import Llama

print("Loading model... (this takes 30-60 seconds)")

# Load the model
llm = Llama(
    model_path="./models/phi-3-mini-q4.gguf",
    n_ctx=2048,  # Context window
    n_threads=4,  # CPU threads
    verbose=False,
)

print("Model loaded successfully!")
print("\nTesting basic prompt...\n")

# Test with a simple prompt
response = llm(
    "Hello! What are you?", max_tokens=100, temperature=0.7, stop=["User:", "\n\n"]
)

print("Response:")
print(response["choices"][0]["text"])
print("\n✓ Test successful!")
