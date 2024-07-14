#!bin/bash

#Set the latest image name and tag in the Docker compose file
sed -E -i 's/image: [^ ]+\.dkr\.ecr/image: $AWS_ACCOUNT_ID\.dkr\.ecr/' app_compose_files/docker-compose-dev.yaml
sed -E -i'' "s/(.*amazonaws.com\/product_review:).*/\1$PRODUCT_REVIEW_VERSION-$ENVIRONMENT/" app_compose_files/docker-compose-dev.yaml 


#Deply the latest stack
sudo docker stack deploy --with-registry-auth --detach=false -c app_compose_files/docker-compose-dev.yaml app_stack