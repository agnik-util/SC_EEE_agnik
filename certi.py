from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm  # For progress bar
import os

# Define the path to save the certificates
save_path = r"D:\koding\Test_certificate\certificates"  # Update with your path

# Create the directory if it doesn't exist
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Load the certificate template
template = Image.open('template.png')

# Initialize the drawing context on the template
draw = ImageDraw.Draw(template)

# Read names from the text file
with open('name.txt', 'r') as file:
    names = [line.strip() for line in file]

# Check if there are names present
if names:
    total_certificates = len(names)
    progress_bar = tqdm(total=total_certificates, desc="Generating Certificates")

    for name in names:
        # Define the font and size for the name
        font_size_name = 70
        font = ImageFont.truetype('Poppins-Bold.ttf', font_size_name)

        # Specify the coordinates for the name placement
        name_x = 80
        name_y = 220

        # Draw the name on the certificate
        temp_image = template.copy()  # Copy the template for each certificate
        draw_temp = ImageDraw.Draw(temp_image)
        draw_temp.text((name_x, name_y), name, fill='#000000', font=font)

        # Save the certificate with the name as a new file
        certificate_name = f'{name}.png'
        certificate_path = os.path.join(save_path, certificate_name)
        temp_image.save(certificate_path)
        print(f"certificates saving in:{certificate_path}")

        progress_bar.update(1)  # Update progress bar

    progress_bar.close()  # Close progress bar
    print(f"Certificates generated successfully! All certificates are saved in: {save_path}")
else:
    print("Error: No names found in the file.")
