# Key Value Store and in memory cache database
These are very fast in memory databases, which allow for very fast read and writes. These are generally used for caching the data that is expensive to read again and again, for example some complex sql query's result, or any other disk intensive or cpu intensive task result that could be cached.
These are also used for storing temporary variables on servers, like user sessions etc.
Example: redis, memcached

