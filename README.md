# Api.ai - webhook implementation in Python

This is a really simple webhook implementation that gets Api.ai classification JSON (i.e. a JSON output of Api.ai /query endpoint) and returns a fulfillment response.

More info about Api.ai webhooks could be found here:
[Api.ai Webhook](https://docs.api.ai/docs/webhook)

# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
It's a trigger fulfillment service without any information retrieval that uses a local Web API 2.0 (or any!) backend server to do some work when triggered.
The services takes 3 parameters as actions (@boolean-type, @subject-type, @location-type).
The action triggers a local lightbulb to turn on or off (light is the @subject-type, on/off is the @boolean-type and the room is the @location-type).

The service packs the result in the Api.ai webhook-compatible response JSON and returns it to Api.ai.

