import os
import dash
from dash import html
from dash.dependencies import Input, Output
#from dash_google_oauth.google_auth import GoogleAuth

#import google.auth
#import googleapiclient.discovery

from dotenv import load_dotenv

load_dotenv()

# Set up the Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"],
)

#auth = GoogleAuth(app)

# Define the app layout
app.layout = html.Div([
    html.Button(id="button", children="Access Google Drive"),
    html.Div(id="output")
])

if __name__ == "__main__":
    app.run_server(debug=True)

