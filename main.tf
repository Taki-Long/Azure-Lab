terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "azure_lab" {
  name = "Azure-Lab"
}

resource "azurerm_static_site" "azure_lab" {
  name                = "azure_lab"
  location            = azurerm_resource_group.azure_lab.location
  resource_group_name = azurerm_resource_group.azure_lab.name
  sku_tier = "Free"
  sku_size = "Free"
}
