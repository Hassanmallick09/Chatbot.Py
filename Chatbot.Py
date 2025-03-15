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
    "A bustling spaceport on Mars"
"A dragon flying over a medieval castle"
"A mysterious cave glowing with bioluminescent plants"
"A steampunk airship in the clouds"
"A peaceful Japanese garden with a koi pond"
"A neon-lit street in Tokyo at night"
"A magical library with floating books"
"A snow-covered mountain peak with a bright blue sky"
"A giant whale swimming in outer space"
"A futuristic cityscape with flying cars"
"A robot exploring an alien planet"
"A samurai warrior in traditional armor"
"A pirate ship sailing through a storm"
"A bustling market in an ancient Arabian city"
"A sunset over a vast desert with sand dunes"
"A majestic lion roaming through a savanna"
"A cyberpunk city with glowing skyscrapers"
"A beautiful autumn forest with colorful leaves"
"A giant tree with a mystical portal at its base"
"A giant, peaceful elephant in a lush jungle"
"A futuristic high-speed train crossing a vast bridge"
"A secret garden hidden within a mountain"
"A time traveler in a futuristic suit"
"A majestic phoenix rising from the ashes"
"A robot cat playing with a glowing ball"
"A surreal city floating in the sky"
"A lighthouse on a cliff during a thunderstorm"
"A winter wonderland with ice sculptures"
"A spaceship landing on a new alien world"
"A surreal underwater city with glowing creatures"
"A giant mechanical spider walking through a forest"
"A glowing jellyfish swimming in the night sea"
"A mystical moonlit forest with enchanted creatures"
"A colorful hot air balloon floating above the clouds"
"A futuristic robot helping a human scientist"
"A wizard casting a spell in a dark forest"
"A cat sailing a small boat on a calm lake"
"A vibrant coral reef with colorful fish"
"A breathtaking view from the top of a skyscraper"
"A desert oasis with clear blue water and palm trees"
"A majestic waterfall cascading down a cliff"
"A large asteroid about to collide with a planet"
"A futuristic robot army marching across a field"
"A tranquil beach with crystal-clear waters and palm trees"
"A group of astronauts walking on the surface of the moon"
"A mysterious, fog-covered forest with glowing orbs"
"A colorful carnival with rides and food stands"
"A dragon perched on a mountain, overlooking a valley"
"A large, ornate clock tower with a giant clock face"
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
