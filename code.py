# Initial Data

json_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]


# Function to calculate BMI
def BMI_calculator(weight, height):
    return  (weight/(height/100)**2)

# Function to figure out BMI Category
def BMI_Category(BMI):
    if BMI <=18.4:
        return "Underweight"

    elif 18.5<= BMI <=24.9:
        return "Normal Weight"

    elif 25<= BMI <= 29.9:
        return "Overweight"
    
    elif 30 <= BMI <= 34.9:
        return "Moderately Obese"

    elif 35 <= BMI <= 39.9:
        return "Severely Obese"

    else:
        return "Very Severly Obese"

# Function to figure out Health Risk
def BMI_health_risk(BMICategory):
    if BMICategory == "Underweight":
        return "Malnutrition Risk"

    elif BMICategory == "Normal Weight":
        return "Low Risk"

    elif BMICategory == "Overweight":
        return "Enhanced Risk"
    
    elif BMICategory == "Moderately Obese":
        return "Medium Risk"
    
    elif BMICategory == "Severely Obese":
        return "High Risk"

    elif BMICategory == "Very Severely Obese":
        return "Very High Risk"



# code to update data with BMI, BMI Category, Health Risk
for item in json_data:
    item["BMI"] = BMI_calculator(item['WeightKg'],item['HeightCm'])
    item["BMICategory"] = BMI_Category(item["BMI"])
    item["HealthRisk"] = BMI_health_risk(item["BMICategory"])          
    
    
# Function to count overweight 
def obese_counter(json_datapoints):
    counter = 0
    for data in json_datapoints:
        if(data["BMICategory"]=="Overweight"):
            counter =+ 1

    return counter


print(json_data)
print("Number of Obese in List: {}".format(str(obese_counter(json_data))))