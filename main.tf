terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.71.0"
    }
  }
}

provider "azurerm" {
  skip_provider_registration = true # This is only required when the User, Service Principal, or Identity running Terraform lacks the permissions to register Azure Resource Providers.
  storage_use_azuread = true
  features {
    key_vault {
      purge_soft_delete_on_destroy    = true
      recover_soft_deleted_key_vaults = true
    }
  }
}

resource "azurerm_resource_group" "rg" {
  name = "azurelab-rg"
  location = "East Asia"
}

resource "random_string" "resource_code" {
  length  = 5
  special = false
  upper   = false
}

resource "azurerm_storage_account" "sa" {
  name                     = "azurelabinfra${random_string.resource_code.result}"
  location                 = azurerm_resource_group.rg.location
  resource_group_name      = azurerm_resource_group.rg.name
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_static_site" "web" {
  name                = "azurelab-web"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku_tier            = "Free"
  sku_size            = "Free"
}

# resource "azurerm_search_service" "search" {
#   name                = "azurelab-search-${random_string.resource_code.result}"
#   resource_group_name = azurerm_resource_group.rg.name
#   location            = azurerm_resource_group.rg.location
#   sku                 = "free"
# }

# resource "azurerm_cognitive_account" "vision" {
#   name                = "azurelab-vision-${random_string.resource_code.result}"
#   location            = azurerm_resource_group.rg.location
#   resource_group_name = azurerm_resource_group.rg.name
#   sku_name            = "F0"
#   kind                = "ComputerVision"
# }

# resource "azurerm_cognitive_account" "speech" {
#   name                = "azurelab-speech-${random_string.resource_code.result}"
#   location            = azurerm_resource_group.rg.location
#   resource_group_name = azurerm_resource_group.rg.name
#   sku_name            = "F0"
#   kind                = "SpeechServices"
# }

# resource "azurerm_cognitive_account" "language" {
#   name                = "azurelab-language-${random_string.resource_code.result}"
#   location            = azurerm_resource_group.rg.location
#   resource_group_name = azurerm_resource_group.rg.name
#   sku_name            = "F0"
#   kind                = "TextAnalytics"
#   custom_question_answering_search_service_id = azurerm_search_service.search.id
#   custom_question_answering_search_service_key = azurerm_search_service.search.primary_key
# }
