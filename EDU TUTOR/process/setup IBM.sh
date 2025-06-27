# Install IBM Cloud CLI
curl -fsSL https://clis.cloud.ibm.com/install/linux | sh
ibmcloud login
ibmcloud target --cf
ibmcloud plugin install cloud-functions