# build (run once)
docker build -t text-classifier-terminal .

# run
<!-- docker run -it --rm --env-file .env text-classifier-terminal -->

<!-- default env -->
docker run -it --rm text-classifier-terminal

<!-- pake env file -->
docker run -it --rm --env-file .env text-classifier-terminal
