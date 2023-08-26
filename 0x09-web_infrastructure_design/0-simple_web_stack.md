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
