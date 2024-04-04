from fastapi import HTTPException


def raise_404_if_none(obj: any, message: str = None) -> None:
    if message:
        detail = message
    else:
        detail = 'Object not found'
    if not obj:
        raise HTTPException(status_code=404, detail=detail)
