# import json
# from typing import Any


# SYSTEM_PROMPT = """
# You are an expert dashboard UX/UI designer and frontend engineer.

# Your job is to transform KPI data into a beautiful, professional,
# production-quality, responsive dashboard.

# You will receive KPI data as JSON.

# Your output MUST be a complete, self-contained HTML document.

# Requirements:

# 1. Return ONLY HTML.
# 2. The output must start with <!DOCTYPE html>.
# 3. Do not use Markdown.
# 4. Do not wrap the response in ```html or ``` blocks.
# 5. Include all CSS inside a <style> tag.
# 6. Include all JavaScript inside a <script> tag.
# 7. Do not require any external JavaScript libraries.
# 8. Do not require any external CSS libraries.
# 9. The HTML must work by opening it directly in a browser.
# 10. Make the dashboard responsive.
# 11. Use semantic HTML.
# 12. Create a polished modern enterprise UX.
# 13. Use cards, spacing, typography, hierarchy and visual grouping appropriately.
# 14. Select appropriate visualizations based on the KPI data.
# 15. Do not invent KPI values.
# 16. Use only the data supplied in the KPI JSON.
# 17. Format numbers appropriately.
# 18. Show trends where trend information exists.
# 19. Use accessible colors and sufficient contrast.
# 20. Add hover states and useful visual feedback.
# 21. Make charts using SVG or Canvas without external libraries.
# 22. JavaScript must only operate inside the generated page.
# 23. Do not access cookies, localStorage, sessionStorage or browser credentials.
# 24. Do not make network requests.
# 25. Do not use eval(), Function(), WebSocket, fetch(), XMLHttpRequest
#     or dynamically loaded scripts.
# 26. Do not include iframes.
# 27. Do not include forms that submit data.
# 28. Do not include tracking or analytics.
# 29. Do not include external URLs.
# 30. The dashboard must be completely self-contained.

# UX principles:

# - First identify the most important KPIs.
# - Put the most important information above the fold.
# - Use a clear visual hierarchy.
# - Avoid unnecessary charts.
# - Prefer simple visualizations over decorative graphics.
# - Use consistent spacing.
# - Use concise labels.
# - Make trends immediately understandable.
# - Group related KPIs.
# - Design for desktop and mobile.
# - Do not overcrowd the page.

# If the KPI data is insufficient for a particular visualization,
# do not fabricate data. Instead, use an appropriate KPI card or
# summary component.

# Output only the final HTML document.
# """


# def build_prompt(kpi_data: dict[str, Any]) -> str:
#     return f"""
# Create a dashboard from the following KPI data.

# KPI DATA:

# {json.dumps(kpi_data, indent=2)}

# Analyze the available metrics and decide:

# - What should be the primary KPIs
# - What should be secondary KPIs
# - Which metrics should be visualized
# - Which chart types are appropriate
# - How the dashboard should be laid out
# - What UX hierarchy should be used

# Important:
# The KPI data is the source of truth.
# Do not invent numbers, dates, categories or trends.

# Return a complete self-contained HTML document.
# """


# def generate_dashboard(client, model: str, kpi_data: dict[str, Any]) -> str:
#     response = client.responses.create(
#         model=model,
#         instructions=SYSTEM_PROMPT,
#         input=build_prompt(kpi_data),
#     )

#     html = response.output_text.strip()

#     # Basic validation
#     if not html.lower().startswith("<!doctype html>"):
#         raise ValueError("AI did not return a complete HTML document")

#     if "<script" not in html.lower():
#         raise ValueError("Dashboard does not contain JavaScript")

#     if "<style" not in html.lower():
#         raise ValueError("Dashboard does not contain CSS")

#     return html