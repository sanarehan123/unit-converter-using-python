import streamlit as st

st.title("Unit Converter 🧩")

# Conversion Unit
conversion_types = ["Length/Distance", "Mass/Weight", "Volume", "Temperature",
                    "Time", "Speed/Velocity", "Area", "Energy", "Power", "Pressure"]

# For the user to select the conversion type
conversion_choice = st.selectbox("Choose Conversion Type", conversion_types)

# Length/Distance Conversion
if conversion_choice == "Length/Distance":
    length_units = {"Meters": 1, "Kilometers": 1000, "Feet": 0.3048, "Inches": 0.0254, "Centimeters": 0.01}
    input_value = st.number_input("Enter Length/Distance Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", length_units.keys())
    to_unit = st.selectbox("To Unit:", length_units.keys())
    if st.button("Convert"):
        result = input_value * (length_units[from_unit] / length_units[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')

# Mass/Weight Conversion
elif conversion_choice == "Mass/Weight":
    weight_units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495, "Tons": 1000}
    input_value = st.number_input("Enter Mass/Weight Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", weight_units.keys())
    to_unit = st.selectbox("To Unit:", weight_units.keys())
    if st.button("Convert"):
        result = input_value * (weight_units[from_unit] / weight_units[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')

# Volume Conversion
elif conversion_choice == "Volume":
    volume_units = {"Liters": 1, "Milliliters": 0.001, "Gallons": 3.785, "Cups": 0.24, "Pints": 0.473}
    input_value = st.number_input("Enter Volume Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", volume_units.keys())
    to_unit = st.selectbox("To Unit:", volume_units.keys())
    if st.button("Convert"):
        result = input_value * (volume_units[from_unit] / volume_units[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')

# Temperature Conversion
elif conversion_choice == "Temperature":
    input_value = st.number_input("Enter Temperature Value:", format="%.2f")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit:", temp_units)
    to_unit = st.selectbox("To Unit:", temp_units)
    if st.button("Convert"):
        if from_unit == to_unit:
            result = input_value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (input_value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (input_value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = input_value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = input_value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (input_value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (input_value - 273.15) * 9/5 + 32
        st.success(f'{input_value} {from_unit} = {result:.2f} {to_unit}')

# Time Conversion
elif conversion_choice == "Time":
    time_units = {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400, "Weeks": 604800}
    input_value = st.number_input("Enter Time Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", time_units.keys())
    to_unit = st.selectbox("To Unit:", time_units.keys())
    if st.button("Convert"):
        result = input_value * (time_units[from_unit] / time_units[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')

# Speed/Velocity Conversion
elif conversion_choice == "Speed/Velocity":
    speed_units = {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.237, "Knots": 1.944}
    input_value = st.number_input("Enter Speed Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", speed_units.keys())
    to_unit = st.selectbox("To Unit:", speed_units.keys())
    if st.button("Convert"):
        result = input_value * (speed_units[from_unit] / speed_units[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')


# Area Conversion
elif conversion_choice == "Area":
    area_units = {"Square meters": 1, "Square kilometers": 1e6, "Square feet": 0.092903, "Acres": 4046.86, "Hectares": 10000}
    input_value = st.number_input("Enter Area Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", area_units.keys())
    to_unit = st.selectbox("To Unit:", area_units.keys())
    if st.button("Convert"):
        result = input_value * (area_units[from_unit] / area_units[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')

# Energy Conversion
elif conversion_choice == "Energy":
    energy_units = {"Joules": 1, "Kilojoules": 1000, "Calories": 4.184, "Kilowatt-hours": 3.6e6, "BTU": 1055.06}
    input_value = st.number_input("Enter Energy Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", energy_units.keys())
    to_unit = st.selectbox("To Unit:", energy_units.keys())
    if st.button("Convert"):
        result = input_value * (energy_units[from_unit] / energy_units[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')

# Power Conversion
elif conversion_choice == "Power":
    power_units = {"Watts": 1, "Kilowatts": 1000, "Horsepower": 745.7, "BTU per hour": 0.293, "Megawatts": 1e6}
    input_value = st.number_input("Enter Power Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", power_units.keys())
    to_unit = st.selectbox("To Unit:", power_units.keys())
    if st.button("Convert"):
        result = input_value * (power_units[from_unit] / power_units[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')

# Pressure Conversion
elif conversion_choice == "Pressure":
    pressure_units = {"Pascals": 1, "Kilopascals": 1000, "Bars": 1e5, "Atmospheres": 101325, "PSI": 6894.76}
    input_value = st.number_input("Enter Pressure Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", pressure_units.keys())
    to_unit = st.selectbox("To Unit:", pressure_units.keys())
    if st.button("Convert"):
        result = input_value * (pressure_units[from_unit] / pressure_units[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')






