
from tieui import TieUi

tie = TieUi(app_name="<YOUR_APP_NAME>")

chartSeries = [
  {
    "name": "Series 1",
    "data": [10, 41, 35, 51, 49, 62, 69, 91, 148],
  },
]

categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']


bar_chart_settings = {
    "title": "Moisture Sensor Data Over Time",
    "chartSeries": chartSeries,
    "categories": categories,
    "syncButtonLabel": "Sync Data",
    "overviewButtonLabel": "View Overview"
}
line_chart_component = tie.barChart(bar_chart_settings)
tie.add(line_chart_component)

tie.publish()
