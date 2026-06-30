resource "aws_vpc" "finops_vpc" {

  cidr_block = var.vpc_cidr

  tags = {
    Name = "finops-vpc"
  }
}
resource "aws_subnet" "public_subnet" {

  vpc_id = aws_vpc.finops_vpc.id

  cidr_block = var.public_subnet_cidr

  availability_zone = "${var.aws_region}a"

  map_public_ip_on_launch = true

  tags = {
    Name = "finops-public-subnet"
  }
}
resource "aws_internet_gateway" "finops_igw" {

  vpc_id = aws_vpc.finops_vpc.id

  tags = {
    Name = "finops-igw"
  }
}
resource "aws_route_table" "public_rt" {

  vpc_id = aws_vpc.finops_vpc.id

  route {
    cidr_block = "0.0.0.0/0"

    gateway_id = aws_internet_gateway.finops_igw.id
  }

  tags = {
    Name = "finops-public-route-table"
  }
}
resource "aws_route_table_association" "public_assoc" {

  subnet_id = aws_subnet.public_subnet.id

  route_table_id = aws_route_table.public_rt.id
}

