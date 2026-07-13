output "instance_id" {
  value = aws_instance.finops_server.id
}

output "public_ip" {
  value = aws_instance.finops_server.public_ip
}

output "public_dns" {
  value = aws_instance.finops_server.public_dns
}

output "vpc_id" {
  value = aws_vpc.finops_vpc.id
}

output "subnet_id" {
  value = aws_subnet.public_subnet.id
}
