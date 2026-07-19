################################################################################
# Google Cloud Storage (GCS) Bucket
# This file defines the storage resources for this Terraform demo.
################################################################################

# Create a Google Cloud Storage bucket for this Terraform demo.
# This bucket will be used for storing application data and artifacts.
# Terraform will manage this bucket and keep its lifecycle in sync with
# the configuration defined here.
resource "google_storage_bucket" "my-bucket" {
  name          = var.bucket_name # Bucket name (from terraform.tfvars)
  location      = "US"            # Geographic location (US multi-region)
  force_destroy = true            # Allow Terraform to delete bucket even if it contains objects

  # Enable uniform bucket-level access control
  # This disables object-level ACLs and uses only bucket-level IAM policies
  uniform_bucket_level_access = true

  # Enforce public access prevention
  # This prevents accidental public access to bucket contents
  public_access_prevention = "enforced"
}

#test3