provider "kubernetes" {
  config_path            = "~/.kube/config"
  config_context_cluster = "minikube"
}

resource "kubernetes_deployment" "ranchbot" {
  metadata {
    name = "ranchbot-deployment"
  }

  spec {
    replicas = 3

    selector {
      match_labels = {
        app = "ranchbot"
      }
    }

    template {
      metadata {
        labels = {
          app = "ranchbot"
        }
      }

      spec {
        container {
          name  = "ranchbot"
          image = "shnauzerr/ranchbot:latest"
          env {
            name = "DISCORD_API_KEY"
            value_from {
              secret_key_ref {
                name = "discord-api-key"
                key  = "DISCORD_API_KEY"
              }
            }
          }
          env {
            name = "GEO_API_KEY"
            value_from {
              secret_key_ref {
                name = "geo-api-key"
                key  = "GEO_API_KEY"
              }
            }
          }
          env {
            name = "MOZAM_API_KEY"
            value_from {
              secret_key_ref {
                name = "mozam-api-key"
                key  = "MOZAM_API_KEY"
              }
            }
          }
          env {
            name = "WEATHER_API_KEY"
            value_from {
              secret_key_ref {
                name = "weather-api-key"
                key  = "WEATHER_API_KEY"
              }
            }
          }
        }
      }
    }
  }
}
