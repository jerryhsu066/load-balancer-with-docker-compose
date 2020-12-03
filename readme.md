# A simple load balancer using docker-compose

```
          [ Load Balancer ] (Nginx)
                  |
        +---------+---------+
        |                   |
[ Web Server 1 ]    [ Web Server 2 ] (Flask)
```

## Usage

```bash
docker-compose up -d
```

