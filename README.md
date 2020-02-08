# watson-assistant-with-discovery


Description: The goal of chat robots is to help intelligent robots to quickly solve problems in factories
 For example: equipment conservative document query, improvement of abnormal report utilization rate, confirmation of warehouse preparations, etc.

*  Environmental preparation
    *  VSCODE is used to develop front-end VUE
    *  Eclipse for back-end Python development
    *  IBM Cloud account registration for Watson service creation


* The package Installation 
    * pip install -r requirements.txt


* Create Watson service:
    * create a IBMCloud Account: https://cloud.ibm.com/registration
    * Watson Assistant (one)
    * Watson Discovery (at least one, more than one current Lite version account can only create two colicction)
    * Cloud Object Storage (at least one)
    * Db2 services


* Modify calling service API_KEY
    *use your own apikey to modify the .env


* Run python service start.py
