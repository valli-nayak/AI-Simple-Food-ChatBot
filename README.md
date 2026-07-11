Open your terminal and type
python3 -m venv <your-environment-name>
source <your-environment-name>/bin/activate

We are using Google Gemni Model LLM(gemini-2.5-flash) here.

Paste the api keys in the .env folder created at the root level of your project
1. Go to Google AI Studio and get the api key https://aistudio.google.com/api-keys
GOOGLE_API_KEY="<YOUR_API_KEY>"

2. Go to https://smith.langchain.com/ and get the API KEY
LANGCHAIN_API_KEY="<YOUR_API_KEY>"

How to run Streamlit applications ?.
Open terminal and type:
`streamlit run <project-name>`
