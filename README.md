# example-upload
How to upload data to SimSage from an external source programmatically.
Go to the `python` folder in this repository to view a code example.

## API & Security

SimSage is built with sophisticated levels of security.  We support single-SignOn through JWTs, and document level access control (Access Control Lists, aka. ACLs) that are baked into our indexes (graph) and SimSage `memory` structures.

The external crawler upload uses a *SID* (security ID) to POST information to SimSage.  Random SIDs are generated by SimSage for each knowledge-base and can be refreshed through the admin UX (or using our SaaS platform API).  
This SID acts as a password for external sources/crawlers.  Please do not share this SID with anyone outside your organisation as that would enable them to POST information into your knowledgebase (if they had access to the platform beyond the firewall).

### Query security
If you've enable SimSage indexing, you can query the data you've uploaded using our Semantic Search Engine.

* We can run querying SimSage in anonymous mode, not using any security for viewing data (selectable per source).
* We can set up Single Sign On (SSO) for auto user/ACL/Role creation for a given organisation and use SSO for querying SimSage.
* We can set up user-name/password access to the query engine (not recommended).

## Relevant APIs

Below is an example of how you can upload a document to your organisation/knowledge-base instance of SimSage and then query it. 

Our sample document is a simple text document, however SimSage can consumer and convert around 300 different types of documents. It does this through a series of libraries and using binary data associated with a mime-type.

Let’s assume this document (or piece of data) is called `test.txt` and let’s assume its content is a single sentence: *Robert often works in recruitment.\n* making for 35 bytes of ASCII/UTF-8 text.

SimSage will need to know the `hash` of that document (to detect changes), and the `base64 encoded` content of that document (We base64 encode the content so it can be posted inside our JSON).
We recommend making the `ACLs` associated with that document part of the `hash`, so that any change in security is picked up as a change to the document.


## POSTing document data to SimSage
Using Linux I can create a hash for the content (without the document ACLs) as follows for demonstration purposes:

`Robert often works in recruitment.\n`

```
# let's get an md5 sum for test.txt
> md5sum test.txt

	38957c50ca1330c74b702655fb1981bf
	
# let's encode the content of test.txt as a base64 string
> base64 test.txt

	Um9iZXJ0IG9mdGVuIHdvcmtzIGluIHJlY3J1aXRtZW50Lgo=

# This string can be up to 50MB in size (configurable).  This string must be prefixed with ;base64, before POSTing.  
```

The final SimSage concept you’ll need is that of a `run-id`. This property isn’t directly relevant to this upload, but the API will insist on one being passed. A `run-id` is simply a random GUID, which represents a single run through the data of a remote system. Its purpose is detect which files are no longer present after running through certain kinds of external systems.  You must use the same `run-id` while you're uploading all your data.  You must change the `run-id` in subsequent runs through the same data (e.g. to upload any changes).

### Example

We POST data using JSON (see below).  The JSON data required is as follows (all parameters are required, unless marked as *Optional*)
*NB:* The below aren’t real Ids, please do not use these!

| field          | example                                                   | meaning                                                                                                                  |
|----------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| organisationId | 9e8e81cf-408a-400c-9202-b1c2eb194797                      | the fixed SimSage assigned `organisation-id` of your SimSage organisation                                                | 
| kbId           | 4f20f106-362a-4541-bdc7-938ddb96a7a7                      | The fixed SimSage assigned `knowledgebase-id` of your SimSage knowledge-base inside that organisation                    |
| sid            | dd59988d-7740-444e-8cda-f670b8ce28ba                      | the SimSage assigned `sid` (security id) for the above knowledge-base                                                    |
| sourceId       | 1                                                         | the `id` of the source set up in SimSage listening for your data uploads                                                 |
| runId          | e8e36035-dada-4f47-8123-59d42a74881c                      | a random GUID you generate for each run through your data, used for detecting deleted files                              |
| url            | /some/folder/test.txt                                     | a unique ID used as a primary-key by SimSage to store the data                                                           |
| mimeType       | text/plain                                                | the data-type / document-type of the `data` POSTed.  SimSage supports over 300 document types.  Use the right mime-type. |
| acls           | {"acl": "user@simsage.ai", "access": "R", "isUser": true} | a list of security (Access Control List) associated with this data                                                       |
| title          | test document                                             | the title for this data / document.  *Optional*                                                                          |
| author         | Rock                                                      | the name of the author of this document.  *Optional*                                                                     |
| hash           | 38957c50ca1330c74b702655fb1981bf                          | a unique content-hash for detecting future content changes.  What hashing algorithm you use is up to you.                |
| data           | ;base64,Um9iZXJ0IG9mdGVuIHdvcmtzIGluIHJlY3J1aXRtZW50Lgo=  | a base64 encoded entity encapsulating the original document you're POSTing.  Must start with ";base64,"                  |
| created        | 1659695061000                                             | a Unix date-time stamp describing when this document was created.                                                        |
| lastModified   | 1659695060000                                             | a Unix date-time stamp describing when this document was last modified                                                   |
| metadata       | {"name1": "value1", "name2": "value2"}                    | a hash-map with unique name/value pairs to be indexed along with the other data of this document.  *Optional*            |
| size           | 35                                                        | the size in bytes of the binary/text of the data posted.  Not the size of the base64 string!                             |

