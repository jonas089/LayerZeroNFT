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
        "https://previews.dropbox.com/p/thumb/ABqP3oVjyDt_Sa8ieT-i8w5Zgqlith2UNFWPRs2rE6qurwwWUBc72mrSiRGROuVw1OnjKH6RAO9-jal-FM6xMXE0uEtbFFhXry2FQaXjgqJ8MvPONYtCYMN0BFCU-Ffq6bGVnjp0VKQ1m_nCs1eMXHDWOEDiixBs_iQxduuFyHkJuzIxJqGQrn2EYnYNfxYnChZ8Cfa12dxBuOYzZMiZYTV7KoN250C73Z9Ib_M0QiV-zxm-a80r9-taZDDpymxMWZ-uxNUqQDR9kWJkgaiMqjqtOEgO91JbBaY1q6IK0K76r_RNdQ0cHqcELZgZKnUiUmbrQJe4lt4BSfucuM7XWCflH2udBtWmflP83XpyfntgWw-5qUSiXXOA4z8C_kHFvlg/p.jpeg",
        "https://previews.dropbox.com/p/thumb/ABqP3oVjyDt_Sa8ieT-i8w5Zgqlith2UNFWPRs2rE6qurwwWUBc72mrSiRGROuVw1OnjKH6RAO9-jal-FM6xMXE0uEtbFFhXry2FQaXjgqJ8MvPONYtCYMN0BFCU-Ffq6bGVnjp0VKQ1m_nCs1eMXHDWOEDiixBs_iQxduuFyHkJuzIxJqGQrn2EYnYNfxYnChZ8Cfa12dxBuOYzZMiZYTV7KoN250C73Z9Ib_M0QiV-zxm-a80r9-taZDDpymxMWZ-uxNUqQDR9kWJkgaiMqjqtOEgO91JbBaY1q6IK0K76r_RNdQ0cHqcELZgZKnUiUmbrQJe4lt4BSfucuM7XWCflH2udBtWmflP83XpyfntgWw-5qUSiXXOA4z8C_kHFvlg/p.jpeg",
        "TEST"
    )
    return jsonify(metadata)

@app.route('/demo')
def demo():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
