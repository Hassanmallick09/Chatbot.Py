import requests
import time

# Function to generate an image
def generate_image(prompt):
    url = "https://api.hyperbolic.xyz/v1/image/generation"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY_HERE"  # Replace with your actual API key
    }
    
    # Define the payload to send to the API
    data = {
        "model_name": "SD1.5",  # Use the model you want
        "prompt": prompt,  # The prompt you want to use for the image generation
        "steps": 30,
        "cfg_scale": 5,
        "enable_refiner": False,
        "height": 1024,
        "width": 1024,
        "backend": "auto"
    }
    
    try:
        # Send the request to the API
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Get the JSON response
        result = response.json()
        
        # Check if the response contains a URL (assuming it's in the 'data' field)
        if 'data' in result:
            image_url = result['data'][0]  # Extract the image URL from the response
            return image_url
        else:
            return "Error: Image URL not found in the response."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Predefined list of prompts for the bot to use
prompts = [
    "A futuristic cityscape",
    "A serene beach at sunset",
    "A mountain range with snow",
    "A robot in a high-tech laboratory",
    "A fantasy forest with glowing mushrooms",
    "A majestic waterfall in a jungle",
    "A surreal abstract painting",
    "A cat with wings flying in the sky",
    "A vibrant sunset over the ocean",
    "A futuristic car driving through a neon city"
]

# Function to run the bot automatically
def run_auto_bot():
    print("Auto Image Generation Bot Started!")
    
    for i, prompt in enumerate(prompts):
        print(f"Generating image {i + 1}: {prompt}")
        
        # Generate the image for the current prompt
        image_url = generate_image(prompt)
        
        # Display the generated image URL
        print(f"Image URL for prompt '{prompt}': {image_url}\n")
        
        # Optional: Delay between image generations (e.g., 10 seconds)
        time.sleep(10)
    
    print("All images generated successfully!")

# Run the bot
if __name__ == "__main__":
    run_auto_bot()
