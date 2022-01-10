### This script is triggered from within docker contrainer
### to start multiple processes in the same container.
### This script is defined in the CMD option in Dockerfile

# Start actions server in background

#python3 -m rasa_sdk --actions actions

rasa run actions --actions actions&

# Start rasa server with nlu model
rasa run -m /app/models/ --enable-api --cors "*" \
        --endpoints /app/endpoints.yml \
        # --credentials /app/credentials.yml   --ssl-certificate /app/certs/chatbot.indiadataportal.com/cert4.pem  --ssl-keyfile /app/certs/chatbot.indiadataportal.com/privkey4.pem
