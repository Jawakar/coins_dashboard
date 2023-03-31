# Setting up a GCS bucket using Terraform

This guide will walk you through the process of setting up a Google Cloud Storage (GCS) bucket using Terraform.

## Prerequisites

Before you begin, you will need to have the following:

* A Google Cloud Platform (GCP) account and project
* The `gcloud` command-line tool installed and authenticated with your GCP project
* The Terraform CLI installed on your local machine

## Steps

Follow these steps to create a GCS bucket using Terraform:

1. Clone this repository to your local machine.
2. Navigate to the `terraform` directory.
3. Create a file named `terraform.tfvars` and enter the following content, replacing the values with your own:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>makefile</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-makefile">project_id     = "your-gcp-project-id"
bucket_name    = "your-gcs-bucket-name"
region         = "your-gcs-bucket-region"
storage_class  = "your-gcs-bucket-storage-class"
</code></div></div></pre>

4. Create a file named `variables.tf` with the following content:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>go</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-go">variable "project_id" {
  description = "The ID of the GCP project"
  type        = string
}

variable "bucket_name" {
  description = "The name of the GCS bucket to create"
  type        = string
}

variable "region" {
  description = "The region to create the GCS bucket in"
  type        = string
}

variable "storage_class" {
  description = "The storage class to use for the GCS bucket"
  default     = "STANDARD"
  type        = string
}
</code></div></div></pre>

5. Create a file named `gcp_bucket.tf` with the following content:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>java</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-java">provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "my-bucket" {
  name          = var.bucket_name
  location      = var.region
  storage_class = var.storage_class
}
</code></div></div></pre>

6. Run `terraform init` to initialize the Terraform workspace.
7. Run `terraform plan` to preview the changes that Terraform will make to your infrastructure.
8. If you're satisfied with the plan, run `terraform apply` to create the GCS bucket in GCP.
9. Verify that the bucket was created in your GCP console or by running the `gsutil` command.

## Conclusion

Congratulations! You have now set up a GCS bucket using Terraform. You can modify the variables in `terraform.tfvars` and run `terraform apply` again to make changes to your infrastructure.

If you have any questions or run into any issues, please refer to the Terraform documentation or feel free to contact us.

I hope this helps! Let me know if you have any further questions.
