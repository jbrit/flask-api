from flask import Blueprint
from flask_apispec import FlaskApiSpec
from flask_restful import Api

from resources.conference import Conference, Conferences
from resources.people import  Speaker, Speakers, Participant, Participants
from resources.talk import Talk, Talks

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

# API routes -- start
api.add_resource(Talk, "/conferences/<int:conference_id>/talks/<int:talk_id>")
api.add_resource(Talks, "/conferences/<int:conference_id>/talks")

api.add_resource(Speaker, "/conferences/<int:conference_id>/talks/<int:talk_id>/speakers/<int:person_id>")
api.add_resource(Speakers, "/conferences/<int:conference_id>/talks/<int:talk_id>/speakers")

api.add_resource(Participant, "/conferences/<int:conference_id>/talks/<int:talk_id>/participants/<int:person_id>")
api.add_resource(Participants, "/conferences/<int:conference_id>/talks/<int:talk_id>/participants")

api.add_resource(Conference, "/conferences/<int:conference_id>")
api.add_resource(Conferences, "/conferences")
# API routes -- end


docs = FlaskApiSpec()

# API docs -- start
docs.register(Talk, blueprint="api")
docs.register(Talks, blueprint="api")
docs.register(Speaker, blueprint="api")
docs.register(Speakers, blueprint="api")
docs.register(Participant, blueprint="api")
docs.register(Participants, blueprint="api")
docs.register(Conference, blueprint="api")
docs.register(Conferences, blueprint="api")
# API docs -- end
