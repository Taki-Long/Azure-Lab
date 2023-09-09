terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">3.0.0"
    }
  }
}

provider "azurerm" {
  skip_provider_registration = true # This is only required when the User, Service Principal, or Identity running Terraform lacks the permissions to register Azure Resource Providers.
  features {
    key_vault {
      purge_soft_delete_on_destroy    = true
      recover_soft_deleted_key_vaults = true
    }
  }
}

data "azurerm_resource_group" "lab" {
  name = "Azure-Lab"
}

resource "azurerm_storage_account" "lab" {
  name                     = "azurelabinfra"
  location                 = data.azurerm_resource_group.lab.location
  resource_group_name      = data.azurerm_resource_group.lab.name
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_service_plan" "lab" {
  name                = "azure-lab"
  location            = data.azurerm_resource_group.lab.location
  resource_group_name = data.azurerm_resource_group.lab.name
  os_type             = "Linux"
  sku_name            = "Y1"
}

resource "azurerm_linux_function_app" "lab" {
  name                = "azure-lab-func"
  location            = data.azurerm_resource_group.lab.location
  resource_group_name = data.azurerm_resource_group.lab.name

  storage_account_name       = azurerm_storage_account.lab.name
  storage_account_access_key = azurerm_storage_account.lab.primary_access_key
  service_plan_id            = azurerm_service_plan.lab.id

  identity {
    type = "SystemAssigned"
  }

  site_config {
    application_stack {
      python_version = "3.10"
    }
  }
}

