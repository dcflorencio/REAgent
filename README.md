# ReAgent tou intellingent Real Estate Agent

This project implements a multi-agent system for generating real estate reports by querying Zillow's API. The application is built using Microsoft Autogen and Streamlit for an interactive user interface. The code includes functionality to fetch real estate data based on user-defined criteria and generate detailed reports in Markdown format. 

## Features

1. **Multi-Agent Chat System**: The system uses a group of agents to collaborate on generating a real estate report:
    - **User Proxy Agent**: Allows the user (Admin) to provide feedback and refine the generated reports.
    - **Planner Agent**: Plans the necessary information required to generate the report.
    - **Engineer Agent**: Writes the code to query Zillow API based on the planner's instructions.
    - **Executor Agent**: Executes the code written by the engineer.
    - **Writer Agent**: Writes and refines the real estate report based on the queried data and user feedback.

2. **Zillow API Integration**: A custom function `fetch_zillow_data` queries the Zillow API for real estate listings based on various parameters like location, price, home type, etc.

3. **Report Generation**: The system generates a Markdown file with real estate listings, including parameters such as:
    - Location (e.g., city or neighborhood)
    - Price, bedrooms, bathrooms, and square footage
    - Filtering options such as property status, home type, and sorting criteria
    - Images and coordinates (latitude and longitude) for each listing

4. **Streamlit Interface**: The application provides an interactive user interface using Streamlit, allowing users to input their search parameters and visualize the results.

## How it Works

1. **Environment Setup**:
    - The `.env` file is loaded to retrieve API keys for OpenAI and RapidAPI.
    - The code interacts with the Zillow API using the `fetch_zillow_data` function.

2. **Agent Collaboration**:
    - A user initiates a request (e.g., "Generate a real estate report to show some homes I am interested in").
    - The planner agent defines the required information based on the user's request.
    - The engineer agent writes Python code to fetch the real estate data.
    - The executor agent runs the code and retrieves the data.
    - The writer agent creates a detailed report based on the fetched data and user feedback. The report is saved as a Markdown file using the `save_markdown_file` function.

3. **Customizable Search**: Users can input various search criteria such as:
    - Location (e.g., "San Francisco")
    - Price range
    - Number of bedrooms, bathrooms
    - Property type (e.g., apartments, houses, townhomes)
    - Sorting options (e.g., price, days on the market)
    
4. **Markdown Report**: The final report includes property details, images, and coordinates, and is saved as a Markdown file for easy viewing and sharing.

## Installation

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies listed in `requirements.txt`.
3. Set up your `.env` file with the following variables:
    - `OPENAI_API_KEY`: Your OpenAI API key.
    - `RAPIDAPI_KEY`: Your RapidAPI key for Zillow API access.
4. Run the application using Streamlit:
   ```bash
   streamlit run app.py

## Screenshots

![Report Screenshot](https://github.com/dcflorencio/REAgent/blob/main/report.JPG)
