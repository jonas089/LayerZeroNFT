from flask import Flask, request, jsonify

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
        "https://previews.dropbox.com/p/thumb/ABoua9EcWINqUTRnhSq-hBpgEih1-GTHAIAGkocI0idsI4Efwhzirf-5zaWXt0cOqBPJI2bWQ9cH7ewYJF75KKz8EnBnzFUPOKyn_ToWcDiNQ3jDFB30TVDREa5yRpha09b1OeWMk1ZUUzS1AuDdNbopOSGQ3DrrOVTKLbGDIp0e6ROHOMrYXI1gPrY5wnYuzB_-FQi780GxcovunlUH5No_ZQ2rUm9K_u7bF6uWwibb4NKoRUSaDbh7UoY-_dbniqk1lEGIk9MrmH9WnSwkI8qX7r9i5kn56mWYmPINgFxmxMv5BBWgOYjIl_MoalPMLk_1mbYcklgrsw3SgxLuCjlKzORLs6--9coDI75e49rml-sozpKijDuEeBZglpTuVfA/p.jpeg",
        "https://previews.dropbox.com/p/thumb/ABoua9EcWINqUTRnhSq-hBpgEih1-GTHAIAGkocI0idsI4Efwhzirf-5zaWXt0cOqBPJI2bWQ9cH7ewYJF75KKz8EnBnzFUPOKyn_ToWcDiNQ3jDFB30TVDREa5yRpha09b1OeWMk1ZUUzS1AuDdNbopOSGQ3DrrOVTKLbGDIp0e6ROHOMrYXI1gPrY5wnYuzB_-FQi780GxcovunlUH5No_ZQ2rUm9K_u7bF6uWwibb4NKoRUSaDbh7UoY-_dbniqk1lEGIk9MrmH9WnSwkI8qX7r9i5kn56mWYmPINgFxmxMv5BBWgOYjIl_MoalPMLk_1mbYcklgrsw3SgxLuCjlKzORLs6--9coDI75e49rml-sozpKijDuEeBZglpTuVfA/p.jpeg",
        "TEST"
    )
    return jsonify(metadata)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
