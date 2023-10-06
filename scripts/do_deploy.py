global
    log /dev/log    local0
    log /dev/log    local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
    stats timeout 30s
    user haproxy
    group haproxy
    daemon
    tune.ssl.default-dh-param 2048
    # Default SSL material locations
    ca-base /etc/ssl/certs
    crt-base /etc/ssl/private

    # Default ciphers to use on SSL-enabled listening sockets.
    ssl-default-bind-ciphers kEECDH+aRSA+AES:kRSA+AES:+AES256:RC4-SHA:!kEDH:!LOW:!EXP:!MD5:!aNULL:!eNULL

defaults
    log global
    mode    http
    option  httplog
    option  dontlognull
    timeout connect 5000
    timeout client  50000
    timeout server  50000
    option forwardfor
    option http-server-close

frontend http_front
    bind *:80
    bind *:443 ssl crt /etc/ssl/private/gvtech.pem
    redirect scheme https code 301 if !{ ssl_fc }
    stats uri /haproxy?stats
    default_backend http_back

backend http_back
    balance roundrobin
    server web-01 18.235.248.71:80 check
    server web-02 54.146.78.208:80 check