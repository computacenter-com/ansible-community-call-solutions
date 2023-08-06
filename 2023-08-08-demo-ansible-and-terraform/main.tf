terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
    ansible = {
      version = "~> 1.1.0"
      source  = "ansible/ansible"
    }
  }
}

provider "docker" {}

resource "docker_image" "rocky9" {
  name = "timgrt/rockylinux9-ansible:latest"
}

# Definition of Ansible Group and variables
resource "ansible_group" "group" {
  name     = "test_group"
  children = ["test_dc1", "test_dc2"]
  variables = {
    ansible_user       = "ansible"
    ansible_connection = "docker"
  }
}

# Definition and Ansible Host-Variables for first test instance
resource "docker_container" "instance1" {
  image = docker_image.rocky9.image_id
  name  = "test-instance1"
  cgroupns_mode = "host"
  privileged = "true"
  ports {
    internal = "80"
    external = "8080"
    ip       = "0.0.0.0"
  }
  volumes {
    host_path      = "/sys/fs/cgroup"
    container_path = "/sys/fs/cgroup"
  }
  volumes {
    host_path      = "/var/lib/containerd"
    container_path = "/var/lib/containerd"
  }
  entrypoint = ["/usr/lib/systemd/systemd", "--system"]
  command = ["sleep", "infinity"]
}

resource "ansible_host" "instance1" {
  name   = docker_container.instance1.name
  groups = ["test_dc1"]
}

# Definition and Ansible Host-Variables for first test instance
resource "docker_container" "instance2" {
  image = docker_image.rocky9.image_id
  name  = "test-instance2"
  cgroupns_mode = "host"
  privileged = "true"
  ports {
    internal = "80"
    external = "8081"
    ip       = "0.0.0.0"
  }
  volumes {
    host_path      = "/sys/fs/cgroup"
    container_path = "/sys/fs/cgroup"
  }
  volumes {
    host_path      = "/var/lib/containerd"
    container_path = "/var/lib/containerd"
  }
  entrypoint = ["/usr/lib/systemd/systemd", "--system"]
  command = ["sleep", "infinity"]
}

resource "ansible_host" "instance2" {
  name   = docker_container.instance2.name
  groups = ["test_dc2"]
}