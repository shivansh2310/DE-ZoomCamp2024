provider "azurerm" {
  features {}
}

data "azuread_client_config" "current" {}

data "azurerm_client_config" "current" {}

data "azurerm_subscription" "current" {}

resource "azurerm_resource_group" "resource_group" {
  name     = "${var.app_name}-${var.app_environment}"
  location = "West US 2"
}

resource "azurerm_network_profile" "containergroup_profile" {
  name                = "${var.app_name}-${var.app_environment}-profile"
  location            = azurerm_resource_group.resource_group.location
  resource_group_name = azurerm_resource_group.resource_group.name

  container_network_interface {
    name = "${var.app_name}-${var.app_environment}-nic"

    ip_configuration {
      name      = "aciipconfig"
      subnet_id = azurerm_subnet.sn-aci.id
    }
  }
}

resource "azurerm_container_group" "container_group" {
  name                = "${var.app_name}-${var.app_environment}"
  location            = azurerm_resource_group.resource_group.location
  resource_group_name = azurerm_resource_group.resource_group.name
  ip_address_type     = "Private"
  os_type             = "Linux"
  # network_profile_id  = azurerm_network_profile.containergroup_profile.id
  subnet_ids          = [azurerm_subnet.sn-aci.id]

  container {
    name      = "${var.app_name}-${var.app_environment}-container"
    image     = "${var.docker_image}"
    cpu       = "${var.container_cpu}"
    memory    = "${var.container_memory}"

    ports {
      port     = 6789
      protocol = "TCP"
    }

    volume {
      name                 = "${var.app_name}-fs"
      mount_path           = "/home/src"
      storage_account_name = azurerm_storage_account.aci_storage.name
      storage_account_key  = azurerm_storage_account.aci_storage.primary_access_key
      share_name           = azurerm_storage_share.container_share.name
    }

    environment_variables = {
      "AZURE_CLIENT_ID"             = azuread_service_principal.app.application_id
      "AZURE_CLIENT_SECRET"         = azuread_service_principal_password.app.value
      "AZURE_STORAGE_ACCOUNT_NAME"  = var.storage_account_name
      "AZURE_STORAGE_ACCOUNT_KEY"   = azurerm_storage_account.aci_storage.primary_access_key
      "AZURE_SUBSCRIPTION_ID"       = data.azurerm_subscription.current.subscription_id
      "AZURE_RESOURCE_GROUP_NAME"   = azurerm_resource_group.resource_group.name
      "AZURE_CONTAINER_GROUP_NAME"  = "${var.app_name}-${var.app_environment}"
      "AZURE_TENANT_ID"             = azuread_service_principal.app.application_tenant_id
      "ULIMIT_NO_FILE"               = 16384
    }
  }

  tags = {
    Environment = "${var.app_environment}"
  }
}

output "ip" {
  value = azurerm_public_ip.public_ip.ip_address
}

output "id" {
  value = azurerm_container_group.container_group.id
}
