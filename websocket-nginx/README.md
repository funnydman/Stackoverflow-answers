### [How to pass client certificate to WebSocket in Python?](https://stackoverflow.com/questions/52005888/how-to-pass-client-certificate-to-websocket-in-python)
## How to deploy?
1) Install `docker` and `docker-compose`
2) Run
```
docker-compose up
```
3) Navigate to `https://localhost/`

## Tips
Take a look at `nginx.conf`, you need to generate proper certificates.

Copy the password protected key to a non-password protected key (need this step after creating a self-signed cert).
```
openssl rsa -in key.pem -out key.pem
```

Useful links:
- [NGINX as a WebSocket Proxy](https://www.nginx.com/blog/websocket-nginx/)
- [How to create a self-signed certificate with OpenSSL](https://stackoverflow.com/questions/10175812/how-to-create-a-self-signed-certificate-with-openssl)
