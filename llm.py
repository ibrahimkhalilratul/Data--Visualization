from transformers import AutoTokenizer, AutoModelForCausalLM

# Load a different model and tokenizer
def load_model():
    """Load the GPT-2 model and tokenizer."""
    model_path = "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    return tokenizer, model

def query_model(prompt, tokenizer, model):
    """Query the model."""
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=200, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# # test_llm.py
# from llm import load_model, query_model

# # Load the model and tokenizer
# tokenizer, model = load_model()

# # Define a test prompt
# prompt = "What is the capital of France?"

# # Query the model
# response = query_model(prompt, tokenizer, model)

# # Print the response
# print("Response:", response)