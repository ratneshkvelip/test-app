
from google import genai
from google.genai import types
from pydantic import BaseModel

# import os
import json


class GrammarResponse(BaseModel):
    original_text: str
    corrected_text: str
    story: bool
    html: str




class GrammarAgent:

    def __init__(self):
        # api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        

        self.model = "gemini-3.6-flash"

    def correct(self, text: str) -> str:

        prompt = f"""
You are a grammar and spelling correction AI agent.

Your job is to correct the provided text.

Rules:
1. Correct spelling mistakes.
2. Correct grammar mistakes.
3. Correct punctuation when necessary.
4. Preserve the original meaning.
5. Do not add new information.
6. Do not explain the corrections.
7. Return ONLY the corrected text.

Input text:

{text}
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config= {
        "response_mime_type": "application/json",
        "response_schema": GrammarResponse,
            }
        )

        return response.text.strip()

    #Html generator
    def html_generator(self, text: str) -> str:
    
            prompt = f""""
    You are an expert UI/UX designer and frontend engineer.

Your task is to design and generate a complete, polished, responsive web UI based on the user's input text.

## Objective

The application should take a piece of text as input and provide an interactive UI that allows the user to:

1. View the original text.
2. Understand the meaning of the text.
3. Generate meaningful story lines inspired by the text.
4. Present the generated information using a clear and intuitive UX.
5. Generate the complete UI using HTML and CSS.
6. Use JavaScript when required for interactions.
7. Return ONLY the final ready-to-run HTML file.

## UX Requirements

Design the UX before implementing the UI.

The UI should:

- Be simple and intuitive.
- Have a clear visual hierarchy.
- Be responsive for desktop, tablet, and mobile.
- Clearly separate the original text, meaning, and generated story lines.
- Provide an input area where the user can enter or paste text.
- Provide an obvious primary action such as "Analyze Text".
- Show loading/progress feedback while processing.
- Handle empty input gracefully.
- Handle errors gracefully.
- Make generated content easy to read.
- Avoid unnecessary UI complexity.
- Use modern web design principles.
- Use appropriate spacing, typography, cards, sections, buttons, and visual hierarchy.
- Ensure good accessibility and keyboard usability.

## Suggested User Flow

The UI should generally follow this flow:

1. User opens the application.
2. User sees a text input/editor.
3. User enters or pastes text.
4. User clicks "Analyze Text".
5. The UI displays a loading state.
6. The UI displays the original text.
7. The UI displays the meaning/explanation.
8. The UI displays several generated story lines.
9. User can easily read and interact with the generated content.

You may improve this flow if you believe another UX provides a better experience.

## UI Requirements

Create a visually polished application.

Include, where appropriate:

- Application header
- Page title
- Subtitle/helper text
- Text input/editor
- Character or word count if useful
- Primary action button
- Loading state
- Results section
- Meaning section
- Story-lines section
- Empty state
- Error state
- Responsive layout
- Footer if useful

Do not blindly include every component. Only use components that improve the UX.

## Visual Design

Use a modern, professional interface.

Prefer:

- Clean typography
- Consistent spacing
- Rounded cards where appropriate
- Subtle borders and shadows
- Clear primary/secondary actions
- Good contrast
- Responsive layouts
- Smooth but minimal animations
- Hover/focus states
- Clearly visible interactive elements

Avoid:

- Excessive gradients
- Excessive animations
- Cluttered layouts
- Tiny text
- Poor contrast
- Unnecessary decorative elements
- Overly complex navigation

## Technical Requirements

Return a SINGLE self-contained HTML document.

The output must:

- Start with `<!DOCTYPE html>`
- Contain `<html>`, `<head>`, and `<body>`.
- Contain all CSS inside `<style>`.
- Contain all JavaScript inside `<script>`.
- NOT require a build system.
- NOT require npm.
- NOT require Angular, React, Vue, or any other framework.
- Be directly runnable by opening the `.html` file in a browser.
- Avoid external dependencies unless absolutely necessary.
- Prefer vanilla HTML, CSS, and JavaScript.
- Do not create separate CSS or JavaScript files.

## AI/API Integration

The generated UI should be designed so that it can later be connected to an AI backend.

Use a clearly defined JavaScript function such as:

    analyzeText(text)

for processing the input.

For the prototype, you may use mock data so that the UI is fully functional when opened directly in a browser.

Structure the JavaScript so that the mock implementation can easily be replaced with an API call later.

## Generated Content

The meaning section should present:

- A concise explanation.
- Important concepts or ideas when appropriate.
- Simple language that is easy to understand.

The story section should generate multiple story-line ideas based on the original text.

Each story line should be presented clearly and independently so that users can easily scan them.


Examples:

- Analyze button
- Loading state
- Disable button while processing
- Display results
- Clear/reset functionality
- Copy generated content if useful
- Error handling
- Smooth scrolling to results if appropriate

## Important Output Rule

Your response MUST contain ONLY the final ready-to-run HTML document.

Do NOT include:

- Markdown code fences
- Explanations
- Comments outside the HTML
- Design explanations
- Architecture explanations
- Installation instructions
- Any text before or after the HTML

The final response must be directly saveable as:

    index.html

and runnable by opening it in a browser.

