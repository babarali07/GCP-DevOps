################################################################################
# Google Cloud Provider Configuration
# This file configures the Terraform provider for Google Cloud Platform (GCP).
# It specifies the required provider version and authentication settings.
################################################################################

# Define the required Terraform provider for Google Cloud.
# This block specifies which provider plugin to use and which version is compatible.
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 7.0" # Use version 7.x (compatible updates)
    }
  }
}

# Configure the Google Cloud provider with authentication and default settings.
# These settings apply to all GCP resources created in this configuration.
provider "google" {
  project = var.project_id  # GCP project ID (from terraform.tfvars)
  region  = "us-central1"   # Default region for resources
  zone    = "us-central1-a" # Default zone for resources
}