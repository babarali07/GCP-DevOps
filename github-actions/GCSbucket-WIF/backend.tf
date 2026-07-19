################################################################################
# Terraform State Backend Configuration
# This file configures remote state storage for Terraform.
# Remote state allows multiple users and CI/CD systems to work with the same
# infrastructure without conflicts.
################################################################################

# Configure Terraform to store state remotely in Google Cloud Storage (GCS).
# Remote state storage is essential for:
# - Keeping state consistent across GitHub Actions runs and local development
# - Enabling team collaboration on infrastructure
# - Preventing accidental state overwrites
terraform {
  backend "gcs" {
    bucket = "my-terraform-state-bucket-5647" # GCS bucket for storing state files
    prefix = "tf-ga-demo/terraform.tfstate"   # Path prefix for organizing state files
  }
}
