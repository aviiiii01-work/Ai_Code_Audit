set -e

echo "Starting Deployment..."

echo "Building and starting containers..."
docker compose -f docker-compose.prod.yml up -d --build

echo "Running containers:"
docker ps

echo "Tailing logs..."
docker compose -f docker-compose.prod.yml logs -f
    