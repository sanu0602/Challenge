# Set the environment variables for the client ID, tenant ID, and password
export AZURE_CLIENT_ID=your_client_id
export AZURE_TENANT_ID=your_tenant_id
export AZURE_CLIENT_SECRET=your_client_secret

# Log in to Azure using the environment variables
az login --service-principal -u $AZURE_CLIENT_ID -t $AZURE_TENANT_ID --password $AZURE_CLIENT_SECRET

# Set the subscription ID
subscription_id=your_subscription_id
az account set --subscription $subscription_id


# Set the resource group name and VM name
resource_group_name=dev-rg
vm_name=dev-web-vm


# Set the subscription
az account set --subscription $subscription_id

# Get the virtual machine metadata
metadata=$(az vm show --name $vm_name --resource-group $resource_group --query 'instanceView.metadata' -o json)

echo $metadata
