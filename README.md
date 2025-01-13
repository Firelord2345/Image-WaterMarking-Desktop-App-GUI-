


# Image Watermarking Application

## Description

This is a simple desktop application built with Python using Tkinter and Pillow libraries. It allows users to apply a customizable watermark to their images. Users can load an image, enter the watermark text, choose its position, adjust the transparency, and set the font size. The application also provides a preview of the image with the watermark before saving the final result.

## Features

- **Image Upload:** Load an image file from your local storage.
- **Watermark Text:** Add custom text as a watermark to the image.
- **Position Selection:** Choose the position of the watermark on the image (Top-Left, Top-Right, Bottom-Left, Bottom-Right, Center).
- **Transparency Adjustment:** Adjust the transparency of the watermark.
- **Font Size Adjustment:** Change the font size of the watermark.
- **Image Preview:** See a preview of the image with the watermark applied.
- **Save Watermarked Image:** Save the final image with the watermark in PNG or JPEG format.

## Requirements

- Python 3.x
- Tkinter (for the GUI)
- Pillow (for image processing)

To install the required libraries, use the following command:

```bash
pip install pillow
```

## Usage

1. **Run the application**: Execute the Python script to launch the GUI.
   
2. **Select an image**: Click the "Browse Image" button to select an image from your local storage.

3. **Add watermark**: Enter the watermark text and adjust the font size and transparency using the sliders. Select the position of the watermark on the image.

4. **Preview**: Click on "Apply Watermark" to see the watermark applied to the image. You can adjust settings and reapply if needed.

5. **Save image**: Once satisfied with the preview, click the "Save Image" button to save the watermarked image to your desired location.

## Example

Here’s an example of how the watermarking works:

1. Select an image (e.g., a logo or a photo).
2. Enter the watermark text such as "Sample Watermark".
3. Adjust the transparency and font size to fit your preference.
4. Position the watermark where you want it (e.g., Bottom-Right).
5. Preview the result, and save the watermarked image.

## Future Improvements

- **Live Preview**: Allow users to see changes to the watermark in real-time as they adjust transparency and font size.
- **Text Rotation**: Allow the watermark text to be rotated for more creative options.
- **Drag-to-Position**: Allow users to drag the watermark to a custom position on the image.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.


