import cv2
import numpy as np

from typing import Any
from ultralytics import YOLO


class YoloModel:
    def __init__(self, model_path: str):
        self.model = YOLO(model_path)

    async def predict(self, image: bytes) -> Any:
        image = await self.prepare(image)
        results = self.model.predict(image)
        return results[0].plot()
        

    async def prepare(self, image: bytes) -> cv2.typing.MatLike:
        nparr = np.frombuffer(image, np.uint8) 
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)  
