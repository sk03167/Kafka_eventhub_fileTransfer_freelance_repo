

# Start Zookeeper in a new Terminal window
echo "Starting Zookeeper in a new terminal..."
open -a Terminal "./zookeeper-server-start-script.sh"

# Wait a few seconds for Zookeeper to start
sleep 7

# Start Kafka in a new Terminal window
echo "Starting Kafka server in a new terminal..."
open -a Terminal "./kafka-server-start-script.sh"

echo "Kafka and Zookeeper have started in separate terminal windows."
