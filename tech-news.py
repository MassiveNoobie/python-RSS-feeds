# techcrunch.com news aggregator
import requests
from bs4 import BeautifulSoup
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
import requests
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
  """Return the source code for the provided URL.

  Args:
      url (string): URL of the page to scrape.

  Returns:
      response (object): HTTP response object from requests_html.
  """

  try:
    session = HTMLSession()
    response = session.get(url)
    return response

  except requests.exceptions.RequestException as e:
    print(e)

def get_feed(url):
  """Return a Pandas dataframe containing the RSS feed contents.

  Args:
      url (string): URL of the RSS feed to read.

  Returns:
      df (dataframe): Pandas dataframe containing the RSS feed contents.
  """

  response = get_source(url)

  df = pd.DataFrame(columns=['guid'])

  with response as r:
    items = r.html.find("item", first=False)

    for item in items:
      guid = item.find('guid', first=True).text

      row = {'guid': guid}


      df = df.append(row, ignore_index=True)

  return df

print('getting rss link')
url = "https://techcrunch.com/feed/"

df = get_feed(url)
pd.set_option("display.max_colwidth", -1)
#print(df)

#print(df.head(2))
#link = (df.head(2))

# turn data frame into list
ne = df.values.tolist()
#print(ne)

# author of blog
wp = Client('https://YOURWORDPRESSTHING.com/xmlrpc.php', 'ADMIN52', 'PASSWORD1')

#loop through list
for x in ne:
  #print(x)
  print(str(x)[2:-2])
  y = (str(x)[2:-2])
  # url to parse
  url = y

  html_text = requests.get(y).text
  soup = BeautifulSoup(html_text, 'html.parser')
  # print(soup)

  images = soup.findAll('img')
  for image in images:
    # print image source
    # just grab "src="value"" value out of src
    bet = str(image['src'])

  # print(soup)
  # getting header1 html
  head1 = (soup.title.string)
  # print(head1)

  # calling header text a string so it's no longer soup
  head2 = str(head1)
  htmlimg = ('<img src="', bet, '" alt="', head2, '">')

  pic = ''.join(htmlimg)
  # print(pic)
  # getting body html
  body = soup.find_all('p')

  # calling it string so it's not soup
  news = str(body)[:-1][1:]

  ### cleaning the body

  # split on "<" to create list to clean the code and leave for further list cleaning operations
  snews = (news.split("<"))

  # fixing split, adding "<" to left side to fix html
  my_list = snews
  string = "<"
  my_new_list = [string + x for x in my_list]

  # print(my_new_list)

  # remove top code, cleans blog output, removing unncessary code
  n = 1
  newlist = my_new_list[n:]

  # turning into single string
  cleannews = ' '.join(newlist)
  ###

  # calling it a string
  stringconvert = str(cleannews)

  # removing unnessary padded "comma" after '</p>,' replacing with proper html
  #cleanestnews = (stringconvert.replace('</p>,', '</p>'))

  newsimage = (stringconvert + pic)

  #
  post = WordPressPost()
  post.post_status = 'publish'
  post.title = head2
  post.content = newsimage
  post.terms_names = {
    'post_tag': ['Startup', 'TechCrunch'],
    'category': ['Tech']
  }
  ## post to blog
  wp.call(NewPost(post))
  print('Published 1 new TECH blog //' + head1 + '// on URWORDPRESSSITE.com!!!1')
