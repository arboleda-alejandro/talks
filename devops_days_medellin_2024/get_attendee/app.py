from flask import Flask, request, jsonify
import requests
from faker import Faker
import json
from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor


# Create one resource to identify the service
resource = Resource(attributes={
    SERVICE_NAME: "devopsdays_attendee_service"
})

# Configure trace provider
trace.set_tracer_provider(TracerProvider(resource=resource))

# Create OTLP exporter
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

# Add span processor
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Create App
app = Flask(__name__)

# OTel Autoinstrumentation
RequestsInstrumentor().instrument()
FlaskInstrumentor().instrument_app(app)

# Create fake instance to build random names in spanish
fake = Faker('es_ES')

# First API method
@app.route('/report_devopsdays2024', methods=['GET'])
def report_devopsdays():
    event = 'devopsdays2024'
    try:
        # call to endpoint get_attendees
        response = requests.get(f'http://127.0.0.1:8765/get_attendees?event={event}')
        response.raise_for_status()
        attendees = response.json()
        return jsonify(attendees), 200
    except requests.exceptions.RequestException as e:
        return str(e), 500

# Second API method
@app.route('/get_attendees', methods=['GET'])
def get_attendees():
    event = request.args.get('event')
    try:
        # Call to endpoint query_main_db
        response = requests.get(f'http://127.0.0.1:8765/query_main_db?entity=attendee&event={event}')
        response.raise_for_status()
        attendees = response.json()
        return jsonify(attendees), 200
    except requests.exceptions.RequestException as e:
        return str(e), 500

# Third API method
@app.route('/query_main_db', methods=['GET'])
def query_main_db():
    entity = request.args.get('entity')
    event = request.args.get('event')
    
    # Generate 10 randon names
    attendees = [{'name': fake.name()} for _ in range(10)]
    json_data = json.dumps(attendees, ensure_ascii=False)
    return json_data, 200

# Run app
if __name__ == '__main__':
    app.run(port=8765, debug=True)

