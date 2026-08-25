from pydantic import BaseModel, field_validator

class PincodeRequest(BaseModel):
    pincode: str

# validates that the picnode must be exactly of 6 digits
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("The pincode must be exactly of 6 digits.")
        return value

class LocationResponse(BaseModel):
    pincode: str
    city: str
    state: str
    district: str

class BulkRequests(BaseModel):
    pincodes: list[str]

    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls, values):
        if len(values) == 0:
            raise ValueError("Atleast one pincode is required.")
        if len(values) >= 16:
            raise ValueError("Only 16 pincodes are allowed.")
        for code in values:
            if len(code) != 6 or not code.isdigit():
                raise ValueError("Each pincode must be exactly of 6 digits.")
        return values

class BulkResponse(BaseModel):
    success: str = "Success"
    found: int
    not_found: int
    results: list[LocationResponse]
    missing: list[str]



