dogs_schema_random_more_1 = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "message": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                },
                {
                    "type": "string"
                }
            ]
        },
        "status": {
            "type": "string"
        }
    },
    "required": [
        "message",
        "status"
    ]
}


dogs_schema_random_1 = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        },
        "status": {
            "type": "string"
        }
    },
    "required": [
        "message",
        "status"
    ]
}


brewery_schema_for_single = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "brewery_type": {
      "type": "string"
    },
    "address_1": {
      "type": ["string", "null"]
    },
    "address_2": {
      "type": "null"
    },
    "address_3": {
      "type": "null"
    },
    "city": {
      "type": "string"
    },
    "state_province": {
      "type": "string"
    },
    "postal_code": {
      "type": "string"
    },
    "country": {
      "type": "string"
    },
    "longitude": {
      "type": ["string", "null"]
    },
    "latitude": {
      "type": ["string", "null"]
    },
    "phone": {
      "type": "string"
    },
    "website_url": {
      "type": ["string", "null"]
    },
    "state": {
      "type": "string"
    },
    "street": {
      "type": ["string", "null"]
    }
  },
  "required": [
    "id",
    "name",
    "brewery_type",
    "address_1",
    "address_2",
    "address_3",
    "city",
    "state_province",
    "postal_code",
    "country",
    "longitude",
    "latitude",
    "phone",
    "website_url",
    "state",
    "street"
  ]
}


brewery_schema_for_meta = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "total": {
      "type": "string"
    },
    "page": {
      "type": "string"
    },
    "per_page": {
      "type": "string"
    }
  },
  "required": [
    "total",
    "page",
    "per_page"
  ]
}


jsonplhold_schema_for_1_post = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "userId": {
      "type": "integer"
    },
    "id": {
      "type": "integer"
    },
    "title": {
      "type": "string"
    },
    "body": {
      "type": "string"
    }
  },
  "required": [
    "userId",
    "id",
    "title",
    "body"
  ]
}


jsonplhold_schema_for_post_query = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "title": {
      "type": "string"
    },
    "body": {
      "type": "string"
    },
    "userId": {
      "type": ["integer", "string"]
    }
  },
  "required": [
    "id",
    "title",
    "body",
    "userId"
  ]
}


jsonplhold_schema_for_patch_query = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "userId": {
      "type": "integer"
    },
    "id": {
      "type": "integer"
    },
    "title": {
      "type": "string"
    },
    "completed": {
      "type": "boolean"
    }
  },
  "required": [
    "userId",
    "id",
    "title",
    "completed"
  ]
}
