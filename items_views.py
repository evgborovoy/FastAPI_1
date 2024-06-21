from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def items():
    return [
        "item1",
        "item2",
        "item3",
    ]


@router.get("/latest/")
def get_latest_item():
    return {
        "item":
            {
                "id": -1,
                "name": "latest"
            }
    }


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1)]):
    return {
        "item": {
            "id": item_id,
        },
    }
