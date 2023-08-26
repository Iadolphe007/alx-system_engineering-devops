<h1>TASK 0</h1>
<h3><strong>a server</strong></h3>
<p> is a computer or software that provides services, data, or resources to other computers, known as clients, over a network like the internet. It responds to requests from clients, delivering the requested information or performing specific tasks</p>
<h3><strong>role of the domain name</strong></h3>
<p>A domain name serves as a human-readable address that represents the numeric IP address of a computer or server on the internet. It's used to easily access websites and online resources without needing to remember complex IP numbers.</p>
<h3><strong> DNS record www is in www.foobar.com</strong></h3>
<P>it's a 'CNAME'</P>
<h3><strong>What is the role of the Web Server</strong></h3>
<p>the role of a web server is to store, process nad display webstise content(codbase) and give web pages to teh users over HTTP protocol</p>
<h3><strong>What is the role of Application server</strong></h3>
<p>is to generate dynamic contents by executing server side code</p>
<h3><strong>What is the role of Database</strong></h3>
<p>the role of a database is to manage data systemically and efficiently in a well organised manner which allows data to be easily added, accessed, updated and deleted</p>
<h3><strong>What is the server using to communicate with the computer of the user requesting the website</strong></h3>
<p>server communicate through HTTP protocol</p>

<h1>ISSUES</h1>

<h3><strong>SPOF</strong></h3>
<p>the points of failure are that having pne server that contains only one Web, APP server and database  A SPOF is a part of system that if it fails all the entinre system will stop working</p>
<h3><strong>Downtime when maintenance needed (like deploying new code web server needs to be restarted)</strong></h3>
<p>the downtimw is dependent on one code base which at the moment its not available user will not be able to access the website </p>

<h3><strong>Cannot scale if too much incoming traffic</strong></h3>
<p>The absence of a load balancer in the domain configuration prevents effective scaling in response to high incoming traffic. This lack of load balancing capability poses challenges in managing increased user loads. Consequently, user experience might degrade, and the website's capacity to accommodate users becomes restricted.
</p>

<h1><strong>TASK 1</strong></h1>
<h3><strong>Reason for Adding Additional Elements</strong></h3>
<p>When we introduce a new server, we achieve two important goals. Firstly, it allows us to implement a load balancer, which efficiently handles high volumes of incoming traffic. Secondly, this setup helps us 
  eliminate the vulnerability of a single point of failure that arises when relying on a single server</p>
  <br>
  <h3><strong>What distribution algorithm your load balancer is configured with and how it works</strong></h3>
  <strong>Load Balancer Distribution Algorithm</strong>
  <p>load balancer operates using the Round Robin algorithm. 
    This algorithm connects to servers in a sequential order, distributing requests evenly. Each server serves requests in turn. 
    Once all servers have received a request, the cycle begins anew. This algorithm is suitable for servers of equal specifications and when persistent connections are not numerous.
</p>
<br>
<h3><strong>Active-Active vs. Active-Passive Setup</strong></h3>
<p>load balancer employs an Active-Active setup. In this configuration, both nodes (servers) provide the same service concurrently. In contrast, an Active-Passive setup has only one node active while others remain inactive. For instance, in a two-node setup, if the first node is active, the second is in standby. The key distinction lies in performance. Active-Activ
  e clusters utilize all server resources during normal operation, whereas active-passive setups
  only activate the backup server during failover</p>
  <br>
  <h3><strong>Database Primary-Replica (Master-Slave) Cluster</strong></h3>
  <p>The master-slave replication mechanism involves copying data from a master database 
    server to one or more slave database servers. Updates made on the master are logged 
    and then replicated to the slaves. Synchronous replication occurs when changes are
    simultaneously made on both master and slave, while asynchronous replication involves
    queued changes written later. This setup is commonly used to distribute read access across multiple servers for scalability. It also serves purposes like failover and data analysis on the slave to prevent overloading the master.
</p>
<br>
<h3><strong>Primary Node vs. Replica Node</strong></h3>
<p>The replica node functions as a duplicate of the primary node. It serves two key roles: safeguarding
  against hardware failures by offering redundant copies of the application codebase, and enhancing capacity to 
  handle read requests, such as searches or document retrieval</p>
  <br>

<h1><strong>ISSUES</strong></h1>
<h3><strong>SPOF</strong><h3>
<p>the points of failure are that having pne server that contains only one Web, APP server and database 
  A SPOF is a part of system that if it fails all the entinre system will stop working</p>
<br>
  <h3><strong>Security issues (no firewall, no HTTPS)</strong></h3>
<p> A firewall acts as a protective barrier between a computer network and potential threats from the internet. Without a firewall, unauthorized access, malicious attacks, and data breaches become more likely, putting sensitive information at risk.</p>
<p>HTTPS (Hypertext Transfer Protocol Secure) encrypts data transmitted between a user's browser and a website's server. Without HTTPS, data exchanged, such as login credentials and personal information, can be intercepted by attackers, leading to privacy breaches and potential misuse.</p>

<h3><strong>No monitoring</strong></h3>
<p>Monitoring involves observing and tracking the performance, activity, and health of systems, networks, or applications. Without monitoring "Issues and inefficiencies might go unnoticed, 
  Downtimes or disruptions might occur without immediate detection,
  Performance bottlenecks might impact user experience,
  Security breaches could remain undetected for longer periods,
  Data on system usage and trends for optimization could be missing
</p>
