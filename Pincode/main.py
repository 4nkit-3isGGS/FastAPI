from fastapi import FastAPI
from pincode_data import pincode_db
from models import PincodeRequest, LocationResponse, BulkResponse, BulkRequests
from custom_exceptions import (
    PincodeNotFoundError,
    pincode_not_found_handler,
    InvalidPincodeError,
    invalid_pincode_handler
)

app = FastAPI(
    title= "Pincode Lookup API",
    description= "Auto-fills the City and State name whenever the pincode of any place provided.",
    version= "0.1.0",
    docs_url = "/docs"
)

# registering the  cusyom exception handlers 
app.add_exception_handler(PincodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPincodeError, invalid_pincode_handler)

@app.get("/")
def root():
    return {
        "message": "Pincode-lookup API"
    }

@app.post("/pincode/bulk", response_model= BulkResponse)
def bulk_pincodes(request: BulkRequests):
    results = []
    missing = []

    for code in request.pincodes:
        if code in pincode_db:
            results.append(pincode_db[code])
        else:
            missing.append(code)
    
    return BulkResponse(
        found= len(results),
        not_found= len(missing),
        results= results,
        missing= missing
    )

@app.get("/pincode/{code}", response_model= LocationResponse)
def lookup_pincode(code: str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPincodeError(code, "Pincode must be exactly 6 digits")
    
    if code not in pincode_db:
        raise PincodeNotFoundError(code)
    return pincode_db[code]
