#!/bin/bash

client_id=$(cat CLIENT_ID)
#echo $client_id

client_secret=$(cat CLIENT_SECRET)
#echo $client_secret

curl -s -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=$client_id&client_secret=$client_secret" | jq
