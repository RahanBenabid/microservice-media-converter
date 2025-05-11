#!/usr/bin/env python3

import pika, json

"""
* this function uploads the file into mongodb db using gridFS
* then we need to put a message into our rabbit mq queue, so that the downstream service, when it's pulled from the queue, can process the upload, by pulling it from mongodb
* this enables an asynchronous communication flow between the gateway service and the one that processes the video
* the async makes it so that we the gateway service doesn't need to wait for an internal service to finish processing the video to be able to send a response to the client
"""

def upload(f, fs, channel, access):
  try:
    # get the file id after putting it
    fid = fs.put(f)
  except Exception as err:
    print(err)
    return "Internal server error", 500
  
  message = {
    "video_fid": str(fid),
    "mp3_fid": None,
    "username": access["username"],
  }
  
  # try to put the message on the queue
  try:
    channel.basic_publish(
      exhange="",
      routing_key="video",
      body=json.dumps(message),
      properties=pika.BasicProperties(
        # make sure the messages are persistent in case of a pod crash or restart
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
      ),
    )
  except:
    fs.delete(fid)
    return "Internal server error", 500
    