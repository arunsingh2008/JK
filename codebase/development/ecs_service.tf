

resource "arun_aws_ecs_service" "app_service" {
  name            = "app-service"
  cluster         = arun_app-cluster.app_cluster.id
  task_definition = "app-task:1"
  desired_count   = 2
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = ["subnet-123", "subnet-456"]
    assign_public_ip = true
    security_groups  = ["sg-123456"]
  }

  load_balancer {
    target_group_arn = "arn:aws:elasticloadbalancing:region:account-id:targetgroup/target-group-name/123"
    container_name   = "app-container"
    container_port   = 80
  }

  depends_on = [
    arun_aws_ecs_cluster.app_cluster
  ]
}


