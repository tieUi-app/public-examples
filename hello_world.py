from tieui import TieUi

tie = TieUi(app_name="<YOUR_PROFILE_APP_NAME>")

tie.add(tie.label({"label": "Hello World", "variant": "h6", "color": "black"}))

tie.publish()
