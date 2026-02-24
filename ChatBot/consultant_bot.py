from engine.simulator import predict_sales

def business_chat(query, marketing=None, employees=None, time=None):

    # Step 1: Get prediction from simulator
    marketing = marketing or 30000
    employees = employees or 20
    time = time or 30
    prediction = predict_sales(marketing, employees, time)

    # Step 2: AI Explanation
    explanation = f"""
Based on:

• Marketing Spend: {marketing}
• Employees: {employees}
• Time: {time} days

Predicted Sales: {prediction["Predicted Sales"]}
Growth Rate: {prediction["Growth Rate"]}%
Risk Level: {prediction["Risk Level"]}
"""

    # Step 3: Strategic Advice
    advice = []

    if marketing < 60000:
        advice.append("Increase marketing for better growth")
    else:
        advice.append("Marketing spend is sufficient")

    if employees < 15:
        advice.append("Hiring more staff may improve operations")
    else:
        advice.append("Workforce size is stable")

    if time < 30:
        advice.append("Longer planning horizon can boost impact")

    return {
        "AI Explanation": explanation,
        "Strategic Advice": advice
    }