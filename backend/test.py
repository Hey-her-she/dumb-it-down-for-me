from llm import get_all_explanations
from extractor import extract_text_from_pdf, chunk_text

# Test extractor with any PDF you have
# Use your resume since it's handy!
text = extract_text_from_pdf("Harshitha A.pdf")
chunked = chunk_text(text)

print("--- EXTRACTED TEXT PREVIEW ---")
print(chunked[:300])  # just peek at first 300 chars

print("\n--- NOW EXPLAINING ---")
results = get_all_explanations(chunked)
for level, explanation in results.items():
    print(f"\n--- {level.upper()} ---")
    print(explanation)