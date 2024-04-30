import os

from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import SimpleSpanProcessor


def instrument():
    collector_endpoint = os.getenv("COLLECTOR_ENDPOINT")
    resource = Resource(
        attributes={
            "model_id": "hackathon1",  # Set this to any name you'd like for your app
            "model_version": "1.0",  # Set this to a version number string
        }
    )
    tracer_provider = trace_sdk.TracerProvider(resource=resource)
    span_exporter = OTLPSpanExporter(endpoint=collector_endpoint)
    span_processor = SimpleSpanProcessor(span_exporter=span_exporter)
    tracer_provider.add_span_processor(span_processor=span_processor)
    trace_api.set_tracer_provider(tracer_provider=tracer_provider)
    ARIZE_SPACE_KEY = os.getenv("ARIZE_SPACE_KEY")
    ARIZE_API_KEY = os.getenv("ARIZE_API_KEY")
    headers = f"space_key={ARIZE_SPACE_KEY},api_key={ARIZE_API_KEY}"
    os.environ["OTEL_EXPORTER_OTLP_TRACES_HEADERS"] = headers

    LlamaIndexInstrumentor().instrument()
    print("🔭 OpenInference instrumentation enabled.")
