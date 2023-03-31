provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "my-bucket" {
  name          = var.bucket_name
  location      = var.region
  storage_class = var.storage_class
}
