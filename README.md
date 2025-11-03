# API Player - Backend

This is the backend API for the API Player application built with FastAPI.

## Deployment to Render

1. Create an account at [Render](https://render.com/)
2. Click "New" and select "Web Service"
3. Connect your GitHub repository or upload your code
4. Set the following configuration:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Environment: Python
5. Add environment variables if needed
6. Deploy!

## Local Development

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## API Documentation

Once running, visit:
- API Docs: `http://localhost:8000/docs`
- Main endpoint: `http://localhost:8000/`