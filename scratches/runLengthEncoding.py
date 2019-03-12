class RunLengthEncoding:

    def encoding(self, text):
        if not text:
            return ""
        else:
            i = 0
            while i < len(text) and text[0] == text[i]:
                i += 1
            return str(i) + text[0] + self.encoding(text[i:])

    def decoding(self, text):
        if not text:
            return ""
        else:
            return int(text[0]) * text[1] + self.decoding(text[2:])

    def encode(self, text):
        return print(self.encoding(text))

    def decode(self, text):
        return print(self.decoding(text))



s = "BWWWWWBWWWW"

r = RunLengthEncoding()

r.encode(s)

encoded = r.encoding(s)

r.decode(encoded)

decoded = r.decoding(encoded)

print("Original text:", s)
print("Encoded text:", encoded)
print("Decoded text:", decoded)
