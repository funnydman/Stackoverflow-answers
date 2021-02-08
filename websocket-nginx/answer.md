Actually, there is no much reason to pass the certificates directly to WebSocket if you're going to use Nginx as a proxy. It's enough to handle SSL only on Nginx stack. 

So the simple example of Nginx configuration would be:
```
upstream wsbackend {
    server app:8765;
}
server {
    listen 443 ssl;
    server_name  _;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location /websocket {
        proxy_pass http://wsbackend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
    }
}
```
After that, connect to WebSocket via `wss://localhost/websocket`. I created a [runnable example][1] with Docker you can play around with it.


  [1]: https://github.com/funnydman/Stackoverflow-answers/tree/main/websocket-nginx
