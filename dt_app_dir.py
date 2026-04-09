#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------
import re
import requests
#----------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#----------------------------------------
from io import BytesIO, StringIO

# -----------------------------------------------------------------------------
# Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Apps Directory",
                    layout="wide",
                    page_icon="🖥️",            
                    initial_sidebar_state="auto")

# -----------------------------------------------------------------------------
# Custom CSS Styles
# -----------------------------------------------------------------------------

# Define the container style
st.markdown("""
        <style>
        .centered-info {
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 18px;
            color: #007BFF; 
            padding: 5px;
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 20px;
            border: 1px solid #007BFF;
            margin-top: 1px;
            margin-bottom: 20px;
        }
        .banner {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
            border-radius: 20px;
            padding: 15px;
            margin: 25px 0;
            border: 1px solid rgba(0, 86, 179, 0.15);
            text-align: center;
            font-size: 1.25rem;
            color: #0056b3;
            font-weight: 600;
        }
        .app-container {
            padding: 15px;
            font-size: 1.1rem;
            background-color: #effefe;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 15px;
            text-align: center;
            display: flex;
            flex-direction: column;
            height: 100%; /* Ensures uniform height */
            transition: all 0.2s;
        }
        .app-container:hover {
            background-color: #E0CCD3;
            transform: translateY(-2px);
            transition: all 0.2s;
        }
        .app-container a {
            text-decoration: none;
            font-weight: bold;
            color: #0073e6;
            font-size: 1.1em;
            margin-bottom: 10px;
            display: block;
        }
        .app-container a:hover {
            color: #005bb5;
        }
        .app-description {
            font-size: 0.9em;
            color: #555;
            margin-top: 5px;
            line-height: 1.4;
            flex-grow: 1; /* Pushes content to fill space */
        }
        </style>
        """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------
### Description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------

file_id = "1fJ6PrVQHZUmfDdBsrJeFVVZ4E_L6MAp6"
pdf_view_link = f"https://drive.google.com/file/d/{file_id}/preview"

st.markdown(
    """
    <style>
    .title-large {{
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .title-small {{
        text-align: center;
        font-size: 20px;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .version-badge {{
        text-align: center;
        display: inline-flex;
        align-items: center;
        gap: 12px;
        background: linear-gradient(120deg, #0056b3, #0d4a96);
        color: white;
        padding: 2px 14px;
        border-radius: 20px;
        font-size: 1.2rem;
        margin-top: 8px;
        font-weight: 600;
        letter-spacing: 0.3px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
        flex-wrap: wrap;
        justify-content: center;
    }}
    .version-badge a {{
        color: #fff;
        text-decoration: none;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 4px;
        background: rgba(255,255,255,0.15);
        transition: background 0.2s;
    }}
    .version-badge a:hover {{
        background: rgba(255,255,255,0.3);
        text-decoration: underline;
    }}
    .version-badge .email {{
        opacity: 0.95;
        font-family: monospace;
    }}
    </style>
    <div style="text-align: center;">
        <div class="title-large">🖥️ Apps Directory</div>
        <div class="version-badge">
            <span class="email">✉ avijit.mba18@gmail.com</span>
            <span style="opacity:0.7;">|</span>
            <a href="{pdf_view_link}" target="_blank">📄 Resume</a>
        </div>
    </div>
    """.format(pdf_view_link=pdf_view_link),
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .footer {
        position: fixed;left: 0;bottom: 0;width: 100%;background-color: #F0F2F6;text-align: center;
        padding: 10px;font-size: 14px;color: #333;z-index: 100;
    }
    .footer p {
        margin: 0;
    }
    .footer .highlight {
        font-weight: bold;color: blue;
    }
    </style>
    <div class="footer">
        <p>© 2026 | Created by : <span class="highlight">Avijit Chakraborty</span> <a href="mailto:avijit.mba18@gmail.com"> 📩 </a> | <span class="highlight">Thank you for visiting the app | Unauthorized uses or copying is strictly prohibited | For best view of the app, please zoom out the browser to 75%.</span> </p>
    </div>
    """,
    unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------
### Connections
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------
#st.write(" ")
st.markdown('<div class="centered-info"><span style="margin-left: 10px;">Click the cards below to access different sections and explore the following features</span></div>',unsafe_allow_html=True,)
#---------------------------------------------------------------------------------------------------------------------------------

apps = [
            {
                "name": "Knowledge DataBase", 
                "url": "https://dl-kdb.streamlit.app/",
                "description": "A comprehensive database for storing and accessing knowledge, with advanced search and categorization features."
            },
            {
                "name": "Machine Learning CookBook", 
                "url": "https://machine-learning-cookbook.streamlit.app/",
                "description": "A collection of machine learning recipes and code snippets to help you solve common ML tasks quickly."
            },        
            {
                "name": "Machine Learning (ML) Studio", 
                "url": "https://ml-studio.streamlit.app/",
                "description": "An interactive platform for experimenting with various machine learning models and algorithms."
            },
            {
                "name": "Forecasting Studio", 
                "url": "https://ts-app.streamlit.app/",
                "description": "A tool for time series forecasting, helping you predict future trends based on historical data."
            },   
            {
                "name": "Anomaly Detection App", 
                "url": "https://anomaly-det.streamlit.app/",
                "description": "An app designed to detect anomalies in datasets, useful for identifying outliers and unusual patterns."
            },          
            {
                "name": "Digi-e | Digital & Analytical & Generative AI Playground", 
                "url": "https://genai-playground.streamlit.app/",
                "description": "A playground for experimenting with digital & generative AI models, allowing you to play with digital documents & create genai applications"
            },
            {
                "name": "PDF Playground", 
                "url": "https://pdf-playground.streamlit.app/",
                "description": "An easy-to-use, open-source PDF application to preview and extract content and metadata from PDFs, add or remove passwords, modify, merge, convert and compress PDFs."
            },    
            {
                "name": "Image Playground", 
                "url": "https://image-playground.streamlit.app/",
                "description": "A lightweight image-processing streamlit app that supports the following operations: upload image,crop,remove background,mirror,convert,rotate,change brightness."
            },   
            {
                "name": "Statistics Playground", 
                "url": "https://stat-playground.streamlit.app//",
                "description": "It provides an intuitive, user-friendly interface for comprehensive statistical analysis and visualization."
            },  
            {
                "name": "Machine Learning (ML) Code Generator", 
                "url": "https://ml-code-gen.streamlit.app/",
                "description": "An easy-to-use, open-source application to generate python codes for machine learning algorithms."
            },      
            {
                "name": "Financial Management Studio", 
                "url": "https://fin-man.streamlit.app//",
                "description": "An open-source financial component calculators which help users solver regular financial requirements."
            },  
            {
                "name": "Games Arena", 
                "url": "https://games-arena.streamlit.app//",
                "description": "A platform which help users to play games on their free time."
            } 

        ] 

num_cols = 5
cols = st.columns(num_cols)

for idx, app in enumerate(apps):
    col_idx = idx % num_cols
    
    with cols[col_idx]:
        st.markdown(
            f"""
            <div class="app-container">
                <a href="{app['url']}" target="_blank">{app['name']}</a>
                <p class="app-description">{app['description']}</p>
                    
            </div>
            """,unsafe_allow_html=True,)
        
