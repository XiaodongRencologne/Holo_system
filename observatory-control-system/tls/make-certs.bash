#!/bin/bash
set -eu -o pipefail

case $# in
    0)
        hostname=localhost
        ipaddr=127.0.0.1
        ;;
    2)
        hostname=$1
        ipaddr=$2
        ;;
    *)
        echo >&2 "usage: $0 <hostname> <ipaddr>"
        exit 1
        ;;
esac

cn=$hostname

# make CA cert
openssl req -x509 -out ca.cert.pem -keyout ca.key.pem \
    -newkey rsa:2048 -nodes -sha256 -days 1000 \
    -subj "/CN=authn-proxy/O=FYST"

# make self-signed localhost cert
# https://letsencrypt.org/docs/certificates-for-localhost/
# https://stackoverflow.com/questions/10175812/how-to-generate-a-self-signed-ssl-certificate-using-openssl#answer-41366949
openssl req -x509 -out server.cert.pem -keyout server.key.pem \
    -newkey rsa:2048 -nodes -sha256 -days 1000 \
    -subj "/CN=$cn" -extensions ext -config <(printf "[req]\ndistinguished_name=dn\n[dn]\nCN=$cn\n[ext]\nsubjectAltName=DNS:$hostname,IP:$ipaddr\nkeyUsage=digitalSignature,keyEncipherment\nextendedKeyUsage=serverAuth")

# make client cert
openssl req -out client.csr.pem -keyout client.key.pem \
    -newkey rsa:2048 -nodes -sha256 -days 1000 \
    -subj "/CN=My Name/emailAddress=me@example.com/UID=me/OU=gid1/OU=gid2"

# sign client w/ CA
openssl x509 -req -CA ca.cert.pem -CAkey ca.key.pem -in client.csr.pem -out client.cert.pem \
    -sha256 -days 1000 -set_serial "$(date +%s)"

