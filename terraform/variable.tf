variable "project_id" {
  description = "The ID of the GCP project"
  default = "jawa-378700"
}

variable "bucket_name" {
  description = "The name of the GCS bucket to create"
  default = "coin_data_raw"
}

variable "region" {
  description = "The region to create the GCS bucket in"
  default = "asia-south1"
}

variable "storage_class" {
  description = "The storage class to use for the GCS bucket"
  default     = "STANDARD"
}
