from fastapi import FastAPI, HTTPException

from agent import GrammarAgent
from model import DashboardRequest, DashboardResponse, GrammarRequest, GrammarResponse



app = FastAPI(
    title="Grammar AI Agent"
)

agent = GrammarAgent()


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.post(
    "/ai/grammar/correct",
    response_model=GrammarResponse
)
def correct_grammar(
    request: GrammarRequest
):

    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )

    corrected_text = agent.correct(
        request.text
    )

    return GrammarResponse(
        original_text=request.text,
        corrected_text=corrected_text
    )

@app.post(
    "/ai/ux/generatehtml",
    response_model=GrammarResponse
)
def correct_grammar(
    request: GrammarRequest
):

    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )

    corrected_text = agent.html_generator(
        request.text
    )

    return GrammarResponse(
        original_text=request.text,
        corrected_text=corrected_text
    )

@app.post(
    "/ai/generatehtml",
    response_model=DashboardResponse
)
def generate_dashboard_api(
    request: DashboardRequest
):

    try:

        html = agent.generate_dashboard(
            request.kpis
        )

        return {
            "success": True,
            "dashboard": {
                "html": html
            }
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    
# def gen_dashboard(
#     request: DashboardRequest
# ):

#     if not request.text.strip():
#         raise HTTPException(
#             status_code=400,
#             detail="Text cannot be empty"
#         )

#     html = agent.generate_dashboard(
#         request.text
#     )

#     return {
#             "success": True,
#             "dashboard": {
#                 "html": html
#             }
#         }