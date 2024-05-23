from flask import Flask, request, jsonify
import requests
from faker import Faker
import json
from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.propagate import inject


# Create one resource to identify the service
resource = Resource(attributes={
    SERVICE_NAME: "devopsdays_attendee_service_no_autoinstrumentation"
})

# Configure trace provider
trace.set_tracer_provider(TracerProvider(resource=resource))

# Create OTLP exporter
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

# Add span processor
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Create App
app2 = Flask(__name__)

# Create fake instance to build random names in spanish
fake = Faker('es_ES')

tracer = trace.get_tracer(__name__)

# First API method
@app2.route('/report_devopsdays2024', methods=['GET'])
def report_devopsdays():
    with tracer.start_as_current_span("report_devopsdays2024") as span:
        event = 'devopsdays2024'
        try:
            headers = {}
            inject(headers)

            print("Headers después de la inyección:", headers)
            # Call to endpoint get_attendees
            response = requests.get(f'http://127.0.0.1:5678/get_attendees?event={event}',headers=headers)
            response.raise_for_status()
            attendees = response.json()
            return jsonify(attendees), 200
        except requests.exceptions.RequestException as e:
            return str(e), 500

# Second API method
@app2.route('/get_attendees', methods=['GET'])
def get_attendees():
    with tracer.start_as_current_span("get_attendees") as span:
        event = request.args.get('event')
        try:
            headers = {}
            inject(headers)

            print("Headers después de la inyección:", headers)
            # Call to endpoint query_main_db
            response = requests.get(f'http://127.0.0.1:5678/query_main_db?entity=attendee&event={event}',headers=headers)
            response.raise_for_status()
            attendees = response.json()
            return jsonify(attendees), 200
        except requests.exceptions.RequestException as e:
            return str(e), 500

# Third API method
@app2.route('/query_main_db', methods=['GET'])
def query_main_db():
    entity = request.args.get('entity')
    event = request.args.get('event')
    
    # Generate 10 randon names
    attendees = [{'name': fake.name()} for _ in range(10)]
    json_data = json.dumps(attendees, ensure_ascii=False)
    return json_data, 200

# Run app
if __name__ == '__main__':
    app2.run(port=5678, debug=True)

