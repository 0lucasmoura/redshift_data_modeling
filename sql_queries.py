import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create = 
("""
CREATE TABLE IF NOT EXISTS staging_events
             (
                          event_id      INT       IDENTITY(0,1) PRIMARY KEY,
                          artist        VARCHAR   NULL,
                          auth          VARCHAR   NULL,
                          firstname     VARCHAR   NULL,
                          gender        VARCHAR   NULL,
                          iteminsession INT       NULL,
                          lastname      VARCHAR   NULL,
                          length        FLOAT     NULL,
                          level         VARCHAR   NULL,
                          location      VARCHAR   NULL,
                          method        VARCHAR   NULL,
                          page          VARCHAR   NULL,
                          registration  VARCHAR   NULL,
                          sessionid     INT       NOT NULL,
                          song          VARCHAR   NULL,
                          status        VARCHAR   NULL,
                          ts            TIMESTAMP NOT NULL,
                          useragent     VARCHAR   NULL,
                          userid        INT       NULL
             );
""")

staging_songs_table_create = 
("""
CREATE TABLE IF NOT EXISTS staging_songs 
    (
                staged_song_id   INT       IDENTITY(0,1) PRIMARY KEY,
                num_songs        INT       NULL,
                artist_id        VARCHAR   NOT NULL,
                artist_latitude  VARCHAR   NULL,
                artist_longitude VARCHAR   NULL,
                artist_location  VARCHAR   NULL,
                artist_name      VARCHAR   NULL,
                song_id          VARCHAR   NOT NULL,
                title            VARCHAR   NULL,
                duration         FLOAT     NULL,
                year             INT       NULL
    );
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
    (
        songplay_id INT       IDENTITY(0,1) PRIMARY KEY,
        start_time  TIMESTAMP NOT NULL,
        user_id     INT       NOT NULL,
        level       VARCHAR   NULL,
        song_id     VARCHAR   NOT NULL,
        artist_id   VARCHAR   NOT NULL,
        session_id  INT NOT   NULL,
        location    VARCHAR   NULL,
        user_agent  VARCHAR   NULL
    ); 
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
  (
     user_id    INT       PRIMARY KEY,
     first_name VARCHAR   NULL,
     last_name  VARCHAR   NULL,
     gender     VARCHAR   NULL,
     level      VARCHAR   NULL
  ); 
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
  (
     song_id   VARCHAR   PRIMARY KEY,
     title     VARCHAR   NULL,
     artist_id VARCHAR   NOT NULL,
     year      INT       NULL,
     duration  INT       NULL
  ); 
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
  (
     artist_id VARCHAR PRIMARY KEY,
     name      VARCHAR NULL,
     location  VARCHAR NULL,
     latitude  INT     NULL,
     longitude INT     NULL
  ); 
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
  (
     start_time TIMESTAMP PRIMARY KEY,
     hour       INT       NOT NULL,
     day        INT       NOT NULL,
     week       INT       NOT NULL,
     month      INT       NOT NULL,
     year       INT       NOT NULL,
     weekday    VARCHAR   NOT NULL
  ); 
""")

# STAGING TABLES

staging_events_copy = ("""

                        """).format()


staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""

""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
