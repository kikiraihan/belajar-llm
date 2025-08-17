# build (run once)
docker build -t bart-cli .

# run
<!-- docker run -it --rm --env-file .env bart-cli -->

<!-- default env -->
docker run -it --rm bart-cli

<!-- pake env file -->
docker run -it --rm --env-file .env bart-cli
