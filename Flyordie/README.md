## Learning Path 

# 31-12-2020
Check url loading parameters:  Added references code from developer tools
- Git push, going outside for fireworks!

# 1-01-2021
    Learn about Frame Binary!
- https://tools.ietf.org/html/rfc6455 
- git push


Research:
```javascript
    var ARCHIVE = CODE_RELEASE + "/load.zip," + CODE_RELEASE + "/code.zip";
    var LOADCODE = CODE_RELEASE + "/code.zip";
    var DROOT = "http://" + "www.flyordie.com" + "/games/deploy/";
    if (JNLP) {
        DHOME = DROOT + PATH + '/';
        JARCHIVE = CODE_RELEASE + "/load.jar";
        if (JNLP < 3)
                JARCHIVE += "," + CODE_RELEASE + "/code.jar";
        AP('server', HOST);

```


3.  WebSocket URIs

   This specification defines two URI schemes, using the ABNF syntax
   defined in RFC 5234 [RFC5234], and terminology and ABNF productions
   defined by the URI specification RFC 3986 [RFC3986].
```javascript

          ws-URI = "ws:" "//" host [ ":" port ] path [ "?" query ]
          wss-URI = "wss:" "//" host [ ":" port ] path [ "?" query ]

          host = <host, defined in [RFC3986], Section 3.2.2>
          port = <port, defined in [RFC3986], Section 3.2.3>
          path = <path-abempty, defined in [RFC3986], Section 3.3>
          query = <query, defined in [RFC3986], Section 3.4>
```
   The port component is OPTIONAL; the default for "ws" is port 80,
   while the default for "wss" is port 443.

   The URI is called "secure" (and it is said that "the secure flag is
   set") if the scheme component matches "wss" case-insensitively.

   The "resource-name" (also known as /resource name/ in Section 4.1)
   can be constructed by concatenating the following:

   o  "/" if the path component is empty

   o  the path component

   o  "?" if the query component is non-empty

   o  the query component

   Fragment identifiers are meaningless in the context of WebSocket URIs
   and MUST NOT be used on these URIs.  As with any URI scheme, the
   character "#", when not indicating the start of a fragment, MUST be
   escaped as %23.


