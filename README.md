# Ubuntu_Requests
🖼️ Ubuntu Image Fetcher

A Python tool for mindfully collecting images from the web.
Built with community, respect, sharing, and practicality in mind — following the spirit of Ubuntu principles.

✨ Features

✅ Multiple URLs Support – Fetch several images in one go
✅ Duplicate Prevention – Avoids downloading the same image twice
✅ Content-Type Validation – Skips files that are not images
✅ Safe Filenames – Extracts names from URLs or generates one if missing
✅ Organized Storage – Saves images in a Fetched_Images folder
✅ Graceful Error Handling – Deals with network errors without crashing

📦 Installation

Clone or download this project:

git clone https://github.com/yourusername/ubuntu-image-fetcher.git
cd ubuntu-image-fetcher


Install dependencies:

pip install requests

🚀 Usage

Run the script:

python3 ubuntu_image_fetcher.py


When prompted, enter one or more image URLs (separated by spaces or commas):

Please enter image URLs (separate multiple with space or comma): 
https://example.com/image1.jpg, https://example.com/image2.png


Images will be saved in the Fetched_Images folder.