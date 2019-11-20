# Photography Locations - Data Centric Milestone Project @ Code Institute

## Project purpose

To build a full-stack site that allows users to manage a common dataset about a particular domain

## My aims with the project

- Practice and learn Flask and MongoDb in more detail.
- Set myself a hard deadline and build as much as possible into the project within a short timeframe (focusing mostly on the backend, especially the database handling).
- Despite the tough deadline, 90% score in project evaluation at Code Institute.

This way I kind of model real life situations with tough deadlines and meeting customer expectations. (I aimed the highest possible score and top quality with previous
two milestone projects, but it took relatively long time to complete them, due to the extensive content. That's not realistic. One has to stop adding features, otherwise the 
project's never going to be finished.)

## Value provided:
1.	Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.
2.	The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner might also benefit from the 
collection of the dataset as a whole.

## My Project idea - Photography Locations
Create an on-line landscape & cityscape photography location recommendation site. Users can upload their landscape images with location information, to recommend places to 
visit for landscape photographers (hobbyists and pros as well). They can also help the community with providing detailed info about their pictures or useful hints and tips.

### External user’s goal:

#### Find ideas for landscape photo locations
Users seeking for opportunities can search the site for location ideas either near their place or around their upcoming trips. They can also plan their next holiday to visit
places they got inspired about.

#### Get inspiration from pictures they like
High quality pictures can inspire others to try and achieve similar results, either at the same location or a similar they know of.

#### Get hints how to approach photographing a particular site 
Check what equipment others used, what technique they applied. Also they may figure out what the best season or time of the day it is to visit a particular scene.

Site owner’s goal may include:
#### Build an extensive location database 
A go-to place for landscape photographers.

#### Promote their web shop of photo equipment and accessories 

#### Advertising their photography courses 

# UX

## Strategy

Present a visually appealing site with landscape and city images, inspiring and helping photographers to find outstanding (potentially not widely-known) locations.

Users should be able to browse images and locations conveniently.

## Scope

### Which features to include in the design? What's on the table for now?

On top of the obvious CRUD operations, must have elements are:
- Map view with all geo-coordinates displayed from database. (Advanced feature but this is the single best option to display locations)
- Overview page with postcard type display of (selected) database records (with limited information to save real estate)
- Detailed view with larger image and full info from database

## Structure

### Page structure

#### Home page
To attract users and highlight key features, including a map, displaying all the database entries.

#### Search page for browsing and filtering the images/locations.
Display images with key information and provide filtering and sorting tools for users. This is where they can start exploring from, therefore 
the images/cards should serve as a springboard for the exploration, clicking on them will bring more details.

#### Detailed view
To display all the available information about each database entry.

#### Housekeeping (CRUD):
1. **C**reate new entry
2. **R**ead (Display) entries - the detailed view
3. **U**pdate entries - allows to make changes to existing records
4. **D**elete entries

### Database structure:
MongoDB data on Atlas with the following collections:
1.	Details:
→ Title
- Category name
- Country
- Region/City
- Post code,
- Latitude,
- Longitude,
- Image URL,
- Camera,
- Lens,
- Filter(s),
- Name of photographer
- Tripod (yes-no)
- Description
- Date created/modified
- Number of views
- Number of likes
2.	Categories:
- Landscape
- Cityscape
- Cloudscape
- Seascape

## Skeleton

### Wireframe sketches:

[Search page: ](documentation/wireframes/wireframe_search.jpg)
[Details page: ](documentation/wireframes/wireframe-details-view.jpg)

## Surface

For the home page, I wanted to use a strong background image and big bold letters to draw attention, then the map under the headlines.

## User stoies
Translating it to user stoies I wanted to:


# Design


# Features


# Technologies used

[*HTML*](https://en.wikipedia.org/wiki/HTML5) 
[*CSS*](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
[Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) framework, more specifically 
[**Bootswatch Cyborg theme**](https://bootswatch.com/cyborg/).   

[*JavaScript*](https://www.javascript.com/), I used [*jQuery*](https://jquery.com/) library to simplify DOM manipulation.

# Testing

## Test planning

During testing, I wanted to test:

- design and responsiveness: to see if I like the look and feel of the game on different devices and screen sizes,
- functioning and operability in different browsers (mobile and pc),
- against user stories,
- against misbehaviour (defensive design).

## Design and responsiveness


## Functioning and operability

### JavaScript

**There were several bugs, a few of the interesting ones:**

### Testing in different browsers

**Chrome**

**Safari**

**Firefox**

## Testing against the user stories


## Defensive testing


# Deployment

## Differences between the deployed production version and the development version


# Credits

## Content

## Media
Images are either my own or of family and frends (names, nicknames of photographers indicated in the database), uploaded by them.

## Acknowledgements

Thanks to Ali Ashik - my mentor - 

Advice from Code Institute Slack community has also helped me to learn about debugging in *JavaScript*. 