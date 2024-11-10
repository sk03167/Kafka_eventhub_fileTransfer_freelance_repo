ZOOKEEPER_CONFIG="/opt/homebrew/etc/kafka/zookeeper.properties"

if [[ ! -f "$ZOOKEEPER_CONFIG" ]]; then
    echo "Error: Zookeeper properties file not found at $ZOOKEEPER_CONFIG"
    exit 1

else zookeeper-server-start $ZOOKEEPER_CONFIG
fi