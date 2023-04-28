# a simple SimSage API upload example

import os.path
import requests
import uuid
import hashlib
import base64

# what SimSage instance are we uploading to?
# get this set of parameters below from your platform - the values shown here aren't real
simsage_instance = 'your-simsage-instance.simsage.ai'
organisation_id = '9e8e81cf-408a-400c-9202-b1c2eb194797'
kb_id = '4f20f106-362a-4541-bdc7-938ddb96a7a7'
sid = 'dd59988d-7740-444e-8cda-f670b8ce28ba'
source_id = 1

# generate a random runId - only change this one once you've processed all files (for each run through a set of files)
run_id = uuid.uuid4()

# this will end up being the unique ID of this entity in SimSage
filename = 'sample-documents/840307.ppt'
# this is the mime-type for a PPT file
mime_type = 'application/vnd.ms-powerpoint'
# empty ACL list for now (i.e. this file is accessible to anyone using the search-engine (if indexing is enabled))
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

url = 'https://{}/api/crawler/external/document/upload'.format(simsage_instance)
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

headers = {'API-Version': '1', 'Content-type': 'application/json', 'Accept': 'application/json'}

# post to SimSage
result = requests.post(url, json=post_data, headers=headers)
# print the return result - do something with it
if result.status_code != 200:
    # a "SimSage configuration error." means your API numbers are wrong (e.g. source_id, organisation_id, kb_id or sid)
    print("upload error for '{}' : {}".format(filename, result.content.decode("ascii")))
else:
    print("upload successful")
