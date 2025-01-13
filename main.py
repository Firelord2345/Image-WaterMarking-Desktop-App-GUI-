import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Base class for image processing
class ImageProcessor:
    def __init__(self):
        self.image = None
        self.watermarked_image = None

    def load_image(self, image_path):
        """Load an image from the given path."""
        try:
            self.image = Image.open(image_path)
            self.watermarked_image = self.image.copy()
        except Exception as e:
            print(f"Error loading image: {e}")
            self.image = None
            self.watermarked_image = None

    def apply_watermark(self, text, position, font_size, transparency):
        """Apply watermark to the image."""
        if not self.image:
            return

        # Create a copy of the image to apply watermark
        self.watermarked_image = self.image.copy()
        draw = ImageDraw.Draw(self.watermarked_image)

        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        # Get bounding box to calculate text size
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        positions = {
            "Top-Left": (10, 10),
            "Top-Right": (self.watermarked_image.width - text_width - 10, 10),
            "Bottom-Left": (10, self.watermarked_image.height - text_height - 10),
            "Bottom-Right": (self.watermarked_image.width - text_width - 10, self.watermarked_image.height - text_height - 10),
            "Center": ((self.watermarked_image.width - text_width) // 2, (self.watermarked_image.height - text_height) // 2),
        }

        watermark_position = positions.get(position, (10, 10))

        # Apply the watermark with transparency
        draw.text(watermark_position, text, fill=(255, 255, 255, int(255 * transparency / 100)), font=font)

    def get_watermarked_image(self):
        """Return the watermarked image or None if not available."""
        return self.watermarked_image

# GUI class for handling user interface
class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermarking Application")
        self.root.geometry("800x600")

        # Initialize image processor
        self.processor = ImageProcessor()

        # Image Selection
        self.image_frame = tk.Frame(root)
        self.image_frame.pack(pady=10)

        self.browse_button = tk.Button(self.image_frame, text="Browse Image", command=self.select_image)
        self.browse_button.pack(side=tk.LEFT, padx=5)

        self.selected_image_label = tk.Label(self.image_frame, text="No image selected")
        self.selected_image_label.pack(side=tk.LEFT, padx=5)

        # Watermark Input
        self.watermark_frame = tk.Frame(root)
        self.watermark_frame.pack(pady=10)

        self.watermark_label = tk.Label(self.watermark_frame, text="Watermark Text:")
        self.watermark_label.pack(side=tk.LEFT, padx=5)

        self.watermark_entry = tk.Entry(self.watermark_frame, width=30)
        self.watermark_entry.pack(side=tk.LEFT, padx=5)

        # Position Selection
        self.position_frame = tk.Frame(root)
        self.position_frame.pack(pady=10)

        self.position_label = tk.Label(self.position_frame, text="Position:")
        self.position_label.pack(side=tk.LEFT, padx=5)

        self.position_var = tk.StringVar(value="Bottom-Right")
        self.positions = ["Top-Left", "Top-Right", "Bottom-Left", "Bottom-Right", "Center"]
        for pos in self.positions:
            rb = tk.Radiobutton(self.position_frame, text=pos, variable=self.position_var, value=pos)
            rb.pack(side=tk.LEFT)

        # Transparency and Size Settings
        self.settings_frame = tk.Frame(root)
        self.settings_frame.pack(pady=10)

        self.transparency_label = tk.Label(self.settings_frame, text="Transparency:")
        self.transparency_label.pack(side=tk.LEFT, padx=5)

        self.transparency_scale = tk.Scale(self.settings_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.transparency_scale.set(50)  # Default value
        self.transparency_scale.pack(side=tk.LEFT, padx=5)

        self.size_label = tk.Label(self.settings_frame, text="Size:")
        self.size_label.pack(side=tk.LEFT, padx=5)

        self.size_scale = tk.Scale(self.settings_frame, from_=10, to=100, orient=tk.HORIZONTAL)
        self.size_scale.set(20)  # Default value
        self.size_scale.pack(side=tk.LEFT, padx=5)

        # Preview Canvas
        self.canvas = tk.Canvas(root, width=600, height=400, bg="lightgray")
        self.canvas.pack(pady=20)

        # Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.apply_button = tk.Button(self.button_frame, text="Apply Watermark", command=self.add_watermark)
        self.apply_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Save Image", command=self.save_image)
        self.save_button.pack(side=tk.LEFT, padx=5)

    def select_image(self):
        """Select an image file to load."""
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        if image_path:
            self.selected_image_label.config(text=image_path)
            self.processor.load_image(image_path)
            self.show_preview(self.processor.get_watermarked_image())

    def show_preview(self, image):
        """Display the preview of the image."""
        if image is None:
            print("Error: No image to display.")
            return

        preview_image = image.copy()
        preview_image.thumbnail((600, 400))
        img_tk = ImageTk.PhotoImage(preview_image)
        self.canvas.image = img_tk
        self.canvas.create_image(300, 200, image=img_tk)

    def add_watermark(self):
        """Add watermark to the image."""
        text = self.watermark_entry.get()
        position = self.position_var.get()
        font_size = int(self.size_scale.get())
        transparency = self.transparency_scale.get()

        # Apply watermark
        self.processor.apply_watermark(text, position, font_size, transparency)
        self.show_preview(self.processor.get_watermarked_image())

    def save_image(self):
        """Save the watermarked image."""
        watermarked_image = self.processor.get_watermarked_image()
        if watermarked_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                watermarked_image.save(save_path)

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
