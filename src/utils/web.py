from fastapi import HTTPException


def raise_404_if_none(obj: any, message: str = None) -> None:
    if message:
        msg = message
    else:
        msg = 'Object not found'
    if not obj:
        raise HTTPException(status_code=404, detail=msg)
