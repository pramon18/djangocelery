broker_url = 'amqp://pablo:12345@localhost:5672/'
result_backend = 'db+sqlite:///results.sqlite'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'America/Recife'