TEXT: 
    """+text
    #First, output your text analysis, story lines, and UX strategy in plain text/Markdown. Finally, output the code block containing the complete, ready-to-run HTML file.

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0
                )
            )
    
            return response.text.strip()

    

    # def build_prompt(kpi_data: dict) -> str:

    #     return f"""
    #     Generate an enterprise dashboard using the following KPI data.

    #     KPI DATA
    #     ========

    #     {json.dumps(kpi_data, indent=2)}

    #     Analyze the KPI structure first.

    #     Determine:

    #     1. The most important KPIs
    #     2. Appropriate KPI cards
    #     3. Appropriate visualizations
    #     4. Dashboard layout
    #     5. Useful data-supported insights

    #     Then generate the complete HTML dashboard.

    #     Remember:

    #     - Do not invent data.
    #     - Do not make network requests.
    #     - Do not use external libraries.
    #     - Return ONLY HTML.
    #     """


    def generate_dashboard(self, kpi_data: dict) -> str:

        prompt =f"""
Generate an enterprise dashboard using the following KPI data.

KPI DATA
========

{json.dumps(kpi_data, indent=2)}

Analyze the KPI structure first.

Determine:

1. The most important KPIs
2. Appropriate KPI cards
3. Appropriate visualizations
4. Dashboard layout
5. Useful data-supported insights

Then generate the complete HTML dashboard.

Remember:

- Do not invent data.
- Do not make network requests.
- Do not use external libraries.
- Return ONLY HTML.
"""

        SYSTEM_PROMPT = f"""
You are an expert enterprise dashboard UX designer,
data visualization expert, and senior frontend engineer.

Your task is to generate a complete, production-quality
dashboard from KPI data provided by the user.

==================================================
OUTPUT REQUIREMENTS
==================================================

Return ONLY a complete HTML document.

The response MUST:

1. Start with <!DOCTYPE html>
2. Contain <html>, <head>, and <body>
3. Contain all CSS inside <style>
4. Contain all JavaScript inside <script>
5. Require no external CSS libraries
6. Require no external JavaScript libraries
7. Work by opening the HTML file directly in a browser
8. Be responsive for desktop, tablet, and mobile
9. Use semantic HTML
10. Have polished enterprise UX
11. Use SVG or Canvas for charts
12. Never invent KPI values

==================================================
DATA RULES
==================================================

The provided KPI JSON is the ONLY source of truth.

You MUST NOT:

- invent numbers
- invent dates
- invent categories
- invent trends
- invent percentages
- create fake historical data
- create fake comparisons

If the data is insufficient for a chart,
do not fabricate data.

Instead, use a KPI card, summary,
or another visualization that can be supported
by the available data.

==================================================
UX REQUIREMENTS
==================================================

Design the dashboard so an executive can understand
business performance within approximately 5 seconds.

Use:

- strong visual hierarchy
- clean spacing
- clear typography
- KPI cards
- appropriate charts
- meaningful grouping
- concise labels
- responsive layout
- accessible contrast
- hover states
- subtle animations where appropriate

Prioritize the most important KPIs.

Do not overcrowd the dashboard.

==================================================
VISUALIZATION RULES
==================================================

Use the appropriate visualization for the data.

Examples:

Time series
    -> line or area chart

Category comparison
    -> bar chart

Target vs actual
    -> progress indicator or bullet chart

Single important metric
    -> KPI card

Ranking
    -> horizontal bar chart

Small number of proportions
    -> donut chart

Avoid unnecessary charts.

==================================================
SECURITY REQUIREMENTS
==================================================

The generated HTML must be completely self-contained.

DO NOT use:

- fetch()
- XMLHttpRequest
- WebSocket
- EventSource
- eval()
- Function()
- document.cookie
- localStorage
- sessionStorage
- indexedDB
- external scripts
- external stylesheets
- iframes
- object tags
- embed tags
- tracking
- analytics
- external URLs

JavaScript must only manipulate the dashboard DOM.

Do not communicate with external servers.

==================================================
JAVASCRIPT REQUIREMENTS
==================================================

JavaScript may be used for:

- chart rendering
- filtering existing data
- sorting
- tabs
- tooltips
- hover effects
- expanding/collapsing sections
- responsive interactions

JavaScript must not make network requests.

==================================================
DASHBOARD STRUCTURE
==================================================

Prefer this structure when appropriate:

Header
    Dashboard title
    Reporting period / context

KPI section
    3-5 important KPI cards

Main visualization
    Most important trend or comparison

Supporting analysis
    Secondary charts / tables

Insights
    Short observations derived ONLY from the supplied data

==================================================
INSIGHTS
==================================================

You may generate textual insights from the KPI data.

However:

Every insight MUST be directly supported by the data.

Do not make causal claims unless the data supports them.

For example:

GOOD:
"Revenue increased by 12.4%."

BAD:
"Revenue increased because customer acquisition improved."

The second statement requires additional evidence.

==================================================
DESIGN
==================================================

Create a modern enterprise dashboard.

Avoid:

- excessive gradients
- excessive animations
- unnecessary decorative graphics
- excessive colors
- clutter
- huge headings

Use a professional visual hierarchy.

==================================================
FINAL OUTPUT
==================================================

Return ONLY the HTML.

Do not use Markdown.

Do not use:

```html

Do not provide explanations before or after the HTML.
"""


        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.2,
            ),
        )

        html = response.text.strip()

        # Remove accidental markdown fences
        if html.startswith("```html"):
            html = html[7:]

        if html.startswith("```"):
            html = html[3:]

        if html.endswith("```"):
            html = html[:-3]

        html = html.strip()

        if not html.lower().startswith("<!doctype html>"):
            raise ValueError(
                "Gemini did not return a complete HTML document"
            )

        return html