Now we have all the information we can upload some data into your SimSage instance.
The following CURL command shows what to POST.

```shell
curl -X POST \
	-H 'Content-Type: application/json'  \
	-H 'API-Version: 1' \
	-d '{"organisationId": "9e8e81cf-408a-400c-9202-b1c2eb194797", \
	     "kbId": "4f20f106-362a-4541-bdc7-938ddb96a7a7", \
	     "sid": "dd59988d-7740-444e-8cda-f670b8ce28ba", \
	     "sourceId": 1, "runId": "e8e36035-dada-4f47-8123-59d42a74881c", \
	     "url": "/some/folder/test.txt", "mimeType": "text/plain",  \
	     "acls": [{"acl": "user@simsage.ai", "access": "R", "isUser": true}, \
	     {"acl": "some group", "access": "R", "isUser": false}], \
	     "title": "test document", "author": "Rock", \
	     "hash": "38957c50ca1330c74b702655fb1981bf", \
	     "data": ";base64,Um9iZXJ0IG9mdGVuIHdvcmtzIGluIHJlY3J1aXRtZW50Lgo=", \
	     "created": 1659695061000, \ 
	     "lastModified": 1659695061000, \
	     "metadata": {"name1": "value1", "name2": "value2"}, "size": 35}' \
	https://your-simsage-instance.simsage.ai/api/crawler/external/document/upload
```

*NB.* this `curl` is best executed as a single line command like so

```shell
curl -X POST -H 'Content-Type: application/json'  -H 'API-Version: 1' -d '{"organisationId": "9e8e81cf-408a-400c-9202-b1c2eb194797", "kbId": "4f20f106-362a-4541-bdc7-938ddb96a7a7", "sid": "dd59988d-7740-444e-8cda-f670b8ce28ba", "sourceId": 1, "runId": "e8e36035-dada-4f47-8123-59d42a74881c", "url": "/some/folder/test.txt", "mimeType": "text/plain",  "acls": [{"acl": "user@simsage.ai", "access": "R", "isUser": true}, {"acl": "some group", "access": "R", "isUser": false}], "title": "test document", "author": "Rock", "hash": "38957c50ca1330c74b702655fb1981bf", "data": ";base64,Um9iZXJ0IG9mdGVuIHdvcmtzIGluIHJlY3J1aXRtZW50Lgo=", "created": 1659695061000, "lastModified": 1659695061000, "metadata": {"name1": "value1", "name2": "value2"}, "size": 35}' https://your-simsage-instance.simsage.ai/api/crawler/external/document/upload
```
on success this POST will return the following JSON message.  The `error` field empty, and the `information` field containing `OK`.
```json
{"error":"","information":"OK","version":"7.7.3","time":1682673957648}
```

*CURL parameters explained*

| Parameter                           | Explanation                                                   |
|-------------------------------------|---------------------------------------------------------------|
| -X POST                             | we use the POST verb to upload information to the SimSage API |
| -H 'Content-Type: application/json' | the information POST-ed must be in JSON format                |
| -H 'API-Verion: 1'                  | the current SimSage API version is 1                          |
| -d '{ ... }'                        | the JSON data posted as a string                              |


*ACLs explained*

| Parameter | value           | description                                                                                                       |
|-----------|-----------------|-------------------------------------------------------------------------------------------------------------------|
| acl       | user@simsage.ai | the name of a group or the email address of a user                                                                |
| access    | R               | the level of access to this document for this user or group. R = Read / Search, W = Write, D = delete, M = modify |
| isUser    | true            | True if `acl` is an email address of a user, otherwise False if the ACL is the name of a group                    |

(Example group ACL: `{"acl": "Group Name", "access": "R", "isUser": false}`)
