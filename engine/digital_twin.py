from engine.simulator import predict_sales

def run_simulation(scenario_a, scenario_b):
    
    result_a = predict_sales(
        scenario_a["marketing"],
        scenario_a["employees"],
        scenario_a["time"]
    )
    
    result_b = predict_sales(
        scenario_b["marketing"],
        scenario_b["employees"],
        scenario_b["time"]
    )
    
    comparison = {
        "Scenario A Sales": result_a,
        "Scenario B Sales": result_b,
        "Better Option": "A" if result_a > result_b else "B"
    }
    
    return comparison