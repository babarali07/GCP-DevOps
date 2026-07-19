################################################################################
# Input Variables
# This file defines input variables for this Terraform configuration.
# Variables allow you to customize the infrastructure without modifying the code.
# Values are typically provided in terraform.tfvars or via command-line flags.
################################################################################

# GCP Project ID
# This is the unique identifier for your Google Cloud Platform project.
# Required for authenticating and managing resources in GCP.
variable "project_id" {
  type        = string
  description = "The GCP project ID where resources will be created"
}

# Google Cloud Storage Bucket Name
# This is the name of the GCS bucket to create.
# Bucket names must be globally unique across all GCP projects.
variable "bucket_name" {
  type        = string
  description = "The name of the Google Cloud Storage bucket for this deployment"
}
