import io
import cv2

from typing import Annotated
from fastapi import APIRouter, File
from fastapi.responses import FileResponse, StreamingResponse

from services.model import YoloModel
from utils.config import MODEL_PATH


router = APIRouter(
    prefix='/predict',
    tags=['Predict']
)

model = YoloModel(model_path=MODEL_PATH)


@router.post('', response_class=FileResponse)
async def predict(
    image: Annotated[bytes, File()]
):
    img_with_boxes = await model.predict(image)
    _, img_encoded = cv2.imencode('.jpg', img_with_boxes)
    return StreamingResponse(io.BytesIO(img_encoded.tobytes()), media_type='image/jpeg')


