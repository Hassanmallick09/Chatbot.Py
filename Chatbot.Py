import requests

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

# Main function to interact with the bot
def main():
    print("Welcome to the Image Generation Bot!")
    
    while True:
        # Get the prompt from the user
        prompt = input("Enter a prompt for image generation (or 'exit' to quit): ")
        
        if prompt.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Generate the image using the provided prompt
        print("Generating image, please wait...")
        image_url = generate_image(prompt)
        
        # Display the generated image URL
        print(f"Image URL: {image_url}")

# Run the bot
if __name__ == "__main__":
    main()
