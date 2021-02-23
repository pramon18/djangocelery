broker_url = 'pyamqp://rabbitmq:5672'
result_backend = 'amqp://rabbitmq:5672'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'America/Recife'