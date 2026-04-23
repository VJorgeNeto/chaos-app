import logging
from pythonjsonlogger import jsonlogger
from opentelemetry import trace

class OTelJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(OTelJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['level'] = record.levelname
        
        # Injeta Trace ID e Span ID do OpenTelemetry no Log
        span = trace.get_current_span()
        if span.is_recording():
            span_context = span.get_span_context()
            log_record['trace_id'] = format(span_context.trace_id, '032x')
            log_record['span_id'] = format(span_context.span_id, '016x')
        else:
            log_record['trace_id'] = None
            log_record['span_id'] = None

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Remove handlers padrão
    while logger.hasHandlers():
        logger.removeHandler(logger.handlers[0])
        
    logHandler = logging.StreamHandler()
    formatter = OTelJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    return logger