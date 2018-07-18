aws --profile serverless_personal --region eu-west-1 ssm put-parameter --name /workshop-node/dev/table_name --type String --value restaurants
aws --profile serverless_personal --region eu-west-1 ssm put-parameter --name /workshop-node/dev/cognito_user_pool_id --type String --value eu-west-1_z9AyExIfw
aws --profile serverless_personal --region eu-west-1 ssm put-parameter --name /workshop-node/dev/cognito_web_client_id --type String --value 29oc5lf4tonbodmuhom07b1srm
aws --profile serverless_personal --region eu-west-1 ssm put-parameter --name /workshop-node/dev/cognito_server_client_id --type String --value 687aijjbjc8nu69qjjr7oglu96
aws --profile serverless_personal --region eu-west-1 ssm put-parameter --name /workshop-node/dev/url --type String --value 4qkmw6oovb.execute-api.eu-west-1.amazonaws.com/dev
aws --profile serverless_personal --region eu-west-1 ssm put-parameter --name /workshop-node/dev/stream_name --type String --value orders-dev
aws --profile serverless_personal --region eu-west-1 ssm put-parameter --name /workshop-node/dev/restaurant_topic_name --type String --value restaurant-notification-dev

aws --profile serverless_personal --region eu-west-1 ssm put-parameter --name /workshop-node/dev/restaurant_retry_topic_name --type String --value restaurant-notification-retry-dev
aws --profile serverless_personal --region eu-west-1 ssm put-parameter --name /workshop-node/dev/restaurant_dlq_topic_name --type String --value restaurant-notification-dlq-dev
