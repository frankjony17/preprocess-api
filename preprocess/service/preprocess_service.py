
import base64
from io import BytesIO

import cv2
import numpy as np
from PIL import Image


class PreprocessService:

    @staticmethod
    def rotate_image(image, angle):
        """Rotate image in a correct way.
        Args:
            image (str): Base64 encoded string to decode.
            angle (int)
        Returns:
            numpy.ndarray: An rotate n dimensional array of the input image.
        """
        (h, w) = image.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        m = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
        cos = np.abs(m[0, 0])
        sin = np.abs(m[0, 1])
        n_w = int((h * sin) + (w * cos))
        n_h = int((h * cos) + (w * sin))
        m[0, 2] += (n_w / 2) - cX
        m[1, 2] += (n_h / 2) - cY
        return cv2.warpAffine(image, m, (n_w, n_h))

    @staticmethod
    def increase_image(image_np, scale=275):
        """Increase the image according to a perceptual.
        Args:
            image_np (numpy.ndarray): n dimensional array.
            scale (int): Scale percentage.
        Returns:
            numpy.ndarray: An increase n dimensional array of the input image.
        """
        width = int(image_np.shape[1] * scale / 100)
        height = int(image_np.shape[0] * scale / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(image_np, dim, interpolation=cv2.INTER_CUBIC)
        return resized

    @staticmethod
    def np_array_to_base64(image_np):
        """Rotate image in a correct way.
        Args:
            image_np (numpy.ndarray): n dimensional array.
        Returns:
            str: 'base64': String from base64 encoded.
        """
        pil_img = Image.fromarray(image_np)
        buff = BytesIO()
        pil_img.save(buff, "PNG")
        new_image_64 = base64.b64encode(buff.getvalue()).decode("utf-8")
        return new_image_64
