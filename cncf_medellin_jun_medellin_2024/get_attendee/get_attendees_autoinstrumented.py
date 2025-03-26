from flask import Flask, request, jsonify
import requests
from faker import Faker
import json
import socket
from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# Create one resource to identify the service
resource = Resource(attributes={
    SERVICE_NAME: "cncf_medellin_attendee_service_auto_instrumented"
})

# Configure trace provider
trace.set_tracer_provider(TracerProvider(resource=resource))

# Create OTLP exporter
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

# Add span processor
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Create App
get_attendees_autoinstrumented = Flask(__name__)

# OTel Autoinstrumentation
RequestsInstrumentor().instrument()
FlaskInstrumentor().instrument_app(get_attendees_autoinstrumented)

# Create fake instance to build random names in spanish
fake = Faker('es_ES')

# First API method
@get_attendees_autoinstrumented.route('/', methods=['GET'])
def report_cncf_medellin():
    event = 'cncfmedellin'
    try:
        # call to endpoint get_attendees
        response = requests.get(f'http://127.0.0.1:8765/get_attendees?event={event}')
        response.raise_for_status()
        attendees = response.json()
        return jsonify(attendees), 200
    except requests.exceptions.RequestException as e:
        return str(e), 500

# Second API method
@get_attendees_autoinstrumented.route('/get_attendees', methods=['GET'])
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
@get_attendees_autoinstrumented.route('/query_main_db', methods=['GET'])
def query_main_db():
    entity = request.args.get('entity')
    event = request.args.get('event')

    # Generate 10 randon names
    hostname_ = socket.gethostname()
    attendees = [fake.name() for _ in range(10)]
    attendes_dictio = {"CNCF-Medellin2024Attendees": attendees}
    attendes_dictio['Origin'] = hostname_
    json_data = json.dumps(attendes_dictio, ensure_ascii=False)
    # json_data = json.dumps({"CNCF-Medellin2024Attendees": attendees}, ensure_ascii=False)
    #
    return json_data, 200

# Run app
if __name__ == '__main__':
    get_attendees_autoinstrumented.run(port=8765, debug=True)
