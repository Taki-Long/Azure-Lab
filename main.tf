terraform {
  backend "local" {}
}

data "azurerm_resource_group" "azure_lab" {
  name = "Azure-Lab"
}

resource "azurerm_static_site" "azure_lab" {
  name                = "azure-lab"
  location            = data.azurerm_resource_group.azure_lab.location
  resource_group_name = data.azurerm_resource_group.azure_lab.name
  sku_tier            = "Free"
  sku_size            = "Free"
}
