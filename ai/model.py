from pydantic import BaseModel


class GrammarRequest(BaseModel):
    text: str

class GrammarResponse(BaseModel):
    original_text: str
    corrected_text: str

class HtmlRequest(BaseModel):
    text: str

class HtmlResponse(BaseModel):
    given_text: str
    html_text: str

class DashboardRequest(BaseModel):
    kpis: dict


class DashboardResponse(BaseModel):
    success: bool
    dashboard: dict

