def analyze_decision(predicted_sales, marketing, employees):
    
    insight = ""
    risk = ""
    suggestion = ""
    
    # Risk Logic
    if marketing > 80000 and employees < 10:
        risk = "High Risk"
        insight = "High marketing without workforce may cause operational stress."
        suggestion = "Consider hiring more employees."
        
    elif employees > 80 and marketing < 20000:
        risk = "Medium Risk"
        insight = "Workforce heavy but low marketing may reduce growth."
        suggestion = "Increase marketing investment."
        
    elif marketing > 60000 and employees > 50:
        risk = "Low Risk"
        insight = "Balanced growth strategy detected."
        suggestion = "Proceed with confidence."
        
    else:
        risk = "Moderate Risk"
        insight = "Growth possible but may need strategic alignment."
        suggestion = "Adjust marketing or workforce for optimization."
    
    return {
        "Predicted Sales": predicted_sales,
        "Risk Level": risk,
        "Insight": insight,
        "Suggested Action": suggestion
    }