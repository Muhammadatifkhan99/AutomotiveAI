To run the flask application please run  the script named app and then a post request, after wards send a get request to check the performance.

Post Request::::
 curl -X POST http://127.0.0.1:5000/upload -H "Content-Type: application/json" -d '{"timestamp":"2025-01-23T12:00:00Z","latitude":52.5200,"longitude":13.4050}'


Get Request::::
 curl http://127.0.0.1:5000/retrieve
