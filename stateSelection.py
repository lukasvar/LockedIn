# Dictionary of states with their general characteristics
states_info = {
    "Alabama": {"climate": "warm", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Alaska": {"climate": "cool", "cost_of_living": "high", "salary": "high", "city": "not"},
    "Arizona": {"climate": "warm", "cost_of_living": "low", "salary": "moderate"},
    "Arkansas": {"climate": "warm", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "California": {"climate": "warm", "cost_of_living": "high", "salary": "high"},
    "Colorado": {"climate": "cool", "cost_of_living": "moderate", "salary": "high"},
    "Connecticut": {"climate": "cool", "cost_of_living": "high", "salary": "high"},
    "Delaware": {"climate": "moderate", "cost_of_living": "moderate", "salary": "high", "city": "not"},
    "Florida": {"climate": "warm", "cost_of_living": "moderate", "salary": "moderate"},
    "Georgia": {"climate": "warm", "cost_of_living": "low", "salary": "moderate"},
    "Hawaii": {"climate": "warm", "cost_of_living": "high", "salary": "high"},
    "Idaho": {"climate": "cool", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Illinois": {"climate": "cool", "cost_of_living": "moderate", "salary": "moderate"},
    "Indiana": {"climate": "cool", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Iowa": {"climate": "cool", "cost_of_living": "low", "salary": "moderate"},
    "Kansas": {"climate": "warm", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Kentucky": {"climate": "moderate", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Louisiana": {"climate": "warm", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Maine": {"climate": "cool", "cost_of_living": "high", "salary": "moderate"},
    "Maryland": {"climate": "moderate", "cost_of_living": "high", "salary": "high"},
    "Massachusetts": {"climate": "cool", "cost_of_living": "high", "salary": "high"},
    "Michigan": {"climate": "cool", "cost_of_living": "moderate", "salary": "moderate"},
    "Minnesota": {"climate": "cool", "cost_of_living": "moderate", "salary": "moderate", "city": "not"},
    "Mississippi": {"climate": "warm", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Missouri": {"climate": "moderate", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Montana": {"climate": "cool", "cost_of_living": "moderate", "salary": "moderate", "city": "not"},
    "Nebraska": {"climate": "cool", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Nevada": {"climate": "warm", "cost_of_living": "moderate", "salary": "moderate"},
    "New Hampshire": {"climate": "cool", "cost_of_living": "high", "salary": "high"},
    "New Jersey": {"climate": "moderate", "cost_of_living": "high", "salary": "high"},
    "New Mexico": {"climate": "warm", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "New York": {"climate": "cool", "cost_of_living": "high", "salary": "high"},
    "North Carolina": {"climate": "warm", "cost_of_living": "moderate", "salary": "moderate"},
    "North Dakota": {"climate": "cool", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Ohio": {"climate": "cool", "cost_of_living": "low", "salary": "moderate"},
    "Oklahoma": {"climate": "warm", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Oregon": {"climate": "cool", "cost_of_living": "high", "salary": "high"},
    "Pennsylvania": {"climate": "moderate", "cost_of_living": "moderate", "salary": "moderate"},
    "Rhode Island": {"climate": "moderate", "cost_of_living": "high", "salary": "high"},
    "South Carolina": {"climate": "warm", "cost_of_living": "moderate", "salary": "moderate", "city": "not"},
    "South Dakota": {"climate": "cool", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Tennessee": {"climate": "warm", "cost_of_living": "low", "salary": "moderate"},
    "Texas": {"climate": "warm", "cost_of_living": "low", "salary": "moderate"},
    "Utah": {"climate": "cool", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Vermont": {"climate": "cool", "cost_of_living": "high", "salary": "moderate", "city": "not"},
    "Virginia": {"climate": "moderate", "cost_of_living": "moderate", "salary": "high"},
    "Washington": {"climate": "cool", "cost_of_living": "high", "salary": "high"},
    "West Virginia": {"climate": "moderate", "cost_of_living": "low", "salary": "moderate", "city": "not"},
    "Wisconsin": {"climate": "cool", "cost_of_living": "moderate", "salary": "moderate"},
    "Wyoming": {"climate": "cool", "cost_of_living": "low", "salary": "moderate", "city": "not"},
}

def get_state_recommendation():
    print("Welcome! Let's find the best state for you to work in.")
    
    # Questions to gather preferences
    climate = input("Do you prefer a warmer climate or cooler climate? (warm/cool): ").strip().lower()
    cost_of_living = input("Do you prefer a low cost of living or are you okay with higher costs? (low/high): ").strip().lower()
    salary_expectations = input("Do you expect a higher salary or is a moderate salary acceptable? (high/moderate): ").strip().lower()
    proximity_to_city = input("How important living in a city? (very/neutral/not): ").strip().lower()
    
    # Filter the states based on the user's preferences
    recommended_states = []
    
    for state, info in states_info.items():
        match = True
        if climate != info["climate"] and climate != "moderate":
            match = False
        if cost_of_living != info["cost_of_living"] and cost_of_living != "moderate":
            match = False
        if salary_expectations != info["salary"] and salary_expectations != "moderate":
            match = False
        if proximity_to_city == "very" and "city" not in info:
            match = False

        if match:
            recommended_states.append(state)
    
    # Ensure at least one state is returned
    if not recommended_states:
        # If no match, return a random state as fallback
        recommended_states = [list(states_info.keys())[45]]  

    # Provide the final recommended state
    return(recommended_states[0])
# Run the function to get the recommendation