import os
import json
import random
import shutil

# Image rarities
images = {
    "sonic.png": 0.20,
    "tails.png": 0.20,
    "knuckles.png": 0.20,
    "amy.png": 0.15,
    "big.png": 0.10,
    "shadow.png": 0.10,
    "eggman.png": 0.04,
    "metalsonic.png": 0.01,
}

# Generate a list of images based on rarities
total_nfts = 500
image_pool = []
image_counts = {image: 0 for image in images}  # Initialize counter for each image
for image, probability in images.items():
    count = int(total_nfts * probability)
    image_pool.extend([image] * count)
    image_counts[image] += count  # Update counts

# Shuffle the pool to randomize
random.shuffle(image_pool)

# Create the output folder if it doesn't exist
output_folder = "test"
os.makedirs(output_folder, exist_ok=True)

# Function to generate metadata JSON
def create_metadata(nft_number, image_file, output_folder):
    image_name = image_file.split('.')[0].capitalize()  # Get the name without extension and capitalize
    rarity_percentage = images[image_file] * 100

    metadata = {
        "name": f"NFT #{nft_number+1}",
        "symbol": "NFT",
        "description": "Your NFT example, made with love.",
        "seller_fee_basis_points": 250,
        "image": f"{nft_number}.png",
        "attributes": [
            {"trait_type": image_name, "value": f"{rarity_percentage:.2f}% Rarity"}
        ],
        "collection": {"name": "YourNFT Collection", "family": "Example"},
        "properties": {
            "files": [{"uri": f"{nft_number}.png", "type": "image/png"}],
            "category": "html",
            "creators": [{"address": "GAJh6ixRTSS6uh47ZDEUgqjhdKXRV7h3LAooMXpKmHqg", "share": 100}]
        }
    }
    with open(os.path.join(output_folder, f"{nft_number}.json"), 'w') as f:
        json.dump(metadata, f, indent=4)

# Create NFT images and metadata in the output folder
for i in range(total_nfts):
    selected_image = image_pool[i]
    nft_number = i  # Start from 0
    shutil.copyfile(selected_image, os.path.join(output_folder, f"{nft_number}.png"))
    create_metadata(nft_number, selected_image, output_folder)

# Log the count of each image used
for image, count in image_counts.items():
    print(f"{image}: {count} NFTs created")
