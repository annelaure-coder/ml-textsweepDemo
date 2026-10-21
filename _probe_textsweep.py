from textsweep import clean_text

samples = [
    "Check out https://example.com!!! 🎉 It's <b>GREAT</b>.",
    "HTML <b>OK</b> https://x.test",
    "Visit https://example.com NOW!!!",
]
for sample in samples:
    print(repr(sample), "->", repr(clean_text(sample)))
