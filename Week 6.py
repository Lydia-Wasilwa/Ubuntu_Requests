import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extract filename from URL or generate one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  # If no filename is found, create one based on hash
        filename = f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"
    return filename

def is_duplicate(filepath, content):
    """Check if a file with the same content already exists."""
    if os.path.exists(filepath):
        with open(filepath, "rb") as existing_file:
            return hashlib.md5(existing_file.read()).hexdigest() == hashlib.md5(content).hexdigest()
    return False

def fetch_image(url):
    """Download a single image with error handling and checks."""
    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Security precaution: Check Content-Type to confirm it's an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipping {url} - Not an image (Content-Type: {content_type})")
            return
        
        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicate downloads
        if is_duplicate(filepath, response.content):
            print(f"⚠ Skipping duplicate image: {filename}")
            return
        
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred for {url}: {e}")

def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    # Accept multiple URLs separated by spaces or commas
    urls = input("Please enter image URLs (separate multiple with space or comma): ")
    url_list = [u.strip() for u in urls.replace(",", " ").split() if u.strip()]

    if not url_list:
        print("✗ No URLs provided. Exiting.")
        return
    
    for url in url_list:
        fetch_image(url)

    print("\n🌱 All done! Your fetched images are organized in 'Fetched_Images'.")
    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
