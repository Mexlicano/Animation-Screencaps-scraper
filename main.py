import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
import time

# Name of the movies
name = "robin-hood-1973"

# Name of the folder
folder_path = ".\\Frames"

# Create a directory to save images and tags
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

num = 10

url = f"https://animationscreencaps.com/{name}/page/{num}"

# Create a session to maintain the connection
session = requests.Session()

# Send a GET request to the post page with headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = session.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

# Find the image URL
img = soup.findAll("img", class_="thumb")
for i in range(len(img)):
    image_source = img[i].get("src")
    print(f"Downloading {image_source}")

    # Parse the URL to get the image extension and file name
    parsed_url = urlparse(image_source)
    image_extension = os.path.splitext(parsed_url.path)[1]
    image_name = f"{name}_{i+1}{image_extension}"

    # Save image
    image_path = os.path.join(folder_path, image_name)
    img_response = session.get(image_source, headers=headers)
    with open(image_path, "wb") as img_file:
        img_file.write(img_response.content)
            
    # Add a 2-second delay
    time.sleep(2)

print(f"Every screencap from {url} has ben downloaded")
