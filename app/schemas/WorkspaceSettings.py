from pydantic import BaseModel


class WorkspaceSettings(BaseModel):
    theme: str
    color: str
    font_size: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "theme": "light",
                "color": "green",
                "font_size": 16,
            }
        }

class WorkspaceSettingsCreate(WorkspaceSettings):
    theme: str
    color: str
    font_size: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "theme": "light",
                "color": "green",
                "font_size": 16,
            }
        }