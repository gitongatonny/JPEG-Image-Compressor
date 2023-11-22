from PIL import Image
import os
import subprocess

def compress_image(input_filename, output_filename):
    original_image = Image.open(input_filename)

    if original_image.format != 'JPEG':
        print("Input image must be in JPEG format.")
        return

    compressed_image_filename = output_filename + ".jpg"
    original_image.save(compressed_image_filename, "JPEG", quality=20)

    return compressed_image_filename

def calculate_percentage(original_size, compressed_size):
    return (1 - compressed_size / original_size) * 100

def open_image_with_viewer(image_filename):
    subprocess.run(["start", "explorer", image_filename], shell=True)

def main():
    input_filename = input("Enter the path to the JPEG image file: ")

    if not os.path.isfile(input_filename):
        print("File not found.")
        return

    output_filename = "compressed_" + os.path.splitext(os.path.basename(input_filename))[0]
    original_size = os.path.getsize(input_filename)
    compressed_image_filename = compress_image(input_filename, output_filename)
    compressed_size = os.path.getsize(compressed_image_filename)

    print("Original image path:", os.path.abspath(input_filename))
    print("Original image size:", original_size, "bytes")
    print("Compressed image path:", os.path.abspath(compressed_image_filename))
    print("Compressed image size:", compressed_size, "bytes")
    print("Compression percentage:", calculate_percentage(original_size, compressed_size), "%")

    open_image_with_viewer(input_filename)
    open_image_with_viewer(compressed_image_filename)

if __name__ == "__main__":
    main()