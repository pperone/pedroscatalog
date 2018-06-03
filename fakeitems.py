from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Fake user
user1 = User(name="Pedro Perone", email="pperone@gmail.com",
             picture='http://pedroperone.com/profpic.jpg')
session.add(user1)
session.commit()

# Bands for Folk category
category1 = Category(name="folk", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Fleet Foxes", user_id=1, description="Fleet Foxes is an American indie folk band formed in Seattle, Washington. Their first two albums were released by the Sub Pop and Bella Union record labels, with their third by Nonesuch and Bella Union. The band came to prominence in 2008 with the release of their second EP, Sun Giant, and their self-titled debut album.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="The Lumineers", user_id=1,  description="The Lumineers are an American folk rock/Americana band based in Denver, Colorado. The founding members are Wesley Schultz (lead vocals, guitar) and Jeremiah Fraites (drums, percussion). Schultz and Fraites began writing and performing together in Ramsey, New Jersey in 2005. Cellist and vocalist Neyla Pekarek joined the band in 2010. The Lumineers emerged as one of the most popular folk rock/Americana artists during the revival of those genres and their growing popularity in the 2010s.", category=category1)

session.add(item2)
session.commit()

# Bands for Indie category
category2 = Category(name="indie", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Pinback", user_id=1, description="Pinback is an indie rock band from San Diego, California. The band was formed in 1998 by singers, songwriters and multi-instrumentalists Armistead Burwell Smith IV and Rob Crow, who have been its two consistent members.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Rogue Wave", user_id=1,  description="Rogue Wave is an indie rock band from Oakland, California, and headed by Zach Schwartz (a.k.a. Zach Rogue) who created the band after losing his job in the dot-com bust. Their first album was Out of the Shadow which was released privately in 2003 and re-released in 2004. In the fall of 2004 they went on a national tour of the United States.", category=category2)

session.add(item2)
session.commit()

# Bands for Classic category
category3 = Category(name="classic", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Fleetwood Mac", user_id=1, description="Fleetwood Mac are a British-American rock band, formed in London in 1967. The band has sold more than 100 million records worldwide, making them one of the world's best-selling bands.", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Talking Heads", user_id=1, description="Talking Heads was an American rock band formed in 1975 in New York City and active until 1991. The band comprised David Byrne (lead vocals, guitar), Chris Frantz (drums), Tina Weymouth (bass), and Jerry Harrison (keyboards, guitar). Described by the critic Stephen Thomas Erlewine as \"one of the most critically acclaimed bands of the '80s, the group helped to pioneer new wave music by integrating elements of punk, art rock, funk, and world music with avant-garde sensibilities and an anxious, clean-cut image.", category=category3)

session.add(item2)
session.commit()

# Bands for Instrumental category
category4 = Category(name="instrumental", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="Explosions in the Sky", user_id=1, description="Explosions in the Sky is an American post-rock band from Texas. The quartet originally played under the name Breaker Morant, then changed to the current name in 1999. The band has garnered popularity beyond the post-rock scene for their elaborately developed guitar work, narratively styled instrumentals - what they refer to as \"cathartic mini-symphonies\" - and their enthusiastic and emotional live shows.", category=category4)

session.add(item1)
session.commit()

item2 = CategoryItem(name="The Go! Team", user_id=1, description="The Go! Team are a six-piece band from Brighton, England. They combine indie rock and garage rock with a mixture of blaxploitation and Bollywood soundtracks, double Dutch chants, old school hip hop and distorted guitars. Their songs are a mix of live instrumentation and samples from various sources.", category=category4)

session.add(item2)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
