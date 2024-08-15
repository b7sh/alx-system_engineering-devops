Issue Summary:
Duration of the Outage: The outage started at 07:30 pm and was resolved by 07:55 PM West saudi arabia Time.

Timeline:

07:30 - The issue was detected
07:35 - the system was down
07:43 - focus on the problem
07:50 - try many solutions
07:55 - the problem solved

Root cause and resolution:
-The root cause was the failure to link the sites-available configuration to sites-enabled, meaning the Nginx server configuration was not active despite being correct.
-The issue was resolved by linking the default configuration from sites-available to sites-enabled and restarting the Nginx service.

Corrective and preventative measures:
Ensuring that after any configuration changes, a script or automated check is run to confirm that the necessary configurations are linked and active. Improve the monitoring system to detect such issues earlier.

![pQ9YzVY](https://github.com/user-attachments/assets/76bc90db-4afb-4335-b981-c7b4cf0ee79b)



