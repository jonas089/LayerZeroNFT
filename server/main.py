from flask import Flask, request, jsonify, render_template

#########################
#   BACKEND NFT         #
#########################

app = Flask(__name__)
def openSeaMetadata(description, url, image, name):
    metadata = {
      "description": description,
      "external_url": url,
      "image": image,
      "name": name,
      "attributes": [], # no attributes set.
    }
    return metadata

# app route default
@app.route('/')
def uri():
    id = request.args.get("id")
    if id == None:
        return "Error 0: Missing ID"
    metadata = openSeaMetadata(
        "some test nft.",
        "",
        "",
        "TEST"
    )
    return jsonify(metadata)

@app.route('/demo')
def demo():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
