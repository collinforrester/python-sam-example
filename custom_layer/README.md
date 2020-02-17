# Python Custom Layer

This is a custom lambda layer to demonstrate how you can package common function dependencies to make authoring business logic functions easier.

## Defining dependencies
Add them to requirements.txt and run `./build.sh` to install them locally.

## Publishing a new version
After running `./build.sh` and verifying your dependencies installed, run the following:

```bash
./publish.sh
```

This will publish the layer into your account, returning the JSON response.  You need the layer ARN to add as a layer dependency to your other function.

You can use `./recall.sh` to get the latest ARN of the layer as a shortcut.

## More Background on Layers with Docker
https://aws.amazon.com/premiumsupport/knowledge-center/lambda-layer-simulated-docker/