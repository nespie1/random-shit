import os
import shutil

def flatten_captcha_images(base_path):
    # List all folders inside the base 'captcha_images' directory
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)

        # Check if it's a directory
        if os.path.isdir(folder_path):
            # List the files inside the directory (should be only one .png file)
            files = os.listdir(folder_path)

            # Assuming there's only one png file in each folder
            if files[0].endswith('.png'):
                if len(files) > 1:
                    print(f"More that 1 file in folder: {folder_name}")
                image_file = files[0]
                original_image_path = os.path.join(folder_path, image_file)

                # Construct the new name and path for the image file
                new_image_name = f"{folder_name}.png"
                new_image_path = os.path.join(base_path, new_image_name)

                # Move and rename the image file to the base path
                shutil.move(original_image_path, new_image_path)
            else:
                print(f"Unexpected content in folder: {folder_name}")

            # Remove the now empty folder
            shutil.rmtree(folder_path)

if __name__ == "__main__":
    captcha_images_path = 'captcha_images_1'  # Update this with your path
    flatten_captcha_images(captcha_images_path)