Creating a complete Python-based web application like "Eco-Trekker" for route planning and carbon footprint calculation involves several components. In this example, I'll create a simplified version using Flask, a popular web framework in Python. This application will allow users to input start and end locations and calculate a rough carbon footprint associated with the travel by different modes of transportation.

First, ensure you have Flask installed. You can do this by running:
```bash
pip install Flask
```

Next, you'll need to create a Python file for the web application logic:

```python
# eco_trekker.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Dummy data for emission factors
EMISSION_FACTORS = {
    'car': 0.120,        # kg CO2 per km
    'bus': 0.068,        # kg CO2 per km
    'train': 0.045,      # kg CO2 per km
    'bicycle': 0.0,      # kg CO2 per km
    'walking': 0.0       # kg CO2 per km
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        start = request.form.get('start')
        end = request.form.get('end')
        mode = request.form.get('mode')

        if not start or not end or not mode:
            raise ValueError("Missing required inputs!")

        # Dummy distance for demonstration purposes
        # Assume Google Maps API or a similar API for actual distance calculation
        distance = 100  # Placeholder for distance in km

        carbon_footprint = distance * EMISSION_FACTORS.get(mode, 0.0)

        return jsonify({
            'start': start,
            'end': end,
            'mode': mode,
            'distance': distance,
            'carbon_footprint': carbon_footprint
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
```

For the application to work, you also need a basic HTML template to interact with the user:

Create a directory named "templates" in the same location as your Python file and add a file named `index.html`:

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eco-Trekker</title>
</head>
<body>
    <h1>Eco-Trekker: Route Planning and Carbon Footprint Calculator</h1>
    <form id="routeForm">
        <label for="start">Start Location:</label>
        <input type="text" id="start" name="start" required><br><br>
        
        <label for="end">End Location:</label>
        <input type="text" id="end" name="end" required><br><br>
        
        <label for="mode">Transport Mode:</label>
        <select id="mode" name="mode" required>
            <option value="car">Car</option>
            <option value="bus">Bus</option>
            <option value="train">Train</option>
            <option value="bicycle">Bicycle</option>
            <option value="walking">Walking</option>
        </select><br><br>
        
        <button type="submit">Calculate</button>
    </form>

    <div id="result"></div>

    <script>
        document.getElementById('routeForm').addEventListener('submit', function(event) {
            event.preventDefault();

            fetch('/calculate', {
                method: 'POST',
                body: new URLSearchParams(new FormData(event.target))
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    document.getElementById('result').innerHTML = `Error: ${data.error}`;
                } else {
                    document.getElementById('result').innerHTML = `
                        Start: ${data.start}<br>
                        End: ${data.end}<br>
                        Mode: ${data.mode}<br>
                        Distance: ${data.distance} km<br>
                        Estimated Carbon Footprint: ${data.carbon_footprint.toFixed(2)} kg CO2
                    `;
                }
            })
            .catch(err => {
                console.error(err);
                document.getElementById('result').innerHTML = 'Error in calculation process!';
            });
        });
    </script>
</body>
</html>
```

### Points to Remember:

- This program is a simplistic example with hardcoded distance. For a real application, integrate with a service like the Google Maps Distance Matrix API to get actual distances.
- The emission factors are dummy values used for demonstration purposes; for a real-world application, you should use data from a reliable source.
- Ensure proper API key management, environment-specific configurations, and secure input handling in a production environment.
- Use a virtual environment to handle dependencies more effectively.

To run the application, execute the following command in the terminal:

```bash
python eco_trekker.py
```

The application should be accessible at `http://127.0.0.1:5000/` in the browser. Explore input forms, and submit data to see how the application processes the input and returns the carbon footprint result.