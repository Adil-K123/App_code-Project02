#!/bin/bash

ENVIRONMENT="-$ENVIRONMENT"
PRODUCT_REVIEW_VERSION=$(git log -1 --pretty=%h)
REPO="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/product_review:"
TAG="$REPO$PRODUCT_REVIEW_VERSION$ENVIRONMENT"
#BUILD_TIMESTAMP=$( date '+%F_%H:%M:%S' )
docker build -t "$TAG" .
docker push "$TAG" 