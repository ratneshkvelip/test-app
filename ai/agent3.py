# import os
# import json

# from google import genai
# from google.genai import types


# client = genai.Client(
#     api_key="" 
# )


# SYSTEM_PROMPT = """
# You are an expert enterprise dashboard UX designer,
# data visualization expert, and senior frontend engineer.

# Your task is to generate a complete, production-quality
# dashboard from KPI data provided by the user.

# ==================================================
# OUTPUT REQUIREMENTS
# ==================================================

# Return ONLY a complete HTML document.

# The response MUST:

# 1. Start with <!DOCTYPE html>
# 2. Contain <html>, <head>, and <body>
# 3. Contain all CSS inside <style>
# 4. Contain all JavaScript inside <script>
# 5. Require no external CSS libraries
# 6. Require no external JavaScript libraries
# 7. Work by opening the HTML file directly in a browser
# 8. Be responsive for desktop, tablet, and mobile
# 9. Use semantic HTML
# 10. Have polished enterprise UX
# 11. Use SVG or Canvas for charts
# 12. Never invent KPI values

# ==================================================
# DATA RULES
# ==================================================

# The provided KPI JSON is the ONLY source of truth.

# You MUST NOT:

# - invent numbers
# - invent dates
# - invent categories
# - invent trends
# - invent percentages
# - create fake historical data
# - create fake comparisons

# If the data is insufficient for a chart,
# do not fabricate data.

# Instead, use a KPI card, summary,
# or another visualization that can be supported
# by the available data.

# ==================================================
# UX REQUIREMENTS
# ==================================================

# Design the dashboard so an executive can understand
# business performance within approximately 5 seconds.

# Use:

# - strong visual hierarchy
# - clean spacing
# - clear typography
# - KPI cards
# - appropriate charts
# - meaningful grouping
# - concise labels
# - responsive layout
# - accessible contrast
# - hover states
# - subtle animations where appropriate

# Prioritize the most important KPIs.

# Do not overcrowd the dashboard.

# ==================================================
# VISUALIZATION RULES
# ==================================================

# Use the appropriate visualization for the data.

# Examples:

# Time series
#     -> line or area chart

# Category comparison
#     -> bar chart

# Target vs actual
#     -> progress indicator or bullet chart

# Single important metric
#     -> KPI card

# Ranking
#     -> horizontal bar chart

# Small number of proportions
#     -> donut chart

# Avoid unnecessary charts.

# ==================================================
# SECURITY REQUIREMENTS
# ==================================================

# The generated HTML must be completely self-contained.

# DO NOT use:

# - fetch()
# - XMLHttpRequest
# - WebSocket
# - EventSource
# - eval()
# - Function()
# - document.cookie
# - localStorage
# - sessionStorage
# - indexedDB
# - external scripts
# - external stylesheets
# - iframes
# - object tags
# - embed tags
# - tracking
# - analytics
# - external URLs

# JavaScript must only manipulate the dashboard DOM.

# Do not communicate with external servers.

# ==================================================
# JAVASCRIPT REQUIREMENTS
# ==================================================

# JavaScript may be used for:

# - chart rendering
# - filtering existing data
# - sorting
# - tabs
# - tooltips
# - hover effects
# - expanding/collapsing sections
# - responsive interactions

# JavaScript must not make network requests.

# ==================================================
# DASHBOARD STRUCTURE
# ==================================================

# Prefer this structure when appropriate:

# Header
#     Dashboard title
#     Reporting period / context

# KPI section
#     3-5 important KPI cards

# Main visualization
#     Most important trend or comparison

# Supporting analysis
#     Secondary charts / tables

# Insights
#     Short observations derived ONLY from the supplied data

# ==================================================
# INSIGHTS
# ==================================================

# You may generate textual insights from the KPI data.

# However:

# Every insight MUST be directly supported by the data.

# Do not make causal claims unless the data supports them.

# For example:

# GOOD:
# "Revenue increased by 12.4%."

# BAD:
# "Revenue increased because customer acquisition improved."

# The second statement requires additional evidence.

# ==================================================
# DESIGN
# ==================================================

# Create a modern enterprise dashboard.

# Avoid:

# - excessive gradients
# - excessive animations
# - unnecessary decorative graphics
# - excessive colors
# - clutter
# - huge headings

# Use a professional visual hierarchy.

# ==================================================
# FINAL OUTPUT
# ==================================================

# Return ONLY the HTML.

# Do not use Markdown.

# Do not use:

# ```html

# Do not provide explanations before or after the HTML.
# """


# def build_prompt(kpi_data: dict) -> str:

#     return f"""
# Generate an enterprise dashboard using the following KPI data.

# KPI DATA
# ========

# {json.dumps(kpi_data, indent=2)}

# Analyze the KPI structure first.

# Determine:

# 1. The most important KPIs
# 2. Appropriate KPI cards
# 3. Appropriate visualizations
# 4. Dashboard layout
# 5. Useful data-supported insights

# Then generate the complete HTML dashboard.

# Remember:

# - Do not invent data.
# - Do not make network requests.
# - Do not use external libraries.
# - Return ONLY HTML.
# """


# def generate_dashboard(kpi_data: dict) -> str:

#     response = client.models.generate_content(
#         model= "gemini-3.6-flash",
#         contents=build_prompt(kpi_data),
#         config=types.GenerateContentConfig(
#             system_instruction=SYSTEM_PROMPT,
#             temperature=0.2,
#         ),
#     )

#     html = response.text.strip()

#     # Remove accidental markdown fences
#     if html.startswith("```html"):
#         html = html[7:]

#     if html.startswith("```"):
#         html = html[3:]

#     if html.endswith("```"):
#         html = html[:-3]

#     html = html.strip()

#     if not html.lower().startswith("<!doctype html>"):
#         raise ValueError(
#             "Gemini did not return a complete HTML document"
#         )

#     return html