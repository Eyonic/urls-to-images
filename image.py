import requests
from PIL import Image
from io import BytesIO
import os

def download_and_convert_images(urls, jpg_save_dir, webp_save_dir, jpg_thumbs_dir, webp_thumbs_dir):
    for url in urls:
        try:
            # Send an HTTP GET request to the URL
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Read the image data
                image_data = response.content

                # Create a PIL Image object from the image data
                image = Image.open(BytesIO(image_data))

                # Convert the image to RGB mode if it's in RGBA mode
                if image.mode == 'RGBA':
                    image = image.convert('RGB')

                # Extract the filename from the URL
                file_name = os.path.basename(url)

                # Remove file extension, if any, to ensure a clean base name
                file_name = os.path.splitext(file_name)[0]

                # Save the image as JPG
                jpg_path = os.path.join(jpg_save_dir, f"{file_name}.jpg")
                image.save(jpg_path, "JPEG")

                # Create a 200x200 thumbnail
                thumbnail = image.resize((200, 200))

                # Save the thumbnail as JPG
                jpg_thumb_path = os.path.join(jpg_thumbs_dir, f"{file_name}.jpg")
                thumbnail.save(jpg_thumb_path, "JPEG")

                # Save the image as WebP
                webp_path = os.path.join(webp_save_dir, f"{file_name}.webp")
                image.save(webp_path, "WEBP")

                # Create a 200x200 thumbnail as WebP
                webp_thumb_path = os.path.join(webp_thumbs_dir, f"{file_name}.webp")
                thumbnail.save(webp_thumb_path, "WEBP")

                print(f"Image {file_name} saved as {jpg_path} and {webp_path}")
                print(f"Thumbnail {file_name}_thumb saved as {jpg_thumb_path} and {webp_thumb_path}")
            else:
                print(f"Failed to download image from {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while processing {url}: {str(e)}")

# Example usage with a list of URLs
url_list = [
'https://fef5c1f60bff157bfd51-1d2043887f30fc26a838f63fac86383c.ssl.cf1.rackcdn.com/a04fe83ae7d8ef0af8cda393365c154fcf23294d_600_600_fill.jpg',
'https://fef5c1f60bff157bfd51-1d2043887f30fc26a838f63fac86383c.ssl.cf1.rackcdn.com/a04fe83ae7d8ef0af8cda393365c154fcf23294d_600_600_fill.jpg',
'https://fef5c1f60bff157bfd51-1d2043887f30fc26a838f63fac86383c.ssl.cf1.rackcdn.com/03b2a957571327e4e9700b6bb5d4a8b825ffd40e_600_600_fill.jpg',
'https://fef5c1f60bff157bfd51-1d2043887f30fc26a838f63fac86383c.ssl.cf1.rackcdn.com/14c2e998980fd241649480053ebae03ab70a42ef_600_600_fill.jpg'

]

jpg_save_directory = "jpg"
webp_save_directory = "webp"
jpg_thumbs_directory = "thumbs-jpg"
webp_thumbs_directory = "thumbs-webp"

# Create directories if they don't exist
for directory in [jpg_save_directory, webp_save_directory, jpg_thumbs_directory, webp_thumbs_directory]:
    os.makedirs(directory, exist_ok=True)

download_and_convert_images(url_list, jpg_save_directory, webp_save_directory, jpg_thumbs_directory, webp_thumbs_directory)
