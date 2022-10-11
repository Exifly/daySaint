from flask_talisman import Talisman
from program import Program
from flask_cors import CORS
from flask import jsonify
from flask import Flask

flask = Flask(__name__)
flask.secret_key = 'pippo123'

# - SSL Configuration - #
SELF = "'self'"
talisman = Talisman(
    flask,
    content_security_policy={
        'default-src': SELF,
        'img-src': '*',
        'script-src': [
            SELF,
            'some.cdn.com',
        ],
        'style-src': [
            SELF,
            'another.cdn.com',
        ],
    },
    content_security_policy_nonce_in=['script-src'],
    feature_policy={
        'geolocation': '\'none\'',
    }
)

# - API DEFITINION - #
@flask.route("/api/v1/getSaint")
@talisman(
    frame_options='ALLOW-FROM',
    frame_options_allow_from='*',
)
def get_saint():
    program = Program()
    return jsonify({
        "message": program.day_saint(program.parse())
    }), 200

if __name__ == "__main__":
    flask.run(
        host='127.0.0.1',
        port='8080',
        debug=True
    )
