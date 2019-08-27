word_definitions = dict()
#"cat", Dagney, website, pen, iPhone

word_definitions["Cat"] = "Queen of Pets"
word_definitions["Dagney"] = "The Taggart with the right values"
word_definitions["Website"] = "something Melanie can make in a matter of days"
word_definitions["Pen"] = "The tool by which we compose our philosophy"
word_definitions["iPhone"] = "doorway to the community"

for (a, b) in word_definitions.items():
    print(f"The definition of '{a}' is '{b}'")

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for (k, v) in idioms.items():
    space = " "
    sentences = space.join(v)
    print(f"The definition of '{k}' is '{sentences}'")