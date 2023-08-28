- What is a server
A server is a computer that provide functionalities to other devices or programs usually known as clients.

 A server is a powerful computer designed to handle various tasks and requests from clients over a network. It can be a physical machine or a virtual instance in a data center.


- What is the role of the domain name?

A domain name plays a pivotal role in how users access websites and other resources on the internet. It serves as a human-readable address that maps to a specific IP address, allowing people to easily navigate to websites without needing to remember complex numerical IP addresses. Here are the key roles of a domain name:

- What type of DNS record www is in www.foobar.com ?
The DNS record type associated with the "www" subdomain in the domain name "www.foobar.com" is typically an "A" (Address) record or a "CNAME" (Canonical Name) record. These records are used to map the subdomain "www" to an IP address, allowing users to access the website using the full domain name.


- What is the role of the web server
Web Server's Role: The web server receives the HTTP request and processes it using its built-in rules and configurations. It determines which files or resources correspond to the requested URL.

The web server software is installed and configured on the server. Common web server software includes Apache, Nginx, Microsoft IIS (Internet Information Services), and LiteSpeed.


- What is the role of the application server

-- An application server's primary role is to execute the business logic of a web application. It handles dynamic content generation and interacts with databases and other back-end services.
-- Application servers are responsible for processing requests that require computation, data manipulation, and interaction with external resources.
-- They can execute server-side code written in languages like Java, Python, PHP, Ruby, etc.
Application servers often provide features like connection pooling, session management, and transaction management.

- What is the role of the database?
The role of a database in the context of application servers is to provide a structured and efficient way to store, manage, and retrieve data used by the applications. Application servers handle the processing and logic of applications, while databases handle the data storage and retrieval. Here are the key roles of a database in conjunction with application servers:


- What is the server using to communicate with the computer of the user requesting the website

- SPOF
Due to lack of redundant server nodes, the web services will go down anytime any of the nodes goes down.

- Downtime when maintenance needed (like deploying new code web server needs to be restarted)

The service will suffer a high down time since there are no spare servers to handle incoming traffic. There the service will be down until the service is completed restarted and functional.

- Cannot scale if too much incoming traffic
There will be loss of traffic if there are simultaneous request. Also there server may take a long time to respond to some of the requests. Hence, affecting the servers scalability.

- For every additional element, why you are adding it

If one web server fails, the load balancer redirects traffic to other healthy servers, minimizing downtime.

Load balancing ensures that requests are evenly distributed,optimizing response times.
Security: The load balancer can act as a barrier, reducing direct exposure of web servers and application servers to the internet.

Scalability: As traffic increases, additional web servers can be added to handle the load, increasing the application's capacity.

- What distribution algorithm your load balancer is configured with and how it works?

 Round Robin Scheduling

Requests are served by the server sequentially one after another. After sending the request to the last server, it starts from the first server again.


- Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both?

Disaster recovery solutions typically set up two homogeneous sites, one active and one passive. Each site is a self-contained system. The active site is generally called the production site, and the passive site is called the standby site.

- How a database Primary-Replica (Master-Slave) cluster works?

A database primary-replica (master-slave) cluster is a configuration in which one database server (the primary or master) handles write operations and serves as the authoritative source of data, while one or more additional database servers (the replicas or slaves) replicate data from the primary server to handle read operations and provide fault tolerance. This setup enhances performance, availability, and data redundancy.


Challenges and Considerations:

Data Consistency: Ensuring that data remains consistent across replicas can be complex, especially in asynchronous replication scenarios.
Network Latency: Geo-replication across distant locations can introduce network latency.
Failover Strategy: Automatic failover mechanisms must be well-configured to ensure seamless transitions.
Monitoring and Maintenance: Regular monitoring and maintenance are required to ensure the health and performance of the cluster.

