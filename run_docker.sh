docker rm unpddatabase
docker run -d -p 5000:5000 --name unpddatabase unpddatabase /app/run_server.sh
