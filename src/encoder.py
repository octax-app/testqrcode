import os
from enum import Enum
from PIL import Image, ImageDraw

class CorrectionLevel(Enum):
    L = 1
    M = 2
    Q = 3
    H = 4

class Circle2DCodeEncoder:
    def __init__(self, text: str, logo: str | None = None, color: str = "#6B39F4", correction_level: CorrectionLevel = CorrectionLevel.H, version: int = 1, size: int = 500):
        self.text = text
        self.logo = logo
        self.color = color
        self.correction_level = correction_level
        self.version = version
        self.size = size
        self.image = Image.new("RGB", (self.size, self.size), "white")
        self.draw = ImageDraw.Draw(self.image)

    def _drewCenter(self):
        img_size = self.image.size[0]
        circle_diameter = int(img_size * 0.1)
        circle_radius = circle_diameter // 2
        
        center_x = img_size // 2
        center_y = img_size // 2

        # Create circle with empty or logo at the center
        left_up_point = (center_x - circle_radius, center_y - circle_radius)
        right_down_point = (center_x + circle_radius, center_y + circle_radius)
        two_point_list = [left_up_point, right_down_point]
        self.draw.ellipse(two_point_list, fill='white', outline=self.color, width=4)

        if self.logo:
            logo_img = Image.open(self.logo)
            logo_size = (circle_diameter, circle_diameter)
            logo_img = logo_img.resize(logo_size)
            
            # Create a mask for the circular logo
            mask = Image.new('L', logo_size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + logo_size, fill=255)

            # Calculate position to paste the logo
            paste_position = (center_x - circle_radius, center_y - circle_radius)
            self.image.paste(logo_img, paste_position, mask)
    
    def _drewPositionDetectionPattern(self):
        pass

    def _drewTimingPattern(self):
        pass

    def _drewAlignmentPattern(self):
        pass

    def _drewFormatInformation(self):
        pass

    def _drewVersionInformation(self):
        pass

    def _drewDataAndErrorCorrectionCodewords(self):
        pass

    def encode(self):
        self._drewCenter()
        self._drewPositionDetectionPattern()
        self._drewTimingPattern()
        self._drewAlignmentPattern()
        self._drewFormatInformation()
        self._drewVersionInformation()
        self._drewDataAndErrorCorrectionCodewords()
        # Further implementation goes here
        self.image.save("output.png")

if __name__ == "__main__":
    encoder = Circle2DCodeEncoder("Hello, World!", correction_level=CorrectionLevel.H, version=1, size=500)
    encoder.encode()