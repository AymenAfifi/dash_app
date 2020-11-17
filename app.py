from flask import Flask, request, make_response
import base64
import dash
import pathlib
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc
import flask 
from flask import request
import numpy as np
import random
from flask import Flask, send_from_directory
import shutil
import os
import sys
import cv2



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
server = Flask(__name__)
app = dash.Dash(server=server,suppress_callback_exceptions=True,external_stylesheets=external_stylesheets)


app.layout = html.Div(
    style={"height": "100%"},
    children=[
        
        html.Div(
            className="container",
            style={"padding": "35px 25px"},
            children=[
                          html.Div([        html.H3("Choose the number of balls "),
                                            dcc.Dropdown(
                                                id="ball_number",
                                                options=[
                                                    {
                                                        "label": "0",
                                                        "value": "0",
                                                    },
                                                    {
                                                        "label": "1",
                                                        "value": "1",
                                                    },
                                                    {
                                                        "label": "2",
                                                        "value": "2",
                                                    },
                                                    {
                                                        "label": "3",
                                                        "value": "3",
                                                    },
                                                    {
                                                        "label": "4",
                                                        "value": "4",
                                                    },
                                                    {
                                                        "label": "5",
                                                        "value": "5",
                                                    },
                                                    {
                                                        "label": "6",
                                                        "value": "6",
                                                    },
                                                    {
                                                        "label": "7",
                                                        "value": "7",
                                                    },
                                                    {
                                                        "label": "8",
                                                        "value": "8",
                                                    },
                                                        {
                                                        "label": "9",
                                                        "value": "9",
                                                    },
                                                    {
                                                        "label": "10",
                                                        "value": "10",
                                                    },
                                                    {
                                                        "label": "11",
                                                        "value": "11",
                                                    },
                                                    {
                                                        "label": "12",
                                                        "value": "12",
                                                    },
                                                    {
                                                        "label": "13",
                                                        "value": "13",
                                                    },
                                                    {
                                                        "label": "14",
                                                        "value": "14",
                                                    },
                                                    {
                                                        "label": "15",
                                                        "value": "15",
                                                    },
                                                    {
                                                        "label": "16",
                                                        "value": "16",
                                                    },
                                                    
                                                ],
                                                
                                                clearable=False,
                                                placeholder="Select a number",
                                                searchable=False,
                                                )],
                                            className="six columns dropdown-box-second",
                                   ),
                                        html.H3("Choose the color of the balls "),
                                        html.Div(
                                            dcc.Dropdown(
                                                id="ball_color",
                                                options=[
                                                    {
                                                        "label": "Red",
                                                        "value": "0",
                                                    },
                                                    {
                                                        "label": "Orange",
                                                        "value": "1",
                                                    },
                                                    {
                                                        "label": "Yellow",
                                                        "value": "2",
                                                    },
                                                    {
                                                        "label": "Green",
                                                        "value": "3",
                                                    },
                                                    {
                                                        "label": "Blue",
                                                        "value": "4",
                                                    },
                                                    {
                                                        "label": "Indigo",
                                                        "value": "5",
                                                    },
                                                    {
                                                        "label": "Violet",
                                                        "value": "6",
                                                    },
                                                ],
                                                
                                                placeholder="Select a color",
                                                clearable=False,
                                                searchable=False,
                                            ),
                                            className="six columns dropdown-box-second",
                                        ),
                                html.Hr(),
                                       
                html.Hr(),
                
                                       html.Div(className="container",id="img_recp", children=[]),
                                    ],
                                ),
       
        
                           
                
               
          
        
    ],
)

@app.callback(
    Output("img_recp", "children"),
    [
        Input("ball_number", "value"),
        Input("ball_color", "value"),
        
    ],
)
def img_show(x,x1):
    if x and x1 is not None:


        
        x=int(x)
    
        x1=int(x1) 
             
        
    
        
        def newjar3(x,x1,imgpath):
            s
            img = cv2.imread(imgpath)
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            radius = 28
            thickness = -1
            liste2=[(0,0,255),(0,127,255),
        
                      (0,255,255),
                        (0,255,0), 
                        (255,0,0),
                        (50,0,15),
                       (255,0,127)]
            liste1=[(45, 420), 
                         (110, 420), 
                           (175, 420), 
                         (240, 420), 
                           (45, 340) , 
                         (110, 340), 
                         (175, 340),
                         (240, 340),
                         (45, 265),
                         (110, 265),
                         (175, 265),
                        (240, 265),
                         (45, 190),
                         (110, 190),
                           (175, 190),
                         (240, 190)]
             
            color=liste2[x1]   
            i=0
            itr=iter(liste1)
            while i<x:
                
                cv2.circle(img, next(itr), radius, color, thickness)
                i=i+1

            imgpath2 = app.get_asset_url('newimg.png')
            return cv2.imwrite(imgpath2, img)
        imgpath=app.get_asset_url('jar2.jpg')
        newjar3(x,x1,imgpath)
        image_filename = app.get_asset_url('jar2.jpg')
        encoded_image = base64.b64encode(open(image_filename, 'rb').read())
        return html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))




# Running the server
if __name__ == "__main__":
    app.run_server(debug=True)

