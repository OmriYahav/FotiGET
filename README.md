# FotiGET
![This is an image](/img/fortiPython.png)



This is a Python script that retrieves information from a FortiGate device using its API. 

The script imports the necessary libraries, sets the API endpoints, and includes the API key in the headers.
Then, it defines the URLs to access the API and makes GET requests to retrieve the desired information.

The script checks if the requests were successful and if so,
it extracts the relevant information from the JSON responses and stores them in separate dictionaries.
These dictionaries are then printed to the console using nested loops to display each key-value pair from REST API.

Overall, the script appears to be a useful tool for retrieving and displaying information from a FortiGate device through its API.
However, it would benefit from additional error handling to ensure that the script can gracefully handle unexpected errors or invalid responses from the API.
