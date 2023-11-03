from tieui_module import TieUi

tie = TieUi(app_name="<YOUR_APP_NAME>")

def calculate_u(r, p, n):
    u_values = [p]
    
    for i in range (0 , n):
        u_i = r * u_values[i] * (1 - u_values[i]) #Logistic Map formula
        u_values.append(u_i)
        
    return u_values

def custom_button_callback_handler(item):
    try:
        r = float(text_input_value)
        p = float(text_input_value2)
        n = int(text_input_value3)
        result = calculate_u(r, p, n)
        tie.components[4]['settings']['label'] = "Result: " + str(result[-1])  # I assume you want the last value, change this as needed
    except ValueError:
        tie.components[4]['settings']['label'] = "Invalid input"
    except TypeError:
        tie.components[4]['settings']['label'] = "Error in calculation"
    tie.update()

def handle_text_input_change(item):
    global text_input_value
    new_value = item.get("value", "")
    text_input_value = new_value

def handle_text_input_change2(item):
    global text_input_value2
    new_value = item.get("value", "")
    text_input_value2 = new_value

def handle_text_input_change3(item):
    global text_input_value3
    new_value = item.get("value", "")
    text_input_value3 = new_value

tie.add(tie.textBox({"id": "unique-id-1","label": "A Float R", "variant": "outlined"},handle_text_input_change))
tie.add(tie.textBox({"id": "unique-id-2","label": "Initial Value P", "variant": "outlined"},handle_text_input_change2))
tie.add(tie.textBox({"id": "unique-id-2","label": "Non Negative Integer", "variant": "outlined"},handle_text_input_change3))

tie.add(tie.button({"id": "unique-id-3", "label": "Add Numbers", "variant": "outlined"}, custom_button_callback_handler))
tie.add(tie.label({"label": "Result: ", "variant": "h6", "color": "black"}))

tie.publish()
