sudo docker run -ti --rm -e CD_API_KEY=$CD_API_KEY -e CD_API_SECRET=$CD_API_SECRET \
-v $(pwd):/canvas_data \
canvas_cli_docker 
 
