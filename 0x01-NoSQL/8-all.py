#!/usr/bin/env python3
"""This function lists all the documents in a collection"""

def list_all(mongo_collection):
    documents = mongo_collection.find()
    document_list = list(documents)

    if len(document_list) == 0:
        return []
    return document_list
