# a simple SimSage API upload example

import os
import requests
import uuid
import hashlib
import base64

# import all the mime-types: 'file-extension' -> 'mime-type'
from mimetypemap import mime_type_map

# what SimSage instance are we uploading to?
# get this set of parameters below from your platform - the values shown here aren't real
server_instance = 'my-simsage-instance.simsage.ai'
organisation_id = '9e8e81cf-408a-400c-9202-b1c2eb194797'
kb_id = '4f20f106-362a-4541-bdc7-938ddb96a7a7'
sid = 'dd59988d-7740-444e-8cda-f670b8ce28ba'
source_id = 1

# SimSage url and headers, always the same
headers = {'API-Version': '1', 'Content-type': 'application/json', 'Accept': 'application/json'}
url = 'https://{}/api/crawler/external/document/upload'.format(server_instance)

# generate a random runId - only change this one once you've processed all files (for each run through a set of files)
run_id = uuid.uuid4()

# upload all files in the sample-documents folder to SimSage
dir_path = 'sample-documents'
for path in os.listdir(dir_path):
    # this will end up being the unique ID of this entity in SimSage
    filename = os.path.join(dir_path, path)
    file_extension = os.path.splitext(filename)
    # no file-extension?  ignore the file
    if len(file_extension) != 2:
        continue
    # get the extension part, and ignore the . part of the filename extension
    file_extension = file_extension[1][1:]
    if os.path.isfile(filename) and len(file_extension) > 1:
        # get the mime-type of this file from its file-extension
        if file_extension in mime_type_map:
            mime_type = mime_type_map[file_extension]
        else:
            raise ValueError('unknown mime-type for file {}'.format(filename))

        # empty ACL list for now (i.e. this file is accessible to anyone using
        # the search-engine (if indexing is enabled))
        acls = []

        # get created and last-modified for this file
        file_stats = os.stat(filename)
        last_modified_time = int(file_stats.st_mtime * 1000)
        created_time = int(file_stats.st_ctime * 1000)

        # read the file's binary
        with open(filename, mode='rb') as file:
            file_content = file.read()

        # calculate the file's md5 hash
        file_size = len(file_content)
        file_md5 = hashlib.md5(file_content).hexdigest()

        # encode the file-content as base-64
        encoded_file = base64.b64encode(file_content).decode('ascii')

        post_data = {"organisationId": organisation_id,
                     "kbId": kb_id,
                     "sid": sid,
                     "sourceId": source_id,
                     "runId": str(run_id),
                     "url": filename,
                     "mimeType": mime_type,
                     "acls": acls,
                     "hash": file_md5,
                     "data": ";base64,{}".format(encoded_file),
                     "created": created_time,
                     "lastModified": last_modified_time,
                     "size": file_size}

        # post to SimSage
        result = requests.post(url, json=post_data, headers=headers)
        # print the return result - do something with it
        if result.status_code != 200:
            # a "SimSage configuration error." means your API numbers are wrong
            # (e.g. source_id, organisation_id, kb_id or sid)
            print("upload error for '{}' : {}".format(filename, result.content.decode("ascii")))
        else:
            print("upload successful for '{}'".format(filename))
