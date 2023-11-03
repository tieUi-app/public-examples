from tieui import TieUi
import requests

tie = TieUi(app_name="<YOUR_APP_NAME>")

def get_historical_data(stock_symbol, interval, period):
    url = f"https://yahoo-finance127.p.rapidapi.com/historic/{stock_symbol}/{interval}/{period}"

    headers = {
        "X-RapidAPI-Key": "<YOUR_API_KEY>",
        "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def handle_text_input_stock_symbol(item):
    global stock_symbol
    stock_symbol = item.get("value", "")

def handle_button_click(item):
    interval = "1d"
    period = "15d"
    
    data = get_historical_data(stock_symbol, interval, period)
    
    if data is not None:
        timestamps = data.get("timestamp", [])
        close_prices = data["indicators"]["quote"][0]["close"]
        
        # Create data for the line chart
        chart_data = [{"x": i + 1, "y": price} for i, price in enumerate(close_prices)]
        
        # Update the line chart with the data
        tie.components[3]['settings']['chartSeries'][0]['data'] = chart_data
        
        tie.update()
    else:
        tie.components[2]['settings']['label'] = f"Stock {stock_symbol} not found or an error occurred."
        tie.update()

def main():
    global stock_symbol
    stock_symbol = ""
    
    tie.add(tie.textBox({"id": "stock-symbol", "label": "Stock Symbol", "variant": "outlined"}, handle_text_input_stock_symbol))
    tie.add(tie.button({"id": "submit-button", "label": "Get Data", "variant": "outlined"}, handle_button_click))
    tie.add(tie.label({"label": "", "variant": "h6", "color": "black"}))  # Placeholder for output text
    
    line_chart_settings = {
        "title": "Stock Prices Over Time",
        "chartSeries": [{
            "name": "p1", "data": [], "color": "#8b2E62" 
        }],
    }
    tie.add(tie.lineChart(line_chart_settings))
    
    tie.publish()

if __name__ == "__main__":
    main()
