KAFKA_CONFIG="/opt/homebrew/etc/kafka/server.properties"

if [[ ! -f "$KAFKA_CONFIG" ]]; then
    echo "Error: Kafka server properties file not found at $KAFKA_CONFIG"
    exit 1

else kafka-server-start $KAFKA_CONFIG
fi