# The lemon.markets Market Data API
This repository contains an example project that demonstrates the 
functionality of the [lemon.markets](https://www.lemon.markets/)
Market Data API.
## Project Structure
This project contains a MarketData model, which you can find in the 
**models** folder. In there, we define all relevant functions 
for the Market Data API.

All helper functions are defined in the helper.py file. 

In the main file, we define functions for the actual requests with the 
/venues/, /instruments/, /quotes/, /ohlc/, and /trades/ endpoints. 

## Set up
To test locally, clone this repo, use the IDE of your choice to run (although we highly recommend PyCharm) and install
all required packages through the provided requirements.txt file.

### Set environment variables
If you want to test locally, you need to define a number of environment variables.

| ENV Variable    |               Explanation               |  
|-----------------|:---------------------------------------:|
| DATA_API_KEY    |        Your Market Data API Key         |     |
| MIC             | Market Identifier Code of Trading Venue |


## Deploy to Heroku
If you are interested in hosting this project in the cloud, 
we suggest that you use Heroku to do so. To make the hosting 
work, you need to create a new project and connect 
your GitHub repo. You can find a good explanation [here](https://dev.to/josylad/how-to-deploy-a-python-script-or-bot-to-heroku-in-5-minutes-9dp).
Additionally, you need to specify the environment variables
through heroku directly. You can do so by either using:

```
heroku config:set [KEY_NAME=value …]
```
or by adding them in your project in the Heroku Dashboard under 
/Settings/Config Vars. 

Use this button to deploy to Heroku directly.


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/lemon-markets/lemon-markets/content-market-data-api-lemon-markets)

## Contribute to this repository
lemon.markets is an API from developers for developers. Therefore, we highly encourage you 
to get involved by opening a PR or contacting us directly via 
[support@lemon.markets](mailto:support@lemon.markets).

---

Have fun and happy coding,

your 🍋.markets team