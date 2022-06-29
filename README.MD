# TwiFriendsMapper

The third part of the second lab this semester was to develop a basic web app, which used Twitter API and geocoding.
**Note:** the app itself is located in *third* folder. Two other folders contain other lab tasks.

### Technologies and Libraries Used

- **FastAPI** for creating a simple web server
- **Jinja** for managing the templates
- **Uvicorn** for deploying the development server
- **Twitter API** for getting data from Twitter
- **Nominatim** for geocoding locations
- **Folium** for creating a web map with python

### Usage

**Note:** first of all you have to generate bearer token at [developer.twitter.com](https://developer.twitter.com/en/products/twitter-api) and put it as BEARER variable in bearer.py.

To start a local server, type `uvicorn main:app --host 0.0.0.0 --port 80` into the command line.
Then go to the localhost address.

At the root ('/') user is suggested to enter someone's Twitter username.

![index_html](/images//index_html_example.png)

At this moment, the program requests user id from Twitter API, and then it once again requesuses the API to get user's friends (basically accounts he/she follows).
After that, we iterate over friends. If their location is adequate and can be geocoded, they are added to the dictionary where coordinates is the key, and location name and friend list are the value.
At the next step, module uses Folium to get an .html map with all of the friends with location on it.
Finally, the map.html template page is rendered with an .html map inside of iframe on it.

![map.html](/images/map_html_example.png)

### Summary

Doing this interesting project I learned the basics of deploying a development server (using FastAPI and Uvicorn) and getting data with the API (using requests library)
