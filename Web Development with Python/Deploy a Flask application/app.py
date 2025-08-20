from flask import Flask, render_template, request

app = Flask(__name__)

# Sample Mad Libs story template
story_template = """
Once upon a time, there was a Python programmer named [name] who loved to code [adjective1] applications. 
One day, [name] decided to build a [noun] that could [verb] like a pro. 
[name] spent [number] hours coding and debugging, but finally, the [noun] was complete! 
[name] was so [adjective2] and couldn't wait to share it with the world. 
"""

word_types = ["name", "adjective1", "noun", "verb", "number", "adjective2"]

@app.route("/", methods=["GET", "POST"])
def mad_libs():
    if request.method == "POST":
        # Get user input for each word type
        words = [request.form.get(f"word_{i}") for i in range(len(word_types))]
        # Fill in the story template with the user's words
        story = story_template
        for i, word in enumerate(words):
            story = story.replace(f"[{word_types[i]}]", word)  # Replace all occurrences
        return render_template("story.html", story=story)
    else:
        return render_template("form.html", word_types=word_types)

if __name__ == "__main__":
    app.run(debug=True)