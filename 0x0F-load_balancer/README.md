# 0x0F. Load balancer

## Resources:
Read or watch:
* [Introduction to load-balancing and HAproxy](https://intranet.hbtn.io/rltoken/ngIXarEyu8jZwOL3Y30PLQ)
* [HTTP header](https://intranet.hbtn.io/rltoken/v32JmcDrSiOnFBfqzXvs_Q)
* [Debian/Ubuntu HAProxy packages](https://intranet.hbtn.io/rltoken/BXGrW_6ocecWaOJb7OK_WA)

---
## Tasks:

* **0. Double the number of webservers**
  * [0-custom_http_response_header](./0-custom_http_response-header): Bash
    script that installs and configures Nginx on a server with a custom HTTP
      response header.
  * The name of the HTTP header is `X-Served-By`.
  * The value of the HTTP header is the hostname of the server.

* **1. Install your load balancer**
  * [1-install_load_balancer](./1-install_load_balancer): Bash script that
    installs and configures HAproxy version 1.5 on a server.
  * Enables management via the init script.
  * Requests are distributed using a round-robin algorithm.

---
## Author
* **Estephania Calvo Carvajal** - [EstephaniaCalvoC](https://github.com/EstephaniaCalvoC)
