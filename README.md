# Api.ai - webhook implementation in Python

This is a really simple webhook implementation that gets Api.ai classification JSON (i.e. a JSON output of Api.ai /query endpoint) and returns a fulfillment response.

More info about Api.ai webhooks could be found here:
[Api.ai Webhook](https://docs.api.ai/docs/webhook)

# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
It's a trigger fulfillment service without any information retrieval which uses a local Web API 2.0 (or any!) backend server to do some work when triggered.
The service takes 3 parameters (@boolean-type, @subject-type, @location-type).

The action triggers a local lightbulb to turn on or off light ('light' is the @subject-type, 'on'/'off' is the @boolean-type and 'room' is the @location-type).

The service packs the result in the Api.ai webhook-compatible response JSON and returns it to Api.ai.

# Google Actions Privacy Policy
What information do I collect?
- Only data transmitted by the Action on Google API.AI is used at runtime. No logs are active, no post analysis of received data will be made. Nothing is collected at all!

How do I use the information?
- The data transmitted by the Action on Google API.AI is used at runtime by a backend service to evaluate which power socket to turn on or off. After processing the information is lost. No data transmittet will be used for any other purpose that controlling power sockets.

What information do I share?
- The webhook collects the intent transmitted by the Action and passes it on to a local backend for processing the voice parameters. After processing, data is gone. Nothing is shared.
