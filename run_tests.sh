docker build -t fastapi-test -f Dockerfile.test .
docker run --rm -v $PWD:/app fastapi-test
