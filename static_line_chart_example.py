
from tieui import TieUi

tie = TieUi(app_name="APP_NAME")

y_data =  [11,12,90,78,33,55,90]
x_data = [0,1,2,3,4,5,6,7,8]

line_chart_settings = {
    "title": "Moisture Sensor Data Over Time",
    "chartSeries": [
        {"name": "Moisture Level", "data": y_data, "color": "#0077B6", 'categories': x_data },
    ],
    "categories": x_data
}
line_chart_component = tie.lineChart(line_chart_settings)
tie.add(line_chart_component)

tie.publish()
