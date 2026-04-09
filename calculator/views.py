from django.shortcuts import render
import math
import re

def home(request):
    result = ""
    expression = ""  # Keep the input visible after calculation

    if request.method == "POST":
        expression = request.POST.get("expression", "")

        try:
            expr = expression

            # Replace symbols with Python operators
            expr = expr.replace('×', '*').replace('÷', '/')

            # Replace squares: 5² → 5**2
            expr = re.sub(r'(\d+|\))²', r'\1**2', expr)

            # Replace percentages: 50% → 50/100
            expr = expr.replace('%', '/100')

            # Replace square roots: √16 → math.sqrt(16)
            expr = re.sub(r'√(\d+(\.\d+)?)', r'math.sqrt(\1)', expr)

            # Handle implicit multiplication:
            # 2(3+4) → 2*(3+4), (2+3)(4+5) → (2+3)*(4+5)
            expr = re.sub(r'(\d|\))\(', r'\1*(', expr)
            expr = re.sub(r'\)(\d|\()', r')*\1', expr)

            # Evaluate safely
            calc = eval(expr)
            result = f"{calc}"

        except Exception:
            result = "Error"

    # Pass both expression and result to template
    return render(request, "index.html", {"result": result, "expression": expression})