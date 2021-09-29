# PG County Housing Inspection Violations

http://rachittableauwebapp.s3-website-us-east-1.amazonaws.com/

The information problem is based on how prospective home buyers and renters in PG County lack the resources to view housing inspection violation data in their area in a clear and easy to understand way.

The target browsers are Android, specifically Google Chrome and Firefox browsers.

# Developer Manual

Node.JS is required in order to run this application. Installing the application requires first cloning the repository from GitHub onto your local system, then running the command "npm install" within the repository directory will install all node packages and dependencies. The main libraries that are being used from the packages are the Express framework, Leaflet, and the Leaflet-GeoSearch package. Running the application on a server only requires changing the port variable in the server.js file and then hosting it on whatever server the developer wishes. The server uses the Fetch API to GET information for PG County open-data, the server gets the dataset on housing inspection violations and then manipulates the data by concatenating the columns describing the address into a single street address column. The server then sends out this data to the front end where it is then used to map the addresses on a Leaflet map using the GeoSearch library by querying each address and getting the longitude and latitude of the address for plotting.
