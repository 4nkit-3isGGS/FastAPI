from fastapi.responses import JSONResponse 
from fastapi import Request

# Custom exception classes
class PincodeNotFoundError(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode

class InvalidPincodeError(Exception):
    def __init__(self, pincode: str, reason: str = "Invalid Format"):
        self.pincode = pincode
        self.reason = reason

# Custom exception Handlers 

async def pincode_not_found_handler(request: Request, exc: PincodeNotFoundError):
    return JSONResponse(
        status_code= 404,
        content= {
            "error": "No Pincode found!",
            "message": f"Location with pincode: '{exc.pincode}' was not found",
            "pincode": exc.pincode
        }
    )

async def invalid_pincode_handler(request: Request, exc: InvalidPincodeError):
    return JSONResponse(
        status_code= 400,
        content= {
            "error": "Invalid Pincode",
            "message": f"The format of the pincode: '{exc.pincode} is invalid. Reason: {exc.reason}",
            "pincode": exc.pincode
        }
    )


