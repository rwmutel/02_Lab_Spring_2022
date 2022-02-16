# 02_Lab_Spring_2022

Probably the most interesting laboratory work assignment I had so far

## Second task

Folder 'second' contains python module which let's user explore .json file with command line interface.
The default file is 'friends.json', which is a response from Twitter API, containing all the users Serhiy Zhadan follows on Twitter. User can change the default file by entering path in command line

## Third task

This task is way more complcated thus interesting. It's a web app which asks user for Twitter username and shows him a map of users specified user follows.

### Technologies and Libraries Used

- **FastAPI** for creating a simple web server
- **Twitter API** for getting data from Twitter
- **Nominatim** for geocoding locations
- **Folium** for creating a web map with python

### Usage

**Note:** first of all you have to generate bearer token at [developer.twitter.com](https://developer.twitter.com/en/products/twitter-api) and put it as BEARER variable in bearer.py.

At the root ('/') user is suggested to enter someone's Twitter username.

![index_html](/images//index_html_example.png)

At this moment, the program requests user id from Twitter API, and then it once again requesuses the API to get user's friends (basically accounts he/she follows).
After that, we iterate over friends and if their location is adequate and can be geocoded, they are added to the dictionary where coordinates is the key, and location name and friend list are the value.
At the next step, module uses Folium to get an .html map with all of the friends with location on it.
Finally, the map.html template page is rendered with an .html map inside of iframe on it.

![map.html](/images/map_html_example.png)
