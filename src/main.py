from program import Program
from flask import jsonify
from flask import Flask

flask = Flask(__name__)

# - API DEFITINION - #
@flask.route("/api/v1/getSaint")
def get_saint():
    program = Program()
    return jsonify({
        "message": program.day_saint(program.parse())
    }), 200

if __name__ == "__main__":
    flask.run()
