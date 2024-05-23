from flask import Flask, request, jsonify
import requests
from faker import Faker
import json
from opentelemetry import trace, context
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.propagate import inject, extract

# Create one resource to identify the service
resource = Resource(attributes={
    SERVICE_NAME: "devopsdays_attendee_service_manual_instrumented"
})

# Configure trace provider
trace.set_tracer_provider(TracerProvider(resource=resource))

# Create OTLP exporter
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

# Add span processor
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Create tracer
tracer = trace.get_tracer(__name__)

# Create App
get_attendees_manualinstrumented = Flask(__name__)

# Create fake instance to build random names in spanish
fake = Faker('es_ES')

# Helper function for context propagation
def get_propagated_headers():
    headers = {}
    inject(headers, context=context.get_current())
    return headers

# First API method
@get_attendees_manualinstrumented.route('/report_devopsdays2024', methods=['GET'])
def report_devopsdays():
    event = 'devopsdays2024'
    with tracer.start_as_current_span("report_devopsdays"):
        try:
            # Prepare headers for context propagation
            headers = get_propagated_headers()

            # Call to endpoint get_attendees
            with tracer.start_as_current_span("HTTP GET /get_attendees"):
                response = requests.get(f'http://127.0.0.1:5678/get_attendees?event={event}', headers=headers)
                response.raise_for_status()
                attendees = response.json()
                return jsonify(attendees), 200
        except requests.exceptions.RequestException as e:
            return str(e), 500

# Second API method
@get_attendees_manualinstrumented.route('/get_attendees', methods=['GET'])
def get_attendees():
    event = request.args.get('event')
    ctx = extract(request.headers)
    token = context.attach(ctx)
    try:
        with tracer.start_as_current_span("get_attendees"):
            # Prepare headers for context propagation
            headers = get_propagated_headers()
            # Call to endpoint query_main_db
            with tracer.start_as_current_span("HTTP GET /query_main_db"):
                response = requests.get(f'http://127.0.0.1:5678/query_main_db?entity=attendee&event={event}', headers=headers)
                response.raise_for_status()
                attendees = response.json()
                return jsonify(attendees), 200
    except requests.exceptions.RequestException as e:
        return str(e), 500
    finally:
        context.detach(token)

# Third API method
@get_attendees_manualinstrumented.route('/query_main_db', methods=['GET'])
def query_main_db():
    entity = request.args.get('entity')
    event = request.args.get('event')
    ctx = extract(request.headers)
    token = context.attach(ctx)
    try:
        with tracer.start_as_current_span("query_main_db"):
            # Generate 10 random names
            attendees = [fake.name() for _ in range(10)]
            json_data = json.dumps({"DevopsDaysMedellin2024Attendees": attendees}, ensure_ascii=False)
            return json_data, 200
    finally:
        context.detach(token)

# Run app
if __name__ == '__main__':
    get_attendees_manualinstrumented.run(port=5678, debug=True)
