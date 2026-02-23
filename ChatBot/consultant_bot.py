from engine.simulator import predict_sales
from engine.automation import analyze_decision
from GenAi.insight_engine import generate_insight

def business_chat(marketing, employees, time):

    sales = predict_sales(marketing, employees, time)

    automation = analyze_decision(sales, marketing, employees)

    insight = generate_insight(marketing, employees, sales)

    response = {
        "Predicted Sales": sales,
        "Risk Level": automation["Risk Level"],
        "Insight": automation["Insight"],
        "Suggested Action": automation["Suggested Action"],
        "AI Explanation": insight["Explanation"],
        "Growth Insight": insight["Growth Insight"],
        "Strategic Advice": insight["Strategic Advice"]
    }

    return response

if __name__ == "__main__":
    
    test = business_chat(
        marketing=50000,
        employees=20,
        time=30
    )

    print("\n--- AI Business Consultant Output ---\n")
    for key, value in test.items():
        print(f"{key}: {value}")