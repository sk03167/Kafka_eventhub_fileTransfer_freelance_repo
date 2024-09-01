#!/usr/bin/env python
#
# Copyright (c) Microsoft Corporation. All rights reserved.
# Copyright 2016 Confluent Inc.
# Licensed under the MIT License.
# Licensed under the Apache License, Version 2.0
#
# Original Confluent sample modified for use with Azure Event Hubs for Apache Kafka Ecosystems

from azure.identity import DefaultAzureCredential
from confluent_kafka import Producer
import sys
from functools import partial


def oauth_cb(cred, namespace_fqdn, config):
    # confluent_kafka requires an oauth callback function to return (str, float) with the values of (<access token>, <expiration date in seconds from epoch>)

    # cred: an Azure identity library credential object. Ex: an instance of DefaultAzureCredential, ManagedIdentityCredential, etc
    # namespace_fqdn: the FQDN for the target Event Hubs namespace. Ex: 'mynamespace.servicebus.windows.net'
    # config: confluent_kafka passes the value of 'sasl.oauthbearer.config' as the config param

    access_token = cred.get_token('https://%s/.default' % namespace_fqdn)
    return access_token.token, access_token.expires_on


if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     sys.stderr.write('Usage: %s <eventhubs-namespace> <topic>\n' % sys.argv[0])
    #     sys.exit(1)

    # namespace = sys.argv[1]
    # topic = sys.argv[2]

    # Azure credential
    # See https://docs.microsoft.com/en-us/azure/developer/python/sdk/authentication-overview
    cred = DefaultAzureCredential()
    print(cred)
    # Producer configuration
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    # conf = {
    #     'bootstrap.servers': '%s:9093' % namespace,

    #     # Required OAuth2 configuration properties
    #     'security.protocol': 'SASL_SSL',
    #     'sasl.mechanism': 'OAUTHBEARER',
    #     # the resulting oauth_cb must accept a single `config` parameter, so we use partial to bind the namespace/identity to our function
    #     'oauth_cb': partial(oauth_cb, cred, namespace),
    # }
