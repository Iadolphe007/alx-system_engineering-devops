<h2>Postmortem: API outage</h2>

<h3>Issue Summary</h3>
<p><strong>Duration:</strong>The API outage occurred from 9:00 AM to 11:00 AM on November 01, 2023 (CAT timezone).</p>
<p><strong>Impact:</strong>During the outage, the Airbnb clone website's core services relying on the API were down. 
    Users were unable to search for listings, make bookings, or access their accounts. Approximately 60% of users were affected.</p>
<h4><strong>Root Cause:</strong></h4>
<p>The root cause of the outage was identified as an unhandled API rate limit issue. A sudden surge in API requests from a partner integration led to a rate limit being exceeded, causing the API to become unresponsive.</p>
<h4><strong>Timeline:</strong></h4>

<p><strong>9:00 AM: </strong>The issue was detected when monitoring system generated alerts for abnormally high API request rates.</p>
<p><strong>9:15 AM: </strong>The engineering team immediately began investigating the issue. Initially, the assumption was that this was a DDoS attack, but after reviewing the logs, it was confirmed to be a legitimate partner integration</p>
<p><strong>10:00 AM: </strong>Initially, it was suspected that a DDoS attack might be underway, but further analysis revealed that the high request rate was from a legitimate partner integration</p>
<p><strong>10:15 AM: </strong>The incident was escalated to the development team and the partner integration team to address the rate limit issue.</p>
<p><strong>11:00 AM: </strong>The rate limit issue was resolved by adjusting the API rate limits, and the API service was restored by 11:00 AM.</p>


<h4>Root Cause and Resolution:</h4>
<p><strong>Root Cause: </strong>The issue was caused by the partner integration exceeding the API rate limit, resulting in unresponsiveness. The system lacked proper handling for this scenario.</p>
<p><strong>Resolutione: </strong>The API rate limits were adjusted to accommodate the partner's legitimate traffic while ensuring system stability. Additionally, error handling mechanisms were improved to prevent such outages.</p>

<h4>Corrective and Preventative Measures:</h4>
<h4>Corrective Measures:</h4>
    <ul>
        <li>Implement more robust rate limiting mechanisms with dynamic adjustments.</li>
        <li>Enhance error handling to provide informative feedback to partners and users.</li>
        <li>Improve partner communication and integration guidelines.</li>
    </ul>


<h4>Preventative Measures:</h4>
    <ul>
        <li>Implement dynamic rate limiting for the API</li>
        <li>Enhance error messages and feedback for API users</li>
        <li>Update partner integration guidelines and communication protocols</li>
    </ul>


